#!/usr/bin/env python3
import argparse
import base64
import json
import logging
import os
import re
import sqlite3
import zipfile
from pathlib import Path
from urllib import request

import pandas as pd

# Import VLM processing utilities from common module
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.vlm_processor import (
    apply_provider_defaults,
    create_vlm_arg_parser,
    create_vlm_client,
    describe_image,
)

XLSX = "all_docs.xlsx"
DB = "../docs.sqlite"
DOCS_DIR = Path("../docs")
IMAGES_DIR = DOCS_DIR / "images"
SUPPORTED_IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = create_vlm_arg_parser("Build docs.sqlite with image descriptions.")
    args = parser.parse_args()
    apply_provider_defaults(args)
    return args


def find_source_path(entry_id: int):
    """Find source document path relative to skill root."""
    filename = f"{entry_id}.docx"
    doc_path = DOCS_DIR / filename

    if doc_path.exists():
        return f"docs/{filename}"
    return None


def has_images(entry_id: int):
    """Check whether the associated docx has embedded images."""
    filename = f"{entry_id}.docx"
    doc_path = DOCS_DIR / filename
    if not doc_path.exists():
        return None
    try:
        with zipfile.ZipFile(doc_path) as zf:
            return any(name.startswith("word/media/") for name in zf.namelist())
    except zipfile.BadZipFile:
        return None


def list_artifact_images(entry_id: int) -> list[Path]:
    artifacts_dir = IMAGES_DIR / f"{entry_id}_artifacts"
    if not artifacts_dir.exists():
        return []
    paths = []
    for path in sorted(artifacts_dir.iterdir()):
        if path.is_file() and path.suffix.lower() in SUPPORTED_IMAGE_EXTS:
            paths.append(path)
    return paths


def build_images_payload(
    entry_id: int,
    client,
    model: str,
    backup_client,
    backup_model: str | None,
    allow_ollama_fallback: bool,
    describe_images_flag: bool,
    db_path: Path,
) -> list[dict]:
    images = []
    db_dir = db_path.parent.resolve()
    for image_path in list_artifact_images(entry_id):
        try:
            rel_path = image_path.resolve().relative_to(db_dir)
            rel_path_str = str(rel_path)
        except ValueError:
            rel_path_str = str(image_path.resolve())
        description = None
        if describe_images_flag:
            try:
                description = describe_image(
                    client,
                    model,
                    image_path,
                    "Describe this document image in 1-2 sentences. Focus on diagrams, tables, or key content.",
                    allow_ollama_fallback,
                )
            except Exception:
                if not backup_client or not backup_model:
                    raise
                logger.warning("Primary model failed; retrying with backup for %s", image_path)
                description = describe_image(
                    backup_client,
                    backup_model,
                    image_path,
                    "Describe this document image in 1-2 sentences. Focus on diagrams, tables, or key content.",
                    allow_ollama_fallback,
                )
        images.append({
            "path": rel_path_str,
            "alt": None,
            "description": description or None,
        })
    return images


def build_images_text(images: list[dict]) -> str | None:
    descriptions = []
    for image in images:
        description = image.get("description")
        if description:
            descriptions.append(description)
    if not descriptions:
        return None
    return "\n".join(descriptions)


def extract_score(answer: str) -> float | None:
    """Extract score value from answer text if present.

    Looks for patterns like "Score: 85", "Score: 85%", "Score:85", etc.
    Returns the numeric score as a float, or None if not found.
    """
    if not answer or not isinstance(answer, str):
        return None

    match = re.search(r"Score:\s*(\d+(?:\.\d+)?)\s*%?", answer, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return None


def main() -> None:
    df = pd.read_excel(XLSX)

    df = df.rename(columns={
        "Library Entry Id": "id",
        "Question *": "question",
        "Answer *": "answer",
        "Sub-Category": "sub_category",
        'Tags (separated by commas ",")': "tags",
        "Library Entry URL": "library_url",
    })

    df["source_path"] = df["id"].apply(find_source_path)
    df["has_images"] = df["id"].apply(has_images)
    df["score"] = df["answer"].apply(extract_score)

    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("DELETE FROM entries_fts;")

    insert_row = """
    INSERT INTO entries_fts (
      rowid, id, question, answer, stack, category, sub_category, tags,
      language, library_url, source_path, has_images, images_text, images, score, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'));
    """

    args = parse_args()
    allow_ollama_fallback = args.provider == "ollama"
    primary_client = create_vlm_client(args.base_url, "lmstudio")
    backup_client = None
    if args.backup_base_url and args.backup_model:
        backup_client = create_vlm_client(args.backup_base_url, "lmstudio")

    db_path = Path(DB).resolve()
    describe_images_flag = not args.disable_descriptions
    inserted = 0

    for _, r in df.iterrows():
        entry_id = int(r["id"])
        entry_id_text = str(entry_id)
        images = build_images_payload(
            entry_id,
            primary_client,
            args.model,
            backup_client,
            args.backup_model,
            allow_ollama_fallback,
            describe_images_flag,
            db_path,
        )
        images_json = json.dumps(images) if images else None
        images_text = build_images_text(images)
        conn.execute(insert_row, (
            entry_id,
            entry_id_text,
            r.get("question"),
            r.get("answer"),
            r.get("Stack"),
            r.get("Category"),
            r.get("sub_category"),
            r.get("tags"),
            r.get("Language"),
            r.get("library_url"),
            r.get("source_path"),
            r.get("has_images"),
            images_text,
            images_json,
            r.get("score"),
        ))
        inserted += 1
        if inserted % 1000 == 0:
            print(f"Processed {inserted} rows...")

    conn.commit()
    conn.close()

    print("Database updated successfully!")
    print(f"Entries inserted: {inserted}")
    print(f"Entries with source documents: {df['source_path'].notna().sum()}")
    print(f"Entries with images: {df['has_images'].fillna(False).sum()}")
    print(f"Entries with extracted scores: {df['score'].notna().sum()}")


if __name__ == "__main__":
    main()