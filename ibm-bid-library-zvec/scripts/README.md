# Scripts

Cross-platform entrypoints for the `ibm-bid-library-zvec` skill.

## Files

- `search.py` — query the zvec store via `zvec_hybrid.query.HybridSearcher`
- `get.py` — retrieve document chunks directly from the zvec store
- `info.py` — show zvec store metadata and index stats
- `cache_models.py` — optional helper to pre-download the local cross-encoder model
- `common.py` — shared path helpers for the store path and extra runtime packages

## Usage

From the skill directory:

```bash
uv run scripts/info.py
uv run scripts/search.py "<query>"
uv run scripts/get.py <doc_id>
```

Optional local reranker cache warm-up:

```bash
uv run scripts/cache_models.py --force-download
```

The scripts use inline PEP 723 metadata and a local `tool.uv.sources` entry for
`zvec-hybrid`. Normal execution no longer requires a skill-local `.venv`.
