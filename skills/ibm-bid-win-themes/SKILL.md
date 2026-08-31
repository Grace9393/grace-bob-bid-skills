---
name: ibm-bid-win-themes
description: Generate Shipley-compliant win themes for IBM tender responses combining tender analysis outputs with IBM strategic differentiators. Use when the user requests win themes, competitive positioning statements, theme development, value propositions, or strategic messaging for proposals, bids, tender responses, or business development materials. Works with ibm-bid-requirements-analysis outputs, ibm-bid-customer-stories for proof points, and ibm-bid-strategy-and-capabilities-2026 for differentiators.
metadata:
  skills-required:
    - ibm-bid-requirements-analysis
    - ibm-bid-strategic-positioning
    - ibm-bid-customer-stories
    - ibm-bid-strategy-and-capabilities-2026
    - ibm-bid-library
  skills-suggested:
    - ibm-bid-hot-buttons
---

# IBM Win Themes

Generate Shipley-compliant win themes linking quantified benefits to IBM discriminators and customer needs.

## Shipley Theme Formula

**[Quantified Benefit] + [Discriminating Feature] + [Customer Issue]**

- Benefit first (customer gains)
- Feature second (IBM's unique capability)  
- Link to customer issue
- Quantify wherever possible
- Single sentence preferred
- Litmus test: "Could competitor claim this?" (Must be NO)

## Eight-Step Process

1. List customer issues (from tender analysis)
2. Match IBM discriminating features (use `ibm-bid-strategy-and-capabilities-2026` skill for current capabilities)
3. Match the IBM bid library (use `ibm-bid-library` skill for previous bid submissions)
4. Define issue specifically and uniquely
5. Identify success story with quantified benefit (use `ibm-bid-customer-stories` skill to search the database)
6. Draft theme linking all three elements
7. Create a candidate customer story pool for review
8. Lock the approved customer story shortlist for downstream use

## Context Management

Write output to `./tmp/ibm-bid-win-themes.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

When win themes will feed downstream content development, also write:
- `./tmp/ibm-bid-candidate-customer-stories.md` - candidate pool for human review, normally around 10 stories
- `./tmp/ibm-bid-approved-customer-stories.md` - approved subset for downstream use after review, normally 3-5 stories

The candidate file is the review pool. The approved file is the controlled evidence pool for downstream wireframes and draft answers.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `win_themes_status: complete`
- `win_themes_artifact: ./tmp/ibm-bid-win-themes.md`
- `win_themes_count`: number of generated themes
- `candidate_customer_stories_artifact: ./tmp/ibm-bid-candidate-customer-stories.md`
- `candidate_customer_stories`: around 10 candidate stories by ID/title
- `approved_customer_stories_artifact: ./tmp/ibm-bid-approved-customer-stories.md`
- `approved_customer_stories`: 3-5 approved stories by ID/title
- `artifacts_generated`: include `./tmp/ibm-bid-win-themes.md`, `./tmp/ibm-bid-candidate-customer-stories.md`, and `./tmp/ibm-bid-approved-customer-stories.md` when those artifacts are written
- `next_skill_recommendation`: normally `ibm-bid-executive-summary` or `ibm-bid-wireframe-creator`

## Identifying True Differentiators

A differentiator must meet two criteria:
1. **Customer needs it** - Addresses a stated or underlying client requirement
2. **Competitor doesn't have it** - A feature that differs from competitor offerings

Use this framework to classify capabilities:

| Position | Customer Needs It | Competitor Has It | IBM Has It | Strategic Value |
|----------|-------------------|-------------------|------------|-----------------|
| **Differentiator** | Yes | No | Yes | High - Use in win themes |
| **Weakness** | Yes | Yes | No | Address or mitigate |
| **Neutral** | Yes | Yes | Yes | Low - Not differentiating |
| **Irrelevant** | No | Yes | Yes | None - Don't emphasise |

**Key insight**: Capabilities in the "Neutral" zone (customer needs it, everyone has it) do not win deals. Focus win themes on true differentiators where IBM has something the competitor cannot claim.

## IBM Strategic Differentiators

**Core positioning**: Client Zero transformation story, AI-powered capabilities (Agentforce, multi-agent systems), government sector expertise (HMRC, NHS, FCDO, SPEN), enterprise-scale deployments, Salesforce centre of excellence, Crown Commercial Service frameworks

**vs Accenture**: More specialised Salesforce expertise, better AI implementation track record, Client Zero story
**vs Capgemini**: Deeper technical architecture, stronger UK government relationships, proven AI deployment

## Theme Patterns

**Cost reduction**: "[Organisation] reduces [cost] by [%] through [IBM capability], as demonstrated [success story]"
Example: "HMRC reduces case handling costs by 35% through IBM's AI-powered triage, as delivered for HSE Ireland's 5.1M citizens"

**Time saving**: "[IBM solution] enables [organisation] to achieve [outcome] in [timeframe] vs [baseline], leveraging [differentiator]"
Example: "IBM's accelerators enable HMRC to launch services in 12 weeks vs 9 months, leveraging Client Zero patterns"

**Risk mitigation**: "[Organisation] minimises [risk] through [IBM capability], proven across [scale]"
Example: "NHS minimises integration risk through IBM's interoperability framework, deployed across 47 trusts managing 2.3bn records"

**Capability enhancement**: "[IBM solution] delivers [capability] enabling [strategic outcome], validated by [metric]"
Example: "IBM's Agentforce delivers conversational AI reducing FCDO response times from 48 hours to 2 minutes with 94% accuracy across 12 languages"

**Competitive advantage**: "As the only provider to [unique achievement], IBM delivers [benefit] through [differentiator]"
Example: "As the only UK provider to implement Salesforce at scale for tax administration, IBM delivers proven patterns managing £700bn annual revenue"

## Quality Checklist

**Litmus test**: Could competitor claim this? (NO) | Could evaluator paste into scorecard? (YES)

**Structure**: Benefit before feature | Quantified | Discriminating | Links to customer issue | Single sentence <40 words | Passes read-aloud test

**Avoid**: "Uniquely qualified", "committed to partnership", "best-in-class", "world-leading", features without benefits, benefits without proof, generic claims

## Inputs Required

**From tender analysis**: Client profile, stated requirements, underlying needs, evaluation criteria, competitive positioning opportunities

**From IBM strategy**: Relevant case studies with metrics, differentiating capabilities vs competitors, quantified benefits, risk mitigation factors, innovation credentials

## Complete Tender Response Workflow

This skill is part of the 5-phase IBM Bid Management workflow.

**Current Phase**: Phase 1 (Strategic Positioning)
**Position**: Sequential execution - must run BEFORE ibm-bid-executive-summary

**Critical**: Win themes form the strategic backbone of the entire bid. All responses in Phase 3 must incorporate these themes for consistency.

See ibm-bid-navigator for complete workflow guidance.

## Integration with Other Skills

### Required Inputs

**Phase 0 outputs** (required):
- **ibm-bid-requirements-analysis**: ./tmp/ibm-bid-requirements-analysis.md (client profile, requirements, underlying needs)
  - Uses: Customer issues, evaluation criteria, operational gaps
  - Essential for Step 1 (list customer issues)
- **ibm-bid-strategic-positioning**: ./tmp/ibm-bid-strategic-positioning.md (competitive positioning, win theme inputs)
  - Uses: Competitive landscape, differentiation opportunities, win theme inputs prepared
  - Essential for understanding differentiation opportunities and competitive positioning

**IBM Knowledge Bases** (required - use via FTS5 search or direct reference):
- **ibm-bid-customer-stories**: 857 customer success stories with quantified outcomes
  - Search by: Industry, technology, Salesforce cloud, challenge type
  - Use for: Proof points with metrics (Step 5 - identify success story with quantified benefit)
  - Example searches: "government Sales Cloud", "NHS", "tax administration"

- **ibm-bid-strategy-and-capabilities-2026**: IBM 2026 strategy and capabilities
  - Use for: IBM differentiators, AI capabilities (Agentforce, GenAI), Client Zero story
  - Reference: Strategic positioning vs competitors (Step 2 - match IBM discriminating features)

- **ibm-bid-library**: 3000+ historical responses
  - Search for: Previous win themes for similar clients or technologies
  - Use for: Proven theme patterns that won previous bids (Step 3 - match IBM bid library)

### Recommended Next Steps

**After win themes generated:**

1. **Review and validate themes**:
   - Apply litmus test: "Could competitor claim this?" (Must be NO)
   - Verify quantified benefits from customer stories are accurate
   - Ensure themes map to evaluation criteria from tender analysis
   - Check themes are concise (<40 words, single sentence preferred)
   - Confirm the candidate story pool is broad enough for review, normally around 10 stories
   - Confirm the approved customer story shortlist is limited to the smallest defensible set, normally 3-5 stories, with each story mapped to one or more win themes
   - Allow a human reviewer to adjust the approved subset before Phase 3 begins

2. **Proceed to ibm-bid-executive-summary** (if required by RFP):
   - Input: ./tmp/ibm-bid-win-themes.md + ./tmp/ibm-bid-requirements-analysis.md + ./tmp/ibm-bid-strategic-positioning.md
   - Output: 1000-word executive summary incorporating all win themes
   - Sequential dependency: Executive summary MUST incorporate win themes

3. **Skip to Phase 2 or Phase 3** (if executive summary not required):
   - Phase 2: Solution architecture (if technical bid)
   - Phase 3: Content development (ibm-bid-wireframe-creator, ibm-bid-writer)
   - All Phase 3 responses must weave win themes throughout for strategic consistency
   - Phase 3 must use only the approved customer stories in `./tmp/ibm-bid-approved-customer-stories.md` unless the shortlist is deliberately refreshed after review

### Supporting Resources

**Throughout theme development:**
| Resource | Purpose | Usage |
|----------|---------|-------|
| **ibm-bid-customer-stories** | Proof points with quantified outcomes | FTS5 search by industry/cloud/challenge |
| **ibm-bid-strategy-and-capabilities-2026** | IBM differentiators and capabilities | Reference for Step 2 (discriminating features) |
| **ibm-bid-library** | Historical win themes and patterns | FTS5 search for similar bids |

### This Skill Feeds All Downstream Skills

Win themes (./tmp/ibm-bid-win-themes.md) are consumed by:

**Phase 1**:
- ibm-bid-executive-summary (incorporates all themes in 4-part structure)

**Phase 3**:
- ibm-bid-wireframe-creator (maps only approved stories to sections where evidence strengthens the answer)
- ibm-bid-writer (weaves themes into every response for strategic consistency)
- Critical: ALL responses must reference relevant win themes to maintain consistent competitive positioning
- Critical: customer story references in Phase 3 must come only from `./tmp/ibm-bid-approved-customer-stories.md`

**Phase 4**:
- ibm-bid-answer-evaluator (validates theme incorporation in responses)
- Final evaluation confirms consistent messaging across all responses

**Oral Presentations** (if required):
- ibm-story-pitch-development (win themes become core pitch messaging)
- ibm-story-presentation-structuring (themes structure presentation flow)

### Theme Development Process

**Step-by-step integration with other skills:**

1. **List customer issues** (Step 1):
   - Source: ./tmp/ibm-bid-requirements-analysis.md (underlying needs, stated requirements, evaluation criteria)
   - Source: ./tmp/ibm-bid-strategic-positioning.md (win theme inputs prepared)
   - Identify: 5-10 key customer issues to address

2. **Match IBM discriminating features** (Step 2):
   - Source: ibm-bid-strategy-and-capabilities-2026
   - Identify: IBM capabilities that competitors cannot claim
   - Apply: Differentiator framework (customer needs it + competitor doesn't have it)

3. **Match IBM bid library** (Step 3):
   - Source: ibm-bid-library (FTS5 search)
   - Search: Similar client types, industries, or technologies
   - Extract: Proven win theme patterns

4. **Define issue specifically and uniquely** (Step 4):
   - Frame: Customer issue in specific, measurable terms
   - Avoid: Generic problems that apply to all clients

5. **Identify success story with quantified benefit** (Step 5):
   - Source: ibm-bid-customer-stories (FTS5 search)
   - Search by: Client's industry, technology, or challenge type
   - Extract: Quantified outcomes (% reduction, timeframes, £ savings, user counts)
   - Candidate pool: Select around 10 strong stories that collectively cover the full set of win themes without unnecessary duplication

6. **Draft theme** (Step 6):
   - Formula: [Quantified Benefit] + [Discriminating Feature] + [Customer Issue]
   - Validate: Litmus test (competitor cannot claim this)
   - Format: Single sentence, <40 words, benefit-first

7. **Create the candidate review pool** (before approval):
   - Create `./tmp/ibm-bid-candidate-customer-stories.md`
   - Include around 10 candidate stories that are plausible fits for the win themes
   - For each story, record: story ID, title, company, industry, why it is a candidate, which win themes it could support, and the specific metrics or proof points available
   - Mark relative strength or fit so a human reviewer can quickly refine the list

8. **Lock the evidence set** (required before Phase 3):
   - Create `./tmp/ibm-bid-approved-customer-stories.md`
   - Start from the candidate pool and reduce it to the 3-5 approved stories that best support the win themes across the bid
   - Allow human review and adjustment of the approved subset before downstream use
   - For each story, record: story ID, title, company, industry, why it was selected, which win themes it supports, and the specific metrics or proof points that may be reused
   - State any exclusions or limits so downstream skills know what not to over-claim

### Quality Gate 1 Impact

Win themes validate the GO decision from Phase 0:
- **Differentiation exists**: If you can generate 3-5 strong win themes, differentiation is possible (supports GO)
- **Proof points available**: If customer stories provide quantified proof, claims are substantiable (reduces risk)
- **Competitive positioning clear**: If themes cannot be claimed by competitors, competitive advantage exists (increases win probability)

**Red flags from theme development**:
- Cannot identify 3+ differentiators (suggests commoditized competition, reconsider bid)
- No relevant customer stories (weak proof points, harder to win)
- Competitors can claim similar themes (no competitive advantage)
- Themes don't map to evaluation criteria (missing strategic alignment)

## Output Format

**Individual theme**:
```
SECTION: [Identifier]
THEME: [Single sentence benefit-feature-issue]
PROOF: [3 bullet points with metrics]
REFERENCE: [Success story]
```

**Approved story shortlist**:
```
STORY: [ID] - [Title]
COMPANY / INDUSTRY: [Company] / [Industry]
SUPPORTS WIN THEMES: [Theme IDs]
REUSABLE PROOF: [metrics, outcomes, challenge/solution details allowed downstream]
RATIONALE: [why this story made the shortlist]
LIMITS: [what downstream skills should avoid implying]
```

**Candidate story pool**:
```
STORY: [ID] - [Title]
COMPANY / INDUSTRY: [Company] / [Industry]
POTENTIAL WIN THEME FIT: [Theme IDs]
REUSABLE PROOF: [metrics, outcomes, challenge/solution details available]
FIT NOTES: [why this is a viable candidate]
REVIEW SIGNAL: [strong fit | medium fit | reserve]
```

**Grouped themes** (for formal evaluation):
```
REQUIREMENT | THEME
-----------|-------
[Text]     | • Benefit 1
           | • Benefit 2
```

## Example

Input: HMRC tender for CRM, 45M taxpayers, 600 agents, reduce case processing, integrate legacy systems

**Primary**: "HMRC reduces tax compliance case processing from 14 days to 3 days whilst improving citizen satisfaction by 40%, leveraging IBM's AI-powered triage deployed for HSE Ireland's 5.1M citizen programme"

**Supporting**:
- Integration: "IBM's middleware framework eliminates legacy risk, deployed across 23 UK agencies with 99.97% uptime"
- AI capability: "As UK's most experienced Agentforce implementer, IBM delivers conversational AI handling 85% tier-1 enquiries autonomously"
- Speed: "HMRC achieves operational service in 16 weeks through Client Zero accelerators vs 12-month industry average"
- Scale: "IBM's architecture supports 45M taxpayers, proven managing 47M NHS patients and €6.8bn Irish revenue"

## Principles

1. Benefits own the statement - customer gains lead
2. Quantification creates credibility - numbers beat adjectives  
3. Specificity beats generality - "35% reduction" beats "significant savings"
4. Proof validates claims - substantiate in proposal body
5. Discriminators win deals - if competitor can claim it, it's worthless
6. Customer language - mirror their terminology
7. Evaluation alignment - map to scoring criteria
8. Concision drives memory - evaluators remember punchy statements
