---
name: motion-probe
description: Deterministic motion-graphics workflow (seek(t) + Playwright probes). Use for titles, typography, vortex/probability animations.
---

# Motion Probe — process notes (proven 2026-10-18)

## What worked
Wrote a 6s test film (`film.html`: title + progress bar, Funnier skin colors
`#07070a/#e8102e`), served via `python3 -m http.server`, screenshotted at
t=0.5/3.0/5.9 with Playwright + system chromium (`--no-sandbox`,
`--enable-unsafe-swiftshader`). 3× 1280×720 stills. Path proven end to end.

## The workflow (from claude-motion-design, adapted)
1. Write `film.html` with a single `window.seek(t)` function — no CSS
   transitions, no timers. Every frame is a pure function of time.
2. Probe stills first (`probe.py` pattern in trial): stills at 3–4 timestamps
   → approve before any full render.
3. Full render: N subframes per frame on a 180° shutter, `tmix` blend, never
   across a hard cut. BT.709 encode.
4. Audio: find the real drop by band energy (never trust auto beat grids),
   place SFX by measured peak, two-pass loudnorm to -14 LUFS.
5. Mux: `ffmpeg -i video.mp4 -i audio.wav -map 0:v -map 1:a -c:v libx264
   -crf 16 -c:a aac -shortest final.mp4`.

## Rules
- Beat-sync by construction: scenes on a beat map, drop on the key frame.
- Never narrate over a punchline in probe stills — pause points are approval
  gates, same as the gold rule (clip → pause → analyze → resume).
- Fix one scene without touching the rest (deterministic = same input,
  same frames).
