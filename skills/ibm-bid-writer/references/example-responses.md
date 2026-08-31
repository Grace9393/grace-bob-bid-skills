# Example Response Patterns

Use these patterns to calibrate answer quality.

## Benefit Claim Pattern

Poor:
- "Our approach reduces response time by 40%."

Good:
- "Our approach reduced response time by 40% (from 10 minutes to 6 minutes) in a comparable deployment."

Better:
- "Our approach reduced response time by 40% (from 10 minutes to 6 minutes), contributing to annual savings of about GBP500,000 in staffing cost."

## Confidence Opener Pattern

Weak:
- "We will deliver this service using an agile methodology."

Strong:
- "Our proposed team will deliver this service through the same operating model that already supports high-volume national digital services, giving you continuity, clear governance, and faster time to value from day one."

## Confidence Summary Bullets Pattern

Best for:
- top-of-document confidence sections
- substantial standalone answers
- responses that need to preview multiple proof themes before numbered sections begin

Shape:
1. Heading such as `Why you should have full confidence in our proposal`
2. One short framing paragraph
3. Two to four bold-led bullets, each previewing a major theme such as continuity, standards, innovation, productivity, or value

Example:
- "**We bring deep account knowledge and proven continuity** through the current team, named leadership, and live service experience."
- "**We accelerate delivery through named mechanisms and controls** including our delivery lifecycle, governance forums, and monitoring dashboards."
- "**We improve value without weakening service integrity** by pairing productivity gains with assurance, standards, and operational discipline."

Worked exemplar:
1. Heading: `Why you should have full confidence in our proposal`
2. Framing paragraph: one short paragraph that states why IBM is credible now
3. Preview bullets:
   - "**We bring continuity and low supervision from day one** through retained account knowledge, named leadership, and a service model already proven in live delivery."
   - "**We accelerate delivery through named mechanisms** including our delivery lifecycle, governance forums, and scorecard dashboard."
   - "**We make innovation safe and valuable** by pairing transformation with assurance, standards, and measurable productivity."

## Evidence Pattern

Weak:
- "We have strong public sector experience."

Strong:
- "In a UK public sector programme, we modernised service operations for more than 30 critical services, reducing incident resolution time by 28% over 12 months."

## Partner Pattern

Weak:
- "We will work with leading ecosystem partners."

Strong:
- "We will use partner X for specialised migration tooling to reduce cutover risk and partner Y for secure testing automation to shorten validation cycles."

## Mechanism Pattern

Weak:
- "We have strong governance and delivery controls."

Strong:
- "We will govern delivery through a fortnightly sprint cadence, a monthly delivery board, and a balanced scorecard that tracks product, service, and operational health, giving the client visibility without slowing decisions."

## Section Template

Use this structure when drafting a full response section:

1. Document-level confidence section if the answer is substantial; otherwise no separate confidence opener unless it adds real value.
2. Opening sentence that answers the question directly.
3. Delivery approach in client language.
4. Named mechanisms that explain how the approach works.
5. Evidence block with quantified outcomes and baseline.
6. Risk and mitigation summary.
7. Implementation timeline and readiness notes.
8. Differentiation statement linked to client priorities.

## Internal Structure Patterns

Use these internal patterns to avoid generic bid prose:

### Pattern A: Confidence + Mechanism Blocks

Best for:
- technical approach
- standards
- delivery model

Shape:
1. Optional document-level confidence section
2. Direct answer sentence
3. Bold-labelled blocks such as `Service Transition`, `Live Support`, `Maintain and Improve`, `Innovation and Strategy`
4. Proof paragraph with baseline and outcome

Use this when the evaluator needs to see how the delivery engine actually works.

Worked exemplar:

```markdown
## Why you should have full confidence in our proposal

[Short framing paragraph on continuity, delivery credibility, and outcomes]

* **We bring continuity and proven delivery knowledge** through the current team, named leaders, and live-service experience.
* **We accelerate delivery through named mechanisms and controls** including our Product Development Lifecycle, Delivery Board, and balanced scorecard dashboard.
* **We improve value without weakening service integrity** by combining productivity measures with assurance, standards, and service resilience controls.

## T1.x Delivery of the service

Our proposed team will deliver the service through a self-sufficient operating model that gives you pace, visibility, and control.

**Service Transition:** [Named transition method and continuity controls]

**Live Support:** [Run model, SRE ownership, incident and operational controls]

**Maintain and Improve:** [Prioritisation model, backlog, quality and performance management]

**Innovation and Strategy:** [Roadmap, partner model, advisory mechanisms, safe innovation]

[Proof paragraph with baseline, outcome, timeframe, and buyer value]
```

### Pattern B: Confidence + Table Mapping

Best for:
- capability and fit
- governance boundaries
- stakeholder model

Shape:
1. Optional short framing paragraph
2. Framing paragraph
3. Table mapping role to relevance, or responsibility to rationale
4. Closing paragraph on credibility, continuity, or control

Use this when a table will score faster than prose because the evaluator is checking fit, accountability, or boundaries.

Worked exemplar:

```markdown
Our proposed team will operate with minimum supervision through clear ownership boundaries and governance visibility.

| Best provided by you | Rationale |
| --- | --- |
| Overall programme ownership | You retain strategic sponsorship and system-wide decision rights. |
| Access to users and policy stakeholders | You control the established NHS channels required for engagement at scale. |
| Governance forum coordination | You maintain enterprise-level governance structures and approvals. |

[Short closing paragraph on how IBM complements these boundaries with autonomous delivery]
```

### Pattern C: Commitment + Activities

Best for:
- social value
- commitments
- mobilisation actions

