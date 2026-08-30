# IBM Bid Navigator Profile

## Purpose

IBM Bid Navigator is a bid-domain profile over Agent State Engine. The engine
owns generic mechanics: state transitions, dependency propagation, claims,
context-pack generation, rendering, row versions, and event logging. This
profile owns bid vocabulary, impact rules, path aliases, dashboard wording, and
bid-friendly command names.

Generic mechanics are documented in the independent `agent-state-engine` skill.
The bid profile depends on the engine CLI and schema contract but keeps
bid-specific vocabulary and migration guidance in this skill.
For this release, the scope is the IBM bid navigation flow: initialise bid
state, create dynamic parent/child work items, route work to specialist bid
skills by tag, and render/current-state views. Fixed bid workflow templates are
out of scope.

Bid-specific migration guidance remains separate:

- `references/ibm-bid-navigator-migration.md`

## Current Problem

`ibm-bid-navigator` currently coordinates bid work through:

```text
./tmp/ibm-bid-project.md
```

That markdown file is readable, but it is fragile as canonical state:

1. Agents can overwrite prior checklist items.
2. Dependencies are implied in prose.
3. Revised client documents require manual ripple assessment.
4. The file tends to collect too much context, even though each bid step needs
   only a subset of documents and artifacts.

## Target Model

Use Agent State Engine as the canonical local state store and generate
bid-friendly views from it:

```text
bid_state.py profile wrapper
  -> agent_state.py engine
      -> ./tmp/ibm-bid-project.sqlite
      -> generated ./tmp/ibm-bid-project.md
      -> generated context packs
      -> generated dependency graph
```

Ownership rule:

- Agent State Engine owns mechanics.
- IBM Bid Navigator owns bid meaning.
- SQLite owns canonical state.
- Generated markdown owns presentation.
- Generated context packs own step-specific context.

`bid_state.py` must be a thin wrapper over `agent_state.py`. It may provide
bid-friendly aliases, defaults, labels, and path conventions, but it must not
duplicate engine state-transition, claiming, propagation, context, or rendering
logic.

## Profile Files

```text
skills/ibm-bid-navigator/assets/
  profile.yaml
  impact-rules/
  vocabularies/
```

Impact rules and vocabularies are YAML so bid teams can adjust profile
behaviour without changing engine code.

## Storage Aliases

The bid profile uses these project paths over the generic engine:

```text
./tmp/ibm-bid-project.sqlite
./tmp/ibm-bid-project.md
./tmp/context-packs/
./tmp/impact-reports/
./inputs/client_docs/
./inputs/converted_markdown/
./outputs/answers/
```

Source documents should live inside the project folder, normally under
`./inputs/client_docs/`. Converted markdown and extracted forms should live
under `./inputs/converted_markdown/`.

The SQLite database may be committed to Git while small. For larger bids, use
Git LFS or periodic JSON exports.

## Schema Mapping

All generic schema mechanics and required engine rules apply from the
`agent-state-engine` skill schema reference.

| Engine Concept | Bid Profile Term |
| --- | --- |
| `project` | bid project |
| `source_asset` | source document |
| `source_asset_version` | source document version |
| `artifact` | bid artifact / answer document |
| `artifact_version` | answer version / artifact version |
| `impact` | document impact |
| `work_item` | bid task / answer / review |
| `work_item.parent_work_item_id` | bid operation / multi-step workflow |
| generated context file | bid context pack |

Bid source document keys map to `source_asset.asset_key`. Bid answer documents
map to `artifact` and `artifact_version`. Bid document impacts map to generic
`impact`.

The engine uses UUID primary keys plus generated human labels. The bid profile
uses labels such as:

- `WI-0042`
- `DOC-0004`
- `DOCV-0012`
- `ART-0101`
- `ARTV-0021`
- `IMP-0017`

## Vocabularies

Source asset types:

- `rfp`
- `itt`
- `pricing_schedule`
- `requirements_spreadsheet`
- `draft_contract`
- `clarification_response`
- `evaluation_criteria`
- `client_strategy`
- `technical_appendix`
- `supporting_document`
- `public_source`

Work item types:

- `skill_task`
- `manual_task`
- `requirement`
- `answer`
- `review`
- `decision`
- `risk`
- `quality_gate`
- `artifact_refresh`

Work item routing tags:

- zero or one tag per work item
- tag values should normally be skill identifiers, for example
  `ibm-bid-writer`, `ibm-bid-fact-checker`, `ibm-bid-pricing-strategy`, or
  `ibm-sf-solution-architect`
- specialist agents should claim work with `claim-next --tag <skill-name>`
- untagged work remains available to generalist orchestration

Impact types:

- `introduces_requirement`
- `changes_requirement`
- `changes_scope`
- `changes_pricing`
- `changes_contract_terms`
- `changes_evaluation_criteria`
- `adds_clarification`
- `changes_solution_assumption`
- `affects_answer`
- `affects_review`

