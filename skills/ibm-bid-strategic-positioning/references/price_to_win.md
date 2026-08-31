# Price to Win Framework

## What is Price to Win?

Price to Win is a **top-down pricing approach** that estimates what the client expects to pay, rather than what our solution costs to deliver. It's fundamentally different from traditional bottom-up cost-plus pricing.

**Key principles:**
- Starts from client budget expectations, not our costs
- Looks outward (client, market, competitors) not inward (our delivery model)
- Creates constraint for solution design, not afterthought
- Informs entire bid strategy from Phase 0 onwards
- Best performed independently from deal team to avoid bias

## Why Price to Win Matters

**Common bid failures it prevents:**
- **"Rolls Royce" proposals**: Over-engineered solutions that exceed client budget expectations
- **Late-stage panic cuts**: Rushed solutioning reductions that increase delivery risk and damage credibility
- **Margin erosion**: Late price cuts that destroy profitability to win
- **Unwinnable pricing**: Pricing so far from client expectations we're eliminated early

**Value it provides:**
- Early GO/NO-GO signal: If Price to Win doesn't support margins, NO-GO before investment
- Solution guardrails: Bounds for solution design throughout proposal development
- Competitive intelligence: Understanding where competitors likely to price
- Credibility with client: Pricing that reflects their budget reality, not our wish list

## Five Viewpoints Framework

Price to Win must consider multiple perspectives. Relying on only one or two viewpoints produces unreliable estimates.

### 1. Value Viewpoint

**Question**: What is a fair price for the value we're delivering?

**Key inputs:**
- Value case: Quantified benefits to client (cost savings, revenue generation, risk reduction)
- ROI/TCO proposition: Return on investment and total cost of ownership analysis
- Cost structure: Client's current spend and cost base
- Fair pricing: What's reasonable given value delivered

**Analysis approach:**
- Quantify client benefits (e.g., "will save £2M per year in operational costs")
- Calculate ROI (e.g., "3-year contract at £4M delivers £6M savings = 150% ROI")
- Compare to client's current spend (e.g., "currently spending £1.5M/year, we're proposing £1.3M/year")
- Determine fair value capture (typically 20-40% of value created)

**Example:**
```
Client operational savings: £2M/year over 3 years = £6M total
Fair value capture (30%): £1.8M
Contract term: 3 years
Price to Win (Value viewpoint): £1.8M (£600K/year)
```

### 2. Market Viewpoint

**Question**: What does the market pay for similar solutions?

**Key inputs:**
- Win/loss analysis: Our historical pricing for similar deals (won vs. lost)
- Competitive benchmarking: Known competitor pricing for similar scopes
- Industry benchmarks: Sector-specific pricing norms (e.g., £X per user, Y% of current spend)
- Deal retrospectives: Lessons from similar opportunities

**Analysis approach:**
- Search ibm-bid-library for similar deals (sector, size, scope)
- Note: pricing on deals won vs. lost (what was acceptable, what was too high)
- Research sector benchmarks (e.g., Gartner, public procurement databases)
- Adjust for scope differences (scale, complexity, risk)

**Example:**
```
Similar NHS deals (3-year, regional scope):
- Won at £500-600/user/year
- Lost when priced >£700/user/year
- This opportunity: 3000 users
Market viewpoint Price to Win: £1.5-1.8M (£500-600/user/year)
```

### 3. Client Viewpoint

**Question**: What can/will the client actually pay?

**Key inputs:**
- Business case dialogue: Client's internal business case and budget approval
- Current spend: What they pay now for similar services/technology
- Contract value indicators: Budget range signals in tender or pre-sales
- Opening negotiation point: Where client expects to start price discussion

**Analysis approach:**
- Identify budget signals in tender (explicit or implicit)
- Research client's public spending (UK: Contracts Finder, USA: USASpending.gov)
- Note client's financial constraints (e.g., "budget pressures", "value for money" emphasis)
- Estimate available budget (often: current spend +/- 20%)

