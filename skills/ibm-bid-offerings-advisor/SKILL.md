---
name: ibm-bid-offerings-advisor
description: Align a business need or set of requirements to IBM offerings by searching and mapping against the local offerings markdown corpus. Use when a user asks which IBM offerings fit a need, wants a shortlist of offerings, or needs help matching requirements to IBM products/services using the files in $SKILL_DIR/references/offerings.
---

# IBM Offering Advisor

## Overview

Identify the most relevant IBM offerings for a stated business need or requirements set by searching the offerings markdown corpus and mapping capabilities to needs. Keep the output concise: shortlist + fit rationale + gaps/questions.

## Workflow

1. Capture the need
Ask for the business outcome, constraints (industry, geography, budget, time), and any must-have capabilities. If a requirements list exists, use it verbatim.

2. Search the offerings corpus
The offerings are markdown files in:
`$SKILL_DIR/references/offerings`
Each file name is the offering name. Use `rg` to search for key terms and synonyms.

Example searches:
```bash
rg -n "data integration|api management|etl" $SKILL_DIR/references/offerings
rg -n "security|zero trust|iam" $SKILL_DIR/references/offerings
```

3. Build a shortlist
Select 3-6 offerings that directly address the core needs. For each, capture 1-2 lines of evidence from the file (paraphrase, do not quote long passages).

4. Map requirements to offerings
Provide a simple mapping: requirement → offering(s) + rationale. Flag any unmet requirements.

5. Ask clarifying questions
If gaps remain or the shortlist is ambiguous, ask 2-4 targeted questions.

## Output Format

Provide results in this order:
1. Shortlist (offering name + 1-2 sentence fit rationale)
2. Requirements mapping (bulleted list)
3. Gaps/assumptions
4. Clarifying questions (if needed)

## Notes

- Keep it simple and factual. Do not invent capabilities not stated in the offering files.
- If the user provides a requirements document, prefer exact phrasing when mapping.
- If you cannot find matches, say so and propose adjacent offerings or ask for more detail.
