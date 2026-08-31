---
name: ibm-bid-answer-evaluator
description: Use this skill when the user asks you to evaluate, review, score, or assess a tender question response or answer. This skill provides a structured evaluation framework to assess the quality and completeness of tender responses against specific criteria.
metadata:
  skills-required:
    - ibm-bid-word-count
  skills-suggested:
    - ibm-bid-writer
    - ibm-bid-requirements-analysis
    - ibm-bid-client-language-analysis
---

# Bid Answer Evaluator Skill

This skill helps you evaluate tender question responses using a comprehensive, structured approach that assesses relevance, comprehensiveness, client knowledge, and alignment with proposal principles.


## Context Management

Write output to `./tmp/ibm-bid-responses/evaluation_report.md` when the user asks for persisted artifacts or when maintaining evaluation history for chained skills. For a comprehensive final pass, write to `./tmp/ibm-bid-final-evaluation.md` when requested. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

Update state checkpoint: `./tmp/ibm-bid-project.md` with:
- `evaluation_status`: pass, revise, in_progress, or final_complete
- `evaluation_artifact: ./tmp/ibm-bid-responses/evaluation_report.md`
- `latest_evaluation_score`: latest score or score summary
- `final_evaluation_artifact: ./tmp/ibm-bid-final-evaluation.md` when a final pass is written
- `artifacts_generated`: include evaluation artifacts when written
- `next_skill_recommendation`: normally `ibm-bid-writer` for revisions or `ibm-bid-tda-review` / submission readiness for a passing final response

Preserve any existing `client_language_analysis_status`, `client_language_analysis_artifact`, and `client_language_analysis_documents` fields.

## Workflow

When asked to evaluate a tender response:

1. **Understand the Question Context**
   - Carefully read the tender question to understand what is being asked
   - Consider what the client's concerns and priorities might be
   - Identify all required components and sub-questions that need to be addressed
   - If the question concerns a service, interpret "service" as the full operating model: people, process, data, and technology. Do not assess it as a technology-only or delivery-process-only question unless the tender explicitly narrows the scope.

2. **Gather Necessary Context**
   - Request or identify the client context document (if available)
   - Request or identify the proposal name and principles
   - Ensure you have both the tender question and the proposed answer to evaluate
   - Check `./tmp/ibm-bid-project.md` for `client_language_analysis_artifact`; if present, read that file. If the tracker is missing or no artifact path is recorded, fall back to `./tmp/ibm-bid-client-language-analysis.md`. Use the language profile to evaluate whether the response mirrors the client's vocabulary, characteristic phrases, tone, and language-to-avoid rules.
   - If `./tmp/ibm-bid-approved-customer-stories.md` exists, treat it as the control point for permitted customer story references
   - If the tender question, response template, evaluation criteria, or writer handoff contains a word limit, load `ibm-bid-word-count`. If the writer supplied a word-count command and result, verify that it used the `ibm-bid-word-count` script and counted the correct evaluator-facing section. If no valid result was supplied, run the existing script before scoring. Do not use `wc -w`, `pandoc`, editor counts, model-estimated counts, copied snippets, or newly written Python/JavaScript/shell counting code.

3. **Conduct Detailed Analysis**
   - Perform your analysis within `<detailed_analysis>` tags
   - This analysis should be thorough and transparent
   - It's acceptable for this section to be quite long
   - If a word limit applies, include the exact `ibm-bid-word-count` command, count, limit, and status in the detailed analysis. Do not approve, reject, or score the response for word-count compliance from a raw markdown count, an estimate, or a custom counting script.

4. **Apply Evaluation Criteria**
   - Assess each criterion systematically
   - List relevant quotes from both the context document and the proposed answer
   - Document your findings clearly

5. **Provide Final Evaluation**
   - Summarize your findings in a structured format
   - Include detailed justification
   - Assign an appropriate score based on the scoring criteria

## Evaluation Criteria

Evaluate the tender response against these five key criteria:

### A. Question Understanding and Client Concerns
- What does the question really mean?
- What are the underlying concerns of the client?
- What problems are they trying to solve?
- What stakeholder needs are being addressed?
- If the question is about a service, has the response recognised the people, process, data, and technology dimensions of that service?

