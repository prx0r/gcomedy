# Experiment 2: Text-level geometry predicts score

**Date:** 2026-10-18
**Data:** 154 scored bits
**Question:** Does the semantic/textual distance between setup and punch predict comedy score?
**Method:** Word overlap (Jaccard), repetition ratio, length features. Pearson correlations with score.

## Results

| Feature | r | R² | Notes |
|---|---|---|---|
| word overlap (Jaccard) | +0.040 | 0.002 | zero |
| repetition (setup→punch) | +0.036 | 0.001 | zero |
| punch_ratio (punch/setup) | -0.168 | 0.028 | shorter punch = funnier |
| setup length | -0.052 | 0.003 | zero |
| **punch length** | **-0.320** | **0.103** | **shorter punch = funnier** |
| total length | -0.304 | 0.093 | shorter bit = funnier |

## Punch ratio distribution
- mean: 1.53, median: 1.06
- 80/154 bits: punch > setup (expansion)
- 60/154 bits: punch < setup (compression)

## Finding

**Word-level geometry doesn't predict score.** Overlap between setup and punch is uncorrelated with funniness. The comedy isn't in the words — it's in the interpretation shift.

**Punch length does predict score (r=-0.32).** Shorter punchlines score higher. This matches the 2009 acoustic finding (punchlines delivered at lower pitch + slower rate — more concise, not louder) and Tymoczko's minimal-displacement principle: the punch barely moves from the setup. It moves DOWN, not OUT.

## Implication for the book

Chapter 2 (Five Components): conjunct melodic motion = the punch barely moves. The violation distance is measured in interpretation shift, not word distance. Chapter 9 (Pause Ladder): the punch is a descent, not an explosion. Shorter is better.
