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

## TTS call
`POST https://api.fish.audio/v1/tts` with `reference_id` = voice id,
`model: s2.1-pro-free` header, `format: mp3`. Cache narration by
(text, voice, settings) — never re-render the same line twice.

## Word timestamps → animation
Fish documents WebSocket streaming with word-level timestamps. Use them to
drive visuals per word: "at no point has it ever truly been a laptop" triggers
the part-by-part dissolve. Keep the animation; regenerate only the narration
segment on rewrite. This is how narration and picture stay in sync without
re-rendering scenes.
