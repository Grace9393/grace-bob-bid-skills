---
name: ibm-bid-tda-review
description: Perform Technical Design Authority (TDA) reviews of solution architectures from the perspective of an IBM Lead Enterprise Architect with 10+ years experience. Evaluate requirements alignment, resource capability, scalability, security, integration complexity, operational readiness, and technology risk. Use when asked to review, assess, or provide TDA analysis of technical solutions, architectures, or bid proposals. Output comprehensive markdown reports with findings, risk ratings, and recommendations.
metadata:
  skills-required:
    - ibm-bid-requirements-analysis
  skills-suggested:
    - ibm-bid-solution-architect
---

# IBM Bid Technical Design Authority Review

Conduct comprehensive Technical Design Authority reviews of solution architectures, evaluating seven critical assessment areas to determine solution viability and risk.

## Context Management

Write output to `./tmp/ibm-bid-tda-review.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `tda_status: complete`
- `tda_artifact: ./tmp/ibm-bid-tda-review.md`
- `tda_risk_rating`: LOW, MEDIUM, or HIGH
- `tda_critical_findings`: highest-priority findings from the review
- `key_risks`: include material technical risks
- `artifacts_generated`: include `./tmp/ibm-bid-tda-review.md` when the artifact is written
- `next_skill_recommendation`: normally final `ibm-bid-answer-evaluator`, architecture revision, or submission readiness depending on risk

## Review Persona

Adopt the perspective of an IBM Lead Enterprise Architect with:
- 10+ years complex solution architecture experience
- Deep expertise across multiple technologies and platforms
- Enterprise-grade governance and risk assessment capability
- Strong understanding of IBM delivery methodologies and standards

## Input Formats

Accept solution documentation in:
- Markdown (.md) files
- PowerPoint presentations (.pptx)
- Combined documentation sets

## Assessment Framework

Load the comprehensive TDA framework from `references/tda_framework.md` before conducting the review. The framework covers seven core assessment areas:

1. **Requirements Alignment & Traceability** - Evaluate how comprehensively the architecture maps to functional and non-functional requirements
2. **Resource Capability Assessment** - Assess team skills, experience, and capability gaps
3. **Scalability, Performance & Resilience** - Review architectural patterns for scale, performance, and failure handling
4. **Security Architecture & Compliance** - Evaluate security controls and regulatory compliance
5. **Integration & Dependency Management** - Assess external system integrations and resilience
6. **Operational Readiness & Supportability** - Review observability, disaster recovery, and support model
7. **Technology Risk & Vendor Lock-in** - Evaluate technology maturity, dependencies, and exit strategies

## Review Process

1. **Load Framework** - Read `references/tda_framework.md` to understand evaluation criteria
2. **Analyse Input** - Extract architecture details, requirements, resource plans, and technical specifications
3. **Systematic Evaluation** - Apply framework questions to each assessment area
4. **Identify Findings** - Document strengths, weaknesses, gaps, and risks
5. **Risk Rating** - Determine overall risk level (High/Medium/Low) based on findings severity
6. **Generate Recommendations** - Provide specific, actionable mitigation strategies

## Risk Rating Criteria

**High Risk:**
- Critical requirements gaps affecting core functionality
- Severe security vulnerabilities or compliance violations
- Single points of failure without mitigation
- Fundamental scalability or performance concerns
- Missing critical skills or resources
- Significant technology risks or vendor lock-in without exit strategy

**Medium Risk:**
- Minor requirements gaps with workarounds available
- Security or compliance concerns requiring attention
- Scalability concerns with planned mitigations
- Resource capability gaps with training plans
- Moderate technology risks with mitigation options

**Low Risk:**
- All critical requirements addressed
- Comprehensive security and compliance controls
- Well-architected scalability and resilience
- Appropriate resource capability and depth
- Mature technology choices with minimal lock-in
- Strong operational readiness

## Output Format

Generate a comprehensive markdown report structured as:

```markdown
# Technical Design Authority Review
## Executive Summary
[Brief overview, overall risk rating, key findings]

## Assessment Areas

### 1. Requirements Alignment & Traceability
**Risk Rating:** [High/Medium/Low]
**Findings:**
- [Finding 1]
- [Finding 2]
**Recommendations:**
- [Recommendation 1]
- [Recommendation 2]

### 2. Resource Capability Assessment
[Same structure]

### 3. Scalability, Performance & Resilience
[Same structure]

### 4. Security Architecture & Compliance
[Same structure]

### 5. Integration & Dependency Management
[Same structure]

### 6. Operational Readiness & Supportability
[Same structure]

### 7. Technology Risk & Vendor Lock-in
[Same structure]

## Overall Risk Rating
[High/Medium/Low with justification]

## Critical Risks & Mitigation Priorities
[Ranked list of most critical issues requiring immediate attention]

