# Tools verdict — trialled on this box, 2026-10-18

Box: no GPU, python 3.11 + playwright + chromium + ffmpeg + node 24 all present.
Disk is tight (~5G free) — sizes matter.

## WORKS — use these

### anatomy → exploded laptop diagrams
**Trial:** `node build.mjs` in `examples/desk-computer` → 237KB self-contained HTML, 7 SVGs. Zero-dep, instant.
**Use for:** the laptop deconstruction (SEQ 10). Build a laptop figure the same way desk-computer builds a CRT + keyboard: plates, case, keys as isometric boxes, then explode along an axis while the word "laptop" floats above. The kit (`iso-kit.mjs`, `lathe.mjs`, audit turn) gives joints + self-check.
**Note:** clone left pristine (restored built HTML after trial).

### pc-anatomy → real hardware structure
**Survey:** Next.js + three.js, ~400 selectable components, all polygons generated in TypeScript, zero runtime assets. Auto-disassemble timeline built in.
**Use for:** accurate mechanical opening of the laptop shot (SEQ 10 stage 1-2: recognition → deconstruction) before the abstract philosophical transformation. Desktop not laptop — adapt the scale tree, reuse the disassembly pattern.
**Cost:** needs `npm install + build` to run; ~10M source only.

### earshot → ears + procedural SFX
**Trial:** `pip install -e .` + `describe` on a synthetic click → "wooden block hit (z+3.1), kalimba (z+3.0), glass ting (z+2.5)". Correct reading, calibrated scores.
**Caveats:** first run downloads ~1GB audio models (CLAP + AST) — now cached at `tools/earshot/.cache/hf` (gitignored, keep on disk). `forge` is slow on CPU; `sfx` bank (201 procedural effects) is the fast path — trial that next.
**Use for:** laptop-sequence foley QC (do clicks land on the animation?), then full-film `critique`.

### claude-motion-design → deterministic motion graphics
**Trial:** wrote a 6s `seek(t)` test film (title + progress bar in Funnier skin colors), probe-rendered 3 stills at 1280×720 via Playwright. Path proven end to end.
**Use for:** title cards, kinetic typography, the probability-collapse + vortex animations. Deterministic = fix one scene without touching the rest. Beat-sync by construction.

## BROKEN HERE — do not use

### manim / manim-skill / motion-canvas skills
**Trial:** `manim -qm` hangs on this box (even `--dry_run`, >110s). Broken runtime — do not build on it.
**Consequence:** manimgx (Rust/wgpu build, 138M source) not attempted — no working Manim baseline to compare, disk too tight for toolchain gamble. Revisit on roomier iron.

## SURVEY-ONLY — need a driver or heavier iron

| Tool | Why parked |
|---|---|
| lemo-opuscar (198M) | 51 styles tuned for Claude Opus 5.5; needs a Claude Code session to direct |
| mortiflix-oss (24M) | Staged review workflow (brief→script→frames→animatic→final); needs Claude login + reviewer (you) |
| montage / gomotion | Remotion+Next.js; need `npm install` + a directing session |
| kinocut (28M) | MCP server; needs a Claude Code host to call it |
| cut-as-code (158M) | Editing skills; useful at edit time, trimmed 350M vendored snippet libs |
| blender-agent / mcp-blender-agent | Skipped — no Blender on box |
| ComfyUI / UniForge / MMAudio / FoleyCrafter | Skipped — need RTX GPU |
| davinci-resolve-mcp | Skipped per owner — no Resolve |

## Recommended stack for the film

```
Script + narration (source of truth)
  → anatomy (exploded laptop diagram)
  → claude-motion-design (titles, typography, vortex/probability animation)
  → pc-anatomy (accurate hardware opening)
  → earshot sfx bank + describe/match (foley + sync QC)
  → kinocut or ffmpeg directly (assembly, captions, grade)
```

Prototype first: one 20-second laptop sequence (anatomy diagram + motion-design titles + earshot foley). Establishes the visual language before the film.
