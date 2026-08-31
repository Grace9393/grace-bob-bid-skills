---
name: ibm-bid-writer
description: Use this skill whenever the user asks you to draft, write, or create tender responses, bid answers, proposal content, RFP responses, or ITT submissions. ALWAYS use it for any scored procurement writing task, even when the user says "answer this question", "write a response", or "draft this section" in a procurement context. This skill writes in a formal evaluator-facing enterprise bid style by default, infers evaluator concern and confidence case from the question when needed, and structures answers around named mechanisms, evidence, and buyer-aligned scoreability rather than generic proposal prose.
metadata:
  skills-required:
    - ibm-bid-strategy-and-capabilities-2026
    - ibm-bid-customer-stories
    - ibm-bid-library
    - ibm-bid-word-count
  skills-suggested:
    - ibm-bid-requirements-analysis
    - ibm-bid-requirements-extractor
    - ibm-bid-win-themes
    - ibm-bid-hot-buttons
    - ibm-bid-client-language-analysis
    - ibm-bid-wireframe-creator
    - ibm-bid-image-definer
    - ibm-bid-answer-evaluator
    - ibm-bid-fact-checker
---

# Bid Writing Skill

This skill helps you draft high-quality tender responses that are compelling, well-structured, and aligned with client needs while showcasing IBM's relevant capabilities. The target style is not generic "good proposal prose". It should feel like a winning enterprise bid: high-confidence, evaluator-aware, specific about delivery, and grounded in named mechanisms, evidence, and measurable outcomes.

## Writing Modes

Use one of these two modes explicitly:

1. **Default: formal scored-response mode**
   - Use this for almost all tender, ITT, framework, and public-sector bid responses.
   - Write in formal, enterprise-oriented, evaluator-facing prose.
   - Prioritise scoreability, credibility, named mechanisms, structured evidence, and buyer-aligned headings.

2. **Optional: conversational drafting mode**
   - Use this only when the user explicitly wants a lighter draft, an internal strawman, workshop content, SME interview synthesis, or exploratory shaping before formal bid conversion.
   - Keep the content clear and commercially useful, but allow a looser internal working tone.

If the user does not specify a mode, always use **formal scored-response mode**.

## Quick Start

Use this sequence every time:

1. Parse the tender question into required sub-questions and scoring signals.
2. Confirm the writing mode. If the user does not specify one, use formal scored-response mode.
3. **Default format for Part 2: flowing prose paragraphs.** Bullet lists are banned in the written response unless the question explicitly enumerates discrete parallel items or the user requests bullets. If bullets are used anywhere in Part 2, record the justification in the pre-draft plan. When in doubt, write prose.
4. Load the wireframe. If the user provides a question number, check `./tmp/ibm-bid-wireframe-Q0X.md` where `Q0X` matches the question reference, then `./tmp/q[N]_wireframe.md`, then any wireframe path recorded in `./tmp/ibm-bid-project.md`. If the user provides wireframe text directly, use that first. Extract `Part 1: Sub-Headings` / `Part 1: Sub-Headings Structure` exactly. Also extract the wireframe's `Diagram Summary`, `Client diagram requirement`, `Diagram count`, `Diagram type(s)`, and `Diagram word count treatment` fields.
5. If no wireframe exists, create a wireframe-style sub-heading structure before drafting: first bullet `How we've structured our response`, then `How we...` bullets that follow the tender question sequence. Use this generated structure as the drafting skeleton.
6. Output `Part 1: Sub-Headings Structure` at the top of the response, then `Part 2: Written Response` structured around those same sub-headings. In Part 2, place `<!-- START-COUNT -->` immediately before the first counted evaluator-facing word and `<!-- END-COUNT -->` immediately after the final counted evaluator-facing word. Do not omit Part 1 unless the user explicitly asks for answer-only output or a tender template forbids it.
7. Identify the evaluator's core concern for this question, the buyer anxiety sitting behind it, and decide whether this answer needs a document-level confidence section, a short local framing line, or no separate confidence opener.
8. Check `./tmp/ibm-bid-project.md` for `client_language_analysis_artifact`; if present, read that file. If the tracker is missing or no artifact path is recorded, fall back to `./tmp/ibm-bid-client-language-analysis.md`. Apply the vocabulary substitutions, tone guidance, and writing rules throughout the draft when a language profile exists.
9. Load `$ibm-bid-library`, `$ibm-bid-customer-stories`, and `$ibm-bid-strategy-and-capabilities-2026`. If the tender question, response template, wireframe, requirements extractor, or user instruction contains a word limit or diagram/image word-count treatment, also load `$ibm-bid-word-count` before drafting.
10. If `./tmp/ibm-bid-approved-customer-stories.md` exists, treat it as the controlled customer evidence pool and use only those stories unless the user explicitly asks to refresh the shortlist.
11. If the question is about a service, map the required answer across people, process, data, and technology before selecting mechanisms. Treat "service" as the full operating model, not only the technical platform or delivery method.
12. Select 2-4 named mechanisms that explain how delivery will actually work (for example lifecycle, governance forum, dashboard, transition model, accelerator, partner construct, operating cadence).
13. Decide the answer composition before drafting: prose only, diagram plus concise prose, table plus prose, or a combination. When a permitted diagram would explain structure, flow, operating model, architecture, governance, roles, timeline, or evidence more clearly than prose, allocate the concept to the diagram and reduce the prose to explanation, significance, controls, and proof. Do not write 500 words of prose where a diagram and 200 focused words would score better and comply with the tender.
14. Mirror the client structure and numbering exactly. Choose format as follows: prose paragraphs for narrative explanation and method description; bold-labelled prose blocks for operating mechanisms; tables for mappings, responsibilities, or commitments; diagram callouts for complex structures when permitted. Bullets are banned for narrative or method content. Write prose instead.
15. Add evidence with quantified outcomes and baseline comparisons, prioritising account-specific or incumbent evidence before generic IBM proof points.
16. Draft each substantive section in the sequence promise -> mechanism -> proof, then show how the method protects the buyer.
17. If using a diagram, include an evaluator-facing diagram placeholder with a concise title, purpose, placement, and label set, then write only the surrounding prose needed to interpret it. If prompts or artwork briefs are needed, use `ibm-bid-image-definer` after the draft structure is agreed.
18. If a word limit applies, run the existing `ibm-bid-word-count` script on the evaluator-facing answer before finalising. Do not use `wc -w`, `pandoc`, editor counts, model-estimated counts, copied snippets, or newly written Python/JavaScript/shell counting code. If the answer is only inline, place the evaluator-facing answer with the `<!-- START-COUNT -->` and `<!-- END-COUNT -->` markers in a temporary markdown file and run the `ibm-bid-word-count` script against that file. If the answer is over limit, revise and rerun the script until the counted answer is within limit. Report the final count, limit, and command used.
19. Run a punctuation and AI-style pass before finalising: remove em dashes, en dashes used as sentence punctuation, generic assistant phrasing, and unsupported adjective stacking.
20. Fact-check every claim, then run `ibm-bid-answer-evaluator`. Pass the verified word count result and command to the evaluator when a word limit applies.

