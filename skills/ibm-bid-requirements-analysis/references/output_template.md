# Requirements Analysis Output Template

## Standard Format

```markdown
# REQUIREMENTS ANALYSIS: [CLIENT NAME]

## EXECUTIVE SUMMARY
[2-3 sentences: what they want, what they really need, key challenges identified]

---

## CLIENT PROFILE

**Organisation:** [Type, sector, scale]
**Context:** [Why this procurement now]
**Stakeholders:** [Key decision makers identified from tender]
**Procurement stage:** [ITT/RFI/Market engagement]
**Current landscape:** [Existing systems/suppliers mentioned]

---

## STATED REQUIREMENTS

### Functional Requirements
[Grouped by: core capabilities, integrations, reporting, user experience]

**Core Capabilities:**
- [Requirement 1]
- [Requirement 2]

**Integration Requirements:**
- [System integrations needed]

**Reporting/Analytics:**
- [Reporting requirements]

**User Experience:**
- [UX/accessibility requirements]

### Technical Requirements
**Infrastructure:**
- [Hosting, scalability, performance]

**Security:**
- [Security standards, compliance, data protection]

**Compliance:**
- [Regulatory requirements, standards]

### Commercial Requirements
**Contract structure:** [Term, extension options]
**Pricing model:** [Fixed price, T&M, outcome-based]
**Delivery timeline:** [Key milestones]
**Resource requirements:** [Team composition, skills]

### Evaluation Criteria
[Criteria with weightings if disclosed]
- **Quality/Technical:** X%
- **Price/Commercial:** Y%
- **Social Value:** Z% (if applicable)
- **Other criteria:** [As specified]

**Pass/fail criteria:** [Mandatory requirements]

---

## LEVEL 2: UNDERLYING NEEDS

### Operational Gaps

**What's broken:**
1. [Current system failure 1] → [stated requirement it drives]
2. [Current system failure 2] → [stated requirement it drives]
3. [Current system failure 3] → [stated requirement it drives]

**Business Impact:**
- [Consequence 1 of current state]
- [Consequence 2 of current state]
- [Cost/risk of inaction]

### Capability Deficits

**Technical capabilities they lack:**
- [Technology gap 1]: [Evidence from tender]
- [Technology gap 2]: [Evidence from tender]
- [Technology gap 3]: [Evidence from tender]

**Organisational capabilities they lack:**
- [Skills gap]: [Training/change management emphasis]
- [Governance gap]: [Control/oversight requirements]
- [Process maturity gap]: [Process improvement needs]

**Process capabilities they lack:**
- [Automation gap]: [Manual processes causing pain]
- [Integration gap]: [Siloed systems]
- [Visibility gap]: [Reporting/analytics deficits]

### Risk Profile

**Stated risks:**
[Risks explicitly mentioned in tender - quote and reference]
1. [Risk 1]: [Why client is concerned]
2. [Risk 2]: [Why client is concerned]

**Unstated risks:**
[Risks implied by requirements patterns or sector context]
1. [Implied risk 1]: [Evidence from requirements]
   - **Why this matters:** [Business impact]
   - **Mitigation needed:** [What response should address]

2. [Implied risk 2]: [Evidence from requirements]
   - **Why this matters:** [Business impact]
   - **Mitigation needed:** [What response should address]

**Sector-specific risks:**
- [Risk based on sector patterns]
- [Compliance/regulatory risk]

### Competitive Dynamics

**Incumbent signals:**
[Evidence of existing supplier influence on tender]
- [Requirement favouring incumbent]: [Platform/approach bias]
- [Terminology from specific vendor]: [Examples]
- **Incumbent likely to be:** [Company name/type]

**Likely bidders:**
1. **[Competitor type 1]** (e.g., Large consultancies - Accenture, Capgemini)
   - **Their likely approach:** [How they'll position]
   - **Their strengths here:** [Why they're competitive]

2. **[Competitor type 2]** (e.g., Tech vendors - Salesforce, Microsoft)
   - **Their likely approach:** [How they'll position]
   - **Their strengths here:** [Why they're competitive]

3. **[Competitor type 3]** (e.g., Specialists - domain-specific firms)
   - **Their likely approach:** [How they'll position]
   - **Their strengths here:** [Why they're competitive]

**Market positioning indicators:**
- [Specific requirements suggesting market testing]
- [Reference to "leading practice" from specific sources]
- [Requirements bundling suggesting shaped opportunity]

**Budget indicators:**
[Evidence of budget range/constraints]
- **Value range estimate:** [Based on scope, sector benchmarks]
- **Constraint signals:** [Phasing, cloud preference, risk transfer language]
- **Flexibility indicators:** [Options for phasing, scaling]

---

## CLARIFICATION NEEDS

[Requirements requiring clarification - feeds ibm-bid-clarifications skill]

**Ambiguous requirements:**
1. [Requirement needing clarification]: [Why it's unclear]
2. [Contradictory requirements]: [What's inconsistent]

**Missing information:**
1. [Critical gap 1]: [Why we need this]
2. [Critical gap 2]: [Why we need this]

---

## NEXT STEPS

**Immediate:**
1. **Run ibm-bid-strategic-positioning**: Strategic analysis, sales strategy, price-to-win
2. **Run ibm-bid-clarifications**: Formulate clarification questions (if permitted)
3. **Run ibm-bid-qualification**: GO/NO-GO scoring

**Supporting research:**
- **ibm-bid-library**: Search for similar [sector] tenders, [client name] previous bids
- **ibm-bid-customer-stories**: Find stories matching [challenges identified]
- **ibm-bid-strategy-and-capabilities-2026**: IBM capabilities for [gaps identified]
```

## Government Sector Additions

For UK public sector tenders, add:

```markdown
## PUBLIC SECTOR CONTEXT

**Framework route:** [G-Cloud, CCS, DPS, OJEU]
**Social value requirements:** [Specific themes/weightings]
**SME/local supply chain:** [Requirements and opportunities]
**Transparency requirements:** [Publishing, audit trail needs]
**Comparator organisations:** [Similar orgs for case studies]
```

## Quick Analysis Format

For rapid opportunity assessment:

```markdown
# QUICK REQUIREMENTS ANALYSIS: [CLIENT]

**Opportunity:** [What they're buying in one sentence]
**Why now:** [Procurement driver]
**Size/Value:** [Estimated contract value]

**Core needs:**
1. [Primary need] ← [Stated requirement]
2. [Secondary need] ← [Stated requirement]
3. [Tertiary need] ← [Stated requirement]

**Key gaps:**
- **Technical:** [Main technology deficit]
- **Organisational:** [Main capability deficit]
- **Process:** [Main workflow problem]

**Risks to address:**
1. [Key risk 1]
2. [Key risk 2]

**Likely bidders:**
- [Competitor 1]
- [Competitor 2]

**Next step:** Run ibm-bid-strategic-positioning for sales strategy and price-to-win
```
