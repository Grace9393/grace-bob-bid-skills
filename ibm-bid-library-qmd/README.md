# IBM Bid Library QMD

Quick-start instructions for creating the markdown collection and running the vector embedding index.

## Prerequisites

- Python 3.12+ and `uv`
- `qmd` CLI installed and on `$PATH`
- `all_docs.xlsx` placed at `skills/ibm-bid-library/src/` (not in the repo)

Install `qmd` if needed:

```bash
pip install qmd
```

## Create the collection

### Full rebuild (recommended)

Rebuilds the corpus from `all_docs.xlsx`, replays durable custom documents, then regenerates SQLite FTS, zvec, and QMD together:

```bash
make bid-library-rebuild-all
```

### QMD only

Use this when the corpus is already current and you only need to refresh `collection/`:

```bash
make qmd-create-bid-library
```

Both targets write output to `skills/ibm-bid-library-qmd/collection/`. Do not edit that directory directly — it is replaced on every rebuild.

## Run the vector embedding

After the collection exists, build the BM25 + vector index:

```bash
uv run skills/ibm-bid-library-qmd/scripts/cache_models.py
```

This runs `qmd embed -f` against the registered `ibm-bid-library` collection. The collection is auto-registered on first use if not already present.

## Verify

```bash
uv run skills/ibm-bid-library-qmd/scripts/info.py
uv run skills/ibm-bid-library-qmd/scripts/search.py "cloud migration" --limit 5 --json
```

## Adding documents

Add one document durably without rebuilding retrieval targets:

```bash
make bid-library-add-document \
  SOURCE=/path/to/document.docx \
  DOCUMENT_ID=document-id \
  CATEGORY=Architecture
```

When ready to refresh all retrieval targets:

```bash
make bid-library-rebuild-all
```

## Environment variables

| Variable | Purpose |
|---|---|
| `IBM_BID_LIBRARY_QMD_HOME` | Override QMD config/cache home (useful for test isolation) |
| `IBM_BID_LIBRARY_QMD_COLLECTION` | Override collection name (default: `ibm-bid-library`) |
| `QMD_COMMAND` | Override the `qmd` binary path |
