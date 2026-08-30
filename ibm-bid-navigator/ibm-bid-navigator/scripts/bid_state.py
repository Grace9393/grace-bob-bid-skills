#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "PyYAML>=6.0.0",
# ]
# ///
from __future__ import annotations

import json
import os
import sqlite3
import sys
from datetime import UTC, datetime
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
ENGINE_SCRIPT_DIR = SKILL_DIR.parent / "agent-state-engine" / "scripts"
PROFILE_CONFIG = SKILL_DIR / "assets" / "profile.yaml"
DEFAULT_DB = Path.cwd() / "tmp" / "ibm-bid-project.sqlite"

sys.path.insert(0, str(ENGINE_SCRIPT_DIR))

from agent_state.cli import create_work, event, link_work_items, main as engine_main, transaction, utc_now  # noqa: E402


PHASES = [
    {
        "key": "phase_0_opportunity_assessment",
        "title": "Phase 0: Opportunity Assessment",
        "phase": "opportunity_assessment",
        "children": [
            ("Requirements Analysis", "requirement", "requirements_analysis", "ibm-bid-requirements-analysis"),
            ("Strategic Positioning", "skill_task", "strategic_positioning", "ibm-bid-strategic-positioning"),
            ("Qualification Assessment", "skill_task", "qualification_assessment", "ibm-bid-qualification"),
            ("Legal Assessment", "skill_task", "legal_assessment", "ibm-bid-legal-assessment"),
            ("Competitor Analysis", "skill_task", "competitor_analysis", "ibm-bid-competitor-analysis"),
            ("Clarifications", "skill_task", "clarifications", "ibm-bid-clarifications"),
        ],
    },
    {
        "key": "phase_1_positioning",
        "title": "Phase 1: Positioning",
        "phase": "strategic_positioning",
        "children": [
            ("Hot Buttons Extraction", "skill_task", "hot_buttons", "ibm-bid-hot-buttons"),
            ("Client Language Analysis", "skill_task", "client_language_analysis", "ibm-bid-client-language-analysis"),
            ("Win Themes", "skill_task", "win_themes", "ibm-bid-win-themes"),
            ("Offerings Advisor", "skill_task", "offerings_advisor", "ibm-bid-offerings-advisor"),
            ("Executive Summary", "answer", "executive_summary", "ibm-bid-executive-summary"),
            ("Customer Stories Shortlist", "skill_task", "customer_stories", "ibm-bid-customer-stories"),
        ],
    },
    {
        "key": "phase_2_solution_commercials",
        "title": "Phase 2: Solution, Scope, Staffing, and Commercials",
        "phase": "solution_architecture",
        "children": [
            ("Solution Architecture", "skill_task", "solution_architecture", "ibm-bid-solution-architect"),
            ("Scope Boundaries", "skill_task", "scope_boundaries", "ibm-bid-scope-constrainer"),
            ("Staffing Plan", "skill_task", "staffing_plan", "ibm-bid-staffing-planner"),
            ("Pricing Strategy", "skill_task", "pricing_strategy", "ibm-bid-pricing-strategy"),
        ],
    },
    {
        "key": "phase_3_content_development",
        "title": "Phase 3: Content Development",
        "phase": "content_development",
        "children": [
            ("Wireframe Creation", "skill_task", "wireframe_creation", "ibm-bid-wireframe-creator"),
            ("Answer Drafting", "answer", "answer_drafting", "ibm-bid-writer"),
            ("Social Value Response", "answer", "social_value_response", "ibm-bid-social-value-expert"),
            ("Answer Evaluation", "review", "answer_evaluation", "ibm-bid-answer-evaluator"),
        ],
    },
    {
        "key": "phase_4_technical_assurance",
        "title": "Phase 4: Technical Assurance",
        "phase": "technical_assurance",
        "children": [
            ("TDA Review", "review", "tda_review", "ibm-bid-tda-review"),
            ("Fact Check and Source Validation", "review", "fact_check", "ibm-bid-fact-checker"),
            ("Final Evaluation", "review", "final_evaluation", "ibm-bid-answer-evaluator"),
            ("AutoRFP Packaging", "skill_task", "autorfp_packaging", "ibm-bid-autorfp-packager"),
        ],
    },
]


def db_path_from_args(argv: list[str]) -> Path:
    if "--db" not in argv:
        return DEFAULT_DB
    index = argv.index("--db")
    if index + 1 >= len(argv):
        return DEFAULT_DB
    return Path(argv[index + 1])


