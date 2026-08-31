#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
from pathlib import Path
from typing import Any

import yaml


def slugify(value: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", value.casefold(), flags=re.UNICODE)
    slug = re.sub(r"[-\s]+", "-", slug, flags=re.UNICODE).strip("-")
    return slug or "untitled"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False), encoding="utf-8")


def find_single(patterns: list[str], tmp_dir: Path) -> Path | None:
    for pattern in patterns:
        matches = sorted(tmp_dir.glob(pattern))
        if matches:
            return matches[0]
    return None


def find_all(patterns: list[str], tmp_dir: Path) -> list[Path]:
    results: list[Path] = []
    for pattern in patterns:
        results.extend(sorted(tmp_dir.glob(pattern)))
    seen: set[Path] = set()
    deduped: list[Path] = []
    for path in results:
        if path not in seen:
            deduped.append(path)
            seen.add(path)
    return deduped


def markdown_section(text: str, heading: str, level_pattern: str = r"##+") -> str | None:
    pattern = rf"(?ms)^{level_pattern}\s+{re.escape(heading)}\s*\n(.*?)(?=^{level_pattern}\s+|\Z)"
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    return None


def markdown_subsection(text: str, heading: str) -> str | None:
    pattern = rf"(?ms)^###\s+{re.escape(heading)}\s*\n(.*?)(?=^###\s+|^##\s+|\Z)"
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    return None


def parse_field(text: str, label: str) -> str | None:
    match = re.search(rf"(?m)^\*\*{re.escape(label)}:\*\*\s*(.+)$", text)
    if match:
        return match.group(1).strip()
    return None


def normalize_question_reference(value: str) -> str:
    match = re.search(r"Q0*(\d+)", value, flags=re.IGNORECASE)
    if not match:
        return value.strip()
    return f"Q{int(match.group(1)):02d}"


def parse_project_state(path: Path) -> dict[str, Any]:
    text = read_text(path)
    source_documents: list[dict[str, str | None]] = []
    for match in re.finditer(r"(?m)^\d+\.\s+\*\*(.+?)\*\*\s*$", text):
        raw_path = match.group(1).strip()
        path_obj = Path(raw_path)
        if not path_obj.is_absolute():
            candidates = [
                (path.parent / raw_path).resolve(),
                (path.parent.parent / raw_path).resolve(),
                (Path.cwd() / raw_path).resolve(),
            ]
            existing = next((candidate for candidate in candidates if candidate.exists()), None)
            path_obj = existing or candidates[-1]
        source_documents.append(
            {
                "kind": "source",
                "title": Path(raw_path).name,
                "location": str(path_obj),
                "notes": None,
            }
        )
    return {
        "tender_name": parse_field(text, "Tender Name"),
        "client": parse_field(text, "Client"),
        "tender_type": parse_field(text, "Tender Type"),
        "source_documents": source_documents,
    }


def parse_requirements_analysis(path: Path) -> dict[str, Any]:
    text = read_text(path)
    client_profile = markdown_subsection(text, "Client Profile") or ""
    stated_requirements = markdown_subsection(text, "Stated Requirements") or ""
    evaluation_section = markdown_subsection(text, "Evaluation Criteria") or ""
    executive_summary = markdown_section(text, "EXECUTIVE SUMMARY") or ""
    return {
        "executive_summary": executive_summary,
        "client_profile": client_profile,
        "stated_requirements": stated_requirements,
        "evaluation": evaluation_section,
    }


def parse_strategic_positioning(path: Path) -> dict[str, Any]:
    text = read_text(path)
    executive_summary = markdown_section(text, "EXECUTIVE SUMMARY") or ""
    sales_strategy = markdown_section(text, "SALES STRATEGY RECOMMENDATION") or ""
    price_to_win = markdown_section(text, "PRICE TO WIN ANALYSIS") or ""
    return {
        "executive_summary": executive_summary,
        "sales_strategy": sales_strategy,
        "price_to_win": price_to_win,
    }


