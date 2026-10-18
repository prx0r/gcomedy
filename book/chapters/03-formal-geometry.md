# The Geometry of Comedy — Formal Statement

> Draft 2026-10-18. The formal companion to Chapter 2. Defines joke-space,
> its coordinates, its symmetries, its metric, and its testable predictions.
> Sources: Tymoczko (2011) Ch.1–3 + Science 2006/2008; Raskin (1985) SSTH;
> Attardo & Raskin (1991) GTVH; McGraw & Warren (2010) BV; our experiments
> 1–3 (n=154); TAMS/DPV timing findings.

## 1. Joke-space and its coordinates

A joke is a point in joke-space. Its coordinates are the GTVH Knowledge
Resources — the sixtuple (Attardo & Raskin 1991):

```
J = (SO, LM, SI, TA, NS, LA)
SO = script opposition (the two opposed readings)
LM = logical mechanism (how the incongruity resolves)
SI = situation (setting, participants)
TA = target (butt; empty for non-aggressive)
NS = narrative strategy (riddle, story, one-liner, ...)
LA = language (wording at every level)
```

The KRs are hierarchically ordered by determining power (Ruch, Attardo &
Raskin 1993, confirmed except LM/SI order):
**SO > LM > SI > TA > NS > LA.**
Choices high in the hierarchy constrain choices below. Two jokes sharing SO
feel more different than two sharing only LA. The hierarchy is the
coordinate system's first geometric fact: joke-space is anisotropic —
distances along SO count more than distances along LA.

## 2. The OPTIC symmetries, translated (with constraint differences)

Tymoczko's five equivalences (O/P/T/I/C) generate 32 chord-types and 243
progression-types. Comedy has all five operations — but with different
constraints, and the constraints are informative:

| Op | Music | Comedy analogue | Constraint difference |
|---|---|---|---|
| O (octave shift) | same note, different octave | same joke, different register (high/low status voicing) | Preserves SO, shifts TA/sympathy |
| P (permute) | reorder notes freely | reorder setup/punch | **CONSTRAINED: punch must be last.** Setup→punch is directed; punch→setup is not a joke but a different object (cf. Bhartṛhari: meaning reorganizes at the final word — direction matters). Music permits P; comedy forbids it. The forbidden symmetry is the theory's first prediction: no culture has punch-first jokes as a stable form. |
| T (transpose) | same chord, different key | same structure, different topic (retargeting) | Preserves (SO, LM), changes (SI, TA). Retargeting IS transposition. Callback across topics = transposed restatement. |
| I (invert) | turn upside down | invert the scoring/selection function | Our inverted games (least-funny-answer: fewest votes wins) are literal inversions. Genre-swap (same scene, noir vs nature-doc) is inversion of the delivery function holding text fixed. |
| C (cardinality) | duplicate notes | add/remove beats (tags, callbacks, runners) | Tags = cardinality increase on the punch. Callbacks = cardinality increase across the night. The night's archive grows by C-operations. |

Counting (Tymoczko-style): 2^5 = 32 joke-equivalence classes under all
combinations; progressions (setup→punch→tag chains) admit uniform vs
individual application, as in music. The full 243-count transfers formally;
which classes are populated is an empirical question for the corpus.

## 3. Voice-leading size = reinterpretation distance

Tymoczko §2.7: compare voice leadings by total semitone motion; efficient =
small. Polyphony is possible because near-even chords link by tiny moves.

Comedy: define **reinterpretation distance** d(S, P) = the minimal
model-update carrying the audience from the setup-reading to the
punch-reading. Efficient jokes move the model a short distance to a
disjoint conclusion. The punch that travels far (long shaggy-dog
explanation) exhausts; the punch that travels one step (short relabeling)
delights.

Empirical anchors (our Exp 1–3, n=154):
- Punch length r = −0.32 with score: shorter travel, funnier. Direct
  confirmation that minimal displacement predicts quality.
