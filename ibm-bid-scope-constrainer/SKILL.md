---
name: ibm-bid-scope-constrainer
description: Transform open-ended or unconstrained client requirements into bounded, scope-limited statements that minimize IBM delivery risk and reduce estimates. Use when client requirements are vague, unlimited, or lack clear boundaries (e.g., "reporting", "integrations", "user management"). Applies domain-specific constraints from Salesforce, web development, integration, data, and AI/ML projects.
---

# Bid Scope Constrainer Skill

Transform open-ended client requirements into bounded, scope-limited statements that protect IBM from delivery risk and enable accurate estimation.

## When to Use This Skill

Use this skill when you encounter client requirements that are:
- **Vague or open-ended**: "We need reporting" → How many reports? What complexity?
- **Unlimited in scope**: "All integrations" → Which systems? What protocols?
- **Missing boundaries**: "User management" → How many users? What roles?
- **Technology-agnostic**: "Data warehouse" → What volume? What platform?
- **Performance-undefined**: "Fast response times" → What latency? What percentile?

## Complete Tender Response Workflow

This skill is part of the 5-phase IBM Bid Management workflow.

**Current Phase**: Phase 1 (Strategic Positioning) or Phase 2 (Solution Architecture)
**Position**: Use after requirements analysis, before detailed solution design

**Typical workflow**:
1. `ibm-bid-requirements-analysis` - Extract requirements
2. **`ibm-bid-scope-constrainer`** - Add scope boundaries ← YOU ARE HERE
3. `ibm-bid-solution-architect` - Design solution within boundaries
4. `ibm-bid-writer` - Write proposal with clear scope

See `ibm-bid-navigator` for complete workflow guidance.

## Quick Start

**Input**: One or more open-ended client requirements
**Output**: Bounded requirements with clear scope-limiting statements

```bash
# Example usage
User: "The client needs reporting capabilities"

Skill output:
- Reporting tool: Power BI
- Reports/dashboards: maximum 25 included
- Data refresh frequency: daily (real-time excluded)
- User concurrency: designed for 50 concurrent users
- Ad-hoc query capability: excluded; predefined reports only
```

## Context Management

- Write analysis to `./tmp/ibm-bid-scope-constrainer.md` for reference
- Copy final bounded requirements to `./outputs/` at completion
- Update `./tmp/ibm-bid-project.md` with:
  - `scope_boundaries_status: applied`
  - `scope_boundaries_artifact: ./tmp/ibm-bid-scope-constrainer.md`
  - `key_risks`: include any residual scope risks or assumptions
  - `artifacts_generated`: include `./tmp/ibm-bid-scope-constrainer.md`
  - `next_skill_recommendation`: normally return to the relevant solution, pricing, or writing skill

## Processing Workflow

### Step 1: Identify Requirement Domain

Classify the requirement into one or more domains:
- **Salesforce**: CRM, CPQ, Communities, custom objects
- **Web Development**: Frontend, responsive design, accessibility
- **Integration**: APIs, data sync, middleware
- **Data**: ETL, data warehouse, analytics, reporting
- **AI/ML**: Machine learning, NLP, computer vision

### Step 2: Load Domain-Specific Boundaries

Reference the appropriate domain guide from `references/`:
- `salesforce-scope-boundaries.md` - Salesforce projects
- `web-development-scope-boundaries.md` - Web/frontend projects
- `integration-scope-boundaries.md` - Integration projects
- `data-scope-boundaries.md` - Data/analytics projects
- `ai-ml-scope-boundaries.md` - AI/ML projects

### Step 3: Apply Bounding Statements

For each open-ended requirement, apply 3-5 bounding statements that:
1. **Quantify scope**: Specify numbers, limits, maximums
2. **Define exclusions**: State what's NOT included
3. **Clarify technology**: Specify platforms, tools, versions
4. **Set performance targets**: Define acceptable thresholds
5. **Establish change control**: Require approval for additions

### Step 4: Calculate Risk Reduction

Estimate the impact of scope boundaries:
- **Estimation accuracy**: Improved by 25-45%
- **Delivery risk**: Reduced by identifying exclusions upfront
- **Change requests**: Minimized through clear boundaries
- **Client expectations**: Managed through explicit constraints

## Bounding Statement Framework

Use this template for each requirement:

```markdown
### Original Requirement
[Client's open-ended requirement]

### Bounded Requirement
[Specific, constrained version]

### Bounding Statements
1. [Quantitative limit]: [specific number/threshold]
2. [Technology constraint]: [specific platform/tool]
3. [Exclusion statement]: [what's NOT included]
4. [Performance target]: [specific metric]
5. [Change control]: [approval process for additions]

### Risk Mitigation
- [How this protects IBM from delivery risk]
- [How this enables accurate estimation]

### Estimation Impact
- Original estimate: [range] (unbounded)
- Bounded estimate: [specific] (25-45% reduction)
```

## Common Requirement Patterns

### Pattern 1: "Reporting" or "Dashboards"

**Open-ended**: "We need reporting capabilities"

**Bounded**:
- Reporting tool: [Power BI / Tableau / Looker]
- Reports/dashboards: maximum [15-25] included
- Data refresh frequency: [daily / hourly] (real-time excluded)
- User concurrency: designed for [50-100] concurrent users
- Ad-hoc query capability: excluded; predefined reports only

### Pattern 2: "Integrations"

**Open-ended**: "Integrate with our systems"

**Bounded**:
- Integration count: [3-5] systems: [list specific systems]
- Integration pattern: [REST API / SOAP / File Transfer]
- Data sync frequency: [hourly / daily] (real-time excluded)
- API endpoints: maximum [10-15] per system
- Custom integration code: excluded; platform connectors only

### Pattern 3: "User Management"

**Open-ended**: "User management functionality"

**Bounded**:
- User count: up to [500 / 1000 / 5000] users
- User roles: maximum [5-10] roles
- Authentication: [SSO / SAML / OAuth 2.0]
- Self-service registration: excluded; admin-provisioned only
- Advanced permissions: excluded; role-based access control (RBAC) only

### Pattern 4: "Data Migration"

**Open-ended**: "Migrate our data"

**Bounded**:
- Data sources: [2-3] systems: [list specific sources]
- Data volume: maximum [100GB / 1TB]
- Migration approach: [full load / incremental]
- Data quality: format validation only; cleansing excluded
- Historical data: [1-2 years]; older data archived

### Pattern 5: "Performance"

**Open-ended**: "Fast performance"

**Bounded**:
- Page load time: [2-3] seconds for [95]% of requests
- API response time: [500ms] for [90]% of requests
- Concurrent users: designed for [100-500] users
- Database queries: [1-2] seconds for [90]% of queries
- Performance testing: [specific scenarios]; load testing excluded

### Pattern 6: "Customization"

**Open-ended**: "Customizable solution"

**Bounded**:
- Custom fields: maximum [50-100] per object
- Custom objects: maximum [10-20]
- Custom workflows: maximum [15-25]
- Custom code: excluded; configuration-based only
- UI customization: branding and layout only; custom components excluded

### Pattern 7: "Mobile Support"

**Open-ended**: "Mobile-friendly"

**Bounded**:
- Mobile approach: responsive web design (native apps excluded)
- Device support: iOS [version+] and Android [version+]
- Screen sizes: [320px-1920px] width
- Offline capability: excluded; online-only
- Mobile-specific features: excluded; responsive layout only

### Pattern 8: "AI/ML Capabilities"

**Open-ended**: "AI-powered features"

**Bounded**:
- ML problem type: [classification / regression / recommendation]
- Model complexity: pre-trained models only; custom training excluded
- Training data: client-provided [10K+] labeled examples
- Target accuracy: [80-85]% on test set
- Real-time inference: excluded; batch predictions only

### Pattern 9: "Security"

**Open-ended**: "Secure solution"

**Bounded**:
- Authentication: [OAuth 2.0 / SAML]
- Authorization: role-based access control (RBAC) with [5-10] roles
- Encryption: TLS 1.2+ in transit; at-rest encryption client responsibility
- Audit logging: access logs retained for [90 days]
- Penetration testing: excluded; security best practices followed

### Pattern 10: "Scalability"

**Open-ended**: "Scalable architecture"

**Bounded**:
- User capacity: designed for [500-1000] concurrent users
- Data volume: up to [1TB / 10TB]
- Transaction volume: [1000] transactions per minute
- Growth projection: [20]% annual growth; re-architecture required beyond
- Auto-scaling: excluded; manual scaling with [notice period]

