---
name: ibm-bid-navigator
description: Use this skill to navigate IBM's bid management workflow when users ask which bid skill to use, how to orchestrate multiple bid skills together, what the complete tender response process looks like, or need guidance on bid workflow phases. This is the central orchestration skill for all bid skills across the 5-phase tender response lifecycle (Opportunity Assessment, Strategic Positioning, Solution Architecture, Content Development, Technical Assurance), including strategic planning skills like ibm-bid-hot-buttons and ibm-bid-wireframe-creator. Use when users mention "bid workflow", "tender process", "which bid skill", "end-to-end bid", "RFP response process", or want to understand how bid skills integrate together.
---

# IBM Bid Navigator

Central orchestration skill for IBM's comprehensive bid management system. This skill helps you navigate the complete tender response workflow across bid delivery skills and supporting resources through 5 phases from RFP receipt to final submission.

## Context Management

Write output to `./tmp/ibm-bid-navigator.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

### Canonical Bid State

For multi-step bid lifecycles, use Agent State Engine through the bid wrapper:

```bash
uv run $SKILL_DIR/scripts/bid_state.py init
uv run $SKILL_DIR/scripts/bid_state.py create-source --path ./inputs/client_docs/itt.md --title "Client ITT" --doc-type ITT --purpose "Primary procurement document"
uv run $SKILL_DIR/scripts/bid_state.py list-assets
uv run $SKILL_DIR/scripts/bid_state.py next                          # seed Phase 0; advance to next phase when current is complete
uv run $SKILL_DIR/scripts/bid_state.py show WI-0001 --children
uv run $SKILL_DIR/scripts/bid_state.py context
uv run $SKILL_DIR/scripts/bid_state.py context build --work-item WI-0002
uv run $SKILL_DIR/scripts/bid_state.py context WI-0002
uv run $SKILL_DIR/scripts/bid_state.py render
uv run $SKILL_DIR/scripts/bid_state.py render-graph
```

Canonical state is stored in:

- `./tmp/ibm-bid-project.sqlite`

Generated views are stored in:

- `./tmp/ibm-bid-project.md`
- `./tmp/context-packs/`
- `./tmp/impact-reports/`
- `./tmp/ibm-bid-project-graph.mmd`

Agents must not reconstruct bid state from chat history or directly edit the generated markdown dashboard. Use `bid_state.py` commands for state changes, claims, dependencies, revised documents, impact review, context packs, and rendering.

### Phase lifecycle via `next`

`next` seeds work items on first call and acts as a phase gate on every subsequent call. On each call it checks whether every child of the current phase has `status='complete'`; if any are open it reports what's blocking and exits. Once all children are complete, `next` seals the current phase and creates the next one.

To advance: complete each blocking child, then re-run `next`:

```bash
uv run $SKILL_DIR/scripts/bid_state.py complete WI-XXXX \
  --agent-id my-agent --expected-row-version N --summary "Done"
uv run $SKILL_DIR/scripts/bid_state.py next
```

Work items seeded per phase:

| Phase | Work items created by `next` | Routing tag |
|---|---|---|
| **Phase 0** | Requirements Analysis | `ibm-bid-requirements-analysis` |
| | Strategic Positioning | `ibm-bid-strategic-positioning` |
| | Qualification Assessment | `ibm-bid-qualification` |
| | Legal Assessment | `ibm-bid-legal-assessment` |
| | Competitor Analysis | `ibm-bid-competitor-analysis` |
| | Clarifications | `ibm-bid-clarifications` |
| **Phase 1** | Hot Buttons Extraction | `ibm-bid-hot-buttons` |
| | Client Language Analysis | `ibm-bid-client-language-analysis` |
| | Win Themes | `ibm-bid-win-themes` |
| | Offerings Advisor | `ibm-bid-offerings-advisor` |
| | Executive Summary | `ibm-bid-executive-summary` |
| | Customer Stories Shortlist | `ibm-bid-customer-stories` |
| **Phase 2** | Solution Architecture | `ibm-bid-solution-architect` |
| | Scope Boundaries | `ibm-bid-scope-constrainer` |
| | Staffing Plan | `ibm-bid-staffing-planner` |
| | Pricing Strategy | `ibm-bid-pricing-strategy` |
| **Phase 3** | Wireframe Creation | `ibm-bid-wireframe-creator` |
| | Answer Drafting | `ibm-bid-writer` |
| | Social Value Response | `ibm-bid-social-value-expert` |
| | Answer Evaluation | `ibm-bid-answer-evaluator` |
| **Phase 4** | TDA Review | `ibm-bid-tda-review` |
| | Fact Check and Source Validation | `ibm-bid-fact-checker` |
| | Final Evaluation | `ibm-bid-answer-evaluator` |
| | AutoRFP Packaging | `ibm-bid-autorfp-packager` |

For mid-bid document updates and clarification responses, see [Handling New Information Mid-Bid](#handling-new-information-mid-bid).

## Handling New Information Mid-Bid

When clarification answers arrive, the ITT is amended, or new documents are
provided at any point in the workflow, use the source change impact pipeline
rather than manually reopening work items.

### Step 1 — Register the new document as a revised source

If the document is new:

```bash
uv run $SKILL_DIR/scripts/bid_state.py create-source \
  --path ./inputs/clarification_responses.md \
  --title "Clarification Responses Round 1" \
  --doc-type clarification_response \
  --purpose "Client answers to our Phase 0 clarification questions"