def parse_hot_buttons(path: Path) -> list[str]:
    text = read_text(path)
    buttons = re.findall(r"(?m)^\*\*Hot Button\*\*:\s*[\"“]?(.+?)[\"”]?\s*$", text)
    return [item.strip() for item in buttons]


def parse_win_themes(path: Path) -> tuple[list[str], list[str]]:
    text = read_text(path)
    themes = re.findall(r"(?m)^THEME:\s*(.+)$", text)
    proofs = re.findall(r"(?m)^\s*-\s+(.+)$", text)
    if not themes:
        primary = re.findall(r'(?m)^\*\*Primary\*\*:\s*"(.+)"\s*$', text)
        supporting = re.findall(r'(?m)^\s*-\s+[A-Za-z ]+:\s*"(.+)"\s*$', text)
        themes = primary + supporting
    return ([item.strip() for item in themes], [item.strip() for item in proofs])


def parse_scoring_matrix_question(path: Path, question_reference: str) -> dict[str, Any] | None:
    text = read_text(path)
    normalized_ref = normalize_question_reference(question_reference)
    for match in re.finditer(r"(?m)^\|\s*(Q\d+)\s*\|\s*(.+?)\s*\|\s*([0-9.]+)%?\s*\|", text):
        row_ref = normalize_question_reference(match.group(1))
        if row_ref == normalized_ref:
            weight = float(match.group(3)) / 100.0
            description = match.group(2).strip()
            return {
                "question": description,
                "criteria": [
                    {
                        "id": slugify(description),
                        "description": description,
                        "weight": weight,
                    }
                ],
            }
    return None


def parse_plan(path: Path) -> dict[str, Any]:
    text = read_text(path)
    sections = {}
    current_heading: str | None = None
    current_lines: list[str] = []
    for line in text.splitlines():
        heading_match = re.match(r"^##\s+(.+)$", line)
        if heading_match:
            if current_heading is not None:
                sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = heading_match.group(1).strip()
            current_lines = []
            continue
        if current_heading is not None:
            current_lines.append(line)
    if current_heading is not None:
        sections[current_heading] = "\n".join(current_lines).strip()

    def bullet_value(section: str, label: str) -> str | None:
        content = sections.get(section, "")
        match = re.search(rf"(?m)^-\s+{re.escape(label)}:\s*(.+)$", content)
        if match:
            return match.group(1).strip()
        return None

    def repeated_values(section: str, prefix: str) -> list[str]:
        content = sections.get(section, "")
        values = re.findall(rf"(?m)^-\s+{re.escape(prefix)}\s*\d*:\s*(.+)$", content)
        return [value.strip() for value in values if value.strip() and value.strip() != "-"]

    confidence_case_parts = [
        bullet_value("Confidence Case", "One-sentence confidence opener"),
        bullet_value("Confidence Case", "Why IBM is credible on this topic now"),
    ]
    confidence_case = "\n".join(part for part in confidence_case_parts if part)

    return {
        "question_reference": bullet_value("Question", "Reference"),
        "question": bullet_value("Question", "Raw question or summary"),
        "evaluator_concern": bullet_value("Evaluator Concern", "Primary concern"),
        "secondary_concerns": repeated_values("Evaluator Concern", "Secondary concerns"),
        "confidence_heading": bullet_value("Confidence Summary Section", "Proposed heading"),
        "confidence_bullets": repeated_values("Confidence Summary Section", "Preview bullet"),
        "confidence_case": confidence_case or None,
        "named_mechanisms": repeated_values("Named Mechanisms", "Mechanism"),
        "repeated_bid_themes": repeated_values("Repeated Bid Themes", "Theme"),
        "response_archetype": bullet_value("Draft Shape", "Recommended response archetype"),
        "phrases_to_mirror": repeated_values("Draft Reminders", "Phrases or terminology to mirror"),
    }


