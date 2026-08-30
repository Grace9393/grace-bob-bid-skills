# IBM Bid Library FTS5 Query Reference

Use this reference for `$SKILL_DIR/../ibm-bid-library/docs.sqlite`.

## Database profile

- DB path: `$SKILL_DIR/../ibm-bid-library/docs.sqlite`
- FTS table: `entries_fts`
- Tokenizer: `porter unicode61`
- Columns:
  - `id` (0, UNINDEXED)
  - `question` (1)
  - `answer` (2)
  - `stack` (3)
  - `category` (4)
  - `sub_category` (5)
  - `tags` (6)
  - `language` (7, UNINDEXED)
  - `library_url` (8, UNINDEXED)
  - `source_path` (9, UNINDEXED)
  - `has_images` (10, UNINDEXED)
  - `images_text` (11)
  - `images` (12, UNINDEXED)
  - `score` (13, UNINDEXED)
  - `updated_at` (14, UNINDEXED)

## Runtime and preflight (run first)

```bash
DB_PATH="$SKILL_DIR/../ibm-bid-library/docs.sqlite"
uv run $SKILL_DIR/../ibm-bid-library/scripts/info.py "$DB_PATH"
```

Search options (sqlite-skill):
- `--offset <n>` pagination
- `--show-status` or `--json-pretty` for query status/warnings
- `--show-scores` or `--min-score <0-1>` for normalized scores
- `--snippet`, `--snippet-length <n>`, `--snippet-column <col>`
- `--query-timeout-ms <ms>`

Get options:
- `--preview-length <n>` (>= 1)

Exit codes:
- `2` database path errors (also invalid `--preview-length`)
- `3` invalid/empty query or timeout
- `4` no results / not found

- Use Python runtime scripts for all database access in this skill.
- Do not use direct `sqlite3` shell/HEREDOC patterns here.

## MATCH and NEAR quick rules

- Phrase search: `'"exact phrase"'`
- Boolean logic: `AND`, `OR`, `NOT` (space-separated terms are implicit `AND`)
- Prefix search: `secur*`
- Column-scoped search: `category:Security` or `stack:"Salesforce"`
- Multi-column scope: `'{question answer tags}:integration'`
- Proximity: `NEAR(term1 term2, 5)` (FTS5 does not support `NEAR/1 5` range syntax)

## Ranking quick rules

- Default runtime search returns BM25 ranked matches; keep query structure consistent when comparing runs.

## Constraints and caveats

- Use `MATCH` for full-text conditions (not `LIKE`/`=` for relevance search).
- Build MATCH expressions as constants or bound parameters.
- Applying many non-FTS filters can reduce FTS performance.
- Very long single terms can fail (SQLite FTS term length limits apply).

## Notes

- Use `question`, `answer`, `tags`, and `images_text` for relevance search.
- `library_url` and `source_path` are for output/citation and should not be used inside MATCH.