Shape:
1. Optional short confidence section
2. Criterion-led commitment statement
3. `Commitment N` plus `Activities` block
4. Timed action, accountability, and measurement

Use this when the buyer expects measurable commitments rather than general intent.

Worked exemplar:

```markdown
## MAC 1a: Exceeding criteria through high-quality job creation

We will deliver measurable social value through named commitments, timed actions, and clear accountability.

|  |
| --- |
| **Commitment 1: We will create and retain high-quality jobs** |
| **Activities**: • [activity 1] • [activity 2] • [activity 3] |
| **Commitment 2: We will expand apprenticeships and in-work progression** |
| **Activities**: • [activity 1] • [activity 2] • [activity 3] |
```

Note:
- This pattern should be the default for social value and other measurable commitment questions where the buyer is scoring delivery commitments, not general aspiration.

### Pattern D: Challenge + Plan To Address

Best for:
- uncertainties
- risks
- value for money

Shape:
1. Challenge statement
2. `Plan to address:` or mitigation block
3. Named mechanisms and controls
4. Precedent with measured impact

Use this when the question is really testing realism, risk awareness, or value protection.

Worked exemplar:

```markdown
**Political and funding instability:** Shifts in policy or budget can disrupt delivery continuity and pace.
*Plan to address:* We will use [named forum], [resourcing mechanism], and [commercial review cadence] to adjust scope safely while protecting service integrity.

**Cybersecurity threat escalation:** Expanding integrations increases exposure across the service boundary.
*Plan to address:* We will embed Secure by Design controls, automated monitoring, and named assurance roles into the delivery lifecycle.

[Close with precedent and measured impact]
```

### Pattern E: Compact Inline Labelled Sequence

Best for:
- standards mapping
- innovation and foresight sections
- assurance domains
- compact delivery method explanation where each item needs only a short explanation

Shape:
1. Direct opening sentence
2. Two to five inline bold labels
3. One to three clauses after each label explaining method, control, or proof
4. Optional closing sentence linking the sequence back to buyer value

Use this when the evaluator needs high information density without a table and without a full bullet list for each point.

Worked exemplar:

```markdown
As requirements evolve, we will adapt delivery without weakening control or service integrity through four mechanisms:

**Innovation and thought leadership:** Our Expert Advisory Board and Innovation Hub will test and validate new ideas before scaled rollout. **Technology foresight:** Quarterly tech radar reviews and partner inputs will identify emerging platform and standards changes early. **Requirements sensing:** User research, analytics, and stakeholder feedback loops will detect changing needs and adoption barriers quickly. **Agile resourcing:** We will rebalance multi-disciplined teams and specialist support as demand changes.
```

Second exemplar:

```markdown
We will maintain standards compliance through clear assurance domains embedded in delivery. **Planning and governance:** We will identify applicable standards, owners, and decision points at mobilisation. **Security and privacy:** We will embed DPIAs, code review, and regular testing into run and change activity. **Interoperability:** We will align APIs and data models to the required NHS standards and onboarding processes. **Oversight and audit:** We will track compliance through dashboards, internal audits, and scheduled reporting.
```

Note:
- This pattern is common in winning bid material because it keeps dense method detail scoreable without fragmenting the narrative.
- Keep each labelled item concise. If an item needs expansion, convert it into a full mechanism block or a dedicated sub-section.

## Minimal Draft Template

```markdown
## [Client Sub-Question Heading]

[Confidence-building framing statement]

[Direct answer in 2-3 sentences]

[Delivery approach and named mechanisms]

[Evidence example with baseline, outcome, and timeframe]

[Risk and mitigation]

[Value statement for relevant stakeholder]
```

## Conversational Drafting Mode Examples

Use this section only when the user explicitly wants an internal strawman, workshop draft, or SME-shaped working version before conversion into formal scored-response prose.

Rule:
1. Keep the same underlying logic as the formal examples
2. Keep named mechanisms, evidence, and buyer value intact
3. Relax the evaluator-facing polish, not the delivery substance

### Confidence Opener: Formal vs Conversational

Formal:
- "Our proposed team will deliver the service through a self-sufficient operating model that gives you continuity, clear governance, and faster time to value from day one."

Conversational:
- "We would start from a strong continuity position here because the team, governance, and operating model are already proven in live delivery."

### Mechanism Block: Formal vs Conversational

Formal:
- "**Service Transition:** Our Prepare-Plan-Learn-Perform method will provide a controlled transition with clear ownership, rapid knowledge transfer, and minimal disruption to live service."

Conversational:
- "**Service Transition:** We would use our Prepare-Plan-Learn-Perform transition method so the handover is structured, knowledge moves early, and live service risk stays low."

### Commitment Statement: Formal vs Conversational

Formal:
- "We will deliver measurable social value through named commitments, timed actions, and clear accountability."

Conversational:
- "We should frame social value here as a set of measurable commitments with owners, dates, and reporting, rather than as general good intent."

### Risk Statement: Formal vs Conversational

Formal:
- "**Cybersecurity threat escalation:** Expanding integrations increases exposure across the service boundary. *Plan to address:* We will embed Secure by Design controls, automated monitoring, and named assurance roles into the delivery lifecycle."

Conversational:
- "**Cybersecurity threat escalation:** More integrations usually mean more exposure. *Plan to address:* We would handle that by building Secure by Design controls, monitoring, and named assurance roles into the delivery lifecycle from the start."

## Quick Self-Test

Before handing off, check:

1. Does every section answer the exact client sub-question?
2. Is each major claim backed by a concrete example or source?
3. Do outcomes include baseline context?
4. Are the mechanisms, controls, or forums named where needed?
5. Is the language plain, specific, and human?
