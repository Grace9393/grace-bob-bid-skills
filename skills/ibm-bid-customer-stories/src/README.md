# IBM Customer Stories Database - Source Files

This directory contains the scripts and schema needed to create and maintain the SQLite database for customer stories.

## Files

- **db.sql**: Database schema definition with FTS5 full-text search
- **create_db.py**: Script to build the base SQLite database from Salesforce CSV
- **add_looip_stories_db.py**: Script to add Loopio customer stories to the database
- **add_ibm_case_studies_db.py**: Script to add IBM.com case study markdown files to the database
- **loopio_customer_stories_consolidated.csv**: Loopio stories source data

## Creating the Database

To create or rebuild the complete database, run all scripts in sequence:

### Step 1: Create Base Database (Salesforce Stories)

```bash
cd /Users/telcott/tmp/code/IBM_skills/skills/ibm-bid-customer-stories
python3 src/create_db.py
```

This will:
1. Read `customer_stories_matrix.csv` from the skill directory
2. Create `stories.sqlite` with full-text search enabled
3. Import 170 Salesforce customer stories with `source='Salesforce'`
4. Set links to Box.com URLs

### Step 2: Add Loopio Stories

```bash
python3 src/add_looip_stories_db.py
```

This will:
1. Read `src/loopio_customer_stories_consolidated.csv`
2. Query `ibm-bid-library/docs.sqlite` to resolve document paths
3. Add 687 Loopio stories with `source='loopio'`
4. Set links to `../ibm-bid-library/docs/{doc_id}.docx`
5. Display statistics about stories linked to documents

### Step 3: Add IBM.com Case Studies

```bash
python3 src/add_ibm_case_studies_db.py [--source-dir PATH]
```

This will:
1. Scan all `.md` files in the source directory (default: `/Users/telcott/tmp/code/ibm_client_stories_scraper/ibm_case_studies_md`)
2. Parse YAML frontmatter for `title`, `url`, and `description`
3. Store frontmatter description + full markdown body in the `description` field (maximises FTS coverage)
4. Derive company name from the filename slug
5. Add ~1100 IBM.com case studies with `source='ibm.com'`
6. Set links to the original IBM.com case study URL
7. Skip entries whose URL is already in the database (idempotent)

**Final Result**: ~1,957 total customer stories (170 Salesforce + 687 Loopio + 1,100 IBM.com)

## Database Schema

### FTS5 Virtual Table: `stories_fts`

Full-text search enabled on all columns except `links`:

- `title`: Story title
- `company`: Client organization name
- `industry`: Industry sector (e.g., "Financial Services", "Healthcare")
- `clouds_implemented`: Salesforce products deployed (e.g., "Service Cloud, Sales Cloud")
- `description`: Detailed challenge/solution/implementation narrative
- `outcomes`: Quantified business results with metrics
- `source`: Story source - either 'Salesforce' or 'loopio'
- `links`: Reference documentation URLs or document paths (UNINDEXED)

**Tokenization**: Uses Porter stemming (`tokenize = 'porter unicode61'`) for better search recall

## Source Column

Stories are tagged with their origin:

- **Salesforce** (170 stories): Original Salesforce customer stories
  - Links: Box.com URLs (e.g., `https://ibm.box.com/s/...`)

- **loopio** (687 stories): Loopio library customer stories
  - Links: Document paths (e.g., `../ibm-bid-library/docs/10013864.docx`)

- **ibm.com** (~1,100 stories): IBM.com case study pages (scraped markdown)
  - Links: IBM.com URLs (e.g., `https://www.ibm.com/case-studies/abb`)
  - Description: Full article text for maximum FTS coverage

## Querying the Database

### Search by source:

```sql
-- Find all Salesforce stories
SELECT title, company FROM stories_fts WHERE source = 'Salesforce';

-- Find all Loopio stories
SELECT title, company FROM stories_fts WHERE source = 'loopio';
```

### Full-text search:

```sql
-- Search across all text fields
SELECT title, company, industry
FROM stories_fts
WHERE stories_fts MATCH 'AI AND banking';

-- Search specific source
SELECT title, company
FROM stories_fts
WHERE stories_fts MATCH 'healthcare' AND source = 'loopio';
```

### Get document path:

```sql
-- Stories with linked documents
SELECT title, company, links
FROM stories_fts
WHERE links LIKE '%ibm-bid-library%';
```

## Maintenance

### Rebuilding from scratch:

```bash
# Start fresh
rm stories.sqlite

# Step 1: Create base database (Salesforce)
python3 src/create_db.py

# Step 2: Add Loopio stories
python3 src/add_looip_stories_db.py

# Step 3: Add IBM.com case studies
python3 src/add_ibm_case_studies_db.py
```

### Updating a single source:

```bash
# Loopio only
sqlite3 stories.sqlite "DELETE FROM stories_fts WHERE source = 'loopio';"
python3 src/add_looip_stories_db.py

# IBM.com only (idempotent — safe to re-run, skips existing URLs)
python3 src/add_ibm_case_studies_db.py

# IBM.com from a custom directory
python3 src/add_ibm_case_studies_db.py --source-dir /path/to/markdown/files
```

## Dependencies

- Python 3.13+
- sqlite3 (built-in)
- csv (built-in)
- Access to `ibm-bid-library/docs.sqlite` for document path resolution
