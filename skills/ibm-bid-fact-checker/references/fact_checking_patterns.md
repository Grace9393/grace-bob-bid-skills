# Fact-Checking Patterns and Examples

This document provides detailed patterns and examples for fact-checking IBM tender responses against source documents.

## Fact-Checking Categories

### 1. Performance Metrics

#### Common Metric Patterns

**Availability Claims:**
- "99.99% availability"
- "99.9% uptime"
- "four nines availability"
- "99.999% availability"

**Verification Approach:**
1. Search for exact percentage in source documents
2. Check for context (e.g., "during business hours", "24/7")
3. Verify if metric is a requirement or a capability claim

**Example:**
```
Claim: "IBM provides 99.99% availability"
Source Search: "99.99%" in RFP document
Result: ✓ Verified - Found in IBM capabilities document
Evidence: IBM_Capabilities.pdf, Section 3.2, Page 15
```

**Example:**
```
Claim: "Our solution achieves 99.99% availability"
Source Search: "99.99%" in RFP document
Result: ✗ Flagged - No exact match in RFP
Recommendation: Remove claim or find supporting evidence
```

#### SLA Claims

**Common SLA Patterns:**
- "99.9% SLA"
- "99.99% service level agreement"
- "99.999% uptime guarantee"
- "24/7 support with 4-hour response time"

**Verification Approach:**
1. Search for SLA requirements in RFP
2. Check if IBM's SLA exceeds RFP requirements
3. Verify SLA applies to the specific service/component

**Example:**
```
Claim: "IBM offers 99.99% SLA with 4-hour response time"
Source Search: "SLA" and "response time" in RFP
Result: ✓ Verified - RFP requires 99.9% SLA, IBM exceeds it
Evidence: RFP.pdf, Section 4.3, Page 22
```

### 2. Capability Claims

#### Technical Capabilities

**Common Capability Patterns:**
- "IBM can deliver AI-powered analytics"
- "IBM provides end-to-end integration"
- "IBM offers cloud migration services"
- "IBM delivers enterprise-grade security"

**Verification Approach:**
1. Search IBM capabilities documentation
2. Check for specific service names and features
3. Verify capabilities match RFP requirements

**Example:**
```
Claim: "IBM delivers AI-powered analytics platform"
Source Search: "AI-powered analytics" in IBM capabilities
Result: ✓ Verified - Found in IBM_Capabilities.pdf
Evidence: IBM_Capabilities.pdf, Section 5.1, Page 34
```

**Example:**
```
Claim: "IBM provides end-to-end Salesforce integration"
Source Search: "Salesforce integration" in IBM capabilities
Result: ✓ Verified - Found in IBM_Capabilities.pdf
Evidence: IBM_Capabilities.pdf, Section 6.2, Page 45
```

#### Implementation Methodologies

**Common Methodology Patterns:**
- "IBM uses Agile methodology"
- "IBM follows ITIL best practices"
- "IBM employs DevOps practices"
- "IBM uses IBM Garage methodology"

**Verification Approach:**
1. Search IBM methodology documentation
2. Verify methodology is applicable to the project
3. Check if methodology is mentioned in RFP requirements

**Example:**
```
Claim: "IBM uses IBM Garage methodology for implementation"
Source Search: "IBM Garage methodology" in IBM capabilities
Result: ✓ Verified - Found in IBM_Capabilities.pdf
Evidence: IBM_Capabilities.pdf, Section 7.1, Page 52
```

### 3. Pricing and Commercial Terms

#### Cost Claims

**Common Pricing Patterns:**
- "$500,000 total cost"
- "$1.2 million over 3 years"
- "Hourly rate of $250"
- "Fixed price of $750,000"

**Verification Approach:**
1. Check RFP for pricing requirements
2. Verify IBM pricing aligns with RFP guidelines
3. Ensure cost claims are realistic and supported

**Example:**
```
Claim: "Total cost of $500,000 over 12 months"
Source Search: "cost" and "$500,000" in RFP
Result: ✓ Verified - RFP allows for this cost range
Evidence: RFP.pdf, Section 8.2, Page 67
```

**Example:**
```
Claim: "Implementation cost of $1.5 million"
Source Search: "cost" in RFP pricing section
Result: ✗ Flagged - RFP maximum is $1.2 million
Recommendation: Reduce claim to $1.2 million or find justification
```

#### Payment Terms

**Common Payment Patterns:**
- "50% upfront, 50% on completion"
- "Quarterly payments"
- "Milestone-based payments"
- "Net 30 payment terms"

**Verification Approach:**
1. Check RFP for payment requirements
2. Verify IBM payment terms comply with RFP
3. Ensure terms are realistic for the project

### 4. Compliance and Requirements

