# Pre-Draft Planning Template

Use this template before drafting a tender answer. Keep it short and practical. The goal is to force the key winning-bid decisions before prose starts.

If the user or source pack has not explicitly supplied any section below, infer it from:
- the question wording
- evaluation or scoring language
- schedule references
- delivery risk implied by the service
- available account, client, or IBM evidence

For any question that concerns a service, treat "service" as the full operating model: people, process, data, and technology. Do not default to a technology-only or governance-only interpretation unless the tender explicitly narrows the scope.

## Planning Template

```markdown
# Bid Response Plan

## Mode
- Writing mode: formal scored-response mode / conversational drafting mode
- Why this mode is appropriate:

## Question
- Reference:
- Raw question or summary:

## Evaluator Concern
- Primary concern:
- Secondary concerns:
- What a high score probably requires:

## Confidence Summary Section
- Use a document-level confidence section: yes / no
- Proposed heading:
- Framing paragraph focus:
- Preview bullet 1:
- Preview bullet 2:
- Preview bullet 3:
- Preview bullet 4:

## Confidence Case
- One-sentence confidence opener:
- Why IBM is credible on this topic now:

## Wireframe Sub-Heading Structure
- Source: user-provided / `./tmp/ibm-bid-wireframe-Q0X.md` / `./tmp/q[N]_wireframe.md` / generated during planning
- Preserve exact wireframe headings in final answer: yes / no, with reason:
- Heading 1: How we've structured our response
- Heading 2: How we...
- Heading 3: How we...
- Heading 4: How we...
- Heading 5: How we...
- Heading 6: How we...

## Named Mechanisms
- Mechanism 1:
- Mechanism 2:
- Mechanism 3:
- Mechanism 4:

## Evidence Stack
- Account-specific or incumbent evidence:
- Named team or leader credibility:
- Relevant public sector or NHS precedent:
- Broader IBM capability proof:
- Metrics, quotes, or outcomes to use:

## Repeated Bid Themes
- Theme 1:
- Theme 2:
- Theme 3:
- Theme 4:

## Draft Shape
- Recommended response archetype:
- Recommended internal structure pattern:
- Output format: `## Part 1: Sub-Headings Structure` followed by `## Part 2: Written Response`
- Prose plan: write Part 2 in flowing prose paragraphs by default. Note any section where the tender explicitly requires a different format:
- Bullet justification: bullets are banned in Part 2 unless the question explicitly enumerates discrete parallel items or the user requests bullets. If bullets are used, record the exact justification here:
- Likely evidence form:
- Required headings or sub-sections:
- Wireframe headings to use as actual answer sections:
- Risks and mitigations to cover:
- Ownership boundaries or dependencies to state:
- Any compact inline labelled sequences to use:

## Diagram / Visual Composition
- Client diagram/image requirement from wireframe or extractor:
- Diagram count to use:
- Diagram type(s):
- Diagram word count treatment: Included / Excluded / Confirm
- Composition choice: prose only / diagram plus concise prose / table plus prose / diagram plus table plus prose
- Content moved into diagram rather than prose:
- Prose that remains necessary to interpret the diagram:
- Caption or label budget:
- Follow-on `ibm-bid-image-definer` needed: yes / no

## Service Scope Lens
- People: roles, capability, leadership, knowledge transfer, stakeholder engagement, and responsibilities to cover:
- Process: lifecycle, governance, controls, workflows, assurance, escalation, change, and improvement to cover:
- Data: records, reporting, metrics, data quality, security, privacy, interoperability, and insight to cover:
- Technology: platforms, tooling, automation, integrations, environments, resilience, security controls, and architecture to cover:
- Dimensions that are out of scope or unsupported by available evidence:

