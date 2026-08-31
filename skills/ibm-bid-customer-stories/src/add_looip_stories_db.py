#!/usr/bin/env python3
"""
Add Loopio customer stories from CSV to existing SQLite FTS5 database.
Maps source_file to actual document paths from ibm-bid-library.
"""

import sqlite3
import csv
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
SKILL_DIR = SCRIPT_DIR.parent
CSV_FILE = SCRIPT_DIR / "loopio_customer_stories_consolidated.csv"
DB_FILE = SKILL_DIR / "stories.sqlite"
BID_LIBRARY_DB = SKILL_DIR.parent / "ibm-bid-library" / "docs.sqlite"


def get_bid_library_path(doc_id, bid_library_conn):
    """
    Look up document path from ibm-bid-library database.

    Args:
        doc_id: Document ID like "10013864"
        bid_library_conn: Connection to ibm-bid-library database

    Returns:
        Document path like "docs/10013864.docx" or None
    """
    cursor = bid_library_conn.cursor()
    cursor.execute("SELECT source_path FROM entries_fts WHERE id = ?", (doc_id,))
    result = cursor.fetchone()
    return result[0] if result else None


def map_source_to_link(source_file, bid_library_conn):
    """
    Map source_file to actual document path from ibm-bid-library.

    Args:
        source_file: Filename like "10013864.md"
        bid_library_conn: Connection to ibm-bid-library database

    Returns:
        Document path string or empty string
    """
    # Extract document ID from source_file (remove .md extension)
    doc_id = source_file.replace('.md', '') if source_file else None

    # Look up actual document path from ibm-bid-library
    if doc_id and bid_library_conn:
        doc_path = get_bid_library_path(doc_id, bid_library_conn)
        if doc_path:
            # Store relative path from ibm-bid-library skill directory
            return f"../ibm-bid-library/{doc_path}"

    return ""


def add_loopio_stories():
    """Add Loopio customer stories to existing database."""

    if not CSV_FILE.exists():
        print(f"Error: CSV file not found at {CSV_FILE}")
        return False

    if not DB_FILE.exists():
        print(f"Error: Database not found at {DB_FILE}")
        print("Please run create_db.py first to create the database")
        return False

    if not BID_LIBRARY_DB.exists():
        print(f"Warning: ibm-bid-library database not found at {BID_LIBRARY_DB}")
        print("Document paths will not be linked")
        bid_library_conn = None
    else:
        bid_library_conn = sqlite3.connect(BID_LIBRARY_DB)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Get count before adding
    cursor.execute("SELECT COUNT(*) FROM stories_fts")
    count_before = cursor.fetchone()[0]
    print(f"Database has {count_before} stories before adding Loopio stories")

    stories_added = 0
    stories_with_docs = 0

    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Map source_file to actual document path (ignore CSV links column)
            links = map_source_to_link(
                row.get('source_file', ''),
                bid_library_conn
            )

            # Track if document path was found
            if links and '../ibm-bid-library/docs/' in links:
                stories_with_docs += 1

            cursor.execute(
                "INSERT INTO stories_fts(title, company, industry, clouds_implemented, description, outcomes, source, links) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    row.get('title', ''),
                    row.get('company', ''),
                    row.get('industry', ''),
                    row.get('clouds_implemented', ''),
                    row.get('description', ''),
                    row.get('outcomes', ''),
                    'loopio',
                    links
                )
            )
            stories_added += 1

    conn.commit()

    # Get count after adding
    cursor.execute("SELECT COUNT(*) FROM stories_fts")
    count_after = cursor.fetchone()[0]

    print(f"Added {stories_added} Loopio stories")
    print(f"  - {stories_with_docs} stories linked to ibm-bid-library documents")
    print(f"Database now has {count_after} total stories")

    conn.close()
    if bid_library_conn:
        bid_library_conn.close()

    return True


if __name__ == "__main__":
    add_loopio_stories()
