# Legal Assessment Methodology

Use this reference to run the review consistently. It defines the two-phase method, confidence schema, fail-closed rules, and standard output contract for `ibm-bid-legal-assessment`.

## Review Principles

- **Evidence first**: Every material finding must be tied to a section, schedule, annex, or page citation.
- **Separate fact from posture**: State what the contract says before classifying it as RED, AMBER, or GREEN.
- **Fail closed**: If the evidence does not support a conclusion, mark the point as silent, ambiguous, conflicting, or unresolved.
- **Framework-aware**: Measure call-off terms against the baseline framework position and flag departures explicitly.
- **Targeted depth**: Deep-dive only where evidence quality is weak or conflicts remain unresolved after the first pass.

## Two-Phase Review Model

### Phase 1: Broad Factual Pass

Review the full document set across all fifteen legal categories in one pass. For each category capture:

- Whether the term is present, absent, or unclear
- A short factual summary of what the contract says
- One or more citations
- Confidence signals
- Any obvious conflict, hierarchy issue, or missing core element

Phase 1 should also capture contract-level metadata:

- Contract title
- Parties
- Contract type and reference
- Framework or procurement route
- Value and currency, if stated
- Term and expiry, if stated

### Phase 2: Targeted Refinement

Run a second pass only for categories that remain weak after Phase 1. Typical triggers:

- Low overall confidence
- Ambiguous or implied wording
- Possible conflict between body text and schedules
- Missing core elements that should exist
- Sparse or weak citations

For each flagged category, revisit only the relevant text and attempt to materially improve the finding. If the second pass does not materially improve the evidence position, keep the item unresolved instead of forcing a conclusion.

## Material Improvement Test

Treat a Phase 2 refinement as successful only if it does at least one of the following:

- Resolves a contradiction or confirmed override using stronger evidence
- Separates baseline obligations from conditional or triggered obligations
- Converts uncertainty into evidence-backed absence, such as "not specified in the reviewed documents"
- Finds a previously missed core term with clear supporting citations

If none of those happen, record the category as unresolved and explain why briefly.

## Confidence Signals

Use the following confidence signals for every category. These signals describe reliability of the evidence, not the legal quality of the clause.

### Evidence Strength

- **Explicit**: directly stated in clear contractual language
- **Implicit**: derivable only by combining clauses or definitions
- **Ambiguous**: present but unclear, conditional, or internally inconsistent
- **Absent**: not found in the reviewed material

### Citation Density

- **High**: multiple clear citations support the finding
- **Medium**: one primary citation supports the finding
- **Low**: weak, indirect, or incomplete citation support

### Conflict or Override Status

- **None detected**
- **Possible conflict**
- **Confirmed override**

If a conflict or override exists, state the competing sections factually.

### Overall Confidence

- **High**
- **Medium**
- **Low**

### Struggle Indicator

State `Yes` or `No`.

If `Yes`, give one reason only:

- Missing information
- Conflicting language
- Implied obligation
- Unclear scope or thresholds

## Risk Classification

After the factual extraction is stable, classify the issue using IBM posture:

- **RED**: bid blocker or materially unacceptable legal/commercial exposure
- **AMBER**: significant risk requiring mitigation, clarification, pricing action, or negotiation
- **GREEN**: acceptable, standard, or manageable position

Examples:

- **RED**: unlimited liability with no acceptable carve-out control, background IP assignment, impossible security clearance model, undefined TUPE exposure with no indemnity
- **AMBER**: parent company guarantee requirement, asymmetric termination rights, unclear acceptance regime, expensive vetting obligations on IBM
- **GREEN**: market-standard caps, standard public-sector GDPR clauses, balanced termination and transition provisions

## Output Schema

Use this shape unless the user requests something narrower.

### 1. Contract Overview

- Contract type
- Parties
- Value
- Term
- Framework
- Documents reviewed

### 2. Key Findings

List the most material evidence-backed facts first. Keep these factual and concise.

### 3. Category Analysis

For each of the fifteen categories, include:

- **Status**: found, not found, unclear, or unresolved
- **Summary**: short factual statement of the term
- **Citations**: section or page references
- **Confidence signals**:
  - Evidence strength
  - Citation density
  - Conflict/override status
  - Overall confidence
  - Struggle indicator
- **Risk classification**: RED, AMBER, or GREEN
- **Rationale**: brief IBM posture statement grounded in the evidence

### 4. Framework Comparison

Identify where the draft departs from the baseline framework or expected public-sector position, especially for:

- Liability structure
- IP ownership
- Payment and acceptance mechanics
- Exit and transition support
- Security and data-handling obligations

### 5. Gaps and Ambiguities

List:

- Terms not found but normally expected
- Internal contradictions
- Incorporated documents not yet reviewed
- Categories left unresolved after Phase 2

### 6. Recommended Actions

Separate:

- Clarification questions
- Commercial mitigations
- Negotiation priorities
- IBM Legal escalations

## Category Review Prompt

When reviewing any category, ask:

1. What does the contract expressly say?
2. Where is that evidenced?
3. Is anything missing, conflicting, conditional, or overridden elsewhere?
4. How does this compare with the framework baseline?
5. What is IBM's resulting RED/AMBER/GREEN posture?

## Common Failure Modes

Watch for these recurring problems:

- Reading a schedule in isolation without checking precedence wording
- Treating tender instructions as final contract terms
- Assuming a protection exists because it is standard in the framework
- Combining multiple weak hints into an overstated conclusion
- Giving legal recommendations before the factual record is stable

## Escalation Triggers

Escalate clearly when you find:

- Unlimited or uncapped liability outside standard carve-outs
- IBM background IP transfer or overly broad licence-back obligations
- TUPE exposure with undefined workforce or uncapped indemnities
- Security, sovereignty, or data-processing obligations incompatible with IBM delivery model
- Framework call-off terms that appear to override mandatory baseline protections
