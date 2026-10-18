#!/usr/bin/env python3
"""Compile per-function resources for the Fundamentals series.

Writes series/resources/<function>/{CLIPS.md,THEORY.md,DATA.md} for
SETUP, ESCALATE, PUNCH, TAG, CALLBACK, BUTTON.

Sources:
  - funnygraph/data/clips_substrate.jsonl (6,876 clips)
  - funnygraph known_bits + measured punch candidates
  - characters2 SKILL-*.md + research/ + theory/

Run from /root/gcomedy on branch resources-2026-10-18.
"""
from __future__ import annotations
import json, re
from pathlib import Path
from collections import defaultdict

FG = Path("/root/funnygraph")
RES = Path("/root/gcomedy/series/resources")

# ---------- load substrate ----------
clips = [json.loads(l) for l in open(FG / "data/clips_substrate.jsonl")]

# known_bits
bits_by_comic = defaultdict(list)
for f in (FG / "comedians").glob("*/comedian-graph.json"):
    d = json.loads(f.read_text())
    for b in d.get("known_bits", []):
        bits_by_comic[f.parent.name].append(b)

# measured punch candidates
punches = []
for f in (FG / "comedians").glob("*/comedian-graph.json"):
    d = json.loads(f.read_text())
    for s in d.get("sets", []):
        if not s.get("timing_measured"):
            continue
        for pc in s.get("punch_candidates", []):
            punches.append({**pc, "comedian": f.parent.name, "set_id": s.get("id"),
                            "max_pause": s.get("timing_measured", {}).get("max_pause_s")})

# ---------- function definitions ----------
FUNCTIONS = {
    "setup": {
        "title": "THE ART OF THE SETUP",
        "thesis": "A setup is a shared world being built in real time — and the audience builds half of it themselves without knowing.",
        "clip_filter": lambda c: (c.get("duration_s") or 0) >= 90 and (c.get("views") or 0) > 100000,
        "clip_note": "Longer, high-view clips — platform-building material. Prefer observational/storytelling.",
        "title_kws": ["story", "observing", "life", "growing up", "normal", "everyday"],
        "theory_files": [
            "SKILL-setup-punch-tag-two-stories.md (Greg Dean two-stories model)",
            "SKILL-seinfeld-noticing.md (platform construction)",
            "SKILL-joke-writing.md §2 (premise clarity)",
        ],
        "data_anchors": [
            "2,941 setups vs 1,048 punchlines across 335 KT sets (~2.8:1 platform ratio)",
            "Setup predictability r=+0.33 (gcomedy exp3) — stable platform amplifies punch",
            "Baseline inter-word gap ~29ms (rapid, unbroken setup delivery)",
        ],
    },
    "escalate": {
        "title": "ESCALATION — THE CLIMB",
        "thesis": "Escalation is repeated AAB cycles at rising intensity — the path spirals outward without leaving the key.",
        "clip_filter": lambda c: any(k in (c.get("title") or "").lower() for k in ["list", "rules", "worst", "best", "three", "top"]),
        "clip_note": "List/rule-of-three material. Heightening patterns.",
        "title_kws": ["list", "rules", "worst", "best", "three", "top", "escalat"],
        "theory_files": [
            "SKILL-joke-writing.md §3 (escalation/AAB)",
            "SKILL-jeselnik-dark.md (dark escalation)",
            "theory/research/BEST-BIT-THEORY.md (escalation as convergence)",
        ],
        "data_anchors": [
            "Rozin 2006 AAB pattern: minimum 2 iterations before violation",
            "Escalation without direction = intensity-without-target (overshoot)",
        ],
    },
    "punch": {
        "title": "THE PUNCH — HOLD THEN SNAP",
        "thesis": "The punch is the shortest path to a disjoint reading — and it fires in two measured modes: overlap (82%) or gap (18%).",
        "clip_filter": lambda c: (c.get("duration_s") or 0) <= 120 and (c.get("views") or 0) > 50000,
        "clip_note": "Short, high-view clips — punchline-forward material. One-liners and tight bits.",
        "title_kws": ["joke", "funny", "punchline", "one liner", "oned liner"],
        "theory_files": [
            "SKILL-setup-punch-tag-two-stories.md (punch mechanics)",
            "theory/research/UNRELIABLE-NARRATOR.md (punch as reveal)",
            "gcomedy THESIS-timing-is-composition.md (H1/H3)",
        ],
        "data_anchors": [
            "H1: laughs fire at temporal violations (14.1x baseline, p<0.0001)",
            "H3: punch = HOLD (1.4-2x pause) then SNAP (1.48x rate, p=0.045)",
            "Overlap mode 82% (laugh ignites mid-utterance) vs Gap mode 18% (1.9-5.1s hold)",
            "Punch length r=-0.32 with score (shorter punch = funnier)",
        ],
    },
    "tag": {
        "title": "THE TAG — RIDING THE LAUGH",
        "thesis": "A tag extends along the punch direction — each one travels less far, riding the laugh's tail.",
        "clip_filter": lambda c: (c.get("duration_s") or 0) <= 180 and any(k in (c.get("title") or "").lower() for k in ["crowd", "heckle", "work", "improv", "riff", "audience"]),
        "clip_note": "Crowd-work and riff material — tags live in the overlap between comic and room.",
        "title_kws": ["crowd", "heckle", "work", "improv", "riff", "audience"],
        "theory_files": [
            "SKILL-tags-toppers.md (tag mechanics)",
            "SKILL-setup-punch-tag-two-stories.md §tags",
            "theory/SKILL-joke-writing.md (economy of tags)",
        ],
        "data_anchors": [
            "First tag pays ~full, subsequent decay (diminishing returns geometrically enforced)",
            "Tags ride overlap mode almost always (held silence before tag kills it)",
            "Pure repetition (same words) pays zero — no new path, no new pleasure",
        ],
    },
    "callback": {
        "title": "THE CALLBACK — THE RETURN PATH",
        "thesis": "A callback is a return path, transposed — same opposition, new victim, and the room recognizes its own co-creation.",
        "clip_filter": lambda c: any(k in (c.get("title") or "").lower() for k in ["callback", "back", "again", "remember", "earlier"]),
        "clip_note": "Material that references earlier bits. The room's retrieval is the mechanism.",
        "title_kws": ["callback", "back", "again", "remember", "earlier", "earlier"],
        "theory_files": [
            "SKILL-callback.md (callback mechanics)",
            "theory/research/UNRELIABLE-NARRATOR.md (return path)",
            "gcomedy book Ch.3 center-callback prediction",
        ],
        "data_anchors": [
            "First invocation ×1.5 (recognition pleasure), second half, pure repeat zero",
            "Callbacks need a mini-gap for retrieval (Bergson habit-memory + recollective-memory)",
            "Near-center jokes get called back most (SO-ambiguity correlates with callback degree)",
        ],
    },
    "button": {
        "title": "THE BUTTON — RETURN TO CENTER",
        "thesis": "The button closes the trajectory — returning to the persona key, discharging tension, and letting the room's own snap land.",
        "clip_filter": lambda c: any(k in (c.get("title") or "").lower() for k in ["closer", "final", "last", "ending", "goodnight", "outro"]),
        "clip_note": "Closers and final moments. The silence AFTER the button belongs to the room.",
        "title_kws": ["closer", "final", "last", "ending", "goodnight", "outro"],
        "theory_files": [
            "SKILL-joke-writing.md §close",
            "funnygraph STRUCTURES.md Structure 7 (THE CLOSE)",
            "gcomedy book Ch.13 conservation laws",
        ],
        "data_anchors": [
            "Set is closed trajectory iff it ends near where it began (SO, rasa, key) with higher archive mass",
            "Button timing: decelerating cadence, final hold, then release (applause = room's own snap)",
            "Do not step on the button's silence — it belongs to the room",
        ],
    },
}

