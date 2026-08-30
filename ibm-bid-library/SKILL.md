---
name: ibm-bid-library
description: Access IBM's comprehensive bid library containing 3000+ historical bid responses, technical documentation, policy documents, financial statements, and delivery artifacts. Use when Claude needs to (1) Find examples of how IBM has answered specific tender questions, (2) Research IBM's technical approaches and methodologies, (3) Access policy documents, financial information, or corporate materials, (4) Find reusable content for proposals including diagrams, architectures, and technical solutions, (5) Search by category (AI, Security, DevOps, etc.) or tags to find relevant materials, (6) Review IBM's past answers to inform new responses.
---

# IBM Bid Library

## PREREQUISITES

Use the self-contained Python runtime scripts from `$SKILL_DIR/scripts/` for all database access.
Run them with `uv run`, which reads each script's inline PEP 723 metadata and provisions
an isolated runtime automatically.

Inspect schema/metadata:

```bash
uv run $SKILL_DIR/scripts/info.py $SKILL_DIR/docs.sqlite
```

Search:

```bash
uv run $SKILL_DIR/scripts/search.py <db_path> "<query>"
uv run $SKILL_DIR/scripts/search.py <db_path> "<query>" --json
```

Search options (sqlite-skill) - tighten results first:
- `--offset <n>` pagination
- `--show-status` or `--json-pretty` for query status/warnings
- `--show-scores` or `--min-score <0-1>` for normalized scores
- `--snippet`, `--snippet-length <n>`, `--snippet-column <col>`
- `--query-timeout-ms <ms>`
- `--limit 10`

Get document:

```bash
uv run $SKILL_DIR/scripts/get.py <db_path> <doc_id>
uv run $SKILL_DIR/scripts/get.py <db_path> <doc_id> --json
uv run $SKILL_DIR/scripts/get.py <db_path> <doc_id> --preview-length 1000
```

Get options:
- `--preview-length <n>` (>= 1)

Exit codes:
- `2` database path errors
- `3` invalid/empty query or timeout (also invalid preview length)
- `4` no results / not found

Do not use shell HEREDOC SQL patterns in this skill (they are not reliable on Windows).

## Context Management

ALWAYS write search results to `./tmp/ibm-bid-library.md` immediately after retrieval. This prevents context saturation when chaining with other skills. Only copy final deliverables to `./outputs` at completion.

## Quick Reference

| Item           | Value                                    |
| -------------- | ---------------------------------------- |
| Database       | `$SKILL_DIR/docs.sqlite`     |
| FTS5 Table     | `entries_fts`                            |
| Documents      | `$SKILL_DIR/docs/` (images)  |
| Total Entries  | 3302                                     |
| Categories     | Technical Solutions, Documentation, Delivery, AI, Security, Architecture, Agile, Financial, G-Cloud 15 Service Offerings, IBM Strategy and Capabilities 2026 |

## Overview

**Total Entries**: 3302 IBM bid entries stored in a SQLite database (`docs.sqlite`) with full-text search (FTS5).

All bid content (questions, answers, metadata) is stored in the database for fast, efficient searching. Use only the Python runtime scripts for queries and retrieval.

Original Word documents in `docs/` are only needed when accessing embedded images or diagrams.

## Search Workflow

### Step 1: Expand Query Terms (Default)

**Apply simplified query expansion before searching to improve recall:**

1. **Generate synonym variants** (5-7 alternatives for each core concept):
   - "lead scoring" → add "prospect evaluation", "lead ranking", "contact qualification"
   - "cloud migration" → add "cloud transformation", "cloud adoption", "cloud modernization"
   - "customer portal" → add "self-service portal", "client portal", "customer hub"

2. **Add phrasal alternatives** (rephrase using common variations):
   - "how to implement X" → also search "X implementation", "deploying X", "X rollout"
   - "benefits of X" → also search "X advantages", "X outcomes", "X results"
   - Technical terms → add colloquial equivalents users actually type

3. **Construct OR-joined FTS5 query** (combine variants for better recall):
   ```bash
   # Original query: "lead scoring healthcare"
   # Expanded query: "(lead OR prospect OR contact) AND (scoring OR ranking OR evaluation OR qualification) AND (healthcare OR medical OR clinical OR hospital)"
   ```

**This 3-step expansion takes ~10 seconds and significantly improves search results.**

### Step 2: Execute Search

Use only the Python scripts in `$SKILL_DIR/scripts/`:

- `info.py` (schema/metadata checks)
- `search.py` (FTS search)
- `get.py` (retrieve full record by ID)

