---
name: earshot-qc
description: Foley generation and audio sync critique with earshot (CPU-only). Use for laptop-sequence sound and full-film audio QC.
---

# Earshot QC — process notes (proven 2026-10-18)

## Install
`pip install --break-system-packages -e .` from `essay1/tools/earshot/`.
First run downloads ~1GB audio models (CLAP + AST) — cached at
`tools/earshot/.cache/hf`, gitignored, keep on disk. `forge` is slow on CPU;
prefer the `sfx` bank path.

## What worked
`earshot describe` on a synthetic 0.25s click → "wooden block hit (z+3.1),
kalimba (z+3.0), glass ting (z+2.5)". Correct reading, calibrated z-scores
(≥3 clear, 2.5–3 plausible). Proves the describe/match engine on this box.

## Foley loop for the film
1. `earshot sfx <id>` — render procedural clicks/hinges/whooshes from the
   201-effect bank by id, aimed at measured sync points. Seconds, no network.
2. `earshot kit` — render a whole scene's effects with sync points.
3. `earshot critique film.mp4` — scorecard vs pro launch films; fix FIRST
   items in order (e.g. "nothing reaches body level until 0:01.01").
4. `earshot match` — verify a rendered SFX against its description
   ("laptop hinge click" vs alts) before accepting.
5. Mirelo SFX 2.0 (fal.ai, $0.01/s) only when procedural foley isn't
   convincing — and only with owner yes (money rule).

## Gotcha
`forge` hung on first run (model download). If any subcommand hangs >3 min,
`pkill -f earshot`, confirm models cached, retry — second run is fast.
