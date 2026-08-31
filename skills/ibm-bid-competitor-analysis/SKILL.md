---
name: ibm-bid-competitor-analysis
description: Analyse likely competitors, incumbent advantage, win paths, attack lines against IBM, and counter-positioning for a tender or bid opportunity. Use when the user asks for competitor analysis, black-hat review, incumbent assessment, likely bidder profiling, competitor-specific win strategy, rebuttal planning, response surgery against rival strengths, public-source competitor intelligence, or questions such as "who are we up against?", "how will the incumbent defend?", "how would Accenture/TCS/Deloitte attack this?", or "how do we beat competitor X?".
---

# IBM Bid Competitor Analysis

# Overview

Assess the competitive field around a bid, convert weak signals into explicit hypotheses, and recommend how IBM should counter likely rival positions. Use this as a black-hat controller for pre-bid positioning, draft response hardening, and late-stage submission review.

## Context Management

Write output to `./tmp/ibm-bid-competitor-analysis.md` only when the user asks for a persisted artifact or when another skill needs a handoff file. Keep responses inline by default.

When bid-state continuity matters, update `./tmp/ibm-bid-project.md` with:
- `competitor_analysis_status: complete`
- `competitor_analysis_artifact: ./tmp/ibm-bid-competitor-analysis.md`
- `competitor_priority_threats`: top 1-3 named competitors or archetypes
- `competitor_hypotheses`: short bullets capturing likely competitor moves or incumbent defences
- `artifacts_generated`: include `./tmp/ibm-bid-competitor-analysis.md` when the artifact is written
- `next_skill_recommendation`: normally `ibm-bid-win-themes`, `ibm-bid-executive-summary`, or response surgery with `ibm-bid-writer`

## How To Use This Skill

Use this file as the controller for the analysis.

- Read `references/analysis-method.md` first for the workflow, evidence rules, confidence model, and output contract.
- Read `references/decomposition-scope.md` when you need a full-scope black-hat review, workshop agenda, or structured coverage check across competitor-analysis dimensions.
- Read `references/web-research.md` when the analysis needs current public-source competitor intelligence beyond the bid pack and internal IBM materials.
- Load competitor profiles from `references/competitors/` when analyzing specific named competitors (Accenture, Capgemini, Cognizant, Deloitte, HCL, Infosys). These profiles provide detailed intelligence on positioning, commercial approach, delivery strategy, and observed behaviors.
- Load only the bid artifacts that materially improve the assessment:
  - `./tmp/ibm-bid-requirements-analysis.md`
  - `./tmp/ibm-bid-strategic-positioning.md`
  - `./tmp/ibm-bid-win-themes.md`
  - `./tmp/ibm-bid-qualification.md`
  - Draft answers or solution documents under `./tmp/`
- Use adjacent skills as needed:
  - `$ibm-bid-library` for similar historical pursuits and competitor clues
  - `$ibm-bid-customer-stories` for proof points that blunt rival narratives
  - `$ibm-bid-strategy-and-capabilities-2026` for IBM differentiators and named capabilities
  - `$ibm-bid-writer` when the outcome should be rewritten into evaluator-facing bid content
- Use public web search when competitor positioning depends on current facts such as recent client wins, partnerships, acquisitions, analyst mentions, geographic presence, hiring signals, or offering changes. Apply the sourcing and labeling rules in `references/web-research.md`.

Do not load every artifact or reference by default. Start with the method and the highest-signal bid context, then expand only where evidence is weak.

## Core Workflow

1. Identify the analysis mode:
   - named competitor review
   - incumbent defence review
   - open-field likely bidder analysis
   - draft response black-hat review
2. Establish the buyer context before discussing competitors:
   - procurement route
   - stated outcomes
   - likely weighted criteria
   - risk appetite
   - delivery and commercial constraints
3. Build the competitor set:
   - confirmed named rivals if evidenced
   - likely archetypes if not evidenced
   - separate evidence from inference
   - gather current public-source signals if the likely field or rival posture is time-sensitive
4. Score each competitor on likely buyer fit, offer strength, delivery credibility, commercial posture, and proof position.
5. Run black-hat reasoning:
   - what each rival will lead with
   - where they will attack IBM
   - which buyer anxieties they can exploit
6. Convert the result into IBM actions:
   - response surgery
   - proof-point insertion
   - price and commercial guardrails
   - stakeholder and relationship actions
   - clarification questions
7. End with a ranked threat view and explicit recommendations.

## Operating Rules

- Ground every named-competitor claim in evidence when possible. If the bid documents do not support a named competitor, use archetypes and say so.
- Label statements as `Evidenced`, `Inferred`, or `Assumed` when the distinction matters.
- When using web research, distinguish between company-stated claims, third-party reporting, and your own inference from the sources.
- Do not invent proprietary knowledge about competitor pricing, margins, or client relationships.
- Avoid generic SWOT dumping. Tie every point to buyer criteria, likely award logic, and IBM response implications.
- Treat incumbent advantage separately from capability advantage; incumbents often win on access, familiarity, and switching risk, not superior solution design.
- When reviewing a draft answer, assess whether the response unintentionally leaves a clean lane for a competitor attack.
- Prefer a short list of decisive competitor moves over exhaustive but weak speculation.

## Output Requirements

Produce a structured assessment with these sections:

- **Situation Summary**: opportunity context, analysis mode, and evidence base
- **Likely Competitors**: named rivals or archetypes, ranked by threat
- **Competitor Cards**: one concise profile per priority rival
- **Likely Attack Lines On IBM**: what each competitor will say and why it may land
- **IBM Counter-Positioning**: how IBM should respond in messaging, proof, solution shape, and commercial stance
- **Response Surgery**: specific changes to drafts, win themes, proof points, or structure
- **Priority Actions**: immediate next steps with owner-style recommendations

## References

- `references/analysis-method.md` - workflow, evidence model, competitor scoring lenses, and output contract
- `references/decomposition-scope.md` - 10 wide, 2 deep scope map for full competitor-analysis coverage
- `references/web-research.md` - public-source competitor-intelligence workflow, source hierarchy, and attribution rules
- `references/competitors/` - detailed competitor intelligence profiles for major IBM rivals:
  - **Global Systems Integrators:**
    - `Accenture.md` - business transformation partner, consulting heritage, premium positioning
    - `Capgemini.md` - European heritage, engineering focus, balanced commercial approach
    - `Cognizant.md` - digital transformation focus, competitive pricing, offshore leverage
    - `Deloitte.md` - Big 4 consulting, advisory-led, premium positioning
    - `HCL.md` - Indian heritage, aggressive pricing, product-led approach
    - `Infosys.md` - Indian heritage, digital transformation, competitive pricing
  - **UK Salesforce Specialists:**
    - `Bluewave.md` - central government and NHS specialist, technical depth, security clearance
    - `DigitalModus.md` - local government and education specialist, social value focus
    - `Infomentum.md` - healthcare and life sciences specialist, regulatory compliance expertise
    - `Ziipline.md` - commercial sector specialist, modern DevOps practices, rapid delivery
  - `README.md` - guide to using competitor profiles in bid analysis
