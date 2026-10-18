# SHARED ESSAY — The Geometry of Comedy

> How this works: OWNER drops speech blocks verbatim under SPEECH (locked —
> never edited by agent). AGENT fills RENDER alongside: visuals, timings,
> tech, prompts, voice direction. Status per beat: ⬜ todo / 🟨 rendering /
> 🟩 rendered. Word counts + durations tracked for the 160 WPM budget.

## Working agreement
- SPEECH is yours. I never rewrite it. If a line won't render or won't fit
  the time budget, I flag it under NOTES, you decide.
- RENDER is mine: shot rows, timestamps, build commands, asset lists, voice
  direction, QC gates. Everything needed for the other agent to build it.
- Timings are cumulative from 0:00. Keep the running total honest.

---

## BEAT 0 — SILENCE OPEN 🟨 rendering

### SPEECH (owner, verbatim, locked)
> [No words for 10 seconds.]
> "silence."
> "Everything you are about to see comes from here. And returns here.
> Nothing in this film ever leaves."

### RENDER (agent)
- **0:00–0:10** black, true silence. No title, no sound. (Level-5 silence —
  intentional; mark in edit notes so nobody "fixes" it.)
- **0:10** whisper "silence" → hard cut to white, SILENCE in black ink
  (Anton 120px), hold 2s → slow fade to black by 0:14.
- **0:14–0:25** single sine E4 + thin white line draws across black;
  line + tone dissolve downward. Twice more (two waves, small chord).
  No narration over this.
- **Tech:** HyperFrames composition `scene-00.html`, canvas lines, earshot
  procedural sine + envelope (same data drives line + audio). `dissect check`
  n/a (no reference). `earshot critique` expect sparse-flagged — mark
  intentional.
- **Voice:** louis_reference_lab, `[whispering]`, ~90 WPM. "silence." half
  normal pace. Second passage flat, 140 WPM, no performance. 2s silence
  after "here." is in the take.
- **Words:** 21 → ~8s spoken + 17s silence/music = 25s total. ✅ in budget.

### NOTES
- Owner to confirm: whisper or full voice on "silence."?

---

## BEAT 1 — POINT → LINE → TRIANGLE → TETRAHEDRON 🟨 rendering

### SPEECH (owner, verbatim, locked)
> [Awaiting owner's words — beat designed, speech not yet dictated.]
> Draft scaffold (replace): "In the beginning, there is a point." ...
> "Four points. The smallest thing that can have an inside."

### RENDER (agent)
- **0:25–1:55** (~90s). E-minor construction per tetrahedron-intro.md:
  dot+E4 (point) → 2nd dot + F♯, "2 semitones" edge label (line) → F♯ slides
  to G, B enters, E–G–B triangle (Autumn Leaves gesture hidden inside) →
  D enters, Em7, tetrahedron rotates once → dissolve to black, E rings on.
- Timbre follows geometry: sine → two sines → triangle wave → full band.
- Edge labels in gold; pitch labels per vertex. Plate rule: every number
  measured (semitone counts are exact by construction).
- **Tech:** HyperFrames canvas + GSAP timeline (same pattern as laptop
  scene-03a). Dots/lines/triangle/tetrahedron as SVG layers. Shaders
  `NoiseDissolve` for the final dissolve. Band entry = licensed Bill Evans
  excerpt (fair-use, transformative commentary) or re-recorded head.
- **Voice:** louis, 135 WPM, quiet awe. One line per stage, nothing more.
  The music carries the argument; narration only names what to look at.
- **Budget:** ~200 words → ~75s + 15s pure music = 90s. ✅

### NOTES
- Needs owner's actual words. Scaffold above is placeholder — dictate yours.
- Confirm: Bill Evans excerpt vs re-recorded head (clearance)?

---

## BEAT 2 — PREMISE PROLOGUE ⬜ todo

### SPEECH (owner, verbatim, locked)
> [Awaiting owner's words.]
> Scaffold: Rock quote → premise defined → Autumn Leaves shared world →
> "each person leaves their world" → "the premise of this video is: what
> is important in comedy?" → hard cut to black.

### RENDER (agent)
- Rock clip (fair-use, ≤8s): freeze on "premise", kinetic type isolate.
- Chord symbols draw in real time under Bill Evans head (Dm7–G7–Cmaj… —
  verify against recording). Second rendition, same symbols (shared
  structure, different performance).
- Audience silhouettes dissolve at edges into chord symbols (openverse CC).
- Final question on black. Hard cut to disclaimer.
- **Voice:** louis 150 WPM conversational; punch words INSTANTLY / LEAVES /
  SHARED; final question genuine lift, not rhetorical flat.
- **Budget:** ~150 words → ~60s + clips/music ≈ 2 min. ✅

### NOTES
- Rock quote source: Chris Rock (via Nerdwriter transcript), NOT Seinfeld
  roundtable. Do not misattribute on screen.

---

## BEAT 3 — COLD OPEN: DELIVERY ⬜ todo
*(voiceover-01 SEQ 1–2 already written — migrate lines here on owner's go)*

### SPEECH (owner, verbatim, locked)
> [Owner: confirm voiceover-01 SEQ 1–2 text stands, or dictate changes.]

### RENDER (agent)
- AI-voice disclaimer over black → "most important thing in comedy?" kinetic
  type → 10s black → "Delivery." red, center.
- Cake diagram builds per ingredient (anatomy labeled-figure pattern);
  timing revealed as oven/pan, not ingredient.
- Mother gag over 1970s-glamour portrait (pixabay, clothed — audacity, not image).

---

## TEMPLATE FOR NEW BEATS (copy-paste)

## BEAT N — <title> ⬜ todo

### SPEECH (owner, verbatim, locked)
> [Paste dictated speech here. Locked on paste.]

### RENDER (agent)
- Timestamps + shot rows.
- Visuals (specific builds).
- Tech (repo + method + commands).
- Voice (pace, emphasis, pauses, cues).
- Words → minutes math.

### NOTES
- Flags for owner.
