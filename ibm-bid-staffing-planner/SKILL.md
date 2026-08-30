---
name: ibm-bid-staffing-planner
description: Build bid-ready staffing plans using the staffing-or optimiser. Use when you need to estimate team shape, delivery duration, cost, and gross profit for a tender response; compare delivery scenarios (location mix, contract type, complexity, budget); or produce a defendable staffing plan with assumptions and trade-offs for bid documentation. Requires Python 3.12+ and the bundled staffing-or wheel shipped with this skill.
---

# IBM Bid Staffing Planner

## PREREQUISITES - MANDATORY

**System Requirements:**
- Python 3.12 or higher

**Runtime:**

The skill includes a bundled wheel for the `staffing-or` runtime. Run the checked-in wrapper with `uv`:

Check CLI availability:

```bash
uv run $SKILL_DIR/scripts/run.py --help
uv run $SKILL_DIR/scripts/run.py --width 180 contracts
```

Do not call `staffing-or` binaries directly in this skill. Always use `run.py`.

## Runtime Source

`uv` resolves the `staffing-or` runtime from the bundled wheel directory:

- `$SKILL_DIR/assets/wheels/staffing_or-0.1.0-py3-none-any.whl`

No external `staffing_OR` checkout is required.

## Context Management

ALWAYS write intermediate scenario analysis to `./tmp/ibm-bid-staffing-planner.md`.

- Capture assumptions, constraints, and rejected options as you go.
- Write the final recommendation to `./outputs/` only when complete.

## Quick Start Workflow

### Step 1: Create Working Files

Use an empty working directory for the bid staffing model:

```bash
mkdir -p ./tmp/staffing-plan-work
cp $SKILL_DIR/assets/staffing_config.yaml ./tmp/staffing-plan-work/staffing_config.yaml
uv run $SKILL_DIR/scripts/run.py init-project --output-dir ./tmp/staffing-plan-work
```

Always use `./tmp/staffing-plan-work/staffing_config.yaml` as the default rates/config file for this skill.

### Step 2: Populate Bid Inputs

Edit `./tmp/staffing-plan-work/project.yaml` with bid specifics:

- `dcut_hours`
- `location_mix`
- `contract_type`
- `project_complexity`
- `target_duration_weeks` and/or `max_budget`
- `touches_production`
- `blended_gp_target_pct` (if used)

See `$SKILL_DIR/assets/project-template.yaml` for a commented example.

### Step 3: Generate Staffing Options

Run baseline and alternatives. Always include `--resource-plan`:

```bash
uv run $SKILL_DIR/scripts/run.py --width 180 plan --project ./tmp/staffing-plan-work/project.yaml --rates ./tmp/staffing-plan-work/staffing_config.yaml --resource-plan
uv run $SKILL_DIR/scripts/run.py --width 180 pareto --project ./tmp/staffing-plan-work/project.yaml --rates ./tmp/staffing-plan-work/staffing_config.yaml
```

Use `--width 180` by default on table-heavy commands so Rich output does not wrap key columns unnecessarily. Increase it further for narrow terminals or large scenario comparisons.

Example scenario override (no file edits):

```bash
uv run $SKILL_DIR/scripts/run.py --width 180 plan 10000 \
  --location-mix uk_mainline:0.2 \
  --location-mix india_cic:0.8 \
  --contract fixed_price \
  --complexity medium \
  --rates ./tmp/staffing-plan-work/staffing_config.yaml \
  --resource-plan
```

### Step 4: Export Evidence for Bid Pack

```bash
uv run $SKILL_DIR/scripts/run.py --width 180 plan \
  --project ./tmp/staffing-plan-work/project.yaml \
  --rates ./tmp/staffing-plan-work/staffing_config.yaml \
  --resource-plan \
  --export-csv ./tmp/staffing-plan-work/resource_plan.csv
```

Summarise:

- Recommended team shape (roles, seniority, location split)
- Duration (base and committed)
- Cost, price, GP, GP%
- Major trade-offs vs alternatives
- Key assumptions and constraints used

## Required Output Structure

When delivering a staffing recommendation, include:

1. **Bid Context** - workload, contract model, timeline and risk posture
2. **Recommended Plan** - team composition and location strategy
3. **Commercial View** - total cost, price, blended GP%
4. **Delivery View** - effort chain, schedule chain, key dependencies
5. **Scenario Comparison** - baseline vs at least one alternative
6. **Assumptions and Risks** - explicit assumptions, constraints, and confidence notes

## Integration with Other Skills

Typical sequence:

1. `ibm-bid-requirements-analysis` - extract delivery scope and constraints
2. `ibm-bid-staffing-planner` - generate staffing and commercial options (this skill)
3. `ibm-bid-solution-overview` or `ibm-bid-solution-architect` - align staffing to solution design
4. `ibm-bid-writer` - turn the plan into proposal narrative

## Quality Checklist

- ✓ Ran `uv run $SKILL_DIR/scripts/run.py ...` successfully from the bundled wheel in `assets/wheels`
- ✓ Used `run.py` wrappers only (no direct binary calls)
- ✓ Used `--width 180` or wider for table-heavy output
- ✓ Used `--resource-plan` on every `plan` run
- ✓ Used `assets/staffing_config.yaml` (copied to working directory) as the default config
- ✓ Tested at least one alternative scenario
- ✓ Reported cost, duration, and GP impact clearly
- ✓ Captured assumptions and constraints explicitly
- ✓ Exported evidence artefacts when requested (CSV/resource tables)
