#!/usr/bin/env python3
"""Generate a lightweight bid-response planning scaffold from a tender question."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


THEME_MAP = [
    (("security", "clinical safety", "privacy", "compliance", "standard"), ["standards by design", "safe innovation", "service integrity"]),
    (("mobilisation", "transition", "handover", "standdown", "exit"), ["continuity", "low supervision", "controlled transition"]),
    (("value", "cost", "commercial", "efficiency", "productivity"), ["value for money", "measurable productivity", "service integrity"]),
    (("integration", "api", "supplier", "interoperability"), ["integration readiness", "safe innovation", "continuity"]),
    (("user", "design", "accessibility", "patient"), ["user-centred delivery", "safe innovation", "standards by design"]),
]


def read_question(args: argparse.Namespace) -> str:
    if args.question:
        return args.question.strip()
    if args.question_file:
        return Path(args.question_file).read_text(encoding="utf-8").strip()
    raise SystemExit("Provide --question or --question-file")


def choose_archetype(text: str) -> str:
    low = text.lower()
    if any(k in low for k in ("standard", "security", "clinical safety", "compliance", "wcag")):
        return "Standards, security, or compliance"
    if any(k in low for k in ("mobilis", "transition", "handover", "standdown", "exit")):
        return "Mobilisation or transition"
    if any(k in low for k in ("team", "capability", "capabilities", "profile", "profiles", "fit", "resource", "resources", "leadership", "role", "roles")):
        return "Capability or team-fit"
    if any(k in low for k in ("social value", "commitment", "community", "apprentice")):
        return "Social value or commitments"
    if any(k in low for k in ("challenge", "uncertaint", "risk", "value for money", "commercial")):
        return "Challenges, uncertainties, or value for money"
    return "Technical or delivery approach"


def infer_structure_pattern(archetype: str) -> str:
    if archetype == "Standards, security, or compliance":
        return "Confidence section plus standards categories and assurance workflow"
    if archetype == "Mobilisation or transition":
        return "Confidence section plus phased plan and transition controls"
    if archetype == "Capability or team-fit":
        return "Confidence section plus role-to-relevance or responsibility table"
    if archetype == "Social value or commitments":
        return "Confidence section plus commitments and activities blocks"
    if archetype == "Challenges, uncertainties, or value for money":
        return "Challenge statement plus plan-to-address or mitigation blocks"
    return "Confidence section plus bold-labelled mechanism blocks"


def infer_evidence_form(text: str, archetype: str) -> str:
    low = text.lower()
    if archetype == "Capability or team-fit":
        return "Table mapping role, experience, or responsibility to relevance"
    if archetype == "Social value or commitments":
        return "Commitment and activities blocks, often supported by tables"
    if archetype == "Mobilisation or transition":
        return "Phased plan with compact control and evidence paragraphs"
    if archetype == "Challenges, uncertainties, or value for money":
        return "Challenge and mitigation blocks with precedent and measured impact"
    if archetype == "Standards, security, or compliance":
        return "Confidence summary bullets followed by standards categories and assurance blocks"
    if any(k in low for k in ("why you should have full confidence", "full confidence", "summary", "overview")):
        return "Confidence summary bullets"
    return "Bold-labelled mechanism blocks with compact supporting evidence"


def infer_concern(text: str, archetype: str) -> tuple[str, list[str], str]:
    low = text.lower()
    if archetype == "Standards, security, or compliance":
        return (
            "IBM must show it can deliver change quickly without losing control of standards, security, accessibility, or clinical assurance.",
            ["Compliance drift", "Assurance bottlenecks", "Unsafe or non-compliant innovation"],
            "A high score will need clear standards-by-design methods, named assurance roles, and proof from live regulated services.",
        )
    if archetype == "Mobilisation or transition":
        return (
            "IBM must show it can take over or transition the service without disruption, knowledge loss, or slowdown.",
            ["Service interruption", "Weak knowledge transfer", "Slow time to productivity"],
            "A high score will need a credible transition method, continuity plan, and early controls for knowledge, governance, and service stability.",
        )
    if archetype == "Capability or team-fit":
        return (
            "IBM must prove the named team has the depth, relevance, and flexibility to meet the service need.",
            ["Thin capability bench", "Role mismatch", "Over-reliance on a few individuals"],
            "A high score will need named leaders, relevant backgrounds, and a clear explanation of how the capability mix fits the requirement.",
        )
    if archetype == "Social value or commitments":
        return (
            "IBM must prove the commitments are measurable, governed, and realistically deliverable rather than generic promises.",
            ["Unmeasurable commitments", "Weak accountability", "Poor link to contract delivery"],
            "A high score will need quantified commitments, a delivery framework, named accountability, and reporting mechanisms.",
        )
    if archetype == "Challenges, uncertainties, or value for money":
        return (
            "IBM must show it understands the real delivery and commercial pressures and has credible mitigations that protect service integrity.",
            ["Cost without value", "Underplayed risk", "Innovation that adds instability"],
            "A high score will need clear challenge statements, mitigations, evidence of savings or throughput improvement, and controls that protect critical services.",
        )
    primary = "IBM must show it can deliver the required outcomes at pace while keeping the service stable, governed, and low risk."
    secondaries = ["Generic delivery method", "Weak proof of control", "Insufficient differentiation"]
    score = "A high score will need a direct answer, named delivery mechanisms, evidence of comparable delivery, and clear buyer value."
    if "minimum supervision" in low:
        primary = "IBM must prove it can operate with minimal supervision while still giving the client visibility and control."
    return primary, secondaries, score


def infer_confidence_case(text: str, archetype: str) -> str:
    if archetype == "Mobilisation or transition":
        return "IBM can be trusted here because it combines service continuity, a named transition method, and proven mobilisation controls that reduce disruption from day one."
    if archetype == "Standards, security, or compliance":
        return "IBM can be trusted here because it has proven delivery in regulated public services and uses named assurance mechanisms that embed compliance into delivery rather than bolting it on later."
    if archetype == "Capability or team-fit":
        return "IBM can be trusted here because the proposed team blends current account knowledge, named specialist capability, and the ability to scale without weakening delivery."
    if archetype == "Social value or commitments":
        return "IBM can be trusted here because the commitments are tied to named accountability, measurable targets, and an operating framework rather than goodwill statements."
    if archetype == "Challenges, uncertainties, or value for money":
        return "IBM can be trusted here because it links improvement and cost control to explicit mechanisms, measured outcomes, and protections for service continuity."
    return "IBM can be trusted here because it combines proven delivery, named operating mechanisms, and measurable outcomes that reduce risk for the client."


def infer_confidence_heading(archetype: str) -> str:
    if archetype in {
        "Technical or delivery approach",
        "Standards, security, or compliance",
        "Mobilisation or transition",
        "Capability or team-fit",
        "Social value or commitments",
    }:
        return "Why you should have full confidence in our proposal"
    return "Why IBM's approach is credible and low risk"


def infer_confidence_bullets(archetype: str, themes: list[str], mechanisms: list[str]) -> list[str]:
    bullets: list[str] = []
    if archetype == "Standards, security, or compliance":
        bullets.extend(
            [
                "We embed standards and assurance into delivery rather than treating them as late-stage gates.",
                "We combine regulated-service experience with named assurance roles, controls, and monitoring.",
                "We make innovation safe by pairing change with clinical, security, and compliance discipline.",
            ]
        )
    elif archetype == "Mobilisation or transition":
        bullets.extend(
            [
                "We protect continuity through a named transition method and retained service knowledge.",
                "We accelerate time to productivity with structured onboarding, governance, and early controls.",
                "We reduce transition risk by making knowledge transfer, service stability, and decision rights explicit.",
            ]
        )
    elif archetype == "Capability or team-fit":
        bullets.extend(
            [
                "We bring relevant leadership, specialist depth, and the ability to flex capacity without weakening delivery.",
                "We reduce dependency risk through a deliberate capability mix, communities of practice, and mentoring.",
                "We align resourcing to the service shape rather than offering a generic bench of skills.",
            ]
        )
    elif archetype == "Social value or commitments":
        bullets.extend(
            [
                "We tie every commitment to named accountability, measurable targets, and a timed action plan.",
                "We connect social value delivery directly to workforce capability, contract performance, and reporting.",
                "We make commitments credible through operating mechanisms rather than goodwill statements.",
            ]
        )
    elif archetype == "Challenges, uncertainties, or value for money":
        bullets.extend(
            [
                "We identify the delivery and commercial pressures clearly rather than treating them as abstract risk.",
                "We protect service integrity by pairing efficiency measures with explicit controls and mitigations.",
                "We support value-for-money claims with precedent, mechanisms, and measurable impact.",
            ]
        )
    else:
        bullets.extend(
            [
                "We combine continuity, proven delivery, and named operating mechanisms that reduce execution risk.",
                "We accelerate delivery through explicit governance, cadence, and delivery controls rather than generic methodology claims.",
                "We translate delivery method into service outcomes, visibility, and value for money.",
            ]
        )

    for theme in themes:
        candidate = f"We reinforce the bid theme of {theme} through explicit mechanisms and delivery proof."
        if len(bullets) >= 4:
            break
        if candidate not in bullets:
            bullets.append(candidate)

    if len(bullets) < 4 and mechanisms:
        bullets.append(
            f"We make the approach believable through named mechanisms such as {', '.join(mechanisms[:3])}."
        )

    return bullets[:4]


def infer_mechanisms(text: str, archetype: str) -> list[str]:
    low = text.lower()
    mechanisms: list[str] = []
    if archetype == "Mobilisation or transition":
        mechanisms.extend(["Named transition method", "Knowledge transfer plan", "Mobilisation governance cadence", "Early productivity or onboarding accelerator"])
    elif archetype == "Standards, security, or compliance":
        mechanisms.extend(["Standards-by-design method", "Named assurance roles and forums", "Compliance checkpoints in delivery lifecycle", "Monitoring or dashboard for compliance health"])
    elif archetype == "Capability or team-fit":
        mechanisms.extend(["Capability mix model", "Named leadership roles", "Resourcing and flex model", "Communities of practice or mentoring structure"])
    elif archetype == "Social value or commitments":
        mechanisms.extend(["Social value delivery framework", "Named accountable lead", "Timed action plan", "Measurement and reporting tool"])
    elif archetype == "Challenges, uncertainties, or value for money":
        mechanisms.extend(["Commercial review forum", "Continuous improvement plan", "Alternative delivery model", "Risk and assurance controls"])
    else:
        mechanisms.extend(["Delivery lifecycle", "Sprint or operating cadence", "Governance forum or board", "Balanced dashboard or scorecard"])

    if "partner" in low or "supplier" in low or "integration" in low:
        mechanisms.append("Partner or ecosystem engagement model")
    return mechanisms[:4]


def infer_themes(text: str) -> list[str]:
    low = text.lower()
    themes: list[str] = []
    for keywords, mapped in THEME_MAP:
        if any(keyword in low for keyword in keywords):
            for theme in mapped:
                if theme not in themes:
                    themes.append(theme)
    default = ["continuity", "low supervision", "safe innovation", "value for money"]
    for theme in default:
        if theme not in themes:
            themes.append(theme)
    return themes[:4]


def infer_terms(text: str) -> list[str]:
    matches = re.findall(r"\b(?:Schedule|Sch\.|SOW|SLA|KPI|OKR|GDS|NHS|WCAG|ISO|DCB\d+|FHIR|API)\b[\w\.\-+ ]*", text)
    deduped = []
    for item in matches:
        cleaned = " ".join(item.split())
        if cleaned and cleaned not in deduped:
            deduped.append(cleaned)
    return deduped[:8]


def make_how_we_heading(fragment: str) -> str:
    cleaned = " ".join(fragment.strip(" -.;:").split())
    cleaned = re.sub(r"^(please\s+)?(describe|explain|set out|provide|outline|detail|confirm)\s+(how\s+)?", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^(your|the|a|an)\s+", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^(you|we)\s+(will|would|can|shall)\s+", r"\2 ", cleaned, flags=re.IGNORECASE)
    if not cleaned:
        return "How we will address this requirement"
    if cleaned.lower().startswith("how "):
        cleaned = cleaned[4:]
    if cleaned.lower().startswith("we "):
        return f"How {cleaned}"
    if cleaned.lower().startswith(("will ", "would ", "can ")):
        return f"How we {cleaned}"
    if re.match(r"^(conduct|manage|deliver|provide|ensure|support|maintain|apply|use|create|develop|implement|monitor|report|govern|mobilise|transition|integrate|test|assure|improve)\b", cleaned, re.IGNORECASE):
        return f"How we will {cleaned[0].lower()}{cleaned[1:]}"
    return f"How we will address {cleaned[0].lower()}{cleaned[1:]}"


def infer_wireframe_headings(text: str) -> list[str]:
    candidates = re.split(r"(?:\n\s*(?:[-*]|\d+[\.\)])\s+|;|\n{2,}|(?:\s+and\s+)?\bhow you will\b)", text)
    headings = ["How we've structured our response"]
    for candidate in candidates:
        cleaned = " ".join(candidate.split())
        if len(cleaned) < 18:
            continue
        heading = make_how_we_heading(cleaned)
        if heading not in headings:
            headings.append(heading)
        if len(headings) >= 6:
            break
    if len(headings) == 1:
        headings.append(make_how_we_heading(text))
    return headings[:6]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--question")
    parser.add_argument("--question-file")
    parser.add_argument(
        "--mode",
        choices=["formal", "conversational"],
        default="formal",
        help="Writing mode scaffold. Defaults to formal scored-response mode.",
    )
    args = parser.parse_args()

    question = read_question(args)
    archetype = choose_archetype(question)
    structure_pattern = infer_structure_pattern(archetype)
    evidence_form = infer_evidence_form(question, archetype)
    concern, secondary, high_score = infer_concern(question, archetype)
    confidence = infer_confidence_case(question, archetype)
    mechanisms = infer_mechanisms(question, archetype)
    themes = infer_themes(question)
    confidence_heading = infer_confidence_heading(archetype)
    confidence_bullets = infer_confidence_bullets(archetype, themes, mechanisms)
    terms = infer_terms(question)
    wireframe_headings = infer_wireframe_headings(question)

    mode_label = (
        "formal scored-response mode"
        if args.mode == "formal"
        else "conversational drafting mode"
    )

    out = f"""# Bid Response Plan

