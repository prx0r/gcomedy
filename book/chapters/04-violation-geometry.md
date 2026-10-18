# Violation Geometry — edge, the line, and overshoot as regions

> Draft 2026-10-18. Formalizes characters2 `theory/jokegate` (VIOLATION.md,
> EDGY.md, EDGE.md, foundations.py, edge.py) inside the Ch.3 joke-space.
> Key realization: the jokegate formulas were ALREADY geometric — edge is a
> volume, the line is a decision plane, overshoot is named regions outside
> the viable manifold. This chapter just says so out loud.

## 1. The norm space (where violation lives)

Six axes, one per moral foundation (MFD lexicon v1, foundations.py):
care, sanctity, liberty, fairness, loyalty, authority. Each axis measures
transgression depth 0–1 against the norm surface the audience holds.

A joke's violation is a VECTOR in this space, not a scalar:
```
v = (v_care, v_sanctity, v_liberty, v_fairness, v_loyalty, v_authority)
V = |v| (magnitude = "how much foundation breaks")
```
Care + sanctity read darkest (max-dark even in clean language). Different
lines, different prices — the axes are anisotropic, like the GTVH hierarchy.

## 2. Edge is a volume

```
edge = V × C × D
V = violation magnitude 0–1 (norm-space distance)
C = commitment ∈ {1.0 lean-in, 0.6 pullback} (trajectory property)
D = speaker distance 0–1 (realm 1.0 / freak 0.7 / human 0.3, +0.2 confessional)
```

V, C, D are three orthogonal axes. Edge is the VOLUME of the box they span.
Calibration points from the trials: 0.1 offices, 0.4 profane self-targeting,
0.7 taboo named flatly, 0.9+ maximal violation as plain fact restated.

`edginess = V × (0.5 + 0.5×D)`: distance discounts violation linearly —
at D=1.0 (realm/non-human) the full V counts; at D=0 the violation counts
half. Distance IS the benign-maker: the discount factor is the geometry of
"they can't be canceled, so the room relaxes."

## 3. The line is a plane

```
line_crossed ⟺ V + D > threshold
subject to: target ∈ {powerful, self, species} (never real_victim),
            benign_present (curiosity/boredom/clinical frame, not malice)
```

"The line" comedians talk about is literally a decision hyperplane in
(V, D) space with admission constraints on two further axes (TA legitimacy,
frame presence). Crossing it skillfully = entering the viable region past
the plane with all constraints satisfied. The line is not a ceiling on
intensity — high V with frame + legit target + commitment is L2 (the Louis
zone), not overshoot. Shape requirement, not height limit.

## 4. Overshoot as named regions outside the viable manifold

| Region | Geometry | Gate |
|---|---|---|
| punch-down | wrong octant on TA axis (butt = real victim) | VETO at every level |
| no-frame | V ≥ 0.6 outside the benign basin (malice/absent frame) | FAIL |
| pullback | trajectory crosses the plane then recedes (C collapses 1.0→0.6 mid-path) | WARN, edge ×0.6, cut the retreat |
| thin-dark | path length below minimum for its V (dark meta in <40 words) | WARN, expand setup (Norm buildup: length IS the mechanism) |
| intensity-without-target | large V, TA unresolved (butt unclear) | WARN, name the butt |

Pullback is the most geometric finding: commitment is a property of the
PATH, not the point. The gate scores trajectories, and a trajectory that
crosses then retreats gets discounted — the room punishes the retreat
more than the crossing. Thin-dark is a minimum-path-length constraint:
large-V moves require long approaches (dark + meta → longer setup).

## 5. Ladders sample the manifold along rays

`edge_trial.py`: input bit → L1/L2/L3 renders (increasing V at fixed D) →
gate each → check monotonicity. A healthy ladder is monotonic with visible
deltas: the gate response must rise along the ray. Non-monotonicity =
render failure, not data. Round-1 results (Louis bits as ground truth):
ladders work clean→dark (L2 discovers self-target + sanctity frame
unprompted — the Louis move, found by the renderer); break dark→darker
(nowhere left to go — drifts earnest). L3's characteristic failure
(loud-but-buttless: high V, TA=none) scores below focused violation —
the geometry correctly ranks unfocused loudness under aimed transgression.

## 6. Density discipline = duty-cycle constraint

~1 dark bit in 4–5 (Louis: 22%). High-V excursions require surrounding
mundane to preserve contrast — all-dark sets numb the room (contrast
detonation needs a baseline). This is a trajectory constraint in time:
the path must return to low-V regions between excursions or the manifold
flattens (no foreground without background — priority again).

## 7. Connection to Ch.3 (formal geometry)

- V extends the coordinate system: norm-space magnitude is the 7th
  coordinate's raw material (status differential was the candidate; the
  MFD transgression vector is the better formalization).
- D (speaker distance) is a coordinate of the performer, not the joke —
  joke-space needs a performer-position fiber over each point. Realm/freak/
  human + confessional modifier = discrete positions on that fiber.
- C (commitment) is path-dependent: the metric must integrate over
  trajectories, not just endpoints (consistent with FINDINGS.md: the punch
  is a trajectory — hold then snap — not a duration).
- The viable manifold (plane + TA octant + benign basin) is the first
  explicitly bounded region in joke-space: everything else so far has been
  distances and centers; this is a fence with named outside-regions.
