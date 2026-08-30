---
name: ibm-bid-strategy-and-capabilities-2026
description: "Use this skill when writing tender responses, proposals, or bids that require IBM capabilities, strategic positioning, or differentiators. Use when: (1) Answering tender questions on AI, cloud, cybersecurity, Salesforce, integration, or delivery methodology, (2) Articulating IBM's unique value proposition or why-IBM differentiation, (3) Citing IBM's Client Zero internal transformation as proof of AI at enterprise scale ($3.5B productivity savings across 15+ business and IT domains with named tools and quantified metrics), (4) Referencing IBM's 2026 strategy — Consulting Advantage AI platform, Seven Bets framework, IBM Research Technology Atlas (roadmaps to 2030+), or Science of Consulting positioning, (5) Finding proof points, metrics, or named assistants (AskHR, AskIT, COPRA, watsonx Orchestrate) to substantiate any IBM capability claim."
---

# IBM Strategy and Capabilities Knowledge Base

Specialist routing layer for IBM strategic information and capabilities in tender responses and proposals.

The source content for this skill is consolidated into `ibm-bid-library` as the durable custom collection:

- Category: `IBM Strategy and Capabilities 2026`
- Batch/tag: ibm-strategy-capabilities-2026 collection marker
- Durable source: `skills/ibm-bid-library/custom-docs/ibm-strategy-and-capabilities-2026/`
- Replay manifest: `skills/ibm-bid-library/src/custom-documents.yaml`

Use this skill to decide what to search for and how to apply the results. Use `ibm-bid-library` to retrieve and cite the actual source records.

## Context Management

