# EDGE MODULE — theory, how it works, metrics, models

**What:** render one bit at 3 edginess levels (L1 safe / L2 line / L3
overboard-calibration-only) + audience-dependent selection.
**Why:** the line can't be learned from one point — it needs a ladder.
L1→L2 delta = what stepping-over adds; L2→L3 = what it costs.

## Theory

Same THE-LINE as the edgy gate (`docs/EDGY.md`). The ladder adds the
audience axis: identical text lands differently per room, so the
*version* is a function of (bit, character, audience). L3 exists to map
where too-far lives — it is calibration data, never a performance
candidate (`select()` cannot return it, by construction).

Hard rules: L3 varies intensity/frame/commitment, NEVER re-aims the butt
at real victims (veto at every level). Refusals recorded as data.

## How it works

`edge.render_ladder(text, character)` → system prompt carries the
character's deal + threads; per-level instruction appended; backend =
`llm.chat()` (OpenRouter-first if key, else house). Each render gated by
EdgyGate and recorded. `edge.select(ladder, audience)` picks the hottest
render under the room cap. `verdict_for_ladder()` gives pipeline shape.

## Metrics

Per-render: edginess, violation, target, benign_ok (from EdgyGate) +
l1_l2_delta / l2_l3_delta on the ladder. Ladder health: L1 ≤ L2 ≤ L3
edginess monotonic (a non-monotonic ladder = render failure, rerun it).

## Models (OpenRouter, verified 2026-10-17)

Base URL `https://openrouter.ai/api/v1/chat/completions` (OpenAI-
compatible). Key in repo-root `.env` as `OPENROUTER_API_KEY` (gitignored,
600). Model via `OPENROUTER_EDGE_MODEL` (default: Dolphin below).

| slug | in $/M | out $/M | ctx | notes |
|---|---|---|---|---|
| `cognitivecomputations/dolphin-mistral-24b-venice-edition` | 0.20 | 0.90 | 128K | default edge model; uncensored instruct, steerable |
| `thedrummer/cydonia-24b-v4.1` | 0.30 | 0.50 | 131K | uncensored creative/roleplay, strong character consistency |
| `thedrummer/unslopnemo-12b` | 0.40 | 0.40 | 1M | deslopinated training; expressive, less formulaic |
| `thedrummer/skyfall-36b-v2` | 0.55 | 0.80 | 33K | biggest drummer; rivals 70B on creative writing |
| `deepseek/deepseek-chat` etc. | ~0.0003 | ~0.0005 | 164K–1M | effectively uncensored via some providers; cheapest |
| `thedrummer/unslopnemo-12b:free` etc. | 0 | 0 | varies | `:free` variants exist; rate-limited, good for tests |

At our volumes (a ladder ≈ 3×500 tokens ≈ $0.001 on Dolphin) cost is
negligible — but the ASK-before-spend rule still holds for anything
beyond edge renders. House mimo ($0) remains the default for slop/feel;
OpenRouter is preferred for edge L2/L3 where mimo flinches.