### B. Relevance to the Question
- Have all aspects of the question been answered?
- Is the answer sufficiently detailed?
- Does the response directly address what was asked?
- Are there any gaps or missing elements?
- If a word limit applies, is the evaluator-facing answer within the limit using the PEP 723 markdown word-count script?
- For service questions, does the answer cover the relevant people, process, data, and technology dimensions without drifting into generic content?

### C. Comprehensiveness of the Response
- Does the answer cover all necessary points?
- Are all sub-questions addressed thoroughly?
- Is the level of detail appropriate?
- Are examples and evidence provided where needed?
- For service questions, does the answer explain how the operating model works end to end across:
  - people: roles, capability, leadership, knowledge transfer, responsibilities, behaviours, and stakeholder engagement
  - process: lifecycle, governance, controls, workflows, assurance, escalation, change, and continuous improvement
  - data: records, reporting, metrics, quality, security, privacy, interoperability, insight, and service evidence
  - technology: platforms, tooling, automation, integrations, environments, resilience, security controls, and architecture

### D. Demonstration of Client Knowledge and Best Practices
- Does the response show understanding of the client's context?
- Are industry best practices applied appropriately?
- Is client-specific knowledge referenced (from the client context document)?
- Does the answer use the client's terminology and language?
- If a client language profile exists, does the response follow its vocabulary substitutions, tone guidance, characteristic phrases, and language-to-avoid rules?

### E. Alignment with Proposal Principles and Guidelines
- Does the response follow the proposal's guiding principles?
- Is it consistent with the overall proposal strategy?
- Does it align with the standards set in the proposal guidelines?
- Is the writing style appropriate and professional?
- If an approved customer story file exists, does the response use only those approved stories?

## Analysis Process

### Step 1: Detailed Analysis

Conduct your detailed analysis inside `<detailed_analysis>` tags. For each evaluation criterion:

1. **Quote relevant passages** from the proposed answer
2. **Reference the context document** where applicable
3. **Identify strengths** in the response
4. **Identify weaknesses or gaps** in the response
5. **Note specific examples** that support or undermine the answer's quality

This analysis should be:
- Thorough and comprehensive
- Evidence-based with specific quotes
- Transparent in reasoning
- Detailed enough to support your final score

### Step 2: Scoring Justification

After your detailed analysis, provide:

1. A clear justification for your score that:
   - Directly relates to the scoring criteria
   - References the proposal principles (if provided)
   - Reflects the quality of the answer based on your analysis
   - Explains why the score is appropriate

2. Specific feedback on:
   - What the response does well
   - Where it falls short
   - How it could be improved
   - Whether it meets the threshold for the tender requirements
   - Whether it complies with the approved customer-story control point when that file exists

## Output Format

Present your final evaluation in the following format:

```
<detailed_analysis>
[Your thorough analysis of each evaluation criterion, with relevant quotes and evidence from both the proposed answer and context documents]

A. Question Understanding and Client Concerns:
[Analysis with quotes and evidence]

B. Relevance to the Question:
[Analysis with quotes and evidence]

C. Comprehensiveness of the Response:
[Analysis with quotes and evidence]

D. Demonstration of Client Knowledge and Best Practices:
[Analysis with quotes and evidence]

E. Alignment with Proposal Principles and Guidelines:
[Analysis with quotes and evidence]
</detailed_analysis>

<evaluation>
<justification>
[Your detailed justification here - explain your reasoning, highlight strengths and weaknesses, and justify the score you're assigning]
</justification>
<score>
[Your numerical score here based on the scoring criteria]
</score>
</evaluation>
```

## Scoring Guidelines

When assigning a score, consider:

1. **Score Range Understanding**
   - Understand what scoring range is being used (e.g., 1-5, 1-10, percentage)
   - Ask for clarification if the scoring criteria aren't provided
   - Be consistent in how you apply the scoring rubric

2. **Scoring Principles**
   - Be objective and evidence-based
   - Consider all five evaluation criteria equally unless otherwise specified
   - Higher scores should reflect exceptional quality, not just adequacy
   - Lower scores should be reserved for responses with significant gaps or issues
   - Mid-range scores for responses that meet basic requirements but lack distinction

3. **Differentiation**
   - Clearly articulate what separates different score levels
   - Use the detailed analysis to support score distinctions
   - Be prepared to explain why a response received a specific score

## Example Scoring Rubrics

Use the scoring scale specified in the tender. Common scales and their interpretation:

### 0-5 Scale (UK Public Sector Standard)

