from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_DIR / "scripts" / "package_autorfp_documents.py"
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
VALIDATE_SCRIPT = (
    Path("/Users/telcott/tmp/code/autorfp/scripts/validate_document.py").resolve()
)


def test_script_packages_and_validates_document(tmp_path: Path) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--pack-context",
            str(FIXTURES_DIR / "pack_context.yaml"),
            "--question",
            str(FIXTURES_DIR / "questions" / "service-mobilisation.yaml"),
            "--output-dir",
            str(tmp_path),
            "--validate-script",
            str(VALIDATE_SCRIPT),
            "--ibm",
            "--json",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0
    payload = json.loads(completed.stdout)
    assert payload["errors"] == []
    assert len(payload["generated"]) == 1
    generated = payload["generated"][0]
    assert generated["validation"]["valid"] is True
    output_path = Path(generated["output_path"])
    assert output_path.exists()


def test_script_reports_missing_required_field(tmp_path: Path) -> None:
    invalid_question = tmp_path / "invalid-question.yaml"
    invalid_question.write_text(
        yaml.safe_dump(
            {
                "question_reference": "Q9",
                "question": "Broken",
                "word_limit": 100,
                "draft_body": "Broken",
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--pack-context",
            str(FIXTURES_DIR / "pack_context.yaml"),
            "--question",
            str(invalid_question),
            "--output-dir",
            str(tmp_path / "out"),
            "--json",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 1
    payload = json.loads(completed.stdout)
    assert payload["generated"] == []
    assert payload["errors"][0]["type"] == "ValueError"
    assert "title" in payload["errors"][0]["message"]
