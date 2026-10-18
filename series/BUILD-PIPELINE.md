# BUILD PIPELINE — essay to rendered video

> How a video gets constructed from everything in this repo. Deterministic,
> staged, gated. No stage starts until the previous gate passes.

## Inputs (per video, all in repo)

| Input | Path | Provides |
|---|---|---|
| Essay script | `series/<fn>/ESSAY.md` | Narration, beats, clip cues |
| Structure | `series/<fn>/STRUCTURE.md` | Beat map, rhythm map, clip table |
| Techniques | `series/<fn>/MICRO-TECHNIQUES.md` | Demoable moves, good/bad table |
| Schema entries | `series/MICRO-SCHEMA.md` | Agent-executable technique specs |
| Clips | `series/resources/<fn>/CLIPS.md` | Candidates with links/views/durations |
| Craft talk | `series/resources/<fn>/CRAFT_TALK.md` | Comic process quotes |
| Timed exemplars | `series/resources/exemplar_timed_*.json` | Beats, punches, laughs, syllables |
| Grammar | `series/VISUAL-GRAMMAR.md` + `OVERLAYS.md` + `COLORS.md` + `TROPES.md` | Every visual rule |
| Rhythm law | `series/README.md` §1 | Centricity, reservoir, conjunct, consistency, consonance, grid |

## Stages + gates

### 1. SCRIPT LOCK
Assemble narration from ESSAY.md at 160 WPM against the beat map.
Word budget per beat; narration 1,100–1,600 words + clips/pauses =
total 9–15 min (matches README §2 + STORYBOARD-TEMPLATE).
GATE: word counts per beat sum to budget. No theory in narration
(check against production notes — paper/author names out; at most ONE
measured number per beat, always paired with its on-screen gold card;
all other statistics live on gold overlay cards + production notes,
never in voiceover). This is the two-channel rule: accessible voiceover,
precise overlays.

### 2. CLIP PULL
Pull candidates from CLIPS.md + exemplars. Fair-use ≤15s each.
Transcripts required before a clip enters the timeline.
GATE: every clip has transcript + timestamps + clearance note.

### 3. TIMING EXTRACTION
Word-level ASR on each clip → `{t_word_start, t_word_end}`.
Laugh onsets via energy-burst detection (measured at build, never invented).
Hold durations, speech rates, pause timers computed.
GATE: all timestamps present; estimated data tagged (Rock/Mulaney rule).

### 4. OVERLAY DATA BUILD
One timestamps JSON per clip: beats, punches (pause_before), laughs,
syllables, function labels. Drives: subtitles (blue/red), track bar,
glyphs, pause timer, tension sphere, metronome, speech ribbon.
GATE: JSON validates (t0<t1, pauses ≥0, labels ∈ function set).

### 5. COMPOSITION BUILD (HyperFrames)
seek(t) canvas + GSAP timeline per sequence. Colors from COLORS.md only.
Typography: Anton titles, Inter Tight body, gold mono timers.
Music bed at fixed BPM; section changes on bars (rhythm law §1).
GATE: `hyperframes lint` 0 errors. Probe stills approved (3+ frames).

### 6. VOICE (Fish, our 7 voices)
Narration via `s2.1-pro-free`, word timestamps back into overlay data
(per-word subtitle sync + emphasis driving). Cache by (text, voice).
GATE: voice matches beat assignment; no unapproved voice appears.

### 7. FOLEY + MIX (earshot)
Procedural SFX from bank (`sfx`/`kit`) placed by measured peak.
Music bed ducked under VO. Master to -14 LUFS.
GATE: `earshot critique` — fix FIRST items in order; music-bed + level
gaps are known v1 issues, mark intentional or fix.

### 8. FRAME QC (Jev eyes)
Probe stills through `jev-1.14` Noul checks (text legible? glyph correct?
color discipline held?). ~$0.0001/shot. Badges: subtitle contrast,
glyph correctness, no red outside punch/violation.
GATE: all checks pass or documented waivers.

### 9. RENDER
`hyperframes render` deterministic MP4. Full watch-through at 1x by a
human before publish. Retention review: first sharp drop → diagnose →
fix cause → re-render.

### 10. PUBLISH + BANK
Upload + chapters + glossary cards in description. Measurements from the
build (timings, rates, ratios) deposited back to the theory bank
(experiments/ or resources/DATA.md). The video pays for the next one.

## Rhythm + music (applies at stages 5–7)
- BPM fixed per video; sections change on bars; metronome overlay during
  setups; freeze mid-swing at punch.
- Tension bar + pause timer + speech ribbon from overlay data (stage 4).
- Theory never narrated; gold overlay labels carry operator names
  (two-channel rule: accessible voiceover, precise overlays).
