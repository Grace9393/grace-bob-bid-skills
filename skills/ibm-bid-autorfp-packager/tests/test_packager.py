from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path

import yaml

SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT_PATH = SKILL_DIR / "scripts" / "package_autorfp_documents.py"
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

spec = importlib.util.spec_from_file_location("ibm_bid_autorfp_packager", SCRIPT_PATH)
assert spec is not None
packager = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(packager)


def test_build_packaged_document_merges_pack_and_question_data() -> None:
    frontmatter, body = packager.build_packaged_document(
        FIXTURES_DIR / "pack_context.yaml",
        FIXTURES_DIR / "questions" / "service-mobilisation.yaml",
    )

    assert frontmatter["title"] == "Service mobilisation"
    assert frontmatter["word_limit"] == 650
    assert frontmatter["dimensions"]["criteria_alignment"]["weight"] == 0.40
    assert "## Executive summary" in body
    assert frontmatter["ibm_bid"]["enabled"] is True
    assert frontmatter["ibm_bid"]["client_name"] == "Example Client"
    assert (
        frontmatter["ibm_bid"]["policy_snapshot"]["source_skill"]
        == "ibm-bid-writer"
    )
    first_ref = frontmatter["ibm_bid"]["policy_snapshot"]["source_refs"][0]
    expected_hash = hashlib.sha256(
        (FIXTURES_DIR / "policy" / "writing-style-guide.md").read_bytes()
    ).hexdigest()
    assert first_ref["path"] == "policy/writing-style-guide.md"
    assert first_ref["sha256"] == expected_hash
    assert (
        frontmatter["ibm_bid"]["pack_context"]["generated_by_skill"]
        == "ibm-bid-autorfp-packager"
    )
    assert frontmatter["ibm_bid"]["claim_provenance"][0]["claim_id"] == (
        "mobilisation-controls-001"
    )


def test_render_document_emits_yaml_frontmatter() -> None:
    frontmatter, body = packager.build_packaged_document(
        FIXTURES_DIR / "pack_context.yaml",
        FIXTURES_DIR / "questions" / "service-mobilisation.yaml",
    )

    rendered = packager.render_document(frontmatter, body)

    assert rendered.startswith("---\n")
    _, yaml_block, markdown_body = rendered.split("---\n", 2)
    parsed = yaml.safe_load(yaml_block)
    assert parsed["title"] == "Service mobilisation"
    assert parsed["ibm_bid"]["required_headings"] == [
        "Executive summary",
        "Approach",
        "Governance",
        "Evidence",
    ]
    assert "## Governance" in markdown_body