For detailed guidance, read:
- `references/pre-draft-planning-template.md`
- `references/writing-style-guide.md`
- `references/quality-checklist.md`
- `references/integration-guide.md`
- `references/example-responses.md`

## Core Workflow

1. **Understand the question**
   - Identify all mandatory parts, constraints, and evaluation language.
   - Mirror client terminology and preserve question order.
   - Mirror client numbering exactly where the tender has numbered sub-parts. This is a scoring aid, not cosmetic formatting.
   - Work out what would make the evaluator trust this answer: continuity, control, standards, capacity, mobilisation speed, innovation, value for money, or low delivery risk.
   - Identify the hidden buyer fear behind the criterion, such as failed mobilisation, over-dependence on the supplier, weak governance, uncontrolled innovation, compliance drift, poor stakeholder handling, or excessive oversight burden on the client.
   - List what must be proven with evidence.
   - If the question references schedules, criteria, service levels, standards, or clarifications, mirror that language explicitly.
   - When the question asks about a service, service delivery, service improvement, service management, transition, operation, or support, interpret the service holistically as people, process, data, and technology. Do not narrow the answer to systems or tooling unless the question explicitly limits scope.
   - For service questions, identify what the evaluator needs to see across all four dimensions:
     - people: roles, capability, leadership, knowledge transfer, responsibilities, behaviours, and stakeholder engagement
     - process: lifecycle, governance, controls, workflows, assurance, escalation, change, and continuous improvement
     - data: records, reporting, metrics, quality, security, privacy, interoperability, insight, and evidence used to run the service
     - technology: platforms, tooling, automation, integrations, environments, resilience, security controls, and technical architecture
   - Decide the mode early. Formal scored-response mode is the default. Conversational drafting mode is opt-in only.
   - Before drafting, create a short pre-draft plan using `references/pre-draft-planning-template.md`.
   - If the user has not supplied the evaluator concern, confidence case, named mechanisms, evidence stack, or repeated bid themes, infer them from the question, the scoring language, and the available source material rather than asking by default.

