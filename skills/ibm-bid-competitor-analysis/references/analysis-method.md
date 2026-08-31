# Competitor Analysis Method

Use this method for bid-stage competitor analysis and black-hat review.

If the analysis needs current public facts, read `web-research.md` and incorporate public-source intelligence using its source hierarchy and attribution rules.

## Modes

Choose one mode before starting:

1. `named-competitor`
   Review a specific rival such as Accenture, Deloitte, PwC, TCS, Capgemini, or the incumbent.
2. `incumbent-defence`
   Focus on why the current supplier is dangerous and how they will try to retain.
3. `open-field`
   Infer the most likely bidder set from the procurement context and evaluation logic.
4. `draft-black-hat`
   Review IBM draft content from a competitor perspective and identify exploitable weaknesses.

## Evidence Model

Classify key assertions with one of these labels:

- `Evidenced`: directly supported by tender text, client history, known framework position, or provided material
- `Inferred`: reasoned from evidence but not explicitly stated
- `Assumed`: plausible working assumption with weak evidence

Do not present inferred or assumed statements as fact.

## Workflow

1. Define the buyer decision frame.
   Capture the client outcomes, mandatory requirements, weighted criteria, risk posture, commercial model, and likely political considerations.
2. Define the competitor set.
   Prefer named rivals only when evidence supports them. Otherwise use archetypes such as incumbent, global SI, platform specialist, niche SME, or low-cost challenger.
   If current public signals matter, gather them before locking the competitor set.
3. Score each competitor across decisive lenses.
   Use the lens set below and keep scoring relative to this specific procurement, not generic market reputation.
4. Build competitor hypotheses.
   State what each rival is likely to lead with, where they are vulnerable, and which buyer anxieties they can exploit.
   Use public-source research where it materially changes the hypothesis, and attribute those points clearly.
5. Run the black-hat pass.
   Ask how the competitor would criticise IBM's offer, evidence, pricing, delivery plan, and credibility.
6. Translate into IBM action.
   Recommend response changes, proof insertions, clarifications, commercial guardrails, and stakeholder actions.

## Scoring Lenses

Use a simple `High`, `Medium`, `Low` strength rating unless the user asks for numeric scoring.

Assess each priority competitor on:

1. Buyer fit
2. Relationship position
3. Offer relevance
4. Delivery credibility
5. Commercial attractiveness
6. Proof strength
7. Attack potential against IBM
8. Exposure to IBM counter-attack

## Black-Hat Questions

Use these to sharpen the analysis:

1. What will this competitor say to make the buyer feel safe?
2. What will this competitor say to make IBM look risky, expensive, slow, or generic?
3. Which evaluation questions naturally favour this competitor today?
4. Where is IBM under-evidenced relative to this rival?
5. Which one or two counter-moves would most reduce this competitor's advantage?

## Output Contract

Produce these sections in order:

1. `Situation Summary`
   State opportunity type, evidence base, and confidence level.
   Note whether public web research was used.
2. `Likely Competitors`
   Rank the top threats and explain why they matter.
3. `Competitor Cards`
   For each priority rival, include likely win path, strengths, vulnerabilities, and confidence.
4. `Likely Attack Lines On IBM`
   State what the competitor will probably claim and where that claim could land with the buyer.
5. `IBM Counter-Positioning`
   State how IBM should respond in narrative, solution, proof, and commercial posture.
6. `Response Surgery`
   Recommend concrete edits to draft answers, win themes, architecture narrative, evidence selection, or pricing framing.
7. `Priority Actions`
   End with the few actions that most change win probability.

If public research materially affected the conclusion, also include:

8. `Public-Source Signals`
   Summarise the few sourced external facts that changed the analysis.
9. `Source Confidence Notes`
   State where the external evidence is strong, mixed, or thin.

## Fail-Closed Rules

- If the likely competitor set is weakly evidenced, say that the field is hypothetical.
- If the buyer criteria are unclear, say which assumptions are driving the competitor view.
- If there is no credible basis to distinguish named competitors, collapse the analysis to archetypes.
- If the input is a draft answer only, assess attack surface rather than pretending to know the full competitive field.