```

If it replaces a document already registered (e.g. ITT v2, amended pricing schedule):

```bash
uv run $SKILL_DIR/scripts/bid_state.py revise-source-document SRC-0001 \
  --path ./inputs/itt_v2.pdf \
  --version-label v2
```

### Step 2 — Review the proposed impacts

```bash
uv run $SKILL_DIR/scripts/bid_state.py review-impacts SRCV-0002
```

The engine applies the impact rules from `assets/impact-rules/default.yaml` and
lists every work item it thinks is affected, with the policy it would apply.

### Step 3 — Approve or reject each impact

```bash
uv run $SKILL_DIR/scripts/bid_state.py approve-impact IMP-0017 --reviewed-by "human"
uv run $SKILL_DIR/scripts/bid_state.py reject-impact IMP-0018 --reviewed-by "human" --reason "Unrelated section"
```

Human review is the gate. Reject impacts where the new document genuinely does
not touch that work item.

### Step 4 — Apply and re-render

```bash
uv run $SKILL_DIR/scripts/bid_state.py apply-approved-impacts SRCV-0002
uv run $SKILL_DIR/scripts/bid_state.py render
```

Approved impacts flip the affected child work items to `needs_review` or
`blocked` (depending on the rule), making them re-claimable. The phase structure
is preserved — only the specific items that need rework are reopened.

### Impact rules by document type

| `--doc-type` | Impact policy | Work item types affected |
|---|---|---|
| `clarification_response` | `mark_outdated` | requirement, answer, review |
| `requirements_spreadsheet` | `block_until_refreshed` | requirement, skill_task, answer |
| `draft_contract` | `mark_outdated` | risk, skill_task, answer |
| `evaluation_criteria` | `mark_needs_review` | review, answer, skill_task |
| `technical_appendix` | `block_until_refreshed` | skill_task, answer, review |
| `pricing_schedule` | `mark_outdated` | skill_task, answer |

### Non-document insights

Verbal clarifications from a site visit, a client phone call, or an email
exchange should be captured as a short markdown note before running the pipeline:

```bash
# Write a brief summary to ./inputs/clarification_verbal_round1.md, then:
uv run $SKILL_DIR/scripts/bid_state.py create-source \
  --path ./inputs/clarification_verbal_round1.md \
  --title "Verbal Clarification — Site Visit 2026-05-06" \
  --doc-type clarification_response \
  --purpose "Key points from client call; not a formal document"
