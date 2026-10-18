# EDGY GATE — theory, how it works, metrics

**Round:** 2. **Question:** did the bit step over the line and lean in —
or flinch, pull back, or punch down? Edginess is NOT required (office
comedy passes at 0.1). This is a veto + commitment check.

## Theory

`theory/research/THE-LINE.md` (owner thesis: non-humans can't be canceled,
so they explore and humans laugh). Crossing formula:

```
line_crossed ⟺ violation + distance > threshold
subject to: target ≠ real_victim, target ∈ {powerful, self, species},
            benign_present (curiosity/boredom/clinical, not malice)
```

Four lines: HARM (butt ≠ victim), STAKE (non-human = infinite room),
IDENTIFICATION (audience laughs from outside), DISTANCE (master dial —
at 1.0, distance itself is the benign-maker). Dark meta needs Norm
buildup: darker + more meta → longer setup (length IS the mechanism).

## How it works

`EdgyGate.classify(text, character)`:

1. **LLM semantic read** (reader, never laugh judge): violation 0–1,
   target (victim/powerful/self/species/none), benign frame + kind,
   dark_meta flag, commitment (commit/pullback). Disk-cached by hash.
2. **Exemplar anchors**: max cosine (stdlib TF) to 33 owner-approved edgy
   bits (realm) + 17 approved-safe bits (pilots). Prior, not verdict.
3. **Lexical floor**: named taboos are always ≥ their floor.
4. **Distance** from roster (realm 1.0 / freak 0.7 / stage 0.3 / ?=0.5).
   `edginess = violation × (0.5 + 0.5×distance)`.
5. **Verdict**: FAIL iff punch-down veto (victim butt, no frame) or
   offensive (violation ≥0.6, no frame). Dark-meta-short and pullback
   WARN with edits (Norm buildup; cut the retreat). Realm-distance carry
   warns when distance does the benign work alone.

Without the LLM reader: lexical floor only, target unresolved (said
honestly), never vetoes on target. No Jev model is called anywhere —
`jevp_agent` is local-policy only (see PIPELINES.md §Jev note).

## Metrics / calibration (2026-10-17)

| set | routing |
|---|---|
| 6 realm exemplars | 6/6 PASS, edginess 0.25–1.0, targets self/powerful, benign found |
| Jesus "crucified" bit | PASS via distance carry + 3 warns (matches owner's own "needs buildup" note); same text as freak FAILS |
| 6 pilot bits | 6/6 PASS, edginess 0.0–0.1 |
| Satan "children" bit | PASS (victim-as-stakes + boredom frame, per exemplar approval) |

Confidence: "limited" (reader can misread; human resolves ambiguity).
Known hard case: lexical violation scores 0.0 on most exemplars — the
morality-model fine-tune (THE-LINE "next step") would replace the floor.
