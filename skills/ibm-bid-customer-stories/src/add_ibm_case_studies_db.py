#!/usr/bin/env python3
"""
Add IBM.com case studies (markdown files) to the customer stories SQLite FTS5 database.

Usage:
    python3 add_ibm_case_studies_db.py [--source-dir PATH]

Parses YAML frontmatter from each .md file and stores title, description, and
full markdown body for full-text search. Idempotent — skips URLs already present.
"""

import argparse
import re
import sqlite3
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
SKILL_DIR = SCRIPT_DIR.parent
DB_FILE = SKILL_DIR / "stories.sqlite"
DEFAULT_SOURCE_DIR = Path(
    "/Users/telcott/tmp/code/ibm_client_stories_scraper/ibm_case_studies_md"
)

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)", re.DOTALL)
FIELD_RE = re.compile(r"^(\w+):\s*['\"]?(.*?)['\"]?\s*$")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (meta_dict, body) from a markdown file with YAML frontmatter."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text.strip()
    meta = {}
    for line in m.group(1).splitlines():
        fm = FIELD_RE.match(line)
        if fm:
            meta[fm.group(1)] = fm.group(2).strip()
    return meta, m.group(2).strip()


def slug_to_name(stem: str) -> str:
    """Convert a filename stem to a display name.

    Examples:
        'kraft-heinz-company' -> 'Kraft Heinz Company'
        'ABB'                 -> 'ABB'
        'abu-dhabi-adnoc'     -> 'Abu Dhabi Adnoc'
    """
    return stem.replace("-", " ").replace("_", " ").title()


def get_existing_urls(conn: sqlite3.Connection) -> set[str]:
    """Return the set of links already stored with source='ibm.com'."""
    cursor = conn.cursor()
    cursor.execute("SELECT links FROM stories_fts WHERE source = 'ibm.com'")
    return {row[0] for row in cursor.fetchall() if row[0]}


def add_ibm_case_studies(source_dir: str) -> bool:
    source_path = Path(source_dir)
    if not source_path.exists():
        print(f"Error: source directory not found: {source_path}")
        return False

    if not DB_FILE.exists():
        print(f"Error: database not found at {DB_FILE}")
        print("Run create_db.py first to initialise the database.")
        return False

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM stories_fts")
    count_before = cursor.fetchone()[0]
    print(f"Database has {count_before} stories before import")

    existing_urls = get_existing_urls(conn)

    md_files = sorted(source_path.glob("*.md"))
    print(f"Found {len(md_files)} markdown files in {source_path}")

    added = skipped = errors = 0

    for md_file in md_files:
        try:
            text = md_file.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)

            url = meta.get("url", "").strip("'\"")
            title = meta.get("title", "").strip("'\"")
            description_meta = meta.get("description", "").strip("'\"")

            if url and url in existing_urls:
                skipped += 1
                continue

            company = slug_to_name(md_file.stem)

            # Store frontmatter description + full body so the entire text is searchable
            description = (
                f"{description_meta}\n\n{body}".strip() if body else description_meta
            )

            cursor.execute(
                "INSERT INTO stories_fts"
                "(title, company, industry, clouds_implemented, description, outcomes, source, links)"
                " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (title, company, "", "", description, "", "ibm.com", url),
            )
            added += 1
            if url:
                existing_urls.add(url)

        except Exception as e:
            print(f"  Error processing {md_file.name}: {e}")
            errors += 1

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM stories_fts")
    count_after = cursor.fetchone()[0]

    print(f"Added {added} IBM.com case studies")
    if skipped:
        print(f"Skipped {skipped} already-present entries")
    if errors:
        print(f"Errors: {errors}")
    print(f"Database now has {count_after} total stories")

    conn.close()
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Add IBM.com case studies to the customer stories database"
    )
    parser.add_argument(
        "--source-dir",
        default=str(DEFAULT_SOURCE_DIR),
        help=f"Directory containing .md files (default: {DEFAULT_SOURCE_DIR})",
    )
    args = parser.parse_args()
    add_ibm_case_studies(args.source_dir)


if __name__ == "__main__":
    main()
