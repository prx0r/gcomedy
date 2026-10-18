#!/usr/bin/env python3
"""Compile resources for ALL series topics (original 9 + new building blocks).

For each topic: CLIPS.md, CRAFT_TALK.md, DATA.md, THEORY.md
Sources: substrate clips, characters2 transcripts + theory files, funnygraph data.
"""
from __future__ import annotations
import json, re, subprocess, sys, time
from pathlib import Path
from collections import defaultdict

FG = Path("/root/funnygraph")
RES = Path("/root/gcomedy/series/resources")
C2 = Path("/root/characters2/theory")

# Load substrate once
clips = [json.loads(l) for l in open(FG / "data" / "clips_substrate.jsonl")]

# Load measured data
punches = []
bits_by_comic = defaultdict(list)
for f in (FG / "comedians").glob("*/comedian-graph.json"):
    d = json.loads(f.read_text())
    for b in d.get("known_bits", []):
        bits_by_comic[f.parent.name].append(b)
    for s in d.get("sets", []):
        if s.get("timing_measured"):
            for pc in s.get("punch_candidates", []):
                punches.append({**pc, "comedian": f.parent.name})

# Topic definitions: {topic: {title, thesis, clip_kws, craft_pats, theory_refs, data_notes, yt_searches}}
TOPICS = {
    # === ORIGINAL 9 ===
    "setup": {
        "title": "SETUP — THE PLATFORM", "fn": "setup",
        "thesis": "The setup is a shared world — declared fast, attitude attached, stable enough to violate.",
        "clip_kws": ["premise","setup","writing","process","explains","how i"],
        "craft_pats": [r"premise", r"set.?up", r"audience.*(understand|get)", r"platform"],
        "theory": ["SKILL-setup-punch-tag-two-stories.md","SKILL-seinfeld-noticing.md"],
        "data": ["2.8:1 setup:punch ratio (335 KT sets)","Setup predictability r=+0.33","Rock premise rule"],
        "yt": ["comedian explains premise setup joke writing","seinfeld how jokes work premise"],
    },
    "premise": {
        "title": "PREMISE — THE WORLD", "fn": "premise",
        "thesis": "The premise is the shared world — declared fast, attitude attached, stable enough to violate.",
        "clip_kws": ["premise","setup","world","declares","attitude"],
        "craft_pats": [r"premise", r"the thing is", r"world.*build", r"attitude"],
        "theory": ["SKILL-seinfeld-noticing.md","THE-LINE.md"],
        "data": ["Rock rule: 9/10 failing bits fail on premise","Gervais: attitude not topic"],
        "yt": ["chris rock premise audience understands","gervais comedy attitude premise"],
    },
    "escalate": {
        "title": "ESCALATION — THE CLIMB", "fn": "escalation",
        "thesis": "Escalation is repeated AAB cycles at rising intensity — the path spirals outward without leaving the key.",
        "clip_kws": ["list","rules","worst","best","three","top","escalat"],
        "craft_pats": [r"escalat", r"heighten", r"rule of three", r"build.*joke"],
        "theory": ["SKILL-joke-writing.md §3","FORMATS-joke-types.md #3 riff"],
        "data": ["Rozin AAB: 2 iterations before violation","1,104 rule_of_three examples in corpus"],
        "yt": ["comedian explains escalation rule of three","norm macdonald building a joke"],
    },
    "punch": {
        "title": "PUNCH — THE SNAP", "fn": "punch",
        "thesis": "The punch is the shortest path to a disjoint reading — hold then snap, two measured modes.",
        "clip_kws": ["joke","funny","punchline","timing","delivery"],
        "craft_pats": [r"punch.?line", r"timing", r"the punch", r"delivery"],
        "theory": ["SKILL-setup-punch-tag-two-stories.md","gcomedy THESIS-timing-is-composition"],
        "data": ["H1: laughs at temporal violations (14x)","H3: HOLD then SNAP (1.48x)","punch length r=-0.32"],
        "yt": ["comedian explains punchline timing","seinfeld count syllables"],
    },
    "tag": {
        "title": "TAG — RIDING THE LAUGH", "fn": "tags",
        "thesis": "A tag extends along the punch direction — each one travels less far, riding the laugh's tail.",
        "clip_kws": ["crowd","heckle","work","improv","riff"],
        "craft_pats": [r"\btag\b", r"topper", r"second.*laugh", r"extend"],
        "theory": ["SKILL-tags-toppers.md","FORMATS-joke-types.md #9 tag ladder"],
        "data": ["First tag full, second half (diminishing returns)","Tags ride overlap mode"],
        "yt": ["comedian explains tags toppers","extending a joke after punchline"],
    },
    "callback": {
        "title": "CALLBACK — THE RETURN", "fn": "callbacks",
        "thesis": "A callback is a return path, transposed — same opposition, new victim.",
        "clip_kws": ["callback","back","again","remember"],
        "craft_pats": [r"callback", r"call.?back", r"plant.*payoff", r"earlier"],
        "theory": ["SKILL-callback.md","FORMATS-joke-types.md #11 callback"],
        "data": ["First invocation x1.5, second half, pure repeat zero","Needs mini-gap for retrieval"],
        "yt": ["comedian explains callbacks comedy","plant and payoff comedy writing"],
    },
    "button": {
        "title": "BUTTON — RETURN TO CENTER", "fn": "button",
        "thesis": "The button closes the trajectory — returning to the persona key, discharging tension.",
        "clip_kws": ["closer","ending","finale","outro","goodnight"],
        "craft_pats": [r"closer", r"ending.*set", r"\bbutton\b", r"that.s my time"],
        "theory": ["SKILL-joke-writing.md §close","funnygraph STRUCTURES.md Structure 7"],
        "data": ["Closed trajectory: ends near where it began","Silence AFTER belongs to the room"],
        "yt": ["comedian explains closer ending a set","how to end a comedy special"],
    },
    "pause": {
        "title": "PAUSE — THE HOLD", "fn": "pause",
        "thesis": "The pause holds accrued weight — 1.4-2x baseline, then snap. The silence IS the joke.",
        "clip_kws": ["pause","silence","timing","hold","moment"],
        "craft_pats": [r"pause", r"silence", r"hold.*beat", r"timing"],
        "theory": ["Attardo & Pickering 2011","DPV framework","gcomedy H1/H3 experiments"],
        "data": ["31s Lee hold","8.16s Louis confession","1.5-3.5s window for big swings","H1: 14x baseline"],
        "yt": ["comedian comedy timing pause silence","louis ck pause timing punchline"],
    },
    "joke": {
        "title": "JOKE — WHAT IS A JOKE?", "fn": "joke",
        "thesis": "A joke is an atomic unit: one setup, one punch, one laugh point. The series opener.",
        "clip_kws": ["one liner","one-liner","joke","hedberg"],
        "craft_pats": [r"one.?liner", r"anatomy.*joke", r"setup.*punch"],
        "theory": ["series/joke/STRUCTURE.md","SKILL-setup-punch-tag-two-stories.md"],
        "data": ["One-liner: setup+punch in single sentence","Bit = premise + jokes + tags","Chunk = bits on topic"],
        "yt": ["anatomy of a joke setup punchline","mitch hedberg one liner"],
    },

    # === TIER 1: VIOLATE, OPERATORS, FORMATS, ANTI-SLOP ===
    "violate": {
        "title": "HOW TO VIOLATE", "fn": "punch",
        "thesis": "Violation is the engine — but it must be benign simultaneously. The safety math makes it funny.",
        "clip_kws": ["dark","edgy","offensive","violation","wrong"],
        "craft_pats": [r"wrong", r"offensive", r"dark", r"edgy", r"cross.*line", r"shouldn.t"],
        "theory": ["THE-LINE.md","McGraw & Warren BV 2010","jokegate/edge.py","jokegate/edgy.py"],
        "data": ["BV r=+0.49 (strongest single predictor)","33 realm exemplars calibrated","Haidt 6-foundation scoring"],
        "yt": ["comedian explains edgy dark comedy","chappelle how he writes dark jokes","jeselnik dark comedy technique"],
    },
    "operators": {
        "title": "THE OPERATOR TOOLKIT", "fn": "punch",
        "thesis": "15 operators are the atomic moves of comedy — each one is a way to bend reality.",
        "clip_kws": ["technique","trick","move","how he does","mechanism"],
        "craft_pats": [r"technique", r"trick", r"move", r"mechanism", r"the way.*works"],
        "theory": ["audition/generate.py OPERATORS","technique-index/mapping.json","GTVH LM_OPTIONS"],
        "data": ["15 operators: rigidify, status_invert, split_knowledge...","KT lift data per operator","12 GTVH LMs"],
        "yt": ["comedian explains comedy technique mechanism","norm macdonald how he does it"],
    },
    "formats": {
        "title": "THE JOKE LAB — FORMATS", "fn": "joke",
        "thesis": "14 joke formats, each with craft rules, anti-patterns, and personality fit.",
        "clip_kws": ["format","style","type","one liner","story","riff","roast"],
        "craft_pats": [r"format", r"style", r"type of joke", r"one.?liner", r"story.*joke"],
        "theory": ["FORMATS-joke-types.md","Corley 13 structures","SKILL-joke-writing.md"],
        "data": ["14 formats catalogued","34k bits with format labels","Format affinity is discovered per personality"],
        "yt": ["types of comedy jokes explained","one liner vs story comedy","comedy formats explained"],
    },
    "anti-slop": {
        "title": "WHY AI JOKES ARE BAD", "fn": "joke",
        "thesis": "The 5 AI tells — definitional copula, three-lists, jagged rhythm, clever pullback, hedges.",
        "clip_kws": ["ai joke","chatgpt comedy","ai written","generated"],
        "craft_pats": [r"ai.*(joke|comedy|write)", r"definitional", r"copula", r"three.*list"],
        "theory": ["SKILL-joke-writing.md PART 1","jokegate/slop.py","human_gate.py"],
        "data": ["NoSlop AUROC 0.84","5 AI tells ranked by frequency","Rhythm gate: 3% human fail vs 94% AI fail"],
        "yt": ["ai writes a joke chatgpt","ai comedy fails","why ai jokes are bad"],
    },

    # === TIER 2: TIMING, DELIVERY, PERSONA, JOKE-WRITING ===
    "timing-doctrine": {
        "title": "TIMING DOCTRINES", "fn": "pause",
        "thesis": "Six timing doctrines — big_stop, never_stop, surgical, sermon, percussive, reload.",
        "clip_kws": ["timing","pace","speed","rhythm","delivery"],
        "craft_pats": [r"timing", r"pace", r"speed", r"rhythm", r"delivery"],
        "theory": ["AXES.md A3 timing doctrine","gcomedy THESIS-timing-is-composition","TAMS 2026"],
        "data": ["6 doctrines mapped to comedians","Norm=never_stop(192wpm)","Lee=sermon(123wpm)","Louis=both modes"],
        "yt": ["norm macdonald delivery timing style","george carlin rhythm delivery","comedy timing doctrine"],
    },
    "delivery-shape": {
        "title": "DELIVERY SHAPES", "fn": "pause",
        "thesis": "Hold-time determines delivery shape — one_liner, riff, story, character. Different shape = different person.",
        "clip_kws": ["delivery","voice","style","perform","stage"],
        "craft_pats": [r"delivery", r"voice", r"style", r"perform", r"stage presence"],
        "theory": ["SKILL-joke-writing.md PART 5","valence-inversion engine","characters2 prosody/"],
        "data": ["hold-time → shape mapping","valence inversion: content/delivery OPPOSITE","wpm spectrum 192-117"],
        "yt": ["comedian delivery style voice","comedy stage presence technique","norm macdonald vs louis ck delivery"],
    },
    "persona": {
        "title": "PERSONA CONSTRUCTION", "fn": "setup",
        "thesis": "The persona is a stage character — built from real traits, exaggerated, with a specific engine.",
        "clip_kws": ["persona","character","stage","persona","identity"],
        "craft_pats": [r"persona", r"character", r"stage persona", r"identity", r"who.*are.*on stage"],
        "theory": ["SPEC-graph-v2.md","AXES.md 9-axis schema","VALIDATION.md","ACASTER-GOLD.md"],
        "data": ["deal, archetype, contradictions, misinterpretation_rule","9 axes incl. status, exit, awareness","Stage persona ≠ person (literature-validated)"],
        "yt": ["comedian explains stage persona character","how comedians build persona","acaster persona technique"],
    },
    "joke-writing": {
        "title": "THE JOKE WRITING PROCESS", "fn": "joke",
        "thesis": "How comedians actually write — from noticing to premise to punch to tags.",
        "clip_kws": ["writing","process","how i write","jokes","writing"],
        "craft_pats": [r"i write", r"my process", r"how i.*joke", r"writing.*joke", r"the way.*write"],
        "theory": ["SKILL-joke-writing.md full","SKILL-seinfeld.md","SKILL-normand.md","SKILL-normand-page-to-stage-live.md"],
        "data": ["Seinfeld: syllable-shaving, legal pad","Normand: bandit over angles","335 KT sets analyzed"],
        "yt": ["seinfeld how to write a joke","mark normand joke writing process","comedian writing process interview"],
    },

    # === TIER 3: ESOTERIC ===
    "where-jokes-come-from": {
        "title": "WHERE DO JOKES COME FROM?", "fn": "joke",
        "thesis": "The inverted possibility space — the joke lives where reality CAN'T go. What's impossible defines what's funny.",
        "clip_kws": ["origin","where jokes","creativity","inspiration","subconscious"],
        "craft_pats": [r"where.*joke.*come", r"inspiration", r"creativity", r"subconscious", r"origin"],
        "theory": ["INVERTED-POSSIBILITY-SPACE.md","gcomedy camatkara/sphota","ACASTER-GOLD.md subconscious bleed"],
        "data": ["Acaster: jokes find you (subconscious bleed)","Gap as co-creation (Iser blanks)","Sphoṭa: punch re-weights the past"],
        "yt": ["where do jokes come from comedian","comedy creativity inspiration","norm macdonald where jokes come from"],
    },
    "minimal-pairs": {
        "title": "THE MINIMAL PAIR", "fn": "punch",
        "thesis": "One word changes everything — the minimal edit that flips funniness.",
        "clip_kws": ["edit","word","change","rewrite","minimal"],
        "craft_pats": [r"one word", r"edit", r"change.*word", r"rewrite", r"minimal"],
        "theory": ["MINIMAL-PAIRS.md","minimal-pairs.json","measure_pairs.py"],
        "data": ["12 same-joke 1-word edits rated","11/12 gate-measured","4 new mechanisms found"],
        "yt": ["comedian editing jokes word choice","one word changes a joke","comedy rewriting process"],
    },
    "rasa": {
        "title": "THE RASA MAP", "fn": "joke",
        "thesis": "Nine aesthetic flavors — comedy is hasya inflected by the other eight.",
        "clip_kws": ["rasa","flavor","emotion","feeling","tone"],
        "craft_pats": [r"rasa", r"flavor", r"emotion", r"feeling", r"tone"],
        "theory": ["gcomedy library/rasa/","RASA-FRAMEWORK-DESIGN.md","9 rasas table"],
        "data": ["Roast = hasya+raudra","Absurdism = hasya+adbhuta","Deadpan = hasya+shanta"],
        "yt": ["rasa theory comedy","indian aesthetics humor","comedy emotional flavors"],
    },
    "the-line": {
        "title": "HOW TO STEP OVER THE LINE", "fn": "punch",
        "thesis": "The line is where funny becomes offensive. Crossing it requires calibration.",
        "clip_kws": ["line","cross","offensive","edgy","too far"],
        "craft_pats": [r"cross.*line", r"too far", r"offensive", r"edgy", r"line"],
        "theory": ["THE-LINE.md","jokegate/edge.py","jokegate/edgy.py","THE-LINE crossing formula"],
        "data": ["33 realm exemplars","distance-1.0 carry implemented","Haidt foundations scoring"],
        "yt": ["comedian explains crossing the line comedy","edgy comedy how far is too far","chappelle line comedy"],
    },
    "sincerity": {
        "title": "THE WINK VETO", "fn": "setup",
        "thesis": "The character never knows it's comedy. The wink destroys the machine.",
        "clip_kws": ["sincere","wink","character","authentic","genuine"],
        "craft_pats": [r"sincer", r"wink", r"authentic", r"genuine", r"character.*knows"],
        "theory": ["SKILL-joke-writing.md PART 6 embodiment","sincerity doctrine","hasya rasa"],
        "data": ["Character never breaks 4th wall","Audience knows it's a show; character doesn't","This distance enables hasya"],
        "yt": ["comedian explains character authenticity","comedy sincerity vs irony","norm macdonald sincerity"],
    },
    "edgy-gate": {
        "title": "THE SAFETY MATH", "fn": "punch",
        "thesis": "Benign violation is safety math — wrong enough to surprise, safe enough to laugh.",
        "clip_kws": ["safety","math","violation","benign","wrong"],
        "craft_pats": [r"safety", r"math", r"violation", r"benign", r"wrong.*safe"],
        "theory": ["jokegate/edgy.py","McGraw & Warren","foundations.py Haidt scoring"],
        "data": ["BV strongest predictor r=+0.49","3 conditions: alt norm, weak commitment, distance","Both appraisals must be SIMULTANEOUS"],
        "yt": ["benign violation theory comedy","what makes something funny wrong safe","comedy safety math"],
    },
    "feel-judge": {
        "title": "WHAT FEELS FUNNY", "fn": "joke",
        "thesis": "The feel gate — 5-dimension rubric + human override. Model scores propose, humans dispose.",
        "clip_kws": ["feel","funny","rubric","judge","evaluate"],
        "craft_pats": [r"feel.*funny", r"what.*funny", r"rubric", r"evaluat"],
        "theory": ["jokegate/feel.py","5-dim rubric","human override protocol"],
        "data": ["LLM 5-dim rubric","human always wins","Wilson before crowns"],
        "yt": ["what makes something funny psychology","comedy evaluation rubric","how comedians judge jokes"],
    },
    "status": {
        "title": "STATUS — THE INVISIBLE HIERARCHY", "fn": "setup",
        "thesis": "Every interaction has a status hierarchy. Comedy plays with it — inverts it, oscillates it.",
        "clip_kws": ["status","hierarchy","confidence","superiority","inferior"],
        "craft_pats": [r"status", r"hierarchy", r"confidence", r"superiority", r"better.*than"],
        "theory": ["status_invert operator","status theory of humor","AXES.md status capital"],
        "data": ["Rock=above room","Louis=below room","Lock=oscillating","status_invert operator lift"],
        "yt": ["comedian explains status comedy","chappelle status comedy","louis ck self deprecation status"],
    },
    "target": {
        "title": "TARGET — WHO YOU ATTACK", "fn": "punch",
        "thesis": "Every joke has a target: self, powerful, species, or victim. The target determines the safety math.",
        "clip_kws": ["target","attack","who","victim","self"],
        "craft_pats": [r"target", r"attack", r"victim", r"myself", r"self.*deprecat"],
        "theory": ["jokegate TARGETS","THE-LINE.md","self-target bonus in edge scoring"],
        "data": ["4 target types: self, powerful, species, victim","Self-target = safest","Powerful target = needs distance"],
        "yt": ["comedian explains who to joke about","self deprecation comedy technique","roast comedy target"],
    },
    "frame": {
        "title": "FRAME — REAL VS FICTIONAL", "fn": "setup",
        "thesis": "The reality frame determines what the audience believes. Fiction outperforms truth when the frame is bought.",
        "clip_kws": ["frame","real","fiction","believe","true"],
        "craft_pats": [r"frame", r"real.*vs.*fiction", r"believe", r"true.*story", r"fiction"],
        "theory": ["UNRELIABLE-NARRATOR.md","sincerity doctrine","Acaster red-dress proof"],
        "data": ["Acaster: true story rejected, fiction bought","Belief irrelevant; co-signing is everything","5 unreliable narrator variants"],
        "yt": ["acaster fictional premises comedy","unreliable narrator standup","comedy frame real vs fiction"],
    },
    "misdirection": {
        "title": "MISDIRECTION — THE GARDEN PATH", "fn": "punch",
        "thesis": "The audience is led toward expectation X, then delivered Y. The Y that wasn't in their probability distribution.",
        "clip_kws": ["misdirection","garden path","surprise","twist","expect"],
        "craft_pats": [r"misdirect", r"garden.*path", r"surprise", r"twist", r"expect.*but"],
        "theory": ["garden_path LM","DPV framework","the sixth option (Locke)"],
        "data": ["garden_path LM","DPV: punch violates temporal+semantic simultaneously","Locke: sixth option out of five"],
        "yt": ["comedian misdirection technique","garden path comedy","norm macdonald misdirection"],
    },
    "confession": {
        "title": "CONFESSION — THE HONESTY ENGINE", "fn": "punch",
        "thesis": "The confession machine — say the quiet part out loud with such commitment the room confesses back.",
        "clip_kws": ["confession","honest","truth","vulnerable","real"],
        "craft_pats": [r"confess", r"honest", r"truth", r"vulnerab", r"real.*self"],
        "theory": ["expose_self_blindness operator","Louis thesis","BV simultaneous condition"],
        "data": ["Louis 8.16s confession hold","expose_self_blindness operator","Room confesses back (recognition not approval)"],
        "yt": ["louis ck confession comedy technique","honest comedy vulnerability","comedy confession engine"],
    },
    "rule": {
        "title": "RULE — INTERNAL LOGIC", "fn": "setup",
        "thesis": "The absurd premise followed sincerely — the rule of the bit is real inside the bit.",
        "clip_kws": ["rule","logic","absurd","sincere","commitment"],
        "craft_pats": [r"rule", r"logic", r"absurd", r"sincere", r"commit.*to.*bit"],
        "theory": ["rigidify operator","bogus_logic","Locke grounded-absurd framework"],
        "data": ["rigidify operator","Locke: grounded person + absurd person","Acaster: legal case out of bad idea"],
        "yt": ["absurdist comedy technique sincere","comedy internal logic rule","acaster absurd premise commitment"],
    },
    "voice": {
        "title": "VOICE — THE PERSONA'S SOUND", "fn": "setup",
        "thesis": "The voice is the persona's sonic signature — pace, pitch, rhythm, vocabulary.",
        "clip_kws": ["voice","sound","pitch","accent","vocabulary"],
        "craft_pats": [r"voice", r"sound", r"pitch", r"accent", r"vocabulary"],
        "theory": ["delivery_archetype","modulator_range","Carlin rhythm analysis","Seinfeld syllable-shaving"],
        "data": ["Carlin: rhythm IS the joke","Seinfeld: count syllables, songwriting","6 timing doctrines = 6 voice types"],
        "yt": ["george carlin rhythm delivery voice","seinfeld syllable counting","comedian voice technique"],
    },
    "gtvh": {
        "title": "THE LOGIC MECHANISMS", "fn": "punch",
        "thesis": "12 logical mechanisms — how the punch re-frames the setup.",
        "clip_kws": ["logic","mechanism","reframe","switch","turn"],
        "craft_pats": [r"logic.*mechanism", r"reframe", r"switch", r"the turn"],
        "theory": ["gtvh.py LM_OPTIONS","technique-index/mapping.json","Attardo GTVH"],
        "data": ["12 LMs: garden_path, juxtaposition, role_reversal...","Mapped to 15 operators","25 theories bridged"],
        "yt": ["gtvh humor theory logic mechanism","comedy reframe technique","incongruity resolution comedy"],
    },
    "aab": {
        "title": "THE AAB ENGINE", "fn": "escalate",
        "thesis": "Two similar events, then a third that breaks the pattern. The oldest engine in comedy.",
        "clip_kws": ["pattern","three","repeat","break","aab"],
        "craft_pats": [r"pattern", r"repeat.*then", r"two.*then.*third", r"aab"],
        "theory": ["Rozin 2006 AAB paper","FORMATS-joke-types.md #4 rule-of-three","Exp3 setup predictability"],
        "data": ["Rozin: minimum 2 iterations before violation","1,104 rule_of_three examples","Setup predictability r=+0.33"],
        "yt": ["rule of three comedy explained","aab pattern humor","comedy pattern break"],
    },
    "inverted-space": {
        "title": "THE INVERTED SPACE", "fn": "joke",
        "thesis": "The joke lives where reality CAN'T go. What's impossible defines what's funny.",
        "clip_kws": ["impossible","can't","inverted","space","reality"],
        "craft_pats": [r"impossible", r"can.t happen", r"inverted", r"reality.*break"],
        "theory": ["INVERTED-POSSIBILITY-SPACE.md","orbifolds of the absurd","center-callback"],
        "data": ["Joke space wraps on itself","Two distant ideas = same point via rotation","Callback = literal orbifold move"],
        "yt": ["comedy impossible reality inverted","absurdist comedy space","surreal comedy technique"],
    },
    "rhythm-gate": {
        "title": "THE RHYTHM GATE", "fn": "pause",
        "thesis": "Sentence structure is rhythm. AI fails the rhythm gate 94% of the time.",
        "clip_kws": ["rhythm","sentence","structure","flow","cadence"],
        "craft_pats": [r"rhythm", r"sentence.*structure", r"flow", r"cadence"],
        "theory": ["RHYTHM-FINDINGS.md","human_gate.py rhythm check","sentence structure vs human band"],
        "data": ["Human: 12.9w/sent","AI: 5.4w/sent","FAIL: mean<7w AND 4+ short in a row","3% human fail vs 94% AI fail"],
        "yt": ["comedy rhythm sentence structure","comedian cadence flow","norm macdonald rhythm delivery"],
    },
}