def parse_response_body(path: Path) -> tuple[str, list[str], str]:
    text = read_text(path).strip()
    title_match = re.search(r"(?m)^#\s+(.+)$", text)
    if title_match:
        title = title_match.group(1).strip()
    else:
        title = re.sub(r"(?i)^Q\d+[_-]?", "", path.stem).replace("_", " ").replace("-", " ").strip()
        title = title[:1].upper() + title[1:] if title else path.stem
    headings = re.findall(r"(?m)^##\s+(.+)$", text)
    return text + "\n", headings, title


def default_policy_snapshot(repo_root: Path) -> tuple[list[dict[str, str]], dict[str, Any]]:
    writer_ref_paths = [
        repo_root / "skills/ibm-bid-writer/references/writing-style-guide.md",
        repo_root / "skills/ibm-bid-writer/references/quality-checklist.md",
        repo_root / "skills/ibm-bid-writer/references/pre-draft-planning-template.md",
    ]
    refs = [
        {
            "path": str(path.resolve()),
            "sha256": sha256_file(path),
        }
        for path in writer_ref_paths
        if path.exists()
    ]
    snapshot = {
        "source_skill": "ibm-bid-writer",
        "style_rules": {
            "tone": "Formal, evaluator-facing, British English",
            "avoid_generic_marketing_language": True,
            "use_will_for_supported_commitments": True,
            "prefer_named_mechanisms_over_adjectives": True,
        },
        "structure_rules": {
            "mirror_buyer_numbering": True,
            "preferred_sequence": ["promise", "mechanism", "proof", "buyer_protection"],
            "confidence_section_policy": "required_if_substantial",
            "preserve_required_headings": True,
        },
        "evidence_rules": {
            "evidence_priority": [
                "account_specific_evidence",
                "named_team_credibility",
                "public_sector_precedent",
                "broader_capability_proof",
            ],
            "require_named_mechanisms": True,
            "require_quantified_outcomes_where_available": True,
            "require_source_provenance_for_claims": True,
        },
        "rewrite_guardrails": {
            "preserve_named_mechanisms": True,
            "preserve_repeated_bid_themes": True,
            "preserve_banned_claims_list": True,
            "do_not_weaken_supported_commitments": True,
            "preserve_british_english": True,
        },
    }
    return refs, snapshot


def build_pack_context(tmp_dir: Path, repo_root: Path) -> tuple[dict[str, Any], list[str]]:
    warnings: list[str] = []
    project_path = find_single(["ibm-bid-project.md"], tmp_dir)
    requirements_path = find_single(["ibm-bid-requirements-analysis.md"], tmp_dir)
    strategic_path = find_single(["ibm-bid-strategic-positioning.md"], tmp_dir)
    hot_buttons_path = find_single(["ibm-bid-hot-buttons.md"], tmp_dir)
    win_themes_path = find_single(["ibm-bid-win-themes.md"], tmp_dir)

    if requirements_path is None:
        raise FileNotFoundError("Missing tmp/ibm-bid-requirements-analysis.md")

    project = parse_project_state(project_path) if project_path else {}
    requirements = parse_requirements_analysis(requirements_path)
    strategic = parse_strategic_positioning(strategic_path) if strategic_path else {}
    hot_buttons = parse_hot_buttons(hot_buttons_path) if hot_buttons_path else []
    win_themes, proofs = parse_win_themes(win_themes_path) if win_themes_path else ([], [])

    if project_path is None:
        warnings.append("Missing ibm-bid-project.md; source document provenance is limited.")
    if strategic_path is None:
        warnings.append("Missing ibm-bid-strategic-positioning.md; strategic messaging will be sparse.")
    if hot_buttons_path is None:
        warnings.append("Missing ibm-bid-hot-buttons.md; hot_buttons will be empty.")
    if win_themes_path is None:
        warnings.append("Missing ibm-bid-win-themes.md; win_themes will be empty.")

    policy_refs, policy_defaults = default_policy_snapshot(repo_root)
    client_context_parts = [
        requirements.get("executive_summary", ""),
        requirements.get("client_profile", ""),
        strategic.get("executive_summary", ""),
    ]
    client_context = "\n\n".join(part for part in client_context_parts if part).strip()

    tender_name = project.get("tender_name") or project.get("client") or "ibm-bid-pack"
    pack_context = {
        "pack_id": slugify(str(tender_name)),
        "pack_version": "1",
        "client_name": project.get("client"),
        "proposal_name": project.get("tender_name"),
        "opportunity_name": project.get("tender_name"),
        "client_context": client_context or None,
        "hot_buttons": hot_buttons,
        "win_themes": win_themes,
        "proposal_principles": ["Buyer protection first", "Evidence before assertion"],
        "approved_proof_points": proofs,
        "banned_claims": ["Best in class", "Market leading"],
        "preferred_structure": ["Executive summary", "Approach", "Evidence"],
        "dimensions": {
            "word_count": {"enabled": True, "weight": 0.10},
            "factual_accuracy": {"enabled": True, "weight": 0.25},
            "criteria_alignment": {"enabled": True, "weight": 0.40},
            "question_coverage": {"enabled": True, "weight": 0.25},
        },
        "optimization": {
            "model": "openai/gpt-oss-20b",
            "max_iterations": 3,
            "convergence_threshold": 0.02,
            "temperature": 0.7,
            "max_tokens": 1024,
        },
        "policy_source_refs": policy_refs,
        "policy_defaults": policy_defaults,
        "source_documents": project.get("source_documents", []),
    }
    return pack_context, warnings


