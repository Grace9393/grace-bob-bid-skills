---
name: ibm-bid-image-definer
description: "Define, recommend, and write AI-ready image-generation prompts for IBM bid, tender, proposal, or case-study documents. Use whenever a user: (1) has drafted or is reviewing a bid answer, proposal section, case study, or RFP response and wants to know what images or diagrams would strengthen it; (2) asks for AI image prompts, diagram concepts, or visual ideas for any proposal or tender; (3) provides a document path or pasted text and asks for a specific number of supporting visuals; (4) wants to visualise a service transformation, operating model, technology architecture, timeline, or value story in a procurement context. Trigger even if the user does not mention \"IBM style\" or \"image prompts\" explicitly — apply IBM visual style by default whenever the context is a bid or proposal document."
metadata:
  skills-suggested:
    - ibm-bid-answer-evaluator
---

# IBM Bid Image Definer

## Context Management

Write output to `./tmp/ibm-bid-image-definer.md` when the user asks for a persisted artefact or when chaining into drafting, design, or presentation work. Keep responses inline by default.

## Inputs

Accept one or more of:

- A file path to a document containing a tender question and answer — read it with the Read tool
- Pasted markdown or plain text of the question and answer
- The requested number of supporting images or diagrams
- Optional: audience, submission format (Word, PowerPoint, PDF), page limit, or house-style constraints

If the number of images is not specified, recommend the smallest useful set, normally 1–3.

**Multi-section documents:** If the document contains multiple questions or sections, ask the user which section(s) to focus on, or scan all sections and surface the two or three highest-value visual opportunities, clearly attributing each to its source section.

If the document cannot be read, ask for the text or a reachable path before proceeding.

## Workflow

1. **Read the document**
   - Read the file at the path provided using the Read tool. Extract the full question text and the complete answer.
   - Identify the client question, scoring/evaluation signals, and answer structure.
   - Separate core messages, proof points, process descriptions, operating model elements, data flows, timelines, and measurable outcomes.
   - Note any claims, metrics, logos, named clients, or sensitive details that must not be invented or visualised without explicit source support.

2. **Find visual opportunities**
   - Choose visuals that clarify complex content, make evaluator scanning easier, or evidence the answer's logic.
   - Prefer diagrams over decorative imagery for procurement responses.
   - Avoid duplicating text that is already clear in the prose.
   - Do not create visuals for unsupported claims, vanity branding, generic transformation language, or weakly evidenced benefits.

3. **Select the best image types**

   | Type | When to use |
   |---|---|
   | Operating model | People, process, data, technology, governance, and assurance layers clearly described in the answer |
   | Journey or lifecycle | End-to-end phases, handoffs, escalation, controls, and feedback loops are a core part of the story |
   | Architecture or integration | Systems, interfaces, data flows, security boundaries, or service ownership described in detail |
   | Value map | Client priorities explicitly linked to IBM interventions, outcomes, and proof points |
   | Before/after | Current-state pain points contrasted with target-state improvements |
   | Evidence panel | 3–5 quantified outcomes where figures appear in the source — never invent numbers |
   | Timeline | Rapid delivery milestones, phased rollout, or key dates with associated metrics |
   | Stakeholder model | Multiple parties (client, partner, vendor, public) with relationships and responsibilities |

4. **Apply IBM visual style**
   - Read `$SKILL_DIR/references/ibm-visual-style.md` for the full palette, layout patterns, and prompt constraints.
   - Build prompts for clean enterprise diagrams: precise geometry, strong alignment, generous whitespace, restrained palette, accessible contrast, and minimal labelling.
   - Use IBM Carbon palette names and hex values explicitly in every prompt.
   - Avoid photorealistic people, stock-photo scenes, 3D renders, cartoon art, glossy gradients, decorative orbs, cluttered icons, and invented screenshots.

5. **Write ready-to-use image prompts**
   - Each prompt must be standalone — someone should be able to paste it directly into an image-generation tool without modification.
   - Target 100–200 words per prompt. Shorter is vague; longer creates noise.
   - Structure every prompt in this order:
     1. **Diagram type and purpose** — what kind of visual, what it communicates
     2. **Aspect ratio** — `16:9 landscape` for slides, `4:3` for Word documents, `1:1` for square insets
     3. **Layout** — how the content is arranged (horizontal layers, swimlanes, left-to-right flow, grid)
     4. **Specific content** — the exact items, nodes, phases, or relationships to show
     5. **Colour palette** — IBM Carbon colour names with hex codes; primary blue, one accent, greys for structure
     6. **Typography and style** — flat vector, thin connector lines, grid alignment, no shadows or gradients
     7. **Text handling** — instruct the tool to render blank outlined containers where labels should appear; list the exact labels separately in the output for manual overlay
     8. **Negative constraints** — what to exclude

   **Why empty containers:** AI image generators produce unreliable text rendering. For any diagram with more than two or three labels, prompt for blank outlined boxes, then provide the exact label text separately for manual overlay in a design tool such as Figma, PowerPoint, or Canva. This consistently produces cleaner, more professional results.

## Selection Criteria

Rank candidate visuals by:

1. Relevance to the tender question and scoring criteria
2. Ability to make the answer easier to understand quickly
3. Strength of source support — every visual element must be traceable to the document
4. Fit with IBM's brand and public-sector/procurement tone
5. Low risk of overclaiming, confusion, or visual clutter

## Output Format

```markdown
# Image Definition Recommendations

## Source Reviewed
- Document: [path or title]
- Requested image count: [number]
- Core response message: [one sentence]

## Recommended Visual Set

### Image 1: [short title]
- **Purpose:** [why this visual improves the answer — one or two sentences]
- **Type:** [from the table in Step 3]
- **Aspect ratio:** [16:9 / 4:3 / 1:1]
- **Source basis:** [specific answer sections, phrases, or evidence used]
- **Placement:** [where it should sit in the response, e.g. "after the 'End-to-End Service Transformation' section"]
- **AI image prompt:**
  """
  [complete standalone prompt, 100–200 words]
  """
- **Labels to add:**
  - [exact label text, one per line]
- **Avoid:**
  - [specific negative constraints]

### Image 2: [short title]
[same structure]

## Rejected / Lower-Priority Ideas
- [visual idea]: [why not selected]

## Risks and Checks
- [facts, metrics, client names, or approvals to verify before commissioning final artwork]
```

## Quality Bar

- Every suggested visual must support the evaluator's reading task, not decorate the response.
- Every visual element must be traceable to the source document — no invented content.
- Prompts must be specific enough for consistent, reproducible image generation: palette, layout, content, and constraints all stated explicitly.
- IBM style must be enforced through Carbon palette names and hex codes, flat vector geometry, and restrained label density.
- Use British English unless the source document requires otherwise.