2. **Research and map evidence**
   - Check `./tmp/ibm-bid-project.md` for `client_language_analysis_artifact`; if present, read that file. If the tracker is missing or no artifact path is recorded, fall back to `./tmp/ibm-bid-client-language-analysis.md`. Apply the vocabulary substitutions, tone guidance, and writing rules throughout the draft. Mirror the client's terminology, characteristic phrases, and register. Observe the language to avoid list.
   - Use `$ibm-bid-library` for reusable approaches and prior response patterns.
   - Use `$ibm-bid-customer-stories` for proof points and quantified outcomes.
   - Use `$ibm-bid-strategy-and-capabilities-2026` for differentiators and strategic positioning.
   - If `./tmp/ibm-bid-approved-customer-stories.md` exists, use only those shortlisted stories in the answer unless the shortlist is explicitly reopened.
   - Prioritise evidence in this order: current account or incumbent experience, named team capability, relevant public sector/NHS examples, then broader IBM proof.
   - Where possible, make the answer feel already mobilised rather than merely mobilisable: current service knowledge, current team continuity, current estate familiarity, existing stakeholder relationships, existing metrics, or named delivery leaders.
   - Use transference of trust deliberately: borrow credibility from recognised clients, senior figures, partners, standards, or live service environments, but explain the operational relevance rather than dropping halo names.
   - Select only evidence that directly supports this specific question.
   - Pull named mechanisms, named leaders, named partner contributions, and measurable outcomes into a note set before drafting.
   - Complete the pre-draft plan before writing full prose.

3. **Structure before drafting**
   - Treat the wireframe sub-heading structure as the governing answer skeleton whenever one exists. Do not replace it with a newly invented structure, generic capability headings, or only client-numbered headings.
   - Look for the wireframe in this order:
     - user-provided wireframe text
     - `./tmp/ibm-bid-wireframe-Q0X.md` matching the current question
     - `./tmp/q[N]_wireframe.md` matching the current question
     - any wireframe artifact path recorded in `./tmp/ibm-bid-project.md`
   - Extract the bullets under `Part 1: Sub-Headings` or `Part 1: Sub-Headings Structure`. Preserve their wording and order unless the tender template expressly requires different section labels.
   - Extract the wireframe's diagram guidance before drafting: `Diagram Summary`, `Client diagram requirement`, `Diagram recommendation`, `Diagram count`, `Diagram type(s)`, `Diagram word count treatment`, and `How the diagram should be used`.
   - Treat `Diagram word count treatment` as a drafting control:
     - `Included`: budget diagram labels, captions, figure titles, and any in-answer diagram text inside the word limit.
     - `Excluded`: use the diagram to carry concise structure or flow, but still budget surrounding explanatory prose and any captions if the wireframe flags uncertainty.
     - `Confirm`: avoid long labels or captions, keep the prose self-contained enough to score, and flag the uncertainty in the handoff.
   - If no wireframe is available, read `./tmp/ibm-bid-requirements-extractor.md` when present, especially `Response Constraints` and `Diagram / Image Limits`, before deciding whether diagrams are allowed or useful.
   - If no wireframe is available, generate the heading structure before drafting using the `ibm-bid-wireframe-creator` pattern:
     - first section: `How we've structured our response`
     - subsequent sections: `How we [verb phrase from question]`
     - order follows the tender question and sub-requirements
     - no generic introduction or conclusion heading
   - Make a deliberate composition choice before writing:
     - **Prose only** when the client prohibits diagrams, the diagram limit is zero, the concept is simple, or the visual would duplicate clear prose.
     - **Diagram plus concise prose** when the client permits or requires diagrams and the answer needs to explain structure, sequence, roles, governance, architecture, controls, timelines, or a value chain.
     - **Table plus prose** when the evaluator needs to check mappings, responsibilities, commitments, or compliance line by line.
     - **Diagram plus table plus prose** only where the word/page allowance and question complexity justify all three.
   - If a diagram is selected, assign the diagram a job that prose will not repeat: show the operating model, flow, architecture, timeline, responsibility model, evidence map, or value chain. Then use prose to explain why the visual matters, how IBM will govern it, and what proof supports it.
   - Use the client's diagram/image count as a writing constraint. If one diagram is allowed, do not create several visual placeholders. If two are required, ensure they cover distinct concepts rather than splitting one idea.
   - Use word-count treatment to shape the draft. If diagram labels and captions are excluded, use the diagram to carry concise labels and reduce body prose. If labels or captions count, keep them short and budget them inside the word limit.
   - Use these sub-headings as actual section headings in the evaluator-facing draft. A document-level confidence section may sit before them, but it must not replace them.
   - Present the output in two parts by default:
     - `## Part 1: Sub-Headings Structure`, containing the exact wireframe or generated sub-heading bullets
     - `## Part 2: Written Response`, containing the drafted answer using those same sub-headings as section headings
   - In `Part 2`, include the default word-count markers exactly once:
     - place `<!-- START-COUNT -->` after the `## Part 2: Written Response` heading and before the first counted evaluator-facing line
     - place `<!-- END-COUNT -->` after the final counted evaluator-facing line and before any evidence log, notes, evaluator feedback, source appendix, or handoff text
     - if the user asks for answer-only output, still wrap the counted answer body with these two comments unless the tender template forbids markdown comments
   - Omit `Part 1` only when the user explicitly requests answer-only content or the tender response template forbids non-answer planning material.
   - In formal scored-response mode, use a document-level confidence section when the answer is substantial, strategic, or benefits from previewing multiple proof themes before the numbered response begins.
   - If the buyer format is already tightly segmented, use a short local framing line only where it helps the evaluator understand why IBM is credible on that sub-question.
   - Do not force a confidence opener into every section. Repetition weakens the effect.
   - Use the winning master template where it fits: `Why you should have full confidence in our proposal`, short theme-setting paragraph, 2-4 high-value confidence bullets, then criterion-led sections that mirror the buyer's numbering.
   - Build headings that track the client sub-questions through the wireframe structure.
   - Lead each section with one orienting sentence before any bullets, tables, or mechanism blocks.
   - Use prose as the default delivery format inside each answer section. Do not turn the main answer into long bullet lists.
   - Use bullets sparingly and deliberately: a maximum of one short bullet list per major section unless the tender explicitly requests lists or the content is a set of deliverables, criteria, risks, commitments, or responsibilities.
   - Prefer short paragraphs with bold-labelled lead-ins over standalone bullets when explaining a method, rationale, governance model, or delivery approach.
   - Choose the right answer archetype for the question rather than forcing one default structure.
   - Make the answer legible to scorers by using labelled sections such as approach, evidence, risks, mitigations, capabilities, commitments, milestones, or challenges where helpful.
   - Use the winning internal pattern that best fits the criterion: short framing prose, confidence summary bullets, bold-labelled mechanism blocks, inline labelled mechanism sequences, accountability tables, commitment-plus-activities tables, phased plans, or challenge-to-mitigation sequences.
   - Prefer the sequence promise -> mechanism -> proof inside sections. Make the evaluator see not just what IBM says, but how it will work and why it is believable.
   - Use tables to compress evaluator workload whenever the buyer is checking mappings, profile fit, responsibilities, commitments, or rationale.
   - Use figures or diagram references only when they genuinely signal process maturity or clarify structure. Do not refer to visuals that the answer does not actually include.
   - When a diagram is included, insert a clear evaluator-facing placeholder in the answer at the intended location:
     - `[[Diagram X: Title - diagram type - purpose]]`
     - followed by a short `Labels:` line when labels are needed
     - followed by a one-sentence caption only if the tender permits or requires captions
   - Do not write a full AI image-generation prompt in the bid answer. If the user needs an artwork brief, run `ibm-bid-image-definer` after the answer structure is agreed.
   - Connect technical features to client outcomes with the "So What?" test.