```bash
DB_PATH="$SKILL_DIR/docs.sqlite"

# Confirm schema/table availability
uv run $SKILL_DIR/scripts/info.py "$DB_PATH"

# Expanded keyword search
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(cloud OR platform) AND (migration OR transformation OR adoption)" --json

# Multi-concept expansion with category terms
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(security OR secure OR protection) AND (assessment OR audit OR review) AND (technical OR architecture)" --json

# Tags/DevOps style query
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(security AND devops) OR (pipeline AND controls)" --json

# Get full entry by ID
uv run $SKILL_DIR/scripts/get.py "$DB_PATH" 4640016 --json
```

### Step 3: Evaluate Results & Escalate if Needed

**If search results are poor (<5 relevant hits or low quality):**

Use `$query-expansion-strategy` for comprehensive 10-category expansion:
- Generates 5-10 sub-questions across definition/process/rationale/comparison/tooling/metrics/mistakes/trends/personas/use-cases
- Creates entity relationship maps for related concepts
- Produces optimized FTS5 MATCH expressions for exhaustive coverage
- Best for: Ambiguous queries, multi-faceted topics, comprehensive coverage requirements

**If results are good (5+ relevant hits):**
- Filter by metadata terms in query (category, sub_category, tags, score context)
- Prioritize high-quality documents
- Review entries with diagrams if visual context needed
- Retrieve full entry content by ID

## Citation Requirements

**Always cite sources when presenting bid library content.** Every piece of content from this library must include a reference to enable traceability and verification.

### Step 4: Retrieve Entry by ID

Use `get.py` from `$SKILL_DIR/scripts/`:

```bash
DB_PATH="$SKILL_DIR/docs.sqlite"

# Get complete story by ID
uv run $SKILL_DIR/scripts/get.py "$DB_PATH" 42

# JSON output for structured processing
uv run $SKILL_DIR/scripts/get.py "$DB_PATH" 42 --json
```

### Required Citation Format

When presenting results, always include:

- **Document ID** - The entry ID from the database
- **Document title** - The `question` field
- **Category** - The `category` field
- **Source path** - The `source_path` field when it points to a useful original source. Legacy entries often map to `docs/{id}.docx`; custom corpus entries may report `source.md` and should instead be traced through `skills/ibm-bid-library/src/custom-documents.yaml`.

### Example Output Format

```text
**Source: Bid Library Entry 4640016**
Title: "Cloud Migration Approach for Enterprise Clients"
Category: Technical Solutions
Document: docs/4640016.docx

[Content from the entry...]
```

## Working with Content

### Workflow

1. **Search** - Use `search.py` to find relevant entries by keyword, category, or tags
2. **Retrieve** - Use `get.py` with the ID from search results
3. **Cite** - Always include entry ID, title (question), category, and source path or custom-manifest trace
4. **Access Images** - Read .docx only when image context is required
5. **Adapt** - Do not copy verbatim; update dates, verify facts, follow `ibm-bid-writer` guidelines

### Accessing Images

If an entry references diagrams, use the `docx` skill to read: `$SKILL_DIR/docs/{id}.docx`

## Search Strategies

For advanced filtering by category, technology stack, quality score, tags, or content type, see [references/search-strategies.md](references/search-strategies.md).

## Integration with Other Skills

**Typical Workflow**:

1. `ibm-bid-requirements-analysis` - Understand requirements
2. `ibm-bid-library` - Find relevant past answers (this skill)
3. `ibm-bid-strategy-and-capabilities-2026` - Current positioning
4. `ibm-bid-customer-stories` - Recent proof points
5. `ibm-bid-writer` - Draft response
6. `ibm-bid-answer-evaluator` - Assess quality

## Quality Checklist

When presenting bid library content, ensure you:
- ✓ Used `uv run $SKILL_DIR/scripts/search.py` and `get.py` for all database access
- ✓ Selected entries that genuinely match the user's criteria
- ✓ Avoided entry duplication
- ✓ Included entry ID, question/title, and category context
- ✓ Checked image availability before accessing .docx files
- ✓ Provided source path or custom-manifest trace for verification
- ✓ Explained relevance to the user's specific needs
- ✓ Used British English spelling and professional tone
- ✓ Avoided fabricating or embellishing details beyond what's in the database

## Reference Files

- **Category definitions**: See [references/categories.md](references/categories.md)
- **Search strategies**: See [references/search-strategies.md](references/search-strategies.md)
- **FTS5 query reference**: See [references/sqlite-fts5-query.md](references/sqlite-fts5-query.md)

## Important Notes

- **Always use Python runtime scripts** - Use `uv run $SKILL_DIR/scripts/search.py` and `get.py` for all searches/retrieval
- **Content may be truncated** - Answers over 32KB may be truncated
- **Verify currency** - Historical content may need updates
- **Respect confidentiality** - Some entries may contain sensitive information
