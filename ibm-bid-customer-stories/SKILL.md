---
name: ibm-bid-customer-stories
description: Use this skill when writing tender responses, proposals, or bids that need customer evidence, proof points, or case studies. Access a database of 850+ IBM customer success stories with quantified outcomes across industries (healthcare, government, finance, retail) and Salesforce clouds (Sales, Service, Marketing, Agentforce, etc.). Use when asked for examples, references, similar implementations, or evidence to substantiate claims in tender responses.
---

# IBM Customer Stories Database

## PREREQUISITES - MANDATORY
Use the cross-platform Python runtime scripts from `$SKILL_DIR/scripts/` for all database access.

Do not use shell HEREDOC SQL patterns in this skill (they are not reliable on Windows).

## Context Management

ALWAYS write search results to `./tmp/ibm-bid-customer-stories.md` immediately after retrieval. This prevents context saturation when chaining with other skills. Only copy final deliverables to `./outputs` at completion.

## Overview

**Total Stories**: 860+ customer success stories stored in a SQLite database (`stories.sqlite`) with full-text search (FTS5).

All story content (titles, companies, industries, descriptions, outcomes) is stored in the database for fast, efficient searching. **Do NOT read the CSV file directly** - always use the Python runtime scripts.

### Source Options

Use these canonical source values when filtering or reporting results:

- `Salesforce`
- `ibm.com`
- `loopio`

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
DB_PATH="$SKILL_DIR/stories.sqlite"

# Confirm schema/table availability
uv run $SKILL_DIR/scripts/info.py "$DB_PATH"

# Expanded keyword search (OR-joined synonyms)
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(cloud OR platform) AND (migration OR transformation OR adoption)" --json

