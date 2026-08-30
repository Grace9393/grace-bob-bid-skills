---
name: ibm-bid-requirements-analysis
description: Extract and analyze tender requirements from RFPs, ITTs, and procurement documents (PDF/DOCX). Performs document extraction, client profile analysis, stated requirements breakdown, and contextual analysis (operational gaps, capability deficits, risk profile). First step in Phase 0, feeds ibm-bid-strategic-positioning and other bid skills.
---

# Bid Requirements Analysis Skill

Extract and analyze tender requirements to understand client needs, operational gaps, and capability deficits. Strategic positioning is handled by the `ibm-bid-strategic-positioning` skill.

## Complete Tender Response Workflow

This skill is part of the 5-phase IBM Bid Management workflow.

**Current Phase**: Phase 0 (Opportunity Assessment)
**Position**: First step - run before strategic-positioning, clarifications, and qualification

**Always execute first**: This provides the foundational requirements analysis that all other bid skills depend on.

See ibm-bid-navigator for complete workflow guidance.

## Quick Start

1. User uploads tender document (PDF or DOCX)
2. Run `scripts/process_document.py <filepath>` to extract structure (uses pandoc for DOCX→Markdown if available)
3. Analyse content using framework in `references/requirements_framework.md`
4. Generate output to `./tmp/ibm-bid-requirements-analysis.md`
5. Then proceed to `ibm-bid-strategic-positioning` for strategic analysis

## Context Management

Write output to `./tmp/ibm-bid-requirements-analysis.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `requirements_analysis_status: complete`
- `requirements_analysis_artifact: ./tmp/ibm-bid-requirements-analysis.md`
- tender identity fields: `tender_name`, `tender_value`, `client`, `tender_type`, `submission_deadline`, and `source_documents` where available
- `current_phase: opportunity_assessment`
- `artifacts_generated`: include `./tmp/ibm-bid-requirements-analysis.md` when the artifact is written
- `next_skill_recommendation`: normally `ibm-bid-strategic-positioning`, `ibm-bid-qualification`, or `ibm-bid-clarifications`

## Processing Workflow

### Step 1: Document Extraction

```bash
python3 scripts/process_document.py /mnt/user-data/uploads/<filename>
```

Returns JSON with:
- `sections`: Tender content organised by type (background, requirements, evaluation, etc.)
- `tables`: Extracted tables (evaluation criteria, timelines, budgets)
- `full_text`: Complete document text
- `headings`: Document structure
 - `markdown`: Markdown representation of DOCX (when pandoc is available)

### Step 2: Level 1 Analysis (Surface Extract)

Extract directly from processed content:

**Client Profile:**
- Organisation details from background/about sections
- Sector and scale indicators
- Procurement context

**Stated Requirements:**
- Functional requirements from requirements/scope sections
- Technical specifications
- Commercial terms
- Evaluation criteria from evaluation/scoring sections

**Evaluation Weightings:**
- Extract from tables or evaluation sections
- Note: UK public sector typically uses quality/price/social value split

### Step 3: Level 2 Analysis (Contextual)

Read `references/requirements_framework.md` then apply:

**Operational Gaps:**
- Map stated pain points → underlying system failures
- Identify what current systems cannot do
- Decode constraint language (e.g., "must integrate with X" = siloed data problem)

**Capability Deficits:**
- Technical gaps (missing technologies, integration requirements)
- Organisational gaps (training emphasis, change management needs)
- Process gaps (automation requirements, reporting needs)

**Risk Profile:**
- Explicit risks (mentioned in tender)
- Implicit risks (inferred from requirements patterns)
- Sector-specific risks (healthcare = data protection, government = transparency)

**Competitive Landscape:**
- Incumbent signals (requirements favouring specific platforms)
- Market testing indicators (unusually specific requirements)
- Budget constraints (phasing, cloud preference, risk transfer)

## Key Patterns to Recognise

**UK Government Tenders:**
- Framework agreements (G-Cloud, CCS, DPS)
- Social value requirements (10-20% weighting typical)
- SME/local supply chain emphasis
- Transparency and audit requirements

**NHS/Healthcare:**
- IG Toolkit compliance
- Integration with NHS Spine/national systems
- Clinical safety requirements
- Patient data protection emphasis

**Central Government:**
- Security clearance requirements
- Citizen service focus
- Digital by default alignment
- GDS service standards

**Local Government:**
- Budget constraints
- Shared services models
- Local priorities (jobs, skills, environment)
- Smaller scale, higher risk aversion

## Analysis Quality Checks

Before finalising output:

1. Every stated requirement mapped to underlying need
2. Client profile complete (organisation, sector, context)
3. Operational gaps clearly identified with business impact
4. Risk profile includes both stated and unstated risks
5. Competitive landscape identifies likely bidders

## Script Usage Notes

`process_document.py` handles:
- PDF text extraction (pdfplumber)
- DOCX structure preservation (python-docx)
- DOCX → Markdown conversion (pandoc if available; used for sectioning and analysis)
- Section identification (UK government tender patterns)
- Table extraction (evaluation criteria, timelines)

**Format support**:
- `.docx` supported
- `.doc` not supported; convert to `.docx` first

Output is JSON for programmatic processing. Extract relevant sections for analysis.

## Output Format

Use template from `references/output_template.md`. Structure:

```markdown
# REQUIREMENTS ANALYSIS: [CLIENT NAME]

