# Salesforce Scope-Limiting Bounding Statements

## Domain-Specific Boundaries for Salesforce Projects

## Consideration Decomposition

Framework: `components`
Depth: `2`
Breadth: `4`
Maturity Mode: `off`
Output Format: `markdown`

Structure Summary:
- Top-level Questions: `4`
- Children Per Parent: `4`
- Leaf Count: `16`

### Tree

- `1` What org and platform assumptions must be fixed to keep the Salesforce scope viable?
  - `1.1` Which edition, clouds, licenses, environments, and platform limits are assumed, and what happens if the client estate differs?
  - `1.2` What object-model limits for objects, fields, record types, relationships, files, and automation artifacts must be stated to constrain design complexity?
  - `1.3` Which assumptions about installed packages, technical debt, automation conflicts, org hygiene, and available sandboxes need to be explicit?
  - `1.4` What client-owned prerequisites for licenses, environments, release windows, and access must be confirmed before delivery starts?
- `2` What solution-delivery boundaries are required to contain implementation effort?
  - `2.1` What limits should be set on declarative automation, Apex, LWCs, integrations, data migration volume, and reporting outputs?
  - `2.2` Which user-experience commitments for Lightning pages, Experience Cloud, mobile usage, and CPQ/Revenue Cloud require explicit exclusions or caps?
  - `2.3` What testing, deployment, API-consumption, release-management, and regression responsibilities need to be fixed before estimation?
  - `2.4` Which assumptions about design authority, backlog control, and change-request thresholds should be stated so requirements cannot expand informally?
- `3` What operational and governance boundaries are required to avoid hidden Salesforce obligations?
  - `3.1` Which ownership split applies to security design, sharing model decisions, profile rationalization, permission-set strategy, and license procurement?
  - `3.2` What managed-service, admin support, hypercare, and enhancement expectations are included, and which backlog items are excluded?
  - `3.3` Which data-quality, deduplication, archival, and reporting-governance responsibilities remain with the client?
  - `3.4` What post-go-live monitoring, incident handling, and performance-optimization commitments are included versus excluded?
- `4` What commercial and re-scope triggers must be explicit in Salesforce bids?
  - `4.1` Which trigger conditions should force re-scoping, such as edition upgrades, new clouds, additional integrations, governor-limit pressure, or major data-cleansing needs?
  - `4.2` What assumptions about non-production environments, deployment tooling, and release coordination should be restated in every estimate?
  - `4.3` Which requests for custom development, advanced analytics, external sharing, or complex CPQ logic should automatically be treated as out-of-scope unless separately priced?
  - `4.4` What wording best protects the bid from implied obligations around org remediation, legacy cleanup, and future scalability beyond the agreed design envelope?

### 1. Salesforce Edition and License Boundaries

**Bounding Statements:**
- "Solution designed for Salesforce Enterprise Edition; Professional Edition requires re-architecture"
- "Assumes [number] Sales Cloud licenses, [number] Service Cloud licenses"
- "Platform licenses excluded; requires full user licenses"
- "Sandbox environments: 1 Full, 2 Partial; additional sandboxes client responsibility"
- "API call limits: solution operates within [percentage]% of org limits"

**Risk Mitigation:**
- Prevents edition-specific feature assumptions
- Clarifies license procurement responsibilities
- Establishes sandbox strategy upfront
- Protects against API limit violations

### 2. Salesforce Object and Field Limits

**Bounding Statements:**
- "Custom objects limited to [number]; standard objects used where possible"
- "Maximum [number] custom fields per object"
- "Formula fields limited to [number] per object due to performance"
- "Lookup relationships capped at [number] per object"
- "Master-detail relationships: maximum [number] per object"

**Risk Mitigation:**
- Prevents hitting Salesforce governor limits
- Manages data model complexity
- Protects against performance degradation
- Establishes clear data architecture boundaries

### 3. Automation and Code Boundaries

