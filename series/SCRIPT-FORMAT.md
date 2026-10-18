# SCRIPT FORMAT — TTS readout files (`series/<ep>/script.md`)

> One file per episode. The exact text Fish speaks + the direction the
> editor follows. Split so a script can go to synthesis with zero edits.

## Voice lock (all 15 episodes — harmonic consistency)

- Voice: `louis_reference_lab` (`fb015415ebf141999fc882baa0e0834c`)
- Model: `s2.1-pro-free` · Format: mp3 · Key: `FISH_API_KEY` (freaktown/.env)
- Chunks: one POST per beat (12 chunks/episode). Cache by (text, voice,
  settings) — never re-render an unchanged beat. Word timestamps from the
  WebSocket stream feed overlay data (BUILD-PIPELINE stage 4/6).
- Subjects speak through CLIPS, never through impersonation. The narrator
  never imitates a comic.

## File anatomy

```
# SCRIPT — Episode N: Title (~X min)

> Voice: louis_reference_lab · Model: s2.1-pro-free · Format: mp3
> Chunks: 12 (one per beat below). Cache key: (text, voice, settings).

## [0:00] ENGINE NAMED

SPEAK lines — exact Fish input. Plain sentences, punctuation-tuned
(periods = full stops, em-dashes = pivots, fragments = punch weight).

> DIR: PAUSE 2s. CLIP vrIw2i4TtA4 <window> — stop narration, play ≤15s, resume.
> DIR: OVERLAY <card> — fires on the timestamp stream, never narrated.
```

## Rules

1. **SPEAK = ESSAY narration, in order, verbatim except normalization.**
   Every essay sentence appears. Nothing added, nothing reworded.
2. **Normalization (speakable):** drop ALL `[BRACKET cues]` (→ DIR lines);
   drop beat-header artifacts, markdown, videoIds, dates-as-metadata
   ("2026-10-18", "840s", "160 WPM", "Ep N"), card/method citations
   ("see ANALYSIS", "method in X"); keep content dates ("2005"), spoken
   numbers (the beat's one), quotes with attribution; `&` → `and`;
   `≤`/`×`/`→` never in SPEAK (DIR only); em-dashes kept (Fish pauses).
3. **Punctuation tuning (delivery/timing in text):** periods for punch
   weight, em-dashes for turns, fragments for emphasis — already in the
   essays; do not retune beyond converting stray commas that would rush a
   punchline. Paragraph break = breath. Clip gap = full stop + DIR.
4. **DIR lines (`> DIR:`):** stripped before POST. Carry pause seconds
   (match overlay hold timers), SFX (earshot bank), music bed, clip IDs +
   windows, overlay triggers, silence marks (level-5 only where scored).
5. **Two-channel law holds:** theory/paper names never in SPEAK (they live
   in DIR overlay labels + production notes). No statistics beyond the
   beat's one spoken number.
6. **Never narrate over a punchline:** every clip DIR stops narration;
   analysis resumes after. No exceptions.
7. End each file with a word count + voice-time estimate (@150 WPM Fish
   pace + clip/pause occupancy vs the 840s board).