#### Requirement Coverage

**Common Compliance Patterns:**
- "Meets all mandatory requirements"
- "Fulfills all RFP requirements"
- "Complies with all technical specifications"
- "Addresses all evaluation criteria"

**Verification Approach:**
1. Cross-reference with RFP requirements checklist
2. Verify each requirement is explicitly addressed
3. Check for missing or incomplete coverage

**Example:**
```
Claim: "Meets all mandatory requirements"
Source Search: "mandatory requirements" in RFP
Result: ✓ Verified - All 15 mandatory requirements addressed
Evidence: RFP.pdf, Section 2.1, Page 8
```

**Example:**
```
Claim: "Fulfills all RFP requirements"
Source Search: "requirements" in RFP
Result: ✗ Flagged - Missing requirement #12 (Data Migration)
Recommendation: Add section on data migration approach
```

#### Technical Specifications

**Common Specification Patterns:**
- "Supports Microsoft Azure"
- "Compatible with Salesforce Lightning"
- "Integrates with SAP S/4HANA"
- "Works with AWS services"

**Verification Approach:**
1. Search RFP for technical specifications
2. Verify IBM capabilities match specifications
3. Check for compatibility claims

**Example:**
```
Claim: "Supports Microsoft Azure cloud platform"
Source Search: "Microsoft Azure" in IBM capabilities
Result: ✓ Verified - Found in IBM_Capabilities.pdf
Evidence: IBM_Capabilities.pdf, Section 4.3, Page 28
```

### 5. Differentiators and Value Propositions

#### Competitive Positioning

**Common Differentiator Patterns:**
- "IBM's AI capabilities are superior"
- "IBM offers unique value proposition"
- "IBM's solution is better than competitors"
- "IBM provides unmatched expertise"

**Verification Approach:**
1. Search IBM capabilities for differentiators
2. Verify claims are supported by evidence
3. Check if differentiators address RFP needs

**Example:**
```
Claim: "IBM's AI capabilities are superior to competitors"
Source Search: "AI capabilities" and "superior" in IBM capabilities
Result: ✓ Verified - Found in IBM_Capabilities.pdf
Evidence: IBM_Capabilities.pdf, Section 5.1, Page 34
```

**Example:**
```
Claim: "IBM offers unmatched expertise in healthcare"
Source Search: "healthcare expertise" in IBM capabilities
Result: ✗ Flagged - No specific healthcare expertise mentioned
Recommendation: Remove claim or find supporting evidence
```

## Fact-Checking Techniques

### 1. Exact Match Verification

**Purpose:** Verify claims using exact text matching

**Process:**
1. Copy claim text exactly as written
2. Search source documents for exact text
3. Check for context and surrounding text
4. Verify no misrepresentation

**Example:**
```
Claim: "99.99% availability"
Source Search: "99.99%" in RFP.pdf
Result: ✓ Exact match found in Section 3.2, Page 15
```

### 2. Partial Match Verification

**Purpose:** Verify claims when exact match not found

**Process:**
1. Extract key terms from claim
2. Search source documents for key terms
3. Check if claim is supported by context
4. Verify no exaggeration or misstatement

**Example:**
```
Claim: "IBM provides 99.99% availability"
Source Search: "99.99%" in IBM_Capabilities.pdf
Result: ✓ Partial match found - IBM claims 99.99% availability
Evidence: IBM_Capabilities.pdf, Section 3.2, Page 15
```

### 3. Contextual Verification

**Purpose:** Verify claims in their full context

**Process:**
1. Read surrounding text in response
2. Check RFP requirements for context
3. Verify claim addresses specific RFP needs
4. Ensure claim is not taken out of context

**Example:**
```
Claim: "Our solution meets all requirements"
Context: Response discusses technical requirements
Source Search: "requirements" in RFP.pdf
Result: ✓ Verified - All technical requirements addressed
Evidence: RFP.pdf, Section 2.1, Page 8
```

### 4. Evidence Strength Assessment

**Purpose:** Evaluate the strength of supporting evidence

**Levels:**
- **Strong evidence:** Exact match in source documents
- **Medium evidence:** Similar claims with supporting context
- **Weak evidence:** General statements without specific support
- **No evidence:** Unsupported claims requiring revision

**Example:**
```
Claim: "IBM provides 99.99% availability"
Evidence: IBM_Capabilities.pdf, Section 3.2, Page 15
Evidence Strength: Strong (exact match)
```

## Reporting Templates

### Fact-Check Report Structure

```markdown
# Fact-Check Report: [Response Title]

## Summary
- Total claims checked: [number]
- Verified claims: [number]
- Flagged claims: [number]
- Evidence gaps: [number]

## Verified Claims
[List of claims with source document references]

## Flagged Claims
[List of unsupported or potentially inaccurate claims with recommendations]

## Evidence Gaps
[List of missing supporting documentation]

## Recommendations
[Actions to address flagged items]
```