## Domain-Specific Guidance

### Salesforce Projects

Key boundaries to apply:
- Edition limits (Professional, Enterprise, Unlimited)
- Object/field limits (custom objects, fields per object)
- Automation limits (workflows, process builders, flows)
- Storage limits (data storage, file storage)
- API call limits (daily API calls)

Reference: `references/salesforce-scope-boundaries.md`

### Web Development Projects

Key boundaries to apply:
- Browser compatibility (specific browsers and versions)
- Responsive breakpoints (specific screen sizes)
- Accessibility level (WCAG 2.1 Level A/AA)
- Performance targets (page load, Time to Interactive)
- Framework/library versions

Reference: `references/web-development-scope-boundaries.md`

### Integration Projects

Key boundaries to apply:
- Integration pattern (point-to-point, hub-and-spoke, ESB)
- System count (specific systems to integrate)
- Data mapping complexity (field count, transformation rules)
- Sync frequency (real-time, batch, scheduled)
- Error handling approach

Reference: `references/integration-scope-boundaries.md`

### Data Projects

Key boundaries to apply:
- Data volume (GB/TB, record count)
- Data sources (specific systems, file formats)
- ETL complexity (transformation rules)
- Data quality scope (validation, cleansing)
- Reporting/analytics scope

Reference: `references/data-scope-boundaries.md`

### AI/ML Projects

Key boundaries to apply:
- ML problem type (classification, regression, etc.)
- Training data requirements (volume, quality)
- Model complexity (algorithms, frameworks)
- Performance targets (accuracy, latency)
- Deployment approach (batch, real-time)

Reference: `references/ai-ml-scope-boundaries.md`

## Output Format

Generate output in this structure:

```markdown
# Scope-Constrained Requirements
**Project**: [Project Name]
**Date**: [Date]
**Analyst**: IBM Bid Team

## Executive Summary
[Brief overview of scope boundaries applied and risk reduction achieved]

## Constrained Requirements

### 1. [Requirement Category]

#### Original Requirement
[Client's open-ended requirement]

#### Bounded Requirement
[Specific, constrained version]

#### Bounding Statements
1. [Quantitative limit]
2. [Technology constraint]
3. [Exclusion statement]
4. [Performance target]
5. [Change control]

#### Risk Mitigation
- [Delivery risk reduction]
- [Estimation accuracy improvement]

#### Estimation Impact
- Unbounded estimate: [range]
- Bounded estimate: [specific]
- Reduction: [percentage]%

---

[Repeat for each requirement]

## Overall Impact

### Estimation Accuracy
- Original estimate range: [wide range]
- Bounded estimate: [specific range]
- Improvement: [percentage]% reduction in uncertainty

### Risk Reduction
- [Key risks mitigated]
- [Clear exclusions established]
- [Change control mechanisms]

### Next Steps
1. Review bounded requirements with client
2. Obtain client approval on scope boundaries
3. Proceed to detailed solution design
4. Update SOW with bounded requirements
```

## Best Practices

### DO:
- ✅ Apply 3-5 bounding statements per requirement
- ✅ Use specific numbers, not ranges (e.g., "25 reports" not "20-30 reports")
- ✅ State exclusions explicitly (e.g., "real-time excluded")
- ✅ Reference industry standards (e.g., "WCAG 2.1 Level AA")
- ✅ Quantify estimation impact (e.g., "30% reduction")
- ✅ Provide rationale for each boundary
- ✅ Consider client's actual needs vs. wants

### DON'T:
- ❌ Leave requirements unbounded
- ❌ Use vague terms (e.g., "reasonable number")
- ❌ Assume unlimited scope
- ❌ Skip exclusion statements
- ❌ Ignore domain-specific constraints
- ❌ Over-constrain to the point of being unusable
- ❌ Apply boundaries without rationale

## Examples

### Example 1: Salesforce Reporting

**Input**: "We need comprehensive reporting in Salesforce"

