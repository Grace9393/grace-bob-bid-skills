---
name: ibm-skills-bid-workflow
description: Run an end-to-end IBM bid response using the IBM Skills marketplace - 5 phases from RFP intake to final submission, with the canonical bid state machine and named skill calls.
---

# ibm-skills-bid-workflow

Use when the user has an RFP/ITT/tender to respond to and wants the full IBM Skills bid workflow, or asks "how do I run a bid end-to-end".

## The 5 phases

```
Phase 0   Phase 1                Phase 2                Phase 3                Phase 4
Opportunity   Strategic               Solution               Content                Technical
Assessment    Positioning             Architecture           Development            Assurance
   ↓                ↓                       ↓                       ↓                       ↓
should we   what's our         what are we        actually                 will it pass
bid?            angle?                 bidding?               write the answers      review?
```

Driver throughout: `ibm-bid-navigator` (orchestrator). It hands off to specialists per phase and uses the **agent-state-engine** to track work-items, sources, and phase progression.

## Workspace setup (one-time per bid)

```bash
# Initialise the canonical bid state via the navigator's wrapper script
uv run $SKILL_DIR/scripts/bid_state.py init

# Register source documents
uv run $SKILL_DIR/scripts/bid_state.py create-source \
   --path ./inputs/client_docs/itt.md \
   --title "Client ITT" \
   --doc-type ITT \
   --purpose "Primary procurement document"

# Verify
uv run $SKILL_DIR/scripts/bid_state.py list-assets
uv run $SKILL_DIR/scripts/bid_state.py context
```

The state lives in `tmp/ibm-bid-project.md` (and a SQLite-backed DB the engine manages). Persist it; commit it to the bid repo.

## Phase 0 — Opportunity Assessment

Decide whether to bid.

```
load $ibm-bid-navigator. Initial intake of @inputs/client_docs/itt.md.
load $ibm-bid-qualification.   Run qualification on the bid state.
```

Outputs (under `outputs/phase-0/`):
- Qualification scorecard (go / no-go / conditional)
- Risks register (initial)
- Resource estimate (rough)

Decision gate: **bid / no-bid**. If no-bid, stop here.

## Phase 1 — Strategic Positioning

How will we win?

```
load $ibm-bid-client-language-analysis.   Mine the ITT for client language.
load $ibm-bid-hot-buttons.                  Identify the client's hot buttons.
load $ibm-bid-competitor-analysis.          Map likely competitors and weaknesses.
load $ibm-bid-strategic-positioning.        Synthesize positioning statement.
load $ibm-bid-win-themes.                   Lock 3-5 win themes for the response.
```

Outputs:
- Win themes (3-5 sentences each)
- Positioning statement
- Hot-button → win-theme map
- Competitor matrix

## Phase 2 — Solution Architecture

What are we actually offering?

```
load $ibm-bid-requirements-extractor. Extract structured requirements.
load $ibm-bid-requirements-analysis.   Analyse requirements (gaps, risks, must-haves).
load $ibm-bid-scope-constrainer.       Constrain scope where ITT is open-ended.
load $ibm-bid-solution-architect.      Top-down solution design.
load $ibm-bid-solution-overview.       Solution narrative for the executive summary.
load $ibm-bid-offerings-advisor.       Map IBM offerings to requirements.
load $ibm-bid-staffing-planner.        Staffing plan.
load $ibm-bid-pricing-strategy.        Pricing approach.
load $ibm-bid-image-definer.           Briefs for diagrams the SA will produce.
load $ibm-bid-wireframe-creator.       Wireframes for any UI elements.
load $ibm-bid-tda-review.              TDA-readiness check.
```

Outputs:
- Requirements register (structured, traceable)
- Solution architecture document
- Offerings map
- Staffing plan and pricing model
- Image / wireframe briefs

## Phase 3 — Content Development

Write the response.

```
load $ibm-bid-customer-stories.  Pull customer stories aligned to win themes.
load $ibm-bid-fact-checker.       Verify claims against the bid library.
load $ibm-bid-library.            Search the bid library for reusable content.
load $ibm-bid-writer.             Draft answers section by section.
load $ibm-bid-executive-summary. Compose the exec summary last.
load $ibm-bid-word-count.         Trim to required limits.
load $ibm-bid-clarifications.    Draft questions for the client.
load $ibm-bid-social-value-expert. Social value section.
load $ibm-bid-legal-assessment.   Legal review of bespoke commitments.
load $ibm-bid-answer-evaluator.   Score each answer against the question.
load $humaniser.                   Final pass to remove AI-isms.
```

Outputs:
- Drafted answer files under `outputs/answers/`
- Executive summary
- Customer story selections
- Clarifications log
- Evaluation scorecards per answer

## Phase 4 — Technical Assurance

Will it pass internal review?

```
load $ibm-bid-tda-review.            Pre-TDA self-check.
load $ibm-bid-fact-checker.          Re-run after late changes.
load $ibm-bid-answer-evaluator.      Final scoring.
load $ibm-bid-autorfp-packager.      Package the response per submission requirements.
```

Outputs (under `outputs/final/`):
- Final response in submission format (often .docx; convert with pandoc)
- TDA pack
- Submission checklist

## Context-refresh prompt

When you start a new agent session mid-bid (Cline / Claude / etc.), don't drag the prior conversation in:

```
load $ibm-bid-navigator. Review tmp/ibm-bid-project.md.
```

Then add the next specific task as a separate prompt.

## Workspace conventions

```
<bid-project>/
├── inputs/
│   └── client_docs/                ← original ITT and attachments (Markdown preferred)
├── outputs/
│   ├── phase-0/                     phase outputs as you go
│   ├── phase-1/
│   ├── phase-2/
│   ├── phase-3/
│   ├── answers/                     question-by-question drafts
│   └── final/                       final submission package
├── tmp/
│   └── ibm-bid-project.md          ← canonical state (do not delete)
└── .claude/                         skills installed here
```

## Tips
- **Don't skip Phase 0**. Bid skills work much better with strong qualification grounding.
- **Convert source docs to Markdown first** (`markitdown`, IBM Docling) — every IBM Skills bid skill expects Markdown input.
- **Keep state in `tmp/ibm-bid-project.md`** — it's how the navigator picks up where you left off.
- **Use `$humaniser` last**, after all answer drafts are evaluated. Running it earlier can mask issues the evaluator would catch.

## Related skills
- `ibm-skills-overview`, `ibm-skills-by-role` — orient before diving in.
- `ibm-skills-story-workflow` — for storytelling-led communications (often plugs into Phase 1 or Phase 3).
- `ibm-skills-sf-workflow` — when the bid involves significant Salesforce delivery.
