# gcomedy — The Geometry of Comedy

Book + research library + film-production stack for *The Geometry of Comedy*
and the video essay *"Comedy, music, and the illusion of self."*

## What this repo is

| Area | Dir | State |
|---|---|---|
| Book outline + chapters | `book/outline/`, `book/chapters/` | OUTLINE.md + Ch.2 draft |
| Core essay | `book/musicomedy.md` | Done |
| Research list (40+ sources) | `book/RESOURCES.md` | Done |
| Timing thesis | `book/THESIS-timing-is-composition.md` | Done (other agent) |
| Gold video-essay refs | `book/gold/` | 7 files |
| Experiments 1–3 + findings | `experiments/` | Done, green |
| Video-essay production | `essay1/` | Active build |
| Theory library | `library/` | Imported |

## Film stack — what to clone, what it does, what it needs

All clones live in `essay1/tools/` (pinned as gitlinks). Clone with `--depth 1`.

### Making scenes (pick ONE orchestrator)

| Repo | Function | Deps | How to use |
|---|---|---|---|
| `lemomo-ai/lemo-opuscar` (198M) | 51 film styles, full direction: animation, narration, music, sound. Has "Exploded Teardown" style — keyboard opens, parts separate, camera goes under the board. Closest to the laptop shot. | Claude Opus 5.5 (styles tuned for it) | Directing session: pick style, bring story |
| `GTKottman/mortiflix-oss` (24M) | Staged pipeline: brief→script→style frames→animatic→final, you approve each gate. AGPL. | Claude Code login or Anthropic key, Remotion | Long-form across sessions |
| `Remocn/remocn-studio` (217M) | Desktop app: agent writes real Remotion project, live preview updates as code changes, click-to-edit, no re-render between edits. MIT. | Linux .deb/AppImage, Claude Code | Daily driver for scene-making |

### Rendering animation (pick ONE)

| Repo | Function | Deps | How to use |
|---|---|---|---|
| `howseen-ai/claude-motion-design` (8.5M) | **PROVEN ON THIS BOX.** Deterministic HTML+Playwright+ffmpeg films. `seek(t)` function, probe stills, beat-sync, -14 LUFS audio. | python + playwright + chromium + ffmpeg (all present) | Write `film.html` with `seek(t)`, probe stills, full render, mux |
| `academa-labs/manimgx` (138M) | Manim-compatible API, Rust/WebGPU renderer, browser + pip | Rust toolchain or pip, GPU helps | Manim scenes, fast preview |
| `vumichien/manim-skill` (3.8M) | 4-role agent pipeline turning papers into narrated Manim | manim (BROKEN here — hangs, do not use) | Parked until roomier iron |
| `VideoZero/skills` (396K) | Motion Canvas framework ref + agent HTTP API | Motion Canvas editor | Diagram animation via editor API |

### Diagrams & 3D objects

| Repo | Function | Deps | How to use |
|---|---|---|---|
| `wheresryan22/anatomy` (15M) | **PROVEN.** Interactive exploded isometric figures (SVG/WebGL). Zero deps, node ≥20. | node only | `node examples/<thing>/build.mjs` → self-contained HTML. Steal `desk-computer` pattern for the laptop |
| `Yoosseph/pc-anatomy` (9.6M) | Real hardware disassembly: ~400 parts, all code-generated three.js, auto-disassemble timeline | npm install + build | Accurate mechanical opening, adapt scale tree |
| `shader-effects-inc/shaders` (27M) | **200+ WebGPU effects** as components (gradients, noise, glass, transitions). MIT engine. Has agent skill + MCP + CLI. v4.0.2 has frame-locked `renderFrame({deltaSeconds})` for deterministic offline rendering. | `npm install shaders` | Backgrounds, transitions, dissolves (laptop→circuitry→spanda) |
| `mdrayyanhussain2006/pc-components-manual` | NOT cloned yet — Blender source disassembly | Blender (absent) | Skip for now |

### Editing & assembly (replaces Resolve — pick ONE)

