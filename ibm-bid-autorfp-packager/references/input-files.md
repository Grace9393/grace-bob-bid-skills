# Input Files

Use this skill with two input types:

1. A shared pack-context YAML or JSON file
2. One or more per-question answer-intent YAML or JSON files

The packager merges the shared pack context with each question file, then emits
one AutoRFP markdown document per question.

## Collector Mode

If you already have the standard IBM bid workflow outputs under `../tmp`, use
`scripts/collect_autorfp_inputs_from_tmp.py` instead of building the YAML files
by hand.

Collector expectations:

- `ibm-bid-project.md` for bid identity and source documents
- `ibm-bid-requirements-analysis.md` for client context
- `ibm-bid-strategic-positioning.md` for strategic context
- `ibm-bid-hot-buttons.md` for client priorities
- `ibm-bid-win-themes.md` for strategic messaging
- `ibm-bid-responses/Q*.md` for per-question draft bodies
- `ibm-bid-responses/Q*_plan.md` when available for per-question planning data

Collector behavior when files are missing:

- missing requirements analysis: hard failure
- missing response files: hard failure
- missing project/strategic/hot-button/win-theme/plan files: continue with
  warnings and best-effort fallbacks
- missing raw question text in plans/source docs: fall back to a title-derived
  question string and emit a warning
- missing criteria in scoring source docs: create one fallback criterion and
  emit a warning

## Pack Context

Expected fields:

```yaml
pack_id: "client-proposal-2026-04"
pack_version: "3"
client_name: "Example Client"
proposal_name: "Managed Services Proposal"
opportunity_name: "Managed Services Reprocurement"
client_context: |
  Buyer context and constraints shared across the bid.
hot_buttons:
  - Low delivery risk
win_themes:
  - Proven mobilisation with strong governance
proposal_principles:
  - Buyer protection first
approved_proof_points:
  - Approved proof point
banned_claims:
  - Best in class
preferred_structure:
  - Executive summary
  - Approach
dimensions:
  word_count:
    enabled: true
    weight: 0.10
optimization:
  model: "openai/gpt-oss-20b"
  max_iterations: 3
policy_source_refs:
  - path: policy/writing-style-guide.md
  - path: policy/quality-checklist.md
policy_defaults:
  source_skill: ibm-bid-writer
  style_rules:
    tone: "Formal, evaluator-facing, British English"
source_documents:
  - kind: rfp
    title: "Main ITT"
    location: "/absolute/path/to/source.pdf"
```

Notes:

- `policy_source_refs` may be a list of strings or objects containing `path`
  and optional `sha256`
- relative `policy_source_refs` are resolved relative to the pack-context file
- `policy_defaults` becomes the base for `ibm_bid.policy_snapshot`
- `dimensions` and `optimization` are usually pack-level defaults

## Question Answer-Intent

Expected fields:

```yaml
question_reference: "Q1.2"
title: "Service mobilisation"
question: |
  Describe your mobilisation approach.
word_limit: 650
criteria:
  - id: mobilisation
    description: "Credible mobilisation approach"
    weight: 0.5
factual_context: |
  Approved facts only.
draft_body: |
  ## Executive summary
  ...
evaluator_concern: "Transition risk"
confidence_case: "IBM is credible because..."
confidence_heading: "Why you should have full confidence in our proposal"
confidence_bullets:
  - Low transition risk
named_mechanisms:
  - Transition Control Tower
required_headings:
  - Executive summary
  - Approach
claim_provenance:
  - claim_id: mobilisation-001
    claim_text: "IBM will run weekly governance reviews."
    source_refs:
      - source_document_title: "Mobilisation plan"
        location: "section-2"
        evidence_quote: "Weekly governance reviews"
    approved_for_rewrite: true
```

Notes:

- question-level values override pack-level defaults
- `draft_body` is required and becomes the markdown body
- if `factual_context` is populated, `claim_provenance` should also be present
- use question files to add or override any final `ibm_bid` fields

## Merge Rules

- dictionaries merge recursively
- lists and scalars from the question file replace pack defaults when present
- `policy_snapshot` is built from `policy_defaults`, question overrides, and
  hashed `policy_source_refs`
- `pack_context` is generated automatically from the pack file path and hash
- `ibm_bid.enabled` is always set to `true` for packaged IBM bid documents