4. **Draft response**
   - Write in plain, specific British English with active voice.
   - In formal scored-response mode, sound authoritative, formal, and delivery-ready, not cautious, chatty, or generic.
   - In conversational drafting mode, keep the content commercially sharp but allow a lighter internal working tone.
   - Do not use em dashes in evaluator-facing prose. Replace them with a comma, colon, semicolon, parentheses, or a new sentence. Use a simple hyphen only for compound modifiers or standard terms.
   - Sell certainty first and transformation second. Lead with continuity, control, and safety before expanding into innovation or optimisation.
   - Use credible ambition: state the ambition, bind it to a formal method, bind that method to governance, bind governance to metrics, and support it with precedent.
   - Include concrete examples with baseline, outcome, timeframe, and financial effect where available.
   - Tie major claims to one or more of: named mechanism, named person or team, named partner, metric, quote, precedent, or governance control.
   - Show differentiation through delivery method, risk handling, governance, or measurable value.
   - Repeat a small set of branded methods and anchor phrases deliberately where they strengthen bid coherence. In bid writing, memory anchors are useful if they are relevant and consistent.
   - Prefer `by design` constructions when true and evidenced, such as standards by design, secure by design, safety by design, or compliance by design. These signal structural control rather than retrospective checking.
   - Use `will` when the commitment is supported. Do not dilute strong evidence-backed commitments into weak modal phrasing.
   - Show collaboration after authority is established. Sound like a proven operator who can work in a blended team, not a bidder waiting to be led.
   - State boundaries and shared accountabilities clearly where that increases credibility.
   - Avoid invented data or unsupported claims.
   - Do not introduce customer stories outside the approved shortlist when a shortlist artifact exists.