Write output to `./tmp/ibm-bid-strategy-and-capabilities-2026.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

## Retrieval Workflow

1. Identify the capability areas required by the tender question.
2. Use `ibm-bid-library` to search within the `IBM Strategy and Capabilities 2026` category or the strategy capabilities collection tag.
3. Retrieve the most relevant bid-library records with `get.py`.
4. Extract specific differentiators, metrics, named assets, and proof points.
5. Cite every source record using the bid-library citation format.
6. Apply the content to the tender response using the client's terminology.

For proof of scale or internal deployment, always search for Client Zero material as well as the capability topic. Questions about IBM practising what it preaches, internal transformation, AI/automation at enterprise scale, or named internal tools such as AskHR, AskIT, COPRA, watsonx Orchestrate, Turbonomic, Apptio, or Maximo should include Client Zero evidence.

## Search Routing

Use these query intents with `ibm-bid-library`. Include `IBM Strategy and Capabilities 2026` in the search terms when you need to constrain results to this curated collection.

| Tender Need | Search Terms |
|-------------|--------------|
| AI/ML capabilities | `IBM Strategy and Capabilities 2026 AI automation machine learning watsonx generative AI` |
| Cloud services | `IBM Strategy and Capabilities 2026 cloud hybrid cloud infrastructure platform services` |
| Security | `IBM Strategy and Capabilities 2026 cybersecurity threat detection security operations zero trust` |
| Data protection | `IBM Strategy and Capabilities 2026 data security privacy GDPR information governance` |
| Delivery methodology | `IBM Strategy and Capabilities 2026 IBM Garage agile co-creation design thinking delivery methodology` |
| Global delivery | `IBM Strategy and Capabilities 2026 globally integrated capabilities delivery centres offshore nearshore` |
| Hybrid cloud and AI | `IBM Strategy and Capabilities 2026 hybrid cloud AI integration multi-cloud watsonx` |
| Research and benchmarks | `IBM Strategy and Capabilities 2026 IBV research benchmarks thought leadership` |
| Industry expertise | `IBM Strategy and Capabilities 2026 industry expertise healthcare government finance sector` |
| Innovation and R&D | `IBM Strategy and Capabilities 2026 IBM Research innovation patents emerging technology` |
| Salesforce | `IBM Strategy and Capabilities 2026 Salesforce CRM MuleSoft clouds implementation` |
| Integration | `IBM Strategy and Capabilities 2026 integration APIs middleware MuleSoft system integration` |
| Why IBM / differentiation | `IBM Strategy and Capabilities 2026 why IBM Consulting strategy Science of Consulting Consulting Reimagined` |
| Consulting Advantage | `IBM Strategy and Capabilities 2026 Consulting Advantage AI assistants delivery productivity watsonx` |
| Strategic trends | `IBM Strategy and Capabilities 2026 Seven Bets AI-first enterprise sustainability supply chain talent` |
| Technology roadmaps | `IBM Strategy and Capabilities 2026 Research Technology Atlas roadmap 2030 AI automation quantum security` |
| Client success stories | `IBM Strategy and Capabilities 2026 client success stories quantified outcomes industry` |
| Client Zero | `IBM Strategy and Capabilities 2026 Client Zero AskHR AskIT COPRA productivity savings internal transformation` |
| Products and assets | `IBM Strategy and Capabilities 2026 offerings assets accelerators reusable tools` |

## Integration with Other Skills

This skill works best when combined with:

- **ibm-bid-writer**: Use capabilities as source material for tender responses
- **ibm-bid-win-themes**: Reference differentiators when developing win themes
- **ibm-bid-requirements-analysis**: Match capabilities to identified client needs
- **ibm-bid-customer-stories**: Pair capabilities with relevant case studies for evidence
- **ibm-bid-answer-evaluator**: Verify capability claims in responses are accurate

## Tender Question-Type Mapping

Quick reference for selecting capability files based on common tender question types:

| Question Topic | Primary Search | Secondary Search |
|---------------|----------------|------------------|
| Security and compliance | `cybersecurity security operations zero trust` | `data security privacy GDPR governance` |
| AI and automation | `AI automation watsonx generative AI` | `Client Zero internal transformation productivity savings` |
| Cloud infrastructure | `cloud infrastructure platform services hybrid cloud` | `multi-cloud AI integration` |
| Integration and APIs | `integration APIs middleware MuleSoft` | `Salesforce MuleSoft CRM` |
| Delivery methodology | `IBM Garage agile co-creation design thinking` | `global delivery centres offshore nearshore` |
| Industry experience | `industry expertise sector healthcare government finance` | `client success stories quantified outcomes` |
| Innovation and R&D | `IBM Research innovation patents emerging technology` | `Technology Atlas IBV benchmarks` |
| Salesforce and CRM | `Salesforce CRM clouds implementation` | `integration MuleSoft APIs` |
| Data privacy and GDPR | `data security privacy GDPR` | `cybersecurity controls governance` |
| Global delivery | `globally integrated capabilities delivery centres` | `IBM Garage delivery methodology` |
| Proof of scale | `Client Zero AskHR AskIT COPRA internal transformation` | `watsonx Turbonomic Apptio Maximo productivity` |
| Why IBM / differentiation | `why IBM Consulting strategy Science of Consulting` | `Consulting Advantage AI platform productivity` |
| Consultant productivity / AI tools | `Consulting Advantage AI assistants delivery productivity` | `AI automation watsonx` |
| Strategic vision / future trends | `Seven Bets AI-first enterprise sustainability supply chain talent` | `Research Technology Atlas roadmap 2030` |
| Quantum / emerging technology | `Technology Atlas quantum emerging technology` | `IBM Research innovation` |
| Named client references | `client success stories quantified outcomes` | `industry expertise sector` |

### Common Question Patterns

**"Describe your security approach"**
→ Search: `IBM Strategy and Capabilities 2026 cybersecurity data security privacy GDPR`

**"How will you deliver AI/automation?"**
→ Search: `IBM Strategy and Capabilities 2026 AI automation Consulting Advantage Client Zero`

**"What is your delivery methodology?"**
→ Search: `IBM Strategy and Capabilities 2026 IBM Garage agile global delivery`

**"Demonstrate relevant experience"**
→ Search: `IBM Strategy and Capabilities 2026 client success stories industry expertise`

**"How do you ensure data protection?"**
→ Search: `IBM Strategy and Capabilities 2026 data security privacy GDPR cybersecurity`

**"Why choose IBM Consulting?"**
→ Search: `IBM Strategy and Capabilities 2026 why IBM Consulting strategy Consulting Advantage`

**"What is your technology roadmap / future-proofing?"**
→ Search: `IBM Strategy and Capabilities 2026 Research Technology Atlas Seven Bets roadmap`

**"Provide evidence of productivity / AI at scale"**
→ Search: `IBM Strategy and Capabilities 2026 Client Zero productivity savings AskHR AskIT COPRA`
