#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "staffing-or==0.1.0",
# ]
# [tool.uv.sources]
# staffing-or = { path = "../assets/wheels/staffing_or-0.1.0-py3-none-any.whl" }
# ///

from __future__ import annotations

from staffing_or.cli import app


def main() -> int:
    app()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
