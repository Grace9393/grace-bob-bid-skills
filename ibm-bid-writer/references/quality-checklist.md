# Quality Checklist

Run this checklist before finalising any tender response.

## Coverage and Structure

1. `## Part 1: Sub-Headings Structure` appears at the top of the response, unless the user or tender template required answer-only output.
2. Part 1 starts with `How we've structured our response`.
3. Part 1 includes one `How we...` bullet per question sub-requirement.
4. `## Part 2: Written Response` uses those same Part 1 bullets as its section headings.
5. Every required element is addressed.
6. Response follows the client question order.
7. Client numbering is mirrored exactly where the buyer uses numbered parts.
8. Client language and terminology are mirrored.
9. Headings are informative and aligned to outcomes.
10. Response opens with a confidence-building framing statement where the question type supports it.
11. Major sections follow promise -> mechanism -> proof.
12. The written response in Part 2 is written in flowing prose paragraphs by default.
13. Bullet lists in Part 2 appear only where the question explicitly enumerates discrete parallel items or the user requested bullets.
14. Every Part 2 bullet list has a justification recorded in the pre-draft plan.
15. Any bullet list that explains a method, rationale, governance model, assurance approach, or delivery sequence has been converted into paragraphs or bold-labelled prose.
16. The chosen format suits the question: prose for explanation, tables for mapping, labelled prose blocks for operating method.
17. If the wireframe recommends or requires a diagram, the answer uses the diagram deliberately rather than duplicating the same material in prose.
18. `Diagram word count treatment` from the wireframe is reflected in the draft: labels/captions are budgeted if included, kept short if uncertain, and not double-counted when excluded.
19. If a diagram is included, the answer contains a clear placeholder with title, type, purpose, labels where needed, and a concise caption only where permitted.
20. For service questions, the response covers people, process, data, and technology, or explicitly explains why a dimension is not relevant.

## Value and Differentiation

1. Response demonstrates clear IBM differentiation.
2. Innovation is concrete, not generic.
3. Stakeholder-specific value is explicit (technical, finance, compliance, operations).
4. "So What?" test is applied to technical features.
5. Named mechanisms explain how IBM will deliver, govern, or accelerate the work.
6. Ambition is balanced with control, assurance, and risk handling.
7. The answer reduces buyer anxiety by showing how IBM protects the client from oversight burden, dependency risk, transition risk, or compliance failure.
8. The response feels operational and staffed, not hypothetical.

## Evidence and Metrics

1. Claims are supported by evidence from source material.
2. Benefits include baseline and measurable outcomes.
3. At least one strong example includes context, timeframe, and impact.
4. Metrics are precise and unambiguous.
5. Partner references explain value, capability contribution, and risk mitigation.
6. Account-specific or incumbent evidence is used before generic proof where available.

## Accuracy and Compliance

1. Every claim is fact-checked against source documents.
2. Unsupported claims are marked with `{{++REPLACE: text}}`.
3. Fabricated content is removed or replaced with verified statements.
4. British English spelling is used consistently.
5. Response avoids empty AI-style filler and unsupported adjective stacking.
6. Response uses no em dashes and avoids en dashes as sentence punctuation.
7. If a word limit applies, the evaluator-facing answer is wrapped with `<!-- START-COUNT -->` and `<!-- END-COUNT -->` markers unless the tender template forbids markdown comments.
8. If a word limit applies, the evaluator-facing answer has been counted with the existing `ibm-bid-word-count` script. Do not use `wc -w`, `pandoc`, editor counts, model-estimated counts, copied snippets, one-off Python, JavaScript, shell pipelines, or custom counting code.
9. If the answer exists only inline, the evaluator-facing answer has been placed in a temporary markdown file with the count markers and counted with the `ibm-bid-word-count` script.
10. Where diagrams/images are used, the final handoff states whether diagram text, labels, captions, and figure titles were treated as included, excluded, or uncertain for word-count purposes.
11. The final handoff includes the exact word-count command, count, limit, and status.

## Readability and Tone

1. Active voice is used throughout.
2. Tone is authoritative, calm, and delivery-ready.
3. Introductory sentence appears before detailed bullet lists.
4. The answer reads like evaluator-facing prose, not a bullet-heavy briefing note.
5. Response is concise and avoids filler.
6. Tone feels authoritative and delivery-ready rather than generic or hesitant.
7. Repeated bid themes or named methods are used deliberately to strengthen coherence, not from habit.
8. Punctuation supports formal evaluator-facing prose: no em dashes, no dash-heavy sentence joins, and no typographic tricks used for emphasis.

## Delivery Readiness

1. Risks and mitigations are covered where relevant.
2. Prerequisites and dependencies are stated where relevant.
3. Deployment timeline and time-to-value are stated where relevant.
4. Scalability and future-proofing are addressed where relevant.
5. Ownership boundaries and client dependencies are made explicit where this improves credibility.
6. The service operating model is clear: who does the work, which processes control it, what data runs or proves it, and which technology enables it.

## Final Gate

1. If a word limit applies, run `ibm-bid-word-count` before evaluation and revise until the counted evaluator-facing answer is compliant.
2. Run `ibm-bid-answer-evaluator`, passing the word-count command/result when a limit applies.
3. If score is below 3, revise and re-evaluate.
4. Only progress when score is 3 or higher.
