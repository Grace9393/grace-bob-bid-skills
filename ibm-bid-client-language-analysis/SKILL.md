---
name: ibm-bid-client-language-analysis
description: Analyse one or more client documents (RFPs, ITTs, strategy documents, annual reports, previous tender responses) to extract client-specific vocabulary, characteristic phrases, tone, and writing style. Use before drafting bid responses when you want the written output to mirror the client's own language rather than defaulting to IBM's internal register. Produces ./tmp/ibm-bid-client-language-analysis.md consumed by ibm-bid-writer. Trigger when the user says "analyse the client's language", "match the client's tone", "write in the client's style", or provides documents beyond the RFP/ITT for language reference.
metadata:
  skills-suggested:
    - ibm-bid-requirements-analysis
    - ibm-bid-hot-buttons
    - ibm-bid-writer
---

# IBM Bid Client Language Analysis

Analyse client documents to build a language profile that `ibm-bid-writer` uses to mirror the client's own vocabulary, tone, and phraseology in bid responses.

## Context Management

Write output to `./tmp/ibm-bid-client-language-analysis.md`. This file is consumed automatically by `ibm-bid-writer` when it exists.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `client_language_analysis_status: complete`
- `client_language_analysis_artifact: ./tmp/ibm-bid-client-language-analysis.md`
- `client_language_analysis_documents`: the source documents analysed for vocabulary, tone, and phraseology
- `artifacts_generated`: include `./tmp/ibm-bid-client-language-analysis.md`

## When to Run

Run this skill when:
- The client has a distinctive writing style worth mirroring (government departments, regulated sectors, clients with house style)
- The RFP or ITT uses specific terminology that must appear in responses
- The user has additional client documents beyond the RFP (strategy papers, annual reports, previous procurement documents, internal comms)
- The user explicitly asks for responses to sound like the client wrote them

Run after `ibm-bid-requirements-analysis` if that has already been completed, so the requirements analysis output can also be mined for language signals.

## Analysis Process

### Step 1: Inventory source documents

List every document being analysed. Note its type and relevance:
- RFP / ITT (primary procurement language)
- Tender specification or schedule (technical vocabulary)
- Client strategy or business plan (strategic framing, priorities language)
- Annual report or accounts (corporate messaging, tone)
- Previous procurement notices or award notices (procurement house style)
- Any other client-authored documents

### Step 2: Extract vocabulary and terminology

Read each document carefully and capture:

**Client-specific terms and acronyms**
- Terms the client uses that differ from IBM's standard vocabulary
- Programme and project names, initiative names, platform names
- Acronyms and initialisms (spell out on first use, then note how the client abbreviates)
- Sector-specific or domain-specific language

**Preferred synonyms**
- Note where the client uses one word consistently when IBM would use another (e.g. "outcomes" vs "results", "colleagues" vs "staff", "procure" vs "buy")
- Build a substitution list: IBM term → client preferred term

**Repeated noun phrases and noun stacks**
- Multi-word compound nouns the client uses repeatedly (e.g. "user-centred design", "continuous service improvement", "in-flight programme")

### Step 3: Identify characteristic phrases

Look for:
- Opening constructions the client favours (e.g. "We will require...", "The successful supplier must...")
- Commitment language (e.g. "We are committed to...", "We expect the supplier to demonstrate...")
- Requirement signalling (e.g. "It is essential that...", "The supplier shall...", "As a minimum...")
- Evaluation language (how the client describes what a good answer looks like)
- Any phrases that appear more than twice across the documents — these are worth mirroring

### Step 4: Assess tone and register

Determine:
- **Formality**: highly formal (legal/government) / formal (enterprise) / semi-formal (commercial)
- **Technical depth**: deeply technical / mixed / non-technical executive language
- **Voice**: predominantly active / predominantly passive / mixed
- **Person**: first person plural ("we") / third person ("the Authority", "the Client") / impersonal ("the supplier shall")
- **Hedging style**: assertive and direct / cautious with qualifiers / prescriptive with obligations
- **Sentence length and structure**: short declarative / long subordinate clause structures / mix

### Step 5: Identify priority and emphasis language