| Score | Label | Description |
|-------|-------|-------------|
| 0 | Unacceptable | Fails to address the question or contains fundamental errors |
| 1 | Poor | Significant gaps; lacks evidence; major concerns about capability |
| 2 | Acceptable | Addresses basic requirements but lacks detail or evidence |
| 3 | Good | Comprehensive response with adequate evidence and some differentiation |
| 4 | Very Good | Strong response with clear evidence, good examples, exceeds expectations |
| 5 | Excellent | Outstanding response; compelling evidence; innovative approach; fully differentiated |

### 0-10 Scale

| Score Range | Label | Description |
|-------------|-------|-------------|
| 0-2 | Inadequate | Does not meet requirements; unsubstantiated claims |
| 3-4 | Partial | Meets some requirements; insufficient evidence |
| 5-6 | Acceptable | Meets requirements; adequate but not differentiated |
| 7-8 | Good | Exceeds requirements; strong evidence; some differentiation |
| 9-10 | Excellent | Significantly exceeds requirements; compelling proof points |

### Percentage Scale

| Score Range | Label | Description |
|-------------|-------|-------------|
| 0-20% | Unacceptable | Major gaps; fails to address key requirements |
| 21-40% | Poor | Partial coverage; lacking evidence or specificity |
| 41-60% | Satisfactory | Meets basic requirements; generic response |
| 61-80% | Good | Above average; demonstrates understanding with evidence |
| 81-100% | Excellent | Exceptional; fully evidenced; compelling differentiators |

### Score Differentiation Tips

- **1-2 point difference**: Minor differences in evidence quality or specificity
- **3+ point difference**: Significant gaps such as missing sections, no proof points, or failure to address client context
- **Top scores require**: Quantified outcomes, relevant case studies, clear differentiators, client-specific language
- **Client language profile**: If a profile exists in `client_language_analysis_artifact` or `./tmp/ibm-bid-client-language-analysis.md`, top scores require credible adherence to its terminology, tone, and writing rules. Do not reward generic IBM or consulting language where the profile says the client uses different terms.
- **Service questions require**: A credible operating-model view across people, process, data, and technology. A response that covers only technology, tools, or governance should not receive a top score unless the tender question explicitly limited the scope.

## Important Notes

- **Client Context is Critical**: Always request the client context document if not provided, as it's essential for evaluating criterion D
- **Proposal Principles Matter**: Understanding the proposal name and its guiding principles is essential for criterion E
- **Be Thorough**: The detailed analysis should be comprehensive - it's better to be too detailed than to miss important points
- **Use Evidence**: Always support your evaluation with specific quotes and examples from the answer being evaluated
- **Be Objective**: Set aside personal preferences and evaluate based on the criteria provided
- **Consider the Evaluator's Perspective**: Remember that tender evaluators are looking for specific evidence that requirements are met
- **Flag Gaps**: Clearly identify where the response fails to address parts of the question
- **Recognize Excellence**: When a response truly excels, acknowledge it with appropriate scoring and justification
- **Word Limits**: When a tender word limit applies, load `ibm-bid-word-count` and check it with the same PEP 723 markdown word-count strategy used by ibm-bid-writer. Do not penalise or approve based on raw markdown `wc -w`, `pandoc`, editor counts, estimated counts, copied snippets, or newly written counting code. If the answer is over limit, reflect that in Criterion B and the final score even if the content quality is otherwise strong.

## Word Count Checking

When the tender specifies a word limit, always load and use the existing `ibm-bid-word-count` skill and its PEP 723 Python script. Do not use raw markdown `wc -w`, `pandoc`, editor counts, model-estimated counts, copied snippets, one-off Python, JavaScript, shell pipelines, or ad hoc approximations.

Treat the word count as an evaluation gate:

1. Identify the tender limit and the section that counts.
2. Accept a writer-supplied count only if it includes the exact `ibm-bid-word-count` command and it matches the counted section.
3. If no valid result exists, run this skill's existing script against the persisted response or a temporary markdown file containing the evaluator-facing answer. If the answer exists only inline, create the temporary markdown file for counting; do not write counting code.
4. Include the command, count, limit, and status in the evaluation.
5. Penalise an over-limit answer under Criterion B and recommend revision before submission.

Count only the evaluator-facing answer content, normally after the `## Answer:` heading:

```bash
uv run python <IBM_BID_WORD_COUNT_SKILL_DIR>/scripts/count_words_in_markdown.py --from-heading "## Answer:" <DOC>
```

