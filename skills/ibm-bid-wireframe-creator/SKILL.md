---
name: ibm-bid-wireframe-creator
description: Structure proposal responses for public sector clients by decomposing procurement questions into "How we..." sub-headings and mapping win themes and hot buttons to each section. Use when responding to formal procurement questions, structuring complex public sector proposals, planning bid writing assignments for IBM teams, or aligning technical responses to client priorities.
metadata:
  skills-required:
    - ibm-bid-hot-buttons
    - ibm-bid-win-themes
  skills-suggested:
    - ibm-bid-requirements-analysis
    - ibm-bid-image-definer
    - ibm-bid-word-count
---

# IBM Bid Wireframe Creator

## Mandatory Context Loading

**Before generating any wireframe, read these files in order:**

1. `./tmp/ibm-bid-requirements-analysis.md` - full bid context, client profile, strategic analysis, evaluation model, digital maturity
2. `./tmp/ibm-bid-requirements-extractor.md` - full question text, sub-requirements, response constraints, and diagram/image limits for each question (Q1-Q8)
3. `./tmp/ibm-bid-hot-buttons.md` - Ofgem's five hot buttons with detail and response suggestions
4. `./tmp/ofgem-crm-win-themes.md` - IBM win themes with proof points and differentiators
5. `./tmp/ibm-bid-customer-stories.md` - candidate customer stories pool

Do not ask the user to supply hot buttons, win themes, or question text - load them from these files. If a file is missing, flag it and proceed with what is available.

**Question lookup:** When the user provides a question number (e.g. "Q3" or "Question 4"), extract the full question text and all sub-requirements from `ibm-bid-requirements-extractor.md`. Also read its `Response Constraints` and `Diagram / Image Limits` sections. Use the word limit, weighting, and any stated diagram/image/figure/table allowance or requirement to calibrate response depth and visual planning.

## Context Management

Write output to `./tmp/ibm-bid-wireframe-Q0X.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

When evaluating multiple questions in a tight loop, `./tmp/q[N]_wireframe.md` is also acceptable if the workflow already uses that naming. Keep one consistent pattern per bid.

Update state checkpoint: `./tmp/ibm-bid-project.md` with wireframe completion status, generated artifacts, and next skill recommendation.

## Input Requirements

The only required input is the question identifier (e.g. "Q1", "Q3", or the full question text if not in the extractor). Everything else is loaded automatically from `./tmp/`.

Optionally, the user may provide:
- **Approved Customer Stories**: a shortlist from the pool in `./tmp/ibm-bid-customer-stories.md` - if not provided, propose the most relevant from the pool and note they are unconfirmed

## Output Structure

Generate two parts:

### Part 1: Sub-Headings

Bullet list format:
- First bullet: "How we've structured our response"
- Subsequent bullets: "How we [verb phrase from question]"
- Order matches question sequence
- No introduction or conclusion headings

### Part 2: Strategic Mapping

For each sub-heading:
```
Subheading: [text]
• Relevant Hot Button(s): [list]
• How can these be described in the written response: [guidance]
• Relevant Win Theme(s): [list]
• How can these be described in the written response: [guidance]
• Approved Customer Story(ies): [story ID/title from approved shortlist only, or "None"]
• How can these be described in the written response: [guidance on where the shortlisted proof strengthens the section]
• Client diagram requirement: [stated requirement/allowance from client documents, or "Not stated"]
• Diagram recommendation: [Use diagram / No diagram]
• Diagram count: [0 / 1 / 2]
• Diagram type(s): [e.g. operating model, lifecycle, architecture, stakeholder model, evidence panel, or "None"]
• Diagram word count treatment: [Included / Excluded / Confirm]
• Diagram word count evidence: [source section/page/row from extractor or client document, or "Not stated"]
• How the diagram should be used: [where it should sit, what it should clarify, and any source-support checks]
```

### Part 3: Diagram Summary

End every wireframe with a short diagram summary:

```
## Diagram Summary
- Recommended diagrams: [total number]
- Client diagram requirement: [summary of stated requirement/allowance by answer]
- Diagram word count treatment: [Included / Excluded / Confirm]
- Diagram word count evidence: [source section/page/row, or "Not stated"]
- Candidate diagrams:
  - [Subheading]: [diagram type] - [one-line purpose] - [Included/Excluded/Confirm] - [evidence]
