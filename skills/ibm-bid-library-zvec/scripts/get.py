
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


def _value(row: object, key: str, default: object = None) -> object:
    if row is None:
        return default
    if isinstance(row, dict):
        return row.get(key, default)
    getter = getattr(row, "get", None)
    if callable(getter):
        try:
            return getter(key, default)
        except TypeError:
            try:
                return getter(key)
            except TypeError:
                pass
    field_fn = getattr(row, "field", None)
    if callable(field_fn):
        try:
            return field_fn(key)
        except Exception:
            pass
    return getattr(row, key, default)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="get.py",
        description="Retrieve a document by ID from the zvec store.",
    )
    parser.add_argument("doc_id", help="Document ID to retrieve")
    parser.add_argument("-f", "--full", action="store_true", help="Show full content")
    parser.add_argument("--preview-length", type=int, default=500, help="Preview length")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output JSON")
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args(sys.argv[1:])
    zvec_store = zvec_store_path()

    if args.preview_length < 1:
        print("Error: --preview-length must be >= 1.", file=sys.stderr)
        return 2
    if not zvec_store.exists():
        print(f"Error: store not found: {zvec_store}", file=sys.stderr)
        return 2

    try:
        import zvec
    except ImportError:
        print(
            "Error: zvec runtime not available. Run this script with uv.",
            file=sys.stderr,
        )
        return 2

    doc_id = args.doc_id
    safe_doc_id = doc_id.replace("'", "\\'")

    try:
        col = zvec.open(str(zvec_store), zvec.CollectionOption(read_only=True))
        results = col.query(
            filter=f"path = '{safe_doc_id}.md'",
        )
    except RuntimeError as exc:
        print(f"Error: unable to open zvec store: {exc}", file=sys.stderr)
        return 2

    if not results:
        print(f"Error: document not found: {doc_id}", file=sys.stderr)
        return 4

    chunks = sorted(results, key=lambda r: _value(r, "chunk_index") or 0)
    full_text = "\n\n".join((_value(chunk, "text", "") or "").strip() for chunk in chunks).strip()
    preview = full_text if args.full else full_text[: args.preview_length]
    if not args.full and len(full_text) > args.preview_length:
        preview = f"{preview}..."

    if args.as_json:
        payload = {
            "doc_id": doc_id,
            "chunk_count": len(chunks),
            "preview": preview,
            "content": full_text if args.full else preview,
            "chunks": [
                {
                    "chunk_index": _value(chunk, "chunk_index"),
                    "chunk_start": _value(chunk, "chunk_start"),
                    "chunk_end": _value(chunk, "chunk_end"),
                    "text": _value(chunk, "text"),
                }
                for chunk in chunks
            ],
        }
        print(json.dumps(payload, indent=2))
        return 0

    print(preview)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
