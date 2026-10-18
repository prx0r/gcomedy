# Experiments — The Geometry of Comedy

First-principles computational tests of the book's core claims. All $0 (DeepSeek via Go key for model ratings).

## Core claim under test

Comedy has measurable geometric structure like music (Tymoczko). Setup is a point in idea-space. Punch is a geodesic to violation. Callback is a harmonic return.

## Experiments

| Exp | Claim | Finding | Paper |
|---|---|---|---|
| 1 | Benign violation predicts score | B+B² inverted-U: R²=0.185. Benignity is the best text-based predictor (r=+0.49). | [exp1](exp1-benign-violation.md) |
| 2 | Semantic distance predicts score | Word overlap: zero. Punch length: r=-0.32 (shorter punch = funnier). | [exp2](exp2-semantic-distance.md) |
| 3 | Uncertainty×surprisal predicts score (Cheung model) | Setup PREDICTABILITY r=+0.33 (opposite of music). Interaction: zero. Comedy inverts the music model. | [exp3](exp3-uncertainty-surprisal.md) |

## The comedy punchline equation (emerging)

```
score ≈ predictability(setup) × benignity² × (1 / punch_length)
```

Not the music equation. Comedy needs:
1. **Predictable setup** (establish the AAB pattern — the setup must be stable enough to violate)
2. **Moderate benignity** (inverted-U — too safe is boring, too risky is unfunny)
3. **Short punch** (minimal displacement — the punch barely moves, it moves DOWN)

## Data

- 154 scored bits from 10 comics (characters2 ROSTER-*.json + grey-fieldworker)
- Fields: setup, punch, score, violation, benign, ops, punch_ratio
- All from jokegate scoring pipeline (violation/benign metrics)

## Reproduce

```bash
# Experiment 1 (pure code, no API)
python3 experiments/exp1_code.py

# Experiment 3 (uses Go key + DeepSeek)
# See exp3 code in git history
```

## What's next

- [ ] Expand Exp 3 to full 154 bits (need faster model or batch scoring)
- [ ] AAB pattern detection in bit corpora (are AAB bits actually funnier?)
- [ ] Callback geometry: measure semantic distance between callback and original
- [ ] Rasa classification: can we label bits by rasa and test the tonality map?
- [ ] Cross-validate benignity inverted-U on held-out comics
