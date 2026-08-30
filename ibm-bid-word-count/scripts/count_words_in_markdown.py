#!/usr/bin/env -S uv run python
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Count words in markdown using the bid response counting strategy."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|\Z)", re.DOTALL)
DEFAULT_START_MARKER = "<!-- START-COUNT -->"
DEFAULT_END_MARKER = "<!-- END-COUNT -->"


def split_front_matter(markdown: str) -> tuple[dict[str, int], str]:
    match = FRONT_MATTER_RE.match(markdown)
    if not match:
        return {}, markdown

    limits = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            continue
        key = key.strip()
        if key not in {"min-word-count", "max-word-count"}:
            continue
        value = value.strip().strip("\"'")
        try:
            limits[key] = int(value)
        except ValueError:
            continue

    return limits, markdown[match.end() :]


def count_words_in_markdown(markdown):
    _, text = split_front_matter(markdown)

    # Comments
    text = re.sub(r"<!--(.*?)-->", "", text, flags=re.MULTILINE)
    # Tabs to spaces
    text = text.replace("\t", "    ")
    # More than 1 space to 4 spaces
    text = re.sub(r"[ ]{2,}", "    ", text)
    # Footnotes
    text = re.sub(r"^\[[^]]*\][^(].*", "", text, flags=re.MULTILINE)
    # Indented blocks of code
    text = re.sub(r"^( {4,}[^-*]).*", "", text, flags=re.MULTILINE)
    # Custom header IDs
    text = re.sub(r"{#.*}", "", text)
    # Replace newlines with spaces for uniform handling
    text = text.replace("\n", " ")
    # Remove images
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    # Remove HTML tags
    text = re.sub(r"</?[^>]*>", "", text)
    # Remove special characters
    text = re.sub(r"[#*`~\-–^=<>+|/:]", "", text)
    # Remove footnote references
    text = re.sub(r"\[[0-9]*\]", "", text)
    # Remove enumerations
    text = re.sub(r"[0-9#]*\.", "", text)

    return len(text.split())


def extract_between_markers(
    markdown: str, start_marker: str, end_marker: str
) -> tuple[str, bool]:
    start_index = markdown.find(start_marker)
    end_index = markdown.find(end_marker)

    if start_index == -1 and end_index == -1:
        return markdown, False
    if start_index == -1:
        raise ValueError(f"Found {end_marker!r} without {start_marker!r}.")
    if end_index == -1:
        raise ValueError(f"Found {start_marker!r} without {end_marker!r}.")
    if end_index < start_index:
        raise ValueError(f"Found {end_marker!r} before {start_marker!r}.")

    return markdown[start_index + len(start_marker) : end_index], True


def extract_from_heading(markdown: str, heading: str, include_heading: bool) -> str:
    lines = markdown.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index if include_heading else index + 1
            return "".join(lines[start:])
    return markdown


def extract_until_heading(markdown: str, heading: str) -> str:
    lines = markdown.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.strip() == heading:
            return "".join(lines[:index])
    return markdown


def read_markdown(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Count words in markdown with the IBM bid response strategy."
    )
    parser.add_argument("path", help="Markdown file to count, or '-' for stdin.")
    parser.add_argument(
        "--from-heading",
        help=(
            "Count only content after this exact heading, for example '## Answer:'. "
            "Ignored when count markers are present."
        ),
    )
    parser.add_argument(
        "--until-heading",
        help=(
            "Stop counting before this exact heading, for example '## Evidence Log'. "
            "Ignored when count markers are present."
        ),
    )
    parser.add_argument(
        "--include-heading",
        action="store_true",
        help="Include the matched --from-heading line in the count.",
    )
    parser.add_argument(
        "--start-marker",
        default=DEFAULT_START_MARKER,
        help="Start marker for the counted section. Defaults to '<!-- START-COUNT -->'.",
    )
    parser.add_argument(
        "--end-marker",
        default=DEFAULT_END_MARKER,
        help="End marker for the counted section. Defaults to '<!-- END-COUNT -->'.",
    )
    parser.add_argument(
        "--ignore-count-markers",
        action="store_true",
        help="Ignore START-COUNT/END-COUNT markers and use heading or whole-document counting.",
    )
    parser.add_argument(
        "--show-limits",
        action="store_true",
        help="Also print min-word-count/max-word-count front matter and status.",
    )
    args = parser.parse_args()

    markdown = read_markdown(args.path)
    limits, markdown = split_front_matter(markdown)
    try:
        markers_found = False
        if not args.ignore_count_markers:
            markdown, markers_found = extract_between_markers(
                markdown, args.start_marker, args.end_marker
            )
        if args.from_heading and not markers_found:
            markdown = extract_from_heading(markdown, args.from_heading, args.include_heading)
        if args.until_heading and not markers_found:
            markdown = extract_until_heading(markdown, args.until_heading)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    count = count_words_in_markdown(markdown)
    if not args.show_limits:
        print(count)
        return 0

    minimum = limits.get("min-word-count")
    maximum = limits.get("max-word-count")
    if minimum is not None and count < minimum:
        status = "under"
    elif maximum is not None and count > maximum:
        status = "over"
    else:
        status = "within"

    print(f"count: {count}")
    if minimum is not None:
        print(f"min-word-count: {minimum}")
    if maximum is not None:
        print(f"max-word-count: {maximum}")
    print(f"status: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