## EXECUTIVE SUMMARY
[2-3 sentences: what they want, what they really need, key challenges]

## CLIENT PROFILE
[Organisation type, sector, scale, procurement context, stakeholders]

## STATED REQUIREMENTS
### Functional Requirements
### Technical Requirements
### Commercial Requirements
### Evaluation Criteria

## LEVEL 2: UNDERLYING NEEDS

### Operational Gaps
**What's broken:** [Current system failures]
**Impact:** [Business consequences]

### Capability Deficits
**Technical:** [Technology gaps]
**Organisational:** [Skills, governance gaps]
**Process:** [Workflow inefficiencies]

### Risk Profile
**Stated risks:** [Explicit from tender]
**Unstated risks:** [Implied by context]

### Competitive Dynamics
**Incumbent signals:** [Existing supplier influence]
**Likely bidders:** [Who else, their approach]
**Budget indicators:** [Value range, constraints]
```

## Integration with Other Skills

### Required Inputs
- **RFP/ITT document**: Primary tender document (PDF or DOCX)
- **Optional: Previous bid analysis**: For rebids, compare with historical analysis

### Recommended Next Steps

**After requirements analysis complete:**

**1. Run ibm-bid-strategic-positioning** (sequential):
- Input: ./tmp/ibm-bid-requirements-analysis.md (this skill's output)
- Output: Strategic positioning, sales strategy, price-to-win analysis
- Creates: ./tmp/ibm-bid-strategic-positioning.md

**2. Run Phase 0 skills in parallel** (if not already executed):
- **ibm-bid-clarifications**: Identify ambiguous requirements requiring client clarification
  - Input: ./tmp/ibm-bid-requirements-analysis.md
- **ibm-bid-qualification**: Score opportunity (GO/NO-GO decision)
  - Input: ./tmp/ibm-bid-requirements-analysis.md

**3. After Phase 0 complete, proceed to Quality Gate 1**:
- Review qualification score
- Make GO/NO-GO decision
- If GO (score ≥60), proceed to Phase 1

### Supporting Resources
- **ibm-bid-library**: Search for similar tenders or previous analysis for this client
- **ibm-bid-customer-stories**: Search for customer stories matching client's sector
- **ibm-bid-strategy-and-capabilities-2026**: Reference IBM capabilities matching identified needs

### This Skill Feeds Downstream Skills

The analysis output (./tmp/ibm-bid-requirements-analysis.md) is consumed by:

**Phase 0**:
- ibm-bid-strategic-positioning (primary next step - strategic analysis)
- ibm-bid-clarifications (identifies gaps requiring clarification)
- ibm-bid-qualification (provides scoring context)

**Phase 1**:
- ibm-bid-win-themes (client context and underlying needs)
- ibm-bid-executive-summary (client context)

**Phase 2**:
- ibm-sf-solution-architect or ibm-bid-solution-architect (requirements traceability)

**Phase 3**:
- ibm-bid-writer (client context for all responses)

**Phase 4**:
- ibm-bid-tda-review (requirements alignment validation)

### Quality Gate 1 Impact

This analysis directly informs Quality Gate 1 (GO/NO-GO decision) by providing:
- **Client profile**: Organization readiness and strategic context
- **Requirements clarity**: Well-defined vs. ambiguous requirements
- **Underlying needs**: Real problems vs. stated requirements
- **Competitive landscape**: Incumbent advantage, likely bidders
- **Risk profile**: Technical and organizational delivery risks

**Analysis quality indicators for GO decision**:
- Clear evaluation criteria with weightings (reduces risk)
- Well-defined requirements (reduces scope ambiguity)
- Identifiable underlying needs (enables differentiation)
- Competitive positioning opportunities (path to win)

**Analysis red flags suggesting NO-GO**:
- Vague or contradictory requirements (high delivery risk)
- RFP written around competitor solution (wired bid)
- Unrealistic timelines or budgets (unwinnable)
- No clear underlying needs (commoditized competition)
