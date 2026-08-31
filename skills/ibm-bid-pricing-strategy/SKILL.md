---
name: ibm-bid-pricing-strategy
description: Develop commercial pricing strategies for IBM bids and proposals, especially when moving from PxQ, FTE, rate-card, or input-based pricing toward value-based contracting. Use when you need to (1) select a commercial model such as T&M, fixed price, managed service, outcome-based, gain-share, hybrid, or performance-based partnering, (2) design pricing that rewards outcomes, automation, service quality, compliance, and continuous improvement, (3) calculate price-to-win, margin, TCO, and sensitivity scenarios, (4) structure innovation funds, outcome payment pools, service credits, gain-share ratios, or discount strategies, (5) assess pricing risks and perverse incentives, or (6) prepare pricing narratives and approval-ready commercial documentation for IBM bids.
metadata:
  skills-suggested:
    - ibm-bid-staffing-planner
    - ibm-bid-solution-architect
---

# IBM Bid Pricing Strategy

Develop pricing strategies that are commercially robust for IBM and credible for the client, with a strong preference for value-based models where automation, outcomes, statutory compliance, user experience, and continuous improvement matter more than labour inputs.

This skill incorporates a broader public-sector value-based contracting pattern: PxQ/FTE models are useful for internal cost estimation, but they can misalign supplier incentives when used as the client-facing value mechanism for modern digital services.

## Quick Reference

| Resource | Location | Use when |
|---|---|---|
| Value-based principles | `$SKILL_DIR/references/value-based-contracting.md` | Moving away from PxQ/FTE, designing outcome-led pricing, checking incentive alignment |
| Contracting models | `$SKILL_DIR/references/contracting-models.md` | Selecting or comparing outcome-based, gain-share, managed service, hybrid, or performance-based partnering models |
| CFO/public-sector transition | `$SKILL_DIR/references/public-sector-transition.md` | Pricing high-integrity public services with statutory duties, vulnerable users, data quality constraints, or legacy technology |
| Pricing negotiation readiness | `$SKILL_DIR/references/negotiation-readiness.md` | Defending price, setting walkaway/ZOPA, planning concessions and tradeables, or responding to discount pressure |
| Staffing cost source | `$SKILL_DIR/assets/staffing_config.yaml` | Local copy of role, seniority, location, availability, rate-card, and governance assumptions for staffing-derived cost baselines |
| Pricing templates | `$SKILL_DIR/references/templates.md` | Writing commercial proposal sections and pricing approval memos |
| Special scenarios | `$SKILL_DIR/references/scenarios.md` | Frameworks, managed services, gain-share, risk/reward, tiers, and multi-year efficiency pricing |
| Detailed examples | `$SKILL_DIR/references/examples.md` | Worked calculations for fixed price, blended rates, and gain-share payments |

## Core Principle

Separate **internal cost build-up** from **client-facing value model**.

- Use FTEs, role rates, location mix, overheads, and contingency to understand IBM's delivery economics.
- Avoid presenting FTE/PxQ as the value basis when the client needs automation, elasticity, resilience, compliance, service quality, or continuous improvement.
- Price the client-facing model around outcomes, SLAs, value creation, risk sharing, predictable service performance, and measurable improvement.

## Commercial Model Selection

### Input-Based Models

**Time & Materials (T&M)**

- Use for uncertain scope, discovery, early agile delivery, or work where outputs cannot yet be defined.
- Be careful: T&M can reward effort rather than value if left unmanaged.
- Add outcome guardrails where possible, such as delivery milestones, quality gates, burn-up transparency, and backlog/value tracking.

**Fixed Price (FP)**

- Use for well-defined deliverables, stable scope, and client need for cost certainty.
- Add contingency for delivery and scope risk.
- Pair with change-control thresholds and outcome acceptance criteria.

### Value-Based Models

Use value-based models when the client cares about service outcomes, automation, reduction of manual effort, measurable business value, statutory compliance, or long-term public value.

Primary patterns:

- **Outcome-Based Contracting:** Payment tied to agreed outcomes and KPIs.
- **Gain-Share:** Benefits from automation, cost reduction, or efficiency are shared.
- **Managed Service with Outcome SLAs:** Predictable service fee with enforceable outcome SLAs and service credits.
- **Hybrid Value-Based Model:** Combines base service fee, outcome SLAs, gain-share, outcome payments, and innovation funding.
- **Performance-Based Partnering:** Adds behavioural, governance, transparency, and collaboration incentives to performance measures.

