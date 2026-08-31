---
name: ibm-bid-strategic-positioning
description: Strategic analysis for bid opportunities including executive decision drivers, transformation vs BAU assessment, competitive sales strategy selection (Attack/Position strategies), and price-to-win analysis. Requires ibm-bid-requirements-analysis output as input. Second step in Phase 0 after requirements analysis.
---

# Bid Strategic Positioning Skill

Develop strategic positioning for tender responses including sales strategy, price-to-win analysis, and win theme inputs. Requires completed requirements analysis from `ibm-bid-requirements-analysis` skill.

## Complete Tender Response Workflow

This skill is part of the 5-phase IBM Bid Management workflow.

**Current Phase**: Phase 0 (Opportunity Assessment)
**Position**: Second step - run after ibm-bid-requirements-analysis, can run parallel with clarifications and qualification

**Prerequisites**: Must have ./tmp/ibm-bid-requirements-analysis.md from requirements-analysis skill

See ibm-bid-navigator for complete workflow guidance.

## Quick Start

1. Ensure `ibm-bid-requirements-analysis` has been run first
2. Read `./tmp/ibm-bid-requirements-analysis.md` for client context
3. Apply strategic frameworks from `references/strategic_frameworks.md`
4. Generate output to `./tmp/ibm-bid-strategic-positioning.md`
5. Feed results to `ibm-bid-win-themes` and `ibm-bid-executive-summary`

## Context Management

