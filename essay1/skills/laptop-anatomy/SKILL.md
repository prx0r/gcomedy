---
name: laptop-anatomy
description: Build exploded isometric technical figures with the anatomy kit (SVG/WebGL, zero-dep). Use for the laptop deconstruction sequence.
---

# Laptop Anatomy — process notes (proven 2026-10-18)

## What worked
`node build.mjs` in `essay1/tools/anatomy/examples/desk-computer/` produced a 237KB
self-contained HTML with 7 SVGs — full CRT + keyboard + case figure. Zero deps,
node 24, instant. Restore built HTML after trial (`git checkout -- <file>`) to keep
the clone pristine.

## How to build the laptop figure
1. Read `essay1/tools/anatomy/examples/desk-computer/build.mjs` — the pattern:
   plates/case/keys as isometric boxes via `kit/iso-kit.mjs` (`boxCorners`,
   `fitProjection`), lathe parts via `kit/lathe.mjs`.
2. Model the laptop as: base plate → keyboard deck (reuse ROWS key layout) →
   screen assembly (BEZEL + glass like the CRT block) → internals layer
   (battery slab, board, fan circle via `lathe.mjs`).
3. Explode along +z in stages: closed → screen-up → deck-lifted → parts
   separated. Each stage is a projection parameter, not new geometry.
4. Frame it: title card + hint + live readout (anatomy convention — every
   number shown comes from the same small model that moves the parts).
5. Self-check: run `kit/audit.mjs` + zoom every joint (the kit's turn protocol).

## For the film (SEQ 10)
Stage 1 recognition: assembled laptop. Stage 2 deconstruction: explode to
parts. Stage 3 convention: parts fade to labeled wireframes while the word
"laptop" floats above the disassembled object (needs motion-probe or
claude-motion-design for the text layer — anatomy is the diagram, not the film).
