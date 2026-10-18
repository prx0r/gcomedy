# FINDINGS — first timing experiments (2026-10-18)

> Ran five hypotheses from THESIS-timing-is-composition.md against
> real data. Two strongly confirmed, one confirmed with a better
> mechanism than either source theory predicted, two honest negatives.
> Machine-readable results: `results/timing_experiments.json`.
> Script: `run_timing_experiments.py`.

## The data

| Source | What | n |
|---|---|---|
| `characters2/theory/scribe/` | Word-level timing (start/end per word) | 5 KT sets + Louis + Norm |
| `scribe/*_laughs.json` | Laugh timestamps | 5 sets, 44 laughs |
| `theory/analysis/*_analysis.json` | Measured punch candidates | Louis Road Rage (12), Norm Moth (4) |
| `theory/transcripts/bits_theory.json` | Paper-scored bit features | 29,617 bits |
| `theory/transcripts/bits_annotated/` | Bit text (setup + punch) | 10,941 comparable |

## H1: Laughs fire at temporal violations — CONFIRMED

**Claim (DPV):** the laugh happens at the extended pause, not after it.

**Result:** pauses before laughs average **2.51s**; baseline gaps average **0.178s**. That's **14.1x**. Permutation test p < 0.0001. Every set independently shows it (5.2x to 54x).

```
kt728_jamesbond     54x   (n=4)
kt728_diversifying  21x   (n=11)
kt715_walking       12x   (n=6)
kt715_ep715         10x   (n=14)
kt704_passport       5x   (n=9)
```

**Interpretation:** the laugh is not a reaction to the punchline's content arriving. The laugh fires at the moment the temporal structure breaks — the extended silence IS the event the audience responds to. The content may have arrived a beat earlier; the silence is what makes the room commit to the laugh.

This is the strongest evidence yet that timing is not delivery. If timing were delivery, the laugh would correlate with content markers, not with pause duration. It correlates with pause duration at 14x baseline.

## H3: The punch has a two-part temporal signature — CONFIRMED (and better than either theory)

**Competing claims:**
- Norrick 2001: punch delivered FASTER than setup.
- DPV 2026: punch preceded by EXTENDED pause.

**Result: both fire, in sequence.**

| Set | Punch pause mean | Set mean pause | Ratio |
|---|---|---|---|
| Louis Road Rage | 1.55s | 0.756s | **2.05x** |
| Norm Moth | 1.415s | 1.003s | **1.41x** |

And the punch itself:
- Speech rate before punch (excluding pause): 6.94 syl/s
- Speech rate at/after punch: 10.25 syl/s
- **Post/pre = 1.48x**, sign-flip p = 0.045

**The signature is: HOLD, then SNAP.**

The pause before the punch is 1.4–2x the set's normal pause (DPV's temporal violation). The punch is then delivered 1.48x faster than the speech preceding it (Norrick's rate increase). They aren't competing explanations — they're sequential phases of one gesture.

Musically: a fermata (held note of indeterminate length) followed by a rush (accelerated passage). The fermata creates the space where the audience's expectation is maximally suspended. The rush fills that space before the room can re-form its prediction model.

This matters for the thesis: the punch's temporal structure is not a single number (pause duration). It's a **trajectory**: slow → hold → snap. The geometric metric needs to capture the shape of the approach, not just the distance.

**Louis vs Norm:** same signature, different absolute values. Louis: longer holds (2x baseline), bigger pauses (8.16s max). Norm: shorter holds (1.4x), faster snaps (post rate up to 34 syl/s in one case). The trajectory shape is conserved; the scale differs by persona. This is exactly what "timing is composition, delivery is voicing" predicts — same composition, different voicing.

## H2: Speech slows into the pause — DIRECTIONAL (underpowered)

**Refined claim:** rate in the 1s before the pause is slower than rate in the 1s after the laugh.

**Result:** pre-pause rate = 0.83x baseline; post-laugh rate = 1.41x baseline. Sign-flip p = 0.069, n = 8.

Direction matches H3's trajectory (slow into hold, fast out). n=8 is too small for significance. The effect is consistent with H1+H3; needs more laugh-timed sets to confirm independently.

## H4: Paper-scored BV coupling — NOT SUPPORTED (honest negative)

**Claim:** benign_violation correlates with incongruity × surprise.

**Result on 29,617 paper-scored bits:**
- corr(incongruity, BV) = -0.004
- corr(surprise, BV) = +0.039
- corr(product, BV) = -0.002

Paper-scored BV is sparse (only 9% of bits nonzero) and doesn't track the product of the other two scores. Surprise alone predicts punch_pos well (r=0.46) — the paper scorer places high-surprise bits late in specials.

**Verdict:** the paper labels are too weak a proxy to test the coupling hypothesis. This is NOT evidence against the coupling hypothesis itself — H1 and H3 test the temporal side of coupling directly on measured data and succeed. The content side needs better labels (measured laugh positions, not paper scores) to test properly.

**Lesson:** paper-scored features are useful for exploration, not for hypothesis tests about mechanism. Measured timing + measured laughs is the only valid path. (Rule 0 spirit.)

## H5: Punch syllable compression — NOT SUPPORTED (wrong operationalization)

**Claim (from Seinfeld):** punches have fewer syllables per word than setups.

**Result:** setup = 1.286 syll/word, punch = 1.284 syll/word. Diff = -0.002. p = 0.26.

**Why it failed:** Seinfeld's "shave syllables" is about fitting a **transition** into a time budget between jokes — a between-bits constraint, not an intra-bit punch property. My operationalization tested the wrong level. The right test: does punch WORD COUNT stay within a consistent time slot across bits? (Future experiment.)

## What this means for the thesis

The core claim — timing is composition, not delivery — survives contact with data:

1. **The laugh fires at the temporal violation** (14x baseline). Timing is where the audience commits.
2. **The punch has a trajectory, not a duration**: hold (1.4–2x) then snap (1.48x). Composition = writing the trajectory.
3. **The trajectory shape is conserved across personas** (Louis vs Norm) at different scales. Same score, different voicing.
4. **The geometric metric needs updating**: punch distance isn't `√(semantic² + temporal²)` with temporal = pause length. It's a path integral over the rate trajectory:

```
d(punch, setup) = √( semantic_distance² + ∫ temporal_profile(t) dt )

where temporal_profile(t) = the rate curve approaching the punch:
  baseline → deceleration → extended hold → acceleration → punch
```

The integral captures the SHAPE, not just the max pause. A punch with the right trajectory but a shorter hold can be as funny as one with a longer hold — which matches the Louis/Norm contrast.

5. **The paper-score coupling hypothesis needs measured laugh data to test.** 29k paper labels aren't enough. The 44 measured laughs we have already confirm the temporal side; scaling to hundreds of laugh-timed sets would let us test content-temporal coupling directly.

## Next experiments

1. **Scale H1/H2/H3** to more laugh-timed sets (need more `*_laughs.json` files — currently only 5 KT sets have them).
2. **Trajectory classification**: cluster the rate-into-punch curves. Do different clusters map to different joke types (confession vs absurd vs one-liner)?
3. **The right H5**: test whether punch word-count fits a consistent time budget across bits (Seinfeld's actual claim).
4. **Louis vs Norm trajectory overlay**: plot the normalized rate curves. Quantify the "same shape, different scale" claim.
5. **Content-temporal coupling on measured laughs**: for the 44 laughs, compute semantic distance (embedding) between pre-pause and post-pause text. Test whether high semantic distance + high pause = higher laugh intensity (when we get intensity, not just onset).
