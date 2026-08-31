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

import subprocess
import sys


def main() -> int:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "zvec_hybrid.cache_cross_encoder_cli",
            *sys.argv[1:],
        ]
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
