# IBM Bid Management Quality Gates

Quality gates ensure systematic Go/No-Go decisions and technical assurance before significant resource investment. This document defines the two mandatory quality gates in the bid lifecycle.

## Quality Gate 1: GO/NO-GO Decision (After Phase 0)

### Purpose
Prevent wasted effort on low-probability opportunities by making evidence-based bid/no-bid decisions before investing in detailed solution development and response drafting.

### Timing
Execute after Phase 0 (Opportunity Assessment) is complete:
- ibm-bid-requirements-analysis completed (Step 1)
- ibm-bid-strategic-positioning completed (Step 2)
- ibm-bid-clarifications completed (Step 2, if applicable)
- ibm-bid-qualification completed (Step 2)

### Decision Authority
- **<£1M**: Bid Manager
- **£1M-£10M**: Bid Manager + Practice Lead
- **£10M+**: Bid Manager + Practice Lead + Partnership approval

---

## Gate 1 Scoring Criteria

### Qualification Score Thresholds

| Score Range | Recommendation | Description | Action |
|-------------|----------------|-------------|--------|
| 81-100 | **STRONG GO** | Highly winnable opportunity | Prioritize resources, fast-track |
| 61-80 | **GO (Conditional)** | Good opportunity with manageable risks | Proceed with standard process, monitor risks |
| 41-60 | **CONDITIONAL** | Medium-risk opportunity | Mitigation plan required before proceeding |
| 0-40 | **NO-GO** | High-risk or unwinnable opportunity | Document no-bid decision, exit |

### Scoring Breakdown (From ibm-bid-qualification)

The qualification score is calculated across 7 categories with 20 criteria:

#### 1. Client Maturity (15 points maximum)
- Organizational readiness (0-5)
- Executive sponsorship (0-5)
- Change management capability (0-5)

#### 2. Justification (15 points maximum)
- Business case clarity (0-5)
- ROI quantification (0-5)
- Budget alignment (0-5)

#### 3. Momentum (15 points maximum)
- Project timeline (0-5)
- Procurement stage (0-5)
- Decision-making velocity (0-5)

#### 4. Relationships (20 points maximum)
- Existing client relationship (0-10)
- Decision-maker access (0-5)
- Reference client (0-5)

#### 5. Reputation (10 points maximum)
- IBM brand perception (0-5)
- Competitive position (0-5)

#### 6. Differentiators (15 points maximum)
- Unique capabilities (0-5)
- Competitive advantage (0-5)
- Innovation opportunity (0-5)

#### 7. Commercial Viability (10 points maximum)
- Pricing competitiveness (0-5)
- Margin potential (0-5)

**Total Maximum Score: 100 points**

---

## Gate 1 Validation Checklist

Before making GO/NO-GO decision, validate:

### Strategic Fit
- [ ] Opportunity aligns with IBM strategy (cloud, AI, Salesforce, cybersecurity focus areas)
- [ ] Supports portfolio goals (geographic expansion, industry penetration, technology adoption)
- [ ] Reference case potential (reusable for future bids)

### Competitive Position
- [ ] IBM has relevant experience and credentials
- [ ] Incumbent or competitive threats identified and assessed
- [ ] Win strategy clearly articulated (see ibm-bid-win-themes)
- [ ] Differentiation is defensible (not easily copied)

### Client Readiness
- [ ] Client has budget and authority to proceed
- [ ] Decision-making process understood (evaluation criteria, timeline, stakeholders)
- [ ] Requirements are achievable (not aspirational or unrealistic)
- [ ] Client expectations aligned with IBM capabilities

### Resource Availability
- [ ] Required skills available (technical, delivery, support)
- [ ] Resource conflicts with other priorities assessed
- [ ] Subcontractor/partner needs identified
- [ ] Timeline achievable with available resources

### Commercial Viability
- [ ] Pricing model understood (fixed price, T&M, outcome-based)
- [ ] Margin targets achievable
- [ ] Payment terms acceptable (not excessive risk)
- [ ] Contract terms reasonable (liability, IP, termination clauses)