## Conclusion
[Summary assessment and go/no-go recommendation]
```

## Review Principles

**Objectivity** - Assess based on evidence in documentation, not assumptions
**Comprehensiveness** - Cover all seven assessment areas systematically
**Specificity** - Provide concrete findings with references to source material
**Actionability** - Ensure recommendations are specific and implementable
**Risk-Based** - Focus on highest-impact concerns
**Enterprise Perspective** - Consider IBM standards, best practices, and delivery track record

## Common Red Flags

Watch for:
- Vague or missing non-functional requirements
- Single-vendor technology dependencies without alternatives
- Resource plans with generic skill descriptions
- Missing security controls or compliance considerations
- Undefined operational support model
- No disaster recovery or resilience patterns
- Unproven or emerging technologies in critical path
- Undocumented integration dependencies
- Absence of testing strategy or acceptance criteria
- No change management or technical debt tracking

## Complete Tender Response Workflow

This skill is part of the 5-phase IBM Bid Management workflow.

**Current Phase**: Phase 4 (Technical Assurance)
**Position**: Parallel execution with Final ibm-bid-answer-evaluator pass

**When to Use**:
- All bids with technical solution architecture (>£5M mandatory)
- Before final submission
- After Phase 2 (Solution Architecture) and Phase 3 (Content Development) complete

**When to Skip**:
- Non-technical bids (professional services, capability statements)
- Bids without custom solution architecture
- Framework call-offs with no technical solution design

See ibm-bid-navigator for complete workflow guidance.

## Integration with Other Skills

### Required Inputs

**Solution Architecture** (ONE of the following required):
- **ibm-sf-solution-architect output**: ./tmp/ibm-sf-solution/complete_solution.md (for Salesforce implementations)
- **ibm-bid-solution-architect output**: ./tmp/ibm-bid-solution/complete_solution.md (for infrastructure/cloud/cybersecurity implementations)

**Supporting Context** (recommended):
- **RFP requirements**: Original tender document requirements section
- **ibm-bid-requirements-analysis output**: ./tmp/ibm-bid-requirements-analysis.md (requirements traceability)
- **Technical responses**: ./tmp/ibm-bid-responses/ (validate consistency between architecture and responses)

### Back-References to Solution Architecture Skills

This TDA review evaluates solutions generated by:

**For Salesforce Implementations**:
- **ibm-sf-solution-architect**: Reviews the 16-section Salesforce solution document
  - Validates Salesforce-specific architecture patterns (data model, security model, integration architecture)
  - Assesses Salesforce platform scalability and limits
  - Reviews Salesforce best practices adherence
  - References ibm-sf-architect patterns and ibm-sf-help capabilities
- **ibm-sf-ams**: Reviews operational support model sizing
  - Validates FTE estimates are realistic
  - Assesses operational readiness of support model
  - Reviews support processes and escalation procedures

**For Non-Salesforce Implementations**:
- **ibm-bid-solution-architect**: Reviews the 15-section technology-agnostic solution document
  - Validates infrastructure architecture (system architecture, technology stack, infrastructure design)
  - Assesses security architecture and compliance
  - Reviews integration architecture complexity
  - Validates scalability, performance, and disaster recovery approaches

### Recommended Next Steps

**After TDA Review:**

**If Overall Risk Rating = LOW**:
- Proceed to final submission preparation
- Run **Final ibm-bid-answer-evaluator pass** (parallel with TDA review)
- Package deliverables for submission
- Quality Gate 2: PASS

**If Overall Risk Rating = MEDIUM**:
- Review mitigation recommendations
- Assess if mitigations can be implemented before submission deadline
- Options:
  1. **Implement mitigations**: Update solution architecture and responses, re-run TDA review
  2. **Document assumptions**: Proceed to submission with documented risk mitigation plans in place
  3. **Escalate to Practice Lead**: Request approval for conditional submission with MEDIUM risks
- Quality Gate 2: CONDITIONAL PASS (requires approval)

**If Overall Risk Rating = HIGH**:
- **STOP**: Do not proceed to submission
- Escalate to CTO for review
- Options:
  1. **Request deadline extension**: If client allows, revise architecture to address HIGH risks
  2. **Scope reduction**: Remove high-risk components, propose phased approach
  3. **No-bid decision**: Withdraw if HIGH risks cannot be mitigated
- Quality Gate 2: FAIL (escalation required)

### Supporting Resources
- **ibm-sf-architect**: Reference Salesforce architecture patterns during review
- **ibm-sf-help**: Validate Salesforce feature capabilities and limitations
- **ibm-bid-strategy-and-capabilities-2026**: Validate IBM capabilities claims
- **ibm-bid-library**: Search for similar solution architectures and lessons learned

### Quality Gate 2: Technical Assurance

This skill directly informs Quality Gate 2. The TDA risk rating is a mandatory input for final submission decision.

**Decision Criteria**:
- **LOW risk**: All assessment areas rated LOW or majority LOW with minor MEDIUM → GO
- **MEDIUM risk**: Mix of LOW/MEDIUM, no HIGH → CONDITIONAL GO (mitigation plans required)
- **HIGH risk**: Any assessment area rated HIGH → ESCALATE (CTO review required, may be NO-GO)

**Decision Authority**:
- <£5M: Bid Manager + Technical Lead
- £5M-£25M: Bid Manager + Technical Lead + Practice Lead
- £25M+ or HIGH risk: Bid Manager + Technical Lead + Practice Lead + CTO approval

### Integration with Evaluator Skills

TDA review and answer evaluation serve complementary purposes:

| Aspect | ibm-bid-tda-review | ibm-bid-answer-evaluator |
|--------|-------------------|-------------------------|
| **Focus** | Technical architecture validity | Response content quality |
| **Input** | Solution architecture documents | Written tender responses |
| **Evaluation** | Engineering soundness, feasibility, risk | Understanding, evidence, structure, clarity, differentiation |
| **Output** | Risk rating (LOW/MEDIUM/HIGH) | Quality score (0-5 scale) |
| **Expertise** | Lead Enterprise Architect | Bid reviewer/evaluator |
| **Can run in parallel** | Yes (Phase 4) | Yes (Phase 4) |

Both must PASS for Quality Gate 2 approval.
