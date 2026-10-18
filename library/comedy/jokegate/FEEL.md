# FEEL JUDGE — theory, how it works, metrics

**Round:** 3 (last before performance). **Question:** does this FEEL AI
or human? Covers the un-metricked remainder — the thing no classifier
scores. A set can clear slop + edgy and still fail feel. That is the point.

## Theory

Feel = flow + voice + surprise + specificity + absence-of-tells, read as
one gestalt. Humans detect AI prose holistically (uniform cadence,
generic narrator, completed patterns) even when every rule passes. No
feature set captures it fully — hence a judge, not a meter. Human
perception is the ground truth; the AI reader is a proxy with known
error.

## How it works

`FeelJudge.classify(text, character, human=None)`:

1. **Human slot first.** `{reviewer, verdict: ai|human|unsure, note}`.
   A filled human verdict ALWAYS wins: human→PASS (confidence strong),
   ai→FAIL with the note as the fix order, unsure→FAIL pending a second ear.
2. **AI reader fallback.** LLM rubric, 5 dims × 1–5 (flow, voice,
   surprise, specificity, no-tells). PASS iff mean ≥3.5 AND no dim <3.
   Confidence capped at "limited" — a model opinion, never ground truth.
3. **Neither available** → FAIL with confidence "none" (unjudged is not
   passed — fail closed, always).

## Metrics

No accuracy metrics exist yet (nothing to validate against until human
verdicts accumulate). The validation plan: log every AI-reader verdict
alongside eventual human verdicts in `feedback.v1`; compute agreement
rate at n≥30; promote confidence only with evidence. Until then the AI
reader points, humans dispose.
