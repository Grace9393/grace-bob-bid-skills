# zvec Store Creation

The IBM Bid Library zvec hybrid vector store is now materialised from the
canonical corpus built by `ibm-document-corpus-builder`.

## Prerequisites

- Python 3.12+
- `uv`
- Place `all_docs.xlsx` in `skills/ibm-bid-library/src/` (not included in the repo)

## Files

| File | Description |
|------|-------------|
| `create_store.py` | Compatibility wrapper that delegates to the corpus zvec builder |

## Recreating the Store

### Full backend rebuild

From the repository root:

```bash
make bid-library-rebuild-all
```

This will:

1. Rebuild `skills/ibm-bid-library/corpus` from `all_docs.xlsx`
2. Replay durable custom documents from `skills/ibm-bid-library/src/custom-documents.yaml`
3. Rebuild SQLite FTS, zvec, and QMD from the same corpus

### zvec only

```bash
make zvec-create-bid-library
```

This will:

1. Back up any existing store to `bid_library_zvec.bak`
2. Ensure the corpus exists
3. Materialise `{entry_id}.md` files from corpus `content.md`
4. Ingest all entries into the zvec store with the configured dense and sparse backends

### Manual steps

```bash
uv run skills/ibm-document-corpus-builder/scripts/build_zvec.py \
  skills/ibm-bid-library/corpus \
  skills/ibm-bid-library-zvec/references/bid_library_zvec \
  --overwrite
```

### Options

```bash
uv run skills/ibm-document-corpus-builder/scripts/build_zvec.py \
  skills/ibm-bid-library/corpus \
  /tmp/bid_library_zvec_test \
  --limit 50 \
  --no-optimize

# Adjust progress reporting
uv run skills/ibm-document-corpus-builder/scripts/build_zvec.py \
  skills/ibm-bid-library/corpus \
  /tmp/bid_library_zvec_test \
  --progress-every 50
```

## Adding Documents

Add one document durably without rebuilding retrieval targets:

```bash
make bid-library-add-document \
  SOURCE=/path/to/document.docx \
  DOCUMENT_ID=document-id \
  CATEGORY=Architecture
```

Repeat that command as documents arrive. When ready, run:

```bash
make bid-library-rebuild-all
```

This full rebuild policy is intentional for BM25 sparse stores. BM25 document
vectors depend on corpus-level statistics, so appending a single document into
an existing zvec BM25 store would produce inconsistent document vectors.

## Store Configuration

| Setting | Value |
|---------|-------|
| Dense backend | `zvec-local` |
| Sparse backend | `bm25` |
| Chunk size | 1000 chars |
| Chunk overlap | 200 chars |
| Dense index | `flat` |
| Optimize | True |

## Verify

After creation, confirm the store is healthy:

```bash
uv run skills/ibm-bid-library-zvec/scripts/info.py
# Expected: ~2994+ chunks, dense=hash/384, sparse=bm25, chunk_size=1000
```

Test a search:

```bash
uv run skills/ibm-bid-library-zvec/scripts/search.py "cloud migration" --limit 5 --json
```