- Follow-on skill: [Use `ibm-bid-image-definer` only if diagram prompts or artwork briefs are needed]
```

## Processing Rules

### Strategic Framing (from Requirements Analysis)

Before mapping sub-headings, internalise the strategic context from `ibm-bid-requirements-analysis.md`:
- This is a **capacity play** in a **dual-supplier model** - Ofgem wants a partner that slots in, not disrupts
- Evaluation is 80% technical / 20% commercial - quality of response is paramount
- Scoring: Excellent (5) -> Fail (0); rejection if any question scores <=1, or two questions score <=2
- Ofgem is 24 months in with an established CoE - responses must respect their maturity, not lecture them
- First delivery won't start until September 2026 - mobilisation capability matters

Use this context to sharpen the "How can these be described" guidance for every sub-heading.

### Sub-Heading Creation

1. Extract distinct question components from `ibm-bid-requirements-extractor.md` for the question
2. Convert to "How we..." format
3. Maintain logical flow matching the question's sub-requirement order
4. Reference question language directly
5. Omit generic intro/conclusion sections

### Hot Button Integration

- Load all five hot buttons from `./tmp/ibm-bid-hot-buttons.md`
- Select the most relevant button(s) per sub-heading - do not force all five into every section
- Use the "Response suggestion" text in the hot buttons file to inform the "How can these be described" guidance
- Link to Ofgem's evaluation criteria and client language

### Win Theme Integration

- Load win themes from `./tmp/ofgem-crm-win-themes.md`
- Map themes to sub-headings where IBM's differentiator directly answers Ofgem's challenge
- Use the proof points and IBM differentiators from the win themes file to inform the "How can these be described" guidance
- Connect each theme back to Ofgem's specific context (regulated environment, CoE maturity, dual-supplier model)

### Approved Customer Story Integration

- Draw from `./tmp/ibm-bid-customer-stories.md` as the candidate pool
- If the user has not provided a confirmed shortlist, propose the most relevant stories and label them `[Proposed - confirm before use]`
- Map stories only where they materially strengthen a section
- Prefer the smallest number of stories needed across the response to avoid evidence sprawl
- If no story fits a sub-heading well, mark `None` rather than forcing a weak match
- Never invent, expand, or swap customer story details

### Diagram Recommendation

For every sub-heading, state whether the drafted response should use a diagram. Do not leave this implicit.

- First check `./tmp/ibm-bid-requirements-extractor.md`, especially the `Response Constraints` and `Diagram / Image Limits` sections, for the stated number of diagrams, images, figures, graphics, visuals, tables, or exhibits required or allowed for the answer. Treat this extracted guidance as the primary source for diagram count.
- Apply question-specific limits before global limits. If a row exists for the requested question, use it. If only a global `All` row exists, apply that global rule to the answer and state that it is a global constraint.
- If the extractor marks the relevant limit as `Not stated`, say so in `Client diagram requirement` and then use judgement within the fallback rules below.
- If the client specifies a diagram count, use that count in the wireframe and distribute diagrams across the sub-headings where they create the most evaluator value. Do not override the stated count unless there is an explicit conflict in the tender documents; if there is a conflict, flag it.
- If the client says diagrams are optional or gives a maximum count, recommend the smallest useful number within that allowance.
- If the client prohibits diagrams or states that only prose is permitted, set the diagram count to `0` and mark every sub-heading as `No diagram`.
- If no diagram count is stated, recommend the smallest useful number. Most tender answers should use `0` or `1`; use `2` only when the question covers two genuinely distinct complex concepts. Do not exceed `2` diagrams for a single answer unless the user or tender explicitly asks for more.
- Recommend a diagram only where it will make complex content easier for evaluators to scan, compare, or trust. Strong candidates include operating models, process lifecycles, architecture or integration flows, governance models, stakeholder/responsibility maps, timelines, value maps, and evidence panels.
- Do not recommend diagrams for simple narrative sections, unsupported claims, generic value statements, or content that would duplicate clear prose.
- Name the recommended diagram type using the taxonomy from `ibm-bid-image-definer` where possible: operating model, journey or lifecycle, architecture or integration, value map, before/after, evidence panel, timeline, or stakeholder model.
- Describe what the diagram should show at concept level only. Do not write full AI image prompts in the wireframe; recommend `ibm-bid-image-definer` as the next skill if prompts or artwork briefs are needed.
- Every visual element must be traceable to the question, requirements analysis, win themes, hot buttons, or approved customer-story evidence. If support is weak, mark the diagram as "No diagram" or flag the source check required.

### Diagram Word Count Treatment

Every diagram recommendation must state whether the diagram is expected to count toward the tender word limit. This is a required handoff to `ibm-bid-writer`.

- Use the exact field name `Diagram word count treatment` in both the per-subheading mapping and the final `Diagram Summary`.
- The value must be exactly one of: `Included`, `Excluded`, or `Confirm`. Do not write alternatives such as "likely excluded", "probably included", "n/a", "unknown", or "confirm with tender instructions".
- Include `Diagram word count evidence` immediately after the treatment field. Cite the source section/page/row from `./tmp/ibm-bid-requirements-extractor.md`, the client document, or write `Not stated`.
- Default to `Excluded` when the diagram will be inserted as markdown image syntax or as a separate figure/artwork object. The IBM bid word-count script removes markdown images from the count.
- Use `Included` when the tender instructions state that text in figures, captions, tables, graphics, or appendices counts toward the word limit, or when the diagram is represented as evaluator-facing typed text inside the answer rather than as an image.
- Use `Confirm` when the source documents do not say whether figure labels, captions, callouts, or diagram text count, or when extracted sources conflict. In that case, advise the writer to keep diagram labels short and assume captions may count until confirmed.
- If diagram labels are likely to count, note that label text should be budgeted within the section word allocation and kept concise.
- If a diagram is recommended but excluded from the word count, still warn that captions, figure titles, or surrounding explanatory prose may count depending on the tender rules.

## Constraints

- Never invent hot buttons or win themes - always load from source files
- Never invent, expand, or swap customer story details
- Never leave diagram usage or diagram word-count treatment unstated
- British English only
- Target internal bid writing teams
- Professional, structured tone
- Focus on selling value against Ofgem's specific needs, not generic IBM capability
- Respect Ofgem's CoE maturity - frame IBM as augmenting capability, not building it from scratch
- Reflect dual-supplier context - responses must convey partnership maturity and governance alignment

## Example Sub-Headings

- How we will lead and manage delivery with multiple stakeholders and resources
- How we will manage comprehensive knowledge transfer with minimal disruption to service quality
- What technical skills and capabilities we will bring whilst keeping pace with market trends

## Error Handling

Request clarification if:
- No question number or text provided
- Question number not found in `ibm-bid-requirements-extractor.md`
- A required context file (`ibm-bid-requirements-analysis.md`, `ibm-bid-hot-buttons.md`, `ofgem-crm-win-themes.md`) cannot be read
- Conflicting requirements between files

Do **not** request clarification for hot buttons, win themes, or customer stories - read them from files first.