def clip_line(c):
    vid = c.get("id", "?")
    dur = c.get("duration_s") or 0
    views = c.get("views") or 0
    transcript = "✓ transcript" if c.get("transcript_url") else ""
    timed = "timed" if c.get("words_timed") else ""
    tags = " ".join(filter(None, [transcript, timed]))
    return (f"| {vid} | {c.get('comic','?')[:25]} | {c.get('title','')[:55]} | "
            f"{dur}s | {views:,} | {tags} | https://youtube.com/watch?v={vid} |")

def main():
    for fn, spec in FUNCTIONS.items():
        d = RES / fn
        d.mkdir(parents=True, exist_ok=True)

        # Filter clips
        candidates = [c for c in clips if spec["clip_filter"](c)]
        # Also score by title keyword match
        for c in candidates:
            t = (c.get("title") or "").lower()
            c["_kw_score"] = sum(1 for k in spec["title_kws"] if k in t)
        candidates.sort(key=lambda c: (c.get("_kw_score", 0), c.get("views") or 0), reverse=True)
        top_clips = candidates[:25]

        # CLIPS.md
        lines = [
            f"# {spec['title']} — clip candidates",
            f"\n> Thesis: {spec['thesis']}",
            f"> Filter: {spec['clip_note']}",
            f"> Generated from data/clips_substrate.jsonl ({len(clips)} clips, {len(candidates)} match filter)",
            "",
            "| videoId | comic | title | dur | views | tags | link |",
            "|---|---|---|---|---|---|---|",
        ]
        for c in top_clips:
            lines.append(clip_line(c))
        lines.append("")
        lines.append(f"**{len(candidates)} total candidates** — top 25 shown. Full substrate: `funnygraph/data/clips_substrate.jsonl`.")
        (d / "CLIPS.md").write_text("\n".join(lines) + "\n")

        # THEORY.md
        t_lines = [
            f"# {spec['title']} — theory references",
            "",
            "## characters2",
        ]
        for tf in spec["theory_files"]:
            t_lines.append(f"- `{tf}`")
        t_lines.append("")
        t_lines.append("## gcomedy")
        t_lines.append("- `book/chapters/05-comedic-functions.md` §" + fn.capitalize())
        t_lines.append("- `THESIS-timing-is-composition.md` (timing is composition)")
        if fn == "punch":
            t_lines.append("- `experiments/FINDINGS.md` H1 + H3 (measured punch signature)")
            t_lines.append("- `experiments/exp3-uncertainty-surprisal.md` (comedy inverts music model)")
        t_lines.append("")
        t_lines.append("## Key claims to verify against data")
        for a in spec["data_anchors"]:
            t_lines.append(f"- {a}")
        (d / "THEORY.md").write_text("\n".join(t_lines) + "\n")

        # DATA.md — measured bits and punch candidates relevant to this function
        d_lines = [
            f"# {spec['title']} — measured data",
            "",
        ]
        if fn == "punch" and punches:
            d_lines.append("## Measured punch candidates (funnygraph known_bits)")
            d_lines.append("")
            d_lines.append("| comedian | pause_before_s | fingerprint | set |")
            d_lines.append("|---|---|---|---|")
            for p in sorted(punches, key=lambda x: x.get("pause_before_s") or 0, reverse=True)[:20]:
                fp = (p.get("fingerprint") or "")[:50]
                d_lines.append(f"| {p['comedian']} | {p.get('pause_before_s','')} | {fp} | {p.get('set_id','')[:30]} |")
            d_lines.append("")
        if bits_by_comic:
            d_lines.append("## Comedians with most known_bits (for specimen selection)")
            d_lines.append("")
            ranked = sorted(bits_by_comic.items(), key=lambda x: -len(x[1]))[:15]
            d_lines.append("| comedian | bits | sample title |")
            d_lines.append("|---|---|---|")
            for comic, blist in ranked:
                sample = (blist[0].get("title") or "")[:50]
                d_lines.append(f"| {comic} | {len(blist)} | {sample} |")
            d_lines.append("")
        d_lines.append("## Data discipline")
        d_lines.append("- Every on-screen number measured or sourced")
        d_lines.append("- Human comics only for examples")
        d_lines.append("- Clips = fair-use excerpts ≤15s, transformative commentary, credited")
        d_lines.append("- Wilson before crowns: no 'funniest/best' claims under n≥30")
        (d / "DATA.md").write_text("\n".join(d_lines) + "\n")

        print(f"  {fn}: {len(candidates)} clip candidates, top {len(top_clips)} in CLIPS.md")

    # Top-level resources README
    (RES / "README.md").write_text("""# SERIES RESOURCES — per-function clip/theory/data packs

> Compiled from funnygraph + characters2 + gcomedy experiments.
> Branch: resources-2026-10-18. Merge when ready — does not touch
> series/README.md or series/setup/ (other agent's files).

## Contents

| Function | Dir | Thesis |
|---|---|---|
| SETUP | `setup/` | A setup is a shared world built in real time |
| ESCALATE | `escalate/` | Repeated AAB cycles at rising intensity |
| PUNCH | `punch/` | Shortest path to disjoint reading; overlap vs gap mode |
| TAG | `tag/` | Extends along punch direction; rides the laugh |
| CALLBACK | `callback/` | Return path, transposed |
| BUTTON | `button/` | Closes trajectory; return to persona key |

Each dir has:
- **CLIPS.md** — top candidates from the 6,876-clip substrate
- **THEORY.md** — characters2 + gcomedy references
- **DATA.md** — measured bits, punch candidates, data discipline

## Sources

- `funnygraph/data/clips_substrate.jsonl` (6,876 clips, 2,395 with transcripts)
- `funnygraph/comedians/*/known_bits` (255 bits, 144 measured punch candidates)
- `characters2/theory/SKILL-*.md` + `research/`
- `gcomedy/experiments/` (timing, BV, uncertainty findings)

## How to use

For each video in the series:
1. Read `series/resources/<function>/CLIPS.md` → pick primary + second-specimen clips
2. Read `THEORY.md` → source the claims
3. Read `DATA.md` → on-screen numbers with provenance
4. Cross-reference `series/setup/STRUCTURE.md` for the beat map template
""")

    print(f"\n=== DONE === resources written to {RES}")

if __name__ == "__main__":
    main()