def list_assets(argv: list[str]) -> int:
    db_path = db_path_from_args(argv)
    as_json = "--json" in argv
    if not db_path.exists():
        print(f"No bid state database found at {db_path}", file=sys.stderr)
        return 1
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT
          src.label,
          src.title,
          src.asset_type,
          src.asset_key,
          src.row_version,
          ver.label AS version_label,
          ver.path,
          ver.version_label AS source_version,
          ver.change_note
        FROM source_asset src
        LEFT JOIN source_asset_version ver ON ver.id = src.current_version_id
        ORDER BY src.label
        """
    ).fetchall()
    if as_json:
        print(json.dumps([dict(row) for row in rows], indent=2, sort_keys=True))
        return 0
    if not rows:
        print("No assets registered.")
        return 0
    for row in rows:
        path = f" path={row['path']}" if row["path"] else ""
        version = f" version={row['version_label']}/{row['source_version']}" if row["version_label"] else ""
        print(f"{row['label']} {row['asset_type']} {row['title']}{version}{path}")
    return 0


def context_summary(argv: list[str]) -> int:
    db_path = db_path_from_args(argv)
    as_json = "--json" in argv
    if not db_path.exists():
        print(f"No bid state database found at {db_path}", file=sys.stderr)
        return 1
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    context_dir = Path.cwd() / "tmp" / "context-packs"
    rows = conn.execute(
        """
        SELECT label, title, item_type, status, validity_status, tag, row_version
        FROM work_item
        ORDER BY priority, label
        """
    ).fetchall()
    items = []
    for row in rows:
        context_path = context_dir / f"{row['label']}.md"
        item = dict(row)
        item["context_path"] = str(context_path)
        item["context_exists"] = context_path.exists()
        items.append(item)
    if as_json:
        print(json.dumps(items, indent=2, sort_keys=True))
        return 0
    if not items:
        print("No work items found.")
        return 0
    print("Available context targets:")
    for item in items:
        tag = f" tag={item['tag']}" if item["tag"] else ""
        context_state = "context=yes" if item["context_exists"] else "context=no"
        print(
            f"{item['label']} {item['status']} {item['validity_status']}{tag} "
            f"{item['title']} row_version={item['row_version']} {context_state}"
        )
    print("\nUse: bid_state.py context build --work-item WI-0001")
    print("Or:  bid_state.py context WI-0001")
    return 0


def connect_bid_db(argv: list[str]) -> tuple[Path, sqlite3.Connection] | tuple[Path, None]:
    db_path = db_path_from_args(argv)
    if not db_path.exists():
        return db_path, None
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    return db_path, conn


def phase_index_for_key(key: str) -> int | None:
    for index, phase in enumerate(PHASES):
        if phase["key"] == key:
            return index
    return None


def project_row(conn: sqlite3.Connection) -> sqlite3.Row | None:
    return conn.execute("SELECT * FROM project ORDER BY created_at LIMIT 1").fetchone()


def existing_phase_rows(conn: sqlite3.Connection, project_id: str) -> list[sqlite3.Row]:
    keys = [phase["key"] for phase in PHASES]
    placeholders = ",".join("?" for _ in keys)
    return list(
        conn.execute(
            f"SELECT * FROM work_item WHERE project_id=? AND work_item_key IN ({placeholders}) ORDER BY label",
            (project_id, *keys),
        ).fetchall()
    )


def create_phase(conn: sqlite3.Connection, project: sqlite3.Row, index: int, previous_label: str | None = None) -> tuple[sqlite3.Row, list[sqlite3.Row]]:
    phase = PHASES[index]
    priority = (index + 1) * 100
    parent = create_work(
        conn,
        project["id"],
        project["profile"],
        phase["title"],
        item_type="phase",
        key=phase["key"],
        phase=phase["phase"],
        status="ready",
        priority=priority,
        tag="ibm-bid-navigator",
    )
    children: list[sqlite3.Row] = []
    for child_index, (title, item_type, key, tag) in enumerate(phase["children"], start=1):
        child = create_work(
            conn,
            project["id"],
            project["profile"],
            title,
            item_type=item_type,
            key=key,
            parent=parent["label"],
            phase=phase["phase"],
            status="ready",
            priority=priority + child_index,
            tag=tag,
        )
        children.append(child)
    if previous_label:
        link_work_items(conn, project["id"], previous_label, parent["label"], "mark_needs_review")
    event(
        conn,
        project["id"],
        "bid_phase_created",
        "work_item",
        parent["id"],
        detail={"phase": phase["key"], "children": [child["label"] for child in children]},
    )
    return parent, children


def phase_children(conn: sqlite3.Connection, phase_id: str) -> list[sqlite3.Row]:
    return list(conn.execute("SELECT * FROM work_item WHERE parent_work_item_id=? ORDER BY priority, label", (phase_id,)).fetchall())


def is_phase_complete(conn: sqlite3.Connection, phase: sqlite3.Row) -> tuple[bool, list[sqlite3.Row]]:
    children = phase_children(conn, phase["id"])
    incomplete = [child for child in children if child["status"] != "complete"]
    if children:
        return not incomplete, incomplete
    return phase["status"] == "complete", [] if phase["status"] == "complete" else [phase]


def advance(argv: list[str]) -> int:
    db_path, conn = connect_bid_db(argv)
    if conn is None:
        print(f"No bid state database found at {db_path}", file=sys.stderr)
        return 1
    project = project_row(conn)
    if project is None:
        print(f"No project found in {db_path}. Run bid_state.py init first.", file=sys.stderr)
        return 1
    with transaction(conn):
        phases = existing_phase_rows(conn, project["id"])
        if not phases:
            parent, children = create_phase(conn, project, 0)
            message = f"Created {parent['label']} {parent['title']} with {len(children)} child work item(s)"
        else:
            current = max(phases, key=lambda row: phase_index_for_key(row["work_item_key"]) or 0)
            current_index = phase_index_for_key(current["work_item_key"])
            if current_index is None:
                print(f"Current phase {current['label']} is not recognised.", file=sys.stderr)
                return 1
            complete, incomplete = is_phase_complete(conn, current)
            if not complete:
                labels = ", ".join(f"{row['label']} {row['title']} [{row['status']}]" for row in incomplete)
                print(f"{current['label']} is not complete. Incomplete work: {labels}")
                return 0
            now = utc_now()
            if current["status"] != "complete":
                conn.execute(
                    "UPDATE work_item SET status='complete', completed_at=?, row_version=row_version+1, updated_at=? WHERE id=?",
                    (now, now, current["id"]),
                )
                event(conn, project["id"], "bid_phase_completed", "work_item", current["id"], detail={"phase": current["work_item_key"]})
            next_index = current_index + 1
            if next_index >= len(PHASES):
                message = f"{current['label']} is complete. No further bid phases are defined."
            else:
                next_key = PHASES[next_index]["key"]
                existing_next = conn.execute(
                    "SELECT * FROM work_item WHERE project_id=? AND work_item_key=?",
                    (project["id"], next_key),
                ).fetchone()
                if existing_next:
                    message = f"{existing_next['label']} {existing_next['title']} already exists"
                else:
                    parent, children = create_phase(conn, project, next_index, current["label"])
                    message = f"Created {parent['label']} {parent['title']} with {len(children)} child work item(s)"
    engine_main(translate(["render"]))
    engine_main(translate(["render-graph"]))
    print(message)
    return 0


def default_agent_id() -> str:
    return (
        os.environ.get("BID_AGENT_ID")
        or os.environ.get("AGENT_ID")
        or os.environ.get("CLINE_AGENT_ID")
        or os.environ.get("CLAUDE_AGENT_ID")
        or "bid-navigator-agent"
    )


def pop_option(argv: list[str], option: str) -> str | None:
    if option not in argv:
        return None
    index = argv.index(option)
    if index + 1 >= len(argv):
        return None
    value = argv[index + 1]
    del argv[index:index + 2]
    return value


def pop_multi_option(argv: list[str], option: str) -> list[str]:
    if option not in argv:
        return []
    index = argv.index(option)
    values: list[str] = []
    cursor = index + 1
    while cursor < len(argv) and not argv[cursor].startswith("--"):
        values.append(argv[cursor])
        cursor += 1
    del argv[index:cursor]
    return values


def translate_create_source(argv: list[str]) -> list[str]:
    translated = list(argv)
    title = pop_option(translated, "--title")
    doc_type = pop_option(translated, "--doc-type")
    purpose = pop_option(translated, "--purpose")
    if doc_type:
        translated.extend(["--type", doc_type])
    if purpose and "--change-note" not in translated:
        translated.extend(["--change-note", purpose])
    if title:
        translated.insert(1, title)
    return translated


def translate_add_children(argv: list[str]) -> list[str]:
    translated = list(argv)
    titles = pop_multi_option(translated, "--titles")
    if not titles:
        return translated
    if "--file" in translated:
        return translated
    tmp_dir = Path.cwd() / "tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    path = tmp_dir / f"bid-state-add-children-{stamp}.json"
    path.write_text(json.dumps({"children": [{"title": title} for title in titles]}, indent=2) + "\n", encoding="utf-8")
    translated.extend(["--file", str(path)])
    return translated


def ensure_agent_id(argv: list[str]) -> list[str]:
    translated = list(argv)
    if "--agent-id" not in translated:
        translated.extend(["--agent-id", default_agent_id()])
    return translated


def translate_context(argv: list[str]) -> list[str]:
    translated = list(argv)
    if len(translated) == 2 and not translated[1].startswith("-"):
        return ["context", "show", translated[1]]
    if len(translated) == 3 and translated[1] == "build" and not translated[2].startswith("-"):
        return ["context", "build", "--work-item", translated[2]]
    return translated


def translate(argv: list[str]) -> list[str]:
    translated = list(argv)
    if translated:
        if translated[0] == "revise-source-document":
            translated[0] = "revise-source"
        elif translated[0] == "create-source":
            translated = translate_create_source(translated)
        elif translated[0] == "add-children":
            translated = translate_add_children(translated)
        elif translated[0] == "context":
            translated = translate_context(translated)
        elif translated[0] in {"claim", "complete", "heartbeat", "release"}:
            translated = ensure_agent_id(translated)
    return [
        "--profile",
        "ibm_bid",
        "--profile-config",
        str(PROFILE_CONFIG),
        *translated,
    ]


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in {"list-assets", "list-sources"}:
        raise SystemExit(list_assets(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == "context" and (len(sys.argv) == 2 or all(arg.startswith("--") for arg in sys.argv[2:])):
        raise SystemExit(context_summary(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == "next":
        raise SystemExit(advance(sys.argv[2:]))
    raise SystemExit(engine_main(translate(sys.argv[1:])))