Read `$SKILL_DIR/references/contracting-models.md` before recommending one of these models.

## Value-Based Pricing Design

When designing value-based pricing, define:

1. **Outcomes:** What the client actually needs, such as accuracy, timeliness, digital adoption, compliance, resilience, user experience, accessibility, automation coverage, or reduced manual interventions.
2. **Baselines:** Current volumes, cost, effort, error rates, rework, processing times, backlog, user contacts, SLA performance, data quality, and automation levels.
3. **Payment mechanics:** Base fee, outcome payment pool, gain-share ratio, service credits, penalties, stretch incentives, risk/reward bands, and innovation fund.
4. **Measurement:** Data sources, dashboards, audit trails, reporting cadence, KPI definitions, and anti-gaming controls.
5. **Governance:** Joint boards, escalation routes, review cycles, change-control thresholds, and decision rights.
6. **Risk allocation:** Which party owns operational risk, statutory/legal risk, transformation risk, data risk, technology risk, and third-party dependency risk.

For high-integrity public services, read `$SKILL_DIR/references/public-sector-transition.md` before finalising the recommendation.

## Rate Card And Cost Build-Up

Use rate cards for internal economics, price-to-win modelling, and staffing validation. Do not let rate cards become the only value story unless the procurement explicitly requires it.

### Preferred Source: Local Staffing Config

Use this skill's local `$SKILL_DIR/assets/staffing_config.yaml` as the preferred source for internal delivery-cost assumptions. It is copied from `ibm-bid-staffing-planner` so this pricing skill remains independently usable.

That config provides:

- Seniority levels, productivity, PRG, and band-mix weighting
- Role definitions and role types: `doer`, `doer_lead`, `leadership`, and `supporting`
- Delivery locations such as `uk_mainline`, `uk_cic`, and `india_cic`
- Weekly hours, availability, currency, and price multipliers by location
- Hourly rate cards by location and seniority
- Band-mix mappings for CIC reporting
- Governance rules for mandatory roles and allocation thresholds

For pricing work, prefer this sequence:

1. Use the local `$SKILL_DIR/assets/staffing_config.yaml` to understand roles, rates, seniority, locations, availability, and governance assumptions.
2. If `ibm-bid-staffing-planner` is available, use it to generate the staffing plan and commercial outputs.
3. Use the exported resource plan, cost, price, GP, GP%, duration, and location mix as the pricing baseline.
4. Use the pricing strategy skill to convert that internal baseline into the client-facing commercial model.
5. Only use the illustrative daily-rate table below when the local staffing config cannot support the required approximation or the user explicitly asks for quick manual approximation.

If the staffing planner source config changes, refresh this local copy so the two skills remain consistent.

### Fallback Manual Reference

**IBM Standard Rate Cards (UK Public Sector - 2026 Reference)**

| Role | Junior | Mid | Senior | Principal |
|---|---:|---:|---:|---:|
| Business Analyst | £550 | £750 | £950 | £1,200 |
| Technical Architect | £650 | £850 | £1,100 | £1,400 |
| Solution Architect | £700 | £900 | £1,200 | £1,500 |
| Developer | £500 | £700 | £900 | £1,150 |
| Project Manager | £600 | £800 | £1,000 | £1,300 |
| Scrum Master | £550 | £750 | £950 | N/A |
| Tester/QA | £450 | £600 | £800 | N/A |
| Service Manager | £550 | £750 | £950 | £1,200 |

Daily rates for UK public sector, March 2026 reference. Validate against the current approved IBM rate card before live use. Adjust for:

- Private sector: +15-25%
- Offshore: -40-60% depending on delivery location and role
- Nearshore: -20-30%
- Specialists: +20-40% for scarce AI/ML, security, cloud, or regulated-domain expertise

Cost build-up:

```text
Direct Labor = Sum(Role x FTE x Duration x Rate)
Expenses = Travel + Tools + Licenses + Subcontractors
Overheads = Direct Labor x 1.4-1.6
Contingency = (Labor + Expenses + Overheads) x risk %
Total Cost = Labor + Expenses + Overheads + Contingency
```

## Price-To-Win And Margin Analysis

Develop at least three scenarios unless the procurement constrains pricing:

| Scenario | Typical margin | Position | Use when |
|---|---:|---|---|
| Aggressive | 25% | Low-price / must-win | Strategic account, high follow-on value, acceptable lower margin |
| Competitive | 35% | Balanced | Sustainable margin and credible win position |
| Premium / Value | 45%+ | High differentiation | Strong differentiators, measurable ROI, high-risk or high-value outcomes |

For value-based proposals, do not evaluate only margin. Evaluate:

- Expected value: `Win probability x margin x contract value`
- TCO reduction for the client
- Risk transfer and risk premium
- Gain-share upside and caps
- Reinvestment potential through innovation funds
- Impact of service credits, penalties, and bonus pools
- Whether the price incentivises automation or accidentally preserves manual effort

## Risk-Adjusted Pricing

Price risk explicitly, especially for fixed price, outcome-based, and managed service models.

Common risk categories:

- Scope creep
- Client or third-party delays
- Technology and integration constraints
- Data quality weaknesses
- Regulatory or statutory change
- Resource availability
- KPI gaming or perverse incentives
- Over-automation in areas requiring human judgement
- Transition or dual-running risk

Formula:

```text
Risk-Adjusted Price = Base Price x (1 + sum(Risk Probability x Risk Impact))
```

Typical contingency reserves:

- Fixed price: 15-20% of base cost
- T&M with cap: 10-15%
- T&M open: 5-10%
- Outcome-based: 20-30%, adjusted for KPI maturity and data quality
- Managed service with outcome SLAs: align reserve to SLA credit exposure, demand volatility, and transition risk

## Workflow

### Step 1: Gather Inputs

Use available bid inputs:

- Solution scope from `ibm-bid-solution-architect`
- Staffing and delivery cost from `ibm-bid-staffing-planner` where available, using this skill's local `$SKILL_DIR/assets/staffing_config.yaml` as the standalone role/rate/location config
- Requirements from `ibm-bid-requirements-analysis`
- Competitive posture from `ibm-bid-strategic-positioning`
- Client value case from `ibm-business-case-creator`
- RFP commercial constraints, budget, payment terms, framework rules, and procurement scoring

### Step 2: Test Incentive Alignment

Before modelling numbers, decide whether PxQ/FTE, T&M, or rate-card pricing would create bad incentives.

Ask:

- Would automation reduce supplier revenue?
- Would the client pay the same even if manual effort falls?
- Are quality, compliance, timeliness, resilience, and user experience directly incentivised?
- Can benefits be baselined and measured credibly?
- Are there statutory duties or vulnerable users that require non-negotiable outcome thresholds?
- Does the model support continuous improvement without constant change requests?

If input-based pricing creates a conflict, move to a hybrid or value-based model.

### Step 3: Build Internal Cost Baseline

Calculate:

- Labour by role, FTE, duration, and location
- Expenses, tools, licences, subcontractors
- Overheads and delivery management
- Transition and dual-running cost
- Governance, reporting, and assurance cost
- Contingency by risk category

If `ibm-bid-staffing-planner` has been run, use its output as the baseline rather than recalculating from the fallback daily-rate table. Capture:

- Resource plan by role, seniority, location, and allocation
- Duration, committed duration, and delivery constraints
- Total cost, price, GP, and GP%
- Location mix and availability assumptions
- Governance and mandatory-role assumptions
- Scenario trade-offs and rejected options

Document in `./tmp/ibm-bid-pricing-strategy-baseline.xlsx` when spreadsheet modelling is required.

### Step 4: Design Client-Facing Commercial Model

Select the model:

- T&M with guardrails
- Fixed price with outcome acceptance
- Managed service with outcome SLAs
- Outcome-based contracting
- Gain-share
- Hybrid model
- Performance-based partnering

Define:

- Base service fee or baseline price
- Outcome payment pool
- SLA/service credit structure
- Gain-share ratio and cap
- Innovation fund contribution and governance
- KPI thresholds, stretch levels, and penalties
- Indexation, payment terms, and change-control rules

### Step 5: Develop Scenarios And Sensitivity Analysis

Create scenarios for:

- Aggressive, competitive, and premium/value price points
- Onshore, blended, and offshore delivery mix
- Demand changes and volume bands
- KPI underperformance and service credit exposure
- Gain-share upside and reinvestment
- Data quality or technology readiness delays
- Scope increase and duration change

