# Example Clarification Questions

Patterns and examples of well-formed clarification questions for procurement tenders.

## Technical Questions

### Integration Requirements

**Poor:**
"What APIs do you have?"

**Good:**
**Document Reference:** Section 4.2 - Integration Requirements, Page 18
**Question:** The requirement states "The solution must integrate with existing CRM and ERP systems." Please provide: (1) The specific CRM product, version, and available integration methods (API, file transfer, database), (2) The ERP system name, version, and any middleware currently in use, (3) Expected data synchronisation frequency and volumes.
**Rationale:** Integration approach significantly impacts architecture design, development effort, and hosting requirements, all of which affect pricing and timeline.
**Expected Detail:** Product names, versions, technical specifications for each integration point, sample API documentation or data schemas if available.

### Current State Volumetrics

**Poor:**
"How many users are there?"

**Good:**
**Document Reference:** Section 2.3 - Current Environment, Page 8
**Question:** The tender references "handling current and future volumes" but does not specify baseline metrics. Please provide: (1) Current number of concurrent users (peak and average), (2) Transaction volumes (daily/monthly) by transaction type, (3) Data storage volumes and growth rate over past 12 months, (4) Expected growth projections over contract period.
**Rationale:** Volumetrics directly determine infrastructure sizing, licensing costs, performance requirements, and scalability design. Underestimating volumes risks service degradation; overestimating inflates cost unnecessarily.
**Expected Detail:** Quantified metrics with breakdown by user type and transaction category, plus 3-year growth projections.

## Commercial Questions

### Pricing Model

**Poor:**
"What pricing do you want?"

**Good:**
**Document Reference:** Section 8.1 - Commercial Model, Page 45
**Question:** The tender requires "competitive pricing" but does not specify preferred commercial structure. Please clarify: (1) Preferred pricing model (per-user, per-transaction, fixed fee, consumption-based), (2) Whether pricing should be submitted as total contract value or annual breakdown, (3) Treatment of one-off vs recurring costs, (4) Whether price assumes client-provided infrastructure or supplier-managed hosting.
**Rationale:** Pricing structure affects commercial risk profile, cash flow, and comparability of bids. Different models suit different client preferences and risk appetites.
**Expected Detail:** Preferred commercial model with any constraints on structure, payment terms, or cost allocation.

### Contract Length and Extension

**Poor:**
"How long is the contract?"

**Good:**
**Document Reference:** Section 9.2 - Contract Terms, Page 52
**Question:** Section 9.2 states "initial contract term with extension options" but does not specify durations. Please confirm: (1) Initial contract term length, (2) Number and duration of extension periods, (3) Notice period required for extensions, (4) Pricing basis for extension periods (fixed, index-linked, re-negotiable).
**Rationale:** Contract duration impacts investment recovery period, price optimisation strategy, and commercial risk. Extension options affect long-term revenue visibility and resource planning.
**Expected Detail:** Specific term lengths, extension mechanisms, and pricing approach for extended periods.

## Governance Questions

### Change Management

**Poor:**
"Who approves changes?"

**Good:**
**Document Reference:** Section 6.4 - Change Control, Page 32
**Question:** The tender requires "formal change control process" but does not define thresholds or governance. Please clarify: (1) Change categorisation criteria (minor/major/emergency), (2) Approval authorities for each change category, (3) Expected turnaround time for change approvals, (4) Whether supplier can implement changes within scope without formal change requests, (5) Commercial treatment of changes (included in fee vs additional cost).
**Rationale:** Change management process affects delivery agility, administrative overhead, and commercial risk. Clear governance prevents scope creep whilst enabling necessary flexibility.
**Expected Detail:** Change categorisation matrix, approval workflow diagram, and commercial framework for changes.

### Performance Measurement

**Poor:**
"What KPIs do you want?"

**Good:**
**Document Reference:** Section 7.1 - Service Levels, Page 38
**Question:** The tender specifies "service levels will be agreed" but provides no baseline expectations. Please provide: (1) Mandatory KPIs and their target values, (2) Relative weighting or criticality of each KPI, (3) Measurement methodology and reporting frequency, (4) Consequences of KPI underperformance (service credits, remediation plans, termination rights), (5) Whether KPI targets are subject to negotiation or fixed.
**Rationale:** KPI targets determine solution design parameters (e.g., availability requirements drive architecture resilience), operational cost (monitoring and reporting overhead), and commercial risk exposure (service credit liability).
**Expected Detail:** Specific KPI targets with measurement definitions, reporting requirements, and service credit regime.

## Timeline Questions

### Mobilisation Period

**Poor:**
"When do you want to start?"

**Good:**
**Document Reference:** Section 5.1 - Implementation Timeline, Page 24
**Question:** The tender states "go-live by Q2 2026" but does not specify mobilisation start date or contract award timeline. Please confirm: (1) Expected contract award date, (2) Mobilisation period duration between award and go-live, (3) Key milestones and interim deliverables required, (4) Client dependencies during mobilisation (e.g., infrastructure readiness, UAT availability, training schedules), (5) Consequences if client dependencies cause delays.
**Rationale:** Mobilisation timeline determines resource ramp-up profile, parallel project commitments, and risk of delay penalties. Client dependencies during mobilisation must be factored into delivery planning and risk allocation.
**Expected Detail:** Full project timeline with key dates, dependencies, and risk allocation for delays.

## Resource Questions

### Client-Provided Assets

**Poor:**
"What access will we get?"

**Good:**
**Document Reference:** Section 3.2 - Client Responsibilities, Page 12
**Question:** The tender states "client will provide necessary access and data" but does not specify scope. Please detail: (1) Infrastructure to be provided (hosting, network, security tools), (2) Data sets to be supplied (format, completeness, data quality), (3) Access to SMEs for requirements clarification and UAT, (4) Office space and facilities for on-site team members, (5) Timeline for provision of each asset relative to project start, (6) Remediation approach if provided assets are inadequate or delayed.
**Rationale:** Client-provided assets are critical dependencies that affect delivery risk and cost. Inadequate or late provision can derail projects; supplier must understand exact scope to price risk appropriately.
**Expected Detail:** Itemised list of all client-provided assets with specifications, delivery timeline, and accountability framework.

## Format Patterns

### Structure Template

Every question should follow this format:

```markdown
### Q[N]: [Concise title describing the topic]
**Document Reference:** [Section number, heading, page number]
**Question:** [Specific question with enumerated sub-points if multiple clarifications needed]
**Rationale:** [Why this matters - link to design/pricing/risk]
**Expected Detail:** [What level of response is required]
```

### Question Characteristics

**Specific**: References exact document location
**Scoped**: Addresses one discrete topic per question
**Justified**: Explains why the information is needed
**Actionable**: Response directly informs solution or pricing decisions
**Professional**: Neutral tone, avoids criticism of tender quality
**Structured**: Uses enumeration for multi-part questions

### Rationale Patterns

Link clarifications to tangible impacts:
- "Affects architecture design approach and hosting requirements"
- "Determines licensing model and commercial structure"
- "Impacts resource profile and delivery timeline"
- "Influences risk allocation and insurance requirements"
- "Changes compliance obligations and audit scope"

### Expected Detail Patterns

Be specific about required response:
- "Product names, versions, and technical specifications"
- "Quantified metrics with 3-year projections"
- "Process diagram with decision points and timelines"
- "Specific contractual terms and conditions"
- "Sample documentation or schema definitions"
