# Search Strategies

Advanced search patterns for the IBM Bid Library using Python runtime scripts only.

## Runtime-first approach

Always use:

```bash
DB_PATH="$SKILL_DIR/docs.sqlite"
uv run $SKILL_DIR/scripts/info.py "$DB_PATH"
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" "<fts_query>" --json
uv run $SKILL_DIR/scripts/get.py "$DB_PATH" <id> --json
```

Search options (sqlite-skill) - tighten results first:
- `--offset <n>` pagination
- `--show-status` or `--json-pretty` for query status/warnings
- `--show-scores` or `--min-score <0-1>` for normalized scores
- `--snippet`, `--snippet-length <n>`, `--snippet-column <col>`
- `--query-timeout-ms <ms>`
- `--limit 10`

Get options:
- `--preview-length <n>` (>= 1)

Exit codes:
- `2` database path errors
- `3` invalid/empty query or timeout (also invalid preview length)
- `4` no results / not found

Do not use direct `sqlite3` or HEREDOC SQL in this skill.

## Coverage loop (default)

Run these passes in order to avoid shallow recall:

1. **Core intent pass** - direct requirement terms.
2. **Synonym pass** - equivalent technical and business phrasing.
3. **Adjacent pass** - nearby concepts (governance, assurance, delivery model, tooling).

Keep each pass as a separate query. Merge and deduplicate IDs before retrieval.

## Strategy patterns

### By category

Available categories include Technical Solutions, Documentation, Delivery, Financial Information, AI, Security, Architecture, and Agile.

```bash
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "category:\"Technical Solutions\" AND (integration OR architecture)" --json
```

### By technology stack

```bash
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "stack:(Kubernetes OR OpenShift OR container*) AND (security OR governance)" --json
```

### By tags

```bash
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "tags:(DevOps AND \"CI CD\") AND (pipeline OR controls)" --json
```

### By content type (diagrams/images)

`has_images` is metadata, so use a two-pass workflow:

1. Search with FTS terms likely to return diagram content.
2. In returned JSON, shortlist entries where `has_images=1`.
3. Retrieve shortlisted IDs with `get.py`.

```bash
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(architecture OR reference OR topology) AND (diagram OR visual OR image)" --json
```

### By quality score

`score` is metadata, so use a two-pass workflow:

1. Search by relevance using FTS query terms.
2. From JSON output, sort/filter by `score` (for example `>= 80`) where present.
3. Retrieve top IDs with `get.py`.

## Result triage rubric

For the top 10-15 hits, score each quickly:

- **Relevance (0-3)**: direct match to requirement language and scope.
- **Transferability (0-3)**: reusable approach without major rewriting.
- **Evidence strength (0-2)**: quantified outcomes or concrete delivery detail.
- **Currency (0-2)**: favor newer `updated_at` entries when tie-breaking.

Prioritize entries scoring 7+.

## Failure recovery playbook

If fewer than 5 strong hits:

1. Split query into two narrower intent queries instead of one broad query.
2. Replace abstract terms with concrete nouns (platforms, controls, methods).
3. Add/removes quoted phrases to adjust strictness.
4. Run one query focused on `question` framing and one on delivery/outcomes.
5. Escalate to `$query-expansion-strategy` for comprehensive decomposition.

## Anti-patterns

- **Too broad**: `cloud AND security` -> use intent + context + outcome terms.
- **Too constrained**: many quoted phrases in one query -> relax to one phrase max.
- **Metadata-only thinking**: trying to force `score`/`has_images` in MATCH -> use post-filtering.
- **Single-shot search**: one query only -> always use the 3-pass coverage loop.

## JSON post-filter examples

Use runtime `--json` output and post-filter locally.

```bash
# Top scored entries (where score exists)
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(integration OR migration) AND (security OR assurance)" --json \
  | jq 'map(select(.score != null)) | sort_by(-.score) | .[:10]'
```

```bash
# Entries that include images/diagrams
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(reference OR architecture) AND (diagram OR topology)" --json \
  | jq 'map(select(.has_images == 1))'
```

```bash
# Prefer most recently updated among relevant hits
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(delivery OR methodology) AND (public sector OR government)" --json \
  | jq 'sort_by(.updated_at // "") | reverse | .[:10]'
```

## Skill-specific search strategies

### For ibm-bid-win-themes

Focus on high-scoring historical content that demonstrates differentiators:

```bash
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(differentiator* OR value OR outcome*) AND (public sector OR transformation)" --json
```

Then post-filter results by `score` and prioritize strong evidence.

### For ibm-bid-writer

Combine category + stack + tags to mirror requirement language:

```bash
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "category:\"Technical Solutions\" AND stack:Salesforce AND tags:(integration OR security)" --json
```

### For ibm-bid-answer-evaluator

Find structurally similar answers and prioritize scored entries:

```bash
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(methodology OR approach) AND (deliver* OR govern* OR assurance)" --json
```

Then compare shortlisted entries by depth, structure, and score.

### For ibm-bid-requirements-analysis

Search requirement language directly from the tender text:

```bash
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(requirement* OR must OR shall) AND (security OR integration OR migration)" --json
```

Retrieve top IDs for detailed extraction and citation.
