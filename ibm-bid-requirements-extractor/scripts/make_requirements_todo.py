#!/usr/bin/env python3
"""
Create a requirements extraction TODO file for a tender/bid document or spreadsheet.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

SUPPORTED_SOURCE_TYPES = {"pdf", "docx", "xlsx", "xls", "csv", "tsv"}
CANONICAL_OUTPUT = "../tmp/ibm-bid-requirements-extractor.md"


def detect_source_type(path: Path) -> str:
    ext = path.suffix.lower().lstrip(".")
    if ext in SUPPORTED_SOURCE_TYPES:
        return ext
    return "other"


def get_repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def resolve_output_path(raw_output: str) -> Path:
    if raw_output == CANONICAL_OUTPUT:
        return get_repo_root() / "tmp" / "requirements_todo.md"

    output_path = Path(raw_output).expanduser()
    if not output_path.is_absolute():
        output_path = Path.cwd() / output_path

    return output_path.resolve()


def validate_source_paths(raw_source_paths: Sequence[str]) -> list[Path]:
    source_paths: list[Path] = []

    for raw_path in raw_source_paths:
        path = Path(raw_path).expanduser()
        if not path.exists():
            raise FileNotFoundError(f"Source file does not exist: {path}")
        if not path.is_file():
            raise ValueError(f"Source path is not a file: {path}")
        source_paths.append(path.resolve())

    return source_paths


def build_template(source_paths: Sequence[Path]) -> str:
    source_types = ", ".join(sorted({detect_source_type(path) for path in source_paths}))
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    source_list = "\n".join(f"- `{path}`" for path in source_paths)

    return f"""# Requirements Extraction TODO

- Output artifact: `{CANONICAL_OUTPUT}`
- Source types: {source_types}
- Generated: {generated}
- Status: Not started

## Source Files
{source_list}

## Extraction Plan
- [ ] Confirm scope (sections, appendices, schedules)
- [ ] Extract requirement statements from all listed source files
- [ ] Extract response-format constraints, including word/page limits and diagram/image guidance
- [ ] Tag each requirement with ID, section, and type (MUST/SHOULD/MAY)
- [ ] Capture total and per-question diagram, image, figure, table, exhibit, and visual limits
- [ ] Capture whether diagram/image labels, captions, or figure titles count toward word limits
- [ ] Capture dependencies, assumptions, and constraints
- [ ] De-duplicate repeated requirements across documents
- [ ] Identify ambiguities and draft clarification questions
- [ ] Summarize counts and coverage

## Normalization Rules
- Preserve requirement text verbatim where possible.
- Use page references for document sources and row references for spreadsheet sources.
- Mark unknown requirement strength as `Unclassified` rather than guessing.

## Requirements
| ID | Source | Section / Row | Requirement | Type | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Response Constraints
| Scope | Question ID | Source | Constraint Type | Limit / Requirement | Mandatory / Optional / Maximum / Prohibited | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Global | All | TBD | Word/page/attachment/template/diagram/image/table | TBD | TBD | TBD | TBD |
| Per-question | TBD | TBD | Word/page/attachment/template/diagram/image/table | TBD | TBD | TBD | TBD |

## Diagram / Image Limits
| Scope | Question ID | Source | Visual Type | Count / Allowance | Word Count Treatment | Evidence | Clarification Needed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Global | All | TBD | Diagram/image/figure/graphic/table/exhibit/visual | TBD | Included / Excluded / Not stated | TBD | TBD |
| Per-question | TBD | TBD | Diagram/image/figure/graphic/table/exhibit/visual | TBD | Included / Excluded / Not stated | TBD | TBD |

## Clarifications Needed
- [ ] TBD

## Risks / Gaps
- [ ] TBD

## Coverage Summary
- Total requirements extracted: TBD
- Mandatory / optional split: TBD
- Questions with explicit diagram/image limits: TBD
- Questions where diagram/image limits are not stated: TBD
- Global diagram/image limits: TBD
- Diagram/image word-count treatment: TBD
- Source coverage gaps: TBD

## Next Actions
- [ ] TBD
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create the canonical requirements TODO file for tender/bid documents or spreadsheets."
    )
    parser.add_argument(
        "source_paths",
        nargs="+",
        help="One or more paths to tender/bid documents or spreadsheets",
    )
    parser.add_argument(
        "--output",
        default=CANONICAL_OUTPUT,
        help="Output path (default: ../tmp/ibm-bid-requirements-extractor.md, resolved to the repo tmp directory)",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Write the template to stdout instead of a file",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output file if it already exists",
    )
    args = parser.parse_args()

    try:
        source_paths = validate_source_paths(args.source_paths)
        content = build_template(source_paths)

        if args.stdout:
            print(content, end="")
            return 0

        output_path = resolve_output_path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if output_path.exists() and not args.force:
            raise FileExistsError(
                f"Output file already exists: {output_path}. Re-run with --force to overwrite it."
            )

        output_path.write_text(content, encoding="utf-8")
    except (FileExistsError, FileNotFoundError, ValueError) as exc:
        parser.exit(status=2, message=f"error: {exc}\n")

    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
