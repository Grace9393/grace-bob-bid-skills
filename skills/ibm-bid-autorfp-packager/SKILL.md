---
name: ibm-bid-autorfp-packager
description: Compile IBM bid answer-intent records and shared pack context into one validated AutoRFP markdown document per requirement. Use when IBM bid planning and drafting outputs need to be packaged for AutoRFP evaluation or optimization, especially when you have per-question YAML/JSON records plus bid-wide context and must produce self-contained `.md` files that conform to the AutoRFP schema and IBM bid semantic checks.
---

# Ibm Bid Autorfp Packager

## Overview

Compile pack-level IBM bid context and per-question answer-intent files into
AutoRFP-ready markdown documents, then validate them against the live AutoRFP
loader and IBM semantic checks.

## Workflow

### 1. If you already have standard `./tmp` bid artifacts, collect structured inputs first

Run:

```bash
uv run python $SKILL_DIR/scripts/collect_autorfp_inputs_from_tmp.py \
  --tmp-dir ./tmp \
  --output-dir ./tmp/ibm-bid-autorfp-inputs \
  --json
```

This collector looks for the standard IBM bid workflow artifacts such as:

- `ibm-bid-project.md`
- `ibm-bid-requirements-analysis.md`
- `ibm-bid-strategic-positioning.md`
- `ibm-bid-hot-buttons.md`
- `ibm-bid-win-themes.md`
- `ibm-bid-responses/Q*.md`
- `ibm-bid-responses/Q*_plan.md`

It produces:

- `pack-context.yaml`
- one YAML file per question under `questions/`

If you want it to package the markdown documents immediately as well:

```bash
uv run python $SKILL_DIR/scripts/collect_autorfp_inputs_from_tmp.py \
  --tmp-dir ./tmp \
  --output-dir ./tmp/ibm-bid-autorfp-inputs \
  --package-output-dir ./tmp/ibm-bid-autorfp-pack \
  --validate-script /Users/telcott/tmp/code/autorfp/scripts/validate_document.py \
  --ibm \
  --json
```

### 2. Confirm the manual structured inputs if you are not using collector mode

Collect:

- one shared pack-context YAML/JSON file
- one or more per-question answer-intent YAML/JSON files
- the AutoRFP validator script path:
  `/Users/telcott/tmp/code/autorfp/scripts/validate_document.py`

Read [input-files.md](references/input-files.md) for the expected pack and
question structures before packaging.

### 3. Package the documents

Run:

```bash
uv run python $SKILL_DIR/scripts/package_autorfp_documents.py \
  --pack-context path/to/pack-context.yaml \
  --question path/to/q01.yaml \
  --question path/to/q02.yaml \
  --output-dir ./tmp/ibm-bid-autorfp-pack \
  --validate-script /Users/telcott/tmp/code/autorfp/scripts/validate_document.py \
  --ibm \
  --json
```

Or package every YAML/JSON file in a directory:

```bash
uv run python $SKILL_DIR/scripts/package_autorfp_documents.py \
  --pack-context path/to/pack-context.yaml \
  --questions-dir path/to/questions \
  --output-dir ./tmp/ibm-bid-autorfp-pack \
  --validate-script /Users/telcott/tmp/code/autorfp/scripts/validate_document.py \
  --ibm
```

Behavior:

- merge pack-level defaults with question-level overrides
- materialize `ibm_bid.policy_snapshot`
- materialize `ibm_bid.pack_context`
- write one markdown file per question using the answer `title` slug
- optionally run the live AutoRFP validator after each file is written

### 4. Fix validation failures before hand-off

If validation fails, repair the source pack/question files rather than patching
the generated markdown by hand. The packager is meant to be deterministic.

Common fixes:

- missing `title`, `question`, `word_limit`, `dimensions`, or `optimization`
- missing `draft_body`
- missing `ibm_bid.policy_snapshot.source_refs`
- missing `approved_proof_points` and `banned_claims`
- missing `claim_provenance` when `factual_context` is populated
- required headings present in front matter but absent in the body

### 5. Keep the contract boundary clean

Do not treat the generated AutoRFP documents as the native editing surface for
upstream IBM bid skills. Update the source answer-intent records, rerun the
packager, then revalidate.

## Resources

### scripts/

Use `scripts/package_autorfp_documents.py` to compile and validate AutoRFP
documents from pack-level and question-level YAML/JSON inputs.

Use `scripts/collect_autorfp_inputs_from_tmp.py` to turn the existing IBM bid
workflow artifacts in `./tmp` into `pack-context.yaml` and one question YAML
per drafted response.

### references/

Read [input-files.md](references/input-files.md) for the pack/question schema,
merge behavior, and field mapping.

Read [testing.md](references/testing.md) for the expected validation and pytest
commands.