## CLI Wrapper

The generic command surface lives in the `agent-state-engine` skill. The bid
wrapper should preserve the same command style: noun-oriented subcommands with
positional IDs.

Preferred examples:

```bash
uv run $SKILL_DIR/scripts/bid_state.py init
uv run $SKILL_DIR/scripts/bid_state.py show WI-0042
uv run $SKILL_DIR/scripts/bid_state.py show WI-0042 --children
uv run $SKILL_DIR/scripts/bid_state.py next WI-0042
uv run $SKILL_DIR/scripts/bid_state.py claim WI-0042 --agent-id agent-pricing-1 --expected-row-version 7
uv run $SKILL_DIR/scripts/bid_state.py claim-next WI-0001 --limit 5 --agent-id-prefix pricing --tag ibm-bid-pricing-strategy
uv run $SKILL_DIR/scripts/bid_state.py claim-next WI-0001 --limit 5 --agent-id-prefix writer --tag ibm-bid-writer
uv run $SKILL_DIR/scripts/bid_state.py expire-claims
uv run $SKILL_DIR/scripts/bid_state.py complete WI-0042 --agent-id agent-pricing-1 --expected-row-version 8 --summary "Pricing refreshed"
uv run $SKILL_DIR/scripts/bid_state.py link WI-0010 WI-0042 --policy mark_outdated
uv run $SKILL_DIR/scripts/bid_state.py create-source --path ./inputs/client_docs/itt.md --title "Client ITT" --doc-type ITT --purpose "Primary procurement document"
uv run $SKILL_DIR/scripts/bid_state.py list-assets
uv run $SKILL_DIR/scripts/bid_state.py list-assets --json
uv run $SKILL_DIR/scripts/bid_state.py add-child WI-0001 "Wireframe Q1 service management" --type answer --tag ibm-bid-wireframe-creator --source-work-item WI-0004
uv run $SKILL_DIR/scripts/bid_state.py add-children WI-0001 --file ./tmp/generated-answer-tasks.yaml --source-work-item WI-0004
uv run $SKILL_DIR/scripts/bid_state.py add-children WI-0001 --titles "Requirements Analysis" "Strategic Positioning" "Bid/No-Bid Decision"
uv run $SKILL_DIR/scripts/bid_state.py context
uv run $SKILL_DIR/scripts/bid_state.py context build WI-0002
uv run $SKILL_DIR/scripts/bid_state.py context WI-0002
```

The bid wrapper accepts a small set of bid-friendly aliases for agent
ergonomics:

- `create-source --title ... --doc-type ... --purpose ...` maps to the generic
  source title, `--type`, and `--change-note` fields.
- `add-children WI-0001 --titles "Task A" "Task B"` writes a temporary children
  file under `./tmp/` and calls the generic batch creation path.
- `list-assets` and `list-sources` list registered source documents from
  `./tmp/ibm-bid-project.sqlite`; use `--json` for machine-readable output.
- bare `context` lists available work items and whether a context pack exists;
  `context WI-0002` shows a context pack and `context build WI-0002` builds one.
- `claim`, `complete`, `heartbeat`, and `release` default `--agent-id` to
  `BID_AGENT_ID`, `AGENT_ID`, `CLINE_AGENT_ID`, `CLAUDE_AGENT_ID`, or
  `bid-navigator-agent` if no environment value exists. Explicit agent ids are
  still preferred for parallel specialist teams.

Skills may expand the plan as they discover bid work. Requirements analysis can
add requirement-level tasks; bid-question review can add wireframe and answer
tasks per question. Batch creation should use `add-children` so the expansion is
auditable and applied in one transaction. Generated children should include a
single routing tag when a specialist skill is required, for example
`tag: ibm-bid-writer` for answer drafting and `tag: ibm-bid-fact-checker` for
source validation.

Source revision workflow:

```bash
uv run $SKILL_DIR/scripts/bid_state.py revise-source-document DOC-0004 \
  --path ./inputs/client_docs/pricing-schedule-v2.xlsx \
  --version-label v2 \
  --change-note "Client revised rate-card assumptions"

uv run $SKILL_DIR/scripts/bid_state.py review-impacts DOCV-0012
uv run $SKILL_DIR/scripts/bid_state.py approve-impact IMP-0017 --reviewed-by "human"
uv run $SKILL_DIR/scripts/bid_state.py reject-impact IMP-0018 --reviewed-by "human" --reason "No dependency"
uv run $SKILL_DIR/scripts/bid_state.py apply-approved-impacts DOCV-0012
```

`apply-approved-impacts` must be visible in the revision workflow.

## Visualising Bid State

Rendering commands must use the engine verbs:

```bash
uv run $SKILL_DIR/scripts/bid_state.py render
uv run $SKILL_DIR/scripts/bid_state.py render-graph
```

