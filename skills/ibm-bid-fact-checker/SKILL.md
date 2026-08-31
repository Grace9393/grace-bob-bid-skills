---
name: ibm-bid-fact-checker
description: Meticulously verify every statement in IBM tender responses against source documents. Use when Claude needs to validate that all claims, metrics, capabilities, and assertions in generated bid content are supported by the original RFP/ITT documents. Essential for ensuring factual accuracy, preventing hallucinations, and maintaining compliance with source requirements. Trigger when user asks to fact-check, verify, validate, check claims, validate metrics, review for hallucinations, ensure accuracy, verify statements, or perform compliance checks on tender responses.
---

# IBM Bid Fact Checker

## Prerequisites

**Dependencies:** The fact-checking script requires optional Python packages for document processing:
```bash
uv pip install python-docx PyPDF2
```

These packages enable processing of DOCX and PDF files. Text files (.txt, .md) work without additional dependencies.

## Quick Reference

| Item | Value |
|------|-------|
| Script | `$SKILL_DIR/scripts/fact_check.py` |
| Patterns | `$SKILL_DIR/references/fact_checking_patterns.md` |
| Dependencies | python-docx (optional), PyPDF2 (optional) |
| Output | `fact_check_report.md` (configurable) |

## Overview

This skill performs comprehensive fact-checking of IBM tender responses against source documents. It systematically verifies every claim, metric, capability, and assertion to ensure 100% alignment with the original RFP/ITT requirements. The fact-checker identifies unsupported statements, potential hallucinations, and discrepancies that could jeopardize bid quality or compliance.

## When to Use This Skill

Use this skill when:
- A tender response has been generated using $ibm-bid-writer
- User requests fact-checking, verification, validation, or accuracy review
- Need to ensure all claims are supported by source documents
- Checking specific metrics (availability, SLA, performance, pricing)
- Verifying IBM capabilities and differentiators are accurately represented
- Preparing for client review or submission
- Ensuring compliance with RFP/ITT requirements
- Verifying that customer story references comply with `./tmp/ibm-bid-approved-customer-stories.md` when that file exists

## Fact-Checking Workflow

### Step 1: Gather Input Documents

Collect all relevant source documents:
- RFP/ITT tender document (PDF/DOCX)
- IBM capabilities documentation
- Previous IBM responses or references
- Clarification documents or addenda
- `./tmp/ibm-bid-approved-customer-stories.md` when present, as the control list for permitted customer story references

### Step 2: Parse Generated Response

Analyze the generated tender response to identify:
- **Claims and assertions**: Any positive statements about capabilities, performance, or outcomes
- **Metrics and numbers**: Availability percentages, SLA targets, pricing figures, timelines
- **References**: Citations to source documents, case studies, or IBM capabilities
- **Differentiators**: Unique value propositions and competitive positioning statements

### Step 3: Extract Source Content

For each claim type, extract supporting evidence from source documents:
- **Capability claims**: Verify IBM can deliver stated capabilities
- **Performance metrics**: Confirm metrics exist in source documents
- **Pricing information**: Validate pricing claims against RFP requirements
- **Compliance requirements**: Ensure all RFP requirements are addressed with supporting evidence

### Step 4: Cross-Reference and Validate

Systematically, verify each claim:
1. **Claim identification**: Extract the exact claim text
2. **Source search**: Search source documents for supporting evidence
3. **Evidence verification**: Confirm the claim is directly supported
4. **Accuracy check**: Ensure no misrepresentation or exaggeration
5. **Attribution**: Verify proper citation of source documents

### Step 5: Generate Fact-Check Report

Create a comprehensive report with:
- **Verified claims**: List of claims with source document references
- **Flagged claims**: Unsupported or potentially inaccurate statements, providing the exact statement
- **Evidence gaps**: Missing supporting documentation
- **Control-point breaches**: Customer stories used in the response that are not in `./tmp/ibm-bid-approved-customer-stories.md`
- **Recommendations**: Actions to address flagged items

## Fact-Checking Categories

### 1. Performance Metrics

Verify all performance claims:
- Availability percentages (e.g., 99.99%)
- SLA targets and response times
- Throughput and capacity metrics
- Uptime guarantees
- Recovery times

**Example**: If response claims "99.99% availability," verify this exact metric exists in source documents or IBM capabilities documentation.

### 2. Capability Claims

Verify IBM can deliver stated capabilities:
- Technical capabilities and features
- Implementation methodologies
- Support and maintenance services
- Integration capabilities
- Industry-specific solutions

**Example**: If response claims "end-to-end integration with Salesforce," verify this capability exists in IBM capabilities documentation.

### 3. Pricing and Commercial Terms

Verify all pricing claims:
- Cost figures and estimates
- Pricing models (hourly, fixed, subscription)
- Payment terms and conditions
- Discounts and incentives
- Total cost of ownership

**Example**: If response claims "$500,000 total cost," verify this aligns with RFP pricing requirements.

### 4. Compliance and Requirements

