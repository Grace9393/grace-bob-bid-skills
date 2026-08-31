---
name: ibm-bid-executive-summary
description: Write executive summaries for IBM tender and proposal responses. Use when asked to write, draft, or create an executive summary for a bid, tender, proposal, or RFP response. Produces compelling, client-focused summaries (typically 1000 words/2 pages max) using a four-part structure that highlights client outcomes and IBM differentiators. Works with ibm-bid-requirements-analysis for client context, ibm-bid-win-themes for strategic messaging, and ibm-bid-strategy-and-capabilities-2026 for IBM capabilities.
metadata:
  skills-required:
    - ibm-bid-requirements-analysis
    - ibm-bid-win-themes
  skills-suggested:
    - ibm-bid-strategic-positioning
    - ibm-bid-hot-buttons
---

# IBM Executive Summary Skill

## Context Management

Write output to `./tmp/ibm-bid-executive-summary.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `executive_summary_status: complete`
- `executive_summary_artifact: ./tmp/ibm-bid-executive-summary.md`
- `artifacts_generated`: include `./tmp/ibm-bid-executive-summary.md` when the artifact is written
- `next_skill_recommendation`: normally `ibm-bid-wireframe-creator`, `ibm-bid-writer`, or the relevant solution architecture skill

Write compelling executive summaries for IBM tender responses that are client-focused, differentiated, and persuasive.

When `./tmp/ibm-bid-approved-customer-stories.md` exists, treat it as the controlled customer-evidence pool. Do not introduce customer stories outside that approved file unless the shortlist has been explicitly refreshed after review.

## Key Principles

**Write it first, not last!**
Draft the executive summary early in the bid process—it guides the bid team and clarifies strategy. A hastily prepared summary written before the deadline is rarely effective.

**Always write one**
Even if not requested, an executive summary outlines the main themes of your proposal strategy. It serves as an excellent guide for the bid team.

**Follow client instructions**
If the client specifies content, length, or format requirements, follow them exactly. Not doing so suggests you aren't listening.

**Appropriate length**
Typically no more than two pages (~1000 words) unless for very large bids. For longer summaries, use subheadings for navigation. For shorter requirements, aim for 350 words.

## Four-Part Structure

Executive summaries use a customer-first structure:

### Headline

A short, attention-grabbing statement describing the outcome for the client. This is the theme statement that captures your value proposition.

### Part 1: Client Understanding

Play back understanding of what the client is trying to achieve:
- Reference the client's objectives, goals, and challenges
- Demonstrate that you understand their situation
- Show you've listened to their needs

### Part 2: Compliance and Hot Buttons

- Confirm compliance with requirements
- Introduce the "hot buttons" important to decision makers (typically 3-5 per deal)
- Don't mention IBM or your solution yet—focus on what matters to them

### Part 3: Solution and Differentiators

Address each hot button one by one:
- Describe how the solution addresses each hot button
- Focus on value and benefit to the client
- Position IBM's differentiators
- Provide proof through experience and performance

### Part 4: Value Proposition and Next Steps

- Summarise the overall value proposition and benefits
- Show forward thinking beyond the ITT
- Describe next steps to demonstrate proactive engagement

## Writing Guidelines

**Tone:**
- Confident but not arrogant
- Compelling and insightful
- Professional and direct
- Natural, fluent language (not corporate speak)

**Persuasive techniques:**
- Present ideas according to customer priorities
- Group similar ideas together
- Start with the most important items first
- Use headings to guide readers
- Keep setups short

**Language standards:**
- British English spelling (realise, colour, programme)
- Precise, engaging phrasing
- Active voice

**Banned words (overcommitment):**
- ensures, guarantees, assures, commits
- Use alternatives: "enables", "delivers", "provides", "supports"

**Anti-AI style:**
- Avoid: delve, leverage, robust, nuanced, multifaceted, paramount
- No flowery transitions: "Furthermore", "Moreover", "It's worth noting"
- No jargon: streamline, optimise, cutting-edge, best-in-class, seamlessly

## Common Pitfalls to Avoid

**Don't confuse with the cover letter**
Executive summaries should not contain:
- Greetings or signatures
- Polite nothings ("thank you for allowing us to prove our abilities")
- Marketing copy or generic clichés ("we put the customer first")

**Don't write it just for executives**
Target both senior decision-makers and evaluation team members.

**Don't focus on IBM throughout**
Avoid constant "IBM will..." or "we will..." statements. Focus on the client and what the solution delivers for them.

**Don't rush it at the end**
Write and review early to create the best product possible.

**Don't confuse with table of contents**
Eliminate navigation statements like "you will find the technical description in Chapter 3."

**Don't add corporate history**
The executive summary is not the place for IBM's corporate history.

## Quality Checklist

Before finalising:
- [ ] Follows client-specified requirements (if any)
- [ ] Uses four-part structure (understanding → hot buttons → solution → value)
- [ ] Client-focused throughout (not IBM-focused)
- [ ] Each hot button addressed with value and proof
- [ ] IBM differentiators positioned clearly
- [ ] Appropriate length (typically max 2 pages/1000 words)
- [ ] British English spelling used throughout
- [ ] No overcommitment words
- [ ] No banned AI-style words or transitions
- [ ] Tone is confident, compelling, and specific
- [ ] Claims are substantiated with proof points
- [ ] Next steps included to show forward thinking

## Complete Tender Response Workflow

This skill is part of the 5-phase IBM Bid Management workflow.

**Current Phase**: Phase 1 (Strategic Positioning)
**Position**: Sequential execution - must run AFTER ibm-bid-win-themes

**When to use**: Only when RFP requires executive summary or narrative section
**When to skip**: Strict Q&A format RFPs, very small bids (<£250K)

See ibm-bid-navigator for complete workflow guidance.

## Integration with Other Skills

### Required Inputs

**Phase 0 outputs**:
- **ibm-bid-requirements-analysis**: ./tmp/ibm-bid-requirements-analysis.md (client profile, requirements, underlying needs)
  - Uses for Part 1: Client understanding - play back what client is trying to achieve
  - Uses for Part 2: Hot buttons - identify what matters to decision makers
- **ibm-bid-strategic-positioning**: ./tmp/ibm-bid-strategic-positioning.md (strategic positioning, transformation assessment)
  - Uses for Part 2: Understanding executive decision drivers
  - Uses for Part 3: Strategic approach and positioning

**Phase 1 outputs** (required):
- **ibm-bid-win-themes**: ./tmp/ibm-bid-win-themes.md (3-7 Shipley-compliant win themes)
  - CRITICAL: Executive summary MUST incorporate all win themes
  - Uses for Part 3: Solution and differentiators - each hot button maps to a win theme
  - Sequential dependency: Cannot write executive summary without win themes
- **Approved customer stories**: ./tmp/ibm-bid-approved-customer-stories.md (approved 3-5 story subset after review)
  - CRITICAL: If this file exists, executive-summary proof points must come only from this approved subset
  - Uses for Part 3: Proof points and quantified outcomes

**IBM Knowledge Bases**:
- **ibm-bid-customer-stories**: 857 customer success stories (FTS5 search)
  - Use for Part 3: Proof points and quantified outcomes
  - Search by: Industry, Salesforce cloud, challenge type
  - Example: "government Sales Cloud", "NHS Service Cloud"

- **ibm-bid-strategy-and-capabilities-2026**: IBM 2026 strategy and capabilities
  - Use for Part 3: IBM differentiators and capabilities
  - Reference: AI capabilities, Client Zero story, Salesforce partnership

### Recommended Next Steps

**After executive summary complete:**

1. **Review and validate**:
   - Check all win themes incorporated from ./tmp/ibm-bid-win-themes.md
   - Verify length appropriate (typically ≤2 pages/1000 words)
   - Confirm four-part structure followed
   - Validate British English spelling
   - Check no overcommitment words or AI-style language
   - Confirm any customer story references come only from `./tmp/ibm-bid-approved-customer-stories.md` when that file exists

2. **Proceed to Phase 2 or Phase 3**:

   **If technical bid** (Salesforce, infrastructure, cloud, cybersecurity):
   - Phase 2: Solution Architecture
     - **ibm-sf-solution-architect** (for Salesforce implementations)
     - **ibm-bid-solution-architect** (for non-Salesforce implementations)
   - Then Phase 3: Content Development

   **If non-technical bid** (professional services, framework, capability statements):
   - Skip Phase 2
   - Phase 3: Content Development
     - **ibm-bid-writer** (draft responses per question)
     - **ibm-bid-answer-evaluator** (quality check)

3. **Maintain consistency throughout**:
   - All Phase 3 responses should align with executive summary messaging
   - Win themes in executive summary must be woven into all detailed responses
   - Hot buttons identified in executive summary should be addressed in responses

### Supporting Resources

**Throughout executive summary development:**
| Resource | Purpose | Usage |
|----------|---------|-------|
| **ibm-bid-customer-stories** | Candidate proof points before approval | FTS5 search by industry/cloud/outcome |
| **./tmp/ibm-bid-approved-customer-stories.md** | Controlled proof points for downstream use | Use only approved stories when the file exists |
| **ibm-bid-strategy-and-capabilities-2026** | IBM differentiators for Part 3 | Reference capabilities and competitive positioning |
| **ibm-bid-library** | Historical executive summaries | FTS5 search for similar client types or industries |

### This Skill Feeds Downstream Skills

Executive summary (./tmp/ibm-bid-executive-summary.md) is consumed by:

**Phase 3**:
- ibm-bid-writer (detailed responses must align with executive summary hot buttons and messaging)
- Critical: Responses should elaborate on themes introduced in executive summary

**Phase 4**:
- ibm-bid-answer-evaluator (validates consistency between executive summary and detailed responses)

**Oral Presentations** (if required):
- ibm-story-pitch-development (executive summary becomes foundation for oral presentation)
- ibm-story-presentation-structuring (hot buttons from executive summary structure presentation)

**Final Submission**:
- Copy to ./outputs/executive_summary.docx for final submission package

### Four-Part Structure Mapping to Other Skills

**Part 1: Client Understanding**
- Source: ./tmp/ibm-bid-requirements-analysis.md (client profile, objectives, challenges)
- Play back: What client is trying to achieve
- Demonstrates: We've listened and understand their situation

**Part 2: Compliance and Hot Buttons**
- Source: ./tmp/ibm-bid-requirements-analysis.md (evaluation criteria, requirements)
- Source: ./tmp/ibm-bid-strategic-positioning.md (executive decision drivers)
- Identify: 3-5 hot buttons important to decision makers
- Focus: What matters to them (not IBM yet)

**Part 3: Solution and Differentiators**
- Source: ./tmp/ibm-bid-win-themes.md (each hot button maps to a win theme)
- Source: ./tmp/ibm-bid-approved-customer-stories.md when available
- For each hot button:
  - Describe how solution addresses it (from win themes)
  - Focus on value and benefit to client
  - Position IBM differentiators
  - Provide proof from the approved customer story file when it exists, otherwise from ibm-bid-customer-stories

**Part 4: Value Proposition and Next Steps**
- Source: Synthesize from Parts 1-3
- Summarize: Overall value proposition and benefits
- Forward thinking: Beyond the ITT
- Next steps: Demonstrate proactive engagement

### Timing: Write Early, Not Last

**Best practice**: Write executive summary after win themes but BEFORE detailed responses
- Guides bid team on strategic direction
- Clarifies hot buttons and positioning early
- Ensures consistency across all responses
- Allows time for review and refinement

**Anti-pattern**: Writing executive summary just before submission deadline
- Results in rushed, ineffective summary
- Misses opportunity to guide bid team
- Creates inconsistency with detailed responses

### Quality Gate Integration

Executive summary quality impacts both gates:

**Quality Gate 1 (GO/NO-GO)**:
- Strong executive summary validates GO decision (clear value proposition)
- Inability to articulate compelling executive summary suggests weak positioning (reconsider bid)

**Quality Gate 2 (Technical Assurance)**:
- Final evaluation checks consistency between executive summary and detailed responses
- Hot buttons in executive summary must be addressed throughout tender responses
- Win themes in executive summary must be woven into all responses
