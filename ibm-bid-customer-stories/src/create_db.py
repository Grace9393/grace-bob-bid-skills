#!/usr/bin/env python3
"""
Create SQLite FTS5 database from customer stories CSV file.
"""

import sqlite3
import csv
import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
SKILL_DIR = SCRIPT_DIR.parent
CSV_FILE = SKILL_DIR / "customer_stories_matrix.csv"
DB_FILE = SKILL_DIR / "stories.sqlite"
SQL_SCHEMA_FILE = SCRIPT_DIR / "db.sql"


def create_database():
    """Create the SQLite FTS5 database from CSV."""

    if not CSV_FILE.exists():
        print(f"Error: CSV file not found at {CSV_FILE}")
        return False

    if DB_FILE.exists():
        os.remove(DB_FILE)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    with open(SQL_SCHEMA_FILE, 'r') as f:
        cursor.executescript(f.read())

    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        cursor.executemany(
            "INSERT INTO stories_fts(title, company, industry, clouds_implemented, description, outcomes, source, links) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            [(row.get('Title', ''), row.get('Company', ''), row.get('Industry', ''),
              row.get('Clouds Implemented', ''), row.get('Description', ''),
              row.get('Outcomes', ''), 'Salesforce', row.get('Links', '')) for row in reader]
        )

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM stories_fts")
    count = cursor.fetchone()[0]
    print(f"Created {DB_FILE.name} with {count} stories")

    conn.close()
    return True


if __name__ == "__main__":
    create_database()