Verify all RFP requirements are addressed:
- Mandatory requirements
- Evaluation criteria
- Technical specifications
- Legal and contractual requirements
- Deliverables and milestones

**Example**: If response claims "meets all mandatory requirements," verify each mandatory requirement is explicitly addressed.

### 5. Differentiators and Value Propositions

Verify competitive positioning claims:
- Unique value propositions
- Competitive advantages
- IBM-specific capabilities
- Differentiation from other vendors

**Example**: If response claims "IBM's AI capabilities are superior," verify this is supported by IBM capabilities documentation.

### 6. Customer Story Control-Point Compliance

Verify customer story usage against the approved shortlist when it exists:
- Identify every customer story reference in the response
- Cross-check each one against `./tmp/ibm-bid-approved-customer-stories.md`
- Flag any customer story that is used but not approved
- Flag any approved story that is materially overstated beyond the permitted reusable proof points or stated limits

## Fact-Checking Tools

### Using Scripts

The skill includes a fact-checking script that can help automate the verification process:

```bash
uv run python $SKILL_DIR/scripts/fact_check.py --response <response_file> --sources <source_files>
```

This script performs:
- Text extraction from source documents
- Claim pattern matching
- Source document indexing
- Evidence retrieval
- Report generation

### Manual Fact-Checking Process

For complex or nuanced claims, use manual verification:
1. Copy claim text
2. Search source documents using grep/ripgrep
3. Verify exact wording and context
4. Document source references
5. Flag discrepancies

## Fact-Checking Best Practices

### 1. Exact Match Verification

Verify claims using exact text matching:
- Search for the exact claim text in source documents
- Check for variations and context
- Ensure no misrepresentation

### 2. Source Attribution

Always attribute claims to specific source documents:
- Include document name and section
- Provide page numbers or line references
- Cite specific clauses or requirements

### 3. Evidence Strength

Assess evidence strength:
- **Strong evidence**: Exact match in source documents
- **Medium evidence**: Similar claims with supporting context
- **Weak evidence**: General statements without specific support
- **No evidence**: Unsupported claims requiring revision

### 4. Contextual Verification

Verify claims in context:
- Check surrounding requirements
- Ensure claims address specific RFP needs
- Validate claims against evaluation criteria

## Reporting Format

Generate a structured fact-check report:

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

## Control-Point Breaches
[List of customer story references that are outside the approved shortlist or exceed approved limits]

## Recommendations
[Actions to address flagged items]
```

## Common Fact-Checking Patterns

### Pattern 1: Metric Verification

**Claim**: "99.99% availability"
**Verification**: Search source documents for "99.99%" or "four nines"
**Result**: [Verified/Flagged]

### Pattern 2: Capability Verification

**Claim**: "IBM can deliver AI-powered analytics"
**Verification**: Search IBM capabilities documentation for "AI-powered analytics"
**Result**: [Verified/Flagged]

### Pattern 3: Requirement Verification

**Claim**: "Meets all mandatory requirements"
**Verification**: Cross-reference with RFP mandatory requirements section
**Result**: [Verified/Flagged]

### Pattern 4: Approved Story Verification

**Claim**: Uses named customer story as proof point
**Verification**: Check that the story appears in `./tmp/ibm-bid-approved-customer-stories.md` and that the cited proof stays within the approved reusable points and limits
**Result**: [Verified/Flagged]

## Resources

This skill includes the following resources:

### $SKILL_DIR/scripts/fact_check.py

Python script for automated fact-checking:
- Parses response documents
- Extracts claims and metrics
- Cross-references with source documents
- Generates verification reports
- Handles PDF and DOCX formats

### $SKILL_DIR/references/fact_checking_patterns.md

Detailed patterns and examples for fact-checking:
- Common claim types in tender responses
- Verification techniques and methods
- Evidence strength assessment criteria
- Reporting templates and formats

## Example Usage

**User Request**: "Fact-check this tender response against the RFP document"

**Skill Execution**:
1. Load the generated response document
2. Load the RFP source document
3. Extract all claims and assertions
4. Cross-reference each claim with source documents
5. Generate comprehensive fact-check report
6. Present findings with source document references

**Output**: Detailed report showing verified claims, flagged items, and recommendations for revision.

## Quality Standards

- **100% verification**: Every claim must be checked
- **Exact matching**: Verify exact wording and context
- **Source attribution**: Always cite source documents
- **Evidence strength**: Assess and document evidence quality
- **Actionable recommendations**: Provide clear guidance for addressing flagged items

## Integration with Other Skills

This skill works seamlessly with:
- **$ibm-bid-writer**: Fact-check generated responses before submission
- **$ibm-bid-requirements-analysis**: Validate responses against requirements analysis
- **$ibm-bid-library**: Cross-reference with IBM historical responses
- **$ibm-bid-tda-review**: Ensure technical claims are accurate

---

**Fact-checking is critical for bid quality and compliance. Always verify claims against source documents before submission.**
