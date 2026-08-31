# IBM Bid Navigator Migration Guidance

## Relationship To Agent State Engine

Generic migration principles live in the independent `agent-state-engine` skill.
This file records the bid-profile migration from `./tmp/ibm-bid-project.md`.

## Principle

Migration from `./tmp/ibm-bid-project.md` is a draft import, not a trusted
canonical conversion.

The existing markdown state is free-form and may contain missing fields,
duplicated sections, incomplete source-document paths, and stale checklist
items. The migration command should produce:

- draft database rows
- a migration review report
- warnings for ambiguous fields
- explicit human approval before the imported state becomes canonical

## Command

```bash
uv run $SKILL_DIR/scripts/bid_state.py migrate-markdown \
  --input ./tmp/ibm-bid-project.md \
  --status draft
```

## Review Report

Write the report to:

```text
./tmp/migration-reports/ibm-bid-project-migration.md
```

The report should list:

- parsed project metadata
- inferred source documents and missing file paths
- inferred artifacts
- inferred work items
- fields that could not be parsed
- proposed workflow template
- records requiring human confirmation

Only after review should the user run:

```bash
uv run $SKILL_DIR/scripts/bid_state.py migration approve <migration-id>
```
