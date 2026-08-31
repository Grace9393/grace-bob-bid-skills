#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


class LiteralDumper(yaml.SafeDumper):
    pass


def _present_str(dumper: yaml.SafeDumper, data: str) -> yaml.nodes.ScalarNode:
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


LiteralDumper.add_representer(str, _present_str)

IBM_BID_FIELDS = (
    "client_name",
    "proposal_name",
    "opportunity_name",
    "question_reference",
    "client_context",
    "hot_buttons",
    "win_themes",
    "proposal_principles",
    "approved_proof_points",
    "banned_claims",
    "preferred_structure",
    "evaluator_concern",
    "secondary_concerns",
    "confidence_case",
    "confidence_heading",
    "confidence_bullets",
    "named_mechanisms",
    "repeated_bid_themes",
    "evidence_stack",
    "response_archetype",
    "required_headings",
    "phrases_to_mirror",
    "source_documents",
    "policy_snapshot",
    "pack_context",
    "claim_provenance",
)


def slugify(value: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", value.casefold(), flags=re.UNICODE)
    slug = re.sub(r"[-\s]+", "-", slug, flags=re.UNICODE).strip("-")
    return slug or "untitled"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_mapping(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        payload = json.loads(text)
    else:
        payload = yaml.safe_load(text)
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain a top-level mapping")
    return payload


def deep_merge(base: Any, override: Any) -> Any:
    if isinstance(base, dict) and isinstance(override, dict):
        merged = {key: deepcopy(value) for key, value in base.items()}
        for key, value in override.items():
            if key in merged:
                merged[key] = deep_merge(merged[key], value)
            else:
                merged[key] = deepcopy(value)
        return merged
    return deepcopy(override)


def resolve_input_path(path_value: str, base_dir: Path) -> Path:
    candidate = Path(path_value)
    if not candidate.is_absolute():
        candidate = (base_dir / candidate).resolve()
    return candidate


def normalize_policy_source_refs(
    raw_refs: list[Any],
    base_dir: Path,
) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    for item in raw_refs:
        if isinstance(item, str):
            declared_path = item
            item_sha = None
        elif isinstance(item, dict):
            declared_path = item.get("path")
            item_sha = item.get("sha256")
        else:
            raise ValueError("policy_source_refs entries must be strings or mappings")
        if not declared_path:
            raise ValueError("policy_source_refs entries must include a path")
        resolved_path = resolve_input_path(str(declared_path), base_dir)
        if not resolved_path.exists():
            raise FileNotFoundError(
                f"policy source reference does not exist: {resolved_path}"
            )
        normalized.append(
            {
                "path": str(declared_path),
                "sha256": item_sha or sha256_file(resolved_path),
            }
        )
    return normalized


def build_policy_snapshot(
    merged: dict[str, Any],
    pack_context_path: Path,
) -> dict[str, Any]:
    policy_snapshot = deep_merge(
        merged.get("policy_defaults", {}),
        merged.get("policy_snapshot", {}),
    )
    raw_refs = policy_snapshot.get("source_refs")
    if not raw_refs:
        raw_refs = merged.get("policy_source_refs", [])
    policy_snapshot["source_refs"] = normalize_policy_source_refs(
        raw_refs,
        pack_context_path.parent,
    )
    policy_snapshot.setdefault("source_skill", "ibm-bid-writer")
    policy_snapshot.setdefault("generated_at", utc_now_iso())
    return policy_snapshot


def build_pack_context(
    merged: dict[str, Any],
    pack_context_path: Path,
) -> dict[str, Any]:
    generated = {
        "pack_id": merged.get("pack_id"),
        "pack_version": merged.get("pack_version"),
        "pack_source_path": str(pack_context_path.resolve()),
        "pack_source_sha256": sha256_file(pack_context_path),
        "generated_by_skill": "ibm-bid-autorfp-packager",
        "generated_at": utc_now_iso(),
    }
    return deep_merge(generated, merged.get("pack_context", {}))


def build_ibm_bid(
    merged: dict[str, Any],
    pack_context_path: Path,
) -> dict[str, Any]:
    ibm_bid: dict[str, Any] = {"enabled": True}
    for field in IBM_BID_FIELDS:
        if field == "policy_snapshot":
            ibm_bid[field] = build_policy_snapshot(merged, pack_context_path)
            continue
        if field == "pack_context":
            ibm_bid[field] = build_pack_context(merged, pack_context_path)
            continue
        if field in merged and merged[field] is not None:
            ibm_bid[field] = deepcopy(merged[field])
    return ibm_bid


def build_packaged_document(
    pack_context_path: Path,
    question_path: Path,
) -> tuple[dict[str, Any], str]:
    pack_context = load_mapping(pack_context_path)
    question_payload = load_mapping(question_path)
    merged = deep_merge(pack_context, question_payload)

    required = ("title", "question", "word_limit", "dimensions", "optimization")
    missing = [field for field in required if not merged.get(field)]
    if missing:
        missing_text = ", ".join(missing)
        raise ValueError(f"{question_path} is missing required field(s): {missing_text}")

    body = merged.get("draft_body") or merged.get("body")
    if not isinstance(body, str) or not body.strip():
        raise ValueError(f"{question_path} must include a non-empty draft_body")

    frontmatter: dict[str, Any] = {
        "title": merged["title"],
        "question": merged["question"],
        "word_limit": merged["word_limit"],
        "dimensions": merged["dimensions"],
        "optimization": merged["optimization"],
        "ibm_bid": build_ibm_bid(merged, pack_context_path),
    }
    if merged.get("slug"):
        frontmatter["slug"] = merged["slug"]
    if "criteria" in merged:
        frontmatter["criteria"] = merged["criteria"]
    if merged.get("factual_context") is not None:
        frontmatter["factual_context"] = merged["factual_context"]
    return frontmatter, body.rstrip() + "\n"


def render_document(frontmatter: dict[str, Any], body: str) -> str:
    yaml_text = yaml.dump(
        frontmatter,
        Dumper=LiteralDumper,
        sort_keys=False,
        allow_unicode=False,
        width=88,
    ).strip()
    return f"---\n{yaml_text}\n---\n\n{body}"


def validate_output(
    document_path: Path,
    validate_script: Path,
    ibm: bool,
) -> dict[str, Any]:
    repo_python = validate_script.resolve().parents[1] / ".venv" / "bin" / "python"
    interpreter = repo_python if repo_python.exists() else Path(sys.executable)
    command = [str(interpreter), str(validate_script), "--json"]
    if ibm:
        command.append("--ibm")
    command.append(str(document_path))
    completed = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False,
    )
    payload = json.loads(completed.stdout)
    if completed.returncode != 0:
        raise ValueError(json.dumps(payload, sort_keys=True))
    return payload


def collect_question_paths(question_paths: list[Path], questions_dir: Path | None) -> list[Path]:
    if question_paths:
        return sorted(path.resolve() for path in question_paths)
    if questions_dir is None:
        raise ValueError("either --question or --questions-dir is required")
    candidates = sorted(
        path.resolve()
        for path in questions_dir.iterdir()
        if path.suffix.lower() in {".yaml", ".yml", ".json"}
    )
    if not candidates:
        raise ValueError(f"no YAML/JSON question files found in {questions_dir}")
    return candidates


def package_question_file(
    pack_context_path: Path,
    question_path: Path,
    output_dir: Path,
    overwrite: bool,
    validate_script: Path | None,
    ibm: bool,
) -> dict[str, Any]:
    frontmatter, body = build_packaged_document(pack_context_path, question_path)
    slug = frontmatter.get("slug") or slugify(str(frontmatter["title"]))
    output_path = output_dir / f"{slug}.md"
    if output_path.exists() and not overwrite:
        raise FileExistsError(f"{output_path} already exists; pass --overwrite")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_document(frontmatter, body), encoding="utf-8")
    result: dict[str, Any] = {
        "question_path": str(question_path),
        "output_path": str(output_path),
        "slug": slug,
        "title": frontmatter["title"],
    }
    if validate_script is not None:
        result["validation"] = validate_output(output_path, validate_script, ibm)
    return result


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Package IBM bid answer-intent files into AutoRFP markdown documents."
    )
    parser.add_argument("--pack-context", required=True, type=Path)
    parser.add_argument("--question", action="append", type=Path, default=[])
    parser.add_argument("--questions-dir", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--validate-script", type=Path)
    parser.add_argument("--ibm", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()
    payload: dict[str, Any] = {"generated": [], "errors": []}
    try:
        question_paths = collect_question_paths(args.question, args.questions_dir)
        for question_path in question_paths:
            try:
                result = package_question_file(
                    pack_context_path=args.pack_context.resolve(),
                    question_path=question_path,
                    output_dir=args.output_dir.resolve(),
                    overwrite=args.overwrite,
                    validate_script=args.validate_script.resolve()
                    if args.validate_script is not None
                    else None,
                    ibm=args.ibm,
                )
                payload["generated"].append(result)
            except Exception as error:
                payload["errors"].append(
                    {
                        "question_path": str(question_path),
                        "message": str(error),
                        "type": error.__class__.__name__,
                    }
                )
    except Exception as error:
        payload["errors"].append(
            {
                "question_path": None,
                "message": str(error),
                "type": error.__class__.__name__,
            }
        )

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        for item in payload["generated"]:
            print(f"PACKAGED {item['output_path']}")
        for item in payload["errors"]:
            location = item["question_path"] or "<startup>"
            print(f"ERROR {location}: {item['message']}")
    return 0 if not payload["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