# Multi-concept expansion with industry terms
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(healthcare OR NHS OR medical OR clinical) AND (UK OR Britain OR \"United Kingdom\")" --json

# Salesforce cloud-focused search
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(agentforce OR \"service cloud\" OR \"sales cloud\") AND (outcomes OR results)" --json

# Company-focused search
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(salesforce OR ibm) AND (implementation OR transformation)" --json
```

Search options (sqlite-skill) - tighten results first:
- `--offset <n>` pagination
- `--show-status` or `--json-pretty` for query status/warnings
- `--show-scores` or `--min-score <0-1>` for normalized scores
- `--snippet`, `--snippet-length <n>`, `--snippet-column <col>`
- `--query-timeout-ms <ms>`
- `--limit 10`


**Important**: Keep result sets small (top 10-20), then retrieve full records for shortlisted IDs only.

### Step 3: Evaluate Results & Escalate if Needed

**If search results are poor (<5 relevant hits or low quality):**

Use `$query-expansion-strategy` for comprehensive 10-category expansion:
- Generates 5-10 sub-questions across definition/process/rationale/comparison/tooling/metrics/mistakes/trends/personas/use-cases
- Creates entity relationship maps for related concepts
- Produces optimized FTS5 MATCH expressions for exhaustive coverage
- Best for: Ambiguous queries, multi-faceted topics, comprehensive coverage requirements

**If results are good (5+ relevant hits):**
- Filter by metadata (industry, clouds, outcomes)
- Review top 10-15 by rank score
- Retrieve full story content by story ID

### Step 4: Retrieve Story by ID

Use `get.py` from `$SKILL_DIR/scripts/`:

```bash
DB_PATH="$SKILL_DIR/stories.sqlite"

# Get complete story by ID
uv run $SKILL_DIR/scripts/get.py "$DB_PATH" 42

# JSON output for structured processing
uv run $SKILL_DIR/scripts/get.py "$DB_PATH" 42 --json
```

Get options:
- `--preview-length <n>` (>= 1)

Exit codes:
- `2` database path errors
- `3` invalid/empty query or timeout (also invalid preview length)
- `4` no results / not found

### Advanced Querying and Schema

For deeper FTS5 syntax, schema-specific query notes, and runtime-safe patterns, see
[references/sqlite-fts5-query.md](references/sqlite-fts5-query.md).
For retrieval coverage loops, triage rubric, failure recovery, and post-filter patterns, see
[references/search-strategies.md](references/search-strategies.md).

## Citation Requirements

**Always cite sources when presenting customer story content.** Every piece of content from this database must include a reference to enable traceability and verification.

### Required Citation Format

When presenting results, always include:

- **Story ID** - The entry `id` from the database
- **Story title** - The `title` field
- **Company and Industry** - For context

### Example Output Format

```text
**Source: Customer Story #42**
Title: "Transforming Patient Access with Salesforce Health Cloud"
Company: Major Pharma Manufacturer
Industry: Life Sciences

[Content from the story...]
```

### For Multiple Results

When presenting multiple stories, list each with its reference:

```text
Found 3 relevant stories:

1. **Story #16**: "IBM Accelerates Onboarding for Dormakaba" - Manufacturing, Sales Cloud + Agentforce
2. **Story #17**: "IBM Transforms Pricing Strategy for Pfizer" - Healthcare, Sales Cloud + Agentforce
3. **Story #18**: "GSA Optimizes Call Center Efficiency" - Government, Service Cloud + Agentforce
```

## Working with Content

### Step 1: Search

Use Python runtime search to find relevant stories by keyword, industry, or clouds:

```bash
# Search with multiple criteria
DB_PATH="$SKILL_DIR/stories.sqlite"
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "your search terms" --json
```

### Step 2: Retrieve Full Content

Use story ID from search results to get complete story:

```bash
# Get all fields for a specific story
DB_PATH="$SKILL_DIR/stories.sqlite"
uv run $SKILL_DIR/scripts/get.py "$DB_PATH" <story_id> --json
```

### Step 3: Present with Citations

Always include story ID, title, company, and industry when presenting content to enable verification.

### Step 4: Adapt Content

- **Do not copy verbatim** - Adapt to current context
- **Update dates** - Ensure information is current
- **Verify facts** - Cross-reference with `ibm-bid-strategy-and-capabilities-2026` skill
- **Follow guidelines** - Apply `ibm-bid-writer` patterns
- **Maintain citations** - Keep source references in adapted content

## Search and Integration References

Use these targeted references when you need deeper retrieval patterns or multi-skill handoffs:

- [Integration playbooks](references/integration-playbooks.md)
- [FTS5 query reference](references/sqlite-fts5-query.md)
- [Search strategies](references/search-strategies.md)

## Quality Checklist

When presenting customer stories, ensure you:
- ✓ Used `$SKILL_DIR/scripts/search.py` and `get.py` for all database access
- ✓ Selected stories that genuinely match the user's criteria
- ✓ Avoid story duplication
- ✓ Included story ID, company name, and industry context
- ✓ Described both the challenge and solution
- ✓ Highlighted quantified outcomes with specific metrics
- ✓ Provided reference links when available
- ✓ Explained relevance to the user's specific needs
- ✓ Used British English spelling and professional tone
- ✓ Avoided fabricating or embellishing details beyond what's in the database

## Important Notes

- **Always use Python runtime scripts** - Use `uv run $SKILL_DIR/scripts/search.py` and `get.py` for all searches/retrieval (not CSV reads, grep, or shell HEREDOCs)
- **All text is in the database** - No need to read CSV file for text content
- **Limit full content retrieval** - Only fetch full records for shortlisted IDs as stories can be lengthy
- **Results sorted by relevance** - Preserve runtime ranking order from `search.py`
- **Verify currency** - Historical content may need updates
- **Cross-reference** - Combine with other skills for comprehensive responses
- **Respect confidentiality**: Some entries have "NA" for company names - these are anonymized stories that should be presented without identifying the client
- **Link to sources**: Always include the documentation links when available so users can access detailed case studies
- **Quantification is critical**: Prioritize stories with specific, measurable outcomes over generic descriptions
- **Match industry context**: When possible, select stories from the same or similar industry as the prospective client
- **Multi-cloud value**: Stories demonstrating integration across multiple Salesforce clouds often show more comprehensive transformation

## Quick Reference

| Item          | Value                      |
| ------------- | -------------------------- |
| Database      | `stories.sqlite`           |
| CSV Source    | `customer_stories_matrix.csv` (for reference only) |
| Source Options | `Salesforce`, `ibm.com`, `loopio` |
| Total Stories | 860+                       |
| FTS5 Enabled  | Yes                        |
| Database Size | ~2-3MB                     |

**Major Industries**: Financial Services, Healthcare, Manufacturing, Retail, Government, Energy, Technology

**Major Salesforce Clouds**: Sales, Service, Experience, Commerce, Marketing, Health, Agentforce, CPQ, Field Service, Platform
