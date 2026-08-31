---
name: ibm-bid-legal-assessment
description: Assess UK government tender documents and draft contracts against IBM legal risk criteria. Use when reviewing ITT documents, framework call-offs, draft contracts, or legal schedules to identify mandatory exclusion grounds, liability issues, IP ownership terms, TUPE obligations, data protection requirements, and contractual ambiguities. Applicable to UK public sector frameworks including DOS6, TS3, G-Cloud, CCS agreements, and departmental procurements.
---

# IBM Bid Legal Assessment

Assess tender documents and contracts against IBM's legal risk framework for UK government procurements.

## Context Management

Write output to `./tmp/ibm-bid-legal-assessment.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `legal_assessment_status: complete`
- `legal_assessment_artifact: ./tmp/ibm-bid-legal-assessment.md`
- `legal_risk_rating`: RED, AMBER, GREEN, or equivalent from the assessment
- `key_risks`: include material legal or commercial risks
- `artifacts_generated`: include `./tmp/ibm-bid-legal-assessment.md` when the artifact is written
- `next_skill_recommendation`: normally `ibm-bid-qualification`, `ibm-bid-clarifications`, or `ibm-bid-strategic-positioning`

## How To Use This Skill

Use this file as the controller for the legal review. Load only the references needed for the current opportunity:

- Read `references/methodology.md` for the review method, confidence model, output schema, and fail-closed rules.
- Read the relevant framework file for baseline terms and framework-specific issues:
  - `references/dos6.md`
  - `references/ts3.md`
  - `references/gcloud.md`
  - `references/ccs.md`
  - `references/departmental.md`

Do not load every reference by default. Start with the methodology reference and the single framework that matches the procurement route.

## Core Assessment Areas

Evaluate the tender documentation across these fifteen categories:

1. **Mandatory eligibility and exclusion grounds**: PCR 2015 Regulations 57-58, declarations, ongoing compliance obligations
2. **Liability caps, indemnification, IP ownership**: liability scope, uncapped carve-outs, indemnities, insurance, ownership model
3. **Data protection and GDPR compliance**: sovereignty, controller/processor roles, breach handling, transfers, sub-processors
4. **Restrictive commercial terms**: benchmarking, MFN clauses, pricing constraints, exclusivity, volume commitments
5. **Parent company guarantees**: requirement, trigger, scope, enforcement, alternative security
6. **Security clearances and vetting**: level, scope, costs, timing, ongoing obligations, failure consequences
7. **Exit provisions and knowledge transfer**: termination asymmetry, transition assistance, wind-down, data return/deletion
8. **Acceptance testing and payment triggers**: criteria, procedures, milestones, rejection rights, deemed acceptance
9. **Subcontracting and supply chain restrictions**: approvals, transparency, onshore/offshore constraints, flow-downs
10. **Change control and scope variation mechanisms**: procedure, pricing, uncompensated change risk, approval thresholds
11. **Performance bonds and retention**: bond requirements, retention levels, working-capital exposure, release conditions
12. **Operational constraints**: key personnel, location restrictions, supplier relief, force majeure, business continuity, SLAs
13. **TUPE obligations**: transfer scope, timing, pension exposure, indemnities, consultation, employee-liability information
14. **Conflicting or ambiguous terms**: hierarchy, precedence, overrides, contradictions, amendment control
15. **Warranty periods and post-contract obligations**: warranty duration, defect correction, support tail, survival clauses

## Workflow

1. **Identify the document set**: Confirm whether the input is an ITT, call-off contract, order form, framework schedule, or supporting legal schedule set.
2. **Identify the framework**: Determine whether the opportunity is DOS6, TS3, G-Cloud, CCS generic, or departmental/bespoke.
3. **Load the methodology**: Read `references/methodology.md` before analysing the contract so the output structure and confidence rules are applied consistently.
4. **Load the framework reference**: Read the matching framework file and use it as the baseline for comparison.
5. **Run Phase 1 review**: Perform a broad factual pass across all fifteen categories, capturing citations, confidence signals, missing items, and conflicts.
6. **Run Phase 2 only if needed**: Revisit only categories with low confidence, weak citations, or unresolved conflicts. Resolve them only if evidence materially improves the finding; otherwise leave them explicitly unresolved.
7. **Classify findings**: Mark findings RED, AMBER, or GREEN based on IBM legal/commercial posture and the framework baseline.
8. **Compare to baseline terms**: Call out where the draft departs from standard framework protections or introduces non-standard obligations.
9. **Prioritise actions**: Separate clarifications, commercial mitigations, negotiation points, and items requiring IBM Legal escalation.

## Operating Rules

- Ground every finding in the document text with section or page citations.
- Separate factual extraction from risk classification. First state what the contract says, then state IBM's risk posture.
- Use explicit uncertainty. If the document is silent, contradictory, or incomplete, say so directly.
- Fail closed. Do not guess, smooth over conflicts, or infer protections that are not evidenced in the contract.
- Treat schedules, appendices, and framework deviations carefully; precedence and override issues are often material.
- When the contract references external URLs or incorporated documents, retrieve and review them if they are needed to support a finding.

## Output Requirements

Produce a structured assessment containing:

- **Contract overview**: parties, contract type, value, term, framework, and document set reviewed
- **Key factual findings**: the most material evidence-backed facts from the review
- **Category-by-category analysis**: findings for all fifteen categories with citations and confidence signals
- **Risk classification**: RED/AMBER/GREEN tagging with concise rationale
- **Framework comparison**: deviations from standard framework terms or expected public-sector protections
- **Gaps and ambiguities**: missing terms, contradictions, unresolved items, and evidence limitations
- **Recommended actions**: clarification questions, commercial mitigations, negotiation priorities, and legal escalations

## References

- `references/methodology.md` - Review method, confidence signals, phase logic, and output schema
- `references/dos6.md` - Digital Outcomes and Specialists 6
- `references/ts3.md` - Technology Services 3
- `references/gcloud.md` - G-Cloud framework
- `references/ccs.md` - Crown Commercial Service generic frameworks
- `references/departmental.md` - Department-specific procurement routes
