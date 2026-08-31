# Requirements Analysis Framework

## Level 1 Analysis: Surface Extraction

Extract information directly as stated in the tender document without interpretation:

**Client Profile:**
- Organisation name, type, and sector
- Scale indicators (staff count, budget, geography)
- Current technology landscape (if mentioned)
- Procurement stage and context

**Stated Requirements:**
- Functional capabilities required
- Technical specifications and constraints
- Integration requirements
- Performance and scalability needs
- Security and compliance requirements
- Commercial and contractual terms

**Evaluation Criteria:**
- Quality/technical scoring weightings
- Price/commercial weightings
- Social value or other scoring dimensions
- Pass/fail criteria or minimum thresholds

## Level 2 Analysis: Contextual Understanding

### Pain Point Analysis
Extract underlying operational failures from stated problems:

**Indicators to look for:**
- Repeated emphasis on specific capabilities → current system lacks these
- Detailed constraints on timelines → pressure from external factors
- Risk management requirements → previous failures or audit findings
- Integration requirements → siloed systems causing inefficiency
- User experience focus → poor adoption of current systems
- Compliance emphasis → regulatory pressure or past violations

**Pattern matching:**
```
Stated: "Must integrate with existing CRM"
→ Underlying: Disconnected data causing decision delays

Stated: "User training and change management essential"
→ Underlying: History of failed implementations due to poor adoption

Stated: "Must demonstrate value within 6 months"
→ Underlying: Political pressure or budget cycle constraints
```

### Capability Gap Identification

**Technical gaps:**
- What technologies are conspicuously absent from requirements?
- Which integrations suggest current system limitations?
- What data formats indicate legacy infrastructure?

**Organisational gaps:**
- Extensive training requirements → low technical capability
- Change management focus → resistance to change
- Governance requirements → lack of internal controls

**Process gaps:**
- Automation requirements → manual process pain
- Reporting emphasis → poor visibility currently
- Workflow requirements → process inefficiency

### Risk Profile Decoding

**Explicit risks in tender:**
- Mentioned risks = confirmed concerns
- Weight these heavily in your response

**Implicit risks from requirements:**
- Excessive detail in one area → past failure in that area
- Backup/recovery emphasis → data loss incidents
- Security focus → breach history or sector requirements
- Scalability requirements → past system collapse under load

### Competitive Landscape Inference

**Incumbent signals:**
- Requirements matching specific vendor capabilities
- Terminology from particular platforms
- Integration requirements favouring certain architectures
- Evaluation criteria weighting familiar patterns

**Market testing indicators:**
- Unusually specific functional requirements
- Reference to "leading practice" from specific sectors
- Requirements that bundle disparate capabilities

**Budget constraint signals:**
- Phased delivery requirements
- Cloud/SaaS preference
- Staff augmentation language
- Risk transfer mechanisms

## Sector-Specific Context

### UK Public Sector
- Framework agreements (G-Cloud, CCS, DPS)
- Social value mandatory (10-20% typical weighting)
- SME and local supply chain emphasis
- Transparency and audit trail requirements
- Value for money justification needed

### NHS/Healthcare
- Information Governance (IG) Toolkit compliance
- NHS Spine and national system integration
- Clinical safety (DCB0129/0160 standards)
- Patient data protection (GDPR + sector-specific)
- Inter-operability with existing clinical systems

### Central Government
- Security clearance requirements (SC, DV)
- Government Digital Service (GDS) standards
- Digital by default service design
- Citizen-centric service delivery
- Cross-government platform integration

### Local Government
- Severe budget constraints
- Shared services models prevalent
- Local economic impact (jobs, skills, environment)
- Smaller scale, higher risk aversion
- Councillor and public accountability

## Analysis Output Requirements

**Completeness checks:**
1. Client profile captures organisation context
2. All stated requirements categorized correctly
3. Evaluation weightings extracted (or noted as absent)
4. Operational gaps mapped to stated requirements
5. Capability deficits identified across technical/organisational/process
6. Risk profile includes stated + unstated risks
7. Competitive landscape identifies likely bidders and incumbent signals

**Quality indicators:**
- Every requirement has an identified underlying need
- Risks are specific and actionable (not generic)
- Competitive analysis names specific likely bidders
- Gaps are traced to business impact