When the answer is followed by evidence logs, evaluator notes, source appendices, or other non-counted sections, bound the counted section with `--until-heading`:

```bash
uv run python <IBM_BID_WORD_COUNT_SKILL_DIR>/scripts/count_words_in_markdown.py --from-heading "## Answer:" --until-heading "## Evidence Log" <DOC>
```

If the document front matter contains `min-word-count` or `max-word-count`, use `--show-limits` to report the count against those limits. Front matter is never counted:

```bash
uv run python <IBM_BID_WORD_COUNT_SKILL_DIR>/scripts/count_words_in_markdown.py --show-limits --from-heading "## Answer:" --until-heading "## Evidence Log" <DOC>
```

If the tender requires the whole markdown response to count, omit `--from-heading`:

```bash
uv run python <IBM_BID_WORD_COUNT_SKILL_DIR>/scripts/count_words_in_markdown.py <DOC>
```

If the response does not use `## Answer:`, replace that heading with the first heading that marks the start of evaluator-facing answer content. If the response uses a different stop heading, replace `## Evidence Log` with the exact heading to exclude. Add `--include-heading` only if the tender requires the start heading to count. Exclude notes, evidence logs, planning text, evaluator feedback, and source appendices unless the tender explicitly says they count.

## Variable Placeholders

When conducting evaluations, you may encounter these variable placeholders:

- `{{.client_name}}` - Replace with the actual client name
- `{{.proposal_name}}` - Replace with the actual proposal or bid name
- `{{ tender_question }}` - The actual tender question being evaluated

These should be replaced with real values when conducting the evaluation.

## Quality Checklist

Before finalising your evaluation, verify that you have:
- ✓ Understood the tender question and client concerns
- ✓ Checked whether a service question needs people, process, data, and technology coverage
- ✓ Requested necessary context documents if not provided
- ✓ Conducted a thorough analysis within `<detailed_analysis>` tags
- ✓ Evaluated all five criteria systematically
- ✓ Included relevant quotes from the proposed answer
- ✓ Referenced the client context document where applicable
- ✓ Provided a detailed justification for your score
- ✓ Assigned a score that reflects the quality of the answer
- ✓ Checked any applicable word limit using `ibm-bid-word-count`, or verified a writer-supplied result from that script, and reported the command, count, limit, and status
- ✓ Used the specified output format
- ✓ Been objective and evidence-based in your assessment
- ✓ Identified both strengths and weaknesses clearly
- ✓ Explained how the response could be improved (if applicable)

## Complete Tender Response Workflow

This skill is part of the 5-phase IBM Bid Management workflow.

**Current Phase**: Phase 3 (Content Development) - Iterative quality check
**Position**: Runs AFTER each ibm-bid-writer response, iterates until score ≥3

**Also used in**: Phase 4 (Technical Assurance) - Final comprehensive evaluation of all responses

See ibm-bid-navigator for complete workflow guidance.

## Integration with Other Skills

### Required Inputs

**Per-question evaluation** (Phase 3 iterative loop):
- **RFP question**: The tender question being answered (required)
- **Drafted response**: ./tmp/ibm-bid-responses/Q0X_[topic].md from ibm-bid-writer (required)

**Context for evaluation**:
- **ibm-bid-requirements-analysis**: ./tmp/ibm-bid-requirements-analysis.md (client context, requirements, evaluation criteria)
  - Uses for Criterion A: Understanding client concerns
  - Uses for Criterion D: Client knowledge verification
- **ibm-bid-client-language-analysis**: check `./tmp/ibm-bid-project.md` for `client_language_analysis_artifact`; if absent, fall back to `./tmp/ibm-bid-client-language-analysis.md`
  - Uses for Criterion D: Client terminology, tone, characteristic phrases, and language-to-avoid compliance
  - Uses for Criterion E: Writing style alignment with the bid's agreed client-language strategy
- **ibm-bid-win-themes**: ./tmp/ibm-bid-win-themes.md (strategic messaging)
  - Uses for Criterion E: Alignment with proposal strategy
- **Approved customer stories**: ./tmp/ibm-bid-approved-customer-stories.md (approved evidence subset, if present)
  - Uses for Criterion C: Evidence appropriateness
  - Uses for Criterion E: Compliance with the controlled evidence pool