**Output**:
```markdown
### Bounded Requirement: Salesforce Reporting

#### Bounding Statements
1. **Report count**: Maximum 25 standard reports included
2. **Dashboard count**: Maximum 10 dashboards with 5 components each
3. **Report complexity**: Standard report types only; matrix reports limited to 5
4. **Refresh frequency**: Daily scheduled refresh; real-time dashboards excluded
5. **Custom report types**: Maximum 5 custom report types

#### Exclusions
- Real-time dashboards
- Einstein Analytics integration
- Custom Lightning components in dashboards
- Report subscriptions beyond standard email
- Advanced analytics (trending, forecasting)

#### Risk Mitigation
- Prevents unlimited report development
- Establishes clear deliverable count
- Protects against complex analytics requests
- Enables accurate effort estimation

#### Estimation Impact
- Unbounded: 40-120 hours (3x variance)
- Bounded: 60-80 hours (1.3x variance)
- Reduction: 33% in estimate uncertainty
```

### Example 2: API Integration

**Input**: "Integrate with our ERP system"

**Output**:
```markdown
### Bounded Requirement: ERP Integration

#### Bounding Statements
1. **Integration pattern**: REST API only; SOAP excluded
2. **API endpoints**: Maximum 10 endpoints (5 read, 5 write)
3. **Data sync frequency**: Hourly batch sync; real-time excluded
4. **Data volume**: Maximum 10,000 records per sync
5. **Error handling**: Standard retry logic (3 attempts); custom workflows excluded

#### Exclusions
- Real-time synchronization
- Complex data transformations
- Multiple ERP systems
- Custom middleware development
- Bi-directional sync (unidirectional only)

#### Risk Mitigation
- Limits integration complexity
- Establishes clear technical approach
- Prevents performance issues
- Protects against unlimited API development

#### Estimation Impact
- Unbounded: 80-240 hours (3x variance)
- Bounded: 120-160 hours (1.3x variance)
- Reduction: 40% in estimate uncertainty
```

## Reference Materials

All domain-specific boundary guides are located in `references/`:

1. **salesforce-scope-boundaries.md** - Salesforce edition limits, objects, automation
2. **web-development-scope-boundaries.md** - Browser support, responsive design, accessibility
3. **integration-scope-boundaries.md** - Integration patterns, data mapping, protocols
4. **data-scope-boundaries.md** - Data volume, ETL, data quality, reporting
5. **ai-ml-scope-boundaries.md** - ML models, training data, performance targets

## Skill Chaining

**Before this skill**:
- `ibm-bid-requirements-analysis` - Extract and analyze requirements
- `ibm-bid-clarifications` - Clarify ambiguous requirements

**After this skill**:
- `ibm-bid-solution-architect` - Design solution within boundaries
- `ibm-bid-writer` - Write proposal with bounded scope
- `ibm-bid-pricing-strategy` - Estimate based on bounded requirements

**Parallel skills**:
- `ibm-bid-strategic-positioning` - Strategic approach
- `ibm-bid-win-themes` - Value proposition

## Success Criteria

A successful scope-constraining session should achieve:

1. **Clear Boundaries**: Every open-ended requirement has 3-5 specific constraints
2. **Explicit Exclusions**: What's NOT included is clearly stated
3. **Quantified Limits**: Numbers, thresholds, maximums are specified
4. **Risk Reduction**: Delivery risks are identified and mitigated
5. **Estimation Improvement**: Estimate uncertainty reduced by 25-45%
6. **Client Alignment**: Boundaries are reasonable and defensible

## Troubleshooting

### Issue: Client pushes back on boundaries

**Solution**: 
- Explain risk and estimation impact of unbounded scope
- Offer tiered options (basic, standard, advanced)
- Quantify cost difference between bounded and unbounded
- Reference industry standards and best practices

### Issue: Requirements span multiple domains

**Solution**:
- Apply boundaries from all relevant domains
- Prioritize the most critical boundaries
- Create a consolidated boundary statement
- Reference multiple domain guides

### Issue: Boundaries seem too restrictive

**Solution**:
- Review client's actual needs vs. wants
- Adjust boundaries to be reasonable but protective
- Provide rationale for each boundary
- Offer expansion options with cost implications

### Issue: Unclear which domain applies

**Solution**:
- Start with the primary technology (Salesforce, web, data, etc.)
- Apply general boundaries from main guide
- Layer in domain-specific boundaries as needed
- Consult `ibm-bid-navigator` for workflow guidance

## Version History

- **v1.0** (2026-02-20): Initial release with 5 domain guides
