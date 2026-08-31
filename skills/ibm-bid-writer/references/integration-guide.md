# Integration Guide

This guide covers cross-skill orchestration, search strategy, and phase handoffs.

## Workflow Position

1. Skill: `ibm-bid-writer`
2. Bid lifecycle phase: Content Development (Phase 3)
3. Typical pattern per question:
   - Draft
   - Evaluate
   - Revise if score <3
   - Progress when score >=3

## Inputs

## Tender Context Inputs

1. RFP or ITT question text (required)
2. `../tmp/ibm-bid-requirements-analysis.md` (if available)
3. `../tmp/ibm-bid-strategic-positioning.md` (if available)
4. `../tmp/ibm-bid-win-themes.md` (if available)
5. Question-specific wireframe from `../tmp/ibm-bid-wireframe-Q0X.md`, `../tmp/q[N]_wireframe.md`, a user-provided wireframe, or a wireframe path recorded in `../tmp/ibm-bid-project.md` (if available)

## IBM Knowledge Inputs

1. `$ibm-bid-library`
   - Use for reusable answer structures, delivery approaches, and technical content.
2. `$ibm-bid-customer-stories`
   - Use for evidence, proof points, and quantified outcomes.
3. `$ibm-bid-strategy-and-capabilities-2026`
   - Use for differentiators and strategic IBM capability positioning.

## Optional Technical Inputs

1. `../tmp/ibm-sf-solution/complete_solution.md`
2. `../tmp/ibm-bid-solution/complete_solution.md`
3. `../tmp/ibm-sf-ams-estimation.md`

## Post-Draft Steps

1. Check the evaluator-facing answer uses the wireframe `Part 1: Sub-Headings` / `Part 1: Sub-Headings Structure` as its actual section structure. If no wireframe was available, check that the writer generated and used a `How we've structured our response` plus `How we...` heading structure before drafting.
2. Check the answer is presented as `## Part 1: Sub-Headings Structure` followed by `## Part 2: Written Response`, unless the user or tender template required answer-only output.
3. Run `ibm-bid-fact-checker` for claim verification.
4. Run `ibm-bid-answer-evaluator` for quality scoring.
5. If score <3:
   - Add stronger evidence and quantified outcomes.
   - Restructure to mirror client order.
   - Tighten clarity and remove generic wording.
6. Re-run evaluator until score >=3.

## Search Strategy

## `ibm-bid-library` Query Ideas

1. Technology: "Salesforce implementation", "cloud migration", "cybersecurity assessment"
2. Method: "agile delivery", "testing approach", "change management"
3. Client type: "government", "NHS", "financial services", "local authority"
4. Question intent: "technical approach", "delivery methodology", "resource plan"
5. Rebid context: client name and service area

Use simple keyword combinations first, then refine with quoted phrases.

## `ibm-bid-customer-stories` Query Ideas

1. Industry: "government", "healthcare", "financial", "retail"
2. Capability: "Sales Cloud", "Service Cloud", "Marketing Cloud", "Agentforce"
3. Challenge: "digital transformation", "operational efficiency", "compliance"
4. Geography: "UK", "Europe", "Global"
5. Scale qualifiers: include user or transaction context where relevant

## Cross-Skill Decision Points

1. Drafting new response text: `ibm-bid-writer`
2. Quality scoring and critique: `ibm-bid-answer-evaluator`
3. Accuracy and source validation: `ibm-bid-fact-checker`
4. Workflow navigation: `ibm-bid-navigator`

## Coordination Rules

1. Different authors can draft different questions in parallel.
2. Keep consistent win themes and terminology across all responses.
3. Avoid cross-references between questions unless explicitly required in tender docs.
4. Ensure each response can be read independently by an evaluator.
5. Preserve the agreed wireframe headings per question so separately drafted answers retain a consistent bid-document structure.

## Quality Gate Preparation

Before moving to technical assurance:

1. All responses should score >=3.
2. Messaging should remain consistent across questions.
3. No fabricated or unsupported claims should remain.
4. Architecture and delivery references should align with technical source documents.
