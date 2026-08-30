---
name: ibm-bid-solution-architect
description: Generate comprehensive technology-agnostic solution architecture documents for non-Salesforce implementations (infrastructure, cloud, cybersecurity, integration). Use when creating solution design documents, architecture documentation, or technical specifications for infrastructure bids, cloud migrations, cybersecurity implementations, or integration projects. Supports incremental updates where requirements change. Follows modular 15-section structure similar to ibm-sf-solution-architect but platform-agnostic.
metadata:
  skills-required:
    - ibm-bid-requirements-analysis
  skills-suggested:
    - ibm-bid-win-themes
---

# IBM Bid Solution Architect (Non-Salesforce)

Generate a 15-section non-Salesforce solution architecture document for tender responses.

## Context Management

Use these paths:
- State: `./tmp/ibm-bid-solution/state.json`
- Section outputs: `./tmp/ibm-bid-solution/sections/`
- Memory summary: `./tmp/ibm-bid-solution/section-memory.md`
- Final assembled doc: `./tmp/ibm-bid-solution/complete_solution.md`

Persist after every section. Copy final output to `./outputs` only at completion.

## Required Generation Mode

Always run in **sectional mode** (one section per pass). Do not generate the full document in one response.

## Load Strategy (Progressive Disclosure)

1. Load this file for orchestration rules.
2. Load `$SKILL_DIR/references/section-contracts.md` for section scope/dependencies.
3. Load `$SKILL_DIR/references/style-rules.md` for writing constraints.
4. Load `$SKILL_DIR/references/workflow-state.md` for state file protocol.
5. Load only the minimum requirement excerpts relevant to the current section.
6. Load section summaries from `section-memory.md`; do not reload full prior sections unless revising that section.

## Workflow

### Step 1: Initialize
- Ensure `./tmp/ibm-bid-solution/sections/` exists.
- Initialize state file if missing.
- Validate required inputs: requirements, NFRs, constraints, integration needs.

### Step 2: Select Next Section
- Choose the next section with dependencies satisfied from `section-contracts.md`.
- Prefer this order: 02-15, then 01 (executive summary last).
- If user requests a specific section, honor it if dependencies are met.

### Step 3: Build Section Context Pack
Include only:
- Current section contract
- Relevant requirement snippets and constraints
- 5-10 line memory summaries of dependency sections
- Global style rules

Hard limits:
- Input pack target: <= 1800 words
- No full-document context loading

### Step 4: Generate Single Section
- Write one section file: `sections/NN-<name>.md`
- Include decision, rationale, alternatives, risks, traceability
- Target 400-900 words unless user requests a different depth

### Step 5: Update Memory and State
- Append a short summary to `section-memory.md`
- Mark section complete in `state.json`
- Record changed requirements if detected

### Step 6: Incremental Updates
When requirements change:
1. Identify impacted sections only.
2. Regenerate only impacted section files.
3. Refresh memory summaries for affected sections.
4. Rebuild `complete_solution.md`.

### Step 7: Assemble Final Document
Assemble sections in numerical order with heading normalization:
1. Executive Summary
2. System Architecture
3. Technology Stack
4. Infrastructure Design
5. Security Architecture
6. Integration Architecture
7. Deployment Model
8. Scalability and Performance
9. Data Architecture
10. Disaster Recovery
11. Operational Model
12. Support Model
13. Migration Approach
14. Testing Strategy
15. Risk Mitigation

## Quality Gate

Before finalizing:
- All section dependencies respected
- All requirements traced at least once
- Security, performance, integration, and DR explicitly covered
- Risks include owner, probability, impact, mitigation
- Terminology consistent across sections