### Claim Entry Format

```markdown
### [Claim text]
**Evidence Strength:** [strong/medium/weak/none]
**Source Documents:**
- [Source file] ([exact/partial])
**Recommendation:** [if flagged]
```

## Common Pitfalls to Avoid

### 1. Out-of-Context Claims

**Pitfall:** Taking a claim out of its original context

**Example:**
```
Claim: "IBM provides 99.99% availability"
Context: Claim is about a specific component, not the entire solution
Result: ✗ Flagged - May be misleading
```

**Solution:** Always verify claims in their full context

### 2. Exaggerated Claims

**Pitfall:** Exaggerating capabilities or performance

**Example:**
```
Claim: "IBM guarantees 100% availability"
Source: IBM capabilities mention 99.99% availability
Result: ✗ Flagged - Exaggerated claim
```

**Solution:** Use exact metrics from source documents

### 3. Missing Source Attribution

**Pitfall:** Making claims without citing sources

**Example:**
```
Claim: "IBM provides superior AI capabilities"
Source: No citation provided
Result: ✗ Flagged - Missing source attribution
```

**Solution:** Always cite source documents

### 4. Misrepresenting Requirements

**Pitfall:** Misrepresenting RFP requirements

**Example:**
```
Claim: "Meets all mandatory requirements"
Source: RFP has 15 mandatory requirements, response addresses 14
Result: ✗ Flagged - Incomplete coverage
```

**Solution:** Verify complete requirement coverage

## Best Practices

### 1. Verify Every Claim

**Principle:** Every claim must be checked against source documents

**Process:**
- Extract all claims from response
- Cross-reference each claim with sources
- Document verification status for each claim

### 2. Use Exact Text Matching

**Principle:** Verify claims using exact text matching

**Process:**
- Search for exact claim text in sources
- Check for variations and context
- Ensure no misrepresentation

### 3. Always Attribute Sources

**Principle:** Always cite source documents

**Process:**
- Include document name and section
- Provide page numbers or line references
- Cite specific clauses or requirements

### 4. Assess Evidence Strength

**Principle:** Assess and document evidence strength

**Process:**
- Strong evidence: Exact match in sources
- Medium evidence: Similar claims with context
- Weak evidence: General statements without support
- No evidence: Unsupported claims

### 5. Provide Actionable Recommendations

**Principle:** Provide clear guidance for addressing flagged items

**Process:**
- Identify specific issues with each flagged claim
- Recommend specific actions (remove, revise, find evidence)
- Prioritize flagged claims by severity

## Example Fact-Check Report

Here's an example of what a fact-check report looks like:

```markdown
# Fact-Check Report

**Response Document:** tender_response.docx
**Source Documents:** rfp.pdf, ibm_capabilities.pdf
**Date:** 2026-03-05 13:45:00

---

## Summary

- Total claims checked: 47
- Verified claims: 42 (89.4%)
- Flagged claims: 5 (10.6%)

## Verified Claims

### IBM provides 99.99% availability

**Evidence Strength:** STRONG

**Source Documents:**
- ibm_capabilities.pdf (exact)

### IBM can deliver AI-powered analytics platform

**Evidence Strength:** STRONG

**Source Documents:**
- ibm_capabilities.pdf (exact)

### Meets all mandatory requirements

**Evidence Strength:** MEDIUM

**Source Documents:**
- rfp.pdf (partial)

## Flagged Claims

### 1. IBM guarantees 100% uptime

**Evidence Strength:** NONE

**Recommendation:**
- Consider removing or finding supporting evidence

### 2. Implementation cost of $1.5 million

**Evidence Strength:** NONE

**Recommendation:**
- Consider removing or finding supporting evidence

## Recommendations

1. Review and revise flagged claims
2. Remove unsupported claims or find supporting evidence
3. Add source document citations to verified claims
4. Consider adding a references section to the response
```

## Integration with Fact-Checker Script

The fact-checking patterns above are implemented in the `fact_check.py` script:

**Script Features:**
- Automatic claim extraction
- Cross-referencing with source documents
- Evidence strength assessment
- Comprehensive report generation
- Support for PDF, DOCX, and TXT formats

**Usage:**
```bash
python3 fact_check.py --response response.docx --sources rfp.pdf ibm_capabilities.pdf
```

**Output:**
- Detailed fact-check report with verified and flagged claims
- Source document references for each claim
- Recommendations for addressing flagged items

---

**Fact-checking is critical for bid quality and compliance. Always verify claims against source documents before submission.**