---
name: fish-voices
description: Our 7 Fish Audio voice clones + word-timestamp animation driving. Use for all narration.
---

# Fish Voices — live inventory (verified 2026-10-18)

## Our voices (`self=true` via api.fish.audio)
| Voice | Model id | Use |
|---|---|---|
| louis_reference_lab | `fb015415ebf141999fc882baa0e0834c` | Louis CK narration, storytelling bits |
| ari_reference_lab | `dbeb1d68566245e2b857617b830e8031` | Ari |
| seinfeld_reference_lab | `f73820b82341447daa943f59ae414415` | Seinfeld writing-process VO |
| casey_reference_lab | `9c36c951cee84457a5cc9f94387e9a42` | Casey |
| kam_reference_lab | `6ab05a976a684ea49798183783cbd3f9` | Kam |
| pickles_reference_lab | `100e10e7c5464a10b5120a01ade115a2` | Pickles |
| Verity | `9156b1acc82641ea941294f20116057d` | Verity |

Model: `s2.1-pro-free` ($0, fair-use). Key: `FISH_API_KEY` in
`freaktown/.env` (51 chars, verified live). MCP configured at
`~/.config/opencode/opencode.jsonc` (`fish-audio` remote, enabled).

## TTS call (verified against docs.fish.audio 2026-10-18)
`POST https://api.fish.audio/v1/tts` with `reference_id` = voice id,
`model: s2.1-pro-free` header ($0 tier, explicit enum — never omit, else
falls back to paid `s2.1-pro`), `format: mp3`. Cache narration by
(text, voice, settings) — never re-render the same line twice.
Request template (series narration lock):
`{text, reference_id, language: "en", normalize: true, latency: "normal",
temperature: 0.7, chunk_length: 200, min_chunk_length: 50,
condition_on_previous_chunks: true, format: "mp3", sample_rate: 44100,
mp3_bitrate: 128}` — `normal` = best quality (not `balanced`);
`condition_on_previous_chunks` keeps voice consistent across our 12
beat-chunks; `language: "en"` pins normalization + timestamp alignment.
`prosody.speed` (0.5–2.0) adjusts pacing without regenerating audio —
use for rush/velocity demos, never as a fix for bad timing.

## Word timestamps → animation (real routes, not folklore)
- `POST /v1/tts/stream/with-timestamp` (HTTP) and
  `GET /v1/tts/live/with-timestamp` (WebSocket) — timestamps ride the
  synthesis stream. Same TTSRequest body + model header (works on
  `s2.1-pro-free`). Use them to drive visuals per word: "at no point has
  it ever truly been a laptop" triggers the part-by-part dissolve.
- Keep the animation; regenerate only the narration segment on rewrite.
  This is how narration and picture stay in sync without re-rendering scenes.

## S2 delivery cues (work on s2.1-pro-free — all tiers, per docs)
Bracket cues go IN the synthesis text (they are not editor marks):
pauses `[break]` (brief) / `[long-break]` (extended); stress `[emphasis]`
(place directly before the word); tone `[whispering]` `[soft tone]`
`[calm]` `[confident]` `[curious]` `[sarcastic]`; sounds `[chuckling]`
`[sighing]` `[gasping]` (never `[laughing]` — the narrator never laughs
at their own jokes; room laughter is real audio, never synth).
Free-form cues allowed (`[barely holding it together]`) but series
scripts use the whitelist above only. Max 3 combined per sentence, one
primary emotion per beat — comedic restraint. Sentence-start placement.
S1 `(parenthesis)` syntax is DEAD (retires 2026-12-31, no auto-convert).

## NOT the lock (test before trusting)
- `drama-3` (plain-language direction, `<emphasis>`/`<whisper>`/`<fast>`/
  `<slow>` paired tags, multi-speaker): separate model header, tier
  unclear — stays an experiment until one beat renders on it. Series
  lock remains `s2.1-pro-free` + S2 cues.
- Fish `transcribe-1-pro` (STT with timestamps): paid path for clip ASR.
  Free path is on-box faster-whisper (installed: faster-whisper 1.2.1 +
  torch) — stage-3 clip word-timestamps at $0. Use Fish STT only if
  local quality fails on a clip.
