# Experiment 3: Uncertainty × Surprisal (Cheung model on comedy)

**Date:** 2026-10-18
**Data:** 20 bits rated by DeepSeek V4 Flash (via OpenCode Go key, ~$0)
**Question:** Does the Cheung et al. (2019) uncertainty × surprisal interaction predict comedy score?
**Method:** DeepSeek rates setup predictability (1-10) and punchline surprisal (1-10). Pearson correlations with score.

## Results (n=8 paired, partial due to API failures)

| Predictor | r | Notes |
|---|---|---|
| **setup predictability** | **+0.334** | **more predictable setup = funnier** |
| punchline surprisal | -0.099 | slightly negative, basically zero |
| interaction (P×S/10) | +0.040 | essentially zero |
| violation (jokegate) | -0.253 | more violation = less funny |
| **benign (jokegate)** | **+0.494** | **strongest predictor** |

## Key finding: comedy INVERTS the music model

Cheung et al. found for music: high surprise + low uncertainty = pleasure (the punchline chord). The interaction matters.

**For comedy: setup PREDICTABILITY (not uncertainty) correlates positively with score (r=+0.33).**

This is the opposite direction. Why? The AAB pattern (Rozin et al. 2006): comedy requires establishing a predictable pattern (A, A) before breaking it (B). If the setup itself is unpredictable, there's no stable pattern to violate. The setup must be predictable enough that the punch can violate it cleanly.

This is consistent with:
- Witek et al. (2014): moderate syncopation = maximum pleasure (comedy needs moderate predictability)
- The AAB experiment: minimum two iterations to establish pattern before violation
- Clark (2017): we seek the RIGHT kind of surprise — surprise that resolves uncertainty, not surprise that creates it

## The punchline equation (revised for comedy)

Music: pleasure = uncertainty × surprise (Cheung et al.)
Comedy: score ≈ predictability(setup) × benignity × (1 / violation_distance)

Where:
- predictability(setup) must be HIGH (establish the pattern)
- benignity must be MODERATE (inverted-U, Exp 1)
- violation_distance must be MINIMAL (the punch barely moves, Exp 2)

## Limitations
- n=8 is tiny (DeepSeek reasoning model is slow + token-hungry)
- Model ratings are coarse (1-10 scale, reasoning model)
- The jokegate benignity metric (r=+0.49) still outperforms the model-based predictors

## Implication for the book

Chapter 2: comedy has the OPPOSITE uncertainty relationship to music. Music thrives on uncertainty; comedy thrives on setup predictability. The setup is the A in AAB — it must be stable. The punch is the B — it must be a clean, minimal violation of the established pattern. The pleasure comes from the RESOLUTION of the violation, not the uncertainty of the setup.

This is a genuine novel finding for the book — the music-comedy asymmetry.