def load_packager_module(skill_dir: Path):
    package_script = skill_dir / "scripts" / "package_autorfp_documents.py"
    spec = importlib.util.spec_from_file_location("package_autorfp_documents", package_script)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {package_script}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_question_file(
    response_path: Path,
    tmp_dir: Path,
    project_state: dict[str, Any],
    pack_context: dict[str, Any],
    warnings: list[str],
) -> dict[str, Any]:
    body, body_headings, inferred_title = parse_response_body(response_path)
    qref_match = re.search(r"(Q\d+)", response_path.name, flags=re.IGNORECASE)
    if not qref_match:
        raise ValueError(f"Could not infer question reference from {response_path.name}")
    question_reference = normalize_question_reference(qref_match.group(1))

    plan_candidates = [
        response_path.parent / f"{question_reference}_plan.md",
        tmp_dir / "ibm-bid-response-plan.md",
    ]
    plan_path = next((path for path in plan_candidates if path.exists()), None)
    wireframe_candidates = [
        tmp_dir / f"ibm-bid-wireframe-{question_reference}.md",
        tmp_dir / f"{question_reference.lower()}_wireframe.md",
    ]
    wireframe_path = next((path for path in wireframe_candidates if path.exists()), None)

    plan = parse_plan(plan_path) if plan_path else {}
    if plan_path is None:
        warnings.append(f"Missing plan for {question_reference}; using fallbacks.")

    scoring_hint: dict[str, Any] | None = None
    for item in project_state.get("source_documents", []):
        location = item.get("location")
        if not location:
            continue
        path = Path(location)
        if path.exists() and "scoring" in path.name.casefold():
            scoring_hint = parse_scoring_matrix_question(path, question_reference)
            if scoring_hint is not None:
                break

    title = inferred_title or (scoring_hint or {}).get("question") or question_reference
    question_text = plan.get("question") or (scoring_hint or {}).get("question")
    if question_text is None:
        question_text = title
        warnings.append(f"Missing raw question for {question_reference}; using title as question text.")

    criteria = (scoring_hint or {}).get("criteria", [])
    if not criteria:
        criteria = [
            {
                "id": slugify(title),
                "description": title,
                "weight": 1.0,
            }
        ]
        warnings.append(f"Missing explicit criteria for {question_reference}; using a single fallback criterion.")

    required_headings = body_headings
    if not required_headings and wireframe_path and wireframe_path.exists():
        wireframe_text = read_text(wireframe_path)
        required_headings = [item.strip() for item in re.findall(r"(?m)^-\s+(.+)$", wireframe_text)]

    question_record = {
        "question_reference": question_reference,
        "title": title,
        "question": question_text,
        "word_limit": 750,
        "criteria": criteria,
        "draft_body": body,
        "evaluator_concern": plan.get("evaluator_concern"),
        "secondary_concerns": plan.get("secondary_concerns", []),
        "confidence_case": plan.get("confidence_case"),
        "confidence_heading": plan.get("confidence_heading") or "Why you should have full confidence in our proposal",
        "confidence_bullets": plan.get("confidence_bullets", []),
        "named_mechanisms": plan.get("named_mechanisms", []),
        "repeated_bid_themes": plan.get("repeated_bid_themes") or pack_context.get("win_themes", []),
        "response_archetype": plan.get("response_archetype"),
        "required_headings": required_headings,
        "phrases_to_mirror": plan.get("phrases_to_mirror", []),
    }
    return question_record


