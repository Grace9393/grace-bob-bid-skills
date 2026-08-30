# IBM Bid Management Workflows

Detailed step-by-step workflows for common bid scenarios. Each workflow shows the complete sequence of skills to use, their inputs/outputs, and rationale for multi-skill orchestration.

## Workflow 1: Simple Bid (< £1M, No Solution Architecture Required)

### Scenario
- Commercial bid for professional services or managed services
- Value < £1M
- No complex technical solution architecture required
- Straightforward question/answer format

### Complete Sequence

**Phase 0: Opportunity Assessment (30 minutes)**

**Step 0: Requirements Extraction (Optional - run first if needed)**
0. **ibm-bid-requirements-extractor**
   - Input: RFP.pdf or requirements spreadsheet (XLSX/CSV/TSV)
   - Output: ../tmp/ibm-bid-requirements-extractor.md
   - Use when: Requirements are in spreadsheets or you need a checklist before analysis
   - Duration: 10 minutes

**Step 1: Requirements Analysis (Sequential - run next, after Step 0 if used)**
1. **ibm-bid-requirements-analysis**
   - Input: RFP.pdf
   - Output: ../tmp/ibm-bid-requirements-analysis.md
   - Extract: Client profile, requirements (5), operational gaps, capability deficits, risk profile, competitive landscape
   - Duration: 15 minutes

**Step 2: Strategic & Qualification (Parallel - run after Step 1)**
2. **ibm-bid-strategic-positioning**
   - Input: ../tmp/ibm-bid-requirements-analysis.md
   - Output: ../tmp/ibm-bid-strategic-positioning.md
   - Analyze: Executive decision drivers, sales strategy selection, price-to-win (5 viewpoints)
   - Duration: 10 minutes

