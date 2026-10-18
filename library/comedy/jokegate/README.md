# JOKEGATE — the classifier house

One definition per classifier, inherited everywhere. A change here
updates the whole codebase. Verbatim process: `docs/PROCESS-jokegate.md`.
Goal it serves: `docs/GOAL-personality-loop.md`.

## The three rounds (a set performs only after all three)

| round | gate | question | fail means |
|---|---|---|---|
| 1 | `slop.py` (SlopGate) | well-formed human-sounding, or AI slop? | fix English / specifics / rhythm, resubmit |
| 2 | `edgy.py` (EdgyGate) | stepped over + leaned in, or flinched / punched down? | re-aim butt, add benign frame, or buildup |
| 3 | `feel.py` (FeelJudge) | FEELS AI or human? | hand-rewrite the seam a human felt |

Every gate returns a Verdict PAYLOAD (`base.py`): pass, scores,
problems, suggested_edits, confidence. The writer consumes the payload
and edits — the iterative loop. `pipeline.py` runs ordered stages with
re-tries; `challenges.py` scores entries through any pipeline.

## Docs (standalone, one per classifier)

- `docs/SLOP.md` — theory / how / metrics (NoSlop band, rhythm rule)
- `docs/EDGY.md` — theory / how / calibration (realm exemplars)
- `docs/FEEL.md` — theory / how / validation plan (human ground truth)
- `docs/PIPELINES.md` — composition, iterate loop, inheritance map, Jev note

## Quick use

```python
import sys; sys.path.insert(0, 'theory')
from jokegate.pipeline import Pipeline
p = Pipeline.named("slop", "edgy")          # custom combo, no feel
res = p.run(text, character={'roster': 'freaks', 'name': 'Ssliss'})
# res = {passed, failed_stage, text_final, trace}
```

```bash
python3 theory/jokegate/challenges.py --demo --pipeline slop,edgy
```