**Optional for comprehensive evaluation**:
- **ibm-sf-solution/complete_solution.md** OR **ibm-bid-solution/complete_solution.md**: Technical solution context
- **ibm-sf-ams-estimation.md**: Support model context (for AMS/commercial questions)

### Recommended Next Steps

**After per-question evaluation:**

**If score ≥3 (Adequate or better)**:
- Response is acceptable quality
- Proceed to next question
- Continue ibm-bid-writer + ibm-bid-answer-evaluator iteration for remaining questions
- **When all questions complete**: Proceed to Phase 4 (Technical Assurance)

**If score <3 (Poor, Unacceptable, or Partial)**:
- Response needs revision
- **Return to ibm-bid-writer** with evaluator feedback
- Provide specific areas for improvement from detailed analysis:
  - Missing evidence → Search ibm-bid-customer-stories for proof points
  - Generic content → Adapt from ibm-bid-library historical responses
  - Missing IBM differentiators → Reference ibm-bid-strategy-and-capabilities-2026
  - Poor structure → Restructure to mirror question format
  - Lack of client knowledge → Reference ibm-bid-requirements-analysis client profile
- After revision, **re-run ibm-bid-answer-evaluator** (iterate until ≥3)

**After all questions evaluated (Phase 3 complete)**:
- All responses should score ≥3
- Proceed to Quality Gate 2 checkpoint
- Then Phase 4: Technical Assurance
  - Run **ibm-bid-tda-review** (if technical solution exists)
  - Run **Final ibm-bid-answer-evaluator pass** (comprehensive review of all responses)

### Scoring Scale (0-5 Standard)

Use this 0-5 scale for all evaluations:

| Score | Label | Description | Decision |
|-------|-------|-------------|----------|
| **5** | Excellent | Outstanding; compelling evidence; innovative; fully differentiated | PASS - Excellent quality |
| **4** | Very Good | Strong response; clear evidence; good examples; exceeds expectations | PASS - High quality |
| **3** | Good | Comprehensive; adequate evidence; some differentiation | PASS - Acceptable quality |
| **2** | Acceptable | Addresses basics but lacks detail or evidence | FAIL - Needs revision |
| **1** | Poor | Significant gaps; lacks evidence; major capability concerns | FAIL - Major revision required |
| **0** | Unacceptable | Fails to address question or contains fundamental errors | FAIL - Complete rewrite required |

**Quality Threshold**: Score ≥3 required to proceed
- Government bids: Average ≥4 preferred (higher bar)
- Commercial bids: Average ≥3.5 acceptable

### Five Evaluation Criteria Mapped to Bid Workflow

**Criterion A: Question Understanding and Client Concerns**
- Source: ibm-bid-requirements-analysis (underlying needs, client context)
- Evaluates: Does response demonstrate understanding of WHY client is asking this question?
- Red flags: Generic response, no client-specific insights, misunderstanding of requirements, service interpreted too narrowly as only technology or delivery process

**Criterion B: Relevance to the Question**
- Source: RFP question requirements
- Evaluates: Are all parts of question answered? Sufficient detail? Direct address?
- Red flags: Missing sub-questions, tangential content, insufficient depth, service answer omits relevant people, process, data, or technology dimensions

**Criterion C: Comprehensiveness of the Response**
- Source: Question requirements + industry best practices
- Evaluates: All necessary points covered? Examples provided? Appropriate detail level?
- Red flags: Gaps in coverage, no examples, oversimplification or excessive complexity, operating model not explained end to end

**Criterion D: Demonstration of Client Knowledge and Best Practices**
- Source: ibm-bid-requirements-analysis (client profile) + ibm-bid-client-language-analysis (if present) + industry standards
- Evaluates: Client-specific knowledge shown? Industry best practices applied? Client terminology used?
- Red flags: Generic content, no client context, client-language profile ignored, industry-standard practices missing
- Validate: Customer stories referenced actually exist in ibm-bid-customer-stories

**Criterion E: Alignment with Proposal Principles and Guidelines**
- Source: ibm-bid-win-themes (strategic messaging)
- Evaluates: Win themes incorporated? Consistent positioning? Appropriate writing style?
- Red flags: No win theme integration, inconsistent messaging, poor writing quality
- Validate: IBM capabilities claimed exist in ibm-bid-strategy-and-capabilities-2026

### Supporting Resources for Validation

**During evaluation, cross-reference:**

