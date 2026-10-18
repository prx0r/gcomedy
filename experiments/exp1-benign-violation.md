# Experiment 1: Benign Violation predicts comedy score

**Date:** 2026-10-18
**Data:** 154 scored bits from 10 comics (ROSTER-*.json + grey-fieldworker.set.json)
**Question:** Does McGraw & Warren's benign violation theory predict comedy score?
**Method:** OLS regression, violation/benign metrics from jokegate.

## Results

| Model | R² | Notes |
|---|---|---|
| violation alone | 0.0005 | r=-0.02, essentially zero |
| benign alone | 0.0828 | r=+0.29, weak positive |
| V + B | 0.0838 | barely better than B alone |
| V + B + V×B | 0.0905 | interaction helps slightly |
| V + V² (inv-U) | 0.0986 | inverted-U on violation |
| **B + B² (inv-U)** | **0.1850** | **inverted-U on benignity — WINNER** |

## Finding

**Benignity has an inverted-U relationship with comedy score.** Not too benign (boring), not too threatening (unfunny), sweet spot in the middle. This is the Witek et al. (2014) syncopation result but for comedy — moderate violation maximizes pleasure.

**Violation alone is uncorrelated with score (r=-0.02).** The jokegate violation metric may be calibrated so all bits have similar violation (mean 0.24, sd 0.26 — low violation across the board). Or violation alone doesn't predict funniness — consistent with McGraw & Warren's claim that incongruity alone is insufficient.

**B + B² explains 18.5% of score variance from text features alone.** For comparison, Cheung et al. (2019) explained ~10-15% of musical pleasure from uncertainty × surprise. Comedy's benignity signal is comparable in strength.

## Implication for the book

Chapter 6 (The Target Field): the benign-violation manifold is measurable. The jokegate's benignity metric is the single best text-based predictor of comedy score we have. This is the "acoustic consonance" component of Tymoczko's five — the benignity fit is what makes a violation land.