def clip_line(c):
    vid = c.get("id", "?")
    dur = c.get("duration_s") or 0
    views = c.get("views") or 0
    tags = "✓ transcript" if c.get("transcript_url") else ""
    return (f"| {vid} | {c.get('comic','?')[:20]} | {c.get('title','')[:50]} | "
            f"{dur}s | {views:,} | {tags} | https://youtube.com/watch?v={vid} |")

def main():
    for topic, spec in TOPICS.items():
        d = RES / topic
        d.mkdir(exist_ok=True)

        # CLIPS.md from substrate
        candidates = [c for c in clips if any(k in (c.get('title') or '').lower() for k in spec['clip_kws'])]
        for c in candidates:
            t = (c.get('title') or '').lower()
            c['_score'] = sum(1 for k in spec['clip_kws'] if k in t)
        candidates.sort(key=lambda c: (c.get('_score',0), c.get('views') or 0), reverse=True)

        lines = [f"# {spec['title']} — clip candidates", "",
                 f"> Thesis: {spec['thesis']}", "",
                 "| videoId | comic | title | dur | views | tags | link |",
                 "|---|---|---|---|---|---|---|"]
        for c in candidates[:20]:
            lines.append(clip_line(c))
        lines.append(f"\n**{len(candidates)} total** — top 20 shown.")
        (d / "CLIPS.md").write_text("\n".join(lines))

        # CRAFT_TALK.md from characters2 transcripts
        passages = []
        for fn in sorted(C2.glob("transcripts/*.txt")):
            try:
                text = fn.read_text(errors='ignore')
            except:
                continue
            if len(text) < 1000:
                continue
            comedian = fn.stem.split('-transcript')[0].split('-full')[0]
            sentences = re.split(r'(?<=[.!?])\s+', text)
            for sent in sentences:
                s = sent.lower()
                if any(re.search(p, s) for p in spec['craft_pats']) and len(sent) > 50:
                    if any(m in s for m in ['i write','my process','the way i','you have to','the key is','jokes are','comedy is','a joke is','what makes']):
                        passages.append({'comedian': comedian, 'excerpt': sent[:300]})
                        if len(passages) >= 15:
                            break
            if len(passages) >= 15:
                break

        ct_lines = [f"# {spec['title']} — craft talk", ""]
        by_comic = defaultdict(list)
        for p in passages:
            by_comic[p['comedian']].append(p)
        for comic in sorted(by_comic):
            ct_lines.append(f"## {comic.replace('-',' ').title()}")
            ct_lines.append("")
            for p in by_comic[comic][:2]:
                ct_lines.append(f"> \"{p['excerpt'][:280]}\"")
                ct_lines.append("")
        (d / "CRAFT_TALK.md").write_text("\n".join(ct_lines))

        # DATA.md
        data_lines = [f"# {spec['title']} — measured data", ""]
        for note in spec['data']:
            data_lines.append(f"- {note}")
        # Add extreme examples if relevant
        if topic in ['pause','timing-doctrine','delivery-shape']:
            data_lines.extend(["", "## Extreme examples",
                "| Value | Comedian | Video |",
                "|---|---|---|",
                "| 31.24s pause | Stewart Lee | [OXo5_ihFkA0](https://youtube.com/watch?v=OXo5_ihFkA0) |",
                "| 192 wpm | Norm Macdonald | [RA0UjWA9iWU](https://youtube.com/watch?v=RA0UjWA9iWU) |",
                "| 8.16s hold | Louis CK | [auHzTfeF64Y](https://youtube.com/watch?v=auHzTfeF64Y) |",
            ])
        (d / "DATA.md").write_text("\n".join(data_lines))

        # THEORY.md
        t_lines = [f"# {spec['title']} — theory references", ""]
        for ref in spec['theory']:
            t_lines.append(f"- `{ref}`")
        t_lines.append("")
        t_lines.append("## gcomedy")
        t_lines.append("- THESIS-timing-is-composition.md")
        t_lines.append("- experiments/FINDINGS.md")
        (d / "THEORY.md").write_text("\n".join(t_lines))

        print(f"  {topic:25s} clips={len(candidates):4d} craft={len(passages):2d}")

    print(f"\n=== DONE: {len(TOPICS)} topics compiled ===")

if __name__ == "__main__":
    main()
