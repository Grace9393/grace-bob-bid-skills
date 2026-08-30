# Database Creation

This directory contains the scripts to create and populate the IBM Bid Library SQLite database.

## Prerequisites

- Python 3.13+


## Files

| File | Description |
|------|-------------|
| `db.sql` | Database schema (FTS5 table) |
| `create_db.py` | Python script to populate database from Excel |
| `all_docs.xlsx` | Source Excel file with bid library entries (not in repo) |

## Recreating the Database

### Step 1: Create the schema

From the `src/` directory:

```bash
cd skills/ibm-bid-library/src
sqlite3 ../docs.sqlite < db.sql
```

Or if starting fresh (removes existing database):

```bash
cd skills/ibm-bid-library/src
rm -f ../docs.sqlite
sqlite3 ../docs.sqlite < db.sql
```

### Step 2: Populate from Excel

Ensure `all_docs.xlsx` is in the `src/` directory, then run:

```bash
cd skills/ibm-bid-library/src
python3 create_db.py
```

This will:
1. Read entries from `all_docs.xlsx`
2. Extract any "Score:" values embedded in the answer text
3. Link to source documents in `../docs/` if they exist
4. Collect document image artifacts from `../docs/images/<doc number>_artifacts/`
5. Optionally describe images using LM Studio or Ollama and store:
   - `images_text`: searchable concatenation of image descriptions
   - `images`: JSON metadata (path/alt/description)
6. Insert all entries in the database
7. Store the `id` column as text (matches the `.docx` filename)

### Step 3: Verify

```bash
sqlite3 -readonly ../docs.sqlite "SELECT COUNT(*) FROM entries_fts;"
sqlite3 -readonly ../docs.sqlite "SELECT COUNT(*) FROM entries_fts WHERE score IS NOT NULL;"
```

## Image Description Providers

`create_db.py` supports LM Studio and Ollama via OpenAI-compatible APIs.

Defaults:
- LM Studio base URL: `http://localhost:1234/v1`
- LM Studio model: `qwen3-vl-4b-instruct-mlx`
- Ollama base URL: `http://localhost:11434/v1`
- Ollama model: `qwen3-vl:8b`

Examples:

```bash
# LM Studio (default)
python3 create_db.py --provider lmstudio

# Ollama
pytho3 create_db.py --provider ollama

# Custom OpenAI-compatible endpoint
python3 create_db.py --provider custom --base-url http://localhost:8080/v1 --model my-vl-model

# Disable image descriptions (still stores image paths)
python3 create_db.py --disable-descriptions
```

## Expected Excel Columns

The `all_docs.xlsx` file should have these columns:

| Excel Column | Database Column |
|--------------|-----------------|
| Library Entry Id | id |
| Question * | question |
| Answer * | answer |
| Stack | stack |
| Category | category |
| Sub-Category | sub_category |
| Tags (separated by commas ",") | tags |
| Language | language |
| Library Entry URL | library_url |

The `source_path` and `score` columns are derived automatically:
- `source_path`: Set if `../docs/{id}.docx` exists
- `has_images`: True if the `.docx` contains any embedded images
- `score`: Extracted from "Score: N" pattern in answer text

Image columns:
- `images_text`: Newline-joined descriptions of image artifacts (searchable)
- `images`: JSON list of image metadata (unindexed)
