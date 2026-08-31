# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "zvec-hybrid==0.1.8",
#   "zvec>=0.3.1",
#   "bm25s",
#   "sentence-transformers>=5.3.0",
# ]
# [tool.uv.sources]
# zvec-hybrid = { path = "../assets/wheels/zvec_hybrid-0.1.8-py3-none-any.whl" }
# ///

from __future__ import annotations

import argparse
import json
import os
import sys

from common import zvec_store_path

os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="search.py",
        description="Search the IBM bid library zvec store.",
    )
    parser.add_argument("query", help="Search query")
    parser.add_argument("--offset", type=int, default=0, help="Result offset for pagination")
    parser.add_argument("--limit", type=int, default=20, help="Max results to return")
    parser.add_argument(
        "--show-scores",
        action="store_true",
        help="Include numeric scores in text output",
    )
    parser.add_argument("--min-score", type=float, help="Minimum score threshold (0-1)")
    parser.add_argument(
        "--reranker",
        choices=["rrf", "weighted", "local", "qwen"],
        default="rrf",
        help="Reranker strategy (default: rrf)",
    )
    parser.add_argument(
        "--candidate-topk",
        type=int,
        help="Candidate retrieval depth before reranking",
    )
    parser.add_argument(
        "--dense-weight",
        type=float,
        default=0.35,
        help="Dense score weight for weighted reranker",
    )
    parser.add_argument(
        "--zvec-filter",
        "--filter",
        dest="filter_expr",
        help="Optional zvec filter expression",
    )
    parser.add_argument("--hnsw-ef", type=int, help="Optional HNSW ef override")
    parser.add_argument("--ivf-nprobe", type=int, help="Optional IVF nprobe override")
    parser.add_argument(
        "--post-reranker",
        choices=["local", "api"],
        default="local",
        help="Stage-2 reranker after fusion (default: local)",
    )
    parser.add_argument(
        "--post-reranker-topk",
        type=int,
        help="Candidate depth for stage-2 reranking",
    )
    parser.add_argument(
        "--post-reranker-model",
        default="cross-encoder/ms-marco-MiniLM-L6-v2",
        help="Cross-encoder model for stage-2 reranking",
    )
    parser.add_argument(
        "--post-reranker-base-url",
        help="OpenAI-compatible base URL for --post-reranker api",
    )
    parser.add_argument(
        "--show-chars",
        type=int,
        default=180,
        help="Number of text chars in text output",
    )
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output JSON")
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args(sys.argv[1:])
    zvec_store = zvec_store_path()
    if args.post_reranker and args.post_reranker_topk is None:
        args.post_reranker_topk = max(args.offset + args.limit, 50)

    if not zvec_store.exists():
        print(f"Error: store not found: {zvec_store}", file=sys.stderr)
        return 2
    if not args.query.strip():
        print("Error: query cannot be empty", file=sys.stderr)
        return 3
    if args.offset < 0 or args.limit <= 0:
        print("Error: offset must be >= 0 and limit must be > 0", file=sys.stderr)
        return 3
    if args.min_score is not None and not 0.0 <= args.min_score <= 1.0:
        print("Error: --min-score must be between 0 and 1", file=sys.stderr)
        return 3
    if args.show_chars < 0:
        print("Error: --show-chars must be >= 0", file=sys.stderr)
        return 3

    try:
        from zvec_hybrid.query import HybridSearcher
    except ImportError:
        print(
            "Error: zvec_hybrid runtime not available. Run this script with uv.",
            file=sys.stderr,
        )
        return 2

    try:
        searcher = HybridSearcher(zvec_store)
        raw_hits = searcher.search(
            args.query,
            topk=args.offset + args.limit,
            candidate_topk=args.candidate_topk,
            reranker=args.reranker,
            dense_weight=args.dense_weight,
            filter_expr=args.filter_expr,
            hnsw_ef=args.hnsw_ef,
            ivf_nprobe=args.ivf_nprobe,
            post_reranker=args.post_reranker,
            post_reranker_topk=args.post_reranker_topk,
            post_reranker_model=args.post_reranker_model,
            post_reranker_base_url=args.post_reranker_base_url,
        )
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 3
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except RuntimeError as exc:
        print(f"Error: unable to open zvec store: {exc}", file=sys.stderr)
        return 2

    hits = raw_hits
    if args.min_score is not None:
        hits = [hit for hit in hits if hit.score >= args.min_score]
    hits = hits[args.offset : args.offset + args.limit]

    if not hits:
        print("No results.", file=sys.stderr)
        return 4

    if args.as_json:
        payload = [
            {
                "doc_id": hit.doc_id,
                "path": hit.path,
                "score": hit.score,
                "text": hit.text,
                "chunk_index": hit.chunk_index,
                "chunk_start": hit.chunk_start,
                "chunk_end": hit.chunk_end,
                "metadata": hit.metadata,
            }
            for hit in hits
        ]
        print(json.dumps(payload, indent=2))
        return 0

    for idx, hit in enumerate(hits, start=1):
        snippet = " ".join(hit.text.split())[: args.show_chars]
        if args.show_scores:
            print(f"{idx}. score={hit.score:.4f} id={hit.doc_id}")
        else:
            print(f"{idx}. id={hit.doc_id}")
        print(f"   path: {hit.path}")
        if hit.chunk_index is not None:
            print(
                f"   chunk: {hit.chunk_index} "
                f"[{hit.chunk_start or 0}:{hit.chunk_end or 0}]"
            )
        print(f"   text: {snippet}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
