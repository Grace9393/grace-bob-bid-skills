---
name: ibm-bid-requirements-extractor
description: Extracts and structures requirements, question constraints, and response-format guidance from tender/bid documents or spreadsheets, and produces a requirements processing TODO file at ./tmp/ibm-bid-requirements-extractor.md. Use when given an RFP/ITT/tender document (PDF/DOCX) or requirements spreadsheet (XLSX/CSV/TSV) and asked to extract requirements, question word/page limits, diagram or image allowances, or prepare a requirements checklist.
---

# Ibm Bid Requirements Extractor

## Overview

Create a consistent, ready-to-process requirements TODO file from one or more tender/bid sources, then populate it with extracted requirements, clarifications, and gaps.

## Workflow

### 1) Intake the source

- Confirm the source file path or paths and whether there are multiple documents.
- Identify the source type (PDF/DOCX/XLSX/CSV/TSV). If multiple files, list all inputs in the TODO and de-duplicate repeated requirements across them.
- Ask for scope boundaries if unclear (e.g., include appendices, schedules, annexes).

### 2) Create the TODO file skeleton

Run the helper script to generate the canonical handoff file `./tmp/ibm-bid-requirements_extractor.md`:

```bash
uv run python $SKILL_DIR/scripts/make_requirements_todo.py <source_path> [<source_path> ...]
```

If needed, override the output path:

```bash
uv run python $SKILL_DIR/scripts/make_requirements_todo.py <source_path> [<source_path> ...] --output ./tmp/ibm-bid-requirements-extractor.md --force
```

### 3) Extract requirements from the source

- For PDFs/DOCX, extract text, preserve page or paragraph references, and capture requirement statements verbatim where possible.
- For spreadsheets, map requirement columns (ID, section, requirement text, priority, compliance notes) and preserve row references.
- Extract response-format constraints separately from solution requirements. This includes total response limits, per-question limits, word/page counts, permitted attachments, mandatory templates, and any diagram, image, figure, graphic, table, exhibit, or visual limits.
- Tag each requirement with:
  - ID (from document or generated)
  - Source file
  - Section/paragraph or row reference
  - Type (MUST/SHOULD/MAY or Mandatory/Optional). If unclear, mark `Unclassified`.
  - Evidence pointer (page/row)

### 3a) Extract diagram and image limits

Client guidance on diagrams and images is a mandatory extraction target because downstream wireframes use this as the authority for visual planning.

- Search all source documents for terms including `diagram`, `image`, `figure`, `graphic`, `visual`, `illustration`, `chart`, `table`, `exhibit`, `screenshot`, `caption`, `label`, `word count`, `page limit`, `attachment`, and `template`.
- Capture both total limits and per-question limits:
  - **Total response limit**: e.g. "maximum 5 diagrams across the submission", "no more than 10 images in total", "graphics permitted in appendices only".
  - **Per-question limit**: e.g. "Q3 may include up to 2 diagrams", "one figure may be included in each answer", "Question 5 requires a delivery timeline graphic".
- Preserve whether each limit is mandatory, optional, maximum, minimum, prohibited, or not stated.
- Preserve whether diagram/image text, captions, labels, tables, or figure titles are included in the word count. If unclear, mark `Not stated` rather than inferring.
- Link each visual constraint to the relevant question ID where possible. If the constraint is global, mark the question as `All`.
- If documents conflict on diagram/image limits, record both source references and add a clarification question.

### 4) Populate `./tmp/ibm-bid-requirements-extractor.md`

- Fill the Requirements table with extracted items.
- Fill the Response Constraints table with total and per-question word/page, diagram, image, figure, table, attachment, and template limits.
- Fill the Diagram / Image Limits table with one row per global or question-specific constraint.
- Add clarification questions for ambiguities or missing detail.
- Note risks/gaps (e.g., missing volumes, unclear acceptance criteria).
- Complete the coverage summary with totals, mandatory / optional split, and remaining gaps.
- Update the checklist status.

### 5) Quick validation

- Ensure all extracted requirements map back to a location in the source.
- Confirm each requirement row includes a source file, evidence pointer, and a non-guessed classification.
- Confirm each question has either an extracted diagram/image limit or `Not stated`.
- Confirm global diagram/image limits are captured separately from per-question limits.
- Confirm word-count treatment for diagram/image labels and captions is captured as `Included`, `Excluded`, or `Not stated`.
- Confirm that the TODO file is ready for downstream processing.

## Resources

### scripts/
Use `scripts/make_requirements_todo.py` to generate the initial TODO file at `./tmp/ibm-bid-requirements-extractor.md`.