Write output to `./tmp/ibm-bid-strategic-positioning.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `strategic_positioning_status: complete`
- `strategic_positioning_artifact: ./tmp/ibm-bid-strategic-positioning.md`
- `strategic_recommendations`: short bullets covering the sales strategy, price-to-win posture, and positioning priorities
- `current_phase: strategic_positioning`
- `artifacts_generated`: include `./tmp/ibm-bid-strategic-positioning.md` when the artifact is written
- `next_skill_recommendation`: normally `ibm-bid-hot-buttons`, `ibm-bid-win-themes`, or `ibm-bid-competitor-analysis`

## Required Input

**./tmp/ibm-bid-requirements-analysis.md** must contain:
- Client profile (organisation, sector, context)
- Stated requirements breakdown
- Operational gaps and capability deficits
- Risk profile
- Competitive landscape overview

If requirements analysis is missing, run `ibm-bid-requirements-analysis` first.

## Strategic Analysis Framework

### Level 3 Analysis: Strategic Positioning

Read `references/strategic_frameworks.md` then apply:

**Executive Decision Drivers:**
Understand what drives the procurement decision at executive level:
- **Career risk mitigation**: Reference requirements, proven solutions, safe choices
- **Organisational credibility**: Sector comparators, audit trails, stakeholder validation
- **Political coverage**: Documentation needs, stakeholder engagement emphasis, decision justification

Look for signals:
- Reference requirements = need for safe choice precedent
- Steering committee involvement = multiple stakeholders to satisfy
- Extensive documentation requirements = covering decision trail

**Transformation vs BAU Assessment:**
Determine if this is problem-solving or capability-building:

*Immediate Problem Solving signals:*
- Tight timelines (6-12 months)
- Operational pain emphasis
- Quick wins required
- BAU maintenance focus
- Fix broken processes

*Future Capability Building signals:*
- Transformation language (change, modernize, transform)
- Platform thinking (foundation, scalability)
- Skills transfer requirements
- Innovation emphasis
- Build new capabilities

**Most tenders are both** - identify the balance and weight accordingly in response strategy.

**Win Theme Inputs Preparation:**
Prepare strategic inputs for the `ibm-bid-win-themes` skill:

1. **Customer issues mapped to evaluation criteria**: Link each pain point to scoring dimensions
2. **Underlying needs** (not just stated requirements): What they really need vs. what they asked for
3. **Competitive positioning opportunities**: Where we can differentiate vs likely bidders
4. **Differentiation areas**: Specific capabilities, approaches, or experiences competitors can't match

*Note: Do not generate win themes directly. Use the `ibm-bid-win-themes` skill which applies the Shipley formula (Quantified Benefit + Discriminating Feature + Customer Issue) and integrates with `ibm-bid-customer-stories` for proof points.*

**Competitive Landscape Strategy:**
Based on requirements analysis, develop positioning against likely bidders:
- Identify likely bidders (large consultancies, tech vendors, specialists)
- Note incumbent signals and market testing indicators
- Flag requirements that favour specific competitors
- Identify areas where competitors will use generic approaches

### Sales Strategy Selection

Based on SWOT, differentiation, competitor, and stakeholder analysis, determine which strategy best suits the deal.

**Note:** Flanking and Delay strategies are likely to be unsuccessful once the ITT is issued, as procurement criteria are already set.

#### Attack Strategies (Seeking New Business)

| Strategy | When to Use | Approach |
|----------|-------------|----------|
| **Frontal** | Clear advantage/superiority | Confront competitor head-on; compete on price or unique/best solution |
| **Flanking** | Parity or slightly disadvantaged | Target areas where competition is weak; alter the rules by resetting procurement criteria to our strengths; requires support from inside the client |
| **Fragment** | Disadvantaged but have one major strength | Target smaller, less defended areas; specialise and tailor for the client; establish a foot in the door; target a specific department or function |

#### Position Strategies (Protecting Existing Business)

| Strategy | When to Use | Approach |
|----------|-------------|----------|
| **Defend** | Incumbent with dominance | Focus on maintaining position; discourage competitors from encroaching; fortify existing strengths; improve service quality; build customer loyalty; support allies in the client |
| **Delay** | Need time to strengthen position | Postpone competitive action; wait for new technological advances or service improvements; invest in the account and service |

**Strategy Selection Process:**
1. Review competitive landscape from requirements analysis
2. Assess our position: incumbent, challenger, or new entrant
3. Evaluate our strengths against likely competitors
4. Select primary strategy based on position and strengths
5. Identify secondary tactics to support primary strategy

### Price to Win Analysis

Begin Price to Win early and update as new information emerges. Avoid common pitfalls:
- "Rolls Royce" proposals that exceed client budget expectations
- Late-stage solutioning cuts that increase delivery risk
- Late-stage price reductions that damage credibility

**What is Price to Win?**
- Top-down approach (vs IBM's traditional bottom-up pricing)
- Focused on client expectations rather than our solution cost
- Looks outward at customer and competitor, not inward at IBM
- Creates baseline expectation for the entire bid team
- Best practice: Performed independently from the deal team to avoid bias

**Five Viewpoints for Price to Win:**

| Viewpoint | Key Inputs |
|-----------|------------|
| **1. Value** | Value case, ROI/TCO proposition, cost structure, fair price for proposal |
| **2. Market** | Win/loss analysis, competitive benchmarking, similar deal retrospectives |
| **3. Client** | Business case dialogue, current spend, contract value, opening negotiation point |
| **4. Competitive** | Competitor price estimates, onshore/offshore ratios, historical win-loss, top-down vs bottom-up |
| **5. Deal Team** | Estimated highest acceptable price, RFP scope and scoring, budgeting |

**Price to Win Process:**
1. Establish preliminary Price to Win using available information
2. Consider multiple viewpoints (not just one or two)
3. Calculate Total Allowable Cost (Price to Win - desired margin)
4. Scope and solution to Total Allowable Cost
5. Iterate on estimated Price to Win as new information emerges

**Document your assumptions:**
- Client budget indicators from tender
- Sector benchmark data (e.g., similar NHS/government contracts)
- Competitive pricing intelligence
- Risk factors affecting price (complexity, timeline, penalties)
- Margin requirements and flexibility

Read `references/price_to_win.md` for detailed framework and examples.

## Analysis Quality Checks

Before finalising output:

1. Executive decision drivers clearly articulated (not generic)
2. Transformation vs BAU balance identified with evidence
3. Win theme inputs prepared for downstream win-themes skill
4. Sales strategy selected with clear rationale
5. Price to Win estimated using multiple viewpoints
6. Competitive positioning addresses each likely bidder type
7. All strategic recommendations trace back to requirements analysis

## Output Format

Use template from `references/output_template.md`. Structure:

```markdown
# STRATEGIC POSITIONING: [CLIENT NAME]

