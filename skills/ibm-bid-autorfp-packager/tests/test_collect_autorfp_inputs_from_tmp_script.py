from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_DIR / "scripts" / "collect_autorfp_inputs_from_tmp.py"
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
VALIDATE_SCRIPT = (
    Path("/Users/telcott/tmp/code/autorfp/scripts/validate_document.py").resolve()
)


def test_script_collects_and_packages_from_tmp(tmp_path: Path) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--tmp-dir",
            str(FIXTURES_DIR / "tmp_workflow"),
            "--output-dir",
            str(tmp_path / "inputs"),
            "--package-output-dir",
            str(tmp_path / "packaged"),
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
    assert payload["packaged_outputs"][0]["validation"]["valid"] is True
    assert payload["question_files"]