5. **Quality gate**
   - Fact-check all claims against source content.
   - Flag unsupported content with `{{++REPLACE: text}}`.
   - If a word limit applies, load `ibm-bid-word-count`, run its existing PEP 723 markdown word-count script against only the marked evaluator-facing response body, and record the exact command and result. Do not rely on raw markdown `wc -w`, `pandoc`, editor counts, model-estimated counts, copied snippets, newly written Python, or ad hoc approximations.
   - If the count is over the tender limit, revise the answer and rerun `ibm-bid-word-count` until the evaluator-facing answer is compliant before returning it.
   - Run `ibm-bid-answer-evaluator` and iterate until score >=3.
   - If score <3, revise with targeted fixes and resubmit.

## Winning Response Method

Use this method to reproduce the qualities seen in successful bids:

1. **Lead with confidence**
   - Start by answering the evaluator's hidden question, not just the written one.
   - Use a confidence section when it improves evaluator orientation, especially for substantial standalone answers.
   - The default winning pattern is one strong document-level confidence section near the top, then direct criterion-led answers underneath.
   - Use local confidence framing only where a subsection genuinely needs a short credibility signal before detail.

2. **Sell through mechanisms, not adjectives**
   - Prefer named operating constructs over vague claims.
   - Instead of saying IBM has a strong delivery model, say what the model is called, what forums or controls sit inside it, and how that reduces risk or speeds delivery.

3. **Mirror the score frame**
   - Reflect the buyer's numbering, wording, criteria labels, standards, and schedule references.
   - Make it easy for evaluators to see where each requirement has been answered.

4. **Pair ambition with control**
   - When describing transformation, always show the governance, security, standards, assurance, or delivery controls that make it credible.
   - A strong answer makes innovation feel safe.

5. **Use repeated themes deliberately**
   - Carry a small set of consistent themes across answers such as continuity, low supervision, standards by design, measurable productivity, integration readiness, and value for money.
   - Repetition is useful when it reinforces a coherent bid story.

6. **Prefer account-specific proof**
   - If IBM already knows the client, service, estate, or stakeholders, use that first.
   - Generic case studies are secondary support, not the primary foundation.

7. **Translate detail into buyer value**
   - Explain what the delivery method means for service reliability, pace, cost, adoption, compliance, interoperability, or user outcomes.

8. **Use the right mode**
   - Formal scored-response mode is the standard for evaluator-facing content.
   - Conversational drafting mode is only for internal development steps before the answer is converted into formal scored-response prose.

9. **Spend the word budget where prose adds value**
   - Treat the word limit as a design constraint, not a target to fill.
   - If a diagram can carry structure, flow, ownership, architecture, timeline, or control logic more clearly than prose, use the diagram and write shorter prose around it.
   - Replace diagram-duplicating prose with evaluator interpretation: what the diagram proves, how IBM will operate it, what controls make it safe, and what evidence shows it works.

10. **Make the evaluator feel protected**
   - Reduce buyer anxiety explicitly.
   - Show the controls, forums, dashboards, charters, scorecards, gates, or acceptance criteria that reduce the client's oversight burden and make the service safer to entrust to IBM.

11. **Make the bid feel operational, not hypothetical**
   - Use named leaders, live-service patterns, concrete work packages, milestone logic, and mobilisation detail so the answer feels staffed and ready to execute.

12. **Use repetition as a scoring tool**
   - Repeat the core strategic story and a small set of named methods across answers when they are genuinely central to the solution. In procurement writing, disciplined repetition improves evaluator recall and coherence.

## Pre-Draft Planning Step

Do not start drafting long-form answer text until you have captured the following:

1. **Evaluator concern**
   - What is the evaluator really worried about scoring on this question?
   - If not supplied, infer it from the wording, criteria, service context, and risk profile.

2. **Confidence case**
   - What is the short argument that says IBM can be trusted on this topic?
   - Build this from continuity, current-account knowledge, proven delivery, named capability, assets, controls, or outcomes.

3. **Named mechanisms**
   - What delivery, governance, assurance, transition, or productivity mechanisms will make the answer believable?
   - Prefer named lifecycles, boards, dashboards, charters, workbenches, accelerators, or partner constructs.

4. **Evidence stack**
   - Which evidence will you use, in what order?
   - Prefer current account evidence first, then named team evidence, then relevant public sector/NHS precedent, then broader IBM proof.

5. **Repeated bid themes**
   - Which cross-bid themes should this answer reinforce?
   - Examples: continuity, low supervision, standards by design, measurable productivity, value for money, integration readiness, safe innovation.

6. **Likely evidence form**
   - What is the best way to present the proof in this answer?
   - Choose between confidence summary bullets, bold-labelled mechanism blocks, inline labelled mechanism sequences, compact prose paragraphs, role or responsibility tables, commitment-plus-activities tables, phased plans, or challenge/mitigation blocks.

7. **Buyer protection logic**
   - How will the answer show that IBM reduces oversight burden, transition risk, compliance risk, delivery risk, or dependency risk?
   - Capture the controls or accountabilities that make the client feel protected.

