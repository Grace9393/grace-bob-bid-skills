---
name: ibm-bid-qualification
description: Evaluates IBM bid opportunities using a 20-criterion qualification framework across client maturity, justification, momentum, relationships, reputation, differentiators, and commercial viability. Use when analysing tender documents, RFPs, or opportunity assessments to determine bid/no-bid decisions, calculate qualification scores, and identify deal risks.
metadata:
  skills-required:
    - ibm-bid-requirements-analysis
  skills-suggested:
    - ibm-bid-strategic-positioning
---

# IBM Bid Qualification

Systematic framework for evaluating bid opportunities against 20 weighted criteria organised into 7 categories.

## Context Management

Write output to `./tmp/ibm-bid-qualification.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `qualification_status: complete`
- `qualification_artifact: ./tmp/ibm-bid-qualification.md`
- `qualification_score`: 0-100
- `qualification_recommendation`: strong_go, proceed_with_caution, mitigation_required, or recommend_no_bid
- `key_risks`: include the top qualification risks
- `artifacts_generated`: include `./tmp/ibm-bid-qualification.md` when the artifact is written
- `next_skill_recommendation`: the next bid step implied by the qualification outcome

## Qualification Process

1. Load criteria structure: `references/qualification_criteria.json`
2. Evaluate each criterion on 1-5 scale based on scoring standards
3. As needed, use the $ibm-bid-library or $ibm-bid-customer-stories skills to help clarify facts.
4. Calculate total score (max 100)
5. Apply decision thresholds:
   - 0-40: High risk - recommend no-bid
   - 41-60: Medium risk - requires mitigation strategy
   - 61-80: Good opportunity - proceed with caution
   - 81-100: Strong opportunity - prioritise

## Category Breakdown

**A: Client Maturity (2 criteria)**
- Incumbent status and competitive landscape
- Organisation size and scale

**B: Client Justification (3 criteria)**
- Operating model status
- Technology upgrade plans
- Leadership appointment

**C: Emotional & Buying Momentum (1 criterion)**
- Case for change strength

**D: Relationship Connections (2 criteria)**
- Decision-maker relationships
- Political and competitive landscape understanding

**E: IBM Reputation (4 criteria)**
- Delivery track record with client
- Recent transformation involvement
- Industry reputation
- Regulatory/specialist expertise

**F: Solution Differentiators (3 criteria)**
- Clear differentiators relevant to opportunity
- Solution-requirement fit
- Competitive positioning

**G: Decision Making Process Knowledge (5 criteria)**
- Bid timeline manageability
- Opportunity sizing
- Budget alignment
- Commercial framework status
- TUPE involvement

## Red Flags

Flag these issues prominently:
- Budget misalignment (criterion 18 scores 1-2)
- Missing commercial framework (criterion 19 scores 1-2)
- High TUPE complexity (criterion 20 scores 1-2)
- Poor client relationships (criterion 7 scores 1-2)
- Strong incumbent advantage (criterion 1 scores 1-2)

## Output Format

Present results in three sections:

1. **Executive Summary**: Score, recommendation, top 3 strengths, top 3 risks
2. **Detailed Assessment**: Score breakdown by category with justifications
3. **Critical Actions**: Specific steps to address red flags or improve positioning

Use plain text with clear section headings. Avoid bullet points unless listing multiple items requires it.

## Complete Tender Response Workflow

This skill is part of the 5-phase IBM Bid Management workflow.

**Current Phase**: Phase 0 (Opportunity Assessment)
**Position**: Step 2 - Parallel execution with ibm-bid-strategic-positioning and ibm-bid-clarifications (after ibm-bid-requirements-analysis)

See ibm-bid-navigator for complete workflow guidance.

## Integration with Other Skills

### Required Inputs
- **ibm-bid-requirements-analysis**: ./tmp/ibm-bid-requirements-analysis.md (provides client profile, requirements, risk profile)
- **ibm-bid-strategic-positioning**: ./tmp/ibm-bid-strategic-positioning.md (optional - provides strategic positioning context)
- **RFP document**: Original tender document for reference

### Recommended Next Steps

**After qualification:**

**If score 81-100 (STRONG GO)**:
- Proceed immediately to **ibm-bid-win-themes** (Phase 1)
- Prioritize resources for this opportunity
- Fast-track through workflow

**If score 61-80 (GO)**:
- Proceed to **ibm-bid-win-themes** (Phase 1) with standard resource allocation
- Monitor identified risks throughout bid development
- Consider mitigation strategies for medium-risk areas

**If score 41-60 (CONDITIONAL)**:
- Review with Practice Lead before proceeding
- Develop mitigation plan for red flags
- If mitigation plan approved, proceed to **ibm-bid-win-themes** (Phase 1)
- If mitigation not feasible, document no-bid decision

**If score 0-40 (NO-GO)**:
- Document no-bid decision with rationale
- Inform stakeholders (sales, practice lead, client relationship manager)
- Consider relationship-building activities for future opportunities
- Exit bid workflow

### Supporting Resources
- **ibm-bid-library**: Search for similar opportunities to validate scoring assumptions
- **ibm-bid-customer-stories**: Reference client relationships and previous delivery track record
- **ibm-bid-strategy-and-capabilities-2026**: Validate IBM differentiators and capabilities

### Quality Gate 1: GO/NO-GO Decision

This skill directly informs Quality Gate 1. The qualification score and recommendation form the basis for the GO/NO-GO decision before investing significant effort in Phases 1-4.

**Decision Authority**:
- <£1M: Bid Manager
- £1M-£10M: Bid Manager + Practice Lead
- £10M+: Bid Manager + Practice Lead + Partnership approval