Capture:
- Words used to signal mandatory requirements (e.g. "must", "shall", "required", "essential", "mandatory")
- Words used to signal desirable requirements (e.g. "should", "expected", "preferred", "would benefit from")
- Words used to signal scoring weight (e.g. "critical", "key", "primary", "central", "fundamental")
- Words used to express client anxiety (e.g. "risk", "concern", "challenge", "barrier", "critical dependency")

### Step 6: Identify language to avoid

Note IBM-internal or consultant vocabulary that clashes with this client's register:
- Overused IBM or consulting jargon that does not appear in client documents (e.g. "leverage", "ecosystem", "synergies", "transformation journey", "co-create")
- Technical IBM product names the client has not used and may not recognise
- Register mismatches (e.g. using informal contractions if the client writes formally throughout)

### Step 7: Synthesise writing guidance

Produce a compact, actionable set of rules for `ibm-bid-writer` to follow. Frame these as concrete dos and don'ts, not observations.

## Output Structure

Write `./tmp/ibm-bid-client-language-analysis.md` with this structure:

```markdown
# Client Language Analysis

**Client**: [organisation name]
**Analysed on**: [date]
**Documents analysed**: [count]

## Source Documents

| Document | Type | Language signals |
|----------|------|-----------------|
| [name] | [RFP / Strategy / Annual report / etc.] | [key vocabulary areas or tonal notes] |

## Vocabulary: Use These Terms

| Client's term | Use instead of | Notes |
|---------------|---------------|-------|
| [term] | [IBM/generic equivalent] | [context or frequency] |

## Acronyms and Programme Names

| Acronym / Name | Full form | Notes |
|---------------|-----------|-------|

## Characteristic Phrases

Phrases the client uses repeatedly that should be mirrored or echoed in responses:

- "[exact phrase]" — [context where used]
- "[exact phrase]" — [context where used]

## Requirement Signal Words

| Obligation level | Client's words |
|-----------------|---------------|
| Mandatory | [must, shall, required, ...] |
| Expected | [should, expected, ...] |
| Desirable | [preferred, would welcome, ...] |

## Tone and Register

| Dimension | Assessment | Guidance for writer |
|-----------|-----------|---------------------|
| Formality | [highly formal / formal / semi-formal] | [specific instruction] |
| Voice | [active / passive / mixed] | [specific instruction] |
| Person | [first plural / third / impersonal] | [specific instruction] |
| Technical depth | [deep / mixed / executive] | [specific instruction] |
| Sentence style | [short / long / mixed] | [specific instruction] |
| Hedging | [assertive / cautious / prescriptive] | [specific instruction] |

## Language to Avoid

Terms and phrases that clash with this client's register or do not appear in their documents:

- [term or phrase] — [reason to avoid]
- [term or phrase] — [reason to avoid]

## Writing Rules for ibm-bid-writer

These rules apply to all responses drafted for this client:

1. [Concrete rule, e.g. "Use 'colleagues' not 'staff' or 'employees'"]
2. [Concrete rule, e.g. "Open requirement responses with 'IBM will...' not 'We would...'"]
3. [Concrete rule, e.g. "Mirror the client's use of 'in-flight' for existing programmes"]
4. [Concrete rule, e.g. "Avoid 'leverage' — the client uses 'use' or 'draw on'"]
5. [Continue as needed]
```

## Quality Check Before Saving

Before writing the output file, confirm:

- [ ] Every substitution in the vocabulary table has been verified against client document text
- [ ] Characteristic phrases are direct quotes, not paraphrases
- [ ] Tone assessment is based on observed evidence, not assumed from sector alone
- [ ] Writing rules are specific and actionable, not general statements about style
- [ ] The language to avoid list is grounded in what the client does not write, not just IBM jargon in general

## Integration with ibm-bid-writer

`ibm-bid-writer` checks for `./tmp/ibm-bid-client-language-analysis.md` at the start of each drafting session. When it exists:

1. Apply vocabulary substitutions throughout the draft
2. Match the tone register identified in this analysis
3. Use characteristic phrases where they fit naturally — do not force them
4. Observe the language to avoid list
5. Follow all writing rules listed in the final section

The language analysis does not override bid writing quality standards. Mirroring client language is a technique for resonance, not a substitute for evidence, named mechanisms, and structured proof.