8. **Service scope lens**
   - If the question concerns a service, what must be said about people, process, data, and technology?
   - Record any dimension that is out of scope, already covered elsewhere in the same answer, or unsupported by available evidence.

9. **Visual composition decision**
   - What diagram/image/table limits apply to this answer?
   - What is the word-count treatment for labels, captions, and diagram text?
   - Should the answer use prose only, diagram plus concise prose, table plus prose, or a combination?
   - If using a diagram, what content will move out of prose and into the visual?
   - What short prose remains necessary to interpret the visual and make it scoreable?

Use `references/pre-draft-planning-template.md` to structure this. If useful, generate a first draft of the plan with:

```bash
uv run python $SKILL_DIR/scripts/pre_draft_plan.py --question-file path/to/question.txt
```

Or:

```bash
uv run python $SKILL_DIR/scripts/pre_draft_plan.py --question "Question text here"
```

The script is only a scaffold. Improve or correct the inferred plan using the real bid context before drafting.

## Response Archetypes

Choose an answer shape that fits the question:

1. **Technical or delivery approach**
   - Document-level confidence section if this is a substantial standalone answer; otherwise a short framing line only if useful
   - Direct answer
   - Named operating mechanisms
   - Evidence and outcomes
   - Risks and mitigations
   - Preferred internal pattern: short framing paragraph, bold-labelled delivery blocks, then proof and controls

2. **Standards, security, or compliance**
   - Document-level confidence section if useful
   - Standards-by-design method
   - How standards apply to the service
   - Assurance roles, controls, and cadence
   - Proof from comparable live services
   - Preferred internal pattern: confidence section, standards categories, then assurance workflow and evidence

3. **Mobilisation or transition**
   - Document-level confidence section if useful
   - Transition model with phases or named method
   - Continuity and knowledge transfer plan
   - Early productivity and governance controls
   - Risks, dependencies, and mitigation
   - Preferred internal pattern: confidence section, phased plan, then transition controls and mobilisation evidence

4. **Capability or team-fit**
   - Short framing paragraph
   - Why the capability mix fits the requirement
   - Named leaders or roles
   - Relevant experience and account context
   - How the team flexes as demand changes
   - Preferred internal pattern: confidence section, capability framing, then tables mapping experience to relevance

5. **Social value or commitments**
   - Optional short confidence section
   - Criterion-led commitment statement
   - Commitment-plus-activities table
   - Measures, timings, and accountability
   - Stakeholder influence and wider value
   - Preferred internal pattern: confidence section, then explicit `Commitment N` and `Activities` blocks, followed by governance and reporting tables or timed action plans

6. **Challenges, uncertainties, or value for money**
   - State the challenge clearly
   - Show IBM's view of the underlying cause
   - Explain the mitigation or alternative model
   - Prove it with precedent and measurable impact
   - Close on how service integrity is protected
   - Preferred internal pattern: challenge statement, `plan to address` or mitigation block, then precedent and value proof

7. **Incumbent defence or continuity-heavy answers**
   - Confidence section anchored in current-account knowledge
   - Direct statement of existing service familiarity and transition-risk reduction
   - Named team continuity, service knowledge, or estate knowledge
   - Mechanisms that preserve momentum while improving the service
   - Proof from live delivery, current metrics, or named stakeholder relationships
   - Preferred internal pattern: confidence section, continuity proof, then controlled-improvement plan

## Bid Pack Story Discipline

Carry one central proposition consistently across the response pack. A winning pack usually repeats one coherent story in different evaluative languages, such as:

- operational confidence
- continuity and low-risk mobilisation
- standards and compliance maturity
- innovation with control
- ecosystem reach and partner leverage
- quantified value for money
- governance and assurance discipline

Every answer does not need every theme, but each answer should reinforce the same overall bid story. Avoid writing isolated good answers that do not accumulate into a coherent evaluator impression.

## Confidence Section Template

When a document-level confidence section is useful, it should do four things quickly:

1. Tell the evaluator why IBM can be trusted on this specific topic.
2. Preview the two to four proof themes that the rest of the answer will substantiate.
3. Reframe the question from `can IBM do this?` to `why IBM is a safe and high-value choice for this requirement`.
4. Set up the detail that follows without repeating background.

Use headings such as:

- `Why you should have full confidence in our proposal`
- `Why you can rely on IBM to deliver this service`
- `Why IBM is well placed to deliver this requirement`

Then include:

- one short framing paragraph
- two to four concise bullets with the strongest trust-building claims
- no generic corporate background

## Persuasion Patterns To Reuse

1. **Promise -> mechanism -> proof**
   - Make this the default internal logic of a scored section.

2. **Innovation -> control**
   - Any innovation claim should be tied to assurance, standards, governance, or piloting.

