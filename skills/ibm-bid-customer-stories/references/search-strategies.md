# Search Strategies

Advanced search patterns for `ibm-bid-customer-stories` using Python runtime scripts only.

## Runtime-first approach

```bash
DB_PATH="$SKILL_DIR/stories.sqlite"
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

Run these passes in order:

1. **Challenge pass** - client pain point/problem statement terms.
2. **Capability pass** - cloud/product and implementation approach terms.
3. **Outcome pass** - measurable results (cost, speed, CSAT, productivity).

Merge and deduplicate IDs before retrieval.

## Strategy patterns

```bash
# Industry + challenge
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(healthcare OR nhs OR clinical) AND (access OR triage OR contact center)" --json
```

```bash
# Cloud + outcomes
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(\"service cloud\" OR agentforce OR \"sales cloud\") AND (outcomes OR productivity OR efficiency)" --json
```

```bash
# Transformation proof points
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(modernization OR transformation OR migration) AND (time-to-value OR roi OR savings)" --json
```

## Result triage rubric

Review top 10-15 and prioritize:

- **Client similarity (0-3)**: industry/regulatory context fit.
- **Solution similarity (0-3)**: comparable cloud mix and delivery approach.
- **Outcome strength (0-2)**: clear quantified benefits.
- **Story quality (0-2)**: concise challenge-solution-outcome narrative.

Prioritize entries scoring 7+.

## Failure recovery playbook

If fewer than 5 strong hits:

1. Swap industry term to adjacent sectors (for example healthcare <-> public sector).
2. Split query into challenge-only and outcome-only variants.
3. Replace strict product names with broader terms (`contact center`, `crm`, `self-service`).
4. Add synonyms for outcomes (`savings`, `efficiency`, `faster`, `reduction`).
5. Escalate to `$query-expansion-strategy`.

## Anti-patterns

- **Too broad**: `salesforce transformation`.
- **Overly vendor-specific**: no domain/problem terms.
- **Outcome-free search**: retrieving stories without measurable value.
- **Single pass**: one query and immediate write-up.

## JSON post-filter examples

```bash
# Prefer stories with explicit outcomes text
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(agentforce OR service cloud) AND (support OR service)" --json \
  | jq 'map(select((.outcomes // "") != "")) | .[:10]'
```

```bash
# Focus on healthcare and government contexts
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(automation OR modernization) AND (service OR experience)" --json \
  | jq 'map(select((.industry // "") | test("health|government|public"; "i")))'
```
