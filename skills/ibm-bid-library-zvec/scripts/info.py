# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "zvec-hybrid==0.1.8",
#   "zvec>=0.3.1",
#   "bm25s",
# ]
# [tool.uv.sources]
# zvec-hybrid = { path = "../assets/wheels/zvec_hybrid-0.1.8-py3-none-any.whl" }
# ///

from __future__ import annotations

import argparse
import json
import sys

from common import zvec_store_path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="info.py",
        description="Show metadata and stats for the zvec store.",
    )
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output JSON")
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args(sys.argv[1:])
    zvec_store = zvec_store_path()
    metadata_path = zvec_store.parent / f"{zvec_store.name}.embedding.json"

    if not zvec_store.exists():
        print(f"Error: store not found: {zvec_store}", file=sys.stderr)
        return 2
    if not metadata_path.exists():
        print(f"Error: metadata not found: {metadata_path}", file=sys.stderr)
        return 2

    try:
        import zvec
    except ImportError:
        print(
            "Error: zvec runtime not available. Run this script with uv.",
            file=sys.stderr,
        )
        return 2

    try:
        col = zvec.open(str(zvec_store), zvec.CollectionOption(read_only=True))
        stats = json.loads(col.stats)
    except RuntimeError as exc:
        print(f"Error: unable to open zvec store: {exc}", file=sys.stderr)
        return 2
    with metadata_path.open(encoding="utf-8") as f:
        meta = json.load(f)

    payload = {
        "store": str(zvec_store),
        "chunks": stats.get("doc_count", 0),
        "dense_dim": meta.get("dense_dim"),
        "dense_backend": meta.get("dense_embedding_backend"),
        "dense_index": meta.get("dense_index"),
        "sparse_backend": meta.get("sparse_embedding_backend"),
        "chunk_size": meta.get("chunk_size"),
        "chunk_overlap": meta.get("chunk_overlap"),
        "index_completeness": stats.get("index_completeness", {}),
    }

    if args.as_json:
        print(json.dumps(payload, indent=2))
        return 0

    dense_pct = int(payload["index_completeness"].get("dense", 0) * 100)
    sparse_pct = int(payload["index_completeness"].get("sparse", 0) * 100)
    print(f"Store:          {payload['store']}")
    print(f"Chunks:         {payload['chunks']}")
    print(f"Dense dim:      {payload['dense_dim']}")
    print(f"Dense backend:  {payload['dense_backend']}")
    print(f"Dense index:    {payload['dense_index']}")
    print(f"Sparse backend: {payload['sparse_backend']}")
    print(f"Chunk size:     {payload['chunk_size']}")
    print(f"Chunk overlap:  {payload['chunk_overlap']}")
    print(f"Index:          dense={dense_pct}%  sparse={sparse_pct}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