3. **Method -> buyer outcome**
   - Never leave a method abstract. Show why it improves pace, safety, cost, resilience, adoption, or visibility.

4. **Capability -> staffing reality**
   - Use named people, teams, or sourcing mechanisms so capability feels real rather than brochure-like.

5. **Commitment -> measurement**
   - Especially for social value, quality, service, or transformation commitments, show activities, measures, timings, owners, and reporting.

## Social Value And Human-Centred Variants

When the question is about social value, workforce design, or community outcomes:

1. Broaden the tone slightly to allow more human language.
2. Keep the same bid discipline: commitments, activities, metrics, governance ownership, and reporting.
3. Connect the social value plan to delivery performance and stakeholder outcomes rather than treating it as a detached CSR annex.

## Compact Labelled Sequence Pattern

Use this pattern when the evaluator needs a high density of scoreable method detail but a full bullet list or table would slow the answer down.

1. Start with one orienting sentence that answers the criterion directly.
2. Follow with two to five inline bold labels in the same paragraph or in adjacent short paragraphs.
3. Make each label name a mechanism, workstream, standards area, or control topic.
4. After each label, explain the specific activity, control, or evidence in one to three clauses.
5. Keep the sequence readable. If any labelled item needs more than two sentences, break it out into a full mechanism block instead.

Good uses:
- standards categories and how they apply
- innovation, foresight, and requirements sensing in one compact section
- adherence domains such as planning, security, interoperability, testing, and oversight
- short challenge-to-response chains where each item needs only concise explanation

Avoid:
- using this pattern for accountability mapping better shown in a table
- hiding key evidence at the end of an overlong sentence
- stacking labels without showing buyer value, control, or proof

## Context Management

Write output to `./tmp/ibm-bid-responses/Q0X_[topic].md` per question only when the user asks for persisted artifacts or when downstream skills require handoff files (e.g., Q01_technical_approach.md, Q02_delivery_methodology.md). Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `questions_answered`: question references or response file paths already drafted
- `next_question_to_draft`: next question reference or response file path
- `artifacts_generated`: include generated response and plan files when written
- `next_skill_recommendation`: normally `ibm-bid-answer-evaluator` for the drafted response or `ibm-bid-writer` for the next response

Preserve any existing `client_language_analysis_status`, `client_language_analysis_artifact`, and `client_language_analysis_documents` fields so downstream drafting continues to use the client language profile.
When useful, save the pre-draft plan to `./tmp/ibm-bid-response-plan.md` or question-specific files such as `./tmp/ibm-bid-responses/Q01_plan.md`.

## Writing and Evidence Rules

1. Use plain, specific British English (`realise`, `programme`, `colour`).
2. Use active voice and concrete language over empty business jargon.
3. Quantify benefits with baseline and outcome, not percentage only.
4. Include relevant, detailed, and credible examples.
5. Explain partner value, not partner names alone.
6. Keep technical detail tied to business impact and stakeholder value.
7. For each major section, identify the named mechanisms that make the answer believable.
8. Use evaluator-friendly signposting so that requirements can be scored quickly.
9. Use prose-first drafting for final scored responses. Prioritise structured prose where explanation matters, tables where mapping matters, labelled prose blocks where operating method matters, and bullets only where a list will score faster than a paragraph.
10. Where useful, state what IBM owns, what the client owns, and how the interface works.
11. For service questions, show the operating model across people, process, data, and technology unless the tender wording deliberately narrows the scope.
12. Before finalising, scan the draft for bullet overuse. If a bullet list explains a method, rationale, sequence, or assurance approach, convert it into prose unless the list format clearly improves evaluator scoring.

See full guidance in `references/writing-style-guide.md`.

## Quality Checklist (Short Form)

Before finalising:

1. Confirm `Part 1: Sub-Headings Structure` is present at the top of the response, with `How we've structured our response` as the first bullet followed by one `How we...` bullet per question sub-requirement, unless the user or tender template required answer-only output.
2. Confirm the written response in `Part 2: Written Response` uses those same sub-headings as section headers.
3. Confirm the written response in Part 2 is written in flowing prose paragraphs. Scan for bullet lists. If any appear outside a genuine parallel enumeration or user-requested list, convert them to prose before finalising.
4. Confirm every required sub-question is answered in client order.
5. Confirm client numbering and terminology are mirrored where present.
6. Confirm the answer opens with a convincing confidence case where appropriate.
7. Confirm all key claims have evidence and source alignment.
8. Confirm quantified outcomes include baseline and context.
9. Confirm named mechanisms, controls, and governance are clear.
10. For service questions, confirm the answer covers people, process, data, and technology or explicitly explains why a dimension is not relevant.
11. Confirm no fabricated or unsupported content remains.
12. Confirm British English, human tone, concise structure, and no em dashes.
13. If a word limit applies, confirm the word count using `ibm-bid-word-count` against the `<!-- START-COUNT -->` / `<!-- END-COUNT -->` section, include the exact command and result in the handoff or final note, and revise before finalising if the counted answer is over limit.
14. Confirm evaluator score is >=3 before progressing.

