# MICRO-TECHNIQUE SCHEMA v1.0 — for AI agents

> Every technique in every video follows this schema. An agent reading a
> filled schema entry must be able to: detect the technique in a transcript,
> score good-vs-bad, generate an implementation, and cite why it works.
> Think audio labeling: segments with start/end, label, confidence, features.

## Schema fields (all required unless marked optional)

| Field | Type | Meaning |
|---|---|---|
| `id` | string | `setup.pipeline-check`, `tags.pov-shift`, ... |
| `function` | enum | setup/escalation/punch/tags/callbacks/button/premise/pause/joke |
| `name` | string | Human name ("Pipeline check") |
| `definition` | 1–2 sentences | What it IS (not what it's for) |
| `good` | list of observables | Detectable criteria, each boolean-testable on text/timing |
| `bad` | list of anti-patterns | Detectable failures, each boolean-testable |
| `implementations` | list of {procedure, example} | Concrete steps + real example (comic/bit named) |
| `why` | mechanism + data | Causal story + citations (papers, measurements, trial results) |
| `labels` | label spec | Audio-label analog: segment type, boundaries, features to extract |
| `thresholds` | numbers | Pass/fail cutoffs where known (else "calibrate") |

## Worked example (complete — template for all others)

```json
{
  "id": "setup.pipeline-check",
  "function": "setup",
  "name": "Pipeline check",
  "definition": "Five-gate audit (truth, attributes, angle, combo, trim) applied to a setup before staging.",
  "good": [
    "truth statable in one boring line",
    ">=3 quirks listed before angle chosen",
    "attitude explicit (cartoon exaggeration present)",
    "combo matches one of 4 structures",
    "funnest word is sentence-final"
  ],
  "bad": [
    "backstory with no tension or laugh",
    "setup >2x punch length with no escalation function",
    "attitude shifts mid-setup",
    "punch words appear in setup"
  ],
  "implementations": [
    {"procedure": "Truth→Attributes→Angle→Combo→Trim on vending-machine bit",
     "example": "r/StandUpWorkshop pipeline (Truth/Exaggeration/Misdirection combo)"},
    {"procedure": "Halve the setup; if it still works, ship the half",
     "example": "Seinfeld syllable-shaving (Pop-Tart transitions)"}
  ],
  "why": "Platform economics: 2.8:1 setup:punch ratio (335 KT sets); setup predictability r=+0.33 (Exp 3); Rock premise rule (Talking Funny). Each gate removes one known failure mode with measured cost.",
  "labels": {"segment": "setup", "start": "first premise word", "end": "last word before turn", "features": ["word_count", "quirk_count", "attitude_present", "final_word_funniness"]},
  "thresholds": {"max_setup_words": 25, "min_quirks": 3, "platform_ratio": 2.8}
}
```

## Rollout (all videos, same treatment)
- [x] setup (example above + MICRO-TECHNIQUES.md bank)
- [ ] escalation, punch, tags, callbacks, button, premise, pause, joke
- Each video's bank converts 1:1 into schema entries. Agents fill the rest;
  this file + the setup example are the spec they implement against.