## Mode
- Writing mode: {mode_label}
- Why this mode is appropriate: {"Default for evaluator-facing bid content." if args.mode == "formal" else "Use only for internal shaping before converting to formal scored-response prose."}

## Question
- Reference:
- Raw question or summary: {question}

## Evaluator Concern
- Primary concern: {concern}
"""  # noqa: E501
    for item in secondary:
        out += f"- Secondary concerns: {item}\n"
    out += f"- What a high score probably requires: {high_score}\n\n"

    out += f"""## Confidence Summary Section
- Use a document-level confidence section: yes
- Proposed heading: {confidence_heading}
- Framing paragraph focus: State why IBM is credible on this topic now and preview the proof themes that matter most to the evaluator.
"""
    for idx, item in enumerate(confidence_bullets, start=1):
        out += f"- Preview bullet {idx}: {item}\n"

    out += f"""

## Confidence Case
- One-sentence confidence opener: {confidence}
- Why IBM is credible on this topic now:

## Wireframe Sub-Heading Structure
- Source: generated during planning unless a user-provided or `./tmp/` wireframe supersedes it
- Preserve exact wireframe headings in final answer: yes
"""
    for idx, heading in enumerate(wireframe_headings, start=1):
        out += f"- Heading {idx}: {heading}\n"

    out += """