### Risk Assessment
- [ ] Technical risks identified and mitigatable
- [ ] Commercial risks quantified
- [ ] Reputational risks considered
- [ ] Resource risks manageable

---

## Gate 1 Red Flags

These indicators suggest heightened risk. Multiple red flags (3+) strongly indicate NO-GO:

### Client Red Flags
- ❌ No budget allocated or budget "to be determined"
- ❌ No executive sponsor identified
- ❌ Client shopping for ideas (using bid process for free consulting)
- ❌ Unrealistic timeline (<3 months for complex implementation)
- ❌ History of failed projects in this area
- ❌ Unstable leadership or organizational turmoil

### Competitive Red Flags
- ❌ RFP written around competitor's solution (wired bid)
- ❌ Incumbent has multi-year relationship and strong performance
- ❌ Evaluation criteria favor competitor capabilities
- ❌ IBM doesn't meet mandatory requirements without waiver
- ❌ Competitor has pricing advantage (10%+ lower)

### Commercial Red Flags
- ❌ Fixed-price contract with poorly defined scope
- ❌ Unlimited liability or indemnification clauses
- ❌ Payment terms >90 days or milestone-based with unclear criteria
- ❌ IP ownership transfers to client (loses reusability)
- ❌ Margin <15% (below IBM minimum for complex bids)

### Resource Red Flags
- ❌ Required skills not available in IBM
- ❌ Requires >5 FTE from scarce skill pools
- ❌ Conflicts with other priority opportunities (same resources)
- ❌ Requires security clearances IBM doesn't have
- ❌ Geographic location incompatible with IBM delivery model

### Relationship Red Flags
- ❌ No existing relationship with client
- ❌ Previous project failures with this client
- ❌ Client reputation for difficult partnerships
- ❌ Procurement process prohibits client engagement
- ❌ No access to decision-makers or influencers

---

## Gate 1 Decision Trees

### Decision Tree 1: Qualification Score + Red Flags

```
Score 81-100?
  ├─ YES → Red flags ≤1?
  │   ├─ YES → STRONG GO (Fast-track)
  │   └─ NO → GO (Monitor red flags)
  └─ NO → Score 61-80?
      ├─ YES → Red flags ≤2?
      │   ├─ YES → GO (Standard process)
      │   └─ NO → CONDITIONAL (Mitigation required)
      └─ NO → Score 41-60?
          ├─ YES → Red flags ≤1 AND mitigation plan?
          │   ├─ YES → CONDITIONAL (Mitigation required)
          │   └─ NO → NO-GO
          └─ NO → NO-GO (Score <41)
```

### Decision Tree 2: Resource Investment vs. Win Probability

```
Win Probability (from qualification)?
  ├─ HIGH (80%+) → Invest full resources
  ├─ MEDIUM (50-80%) → Invest standard resources, monitor
  ├─ LOW (25-50%) → Minimal investment, focus on relationship
  └─ VERY LOW (<25%) → NO-GO (unless strategic exception)

Resource Requirement?
  ├─ LOW (<40 hours) → Acceptable for MEDIUM-HIGH probability
  ├─ MEDIUM (40-150 hours) → Requires MEDIUM+ probability
  └─ HIGH (150+ hours) → Requires HIGH probability OR strategic exception
```

---

## Gate 1 Documentation Requirements

After Gate 1 decision, document in `../tmp/ibm-bid-qualification.md`:

### For GO Decisions
- Qualification score and category breakdown
- Key strengths (top 3-5)
- Identified risks and mitigation strategies
- Resource allocation plan
- Next steps (proceed to Phase 1)