```

This keeps all insights traceable through the same impact pipeline regardless of
how they arrived.

### After rework — resuming phase progression

Once reopened work items are re-completed:

- **If they belong to the current phase**, run `bid_state.py next` — it will re-check the gate and, if all children are now complete, seal the phase and create the next one.
- **If they belong to an earlier phase** (e.g., a Phase 1 answer was flagged while you are in Phase 2), re-complete them directly. The current phase structure is unaffected and `next` is not needed — Phase 2 continues from where it was.

### Visualising Bid State

When the user asks to visualise, inspect, show, or summarise bid state:

```bash
uv run $SKILL_DIR/scripts/bid_state.py render
uv run $SKILL_DIR/scripts/bid_state.py render-graph
uv run $SKILL_DIR/scripts/bid_state.py show WI-0001 --children
uv run $SKILL_DIR/scripts/bid_state.py list-assets
uv run $SKILL_DIR/scripts/bid_state.py context
```

- `./tmp/ibm-bid-project.md` — primary readable dashboard of project, work items, row versions, tags, statuses, parents, and open impacts
- `./tmp/ibm-bid-project-graph.mmd` — Mermaid dependency graph generated from live state
Do not hand-draw state diagrams from memory. Regenerate the dashboard and graph,
then summarise work-item status, assets, and next claimable work.

The legacy markdown template remains available for migration and compatibility:
- `references/legacy-ibm-bid-project-template.md`

When migrating older projects, treat the markdown as draft input, not trusted canonical state. The legacy template fields include:
- `tender_name`
- `tender_value`
- `client`
- `tender_type`
- `submission_deadline`
- `source_documents` (all primary and additional source documents provided by the user, with a short note on relevance)
- `current_phase` (opportunity_assessment | strategic_positioning | solution_architecture | content_development | technical_assurance)
- `routing_tag` (optional single work routing tag, normally a skill identifier such as ibm-bid-writer or ibm-bid-fact-checker)
- `requirements_analysis_status` (not_started | complete | refresh_required)
- `requirements_analysis_artifact` (path to the requirements analysis file, normally `./tmp/ibm-bid-requirements-analysis.md`)
- `qualification_status` (not_started | complete | refresh_required)
- `qualification_artifact` (path to the qualification file, normally `./tmp/ibm-bid-qualification.md`)
- `qualification_score` (0-100)
- `qualification_recommendation` (strong_go | proceed_with_caution | mitigation_required | recommend_no_bid)
- `strategic_positioning_status` (not_started | complete | refresh_required)
- `strategic_positioning_artifact` (path to the strategic positioning file, normally `./tmp/ibm-bid-strategic-positioning.md`)
- `strategic_recommendations` (short bullets covering the selected sales strategy and positioning priorities)
- `competitor_analysis_status` (not_started | complete | refresh_required)
- `competitor_analysis_artifact` (path to the competitor analysis file, normally `./tmp/ibm-bid-competitor-analysis.md`)
- `competitor_priority_threats` (top 1-3 named competitors or archetypes)
- `competitor_hypotheses` (short bullets capturing likely competitor moves or incumbent defences)
- `clarifications_status` (not_started | drafted | submitted | answered | closed)
- `clarifications_artifact` (path to the clarifications file, normally `./tmp/ibm-bid-clarifications.md`)
- `clarification_questions_count` (number of open or generated clarification questions)
- `legal_assessment_status` (not_started | complete | refresh_required)
- `legal_assessment_artifact` (path to the legal assessment file, normally `./tmp/ibm-bid-legal-assessment.md`)
- `legal_risk_rating` (RED | AMBER | GREEN, or equivalent)
- `client_language_analysis_status` (not_started | complete | refresh_required)
- `client_language_analysis_artifact` (path to the language profile file, normally `./tmp/ibm-bid-client-language-analysis.md`)
- `client_language_analysis_documents` (documents analysed for client vocabulary, tone, and phraseology)
- `hot_buttons_status` (not_started | complete | refresh_required)
- `hot_buttons_artifact` (path to the hot buttons file, normally `./tmp/ibm-bid-hot-buttons.md`)
- `key_client_priorities` (the 5 extracted hot buttons)
- `win_themes_status` (not_started | complete | refresh_required)
- `win_themes_artifact` (path to the win themes file, normally `./tmp/ibm-bid-win-themes.md`)
- `win_themes_count` (number of generated win themes)
- `candidate_customer_stories_artifact` (path to the review pool file, normally `./tmp/ibm-bid-candidate-customer-stories.md`)
- `candidate_customer_stories` (around 10 candidate stories by ID/title for review against the win themes)
- `approved_customer_stories_artifact` (path to the approved shortlist file, normally `./tmp/ibm-bid-approved-customer-stories.md`)
- `approved_customer_stories` (3-5 shortlisted stories by ID/title chosen to best evidence the win themes)
- `executive_summary_status` (not_started | complete | refresh_required)
- `executive_summary_artifact` (path to the executive summary file, normally `./tmp/ibm-bid-executive-summary.md`)
- `wireframe_status` (not_started | in_progress | complete | refresh_required)
- `wireframe_artifacts` (paths to generated wireframe files)
- `questions_answered` (question references or filenames already drafted)
- `next_question_to_draft` (next question reference or filename)
- `social_value_status` (not_started | in_progress | complete | refresh_required)
- `social_value_artifacts` (paths to social value response files)
- `social_value_questions_answered` (social value question references already drafted)
- `scope_boundaries_status` (not_started | applied | refresh_required)
- `scope_boundaries_artifact` (path to the scope constrainer file, normally `./tmp/ibm-bid-scope-constrainer.md`)
- `evaluation_status` (not_started | in_progress | pass | revise | final_complete)
- `evaluation_artifact` (path to latest evaluation report, normally `./tmp/ibm-bid-responses/evaluation_report.md`)
- `latest_evaluation_score` (latest score or score summary)
- `final_evaluation_artifact` (path to final evaluation report, normally `./tmp/ibm-bid-final-evaluation.md`)
- `tda_status` (not_started | complete | refresh_required)
- `tda_artifact` (path to the TDA review file, normally `./tmp/ibm-bid-tda-review.md`)
- `tda_risk_rating` (LOW | MEDIUM | HIGH)
- `tda_critical_findings` (highest-priority TDA findings)
- `key_risks` (bullets, max 5)
- `artifacts_generated` (list of ./tmp/ files)
- `next_skill_recommendation`
- `required_skills_remaining` (list of skills not yet executed)

If `./tmp/ibm-bid-project.sqlite` exists, use `bid_state.py show`, `next`, and
`context show` to answer "what's next?" with minimal context drift. If only the
legacy markdown exists, migrate or treat it as draft context.

## Quality Gate Checks

Before proceeding between phases, confirm gate criteria:

### Quality Gate 1: GO/NO-GO (After Phase 0)
- **Score 81-100**: Strong opportunity - prioritize resources
- **Score 61-80**: Good opportunity - proceed with caution
- **Score 41-60**: Medium risk - mitigation strategy required
- **Score 0-40**: High risk - recommend no-bid

Gate 1 must pass before investing effort in Phases 1-4.

### Quality Gate 2: Technical Assurance (After Phase 4)
- **TDA Risk Rating**: LOW (GO) / MEDIUM (Conditional) / HIGH (Escalate)
- **Answer Scores**: All ≥3 (PASS) / Any <3 (Review) / Any <2 (Fail)

Gate 2 validates technical quality before final submission.

For detailed gate criteria, see [quality-gates.md](references/quality-gates.md).

## How This Skill Works

This skill helps you determine which bid skills to use based on:

1. **Your current phase** (0: Opportunity Assessment → 1: Strategic Positioning → 2: Solution Architecture → 3: Content Development → 4: Technical Assurance)
2. **Your stage** (just received RFP, drafting responses, final review)
3. **Your quality gate status** (pre-qualification, post-qualification, pre-submission)

## Quick Navigation

### By Current Situation

**"I just received..."** (Use these FIRST - Phase 0)
- A requirements spreadsheet or need a structured checklist → **Start with ibm-bid-requirements-extractor** (creates ./tmp/ibm-bid-requirements_extractor.md from PDF/DOCX/XLSX/CSV/TSV)
- A new RFP/ITT → **Start with ibm-bid-requirements-analysis** (extract and analyze tender requirements)
- After requirements analysis → **Run ibm-bid-strategic-positioning** (strategic analysis, sales strategy, price-to-win)
- Need to know who we are really up against or how rivals will attack → **Also run ibm-bid-competitor-analysis** (named competitor review, open-field likely bidder analysis, black-hat review, public-source competitor intelligence)
- An RFP with ambiguous requirements → **Also run ibm-bid-clarifications** (identify questions for client)
- A high-value opportunity (>£5M) → **Also run ibm-bid-qualification** (score against 20 criteria)
- Draft contract terms or legal schedules → **Also run ibm-bid-legal-assessment** (identify legal/commercial risks and clarifications)

**"I'm working on..."** (Use these DURING - Phases 1-3)
- Client motivations and buying priorities → **ibm-bid-hot-buttons** (extract 5 client hot buttons from procurement language)
- Client language, tone, and vocabulary analysis → **ibm-bid-client-language-analysis** (build a language profile so ibm-bid-writer mirrors the client's own style)
- Strategic positioning → **ibm-bid-win-themes** (generate Shipley-compliant themes)
- Competitor-led positioning or black-hat review → **ibm-bid-competitor-analysis** (pressure-test positioning, attack lines, counter-moves, response surgery)
- Executive summary → **ibm-bid-executive-summary** (write compelling summary)
- Salesforce solution design → **ibm-sf-solution-architect** (technical solution document)
- Non-Salesforce solution design → **ibm-bid-solution-architect** (infrastructure/cloud/cyber solution)
- Support model sizing → **ibm-sf-ams** (calculate FTE requirements)
- High-level solution overview → **ibm-bid-solution-overview** (concise architecture overview for executive summaries or high-level technical positioning)
- Delivery staffing and cost baseline → **ibm-bid-staffing-planner** (team shape, duration, cost, price, GP/GP%, location mix)
- Pricing strategy / commercial model → **ibm-bid-pricing-strategy** (value-based contracting, price-to-win scenarios, margin, TCO, concessions, negotiation guardrails)
- Offering alignment → **ibm-bid-offerings-advisor** (map requirements or business needs to IBM offerings)
- Structuring complex question responses → **ibm-bid-wireframe-creator** (create "How we..." wireframe with hot button/win theme mapping)
- Answering tender questions → **ibm-bid-writer** (draft responses with evidence)
- Social value questions (UK public sector) → **ibm-bid-social-value-expert** (TOMs framework, measurable commitments, scoring-aligned)
- Visual recommendations for bid answers → **ibm-bid-image-definer** (optional: AI-ready image-generation prompts to strengthen a drafted answer)
- Word count against tender limits → **ibm-bid-word-count** (strips markdown syntax, counts evaluator-facing content only)

**"I need to review..."** (Use these FOR ASSURANCE - Phase 4)
- Answer quality → **ibm-bid-answer-evaluator** (score against 5-point scale)
- Factual accuracy and source support → **ibm-bid-fact-checker** (validate claims, metrics, capabilities, and assertions against source documents)
- Technical architecture → **ibm-bid-tda-review** (Technical Design Authority review)
- Final submission readiness → **Final ibm-bid-answer-evaluator pass** (comprehensive review)

## Diagnostic Questions

When the user's needs are unclear, ask:

1. **What stage are you at?**
   - Just received RFP (→ Phase 0)
   - Drafting responses (→ Phase 3)
   - Final review before submission (→ Phase 4)
   - Need to decide bid/no-bid (→ ibm-bid-qualification)

2. **Have you completed Phase 0 (Opportunity Assessment)?**
   - No (→ Start with ibm-bid-requirements-analysis, then ibm-bid-strategic-positioning)
   - Yes, scored <60 (→ Review qualification, consider no-bid)
   - Yes, scored ≥60 (→ Proceed to Phase 1)

3. **Do you have existing artifacts?**
   - None (→ Start at Phase 0)
   - Analysis complete (→ Phase 1)
   - Win themes complete but candidate story pool missing (→ create review pool first)
   - Candidate story pool ready but approved shortlist not yet reviewed/finalised (→ review and finalise approved subset before Phase 3)
   - Win themes complete with approved story shortlist (→ Phase 2/3)
   - Responses drafted (→ Phase 4)

4. **Do you need a requirements checklist or have a requirements spreadsheet?**
   - Yes (→ ibm-bid-requirements-extractor, then proceed to Phase 0 Step 1)
   - No (→ proceed to ibm-bid-requirements-analysis)
5. **Do you have draft contract terms or legal schedules?**
   - Yes (→ ibm-bid-legal-assessment in Phase 0 Step 2)
   - No (→ proceed without legal assessment)
6. **Do you need competitor intelligence or a black-hat review?**
   - Yes (→ ibm-bid-competitor-analysis in Phase 0 Step 2, and optionally again in Phase 1/3 to pressure-test drafts)
   - No (→ proceed without competitor-specific analysis)
7. **Do you need to structure complex responses before drafting?**
   - Yes (→ prepare ibm-bid-hot-buttons in Phase 1, then use ibm-bid-wireframe-creator in Phase 3)
   - No (→ draft directly with ibm-bid-writer)
8. **Do you need staffing, price, or commercial model support?**
   - Staffing/team shape/cost/GP (→ ibm-bid-staffing-planner)
   - Pricing strategy/value-based model/discounts/concessions/negotiation guardrails (→ ibm-bid-pricing-strategy)

Based on answers, recommend specific skills and sequences.

## The 5 Phases

### Phase 0: OPPORTUNITY ASSESSMENT (Optional pre-step, then Sequential/Parallel)
Understand the opportunity and decide GO/NO-GO before investing significant effort.

**Step 0 - Requirements Extraction (optional, run first if needed):**
- **ibm-bid-requirements-extractor** - Extract and structure requirements into a TODO checklist
  - Document or spreadsheet extraction (PDF/DOCX/XLSX/CSV/TSV)
  - Output: ./tmp/ibm-bid-requirements_extractor.md
  - Use when: RFP requirements are in spreadsheets or when you need a structured checklist before analysis

**Step 1 - Requirements Analysis** (run first if Step 0 not used, otherwise run next):
- **ibm-bid-requirements-analysis** - Extract and analyze tender requirements
  - Document extraction (PDF/DOCX processing)
  - Level 1: Client profile, stated requirements, evaluation criteria
  - Level 2: Operational gaps, capability deficits, risk profile, competitive landscape
  - Output: ./tmp/ibm-bid-requirements-analysis.md

**Step 2 - Strategic & Qualification** (run in parallel, after Step 1):
- **ibm-bid-strategic-positioning** - Strategic analysis and commercial positioning
  - Level 3: Executive decision drivers, transformation vs BAU assessment
  - Sales strategy selection (Attack/Position strategies)
  - Price-to-win analysis (5 viewpoints)
  - Win theme inputs preparation
  - Output: ./tmp/ibm-bid-strategic-positioning.md
- **ibm-bid-competitor-analysis** - Identify likely competitors, incumbent advantage, black-hat attack lines, and IBM counter-positioning
  - Input: ./tmp/ibm-bid-requirements-analysis.md
  - Optional inputs: ./tmp/ibm-bid-strategic-positioning.md, draft answers, win themes, public-source research
  - Output: ./tmp/ibm-bid-competitor-analysis.md
- **ibm-bid-clarifications** - Identify ambiguous requirements requiring client clarification
  - Input: ./tmp/ibm-bid-requirements-analysis.md
- **ibm-bid-qualification** - Score against 20 criteria (client maturity, justification, momentum, relationships, reputation, differentiators, commercial viability)
  - Input: ./tmp/ibm-bid-requirements-analysis.md
- **ibm-bid-legal-assessment** - Assess UK government tender documents and draft contracts against IBM legal risk criteria
  - Input: ITT/contract schedules/framework terms (often within the RFP pack)
  - Output: ./tmp/ibm-bid-legal-assessment.md

**When to use Phase 0:**
- Immediately upon RFP receipt
- Before committing resources to bid development
- For all opportunities >£1M
- If requirements are in a spreadsheet or need a checklist: run ibm-bid-requirements-extractor first

**Quality Gate 1 Checkpoint:**
- Review qualification score
- Review strategic positioning and price-to-win
- Review competitor analysis threat view and counter-positioning (if performed)
- Review legal assessment for RED/AMBER risks (if performed)
- Assess red flags and risks
- Make GO/NO-GO decision
- Document recommendation

### Phase 1: STRATEGIC POSITIONING (Sequential Execution)
Develop competitive positioning and strategic messaging.

**Skills** (run sequentially):
- **ibm-bid-hot-buttons** - Extract exactly 5 client hot buttons to anchor client-priority messaging
- **ibm-bid-client-language-analysis** - Optional but recommended: analyse client documents to build a vocabulary, tone, and phrase profile for ibm-bid-writer to mirror
- **ibm-bid-competitor-analysis** - Optional but recommended black-hat checkpoint to convert threat hypotheses into counter-positioning and response surgery
- **ibm-bid-win-themes** - Generate Shipley-compliant win themes, create a review pool in `./tmp/ibm-bid-candidate-customer-stories.md`, then lock the approved subset into `./tmp/ibm-bid-approved-customer-stories.md`
- **ibm-bid-executive-summary** - Write compelling executive summary (typically 1000 words/2 pages max) using four-part structure

**When to use Phase 1:**
- After Phase 0 qualification (GO decision)
- Before detailed solution architecture
- For bids requiring executive summary or oral presentation
- To establish competitive positioning

**Integration:**
- Hot buttons provide client-language anchors for win-theme and writing teams
- Client language analysis produces `./tmp/ibm-bid-client-language-analysis.md` and should be recorded through `bid_state.py` as an artifact or work item update before rendering the dashboard.
- ibm-bid-writer should use the current work-item context pack first; if no client language artifact is present there, it must fall back to `./tmp/ibm-bid-client-language-analysis.md`.
- Win themes also establish a candidate customer story pool for human review and then an approved shortlist that Phase 3 must reuse without expanding unless the shortlist is deliberately refreshed
- Competitor analysis sharpens differentiators, rebuttals, and proof priorities before themes are locked
- Win themes inform executive summary
- Both leverage ibm-bid-requirements-analysis and ibm-bid-strategic-positioning outputs
- Both use ibm-bid-customer-stories for proof points
- Both reference ibm-bid-strategy-and-capabilities-2026 for IBM capabilities

### Phase 2: SOLUTION ARCHITECTURE (Conditional - Technical Bids Only)
Design technical solution architecture, support model, staffing baseline, and commercial model where required.

**Skills** (run sequentially as needed):
- **ibm-bid-scope-constrainer** - Transform open-ended or vague requirements into bounded statements before designing a solution (reduces estimate uncertainty 25-45%)
- **ibm-bid-offerings-advisor** - Map requirements to IBM offering shortlist; identify fit, gaps, and questions before committing to a solution approach
- **ibm-sf-solution-architect** - Generate comprehensive Salesforce solution document (16 sections) — use for Salesforce implementations
- **ibm-sf-ams** - Calculate Application Management Services FTE requirements (if ongoing support required)
- **ibm-bid-solution-architect** - Generate technology-agnostic solution document (15 sections) — use for non-Salesforce technical bids
- **ibm-bid-solution-overview** - High-level architecture overview (up to 15 sections, 10,000 words) — use when a concise technical summary is needed rather than a full detailed solution
- **ibm-bid-staffing-planner** - Build bid-ready staffing plan with team shape, duration, cost, price, GP, GP%, and location mix
- **ibm-bid-pricing-strategy** - Develop pricing strategy, value-based contracting model, TCO/margin scenarios, concession strategy, and negotiation guardrails

**When to use Phase 2:**
- For technical implementation bids requiring solution architecture
- Use commercial modelling for: bids with pricing schedules, staffing assumptions, managed services, value-based contracting, gain-share, discounts, or negotiation pressure
- Skip technical architecture for: framework agreements, managed services only, professional services bids
- After strategic positioning (Phase 1) complete
- Before detailed question responses (Phase 3)

**Integration:**
- Scope constrainer bounds open-ended requirements before solution design begins
- Offerings advisor maps requirements to IBM portfolio before committing to architecture approach
- Solution architecture informs technical responses in Phase 3
- AMS estimate provides commercial model for ongoing support
- Staffing planner provides the internal cost and GP baseline for pricing strategy
- Pricing strategy converts internal cost into client-facing commercial model and negotiation guardrails
- Validates feasibility before committing to detailed responses

### Phase 3: CONTENT DEVELOPMENT (Iterative Execution)
Draft and refine tender question responses.

**Skills** (iterate until quality threshold met):
- **ibm-bid-wireframe-creator** - Break each question into "How we..." sections and map hot buttons/win themes before drafting
- **ibm-bid-competitor-analysis** - Optional draft black-hat review when you need to identify exploitable weaknesses before rewriting
- **ibm-bid-writer** - Draft responses following best practices (client-focused, evidence-based, structured)
- **ibm-bid-social-value-expert** - Draft social value responses for UK public sector tenders (TOMs framework, measurable commitments, governance); uses ibm-bid-writer internally — invoke in place of ibm-bid-writer for social value questions
- **ibm-bid-image-definer** - Optional: define AI-ready image-generation prompts and visual recommendations for drafted answers
- **ibm-bid-word-count** - Check response word count against tender limits (strips markdown, counts evaluator-facing content only)
- **ibm-bid-answer-evaluator** - Score responses against 5-point scale (0=Non-responsive to 5=Outstanding)

**When to use Phase 3:**
- After Phase 1 strategic positioning complete
- After Phase 2 solution architecture (if applicable)
- For all bids requiring written question responses

**Iteration Loop:**
1. Wireframe creator structures response sections and strategic mapping
2. Writer (or ibm-bid-social-value-expert for social value questions, which uses ibm-bid-writer internally) drafts response
3. ibm-bid-word-count checks word count against tender limit (required before evaluation when a limit applies)
4. Evaluator scores response
5. If score <3: Revise (return to writer with feedback)
6. If score ≥3: Proceed to next question or Phase 4

**Integration:**
- Wireframe creator sets section structure and strategic mapping before writing
- Writer leverages ibm-bid-library (3000+ historical responses via FTS5 search)
- Writer uses ibm-bid-customer-stories (857 stories via FTS5 search)
- Writer references ibm-bid-strategy-and-capabilities-2026 (IBM capabilities)
- Writer incorporates win themes from Phase 1
- Competitor analysis can be re-run on drafts to identify open attack surfaces and required response surgery
- Writer references solution architecture from Phase 2
- Evaluator provides objective quality assessment

### Phase 4: TECHNICAL ASSURANCE (Parallel Execution)
Validate technical quality and submission readiness.

**Skills:**

Run in parallel:
- **ibm-bid-tda-review** - Technical Design Authority review from Lead Enterprise Architect perspective (requirements alignment, scalability, security, integration complexity, operational readiness, technology risk)
- **Final ibm-bid-answer-evaluator pass** - Comprehensive review of all responses
- **ibm-bid-fact-checker** - Source-grounding review for claims, metrics, capabilities, and assertions where factual support matters

Run sequentially after all content is finalised:
- **ibm-bid-autorfp-packager** - Package bid answer-intent records and shared context into validated AutoRFP markdown documents per requirement (requires Phase 3 Q*.md outputs to be complete)

**When to use Phase 4:**
- After Phase 3 content development complete
- Before final submission
- For all bids >£5M (mandatory)
- For bids with complex technical architecture
- For bids with generated claims, metrics, client references, or compliance assertions that need source verification

**Quality Gate 2 Checkpoint:**
- Review TDA risk rating (LOW/MEDIUM/HIGH)
- Review answer evaluator scores (all ≥3)
- Review fact-check findings and correct unsupported claims
- Address any HIGH risks or failing scores
- Final submission decision

**Integration:**
- TDA reviews solution architecture from Phase 2
- Evaluator reviews all responses from Phase 3
- Fact checker validates response claims against source documents
- Both inform final submission quality

## Supporting Resources (Available Throughout)

These skills/resources support the entire workflow:

**Knowledge Bases:**
- **ibm-bid-library** - 3000+ historical bid responses, technical documentation, policy documents (SQLite with FTS5 full-text search)
- **ibm-bid-customer-stories** - 857 IBM customer success stories with quantified outcomes across industries and Salesforce clouds (SQLite with FTS5 search)
- **ibm-bid-strategy-and-capabilities-2026** - IBM 2026 strategy including AI capabilities, cloud services, cybersecurity, Salesforce partnership, IBM Garage methodology, Client Zero transformation story
- **ibm-bid-offerings-advisor** - IBM offering shortlist and requirement-to-offering mapping from the local offerings corpus
- **ibm-bid-competitor-analysis** - Public-source competitor intelligence and black-hat review for likely bidder analysis, attack lines, and IBM counter-positioning

**Salesforce Expertise** (when solution involves Salesforce):
- **ibm-sf-help** - Search Salesforce Help Center documentation (FTS5 search)
- **ibm-sf-architect** - Salesforce architecture patterns and design best practices from architect.salesforce.com

**Presentation Skills** (for oral presentations/pitches):
- **ibm-story-pitch-development** - Business pitch structures
- **ibm-story-stakeholder-mapping** - Map decision-makers
- **ibm-story-presentation-structuring** - Presentation architecture
- **ibm-story-visual-narrative** - Slide design
- **ibm-story-speaker-performance** - Delivery mechanics

**Legal Risk (UK Government)**
- **ibm-bid-legal-assessment** - Legal/commercial risk review for ITTs and contract schedules (UK public sector)

**Commercial And Pricing**
- **ibm-bid-staffing-planner** - Staffing plan, delivery duration, cost, price, GP/GP%, location mix, and scenario comparisons
- **ibm-bid-pricing-strategy** - Commercial model selection, value-based contracting, internal cost-to-client-price translation, TCO/margin scenarios, discount/tradeable strategy, and negotiation guardrails

**Additional Assurance**
- **ibm-bid-fact-checker** - Verify generated bid content against RFP/ITT/source documents to prevent unsupported claims or hallucinated metrics

## Common Workflows

For detailed workflows with specific sequences, see [workflows.md](references/workflows.md).

For comprehensive skill descriptions and decision logic, see [skill-matrix.md](references/skill-matrix.md).

## Integration Principles

Skills work together in documented phases:
- **Phase 0 Step 1 feeds Step 2** → Requirements analysis informs strategic positioning
- **Phase 0 Step 2 legal review informs Gate 1** → Legal risks drive GO/NO-GO and clarifications
- **Phase 0 competitor review sharpens Phase 1** → Competitor threats and counter-positioning tighten win themes and executive summary
- **Phase 0 feeds Phase 1** → Requirements + strategic analysis inform hot buttons and win themes
- **Phase 1 feeds Phase 2** → Win themes guide solution architecture decisions
- **Phase 1 feeds Phase 3** → Hot buttons + win themes feed wireframe planning
- **Phase 2 feeds Phase 3** → Solution architecture informs technical responses
- **Staffing feeds pricing** → Staffing planner output provides cost, price, GP, duration, and location mix for pricing strategy
- **Pricing feeds Phase 3** → Pricing strategy informs commercial responses, pricing narratives, assumptions, concessions, and negotiation-ready language
- **Phase 3 validates against Phase 1** → Responses align with win themes
- **Phase 4 validates Phases 2-3** → Technical assurance reviews architecture and responses

Use multiple skills in sequence for complex bids. Single skills work for focused needs (e.g., just answer evaluation, just qualification).

## Document Flow Convention

**Standard ./tmp/ locations:**
```
./tmp/ibm-bid-requirements_extractor.md (Optional pre-step checklist)
./tmp/ibm-bid-requirements-analysis.md (Phase 0 Step 1)
./tmp/ibm-bid-strategic-positioning.md (Phase 0 Step 2)
./tmp/ibm-bid-competitor-analysis.md
./tmp/ibm-bid-clarifications.md
./tmp/ibm-bid-qualification.md
./tmp/ibm-bid-legal-assessment.md
./tmp/ibm-bid-hot-buttons.md
./tmp/ibm-bid-client-language-analysis.md
./tmp/ibm-bid-win-themes.md
./tmp/ibm-bid-executive-summary.md
./tmp/ibm-sf-solution/complete_solution.md (if Salesforce solution architecture)
./tmp/ibm-bid-solution/complete_solution.md (if non-Salesforce solution architecture)
./tmp/ibm-sf-ams-estimation.md
./tmp/ibm-bid-staffing-planner.md
./tmp/ibm-bid-pricing-strategy-baseline.xlsx
./tmp/ibm-bid-pricing-strategy-scenarios.xlsx
./tmp/ibm-bid-pricing-strategy-sensitivity.xlsx
./tmp/ibm-bid-wireframe-Q01.md
./tmp/ibm-bid-responses/Q01_technical_approach.md
./tmp/ibm-bid-responses/Q02_delivery_methodology.md
./tmp/ibm-bid-responses/evaluation_report.md
./tmp/ibm-bid-tda-review.md
./tmp/ibm-bid-final-evaluation.md
./tmp/ibm-bid-project.md (GENERATED DASHBOARD)
```

**Final ./outputs/ deliverables:**
```
./outputs/executive_summary.docx
./outputs/technical_responses.docx
./outputs/solution_architecture.pdf
./outputs/submission_checklist.md
```

## Output Format

Write a compact navigation artifact (1-2 pages) to `./tmp/ibm-bid-navigator.md` with this structure:

- **Tender Summary** (name, value, client, type, deadline)
- **Source Documents** (list every source document provided by the user, including any additional supporting documents beyond the core RFP/ITT pack, with a short note on purpose or relevance)
- **Current Phase** (0-4)
- **Phase Status** (completed phases, current phase, remaining phases)
- **Quality Gate Status** (Gate 1 score/decision, Gate 2 pending/complete)
- **Artifacts Generated** (list of ./tmp/ files with status)
- **Client Language Analysis** (status, artifact path, documents analysed, and whether the profile needs refresh)
- **Next Recommended Skill** (specific skill name + rationale)
- **Required Skills Remaining** (skills not yet executed in workflow)
- **Key Risks/Blockers** (if any)
- **Estimated Completion** (phase completion % only - no time estimates)

Use `bid_state.py` to update canonical state after each phase transition, then
run `bid_state.py render` to regenerate `./tmp/ibm-bid-project.md`.
For bid agents, `create-source --title ... --doc-type ...
--purpose ...` and `add-children --titles ...` are supported wrapper shortcuts.
Use `list-assets` or `list-assets --json` to inspect registered source
documents.
Use bare `context` to list available context targets. `context WI-0002` shows an
existing context pack, and `context build WI-0002` is a shortcut for
`context build --work-item WI-0002`.
If `claim`, `complete`, `heartbeat`, or `release` omit `--agent-id`, the wrapper
uses `BID_AGENT_ID`, `AGENT_ID`, `CLINE_AGENT_ID`, `CLAUDE_AGENT_ID`, or
`bid-navigator-agent`.