def collect_inputs(
    tmp_dir: Path,
    output_dir: Path,
    package_output_dir: Path | None,
    validate_script: Path | None,
    ibm: bool,
    overwrite: bool,
) -> dict[str, Any]:
    repo_root = Path(__file__).resolve().parents[5]
    project_path = find_single(["ibm-bid-project.md"], tmp_dir)
    project_state = parse_project_state(project_path) if project_path else {}
    pack_context, warnings = build_pack_context(tmp_dir, repo_root)

    questions_output_dir = output_dir / "questions"
    output_dir.mkdir(parents=True, exist_ok=True)
    write_yaml(output_dir / "pack-context.yaml", pack_context)

    response_paths = find_all(["ibm-bid-responses/Q*.md"], tmp_dir)
    response_paths = [path for path in response_paths if "_plan" not in path.stem.casefold()]
    if not response_paths:
        raise FileNotFoundError("No response files found under tmp/ibm-bid-responses/")

    generated_questions: list[str] = []
    packaged_outputs: list[dict[str, Any]] = []

    packager = load_packager_module(Path(__file__).resolve().parents[1]) if package_output_dir else None
    for response_path in response_paths:
        question_record = build_question_file(response_path, tmp_dir, project_state, pack_context, warnings)
        question_path = questions_output_dir / f"{normalize_question_reference(question_record['question_reference']).lower()}.yaml"
        if question_path.exists() and not overwrite:
            raise FileExistsError(f"{question_path} already exists; pass --overwrite")
        write_yaml(question_path, question_record)
        generated_questions.append(str(question_path))

        if package_output_dir is not None and packager is not None:
            packaged_outputs.append(
                packager.package_question_file(
                    pack_context_path=(output_dir / "pack-context.yaml").resolve(),
                    question_path=question_path.resolve(),
                    output_dir=package_output_dir.resolve(),
                    overwrite=overwrite,
                    validate_script=validate_script.resolve() if validate_script is not None else None,
                    ibm=ibm,
                )
            )

    return {
        "pack_context": str((output_dir / "pack-context.yaml").resolve()),
        "question_files": generated_questions,
        "warnings": warnings,
        "packaged_outputs": packaged_outputs,
    }


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Collect standard IBM bid tmp artifacts into pack-context and per-question AutoRFP input files."
    )
    parser.add_argument("--tmp-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--package-output-dir", type=Path)
    parser.add_argument("--validate-script", type=Path)
    parser.add_argument("--ibm", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()
    try:
        payload = collect_inputs(
            tmp_dir=args.tmp_dir.resolve(),
            output_dir=args.output_dir.resolve(),
            package_output_dir=args.package_output_dir.resolve() if args.package_output_dir else None,
            validate_script=args.validate_script.resolve() if args.validate_script else None,
            ibm=args.ibm,
            overwrite=args.overwrite,
        )
        exit_code = 0
    except Exception as error:
        payload = {
            "error": {
                "type": error.__class__.__name__,
                "message": str(error),
            }
        }
        exit_code = 1

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        if exit_code == 0:
            print(f"PACK CONTEXT {payload['pack_context']}")
            for path in payload["question_files"]:
                print(f"QUESTION {path}")
            for warning in payload["warnings"]:
                print(f"WARN {warning}")
        else:
            print(f"ERROR {payload['error']['type']}: {payload['error']['message']}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