`render` writes `./tmp/ibm-bid-project.md`, the primary readable dashboard.
`render-graph` writes `./tmp/ibm-bid-project-graph.mmd`, a Mermaid dependency
graph. Both are generated from SQLite state and may be deleted/recreated.

Navigator agents should use this flow when asked to visualise bid state:

1. Run `bid_state.py render`.
2. Run `bid_state.py render-graph`.
3. Run `bid_state.py show WI-0001 --children` if a parent work item is known.
4. Run `bid_state.py list-assets` to show registered client/source documents.
5. Run `bid_state.py context` to list context targets and context-pack status.
6. Summarise ready, blocked, in-progress, and complete work items from generated
   state; do not reconstruct the graph from chat history.

If the user wants a visual graph, point them to
`./tmp/ibm-bid-project-graph.mmd`. If their viewer supports Mermaid, the file can
be rendered directly. If they only need a text view, use
`./tmp/ibm-bid-project.md`.

Rendering must write to a temporary file and atomically rename it into place.

## Source Document Updates

When a revised client document or clarification arrives, the bid wrapper should
call the engine to:

1. Register a new `source_asset_version`.
2. Add an `event_log` entry.
3. Generate proposed `impact` rows using bid impact rules.
4. Render an impact report for human review.
5. Apply only approved impacts.
6. Update affected work item `validity_status`.
7. Create follow-on refresh work items.
8. Regenerate the dashboard and relevant context packs.

Impact propagation is not automatic. It is proposed first and applied only after
human approval. Rejected and unnecessary impacts remain in the audit trail.

Completed work stays complete. A source change changes `validity_status` and
creates follow-on work, rather than erasing completion history.

## Impact Rules

Default source impact rules:

| Source type | Direct impact |
| --- | --- |
| `pricing_schedule` | pricing strategy, staffing plan, commercial assumptions, affected answer drafts |
| `requirements_spreadsheet` | requirements extraction, requirements analysis, solution architecture, response wireframes |
| `draft_contract` | legal assessment, risk register, assumptions, pricing strategy |
| `clarification_response` | clarifications, requirements analysis, affected answer drafts, fact-check pass |
| `evaluation_criteria` | win themes, answer evaluator, response structure, executive summary |
| `technical_appendix` | solution architecture, TDA review, technical answer drafts |

The rule set should be conservative. If uncertain, propose a review item rather
than silently assuming no impact.

## Answer Concurrency

Each tender answer should be a separate logical artifact and file:

```text
ART-0101 q1_service_management_answer -> ./outputs/answers/q1-service-management.md
ART-0102 q2_implementation_approach -> ./outputs/answers/q2-implementation-approach.md
ART-0103 q3_social_value -> ./outputs/answers/q3-social-value.md
```

Artifact writes are allowed only by the active claimant of the artifact's owning
work item. Shared final outputs should be produced by an explicit integration
work item.

## Context Policies

Generic context policy mechanics live in the `agent-state-engine` skill.
Context packs are generated files with metadata headers, not database rows.

Context policies provide progressive disclosure for bid work. Agents should use
the generated context pack for the current work item, not all project documents:

```bash
uv run $SKILL_DIR/scripts/bid_state.py context build --work-item WI-0042
uv run $SKILL_DIR/scripts/bid_state.py context show WI-0042
```

Policy example:

```yaml
schema_version: 1
skill: ibm-bid-pricing-strategy
include:
  - document_type: pricing_schedule
    disclosure: full
    required: true
  - artifact_type: staffing_plan
    disclosure: full
  - artifact_type: requirements_analysis
    disclosure: excerpt
  - item_type: risk
    disclosure: summary
exclude:
  - document_type: technical_appendix
  - artifact_type: answer_draft
```

Bid policy precedence follows the engine rules:

1. Work-item required context is included first.
2. Explicit human-added context items override policy excludes.
3. Policy excludes override generic policy includes.
4. Required policy includes are included unless explicitly rejected by a human.
5. Optional includes are included only when they match the current work item or
   dependency neighbourhood.
6. Every context pack records the policy file path and `schema_version`.

Disclosure levels:

- `metadata_only`
- `summary`
- `excerpt`
- `full`
- `reference`

Each context item must have a relevance reason. If the system cannot explain why
an item is needed, it should not include it by default.

## Navigation Flow

The bid navigator should not carry a fixed implementation workflow template.
It should initialise canonical state, then create parent/child work items as
the bid shape becomes clear. Mermaid is generated from live state through
`render-graph`.

## Confirmed Decisions

1. Agent State Engine is the generic state layer.
2. IBM Bid Navigator is a profile over the engine.
3. `bid_state.py` wraps `agent_state.py`; it does not duplicate engine logic.
4. The bid profile uses `render-graph` to match the engine CLI.
