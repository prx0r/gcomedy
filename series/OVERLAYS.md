# OVERLAYS — persistent lower-third system (all videos)

> Black band below every analyzed clip. Always present, never decorated.
> Three instruments: pause timer, tension sphere, track bar. All driven by
> measured timestamps, rendered deterministically (HyperFrames seek(t)).

## Layout (1080p: 1920×1080, band = bottom 140px, `#07070a`)

```
+----------------------------------------------------------+
|                                                          |
|                      CLIP (940px)                        |
|                                                          |
+----------------------------------------------------------+
| 00:00 |  ●━━━━━━●    TRACK BAR w/ glyphs                 |
| TIMER |  sphere grows here during holds               |
+----------------------------------------------------------+
```

## 1. Pause timer (left, 200px)
- Mono font (gold `#F5C76b`, 44px): `0.00` ticking in centiseconds.
- Runs ONLY in true silence (no speech, below -40dB). Freezes at punch
  onset and latches the peak as `HOLD 2.51s` for 2s, then resets.
- Baseline gaps (~29ms) flash by too fast to read — correct, they should
  be felt as texture, not numbers. Holds ≥0.5s become legible events.
- Timer digits are measurement color (gold), never function color.

## 2. Tension sphere (center, ~300px zone)
- White circle (`#F8FAFC`) on black. Appears when the timer starts.
- Radius: `r = r0 + k·t` (t = hold seconds; calibrated so 2.5s ≈ 3× r0).
- Surface jitter amplitude ∝ accrual rate (steeper expectation = rougher
  skin). Glassy at 0.3s, visibly straining past 1.5s.
- Pop frame at laugh/punch onset: 1 frame of white shards radiating,
  then shards assemble into the punch's keywords (Anatomy-style labels).
- Shards fade in 0.5s. Timer latches peak simultaneously. One frame,
  one pop, one stamp — the series' signature image.

## 3. Track bar (full width, 40px)
- Function glyphs in function colors (COLORS.md) fire at beat onsets.
- Laugh markers: vertical ticks (overlap-mode ON the punch glyph,
  gap-mode AFTER empty track — the two timing modes, instantly readable).
- Callback arcs (gold, half-alpha second returns), button rings (green).

## Behavior rules
- Silence with no accrued weight (dead air): timer runs, sphere does NOT
  grow (stays a small dot). The audience learns: dot = empty, sphere =
  charged. The distinction is the lesson.
- Overlapping speech: timer hidden, sphere hidden. Only the track bar +
  speech ribbon show. Overlays never compete with active content.
- The pop frame is never narrated over. 0.5s of shards + stamp, then voice.

## Build
HyperFrames canvas layers (timer text, sphere circles, track SVG) driven
by one timestamps file per clip: `{t_word_start, t_word_end, t_laugh,
t_hold_start}[]`. Deterministic seek(t) render. `earshot critique` on
final audio before acceptance.