- Benignity inverted-U (B+B², R² = 0.185): the landing zone must be
  habitable. Distance alone is insufficient — the destination must be
  benign. (McGraw & Warren's simultaneity = arrival + habitability judged
  together; timing is the mechanism forcing simultaneity.)
- Setup predictability r = +0.33: the starting point must be stable for
  the measured move to register. (Cheung inversion: music rewards
  uncertainty; comedy rewards platform stability.)
- Violation alone r = −0.02: raw distance without direction/habitability
  predicts nothing. Incongruity alone is insufficient — the formal
  analogue of Tymoczko's point that voice-leading size matters only
  between *meaningful harmonies*.

## 4. Center, symmetry, and callbacks

Tymoczko's orbifold center holds the perfectly even chords (augmented
triad); familiar sonorities cluster near it; near-symmetry (not exact)
links most efficiently; boundaries hold duplicate-heavy chords.

Joke-space center: jokes with two equally-live readings (puns, double
entendre — the superposition jokes from our pun analysis: ambiguity +
distinctiveness both high). These connect to the most callbacks, because a
callback can depart toward either reading. Extreme jokes (single forced
reading, heavy TA-dependence) sit near the boundary: hard to callback,
hard to transpose. Prediction: callback rate correlates inversely with
distance from center. Testable on the night archive (callback graph degree
vs. SO-ambiguity score).

Near-symmetry preference transfers: the best callback targets are NEARLY
ambiguous (leaning one way), not perfectly balanced (no direction to
resolve) nor fully determined (nothing to re-weight). Comedians already
know this as "leave them somewhere to go."

## 5. Rasa as macroharmony (tonality level)

Tymoczko Ch.5: macroharmony (the 5–8 note reservoir) + centricity (the
stable pitch). Comedy: the rasa range (hasya inflected by ≤8 companions)
+ the persona center (the comic's key). A set stays within its
macroharmony; modulation (rasa change) is a compositional resource costing
a transition. Persona = key: certain responses are diatonic (natural),
others chromatic (need preparation). Roast in a deadpan key is a
modulation — playable, but the bridge must be built.

## 6. Trajectories: the night as a progression

- Beat = point. Setup→punch = directed path (P-forbidden direction).
- Tag chain = cardinality extension of the path.
- Callback = return path to an earlier point, revoiced (transposed).
- Set = ordered path through joke-space minimizing total reinterpretation
  distance subject to a novelty constraint (never revisit a point
  identically — pure repetition pays zero, per the callback economy).
- Night = the full trajectory + archive graph. Champion = maximal
  coverage with minimal backtracking (the traveling-comedian problem).

## 7. Testable predictions (the geometry earns its keep)

1. **P-constraint:** no stable punch-first joke form exists cross-culturally
   (direction is constitutive, unlike music).
2. **Distance-quality:** reinterpretation distance (LLM surprisal of punch
   given setup, cf. Xie 2020) correlates negatively with funniness ratings
   within fixed SO classes.
3. **Center-callback:** callback degree correlates with SO-ambiguity
   (near-center jokes get called back more).
4. **Transposition invariance:** retargeted jokes (same SO+LM, new SI+TA)
   preserve rank-order of funniness (structure carries quality across topics).
5. **Inverted-U benignity** replicates on held-out comics (our R²=0.185
   must survive new data).
6. **Setup-stability:** setup predictability correlates positively with
   punch rating (r≈+0.3), opposite sign to music's uncertainty effect.

## 8. What the geometry is NOT

- Not a claim that jokes ARE chords (no ontological identity; shared
  formal structure only — the ochema research rule: vocabulary without a
  shared constraint is description, not convergence; §7's predictions ARE
  the constraints).
- Not a replacement for performance theory (delivery = voicing; the map
  in Ch.2 stands: same joke, different voicing, different outcome).
- Not complete: superiority dynamics (TA/status movement) and relief
  dynamics (arousal discharge) are real forces in the space not yet given
  coordinates. The geometry currently formalizes the incongruity family;
  TA-status needs its own axis (status differential as a 7th coordinate
  is the leading candidate).