## EXECUTIVE SUMMARY
[2-3 sentences: strategic approach, sales strategy, price positioning]

## EXECUTIVE DECISION DRIVERS
[What drives this decision at exec level]

## TRANSFORMATION VS BAU
[Balance between problem-solving and capability-building]

## COMPETITIVE LANDSCAPE STRATEGY
[Positioning against likely bidders]

## SALES STRATEGY RECOMMENDATION
[Selected strategy with rationale]

## PRICE TO WIN ANALYSIS
[Estimated price range with viewpoint analysis]

## WIN THEME INPUTS
[Prepared inputs for ibm-bid-win-themes skill]
```

## Integration with Other Skills

### Required Inputs
- **./tmp/ibm-bid-requirements-analysis.md**: Client profile, requirements, gaps, risks, competitive landscape (from ibm-bid-requirements-analysis skill)

### Recommended Next Steps

**After strategic positioning complete:**

**1. Continue Phase 0 in parallel** (if not already executed):
- **ibm-bid-clarifications**: Identify ambiguous requirements
- **ibm-bid-qualification**: Score opportunity (GO/NO-GO decision)

**2. After Phase 0 complete, proceed to Quality Gate 1**:
- Review qualification score + strategic positioning
- Make GO/NO-GO decision
- If GO (score ≥60), proceed to Phase 1

**3. Proceed to Phase 1 (Strategic Positioning)**:
- **ibm-bid-win-themes**: Generate Shipley-compliant win themes
  - Input: ./tmp/ibm-bid-requirements-analysis.md + ./tmp/ibm-bid-strategic-positioning.md
  - Uses: Win theme inputs, competitive positioning, customer issues
  - Integrates: ibm-bid-customer-stories for proof points
  - Output: 3-7 win themes forming strategic backbone

- **ibm-bid-executive-summary**: Write executive summary (if required by RFP)
  - Input: ./tmp/ibm-bid-requirements-analysis.md + ./tmp/ibm-bid-strategic-positioning.md
  - Output: 1000-word executive summary

### Supporting Resources
- **ibm-bid-library**: Search for win/loss analysis, competitive intelligence, pricing data
- **ibm-bid-customer-stories**: Search for proof points matching differentiation areas
- **ibm-bid-strategy-and-capabilities-2026**: Reference IBM strategic positioning and capabilities

### This Skill Feeds Downstream Skills

The strategic positioning output (./tmp/ibm-bid-strategic-positioning.md) is consumed by:

**Phase 1**:
- ibm-bid-win-themes (primary consumer - win theme inputs, competitive positioning)
- ibm-bid-executive-summary (strategic approach, transformation vision)

**Phase 2**:
- ibm-sf-solution-architect or ibm-bid-solution-architect (strategic architecture decisions)

**Phase 3**:
- ibm-bid-writer (competitive positioning, win themes, strategic messaging)

### Quality Gate 1 Impact

This strategic analysis directly informs Quality Gate 1 (GO/NO-GO decision) by providing:
- **Sales strategy**: Confidence in approach (Frontal = high confidence, Fragment = lower)
- **Price-to-win estimate**: Commercial viability and margin potential
- **Competitive positioning**: Realistic assessment of win probability
- **Strategic complexity**: Transformation vs BAU affects resource needs

**Strategic indicators for GO decision**:
- Clear sales strategy with strong rationale (winnable position)
- Price-to-win supports margin objectives (profitable)
- Competitive differentiation opportunities identified (defensible win)
- Executive decision drivers aligned with IBM strengths (credible)

**Strategic red flags suggesting NO-GO**:
- No viable sales strategy (all strategies show low win probability)
- Price-to-win incompatible with margin requirements (unprofitable)
- No competitive differentiation opportunities (commoditized)
- Incumbent heavily favoured with no flanking opportunities (unwinnable)