**Bounding Statements:**
- "Declarative automation preferred; Apex code only where necessary"
- "Maximum [number] workflow rules, [number] process builders, [number] flows"
- "Apex code coverage minimum 85%; test classes included"
- "Trigger framework: one trigger per object maximum"
- "Batch Apex jobs limited to [number]; scheduled jobs capped at [number]"

**Risk Mitigation:**
- Prevents automation sprawl and conflicts
- Establishes code quality standards
- Manages governor limit exposure
- Clarifies technical approach

### 4. Integration Scope (Salesforce-Specific)

**Bounding Statements:**
- "Integrations via REST API only; SOAP API excluded"
- "Real-time integrations limited to [number] systems"
- "Batch integrations: maximum [frequency] per day"
- "Middleware: client-provided (MuleSoft/Dell Boomi/etc.)"
- "Platform Events limited to [number] event types"

**Risk Mitigation:**
- Clarifies integration architecture
- Establishes middleware ownership
- Limits integration complexity
- Protects against integration failures

### 5. User Interface Customization Boundaries

**Bounding Statements:**
- "Lightning Experience only; Classic UI not supported"
- "Standard Lightning components used; custom LWC limited to [number]"
- "Page layouts: maximum [number] per object"
- "Record types: limited to [number] per object"
- "Mobile app: Salesforce Mobile App only; custom mobile app excluded"

**Risk Mitigation:**
- Prevents UI complexity explosion
- Clarifies mobile strategy
- Establishes component reuse approach
- Manages maintenance burden

### 6. Data Migration Boundaries (Salesforce)

**Bounding Statements:**
- "Data migration via Data Loader; ETL tools excluded"
- "Historical data: [timeframe] only; older data archived"
- "Data cleansing: deduplication and format standardization only"
- "Attachments/files: maximum [size] per record, [total size] overall"
- "Migration validation: [percentage]% sample verification"

**Risk Mitigation:**
- Manages migration complexity and duration
- Establishes data quality responsibilities
- Protects against storage limit violations
- Clarifies validation approach

### 7. Salesforce Security and Sharing

**Bounding Statements:**
- "Security model: [approach] (e.g., private with sharing rules)"
- "Profiles: maximum [number]; permission sets preferred"
- "Sharing rules: limited to [number] per object"
- "Field-level security: defined for [user types] only"
- "External sharing: excluded unless explicitly scoped"

**Risk Mitigation:**
- Prevents security model complexity
- Establishes access control approach
- Manages sharing rule performance impact
- Clarifies external user strategy

### 8. Salesforce Reporting and Analytics

**Bounding Statements:**
- "Standard reports and dashboards: [number] included"
- "Custom report types: maximum [number]"
- "Dashboard components: maximum [number] per dashboard"
- "Einstein Analytics/Tableau CRM: excluded from scope"
- "Report scheduling: maximum [number] scheduled reports"

**Risk Mitigation:**
- Prevents unlimited reporting requests
- Establishes analytics platform boundaries
- Manages report performance impact
- Clarifies advanced analytics exclusions

### 9. Salesforce CPQ/Revenue Cloud Boundaries

**Bounding Statements:**
- "CPQ product catalog: maximum [number] products"
- "Price rules: limited to [number] active rules"
- "Quote templates: [number] templates included"
- "Approval processes: maximum [number] approval steps"
- "Advanced approvals and contracted pricing excluded"

**Risk Mitigation:**
- Manages CPQ complexity
- Establishes pricing rule boundaries
- Clarifies approval workflow scope
- Protects against performance issues

### 10. Salesforce Communities/Experience Cloud

**Bounding Statements:**
- "Community template: [specific template] (e.g., Customer Service)"
- "Community users: maximum [number] members"
- "Custom branding: logo and colors only; full rebrand excluded"
- "Community pages: maximum [number] custom pages"
- "External integrations from community: excluded"