3. **ibm-bid-competitor-analysis** (Parallel with #2)
   - Input: ../tmp/ibm-bid-requirements-analysis.md + optional ../tmp/ibm-bid-strategic-positioning.md
   - Output: ../tmp/ibm-bid-competitor-analysis.md
   - Analyze: Likely bidder set, incumbent threat, attack lines on IBM, counter-positioning
   - Duration: 20-30 minutes

4. **ibm-bid-qualification** (Parallel with #2 and #3)
   - Input: RFP.pdf + ../tmp/ibm-bid-requirements-analysis.md
   - Output: ../tmp/ibm-bid-qualification.md
   - Score: 20 criteria across 7 categories
   - Decision: GO if ≥60, NO-GO if <60
   - Duration: 15 minutes

**Quality Gate 1: GO/NO-GO Decision**
- Review qualification score
- If score <60: Document no-bid and exit
- If score ≥60: Proceed to Phase 1

**Phase 1: Strategic Positioning (30 minutes)**
4. **ibm-bid-win-themes**
   - Input: ../tmp/ibm-bid-requirements-analysis.md + ../tmp/ibm-bid-strategic-positioning.md + ../tmp/ibm-bid-competitor-analysis.md + ibm-bid-strategy-and-capabilities-2026
   - Output: ../tmp/ibm-bid-win-themes.md
   - Generate: 3-5 Shipley-compliant win themes
   - Duration: 20 minutes

5. **ibm-bid-executive-summary** (If required by RFP)
   - Input: ../tmp/ibm-bid-requirements-analysis.md + ../tmp/ibm-bid-strategic-positioning.md + ../tmp/ibm-bid-win-themes.md
   - Output: ../tmp/ibm-bid-executive-summary.md
   - Generate: 1000-word executive summary (4-part structure)
   - Duration: 30 minutes
   - Skip if: RFP doesn't require executive summary

**Phase 2: Solution Architecture**
- SKIP for simple bids - no complex technical solution required

**Commercial Modelling (Optional but recommended if pricing is evaluated)**
6. **ibm-bid-pricing-strategy**
   - Input: ../tmp/ibm-bid-strategic-positioning.md + RFP pricing requirements
   - Output: pricing strategy, assumptions, concessions, and negotiation guardrails
   - Use when: Pricing schedule, discount, value-based model, or commercial narrative is required
   - Duration: 30-60 minutes

**Phase 3: Content Development (2-4 hours depending on question count)**
7. **ibm-bid-writer** (Iterate for each question)
   - Input: RFP question + ../tmp/ibm-bid-win-themes.md + optional ../tmp/ibm-bid-competitor-analysis.md + ibm-bid-library + ibm-bid-customer-stories
   - Output: ../tmp/ibm-bid-responses/Q01_[topic].md, Q02_[topic].md, etc.
   - Search ibm-bid-library for similar historical responses (FTS5 search)
   - Search ibm-bid-customer-stories for relevant proof points
   - Draft response following best practices
   - Duration: 20-40 minutes per question

8. **ibm-bid-answer-evaluator** (After each response)
   - Input: Question + ../tmp/ibm-bid-responses/Q0X_[topic].md
   - Output: Score (0-5) + feedback in ../tmp/ibm-bid-responses/evaluation_report.md
   - Criteria: Understanding (0-5), evidence (0-5), structure (0-5), clarity (0-5), differentiation (0-5)
   - If score <3: Return to ibm-bid-writer with feedback
   - If score ≥3: Proceed to next question
   - Duration: 10 minutes per question

**Phase 4: Technical Assurance (30 minutes)**
9. **Final ibm-bid-answer-evaluator pass**
   - Input: All responses in ../tmp/ibm-bid-responses/
   - Output: Comprehensive evaluation report
   - Validate: Consistency across responses, no contradictions, quality threshold met
   - Duration: 30 minutes

**Quality Gate 2: Submission Readiness**
- Review evaluation report
- Confirm all scores ≥3
- Address any failing responses
- Final submission decision

### Total Duration Estimate
- Phase 0: 30 minutes
- Phase 1: 30-60 minutes (depending on executive summary requirement)
- Phase 3: 2-4 hours (depending on question count)
- Phase 4: 30 minutes
- **Total: 3.5-6 hours**

### Rationale for Multi-Skill Approach
- **ibm-bid-qualification prevents wasted effort** on low-probability bids
- **ibm-bid-competitor-analysis exposes attack lines early** so IBM can differentiate before drafting
- **ibm-bid-win-themes provides strategic consistency** across all responses
- **ibm-bid-library search reduces drafting time** by reusing historical content
- **ibm-bid-answer-evaluator ensures quality** before submission
- **Iterative writer/evaluator loop** improves response quality systematically

---

## Workflow 2: Complex Government Salesforce Bid (Full Sequence)

### Scenario
- UK government procurement for Salesforce implementation
- Value £10M-£50M
- Complex technical solution architecture required
- Ongoing Application Management Services (AMS) required
- High compliance requirements (G-Cloud, Cyber Essentials Plus)
- Oral presentation required

### Complete Sequence

**Phase 0: Opportunity Assessment (1 hour)**

**Step 0: Requirements Extraction (Optional - run first if needed)**
0. **ibm-bid-requirements-extractor**
   - Input: ITT.pdf or requirements spreadsheet (XLSX/CSV/TSV)
   - Output: ../tmp/ibm-bid-requirements-extractor.md
   - Use when: Requirements are in spreadsheets or you need a checklist before analysis
   - Duration: 10 minutes

**Step 1: Requirements Analysis (Sequential - run next, after Step 0 if used)**
1. **ibm-bid-requirements-analysis**
   - Input: ITT.pdf (UK government tender document)
   - Output: ../tmp/ibm-bid-requirements-analysis.md
   - Extract: Client profile, requirements (10+), operational gaps, capability deficits, risk profile, competitive landscape
   - Government-specific: Identify compliance requirements, framework terms, sector patterns
   - Duration: 30 minutes

**Step 2: Strategic & Qualification (Parallel - run after Step 1)**
2. **ibm-bid-strategic-positioning**
   - Input: ../tmp/ibm-bid-requirements-analysis.md
   - Output: ../tmp/ibm-bid-strategic-positioning.md
   - Analyze: Executive decision drivers, transformation vs BAU, sales strategy, price-to-win (5 viewpoints)
   - Government-specific: Public sector decision drivers, social value positioning
   - Duration: 20 minutes

3. **ibm-bid-competitor-analysis** (Parallel with #2)
   - Input: ../tmp/ibm-bid-requirements-analysis.md + optional public-source research
   - Output: ../tmp/ibm-bid-competitor-analysis.md
   - Analyze: likely bidders, incumbent defence patterns, public-sector credibility signals, attack lines on IBM
   - Duration: 30 minutes

4. **ibm-bid-clarifications** (Parallel with #2 and #3)
   - Input: ITT.pdf + ../tmp/ibm-bid-requirements-analysis.md
   - Output: ../tmp/ibm-bid-clarifications.md
   - Identify: Ambiguous requirements, missing details, contradictions
   - Generate: 10-20 clarification questions for client
   - Track: Previously raised questions to avoid duplication
   - Duration: 20 minutes

5. **ibm-bid-qualification** (Parallel with #2, #3 and #4)
   - Input: ITT.pdf + ../tmp/ibm-bid-requirements-analysis.md + ../tmp/ibm-bid-strategic-positioning.md
   - Output: ../tmp/ibm-bid-qualification.md
   - Score: 20 criteria (client maturity, justification, momentum, relationships, reputation, differentiators, commercial)
   - Red flags: Budget alignment, resource capability, competitive position
   - Duration: 30 minutes

**Quality Gate 1: GO/NO-GO Decision**
- Review qualification score (target: ≥70 for government bids)
- Assess red flags (any HIGH risks require mitigation plan)
- Review clarifications (major gaps may indicate hidden risks)
- Decision: GO / Conditional GO / NO-GO

**Phase 1: Strategic Positioning (2 hours)**
5. **ibm-bid-win-themes**
   - Input: ../tmp/ibm-bid-requirements-analysis.md + ../tmp/ibm-bid-strategic-positioning.md + ../tmp/ibm-bid-competitor-analysis.md + ibm-bid-strategy-and-capabilities-2026 + ibm-bid-customer-stories
   - Output: ../tmp/ibm-bid-win-themes.md
   - Generate: 5-7 Shipley-compliant win themes
   - Government focus: Public sector experience, security clearances, compliance
   - Search ibm-bid-customer-stories for UK government proof points
   - Duration: 60 minutes

6. **ibm-bid-executive-summary**
   - Input: ../tmp/ibm-bid-requirements-analysis.md + ../tmp/ibm-bid-strategic-positioning.md + ../tmp/ibm-bid-win-themes.md + ibm-bid-customer-stories
   - Output: ../tmp/ibm-bid-executive-summary.md
   - Generate: 1000-word executive summary (4-part structure)
   - Incorporate: Win themes, customer success stories, IBM differentiators
   - Government tone: Formal, compliance-focused, evidence-based
   - Duration: 60 minutes

**Phase 2: Solution Architecture (4-6 hours)**
7. **ibm-sf-solution-architect**
   - Input: ../tmp/ibm-bid-requirements-analysis.md + requirements from ITT + ibm-sf-help + ibm-sf-architect
   - Output: ../tmp/ibm-sf-solution/complete_solution.md (16 sections)
   - Generate: Complete Salesforce solution architecture document
   - Sections: Executive summary, business context, user stories, architecture, data model, security, integrations, deployment, training, change management, testing, go-live, success metrics, risks, timeline, cost breakdown
   - Validate: Search ibm-sf-help for feature availability
   - Reference: ibm-sf-architect for architecture patterns
   - Support incremental generation: Can build sections iteratively
   - Duration: 4-6 hours

7. **ibm-sf-ams**
   - Input: ../tmp/ibm-sf-solution/complete_solution.md + user counts + complexity assessment
   - Output: ../tmp/ibm-sf-ams-estimation.md
   - Calculate: FTE requirements for Application Management Services
   - Models: Ticket-based or user-based estimation
   - Include: Incident management, service requests, minor enhancements, non-ticketing activities
   - Factor: IBM GenAI accelerators (15-25% productivity gain)
   - Multi-year: Staffing projections for 3-5 year term
   - Duration: 60 minutes

8. **ibm-bid-staffing-planner** (If delivery staffing or GP baseline is needed)
   - Input: Solution scope, workload/DCUT hours, project complexity, contract type, target duration, location mix
   - Output: ../tmp/ibm-bid-staffing-planner.md plus optional resource plan CSV
   - Calculate: Team shape, duration, cost, price, GP, GP%, and location-mix scenarios
   - Duration: 30-90 minutes

9. **ibm-bid-pricing-strategy**
   - Input: ../tmp/ibm-bid-staffing-planner.md + ../tmp/ibm-bid-strategic-positioning.md + pricing schedules/commercial terms
   - Output: Pricing strategy, value-based commercial model, TCO/margin scenarios, concessions, and negotiation guardrails
   - Use when: Pricing is evaluated, value-based contracting is possible, discounts/concessions are likely, or commercial narrative is required
   - Duration: 45-90 minutes

**Phase 3: Content Development (8-12 hours depending on question count)**
10. **ibm-bid-writer** (Iterate for 15-30 questions)
   - Input: ITT question + ../tmp/ibm-bid-win-themes.md + optional ../tmp/ibm-bid-competitor-analysis.md + ../tmp/ibm-sf-solution/complete_solution.md + ibm-bid-library + ibm-bid-customer-stories
   - Output: ../tmp/ibm-bid-responses/Q01_[topic].md, Q02_[topic].md, etc.
   - Search ibm-bid-library: "Salesforce government implementation" (FTS5 search)
   - Search ibm-bid-customer-stories: "government Sales Cloud" or similar
   - Reference: Solution architecture for technical responses
   - Incorporate: Win themes in all responses for consistency
   - Government compliance: Address security, accessibility, data protection
   - Duration: 30-45 minutes per question

11. **ibm-bid-answer-evaluator** (After each response)
   - Input: Question + ../tmp/ibm-bid-responses/Q0X_[topic].md
   - Output: Score (0-5) + feedback in ../tmp/ibm-bid-responses/evaluation_report.md
   - Criteria: Understanding (0-5), evidence (0-5), structure (0-5), clarity (0-5), differentiation (0-5)
   - Government standards: Higher bar for evidence and compliance
   - If score <3: Return to ibm-bid-writer with detailed feedback
   - If score ≥3: Proceed to next question
   - Duration: 10-15 minutes per question

**Phase 4: Technical Assurance (2-3 hours)**
12. **ibm-bid-tda-review**
    - Input: ../tmp/ibm-sf-solution/complete_solution.md + all responses in ../tmp/ibm-bid-responses/
    - Output: ../tmp/ibm-bid-tda-review.md
    - Perspective: IBM Lead Enterprise Architect with 10+ years experience
    - Evaluate: Requirements alignment, resource capability, scalability, security, integration complexity, operational readiness, technology risk
    - Risk rating: LOW / MEDIUM / HIGH for each dimension
    - Recommendations: Specific actions to mitigate identified risks
    - Duration: 90-120 minutes

13. **Final ibm-bid-answer-evaluator pass**
    - Input: All responses in ../tmp/ibm-bid-responses/
    - Output: Comprehensive evaluation report in ../tmp/ibm-bid-final-evaluation.md
    - Validate: Consistency across responses, alignment with solution architecture, no contradictions, no fabricated information
    - Government focus: Compliance completeness, security adequacy
    - Duration: 60 minutes

**Quality Gate 2: Technical Assurance**
- Review TDA risk rating (all dimensions should be LOW or MEDIUM)
- Review final evaluation scores (all ≥3, ideally ≥4 for government)
- Address any HIGH risks (escalate or no-bid)
- Address any failing responses (score <3)
- Final submission decision

**Oral Presentation Preparation (If Required - 4-6 hours additional)**
14. **ibm-story-pitch-development**
    - Input: ../tmp/ibm-bid-win-themes.md + ../tmp/ibm-bid-executive-summary.md
    - Output: ../tmp/oral-presentation-pitch.md
    - Structure: Business pitch for oral presentation
    - Duration: 90 minutes

15. **ibm-story-stakeholder-mapping**
    - Input: Evaluator panel composition
    - Output: ../tmp/stakeholder-map.md
    - Map: Decision-makers and their priorities
    - Duration: 30 minutes

16. **ibm-story-presentation-structuring**
    - Input: ../tmp/oral-presentation-pitch.md + time limit
    - Output: ../tmp/presentation-structure.md
    - Choose: Architecture (Problem-Solution, Pixar, etc.)
    - Duration: 60 minutes

17. **ibm-story-visual-narrative**
    - Input: ../tmp/presentation-structure.md
    - Output: Slide deck in ../outputs/
    - Design: Slides supporting narrative
    - Duration: 2-3 hours

18. **ibm-story-speaker-performance**
    - Input: Final slide deck + presenter list
    - Output: ../tmp/speaker-performance-guide.md
    - Guide: Delivery mechanics (voice, body, presence)
    - Duration: 60 minutes

### Total Duration Estimate
- Phase 0: 1 hour
- Phase 1: 2 hours
- Phase 2: 5-7 hours
- Phase 3: 12-18 hours (15-30 questions)
- Phase 4: 2-3 hours
- Oral presentation (optional): 4-6 hours
- **Total: 22-31 hours (26-37 hours with oral presentation)**

### Rationale for Multi-Skill Approach
- **Government bids require comprehensive analysis** across all dimensions
- **Clarifications reduce risk** of misinterpreting requirements
- **Qualification prevents wasted effort** on unwinnable opportunities
- **Competitor analysis sharpens differentiation** before 15-30 answers are written
- **Win themes provide strategic consistency** across 15-30 responses
- **Solution architecture informs technical responses** and ensures feasibility
- **AMS and staffing estimates demonstrate operational planning** and realistic support/commercial models
- **Pricing strategy protects margin** and translates cost baseline into value-based, negotiation-ready commercial narrative
- **TDA review catches architectural flaws** before submission
- **Iterative evaluation ensures quality** meets government standards
- **Story skills enable compelling oral presentation** differentiation

---

## Workflow 3: Framework Agreement Response

### Scenario
- UK government framework agreement (G-Cloud, DOS, CCS framework)
- Pre-qualified supplier responding to call-off
- Simplified procurement process
- Focus on capability statements and case studies
- No complex solution architecture required

### Complete Sequence

**Phase 0: Opportunity Assessment (30 minutes)**

**Step 0: Requirements Extraction (Optional - run first if needed)**
0. **ibm-bid-requirements-extractor**
   - Input: Call-off specification (PDF/DOCX) or requirements spreadsheet (XLSX/CSV/TSV)
   - Output: ../tmp/ibm-bid-requirements-extractor.md
   - Use when: Requirements are in spreadsheets or you need a checklist before analysis
   - Duration: 10 minutes

**Step 1: Requirements Analysis**
1. **ibm-bid-requirements-analysis**
   - Input: Call-off specification
   - Output: ../tmp/ibm-bid-requirements-analysis.md
   - Extract: Client profile, requirements (5-8), needs, gaps
   - Framework context: Reference framework terms and pricing
   - Duration: 15 minutes

**Step 2: Strategic & Qualification (Parallel)**
2. **ibm-bid-strategic-positioning**
   - Input: ../tmp/ibm-bid-requirements-analysis.md
   - Output: ../tmp/ibm-bid-strategic-positioning.md
   - Analyze: Strategic approach, price-to-win positioning
   - Framework context: Framework pricing constraints
   - Duration: 10 minutes

3. **ibm-bid-competitor-analysis**
   - Input: ../tmp/ibm-bid-requirements-analysis.md
   - Output: ../tmp/ibm-bid-competitor-analysis.md
   - Analyze: likely framework competitors, incumbent and relationship advantage, case-study attack lines
   - Duration: 20 minutes

4. **ibm-bid-qualification**
   - Input: Call-off spec + ../tmp/ibm-bid-requirements-analysis.md
   - Output: ../tmp/ibm-bid-qualification.md
   - Score: 20 criteria (relationships weigh heavily for call-offs)
   - Framework advantage: Simplified procurement reduces some risks
   - Duration: 15 minutes

**Quality Gate 1: GO/NO-GO Decision**
- Framework call-offs typically lower barrier
- Score ≥50 may be acceptable if relationship is strong

**Phase 1: Strategic Positioning (1 hour)**
4. **ibm-bid-win-themes**
   - Input: ../tmp/ibm-bid-requirements-analysis.md + ../tmp/ibm-bid-strategic-positioning.md + ../tmp/ibm-bid-competitor-analysis.md + ibm-bid-strategy-and-capabilities-2026
   - Output: ../tmp/ibm-bid-win-themes.md
   - Generate: 3-4 win themes
   - Framework focus: Emphasize framework compliance, ease of procurement
   - Duration: 45 minutes

5. **ibm-bid-executive-summary** (Optional)
   - May be required depending on call-off size
   - Duration: 30-60 minutes
   - Skip if: Call-off is small (<£500K) or doesn't require summary

**Phase 2: Solution Architecture**
- SKIP for framework call-offs unless explicitly required
- Most call-offs focus on capability statements, not detailed design

**Phase 3: Content Development (3-6 hours)**
6. **ibm-bid-writer** (Focus on capability statements and case studies)
   - Input: Call-off questions + ../tmp/ibm-bid-win-themes.md + ibm-bid-library + ibm-bid-customer-stories
   - Output: ../tmp/ibm-bid-responses/Q01_capability.md, Q02_case_study.md, etc.
   - Search ibm-bid-library: "framework" OR "G-Cloud" OR "DOS"
   - Search ibm-bid-customer-stories: Filter by relevant industry/technology
   - Framework format: Often requires specific case study template
   - Duration: 20-30 minutes per response (simpler than full bids)

7. **ibm-bid-answer-evaluator** (After each response)
   - Input: Question + ../tmp/ibm-bid-responses/Q0X_[topic].md
   - Output: Score (0-5) + feedback
   - Framework standards: Still require evidence and clarity
   - If score <3: Return to ibm-bid-writer
   - Duration: 10 minutes per response

**Phase 4: Technical Assurance (30 minutes)**
7. **Final ibm-bid-answer-evaluator pass**
   - Input: All responses
   - Output: ../tmp/ibm-bid-final-evaluation.md
   - Framework focus: Compliance with framework terms, consistent capability claims
   - Duration: 30 minutes

**Quality Gate 2: Submission Readiness**
- Review evaluation report
- Confirm framework compliance
- Final submission decision

### Total Duration Estimate
- Phase 0: 30 minutes
- Phase 1: 45-90 minutes
- Phase 3: 3-6 hours
- Phase 4: 30 minutes
- **Total: 5-8 hours**

### Rationale for Multi-Skill Approach
- **Framework call-offs are faster but still competitive**
- **Win themes ensure differentiation** even in simplified process
- **Competitor analysis prevents generic framework positioning** and exposes relationship threats
- **Library search leverages previous framework responses**
- **Customer stories provide required proof points** efficiently
- **Evaluation ensures quality** meets framework standards

---

## Workflow 4: Rebid Using Historical Content

### Scenario
- Re-bidding previous opportunity (lost or expired contract)
- IBM has bid this client/solution before
- Extensive historical content available in ibm-bid-library
- Need to refresh positioning and update responses

### Complete Sequence

**Phase 0: Opportunity Assessment + Historical Search (1 hour)**

**Step 1: Requirements Analysis + Historical Search**
0. **ibm-bid-requirements-extractor** (Optional)
   - Input: New RFP.pdf or requirements spreadsheet (XLSX/CSV/TSV)
   - Output: ../tmp/ibm-bid-requirements-extractor.md
   - Use when: Requirements are in spreadsheets or you need a checklist before analysis
   - Duration: 10 minutes

1. **ibm-bid-requirements-analysis**
   - Input: New RFP.pdf
   - Output: ../tmp/ibm-bid-requirements-analysis.md
   - Compare: Previous bid analysis (if available)
   - Identify: Changes in requirements, client priorities, competitive landscape
   - Duration: 25 minutes

2. **Search ibm-bid-library for historical responses**
   - Search: Client name OR previous opportunity name
   - Review: Previous bid responses, solution architecture, win themes
   - Extract: Reusable content, client insights, lessons learned
   - Document: Available historical artifacts
   - Duration: 20 minutes

**Step 2: Strategic & Qualification (Parallel)**
3. **ibm-bid-strategic-positioning**
   - Input: ../tmp/ibm-bid-requirements-analysis.md + historical bid analysis
   - Output: ../tmp/ibm-bid-strategic-positioning.md
   - Analyze: Updated price-to-win, strategic approach refresh
   - Compare: What changed in competitive landscape since last bid
   - Duration: 15 minutes

4. **ibm-bid-qualification**
   - Input: New RFP + ../tmp/ibm-bid-requirements-analysis.md + historical bid outcome
   - Output: ../tmp/ibm-bid-qualification.md
   - Score: 20 criteria
   - Lessons learned: Why did we lose previously? What changed?
   - Decision: Higher bar for rebids - should score ≥70 to proceed
   - Duration: 20 minutes

**Quality Gate 1: GO/NO-GO Decision**
- Review why previous bid lost
- Confirm changes address previous weaknesses
- Higher scrutiny for rebids

**Phase 1: Strategic Positioning (1.5 hours)**
5. **ibm-bid-win-themes** (Refresh positioning)
   - Input: ../tmp/ibm-bid-requirements-analysis.md + ../tmp/ibm-bid-strategic-positioning.md + historical win themes + competitive intel on why we lost
   - Output: ../tmp/ibm-bid-win-themes.md (UPDATED)
   - Refresh: Update themes to address previous weaknesses
   - New angle: What's changed since last bid? New capabilities, customer stories, market position
   - Duration: 60 minutes

6. **ibm-bid-executive-summary** (If required)
   - Input: ../tmp/ibm-bid-requirements-analysis.md + ../tmp/ibm-bid-strategic-positioning.md + updated win themes + new customer stories since last bid
   - Output: ../tmp/ibm-bid-executive-summary.md (UPDATED)
   - Emphasize: What's different this time
   - Duration: 45 minutes

**Phase 2: Solution Architecture (Variable - 1-4 hours)**
7. **Update solution architecture** (If technical requirements changed)
   - Review historical solution architecture
   - Identify: Changes in requirements
   - Update: Only sections that need refresh
   - Duration: 1-4 hours (depending on scope of changes)
   - Skip: If requirements substantially unchanged

**Phase 3: Content Development (4-8 hours - faster due to historical content)**
8. **ibm-bid-writer** (Adapt historical responses)
   - Input: RFP question + historical response + ../tmp/ibm-bid-win-themes.md (updated)
   - Output: ../tmp/ibm-bid-responses/Q0X_[topic].md (ADAPTED)
   - Process:
     1. Retrieve historical response from ibm-bid-library
     2. Review for relevance and currency
     3. Update with new win themes
     4. Update with recent customer stories
     5. Update with new IBM capabilities (2026 strategy)
     6. Refresh evidence and examples
   - Faster: 50-70% of content may be reusable with updates
   - Duration: 15-30 minutes per question (vs. 30-45 for new responses)

8. **ibm-bid-answer-evaluator** (After each adapted response)
   - Input: Question + ../tmp/ibm-bid-responses/Q0X_[topic].md
   - Output: Score + feedback
   - Focus: Currency of examples, alignment with updated win themes, competitive differentiation
   - If score <3: Revise (may need more substantial rewrite)
   - Duration: 10 minutes per response

**Phase 4: Technical Assurance (1.5 hours)**
9. **ibm-bid-tda-review** (If solution architecture changed)
   - Input: Updated solution architecture
   - Output: ../tmp/ibm-bid-tda-review.md
   - Focus: Changes since last bid, new risks
   - Duration: 60 minutes

10. **Final ibm-bid-answer-evaluator pass**
    - Input: All adapted responses
    - Output: ../tmp/ibm-bid-final-evaluation.md
    - Validate: No outdated information, consistent updated messaging, competitive differentiation
    - Duration: 30 minutes

**Quality Gate 2: Submission Readiness**
- Confirm all references are current
- Validate competitive differentiation vs. last bid
- Final submission decision

### Total Duration Estimate
- Phase 0: 1 hour (including historical search)
- Phase 1: 1.5 hours
- Phase 2: 1-4 hours (variable)
- Phase 3: 4-8 hours (50% faster due to historical content)
- Phase 4: 1.5 hours
- **Total: 9-16 hours (vs. 22-31 hours for new complex bid)**

### Rationale for Multi-Skill Approach
- **Historical content provides 50-70% head start** but needs updating
- **Updated win themes address previous weaknesses** competitively
- **Evaluation ensures historical content is current** and competitive
- **TDA review catches architectural drift** if requirements changed
- **Faster than new bid but maintains quality** standards

---

## Workflow 5: Multi-Lot Procurement

### Scenario
- Government or large commercial procurement with multiple lots
- IBM bidding for 3-5 lots (e.g., Lot 1: Implementation, Lot 2: AMS, Lot 3: Training)
- Shared requirements + lot-specific requirements
- Need consistent messaging across lots while addressing specific evaluation criteria per lot

### Complete Sequence

**Phase 0: Opportunity Assessment (1.5 hours - once for all lots)**

**Step 1: Requirements Analysis (Sequential)**
0. **ibm-bid-requirements-extractor** (Optional)
   - Input: Multi-lot ITT.pdf or requirements spreadsheet (XLSX/CSV/TSV)
   - Output: ../tmp/ibm-bid-requirements-extractor.md
   - Use when: Requirements are in spreadsheets or you need a checklist before analysis
   - Duration: 10 minutes

1. **ibm-bid-requirements-analysis** (Comprehensive multi-lot analysis)
   - Input: Multi-lot ITT.pdf
   - Output: ../tmp/ibm-bid-requirements-analysis.md
   - Extract: Shared requirements + lot-specific requirements
   - Structure: Analysis by lot with shared elements identified
   - Duration: 35 minutes

**Step 2: Strategic & Qualification (Parallel)**
2. **ibm-bid-strategic-positioning** (Multi-lot strategic analysis)
   - Input: ../tmp/ibm-bid-requirements-analysis.md
   - Output: ../tmp/ibm-bid-strategic-positioning.md
   - Analyze: Which lots to bid (bid all or subset?), combined pricing strategy
   - Strategic: Cross-lot positioning and dependencies
   - Duration: 25 minutes

3. **ibm-bid-clarifications** (Across all lots)
   - Input: Multi-lot ITT.pdf + ../tmp/ibm-bid-requirements-analysis.md
   - Output: ../tmp/ibm-bid-clarifications.md
   - Identify: Ambiguities in shared requirements and lot-specific requirements
   - Cross-lot: Flag inconsistencies between lot requirements
   - Duration: 30 minutes

4. **ibm-bid-qualification** (Per lot + combined)
   - Input: ITT + ../tmp/ibm-bid-requirements-analysis.md + ../tmp/ibm-bid-strategic-positioning.md
   - Output: ../tmp/ibm-bid-qualification-lot1.md, lot2.md, lot3.md, combined.md
   - Score: Each lot individually (20 criteria per lot)
   - Combined: Overall opportunity score
   - Decision: Which lots to bid (may decline some lots if score <60)
   - Duration: 20 minutes per lot (60 minutes for 3 lots)

**Quality Gate 1: GO/NO-GO Decision (Per Lot)**
- Review each lot qualification score
- Decide: Which lots to bid
- Combined strategy: Bidding multiple lots may increase win probability

**Phase 1: Strategic Positioning (2 hours - shared across lots)**
5. **ibm-bid-win-themes** (Consistent across lots)
   - Input: ../tmp/ibm-bid-requirements-analysis.md + ../tmp/ibm-bid-strategic-positioning.md + ibm-bid-strategy-and-capabilities-2026
   - Output: ../tmp/ibm-bid-win-themes.md (SHARED + lot-specific variants)
   - Generate: 5-7 master win themes applicable across all lots
   - Adapt: Lot-specific variations emphasizing relevant capabilities
   - Consistency: Core messaging must align across all lots
   - Duration: 90 minutes

6. **ibm-bid-executive-summary** (If required per lot or overall)
   - Input: ../tmp/ibm-bid-requirements-analysis.md + ../tmp/ibm-bid-strategic-positioning.md + ../tmp/ibm-bid-win-themes.md
   - Output: ../tmp/ibm-bid-executive-summary-lot1.md, lot2.md, lot3.md, OR combined.md
   - Structure: May require separate summary per lot or combined summary
   - Cross-reference: Lots reference each other to show integrated approach
   - Duration: 45 minutes per summary

**Phase 2: Solution Architecture (Variable by lot - 4-10 hours)**
6. **Solution architecture per lot** (Lot-dependent)
   - Lot 1 (Implementation): ibm-sf-solution-architect or ibm-bid-solution-architect
     - Output: ../tmp/ibm-sf-solution-lot1/complete_solution.md
     - Duration: 4-6 hours
   - Lot 2 (AMS): ibm-sf-ams
     - Output: ../tmp/ibm-sf-ams-lot2-estimate.md
     - Duration: 60 minutes
   - Lot 3 (Training): Lightweight solution approach
     - Output: ../tmp/training-approach-lot3.md
     - Duration: 60 minutes
   - Integration: Ensure solutions integrate across lots (e.g., AMS supports Implementation solution)

**Phase 3: Content Development (12-20 hours depending on lot count and questions)**
7. **ibm-bid-writer** (Per lot, leveraging shared content)
   - Approach:
     1. Draft shared/common responses first (can reuse across lots)
     2. Adapt for lot-specific requirements
     3. Cross-reference between lots to show integrated approach
   - Shared responses (write once, adapt for each lot):
     - Company overview
     - Corporate experience
     - Quality management
     - Governance approach
   - Lot-specific responses:
     - Technical approach (specific to lot)
     - Delivery methodology (adapted per lot scope)
     - Resource plan (specific to lot)
   - Output structure:
     - ../tmp/ibm-bid-responses-lot1/Q01_[topic].md
     - ../tmp/ibm-bid-responses-lot2/Q01_[topic].md
     - ../tmp/ibm-bid-responses-lot3/Q01_[topic].md
   - Duration: 20-40 minutes per unique response (shared responses faster on subsequent lots)

8. **ibm-bid-answer-evaluator** (Per lot)
   - Input: Lot-specific questions + responses
   - Output: ../tmp/ibm-bid-responses-lot1/evaluation_report.md (per lot)
   - Evaluate: Each lot's responses against lot-specific evaluation criteria
   - Consistency check: Shared responses align across lots
   - Duration: 10 minutes per response

**Phase 4: Technical Assurance (2-3 hours)**
9. **ibm-bid-tda-review** (Per lot if complex, or combined)
   - Input: Solution architecture from each lot
   - Output: ../tmp/ibm-bid-tda-review-lot1.md (per lot) OR ../tmp/ibm-bid-tda-review-combined.md
   - Evaluate: Each lot's technical solution + integration across lots
   - Critical: Ensure lots don't contradict each other technically
   - Duration: 60-90 minutes per complex lot

10. **Final ibm-bid-answer-evaluator pass** (Per lot)
    - Input: All responses per lot
    - Output: ../tmp/ibm-bid-final-evaluation-lot1.md (per lot)
    - Validate: Consistency within lot and across lots
    - Cross-lot check: No contradictions in shared responses
    - Duration: 45 minutes per lot

**Quality Gate 2: Technical Assurance (Per Lot)**
- Review each lot's TDA risk rating and evaluation scores
- Confirm cross-lot consistency
- Final submission decision per lot

### Total Duration Estimate (3 Lots)
- Phase 0: 1.5 hours (shared)
- Phase 1: 2 hours (shared)
- Phase 2: 6-8 hours (lot-dependent)
- Phase 3: 12-20 hours (shared responses provide efficiency)
- Phase 4: 3-4 hours (per-lot reviews)
- **Total: 24.5-35.5 hours for 3 lots**

### Efficiency Gains from Multi-Lot Approach
- Shared responses (30-40% of content) written once and adapted
- Shared analysis, qualification, win themes across lots
- **Cost per lot decreases**: First lot ~15 hours, subsequent lots ~8-10 hours each

### Rationale for Multi-Skill Approach
- **Multi-lot procurement requires cross-lot consistency**
- **Qualification per lot enables strategic lot selection**
- **Shared win themes ensure consistent competitive positioning**
- **Separate evaluations per lot** ensure compliance with lot-specific criteria
- **TDA review catches cross-lot integration risks**
- **Efficiency gains from shared content** while maintaining lot-specific quality

---

## Workflow Selection Guide

Use this guide to select the appropriate workflow:

| Scenario | Use Workflow | Key Differentiators |
|----------|--------------|---------------------|
| Simple commercial bid, <£1M, no technical solution | Workflow 1 | Simplified, skip Phase 2 |
| Complex government bid, £10M+, Salesforce implementation | Workflow 2 | Full sequence, all phases |
| Framework call-off, pre-qualified supplier | Workflow 3 | Simplified Phase 0/1, focus on capability |
| Re-bidding previous opportunity with historical content | Workflow 4 | Leverage library, focus on updates |
| Multi-lot procurement, bidding multiple lots | Workflow 5 | Per-lot + shared content approach |
| Infrastructure/cloud/cyber bid (non-Salesforce) | Adapt Workflow 2 | Replace ibm-sf-* with ibm-bid-solution-architect |
| Proactive bid (no RFP, relationship-based) | Adapt Workflow 1 | Skip clarifications, emphasis on value proposition |

## Common Patterns Across Workflows

### Always Start with Phase 0
Every workflow begins with opportunity assessment. Never skip qualification for opportunities >£1M.

### Quality Gates are Mandatory
Gate 1 (GO/NO-GO) and Gate 2 (Technical Assurance) checkpoints prevent wasted effort and ensure quality.

### Iterative Writer/Evaluator Loop
All workflows use ibm-bid-writer + ibm-bid-answer-evaluator iteration until quality threshold met.

### Optional Visual Enrichment
After drafting an answer with ibm-bid-writer, use ibm-bid-image-definer to define AI-ready image prompts and visual recommendations for answers that would benefit from diagrams or imagery. Skip for text-only submissions or where images are not evaluated.

### Document Flow Convention
All workflows follow ../tmp/ -> ../outputs/ document flow pattern for context management.

### Supporting Resources Available Throughout
All workflows can leverage ibm-bid-library, ibm-bid-customer-stories, and ibm-bid-strategy-and-capabilities-2026 at any phase.

## Customizing Workflows

These workflows are templates. Customize based on:
- **Tender complexity**: Add/remove skills as needed
- **Time constraints**: Prioritize critical skills if time-limited
- **Resource availability**: Parallel execution requires multiple team members
- **Client requirements**: Some tenders have specific requirements (e.g., oral presentation, site visit)

Always maintain the phase sequence (0→1→2→3→4) even if skipping individual phases.
