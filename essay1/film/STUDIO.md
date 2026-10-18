# STUDIO — browser-based AI film studio (live)

## What's running
- HyperFrames project: `essay1/film/laptop-film/` (lint: 0 errors)
- Composition: `compositions/scene-03a.html` — 20s laptop deconstruction,
  GSAP paused timeline, local gsap asset (no CDN dependency at render)
- Render proven: `hyperframes render . -c compositions/scene-03a.html -f 24`
  → 20.0s MP4 in 28.5s (software GL). Frames verified: exploded stack,
  labels, ghost word all correct.

## The edit loop (you direct, Claude builds)
1. Edit `essay1/film/screenplay.md` (narration + intent) and/or
   `essay1/film/shots.json` (shot durations, camera, audio cues).
2. Claude regenerates `laptop-film/build-scene-03a.mjs` output
   (`node build-scene-03a.mjs`) or edits the composition directly.
3. `npx hyperframes preview --port 3002 --no-open` → watch in browser
   (via `ssh -N -L 3002:127.0.0.1:3002` from your laptop).
4. Direct in words ("slower deconstruction, close-up on the processor
   before pulling back") → Claude edits → preview hot-reloads.
5. `hyperframes render` when approved. Foley via earshot, mux with ffmpeg.

## Director commands that work now
- "Slow this sequence down" → stretch GSAP tween durations in the timeline.
- "Rotate the laptop" → change azimuth in `build-scene-03a.mjs`, rebuild.
- "Show the motherboard close-up" → new camera: re-fit projection bounds
  around the board part, render as separate shot, cut in via shots.json.
- "More dramatic transition" → swap easing (`power2.in` → `expo.in`),
  add earshot downlifter under it.

## On your machine (owner)
```
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
ssh -N -L 3002:127.0.0.1:3002 root@<vps>
# open http://localhost:3002
```

## v2 gaps (known, from earshot critique)
Music bed under the whole film (duck under VO), master to -14 LUFS,
fill the 2.1s silent holes or make them deliberate stops. Fish narration
line over the ghost beat (word timestamps drive the "laptop" hold).