**Risk Mitigation:**
- Establishes community platform boundaries
- Manages user licensing costs
- Clarifies customization scope
- Protects against community complexity

### 11. Environment and Release Management Boundaries

**Bounding Statements:**
- "Environments: [developer / QA / UAT / production] only; extra sandboxes client responsibility"
- "Deployment tooling: [Change Sets / DevOps Center / Copado] only"
- "Release cadence: [number] planned releases per phase"
- "Hotfix process: emergency fixes only; backlog reprioritization excluded"
- "Parallel release trains across multiple orgs: excluded unless explicitly scoped"

**Risk Mitigation:**
- Clarifies release-management model
- Limits environment sprawl
- Protects against multi-org deployment complexity
- Establishes tooling assumptions early
- Bounds hotfix and release overhead

### 12. Managed Package and ISV Dependency Boundaries

**Bounding Statements:**
- "Managed packages: [specific packages] only"
- "ISV configuration limited to standard documented capabilities"
- "Custom extensions to third-party packages: excluded"
- "Package licensing and vendor support: client responsibility"
- "Vendor defect remediation beyond configuration workaround: excluded"

**Risk Mitigation:**
- Prevents third-party dependency sprawl
- Clarifies vendor responsibility split
- Limits unpriced package customization
- Protects against inherited vendor defects
- Establishes configuration-only boundary

### 13. Org Remediation and Technical Debt Boundaries

**Bounding Statements:**
- "Pre-existing automation conflicts remediated only where directly blocking scoped functionality"
- "Legacy cleanup: limited to [specific objects/processes]"
- "Data-quality remediation: excluded beyond agreed migration cleansing rules"
- "Unused configuration rationalization: excluded"
- "Org-wide architecture refactor: excluded unless separately scoped"

**Risk Mitigation:**
- Prevents discovery of technical debt from expanding the programme
- Clarifies what remediation is and is not included
- Protects estimate from inherited-org problems
- Keeps focus on scoped outcomes
- Separates transformation from cleanup

### 14. Support, Hypercare, and Admin Boundary Conditions

**Bounding Statements:**
- "Hypercare period: [number] weeks post-go-live"
- "Admin support: incident triage and scoped defect fixes only"
- "Business-as-usual admin backlog: excluded"
- "Report/dashboard changes after sign-off: change request required"
- "Managed Salesforce AMS service: excluded unless explicitly scoped"

**Risk Mitigation:**
- Prevents hidden BAU support obligations
- Clarifies post-go-live support depth
- Limits backlog creep after acceptance
- Distinguishes project delivery from AMS
- Defines supportable change boundaries

---

## Salesforce-Specific Risk Scenarios

### Governor Limits Protection
**Scenario:** Client wants unlimited automation
**Bounded Response:** "Solution designed to operate within 70% of Salesforce governor limits (SOQL queries, DML statements, CPU time). Exceeding these thresholds requires architecture review and potential re-design."

### Edition Limitations
**Scenario:** Client on Professional Edition wants Enterprise features
**Bounded Response:** "Proposed solution requires Salesforce Enterprise Edition for: workflow rules, approval processes, API access. Professional Edition implementation requires alternative approach with reduced functionality."

### Customization vs. Configuration
**Scenario:** Client wants extensive custom development
**Bounded Response:** "Solution prioritizes declarative configuration (80%) over custom code (20%). Custom Apex/LWC development limited to: [specific use cases]. Additional custom development requires separate SOW."

---

## Salesforce Project Estimation Impact

Proper Salesforce scope bounding reduces estimates by:
- **Data Model Complexity:** 25-35% reduction (clear object/field limits)
- **Automation Scope:** 30-40% reduction (defined automation boundaries)
- **Integration Effort:** 20-30% reduction (specific integration approach)
- **Testing Effort:** 15-25% reduction (clear test coverage requirements)
- **Overall Salesforce Project:** 20-30% reduction in total estimate
