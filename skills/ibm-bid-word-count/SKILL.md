---
name: ibm-bid-word-count
description: Count words in markdown bid responses using IBM's standard tender word-count strategy. Use when a tender, RFP, ITT, proposal response, bid answer, evaluator review, or quality check has a word limit and the answer is written in markdown. Provides a PEP 723 Python script that strips markdown syntax consistently and counts content between `<!-- START-COUNT -->` and `<!-- END-COUNT -->` markers by default, with heading-based and whole-response fallbacks for older drafts.
---

# IBM Bid Word Count

Use this skill whenever a bid response, tender answer, or evaluation needs a word count. Do not use raw markdown `wc -w`, `pandoc`, editor counts, model-estimated counts, copied snippets, one-off Python, or ad hoc shell approximations for bid word-limit checks.

## Non-Negotiable Rule

Run the existing script in this skill. Do not write a new Python script, inline Python command, JavaScript snippet, shell pipeline, regex counter, or manual counting method.

If the answer exists only in chat, first place the evaluator-facing answer content in a temporary markdown file, then run this skill's script against that file. If the script is unavailable, report that the canonical IBM bid word count could not be performed instead of substituting another counting method.

## Standard Command

Count only evaluator-facing answer content by placing the standard count markers around the counted section:

```markdown
<!-- START-COUNT -->

Evaluator-facing answer content goes here.

<!-- END-COUNT -->
```

Then run:

```bash
uv run python $SKILL_DIR/scripts/count_words_in_markdown.py <DOC>
```

The marker comments themselves are never counted. If both markers are present, the script counts only the content between them and ignores `--from-heading` / `--until-heading` arguments. If only one marker is present, the script fails rather than silently counting the wrong content.

For older drafts that do not have count markers, count content after a heading such as `## Answer:`:

```bash
uv run python $SKILL_DIR/scripts/count_words_in_markdown.py --from-heading "## Answer:" <DOC>
```

For older drafts, count a bounded section between two headings:

```bash
uv run python $SKILL_DIR/scripts/count_words_in_markdown.py --from-heading "## Answer:" --until-heading "## Evidence Log" <DOC>
```

If the document has front matter, it is never counted. The script recognises `min-word-count` and `max-word-count` values:

```markdown
---
min-word-count: 100
max-word-count: 1000
---
```

Print the count with those limits and an under/within/over status:

```bash
uv run python $SKILL_DIR/scripts/count_words_in_markdown.py --show-limits <DOC>
```

If the tender requires the whole markdown response to count and the document contains count markers that should be ignored, use `--ignore-count-markers`:

```bash
uv run python $SKILL_DIR/scripts/count_words_in_markdown.py --ignore-count-markers <DOC>
```

If the response uses custom count markers, pass them with `--start-marker` and `--end-marker`. If the response uses different section headings and no markers, replace `## Answer:` and `## Evidence Log` with the exact headings. `--until-heading` excludes the matched heading and anything after it. Add `--include-heading` only if the tender requires the start heading to count. Exclude notes, evidence logs, planning text, evaluator feedback, and source appendices unless the tender explicitly says they count.

## Counting Strategy

The script uses `count_words_in_markdown(markdown)` as the canonical strategy:

```python
import re


FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|\Z)", re.DOTALL)
DEFAULT_START_MARKER = "<!-- START-COUNT -->"
DEFAULT_END_MARKER = "<!-- END-COUNT -->"


def split_front_matter(markdown):
    match = FRONT_MATTER_RE.match(markdown)
    if not match:
        return {}, markdown

    limits = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            continue
        key = key.strip()
        if key not in {"min-word-count", "max-word-count"}:
            continue
        value = value.strip().strip("\"'")
        try:
            limits[key] = int(value)
        except ValueError:
            continue

    return limits, markdown[match.end():]


def count_words_in_markdown(markdown):
    _, text = split_front_matter(markdown)

    # Comments
    text = re.sub(r'<!--(.*?)-->', '', text, flags=re.MULTILINE)
    # Tabs to spaces
    text = text.replace('\t', '    ')
    # More than 1 space to 4 spaces
    text = re.sub(r'[ ]{2,}', '    ', text)
    # Footnotes
    text = re.sub(r'^\[[^]]*\][^(].*', '', text, flags=re.MULTILINE)
    # Indented blocks of code
    text = re.sub(r'^( {4,}[^-*]).*', '', text, flags=re.MULTILINE)
    # Custom header IDs
    text = re.sub(r'{#.*}', '', text)
    # Replace newlines with spaces for uniform handling
    text = text.replace('\n', ' ')
    # Remove images
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
    # Remove HTML tags
    text = re.sub(r'</?[^>]*>', '', text)
    # Remove special characters
    text = re.sub(r'[#*`~\-–^=<>+|/:]', '', text)
    # Remove footnote references
    text = re.sub(r'\[[0-9]*\]', '', text)
    # Remove enumerations
    text = re.sub(r'[0-9#]*\.', '', text)

    return len(text.split())


def extract_between_markers(markdown, start_marker=DEFAULT_START_MARKER, end_marker=DEFAULT_END_MARKER):
    start_index = markdown.find(start_marker)
    end_index = markdown.find(end_marker)

    if start_index == -1 and end_index == -1:
        return markdown, False
    if start_index == -1:
        raise ValueError(f"Found {end_marker!r} without {start_marker!r}.")
    if end_index == -1:
        raise ValueError(f"Found {start_marker!r} without {end_marker!r}.")
    if end_index < start_index:
        raise ValueError(f"Found {end_marker!r} before {start_marker!r}.")

    return markdown[start_index + len(start_marker):end_index], True
```
