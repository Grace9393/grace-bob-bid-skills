# Testing

Run these checks after editing the skill or packager script.

## Skill validation

```bash
uv run python /Users/telcott/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  $SKILL_DIR
```

## Skill link validation

```bash
python3 scripts/skills_link.py
```

## Registry regeneration

```bash
python3 scripts/generate-registry.py
```

## Packager tests

```bash
uv run pytest skills/ibm-bid-autorfp-packager/tests -q
```

## Collector fixture run

```bash
uv run python $SKILL_DIR/scripts/collect_autorfp_inputs_from_tmp.py \
  --tmp-dir $SKILL_DIR/tests/fixtures/tmp_workflow \
  --output-dir ../tmp/ibm-bid-autorfp-inputs-test \
  --package-output-dir ../tmp/ibm-bid-autorfp-pack-test \
  --validate-script /Users/telcott/tmp/code/autorfp/scripts/validate_document.py \
  --ibm \
  --json
```

## Direct fixture run

```bash
uv run python $SKILL_DIR/scripts/package_autorfp_documents.py \
  --pack-context $SKILL_DIR/tests/fixtures/pack_context.yaml \
  --question $SKILL_DIR/tests/fixtures/questions/service-mobilisation.yaml \
  --output-dir ../tmp/ibm-bid-autorfp-pack-test \
  --validate-script /Users/telcott/tmp/code/autorfp/scripts/validate_document.py \
  --ibm \
  --json
```
