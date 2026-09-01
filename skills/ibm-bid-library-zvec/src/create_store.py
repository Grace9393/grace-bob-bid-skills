"""
Create the IBM Bid Library zvec hybrid vector store from all_docs.xlsx.

Run via the Makefile target:
    make zvec-create-bid-library

Or manually (from this directory):
    uv run --with pandas --with openpyxl create_store.py [--limit N] [--no-optimize] [--progress-every N]
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

XLSX = Path(__file__).parent / "all_docs.xlsx"
STORE_PATH = Path(__file__).resolve().parents[1] / "references" / "bid_library_zvec"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create IBM Bid Library zvec hybrid store")
    parser.add_argument(
        "--progress-every",
        type=int,
        default=100,
        metavar="INT",
        help="Print progress every N documents (default: 100)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        metavar="INT",
        help="Cap the number of entries processed (for testing)",
    )
    parser.add_argument(
        "--no-optimize",
        action="store_true",
        help="Skip the optimize step (faster for test runs)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        import pandas as pd
    except ImportError:
        print(
            "Error: pandas is not installed. Run:\n"
            "  uv run --with pandas --with openpyxl src/create_store.py",
            file=sys.stderr,
        )
        return 1

    try:
        from zvec_hybrid.ingest import IngestionConfig, ingest_directory
    except ImportError:
        print(
            "Error: zvec_hybrid is not installed. Run via uv so dependencies are provisioned:\n"
            "  uv run --with pandas --with openpyxl src/create_store.py",
            file=sys.stderr,
        )
        return 1

    if not XLSX.exists():
        print(
            f"Error: source file not found: {XLSX}\n"
            "Place all_docs.xlsx in the src/ directory and re-run.",
            file=sys.stderr,
        )
        return 1

    print(f"Reading {XLSX} ...")
    df = pd.read_excel(XLSX)

    df = df.rename(columns={
        "Library Entry Id": "id",
        "Question *": "question",
        "Answer *": "answer",
        "Sub-Category": "sub_category",
        'Tags (separated by commas ",")': "tags",
        "Library Entry URL": "library_url",
    })

    if args.limit is not None:
        df = df.head(args.limit)
        print(f"Limited to {len(df)} entries (--limit {args.limit})")

    print(f"Writing {len(df)} document files to temp directory ...")
    tmp_dir = Path(tempfile.mkdtemp(prefix="bid_library_zvec_"))
    try:
        for _, row in df.iterrows():
            entry_id = str(row.get("id", "")).strip()
            question = str(row.get("question", "") or "").strip()
            category = str(row.get("Category", "") or "").strip()
            sub_category = str(row.get("sub_category", "") or "").strip()
            tags = str(row.get("tags", "") or "").strip()
            language = str(row.get("Language", "") or "").strip()
            library_url = str(row.get("library_url", "") or "").strip()
            answer = str(row.get("answer", "") or "").strip()

            content = (
                f"Question: {question}\n"
                f"\n"
                f"Category: {category}\n"
                f"Sub-category: {sub_category}\n"
                f"Tags: {tags}\n"
                f"Language: {language}\n"
                f"Library URL: {library_url}\n"
                f"\n"
                f"{answer}"
            )

            doc_path = tmp_dir / f"{entry_id}.md"
            doc_path.write_text(content, encoding="utf-8")

        optimize = not args.no_optimize

        print(f"Ingesting into zvec store at {STORE_PATH} ...")
        print(f"  dense_backend=zvec-local, sparse_backend=bm25, chunk_size=1000, chunk_overlap=200")
        print(f"  optimize={optimize}, overwrite=True")

        config = IngestionConfig(
            source_dir=tmp_dir,
            store_path=STORE_PATH,
            pattern="**/*",
            overwrite=True,
            dense_embedding_backend="zvec-local",
            sparse_embedding_backend="bm25",
            chunk_size=1000,
            chunk_overlap=200,
            optimize=optimize,
            progress_every=args.progress_every,
        )
        summary = ingest_directory(config)

        print("\nDone.")
        if hasattr(summary, "__dict__"):
            for k, v in vars(summary).items():
                print(f"  {k}: {v}")
        else:
            print(f"  {summary}")

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