Use full checklist in `references/quality-checklist.md`.

## Word Count Checking

When the tender specifies a word limit, always load and use the existing `ibm-bid-word-count` skill and its PEP 723 Python script before finalising the answer. Do not use raw markdown `wc -w`, `pandoc`, editor counts, model-estimated counts, copied snippets, one-off Python, JavaScript, shell pipelines, or ad hoc approximations.

Treat word-count compliance as a hard quality gate:

1. Identify the counted section from the tender rules.
2. Run this skill's existing script against the persisted draft or a temporary markdown file containing the evaluator-facing answer wrapped in `<!-- START-COUNT -->` and `<!-- END-COUNT -->`. If the answer exists only inline, create the temporary markdown file for counting; do not write counting code.
3. If the count is over limit, edit the answer and rerun the script.
4. Report the final count, limit, status, and exact command used.
5. Pass that result to `ibm-bid-answer-evaluator` so the evaluator does not repeat or approximate the count.

Count only the evaluator-facing answer content by wrapping the counted section with the default markers:

```markdown
<!-- START-COUNT -->

Evaluator-facing answer content goes here.

<!-- END-COUNT -->
```

Then run:

```bash
uv run python <IBM_BID_WORD_COUNT_SKILL_DIR>/scripts/count_words_in_markdown.py <DOC>
```

When the answer is followed by evidence logs, evaluator notes, source appendices, or other non-counted sections, place `<!-- END-COUNT -->` before those sections.

If both markers are present, they override heading arguments. For older drafts that do not have count markers, fall back to heading-based extraction:

```bash
uv run python <IBM_BID_WORD_COUNT_SKILL_DIR>/scripts/count_words_in_markdown.py --from-heading "## Answer:" --until-heading "## Evidence Log" <DOC>
```

If the document front matter contains `min-word-count` or `max-word-count`, use `--show-limits` to report the count against those limits. Front matter is never counted:

```bash
uv run python <IBM_BID_WORD_COUNT_SKILL_DIR>/scripts/count_words_in_markdown.py --show-limits <DOC>
```

If the tender requires the whole markdown response to count and the document contains markers that should be ignored, use `--ignore-count-markers`:

```bash
uv run python <IBM_BID_WORD_COUNT_SKILL_DIR>/scripts/count_words_in_markdown.py --ignore-count-markers <DOC>
```

If the tender template forbids markdown comments and the response does not use `## Answer:`, replace that heading with the first heading that marks the start of evaluator-facing answer content. If the response uses a different stop heading, replace `## Evidence Log` with the exact heading to exclude. Add `--include-heading` only if the tender requires the start heading to count. Exclude notes, evidence logs, planning text, evaluator feedback, and source appendices unless the tender explicitly says they count.

## Integration At A Glance

1. **Before drafting**: Use requirements analysis, strategic positioning, and win themes if available.
2. **During drafting**: Pull evidence from required IBM knowledge skills.
3. **After drafting**: Run fact-check and answer evaluator; iterate if score <3.
4. **After all questions pass**: Move to technical assurance workflow.

For full workflow, search strategy, and cross-skill orchestration, use `references/integration-guide.md`.

## Which Skill To Use

1. Need to draft or rewrite tender answer content: use `ibm-bid-writer`.
2. Need to score or critique an existing answer: use `ibm-bid-answer-evaluator`.
3. Need to verify claim accuracy against source docs: use `ibm-bid-fact-checker`.
4. Need end-to-end process guidance: use `ibm-bid-navigator`.

## Troubleshooting

1. Score below 3 due to weak evidence: add stronger customer story proof points and measurable outcomes.
2. Score below 3 due to generic answer: mirror client wording and tighten structure to question order.
3. Score below 3 due to low credibility: add named mechanisms, account-specific experience, and clearer ownership boundaries.
4. Unsupported claims found: replace with verified data or mark `{{++REPLACE: text}}`.
5. Tone sounds AI-generated: simplify language, remove filler, and replace adjectives with mechanisms or evidence.

## Important Notes

1. Different evaluators may only see assigned question responses, so avoid cross-question dependencies.
2. Cross-reference within a single question and its attachments is acceptable.
3. Choose the format that scores fastest for the criterion: explanation in prose, mapping in tables, operating method in labelled prose blocks, and bullets only for genuinely list-like material.
4. All examples must be real and verifiable.
5. Reuse bid themes consistently, but vary the evidence and mechanism details so each answer still feels tailored.
