# Adding a Skill to the ibm-bid-* Workflow

When a new skill participates in the ibm-bid-* flow (sits in the Phase 0–4 lifecycle, reads or writes `../tmp/ibm-bid-*.md` files, or is consumed by `ibm-bid-writer` or `ibm-bid-navigator`), update all of the following in addition to the standard skill creation checklist in `CLAUDE.md`.

## 1. `scripts/bid_state.py` — PHASES constant (authoritative work-item registry)

**Do this first.** The `PHASES` list in `bid_state.py` is the single source of truth for what work items `next` seeds in each phase. Add a tuple to the correct phase's `children` list:

```python
("Human-readable title", "work_item_type", "slug_key", "ibm-bid-skill-name"),
```

Work item types: `requirement`, `skill_task`, `answer`, `review`.

The phase lifecycle table in `SKILL.md` is derived from this list — update that table to match after editing the script.

## 2. `skills/ibm-bid-navigator/SKILL.md`

| Section | What to add |
| --- | --- |
| **Phase lifecycle table** (`### Phase lifecycle via next`) | Add a row in the correct phase block: `\| \| Human-readable title \| \`ibm-bid-skill-name\` \|` |
| **Quick Navigation → relevant section** | Add a bullet: `- Topic → **skill-name** (one-line description)` |
| **Phase X: ... Skills list** | Add the skill under the correct phase with a one-line description |
| **Phase X: ... Integration** | Add a bullet explaining how this skill feeds other skills or is fed by them |
| **Document Flow Convention** (the `../tmp/` listing) | Add the `../tmp/ibm-bid-skill-name.md` output file in phase order |

## 3. `skills/ibm-bid-navigator/references/skill-matrix.md`

| Section | What to add |
| --- | --- |
| **Complete Skill Inventory table** (top) | Add a row: phase, skill name, primary purpose, execution mode, typical duration |
| **Dependency Graph** (Mermaid) | Add a node in the correct `subgraph P*` block and any edges to/from dependent skills |
| **Skill Comparison Matrix** (relevant phase section) | Add a row: skill, focus, output structure, when to use, when to skip |
| **Input/Output Mapping** | Add a full `### ibm-bid-skill-name` section: inputs, outputs, consumed by |
| **Skill Selection Decision Tree** | Add a branch at the appropriate stage question |
| **Phase Checklist** (bottom) | Add a `- [ ]` item in the correct phase's completion checklist |

## 4. `skills/ibm-bid-navigator/references/legacy-ibm-bid-project-template.md`

Add a `- [ ] skill_name_artifact:` line only if legacy markdown migration needs
to recognise that field. New active state should be represented in SQLite via
Agent State Engine.

## 3. `skills/ibm-bid-navigator/assets/vocabularies/ibm_bid_project_fields.yaml`

This field schema is hand-maintained. It is not generated from
`references/legacy-ibm-bid-project-template.md`.

Add a matching field definition for any new template field. If the skill can own
work items, add its skill identifier to `routing_tag.values` so specialist
agents can claim work with `claim-next --tag <skill-name>`.

## 6. `skills/IBM-BID-README.md`

| Section | What to add |
| --- | --- |
| **Header skill count** | Increment the `**N ibm-bid-* skills**` number |
| **Current Skill Inventory → Phase X table** | Add a row: skill link, use-it-when description, main output |
| **Recommended End-to-End Workflow → Mermaid diagram** | Add a node inside the correct `subgraph P*` block |
| **Phase Guidance → Phase X numbered list** | Add a numbered step with the skill name and when to use it |
| **Document Flow Convention** (the `../tmp/` listing) | Add the `../tmp/ibm-bid-skill-name.md` file in phase order |
| **Quick Reference table** | Add a row: `\| I need to... \| \`skill-name\` \|` |
| **Version History** | Add a `- **vX.Y** (date): ...` entry |

## 7. `skill-categories.json`

Add the skill name to the `skills` array of every relevant role category (at minimum `go-to-market`; also `business-analyst` if the skill is analysis-focused).

## 8. Skills that consume the new skill's output

If the new skill produces a file that another skill reads automatically (e.g. `ibm-bid-writer` reads `../tmp/ibm-bid-client-language-analysis.md`):

- Add the new skill to the consuming skill's `skills-suggested` frontmatter metadata
- Add a check-for-file step to the consuming skill's Quick Start and Core Workflow sections
- Document the integration in the consuming skill's SKILL.md

## 9. Regenerate and verify

```bash
python3 scripts/generate-registry.py
```

Confirm the new skill appears in `skills-registry.json` and `skills-definitions.json` with the correct category tags.

Then run a quick coverage check to confirm the navigator references every ibm-bid skill:

```bash
# List all ibm-bid skill names (excluding navigator, library variants)
find skills -name "SKILL.md" | xargs grep -l "^name: ibm-bid" \
  | xargs grep -h "^name: " | sed 's/name: //' \
  | grep -v -E "ibm-bid-navigator|ibm-bid-library-qmd|ibm-bid-library-zvec" \
  | sort > /tmp/all_skills.txt

# Check which are missing from the navigator
while read skill; do
  grep -q "$skill" skills/ibm-bid-navigator/SKILL.md || echo "MISSING: $skill"
done < /tmp/all_skills.txt
```

Any `MISSING:` output means the navigator and/or `bid_state.py` needs updating.
