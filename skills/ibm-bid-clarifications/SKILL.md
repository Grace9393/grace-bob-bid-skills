---
name: ibm-bid-clarifications
description: Extract clarification questions from procurement tender documents (PDF/DOCX) where requirements are ambiguous, incomplete, or need additional detail. Use when analysing RFPs, ITTs, tenders, or bid opportunities to identify gaps requiring client clarification. Supports iterative refinement by tracking previously raised questions to avoid duplication.
metadata:
  skills-required:
    - ibm-bid-requirements-analysis
---

# Bid Clarifications

Extract structured clarification questions from tender documents where client requirements need additional detail or contain ambiguities.

## Context Management

Write output to `./tmp/ibm-bid-clarifications.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `clarifications_status`: drafted, submitted, answered, or closed
- `clarifications_artifact: ./tmp/ibm-bid-clarifications.md`
- `clarification_questions_count`: number of generated or open clarification questions
- `artifacts_generated`: include `./tmp/ibm-bid-clarifications.md` when the artifact is written
- `next_skill_recommendation`: normally `ibm-bid-requirements-analysis`, `ibm-bid-qualification`, or `ibm-bid-strategic-positioning` if clarification answers change the bid view

## Workflow

### 1. Load Existing Questions (if provided)

If the user provides a spreadsheet or markdown file of existing clarification questions:
- Read and parse all previously raised questions
- Extract question text, status (raised/answered), and any responses
- Store in memory to prevent duplication

### 2. Analyse Tender Document

Read the tender document systematically:
- Extract requirements, evaluation criteria, technical specifications, and commercial terms
- Identify sections with insufficient detail, ambiguity, or contradictions
- Flag undefined acronyms, missing processes, or gaps in requirements
- Note any requirements that conflict with standard practice or each other

### 3. Generate Clarification Questions

For each ambiguity or gap, create a question that:
- References the specific document section/page number
- Clearly states what information is missing or unclear
- Explains why the clarification matters (impact on solution design, pricing, risk)
- Suggests the expected level of detail required in the response

Categorise questions by:
- **Technical**: Solution requirements, specifications, integration points, standards
- **Commercial**: Pricing models, payment terms, contract structure, volumes
- **Governance**: Approval processes, reporting requirements, KPIs, SLAs
- **Timeline**: Key dates, milestones, mobilisation periods
- **Resources**: Client-provided assets, access, data, infrastructure

### 4. De-duplicate Against Existing Questions

Compare each new question against previously raised questions:
- Skip if substantially similar question already raised
- If related but different angle, note the relationship
- If previous question was answered, incorporate answer into context

### 5. Output Format

Generate markdown file with structure:

```markdown
# Clarification Questions - [Tender Name]
Generated: [Date]

## Summary
- New questions: X
- Previously raised: Y (not repeated)
- Categories: Technical (X), Commercial (Y), Governance (Z)...

## Technical Questions

### Q1: [Brief title]
**Document Reference:** Section X.Y, Page Z
**Question:** [Clear, specific question]
**Rationale:** [Why this matters - impact on design/pricing/risk]
**Expected Detail:** [What level of response is needed]

---

## Commercial Questions
[Same structure...]

## Previously Raised Questions
[Optional: List questions not repeated with their status]
```

### 6. Iteration Support

When provided with updated questions files:
- Mark questions as "raised" or "answered"
- Incorporate answered questions into context
- Continue extraction without re-raising answered points
- Track question evolution across iterations

## Question Quality Standards

**Specificity**: Reference exact document sections and requirements
**Actionability**: Frame questions so responses directly inform solution design or pricing
**Justification**: Always explain why the clarification is needed
**Appropriate scope**: Each question addresses one discrete topic
**Professional tone**: Neutral, non-confrontational language

## Common Ambiguity Patterns

Target these typical tender gaps:
- Undefined "current state" or legacy system details
- Missing volumetrics or transaction counts
- Unclear evaluation criteria weightings
- Ambiguous "must have" vs "should have" requirements
- Unspecified data formats, schemas, or protocols
- Missing compliance or certification requirements
- Undefined roles and responsibilities (client vs supplier)
- Unclear change management or governance processes
- Missing infrastructure or environment specifications
- Ambiguous acceptance criteria or success measures

## References

See `references/example_questions.md` for patterns and examples of well-formed clarification questions across different tender types.

## Complete Tender Response Workflow

This skill is part of the 5-phase IBM Bid Management workflow.

**Current Phase**: Phase 0 (Opportunity Assessment)
**Position**: Step 2 - Parallel execution with ibm-bid-strategic-positioning and ibm-bid-qualification (after ibm-bid-requirements-analysis)

**When to Use**:
- Complex requirements with ambiguous specifications
- Government tenders with formal clarification processes
- First-time client engagements where assumptions need validation
- Large procurements (>£5M) where requirements clarity is critical

**When to Skip**:
- Simple, well-defined RFPs
- Rebids where requirements are substantially unchanged
- Time-constrained opportunities where clarification window has closed

See ibm-bid-navigator for complete workflow guidance.

## Integration with Other Skills

### Required Inputs
- **RFP/ITT document**: Primary tender document to analyse
- **ibm-bid-requirements-analysis**: ./tmp/ibm-bid-requirements-analysis.md (provides context on client profile and requirements - optional but recommended)
- **Previous clarifications**: Existing question files to avoid duplication (if iterative)

### Recommended Next Steps

**After generating clarifications:**

1. **Review and prioritize**: Not all questions may need to be raised
   - Focus on questions that materially impact solution design or pricing
   - Consider client relationship - avoid overwhelming with excessive questions
   - Prioritize HIGH impact questions over MEDIUM or LOW

2. **Submit to client**: Follow tender clarification process
   - Respect clarification deadline (typically 7-14 days before submission)
   - Submit via required channel (procurement portal, email, etc.)
   - Track submission for compliance records

3. **Incorporate responses**: When client provides answers
   - Update ./tmp/ibm-bid-clarifications.md with responses
   - Feed clarifications into ibm-bid-requirements-analysis (update requirements understanding)
   - Use clarifications to inform ibm-bid-qualification (may impact risk assessment)

4. **Continue to Phase 0 completion**: Run in parallel or after
   - **ibm-bid-requirements-analysis** (if not already complete)
   - **ibm-bid-strategic-positioning** (may update based on clarifications)
   - **ibm-bid-qualification** (incorporates clarification insights into risk assessment)

5. **Proceed to Gate 1**: After Phase 0 complete
   - Use clarifications to inform GO/NO-GO decision
   - Major gaps in client responses may indicate heightened risk

### Supporting Resources
- **ibm-bid-library**: Search for similar tender clarifications from previous bids
- Reference previous clarification questions as templates

### Quality Gate 1 Impact

Clarification questions inform Quality Gate 1 by:
- **Identifying hidden risks**: Ambiguous requirements often hide scope or complexity risks
- **Validating assumptions**: Client responses confirm or challenge bid assumptions
- **Improving qualification accuracy**: Better understanding improves ibm-bid-qualification scoring
- **Supporting no-bid decisions**: Non-responses or concerning answers may trigger NO-GO

**Red flags from clarifications**:
- Client unwilling or unable to answer fundamental questions
- Responses reveal significantly more complexity than apparent in RFP
- Contradictory answers suggesting internal client misalignment
- Procurement process prohibits clarifications (suggests inflexible or problematic client)
