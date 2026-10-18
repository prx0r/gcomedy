# STORYBOARD TEMPLATE — all series videos

> Shot rows, not essays. Every video gets `series/<fn>/STORYBOARD.md` in
> this format. Beethoven shape underneath: motif (statement) → development
> (variation) → recapitulation (return changed). Beats map onto it.

## Row format (one row per shot)

| # | t0–t1 | Visual | Audio | Overlay data | Dur |
|---|---|---|---|---|---|
| S01 | 0:00–0:08 | Black, kinetic title | Cold-open line (Fish) | none (level-5 silence) | 8s |

Fields: `#` shot id, `t0–t1` timestamps, `Visual` (what's on screen +
build ref), `Audio` (narration line / clip / music / foley + timestamps),
`Overlay data` (timestamps JSON keys driving glyphs/timers), `Dur`.

## Beethoven mapping (structural, not decorative)

| Sonata section | Series beat | Function |
|---|---|---|
| Exposition (motif stated) | Cold open + proof | State the thesis-motif plainly |
| Development (motif varied) | Lens → persona → case → specimen | Vary the motif across domains/comics |
| Recapitulation (return changed) | Failure → universal → close | Motif returns carrying everything since |
| Coda (hook) | Last 60s | Next video's motif previewed |

## Rules
- Every shot has timestamps before anything renders. No untimed shots.
- Clip shots cite: videoId + start/end + transcript status + clearance.
- Overlay shots cite: timestamps JSON path + keys used.
- Narration lines quoted verbatim from ESSAY.md (never paraphrased in rows).
- Total runtime sums to 9–15 min or the board fails review.