## Named Mechanisms
"""
    for idx, item in enumerate(mechanisms, start=1):
        out += f"- Mechanism {idx}: {item}\n"

    out += """
## Evidence Stack
- Account-specific or incumbent evidence:
- Named team or leader credibility:
- Relevant public sector or NHS precedent:
- Broader IBM capability proof:
- Metrics, quotes, or outcomes to use:

## Repeated Bid Themes
"""
    for idx, item in enumerate(themes, start=1):
        out += f"- Theme {idx}: {item}\n"

    out += f"""
## Draft Shape
- Recommended response archetype: {archetype}
- Recommended internal structure pattern: {structure_pattern}
- Output format: `## Part 1: Sub-Headings Structure` followed by `## Part 2: Written Response`
- Prose plan: Write Part 2 in flowing prose paragraphs by default. Convert method, rationale, governance, assurance, and delivery-sequence detail into prose rather than bullets.
- Bullet justification: bullets are banned in Part 2 unless the question explicitly enumerates discrete parallel items or the user requests bullets. No Part 2 bullet list is pre-authorised by this scaffold.
- Likely evidence form: {evidence_form}
- Required headings or sub-sections:
- Wireframe headings to use as actual answer sections: {", ".join(wireframe_headings)}
- Risks and mitigations to cover:
- Ownership boundaries or dependencies to state:

## Diagram / Visual Composition
- Client diagram/image requirement from wireframe or extractor:
- Diagram count to use:
- Diagram type(s):
- Diagram word count treatment: Included / Excluded / Confirm
- Composition choice: prose only / diagram plus concise prose / table plus prose / diagram plus table plus prose
- Content moved into diagram rather than prose:
- Prose that remains necessary to interpret the diagram:
- Caption or label budget:
- Follow-on `ibm-bid-image-definer` needed: yes / no

## Draft Reminders
"""
    if terms:
        out += f"- Phrases or terminology to mirror: {', '.join(terms)}\n"
    else:
        out += "- Phrases or terminology to mirror:\n"
    out += "- Claims that need fact-checking:\n"
    out += "- Weak spots or missing evidence:\n"

    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