| Repo | Function | Deps | How to use |
|---|---|---|---|
| `0xsline/OpenChatCut` (154M) | Full timeline editor (narration/effects/video/music/captions/transitions), MCP-driven, undo/redo, local-first. AGPL. | Build from source | Assembling the full film |
| `KyaniteLabs/kinocut` (28M) | Guardrailed FFmpeg MCP tools + receipts + quality gates | MCP host (Claude Code) | Agent-driven cuts, captions, checks |
| `WhiteTowerAI/cut-as-code` (158M, trimmed) | Reviewable cuts, grading, B-roll, captions as skills | Claude Code | Edit-time skills |
| `simplexlabs/montage`, `gomotion-io/gomotion` | Remotion compositions from prompts | npm + directing session | Titles, montage, graphic sequences |

### Audio: voice + foley + QC

| Repo / service | Function | Deps | How to use |
|---|---|---|---|
| **Fish Audio MCP** (configured in `~/.config/opencode/opencode.jsonc`) | TTS + voice clones. **Our 7 voices live:** `louis_reference_lab`, `ari_reference_lab`, `seinfeld_reference_lab`, `casey_reference_lab`, `kam_reference_lab`, `pickles_reference_lab`, `Verity`. Model `s2.1-pro-free` = $0. WebSocket streaming gives word-level timestamps → drive animation per word. | `FISH_API_KEY` in `freaktown/.env` | MCP tools or `POST api.fish.audio/v1/tts` with `reference_id` |
| `Leonxlnx/earshot` (14M) | **PROVEN.** Ears for agents: describe/match/critique audio, 201-procedural-SFX bank (`sfx`/`kit`), sync measurement. CPU-only. | pip install; first run pulls ~1GB models (cached, gitignored) | `earshot sfx` for foley → `earshot critique film.mp4` to verify sync |
| Mirelo SFX 2.0 (fal.ai, hosted) | Video-to-audio: give MP4, get synced foley. $0.01/s promo. | FAL key, $$ | Only when procedural foley isn't convincing |

### Vision checks (agent eyes)

| Model | Function | Key |
|---|---|---|
| `typesafe/jev-1.14` (OpenRouter Decisions API) | Noul/Choice/Score/Box on images. Probed live: $0.000129/call. Use Box+Noul for drawing checks, Noul for smile/crack checks. | `OPENROUTER_API_KEY` in `freaktown/.env` (Jev-ONLY) |

## Free asset sources

| Source | What | License note |
|---|---|---|
| [api.openverse.org](https://api.openverse.org) | CC image/audio search API (WordPress). Query programmatically, filter by license. | Check per-item license, attribute |
| [pixabay.com](https://pixabay.com) (+ API) | Free photos, video, music, SFX | Pixabay license (no attribution needed, no redistribution as stock) |
| [joecroskey.com/aurora](https://joecroskey.com/aurora) | Aurora/background visuals | Check site terms |
| [transitions.dev](https://transitions.dev) | CSS/view transitions | MIT-ish, check repo |
| Bill Evans Trio — Autumn Leaves | Running motif | Commercial recording — fair-use excerpt only |
| Happy Birthday | Jazz experiment motif | US public domain — record your own |

## Recommended pipeline (from TOOLS-VERDICT.md + studio research)

```
Fish Audio (our 7 voices, word timestamps)
  → claude-motion-design (titles, typography, vortex/probability animation)
  → anatomy (exploded laptop diagram) + pc-anatomy (accurate hardware opening)
  → shaders (backgrounds, transitions, dissolves)
  → lemo-opuscar Exploded Teardown style (cinematic direction)
  → earshot sfx bank + critique (foley + sync QC)
  → Remocn Studio (daily scene-making, live preview)
  → OpenChatCut or kinocut (full-film assembly)
  → Jev eyes (frame QC: $0.0001/shot)
```

Prototype first: one 20-second laptop sequence before building the film.

## Skills in this repo (`essay1/skills/`)

| Skill | Covers | Status |
|---|---|---|
| `laptop-anatomy` | Building exploded figures with anatomy kit | Proven on box |
| `earshot-qc` | Foley + audio critique loop | Proven on box |
| `motion-probe` | Deterministic probe-still workflow | Proven on box |
| `fish-voices` | Our 7 voices + word-timestamp animation driving | Live, listed |

## Disk discipline

Box runs ~93% full. Rules: `--depth 1` every clone, never commit model caches (`tools/earshot/.cache/` is gitignored), trim vendored snippet libs, prefer gitlinks over vendored code.