**Example:**
```
Current supplier contract (public data): £1.2M/year
Contract term: 3 years
Tender emphasis: "value for money", "constrained budgets"
Client viewpoint Price to Win: £3.0-3.6M (£1.0-1.2M/year, slightly below current)
```

### 4. Competitive Viewpoint

**Question**: What will competitors price, and how can we position?

**Key inputs:**
- Competitor price estimates: Known pricing models of likely bidders
- Onshore/offshore ratios: Cost structure advantages/disadvantages
- Historical win-loss: Competitive pricing intelligence from past bids
- Pricing strategy: Top-down vs. bottom-up (are they also doing Price to Win?)

**Analysis approach:**
- Identify likely bidders from requirements analysis
- Estimate their cost structures (e.g., Accenture: 40% offshore, us: 60% offshore)
- Research their historical pricing (ibm-bid-library, market intelligence)
- Determine if we need to price below, at, or above competitors (depends on sales strategy)

**Example:**
```
Likely bidders:
- Accenture: 40% offshore, likely £2.5-3M (higher cost base)
- Capgemini: 50% offshore, likely £2.0-2.5M (competitive)
- Tech vendor (Salesforce): License-heavy model, likely £1.8M+ annual licenses

Our offshore ratio: 60%
Our cost advantage: ~20% below Accenture
Competitive viewpoint Price to Win: £2.0-2.2M (below Accenture, match Capgemini)
```

### 5. Deal Team Viewpoint

**Question**: What's the highest price we believe the client will accept?

**Key inputs:**
- Estimated highest acceptable price: Deal team's assessment from client interactions
- RFP scope and scoring: How price weighs against quality/technical
- Budget intelligence: Any specific budget information from pre-sales
- Client sophistication: Procurement maturity and negotiating capability

**Analysis approach:**
- Gather deal team assessment (account manager, pre-sales, delivery leads)
- Weight by price scoring (e.g., if price is 40% of evaluation, pricing is critical)
- Consider client procurement sophistication (experienced buyers vs. first-time)
- Factor in relationship strength (strong relationship = some price tolerance)

**Example:**
```
Deal team assessment:
- Account manager: "Client has £4M approved, won't go higher"
- Pre-sales: "They're price-sensitive but value quality"
- Price weighting in tender: 30% (quality 60%, social value 10%)

Deal team viewpoint Price to Win: £3.5-4.0M (client's approved budget range)
```

## Synthesizing the Five Viewpoints

After analyzing all five viewpoints, synthesize into a single Price to Win estimate:

**Step 1: Document all viewpoints**
```
Value viewpoint:        £1.8M
Market viewpoint:       £1.5-1.8M
Client viewpoint:       £3.0-3.6M
Competitive viewpoint:  £2.0-2.2M
Deal team viewpoint:    £3.5-4.0M
```

**Step 2: Identify outliers and understand why**
```
Client and Deal Team viewpoints are higher (£3-4M range)
→ May have larger budget than market norms suggest
→ Or may be willing to pay premium for quality/risk reduction

Value and Market viewpoints are lower (£1.5-2M range)
→ Market benchmark pricing is competitive
→ Value delivered doesn't justify premium pricing
```

**Step 3: Weight viewpoints by reliability**
```
Client viewpoint: HIGH reliability (have budget intelligence)
Competitive viewpoint: MEDIUM reliability (estimates, not confirmed)
Market viewpoint: MEDIUM reliability (similar but not identical deals)
Deal team viewpoint: MEDIUM reliability (based on relationship, but subjective)
Value viewpoint: LOW reliability (depends on client's value perception)
```

**Step 4: Determine Price to Win range**
```
Preliminary Price to Win: £2.5-3.0M
Rationale:
- Client has budget up to £4M (client viewpoint)
- Market pricing is £1.5-1.8M, but client may pay premium for quality
- Competitive pricing is £2.0-2.2M (we can price slightly above if differentiated)
- Balance: Price above market to fund quality, below client budget to show value
```

**Step 5: Calculate Total Allowable Cost**
```
Price to Win: £2.5-3.0M
Target margin: 20%
Total Allowable Cost: £2.0-2.4M

→ This is the cost envelope for solution design
→ If solution can't be delivered within this, revisit Price to Win or NO-GO
```