Document in `./tmp/ibm-bid-pricing-strategy-scenarios.xlsx` or `./tmp/ibm-bid-pricing-strategy-sensitivity.xlsx` when needed.

### Step 6: Prepare Negotiation Guardrails

Read `$SKILL_DIR/references/negotiation-readiness.md` when pricing may be negotiated, challenged, or discounted.

Define:

- Opening position, target position, and walkaway point
- IBM BATNA and WATNA
- Estimated client BATNA, WATNA, and reservation position
- ZOPA and likely negotiation range
- Conditional concessions and required client gives
- High-value / low-cost tradeables to use before discounting
- Responses to price objections and competitor undercutting
- Escalation points for margin, scope, legal, delivery, or risk changes

### Step 7: Recommend Pricing Strategy

Provide:

- Recommended commercial model and why it fits
- Recommended total contract value and yearly profile
- IBM cost baseline, margin, and risk reserve
- Client value story, including TCO, risk reduction, and outcome improvement
- Payment mechanics and governance
- Key assumptions, exclusions, dependencies, and approval needs
- Risks, mitigations, and anti-gaming controls

### Step 8: Write Pricing Narrative

Use `$SKILL_DIR/references/templates.md` for proposal and approval memo structures.

The pricing narrative should explain:

- Why this model is commercially fair and aligned to client outcomes
- How it avoids PxQ/FTE perverse incentives where relevant
- How IBM is rewarded for automation, quality, compliance, and continuous improvement
- How the client receives predictable value, transparency, and risk assurance
- How baselines, dashboards, governance, and audit trails make the model measurable

## Quality Checklist

- [ ] Cost baseline validated with the delivery unit
- [ ] Local staffing config used as the preferred internal cost baseline
- [ ] Current IBM-approved rate cards validated before live use
- [ ] Client-facing value model separated from internal cost build-up
- [ ] PxQ/FTE incentive risks considered and documented
- [ ] Commercial model aligned to outcomes, not only effort
- [ ] Baselines and data sources credible enough for proposed KPIs
- [ ] Outcome measures include quality, compliance, timeliness, and user experience where relevant
- [ ] Gain-share or innovation mechanisms include measurement, caps, and governance
- [ ] Risk contingency adequate for delivery model and KPI exposure
- [ ] Service credits, penalties, and bonuses tested for perverse incentives
- [ ] Discount strategy justified and approval path identified
- [ ] TCO and value case completed for value-based proposals
- [ ] Sensitivity analysis performed
- [ ] Negotiation guardrails defined: opening, target, walkaway, ZOPA, BATNA, and WATNA
- [ ] Concessions are conditional and tied to client gives
- [ ] Tradeables considered before discounting
- [ ] Pricing assumptions, dependencies, and exclusions documented clearly
- [ ] Pricing narrative aligns with win themes and client hot buttons

## Common Pitfalls To Avoid

1. Treating rate cards as the value story when outcomes matter more.
2. Designing outcome pricing without reliable baselines or data quality.
3. Rewarding suppliers for activity while asking them to automate activity away.
4. Creating KPIs that can be gamed or that conflict with statutory duties.
5. Underpricing transition, dual-running, governance, and reporting.
6. Omitting innovation funding, then expecting continuous improvement.
7. Discounting price before testing non-price commercial levers.
8. Ignoring service credit exposure in managed service models.
9. Presenting a complex pricing model that the buyer cannot govern.
10. Failing to show how savings are reinvested or shared.
11. Entering negotiation without a defined walkaway point, ZOPA, or concession plan.
12. Giving unilateral concessions without a linked client commitment.

## Integration With Other Skills

This skill works best combined with:

- `ibm-bid-staffing-planner`: Baseline labour cost, delivery duration, and gross profit assumptions
- `ibm-bid-solution-architect`: Solution scope, technical dependencies, and delivery risk
- `ibm-bid-strategic-positioning`: Competitive intelligence and price-to-win context
- `ibm-business-case-creator`: Client-side ROI, TCO, and value case
- `xlsx`: Detailed pricing models and scenarios
- `docx` / `ibm-bid-writer`: Proposal pricing narrative and approval documents

**Output:** Comprehensive pricing strategy with recommended commercial model, internal cost baseline, margin analysis, client value case, risk-adjusted pricing, and approval-ready narrative.
