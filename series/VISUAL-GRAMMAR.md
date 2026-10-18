# VISUAL GRAMMAR v1.0 — canonical spec for all videos

> Single source of truth for every overlay, color, glyph, and subtitle rule.
> Rendering agent: implement exactly this. No invented elements.

## 1. Colors (from COLORS.md — normative)

| Function | Hex | Used for |
|---|---|---|
| Setup blue | `#3B82F6` | Setup subtitles, setup blocks/glyphs |
| Escalation orange | `#F97316` | Escalation glyphs, stair risers |
| Punch red | `#E8102E` | Punch subtitles, punch glyphs, violation marks ONLY |
| Tags rose | `#FB7185` | Tag ticks, diminishing per hit (-20% opacity each) |
| Callback gold | `#F5C76B` | Return arcs, labels, measurements, timers |
| Button green | `#22C55E` | Closure rings |
| Premise violet | `#8B5CF6` | World-plates, premise cards |
| Pause white | `#F8FAFC` | Sphere, silence markers |
| Background | `#07070a` | Every frame behind content |
| Text | `#f3f1ec` | Body text. Muted `#8d8b93` secondary. |

Hard rules: red = punch/violation ONLY. Gold = callbacks/measurements/theory
ONLY. No other colors for these meanings, ever.

## 2. Subtitles (all clips, all videos)

- Setup speech: blue. Punch speech: red. Switch exactly at the turn word.
- Tags: rose. Callback returns: gold. All other speech: white.
- Font: Inter Tight 500, 22px minimum at 1080p, lower third, never covering faces.
- Source: word-level timestamps (scribe/ASR). No guessed timings.

## 3. Lego blocks (Episode 0 grammar, reused in explanations)

- Setup block: blue rounded rect. Punch block: red rounded rect. Tags: rose
  studs snapping on. Premise: violet plate underneath. Bit = plate of blocks.
- Blocks snap with a 2-frame scale pop + click SFX (earshot). Never slide.

## 4. Track bar + glyphs (analysis overlay)

Full-width 40px bar under the clip. Glyphs fire at beat onsets, persist:
- Setup: foundation line, thickens with weight.
- Escalation: staircase risers, one per pass.
- Punch: break mark + swap arrow (that→this).
- Tags: diminishing echo ticks along punch direction.
- Callback: return arc to earlier marker (gold; half-alpha second return).
- Button: closing ring (green).
- Laugh markers: vertical ticks (overlap-mode ON punch glyph; gap-mode AFTER gap).
- Pause timer: gold mono `0.00`, runs in true silence only, latches peak 2s.
- Tension sphere: white circle, radius ∝ hold seconds, jitter ∝ accrual;
  pops to shards at laugh onset; shards assemble punch keywords.

## 5. Timing instruments

- Pause timer digits: gold mono 44px. Baseline gaps flash past (texture).
  Holds ≥0.5s become legible events.
- Speech ribbon: height = syllables/sec (requires syllables field — present
  on all 5 timed exemplars, dict-v1 tagged).
- Tension bar: fill ∝ accrued expectation; discharges vertically at laugh.
- Metronome (Beat 4): arm swings on beat during setups; FREEZES mid-swing
  at punch onset, holds 1s, drops.

## 6. Motion rules

- Hard cuts for beats/violations. Dissolves for ontology only (parts→whole,
 idetour transitions). Never crossed.
- Deterministic renders only (HyperFrames seek(t) or equivalent). Same input,
  same frames. Probe stills approved before full renders.
- Never narrate over a punchline. Pause clip → analyze → resume.
- Silence policy: 10s open + coda black are the only level-5 silences.
  Mid-film holds 1–3s max, ≤2 per video.

## 7. Type

Titles Anton. Body Inter Tight. Overlays Inter Tight 500. Mono digits for
timers (gold). Devanagari verified against repo for sutra text (c1_sivasutra.md).

## 8. Data honesty on screen

- Every number gold = measured (pause durations, word counts, rates, ratios)
  or sourced (paper, timestamp). No invented stats.
- Estimated data (Rock/Mulaney `estimated: True`) must carry an on-screen
  "timing estimated" tag until measured captions replace it.
- Applause ≠ laugh: pop frames fire on `type=='laugh'` onsets only.
