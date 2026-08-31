# Technical Design Authority Review Framework

This framework provides the structured evaluation criteria for conducting comprehensive TDA reviews of solution architectures. It is organised into seven core assessment areas, each containing specific evaluation questions.

## 1. Requirements Alignment & Traceability

Assess how comprehensively the proposed solution architecture maps to each functional and non-functional requirement, identifying requirements gaps, overlaps, or technical debt implications.

**Key evaluation areas:**
- Requirements inventory (FRs and NFRs) with categorisation and prioritisation
- Requirements Traceability Matrix (RTM) coverage
- Gap analysis identifying missing architectural components
- NFR critical path addressing performance, scalability, availability, security, and maintainability
- Implicit requirements (regulatory compliance, data residency, audit trails, disaster recovery)
- Over-engineering assessment versus legitimate future-proofing
- Technical debt quantification with remediation roadmap
- Stakeholder view alignment across different groups
- Constraint impact analysis on requirement de-scoping
- Requirements overlap and conflict resolution
- Testability and acceptance criteria
- Operational readiness requirements
- Integration requirements (interfaces, data contracts, SLAs)
- Requirements change impact and change control process
- Enabler requirements (infrastructure, security frameworks, CI/CD)

## 2. Resource Capability Assessment

Evaluate whether the proposed resource plan demonstrates sufficient depth in critical technical skills and identify capability gaps or single points of failure.

**Key evaluation areas:**
- Technical skill requirements by architectural domain with proficiency levels
- Resource mapping to critical capabilities with certification evidence
- Single points of failure identification
- Technology stack experience (specific versus generic)
- Critical skill intersection competencies
- Senior/lead architect to mid/junior resource ratio
- Experience delivering comparable complexity and scale
- Knowledge transfer and documentation strategy
- On-call and support model alignment to resource availability
- Vendor relationship management capabilities
- Third-party assessment and governance skills

## 3. Scalability, Performance & Resilience

Assess whether the architecture adequately addresses scalability requirements, performance targets, and resilience patterns including failure handling.

**Key evaluation areas:**
- Horizontal and vertical scaling patterns with load thresholds
- Performance testing results against SLAs
- Bottleneck identification and mitigation plans
- Caching strategy (CDN, application, database levels)
- Resilience patterns (circuit breakers, bulkheads, retries, timeouts, graceful degradation)
- Load balancing and auto-scaling configuration
- Database performance optimisation (indexing, query patterns, sharding)
- Network latency and bandwidth considerations
- Resource contention handling (CPU, memory, I/O)
- Failover mechanisms and health check implementation
- Capacity planning with growth projections
- Performance monitoring and alerting thresholds
- Chaos engineering validation

## 4. Security Architecture & Compliance

Evaluate the comprehensive security controls including authentication, authorisation, encryption, data protection, and regulatory compliance.

**Key evaluation areas:**
- Authentication and authorisation mechanisms (IAM, SSO, MFA, RBAC)
- Data encryption (in transit, at rest, key management)
- Network security (firewalls, segmentation, VPCs, WAF)
- API security (rate limiting, input validation, threat protection)
- Secrets management and credential rotation
- Vulnerability management and patching strategy
- Security monitoring and incident response (SIEM integration)
- Compliance requirements (GDPR, HIPAA, PCI-DSS, SOC 2)
- Data classification and handling procedures
- Audit logging and tamper-proof retention
- Third-party security assessments (penetration testing, vulnerability scanning)
- Supply chain security (dependencies, container images)
- Security by design principles implementation
- Least privilege access controls
- Security operations integration

## 5. Integration & Dependency Management

Assess the complexity, risk, and resilience of external system integrations, including API contracts and error handling.

**Key evaluation areas:**
- Complete integration endpoint inventory with versions and limitations
- Integration pattern justification (synchronous, asynchronous, batch, event-driven)
- API contracts and data schemas with versioning strategy
- Error handling and resilience patterns (circuit breakers, retries, timeouts, dead letter queues)
- Fallback and degradation strategies with maximum tolerable downtime
- Authentication, authorisation, and data security across integrations
- Testing and monitoring strategy (contract testing, synthetic monitoring, SLA tracking)

## 6. Operational Readiness & Supportability

Evaluate the observability capabilities, disaster recovery design, operational runbooks, and support model alignment.

**Key evaluation areas:**
- Observability capabilities (logging, metrics, tracing, alerting)
- Monitoring and alerting alignment with existing platforms
- RTO and RPO targets with disaster recovery design
- Operational runbooks and incident response playbooks
- Support model definition (L1/L2/L3, escalation, on-call, RACI)
- Organisational operational maturity assessment
- Specialised knowledge dependencies and knowledge transfer
- Supportability NFRs (diagnostic capabilities, administrative interfaces)
- Operational metrics and KPIs with feedback loops
- Security operations integration (SIEM, vulnerability management)
- Operational data growth management
- Capacity management and performance tuning procedures
- Operational testing (chaos engineering, DR drills, failover testing)
- Multi-environment operational visibility
- Contractual and organisational dependencies on operational effectiveness

## 7. Technology Risk & Vendor Lock-in

Evaluate risks associated with technology choices including maturity, vendor dependencies, licensing constraints, and skills availability.

**Key evaluation areas:**
- Technology maturity assessment (emerging, growing, mature, declining)
- Vendor dependency analysis with lock-in cost and complexity
- Licensing and commercial risk (cost scaling, restrictive clauses)
- Skills availability and knowledge transfer requirements
- Migration and exit strategy documentation
- Technology obsolescence risk and modernisation roadmap
- Integration and interoperability standards adherence