## Iterative Price to Win Process

Price to Win is not a one-time analysis. Update as new information emerges:

**Phase 0 (Opportunity Assessment):**
- Initial Price to Win based on tender document and pre-sales intelligence
- Wide range acceptable (e.g., £2-4M)
- Primarily uses Market, Competitive, and Value viewpoints

**Phase 1 (Strategic Positioning):**
- Refined Price to Win after clarifications and client dialogue
- Narrower range (e.g., £2.5-3.0M)
- Adds Client and Deal Team viewpoints

**Phase 2 (Solution Development):**
- Validated Price to Win with preliminary solution costing
- Tight range (e.g., £2.7-2.9M)
- Confirms Total Allowable Cost is achievable

**Phase 3 (Response Writing):**
- Final Price to Win before submission
- Single point estimate (e.g., £2.8M)
- Reflects all information including competitive intelligence

## Red Flags and Warning Signs

**Warning sign**: Wide divergence between viewpoints (e.g., 2x difference)
→ Need more information, or opportunity may be poorly defined

**Warning sign**: Price to Win doesn't support required margins
→ Early GO/NO-GO signal - can we win profitably?

**Warning sign**: Deal team viewpoint much higher than others
→ May be over-optimistic about client budget or relationship

**Warning sign**: Competitive viewpoint much lower than client budget
→ Competitors may have cost advantage we can't match

**Warning sign**: Client tender emphasizes "value for money" but budget seems high
→ May be room for budget cuts after award (risk factor)

## Using Price to Win for Solution Design

Price to Win creates guardrails for solution development:

**Total Allowable Cost**: Price to Win minus desired margin
→ This is the maximum cost for delivery

**Solution design process:**
1. Start from Total Allowable Cost (not unconstrained "best solution")
2. Allocate cost across solution components (technology, services, support)
3. Make explicit trade-offs (e.g., more offshore, less customization)
4. Validate that solution delivers required value within cost envelope
5. If cost exceeds Total Allowable Cost: revisit scope, efficiency, or Price to Win

**Example:**
```
Price to Win: £3.0M
Target margin: 20%
Total Allowable Cost: £2.4M

Solution breakdown:
- Software licenses: £600K (25%)
- Implementation services: £1,200K (50%) - 60% offshore to manage cost
- Support (3 years): £400K (17%)
- Training & change: £200K (8%)
Total: £2.4M ✓

If bottom-up costing was £3.0M (pre-Price to Win):
→ Reduce customization, increase offshore ratio, simplify change program
→ NOT: cut solution quality in panic at end
```

## Documentation Template

Document your Price to Win analysis for deal team review:

```markdown
# PRICE TO WIN ANALYSIS: [CLIENT NAME]

## Executive Summary
**Recommended Price to Win**: £X.X - X.XM
**Confidence level**: High/Medium/Low
**Key constraint**: [e.g., "Client budget", "Competitive pressure", "Market benchmark"]

## Five Viewpoints Analysis

### 1. Value Viewpoint: £X.XM
[Rationale, calculations, assumptions]

### 2. Market Viewpoint: £X.XM
[Comparable deals, benchmarks, sources]

### 3. Client Viewpoint: £X.XM
[Budget intelligence, current spend, constraints]

### 4. Competitive Viewpoint: £X.XM
[Likely bidders, pricing estimates, our position]

### 5. Deal Team Viewpoint: £X.XM
[Team assessment, relationship factors, intelligence]

## Synthesis
[How viewpoints were weighted, rationale for final range]

## Total Allowable Cost
**Price to Win**: £X.XM
**Target margin**: X%
**Total Allowable Cost**: £X.XM
→ Solution must be delivered within this cost envelope

## Assumptions & Risks
- [Assumption 1 and risk if wrong]
- [Assumption 2 and risk if wrong]

## Update Plan
- Phase 1: Refine after clarifications and client dialogue
- Phase 2: Validate against preliminary solution costing
- Phase 3: Finalize before submission
```
