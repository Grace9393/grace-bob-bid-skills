from __future__ import annotations

import importlib.util
from pathlib import Path

import yaml

SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT_PATH = SKILL_DIR / "scripts" / "collect_autorfp_inputs_from_tmp.py"
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

spec = importlib.util.spec_from_file_location("collect_autorfp_inputs_from_tmp", SCRIPT_PATH)
assert spec is not None
collector = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(collector)


def test_collect_inputs_generates_pack_context_and_question_files(tmp_path: Path) -> None:
    payload = collector.collect_inputs(
        tmp_dir=(FIXTURES_DIR / "tmp_workflow").resolve(),
        output_dir=tmp_path / "inputs",
        package_output_dir=None,
        validate_script=None,
        ibm=False,
        overwrite=False,
    )

    pack_context = yaml.safe_load((tmp_path / "inputs" / "pack-context.yaml").read_text())
    question_file = yaml.safe_load(Path(payload["question_files"][0]).read_text())

    assert pack_context["client_name"] == "Example Client"
    assert pack_context["win_themes"][0].startswith("IBM reduces mobilisation risk")
    assert question_file["question_reference"] == "Q01"
    assert question_file["question"] == "Describe your service mobilisation approach."
    assert question_file["named_mechanisms"] == [
        "Transition Control Tower",
        "Mobilisation Design Authority",
    ]
    assert "## Approach" in question_file["draft_body"]

