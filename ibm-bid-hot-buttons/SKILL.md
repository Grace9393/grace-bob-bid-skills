---
name: ibm-bid-hot-buttons
description: Extract 5 client Hot Buttons from government procurement documents (RFPs, ITTs, tenders) and combine with known client context to inform bid response strategy. Use when analysing procurement materials to identify client motivations, pain points, and strategic concerns for public sector proposals.
metadata:
  skills-required:
    - ibm-bid-requirements-analysis
  skills-suggested:
    - ibm-bid-strategic-positioning
---

# IBM Bid Hot Buttons

Extract 5 client Hot Buttons from procurement documents. A Hot Button is a concise client motivation or core issue driving their supplier request.

## Context Management

Write output to `./tmp/ibm-bid-hot-buttons.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `hot_buttons_status: complete`
- `hot_buttons_artifact: ./tmp/ibm-bid-hot-buttons.md`
- `key_client_priorities`: the 5 extracted hot buttons
- `artifacts_generated`: include `./tmp/ibm-bid-hot-buttons.md` when the artifact is written
- `next_skill_recommendation`: normally `ibm-bid-win-themes` or `ibm-bid-wireframe-creator`

## Process

1. Read the procurement document thoroughly
2. Identify exactly 5 Hot Buttons from client statements, requirements, and context
3. Integrate any additional client information provided
4. Structure each as first-person client voice with response guidance

## Constraints

- Extract exactly 5 Hot Buttons
- Use only information from provided documents and context
- Write Hot Buttons in first person as client statements
- Maintain professional tone
- No repetition or filler content
- British English only

## Output Structure

For each Hot Button (numbered 1-5):

**Hot Button**: [First-person client statement expressing motivation or concern]

**Additional detail**: [Supporting evidence from procurement document]

**Response suggestion**: [How to address this in the proposal]

## Examples

**Hot Button**: "I must be able to increase the reliability of the service for my end users, to avoid disrupting their day-to-day working."

**Hot Button**: "I need to be able to demonstrate a return of investment for this solution with clear benefits and value articulated."

**Hot Button**: "I want to reduce my yearly spend in marketing."