### For NO-GO Decisions
- Qualification score and category breakdown
- Disqualifying factors (red flags, low score categories)
- Lessons learned (why this opportunity didn't qualify)
- Alternative approaches (e.g., decline this bid, pursue relationship for future opportunities)
- Notification plan (who to inform, when)

---

## Quality Gate 2: Technical Assurance (After Phase 4)

### Purpose
Validate technical quality and submission readiness before final submission, ensuring:
- Technical solution is architecturally sound
- All responses meet quality standards
- No fabricated information or unsubstantiated claims
- Submission is compliant and competitive

### Timing
Execute after Phase 4 (Technical Assurance) is complete:
- ibm-bid-tda-review completed
- Final ibm-bid-answer-evaluator pass completed
- All responses and solution documents finalized

### Decision Authority
- **<£5M**: Bid Manager + Technical Lead
- **£5M-£25M**: Bid Manager + Technical Lead + Practice Lead
- **£25M+**: Bid Manager + Technical Lead + Practice Lead + CTO approval

---

## Gate 2 Criteria

### Criterion 1: TDA Risk Rating (from ibm-bid-tda-review)

Technical Design Authority reviews 7 dimensions and assigns risk rating:

| Dimension | LOW Risk | MEDIUM Risk | HIGH Risk |
|-----------|----------|-------------|-----------|
| **Requirements Alignment** | 95%+ requirements met | 85-95% met, minor gaps | <85% met, major gaps |
| **Resource Capability** | Team fully capable | Some capability gaps, mitigatable | Significant capability gaps |
| **Scalability** | Scales to 3x+ current needs | Scales to 2x with effort | Cannot scale beyond current |
| **Security Architecture** | Exceeds requirements | Meets requirements | Gaps in security requirements |
| **Integration Complexity** | Well-defined, low risk | Moderate complexity, manageable | High complexity, significant risk |
| **Operational Readiness** | Full operational plan | Basic operational plan | Insufficient operational planning |
| **Technology Risk** | Proven technologies | Some emerging technologies | Unproven or high-risk technologies |

**Overall TDA Risk Rating:**
- **LOW**: All dimensions LOW or MEDIUM with majority LOW → **GO**
- **MEDIUM**: Mix of LOW/MEDIUM, no HIGH → **CONDITIONAL GO** (address medium risks)
- **HIGH**: Any dimension rated HIGH → **ESCALATE** (CTO review required, may be NO-GO)

### Criterion 2: Answer Quality Scores (from ibm-bid-answer-evaluator)

Each response scored on 5-point scale across 5 dimensions:

| Score | Understanding | Evidence | Structure | Clarity | Differentiation |
|-------|---------------|----------|-----------|---------|-----------------|
| 5 | Exceptional understanding, goes beyond question | Multiple strong sources, quantified | Perfect structure, exemplary | Crystal clear, compelling | Strongly differentiated, unique |
| 4 | Thorough understanding, comprehensive | Good evidence, specific examples | Well-structured, clear flow | Clear, professional | Differentiated, distinctive |
| 3 | Adequate understanding, addresses question | Adequate evidence, relevant | Structured, logical | Clear enough, understandable | Some differentiation |
| 2 | Partial understanding, misses elements | Weak evidence, generic | Poor structure, disorganized | Unclear, confusing | Limited differentiation |
| 1 | Minimal understanding, mostly off-topic | No evidence, unsupported claims | No structure, incoherent | Very unclear | No differentiation |
| 0 | No understanding, non-responsive | Fabricated or false information | - | - | - |

**Quality Thresholds:**
- **PASS**: All responses score ≥3 (adequate) with average ≥4 (good)
- **REVIEW**: Any responses score 2 (partial) → Revise failing responses
- **FAIL**: Any responses score ≤1 (minimal/non-responsive) → Major revision required

---

## Gate 2 Validation Checklist

Before final submission, validate:

### Technical Validation
- [ ] Solution architecture reviewed and approved by Technical Design Authority
- [ ] All technical requirements addressed
- [ ] No unproven or high-risk technologies without mitigation
- [ ] Integration points clearly defined
- [ ] Security requirements met
- [ ] Scalability validated
- [ ] Operational model defined

### Content Validation
- [ ] All questions answered completely
- [ ] No non-responsive or off-topic answers
- [ ] All claims substantiated with evidence
- [ ] No fabricated information (customer stories, statistics, capabilities)
- [ ] Consistent messaging across all responses
- [ ] Win themes incorporated throughout
- [ ] Customer success stories relevant and accurate

### Quality Validation
- [ ] All responses score ≥3 on answer evaluator
- [ ] Average score ≥4 across all responses
- [ ] Executive summary compelling and aligned with responses
- [ ] Solution document complete and coherent
- [ ] No contradictions between responses or documents
- [ ] Professional presentation quality

### Compliance Validation
- [ ] Page limits adhered to
- [ ] Required sections included
- [ ] Formatting requirements met
- [ ] Mandatory attachments included
- [ ] Pricing structured per RFP requirements
- [ ] Submission deadline achievable
- [ ] Electronic submission tested (if applicable)

### Commercial Validation
- [ ] Pricing competitive and defensible
- [ ] Margin targets met
- [ ] Commercial terms acceptable
- [ ] Contract redlines documented (if applicable)
- [ ] Payment terms understood
- [ ] Assumptions clearly stated

### Risk Validation
- [ ] All HIGH risks mitigated or escalated
- [ ] MEDIUM risks have mitigation plans
- [ ] Risk register complete and reviewed
- [ ] Contingency plans documented
- [ ] Escalation paths defined

---

## Gate 2 Red Flags

These indicators suggest submission is not ready. Any red flag requires resolution before submission:

### Technical Red Flags
- 🚨 TDA identifies any HIGH risk dimension
- 🚨 Solution doesn't meet mandatory requirements
- 🚨 Integration complexity not adequately addressed
- 🚨 Security gaps identified
- 🚨 Unproven technology without risk mitigation

### Content Red Flags
- 🚨 Any response scores ≤1 (non-responsive)
- 🚨 Multiple responses score 2 (partial understanding)
- 🚨 Fabricated or inaccurate information detected
- 🚨 Contradictions between responses
- 🚨 Claims without evidence

### Compliance Red Flags
- 🚨 Page limits exceeded
- 🚨 Required sections missing
- 🚨 Formatting non-compliant (may be disqualified)
- 🚨 Mandatory attachments missing
- 🚨 Cannot meet submission deadline

### Commercial Red Flags
- 🚨 Pricing non-compliant with RFP requirements
- 🚨 Margin below IBM minimums
- 🚨 Unacceptable contract terms not escalated
- 🚨 Assumptions not clearly documented

---

## Gate 2 Decision Matrix

### Decision: SUBMIT

**Criteria:**
- TDA Risk Rating: LOW or MEDIUM (with mitigation plans)
- All responses score ≥3, average ≥4
- All validation checklist items passed
- No unresolved red flags
- Bid Manager + Technical Lead + Practice Lead (if required) approve

**Action:**
- Finalize submission package
- Complete final proofreading
- Submit by deadline
- Update CRM/opportunity tracking

### Decision: CONDITIONAL SUBMIT

**Criteria:**
- TDA Risk Rating: MEDIUM with minor gaps
- All responses score ≥3, average 3.5-4.0
- Most validation checklist items passed
- 1-2 minor red flags with mitigation plans

**Action:**
- Address identified gaps within 24-48 hours
- Re-review after corrections
- Escalate to Practice Lead for approval
- Submit with documented assumptions/caveats

### Decision: DELAY SUBMISSION (Request Extension)

**Criteria:**
- TDA Risk Rating: MEDIUM-HIGH
- Some responses score 2 (partial)
- Multiple validation checklist items failed
- 3+ red flags requiring resolution

**Action:**
- Request submission deadline extension from client (if possible)
- Address all failing items
- Re-run Gate 2 after corrections
- Consider no-bid if extension not granted and quality cannot be achieved

### Decision: NO-GO (Withdraw Bid)

**Criteria:**
- TDA Risk Rating: HIGH (unmitigatable)
- Multiple responses score ≤1 (non-responsive)
- Critical red flags (fabricated information, non-compliance)
- Cannot meet submission deadline with quality standards

**Action:**
- Document decision and rationale
- Notify client of withdrawal (if relationship permits)
- Conduct lessons learned session
- Update opportunity tracking

---

## Gate 2 Documentation Requirements

After Gate 2 decision, document in appropriate files:

### For SUBMIT/CONDITIONAL SUBMIT
In `../tmp/ibm-bid-tda-review.md`:
- TDA risk rating by dimension
- Overall risk assessment
- Mitigation plans for MEDIUM risks
- Technical approval signature

In `../tmp/ibm-bid-final-evaluation.md`:
- All response scores
- Average quality score
- Key strengths
- Areas for improvement (if conditional)
- Final approval signature

In `../tmp/ibm-bid-project.md`:
- Update `current_phase`: "ready_for_submission"
- Document Gate 2 approval

### For DELAY/NO-GO
In `../tmp/ibm-bid-project.md`:
- Document decision and rationale
- List unresolved issues
- Capture lessons learned
- Define next steps (withdraw vs. request extension)

---

## Integration Between Gates

### Gate 1 Informs Resource Allocation
- **STRONG GO** (81-100) → Full resource allocation, priority scheduling
- **GO** (61-80) → Standard resource allocation
- **CONDITIONAL** (41-60) → Limited initial investment pending mitigation

### Gate 1 Sets Quality Expectations for Gate 2
- Higher qualification scores should correlate with higher Gate 2 quality
- If Gate 1 identified risks, Gate 2 should validate mitigation
- Win themes from Phase 1 should be validated in Gate 2 responses

### Both Gates Feed Continuous Improvement
- Track win/loss against Gate 1 scores (do scores predict wins?)
- Track Gate 2 quality against submission outcomes (do higher scores win?)
- Refine thresholds based on historical data
- Update criteria as IBM capabilities evolve

---

## Escalation Procedures

### When to Escalate

**Escalate to Practice Lead:**
- Qualification score 41-60 (CONDITIONAL)
- TDA Risk Rating MEDIUM with significant gaps
- Commercial terms outside standard parameters
- Resource conflicts with other priorities

**Escalate to CTO:**
- Qualification score <41 but strategic exception requested
- TDA Risk Rating HIGH
- Unproven technology with >£10M contract value
- Client demanding technical approach outside IBM standards

**Escalate to Partnership:**
- Qualification score <60 but >£10M opportunity
- Reputational risk to IBM brand
- Contract terms with unusual liability or IP provisions
- Client relationship issues requiring executive engagement

### Escalation Documentation

When escalating, provide:
1. **Summary**: 1-paragraph overview of issue
2. **Analysis**: Detailed assessment with data
3. **Options**: 2-3 alternative approaches with pros/cons
4. **Recommendation**: Preferred approach with rationale
5. **Timeline**: Decision urgency and impact of delay

---

## Quality Gate Metrics

Track these metrics to improve gate effectiveness:

### Gate 1 Metrics
- **Qualification Score Distribution**: Are we targeting the right opportunities?
- **GO/NO-GO Ratio**: Are we too aggressive or too conservative?
- **Win Rate by Qualification Score**: Do scores predict wins?
- **Time to Gate 1 Decision**: Are we deciding fast enough?

### Gate 2 Metrics
- **Average Response Quality Score**: Are we improving over time?
- **TDA Risk Distribution**: Are we taking appropriate technical risks?
- **Gate 2 Failures**: How often do we fail Gate 2 (should be rare)?
- **Submission Quality vs. Win Rate**: Does higher quality correlate with wins?

### Cross-Gate Metrics
- **Gate 1 to Win Conversion**: What % of GO decisions win?
- **Gate 2 Quality vs. Gate 1 Score**: Does qualification predict submission quality?
- **Resource Investment by Gate 1 Score**: Are we allocating resources appropriately?
- **Cycle Time by Tender Type**: Are workflows efficient?

---

## Continuous Improvement

Quality gates should evolve based on:
- Win/loss analysis
- Client feedback
- IBM capability changes
- Market dynamics
- Regulatory changes

Review gate criteria annually and update thresholds as needed.