| Criterion | Resource | Purpose |
|-----------|----------|---------|
| D (Client Knowledge) | **ibm-bid-customer-stories** | Verify referenced case studies exist and are accurate |
| D (Client Language) | **ibm-bid-client-language-analysis** | Verify the response follows the client vocabulary, tone, phrases, and avoid-list |
| E (IBM Capabilities) | **ibm-bid-strategy-and-capabilities-2026** | Verify IBM capability claims are accurate |
| A (Client Concerns) | **ibm-bid-requirements-analysis** | Confirm response addresses identified client needs |
| E (Strategic Alignment) | **ibm-bid-win-themes** | Verify win themes incorporated |

### Iterative Quality Loop (Phase 3)

**The Writer-Evaluator Cycle:**

```
ibm-bid-writer (draft Q01)
  ↓
ibm-bid-answer-evaluator (score Q01)
  ↓
Score ≥3?
  → YES: Proceed to Q02
  → NO: Feedback to ibm-bid-writer
      ↓
ibm-bid-writer (revise Q01 based on feedback)
      ↓
ibm-bid-answer-evaluator (re-score Q01)
      ↓
Score ≥3?
  → YES: Proceed to Q02
  → NO: Iterate again (max 3 iterations before escalation)
```

**Escalation**: If response fails 3 evaluation cycles, escalate to Bid Manager for guidance (may indicate unclear requirements or scope issue).

### Final Comprehensive Evaluation (Phase 4)

**After all individual questions evaluated:**

1. **Final ibm-bid-answer-evaluator pass**:
   - Input: ALL responses in ./tmp/ibm-bid-responses/
   - Output: ./tmp/ibm-bid-final-evaluation.md
   - Additional checks:
     - **Cross-response consistency**: No contradictions between responses
     - **Win theme integration**: Themes consistently incorporated across all responses
     - **Solution architecture alignment**: Technical responses match solution documents
     - **Evidence currency**: No outdated customer stories or statistics
     - **Compliance**: Page limits, word limits, formatting requirements, mandatory sections met

2. **Quality Gate 2 criteria**:
   - All individual responses score ≥3
   - Average score ≥4 for government bids
   - No fabricated information detected
   - Consistent messaging across all responses
   - If any criteria fail: Return to ibm-bid-writer for revisions before submission

### Common Feedback Patterns

**Score 2 (Acceptable) - Typical Issues:**
- Lacks specific evidence → Add customer stories from ibm-bid-customer-stories
- Generic content → Adapt from ibm-bid-library for similar questions
- Missing IBM differentiators → Reference ibm-bid-strategy-and-capabilities-2026
- Weak structure → Reorganize to mirror question order
- Service scope too narrow → Add the missing people, process, data, or technology dimensions where relevant

**Score 1 (Poor) - Typical Issues:**
- Major gaps in addressing question → Re-read question, address all sub-questions
- No evidence → Search ibm-bid-customer-stories extensively, quantify benefits
- No client context → Reference ibm-bid-requirements-analysis, use client terminology
- Contradicts other responses → Check consistency across ./tmp/ibm-bid-responses/
- Treats a service question as only a tooling or technical-platform answer → Rebuild around the full service operating model

**Score 0 (Unacceptable) - Typical Issues:**
- Fabricated information → Remove and replace with verified content
- Fundamental misunderstanding → Re-analyze question, consult ibm-bid-requirements-analysis
- Non-responsive → Start over, follow question structure exactly

### Quality Gate 2 Impact

This skill directly informs Quality Gate 2 (Technical Assurance):

**Gate 2 Criteria for Responses** (from evaluator):
- All responses score ≥3 (adequate quality minimum)
- Average score ≥4 for government bids (higher standard)
- No fabricated information (score 0 triggers automatic fail)
- Consistent messaging across all responses
- Win themes incorporated throughout

**Combined with ibm-bid-tda-review:**
- TDA: Technical architecture validation (LOW/MEDIUM/HIGH risk)
- Evaluator: Response content quality (0-5 scale)
- Both must PASS for Quality Gate 2 approval

**Submission Decision:**
- TDA LOW + All scores ≥3 → **SUBMIT** (approved for submission)
- TDA MEDIUM + All scores ≥3 → **CONDITIONAL SUBMIT** (escalate for approval)
- TDA HIGH OR Any score <3 → **NO-GO** (cannot submit, revise failing areas)
