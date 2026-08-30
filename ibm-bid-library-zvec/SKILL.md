---
name: ibm-bid-library-zvec
description: Access IBM's comprehensive bid library containing 3000+ historical bid responses, technical documentation, policy documents, financial statements, and delivery artifacts. Use when Claude needs to (1) Find examples of how IBM has answered specific tender questions, (2) Research IBM's technical approaches and methodologies, (3) Access policy documents, financial information, or corporate materials, (4) Find reusable content for proposals including diagrams, architectures, and technical solutions, (5) Search by category (AI, Security, DevOps, etc.) or tags to find relevant materials, (6) Review IBM's past answers to inform new responses.
---

# IBM Bid Library

## PREREQUISITES

Use the cross-platform Python runtime scripts from `$SKILL_DIR/scripts/` for all database access.
Do not call `zvec_hybrid` binaries directly in this skill; use the Python wrappers only.
Run them with `uv run`, which reads each script's inline PEP 723 metadata and
provisions an isolated runtime automatically.

Inspect schema/metadata:

```bash
uv run $SKILL_DIR/scripts/info.py
```

Search:

```bash
uv run $SKILL_DIR/scripts/search.py "<query>"
uv run $SKILL_DIR/scripts/search.py "<query>" --json
```

Search options:
- `--offset <n>` pagination
- `--limit <n>` (e.g. `--limit 10`)
- `--show-scores` or `--min-score <0-1>`
- `--reranker rrf|weighted` (default: rrf)
- `--candidate-topk <n>` number of candidates before reranking
- `--post-reranker local|api`
- `--json` for structured output

Get document:

```bash
uv run $SKILL_DIR/scripts/get.py <doc_id>
uv run $SKILL_DIR/scripts/get.py <doc_id> --json
uv run $SKILL_DIR/scripts/get.py <doc_id> --preview-length 1000
```

Get options:
- `--preview-length <n>` (>= 1)

Exit codes:
- `2` database path errors (also invalid `--preview-length`)
- `3` invalid/empty query or timeout
- `4` no results / not found

Do not use shell HEREDOC SQL patterns in this skill (they are not reliable on Windows).

Optional model prefetch for the local cross-encoder reranker:

```bash
uv run $SKILL_DIR/scripts/cache_models.py --force-download
```

## Context Management

ALWAYS write search results to `./tmp/ibm-bid-library-zvec.md` immediately after retrieval. This prevents context saturation when chaining with other skills. Only copy final deliverables to `./outputs` at completion.

## Quick Reference

| Item           | Value                                    |
| -------------- | ---------------------------------------- |
| Vector Store   | `$SKILL_DIR/references/bid_library_zvec` |
| Backend        | `zvec-hybrid` (via Python wrappers)      |
| Documents      | `$SKILL_DIR/docs/` (images)  |
| Total Entries  | 2994                                     |
| Categories     | Technical Solutions, Documentation, Delivery, AI, Security, Architecture, Agile, Financial |

## Overview

**Total Entries**: 2994 IBM bid entries indexed in a pre-built zvec store (`references/bid_library_zvec/`) queried through `zvec_hybrid`.

All bid content (questions, answers, metadata) is accessible via the zvec store for semantic and keyword search. Use only the Python runtime scripts (which call `zvec_hybrid`) for queries and retrieval.

Original Word documents in `docs/` are only needed when accessing embedded images or diagrams.

## Search Workflow

### Step 1: Phrase Your Query

The zvec backend performs semantic matching, so plain keyword phrases work well without boolean expansion. Use natural language or short keyword phrases:

- "cloud migration approach" (not `(cloud OR platform) AND (migration OR transformation)`)
- "security architecture review"
- "agile delivery methodology"

For broad topics, try 2-3 short focused queries rather than one complex expression.

### Step 2: Execute Search

Use only the Python scripts in `$SKILL_DIR/scripts/`:

- `info.py` (store metadata/stats checks via `zvec_hybrid`)
- `search.py` (semantic search via `zvec_hybrid`)
- `get.py` (retrieve full record by ID via `zvec_hybrid`)
- `cache_models.py` (optional local reranker model prefetch)

```bash
# Confirm metadata
uv run $SKILL_DIR/scripts/info.py

# Keyword search (zvec handles semantic matching)
uv run $SKILL_DIR/scripts/search.py "cloud migration" --json

# With options
uv run $SKILL_DIR/scripts/search.py "security architecture" --limit 10 --json

# Get full entry by ID
uv run $SKILL_DIR/scripts/get.py 4640016 --json
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
# Get complete entry by ID
uv run $SKILL_DIR/scripts/get.py 42

# JSON output for structured processing
uv run $SKILL_DIR/scripts/get.py 42 --json
```

### Required Citation Format

When presenting results, always include:

- **Document ID** - The entry ID from the database
- **Document title** - The `question` field
- **Source path** - Path to original document: `docs/{id}.docx`

### Example Output Format

```text
**Source: Bid Library Entry 4640016**
Title: "Cloud Migration Approach for Enterprise Clients"
Document: docs/4640016.docx

[Content from the entry...]
```

## Working with Content

### Workflow

1. **Search** - Use `search.py` to find relevant entries by keyword, category, or tags
2. **Retrieve** - Use `get.py` with the ID from search results
3. **Cite** - Always include entry ID, title (question), and source path
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
- ✓ Used `$SKILL_DIR/scripts/search.py` and `get.py` for all database access
- ✓ Selected entries that genuinely match the user's criteria
- ✓ Avoided entry duplication
- ✓ Included entry ID, question/title, and category context
- ✓ Checked image availability before accessing .docx files
- ✓ Provided source path (`docs/{id}.docx`) for verification
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