## Draft Reminders
- Phrases or terminology to mirror:
- Claims that need fact-checking:
- Weak spots or missing evidence:
```

## How To Use It

1. Fill this plan before drafting full prose.
2. Keep each section compact. Bullet fragments are fine.
3. Default to formal scored-response mode unless the user explicitly wants an internal or conversational draft.
4. Infer missing fields rather than stopping, unless a missing fact creates material risk.
5. Use the plan to keep repeated bid themes consistent across questions.
6. After drafting, check that the final response still reflects the plan rather than drifting into generic prose.
7. For substantial standalone answers, plan the opening confidence section before you plan the section-by-section body.
8. If a wireframe artifact exists, copy its `Part 1: Sub-Headings` / `Part 1: Sub-Headings Structure` bullets into the plan and use them as the final answer headings.
9. If no wireframe artifact exists, create the same structure during planning: first `How we've structured our response`, then `How we...` headings that follow the tender question sequence.
10. Plan the best composition before prose length. If the wireframe permits or requires a diagram, decide whether the answer scores better as diagram plus concise prose rather than longer prose.
11. Record `Diagram word count treatment` before drafting. If it is `Included`, budget labels and captions inside the word limit. If it is `Excluded`, use the diagram to carry structure without duplicating it in prose. If it is `Confirm`, keep visual text short and flag the uncertainty.
12. Plan prose first. Bullets are banned in Part 2 unless the question explicitly enumerates discrete parallel items or the user requests bullets. Record the justification before drafting any Part 2 bullet list.

## Fast Heuristics

### Infer evaluator concern from question type

- Delivery approach:
  - Can IBM deliver at pace without losing control across people, process, data, and technology?
- Mobilisation or transition:
  - Can IBM take over quickly without disruption to roles, operating processes, service data, tooling, and live technology?
- Standards or security:
  - Can IBM innovate without breaking compliance across process, data handling, technology controls, and accountable roles?
- Capability or fit:
  - Does IBM really have the people and depth claimed?
- Social value:
  - Are the commitments measurable, governed, and believable?
- Value for money:
  - Can IBM improve outcomes while controlling cost and protecting service integrity?

### Infer confidence case from evidence available

Look first for:
1. Current account or incumbent knowledge
2. Named leaders or specialist roles
3. Live service experience
4. Proven operating model
5. Quantified outcomes
6. Trusted partners with clear roles

### Plan the document-level confidence section

Use this by default for substantial standalone answers and whole-question responses.

1. Heading:
   - Prefer `Why you should have full confidence in our proposal` unless the pack format strongly suggests a different label
2. Framing paragraph:
   - Summarise why IBM is credible on this topic now
3. Preview bullets:
   - Write 2-4 bold-led bullets
   - Each bullet should preview one proof theme that the body will substantiate
   - Good themes include continuity, standards by design, measurable productivity, strategic partnerships, safe innovation, and value for money
4. Bullet style:
   - Lead with the claim in bold
   - Follow immediately with the mechanism, evidence, or outcome that makes the claim believable

### Infer named mechanisms from the service context

Good mechanism types include:
1. Delivery lifecycle
2. Governance forum or board
3. Dashboard or scorecard
4. Transition or mobilisation method
5. Assurance process
6. Accelerator, toolkit, or workbench
7. Partner model or innovation forum
8. Data quality, reporting, or insight mechanism
9. Role, responsibility, or knowledge-transfer mechanism

### Infer repeated bid themes

Prefer a small stable set, for example:
1. Continuity and low supervision
2. Standards or security by design
3. Measurable productivity and value for money
4. Safe innovation
5. Integration readiness
6. User-centred delivery

### Infer internal structure pattern

Use these defaults:
1. Technical or delivery approach -> confidence section plus bold-labelled mechanism blocks
2. Standards, security, or compliance -> confidence section plus standards categories and assurance workflow
3. Mobilisation or transition -> confidence section plus phased plan and transition controls
4. Capability or fit -> confidence section plus role-to-relevance or responsibility tables
5. Social value or commitments -> confidence section plus commitments and activities blocks
6. Challenges, uncertainties, or value for money -> challenge plus `plan to address` or mitigation blocks
7. Dense method explanation with several short scoreable elements -> compact inline labelled sequence

### Infer likely evidence form

Use these cues:
1. Whole-answer or executive framing need -> confidence summary bullets
2. Technical or delivery engine explanation -> bold-labelled mechanism blocks
3. Role fit, ownership, or boundary setting -> table
4. Commitment-heavy answers -> commitment plus activities blocks or tables
5. Transition or mobilisation -> phased plan
6. Risks, uncertainty, or value-for-money -> challenge plus mitigation blocks
7. Dense standards, assurance, innovation, or operating method content -> compact inline labelled sequence
