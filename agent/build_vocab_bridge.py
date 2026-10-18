#!/usr/bin/env python3
"""UNIFIED VOCABULARY BRIDGE — Attardo concepts ↔ operators ↔ GTVH LMs ↔ funnygraph.

The canonical mapping across all four vocabularies. Extends
characters2/technique-index/mapping.json to include Attardo graph node IDs.

Source of truth for: agent navigation, series resources, video overlays.
"""
import json
from pathlib import Path

BRIDGE = {
    "schema": "pogtown.unified-vocab.v1",
    "note": "Attardo graph node ↔ characters2 operator ↔ GTVH LM ↔ funnygraph field. Every vocabulary used in the system.",
    "vocabularies": {
        "attardo": "gcomedy/library/comedy/attardo-graph/graph.json (76 nodes)",
        "operators": "characters2/audition/generate.py OPERATORS (15)",
        "gtvh_lm": "characters2/audition/gtvh.py LM_OPTIONS (12)",
        "funnygraph": "funnygraph/comedians/*/operator_priors",
        "series_topics": "gcomedy/series/resources/ (41 topics)",
    },
    "mappings": {
        # === PUNCH MECHANISMS ===
        "punchline": {
            "attardo_nodes": ["punchline", "KR-SO", "KR-LM", "isotopy-disjunction-model"],
            "operators": ["garden_path", "literalize", "double_interpret"],
            "gtvh_lm": ["garden_path", "juxtaposition"],
            "funnygraph_fields": ["known_bits", "punch_candidates"],
            "series_topics": ["punch", "misdirection"],
            "measured_data": "H1: laughs fire at temporal violations (14x). H3: HOLD then SNAP (1.48x).",
        },
        "incongruity": {
            "attardo_nodes": ["incongruity", "incongruity-theory", "script-opposition-SSTH"],
            "operators": ["double_interpret", "garden_path", "literalize"],
            "gtvh_lm": ["garden_path", "juxtaposition", "false_analogy"],
            "funnygraph_fields": ["operator_priors", "humor_type"],
            "series_topics": ["punch", "misdirection", "gtvh"],
            "measured_data": "Setup predictability r=+0.33 (Exp 3). Benign violation r=+0.49.",
        },
        "script-opposition": {
            "attardo_nodes": ["script-opposition-SSTH", "KR-SO", "script-overlap", "script-opposition-opposition"],
            "operators": ["double_interpret", "split_knowledge", "mistake_identity"],
            "gtvh_lm": ["garden_path", "role_reversal", "perspective_shift"],
            "funnygraph_fields": ["operator_priors.double_interpret"],
            "series_topics": ["gtvh", "punch", "misdirection"],
            "measured_data": "",
        },
        "garden-path": {
            "attardo_nodes": ["garden_path" in BRIDGE if False else "isotopy-disjunction-model", "linear-organization"],
            "operators": ["garden_path"],
            "gtvh_lm": ["garden_path"],
            "funnygraph_fields": ["operator_priors.garden_path"],
            "series_topics": ["misdirection", "punch", "setup"],
            "measured_data": "Golden-ticket signature: escalation + garden_path (10/10 sampled GT sets)",
        },
        "literalize": {
            "attardo_nodes": ["saussurean-sign", "ambiguity-taxonomy"],
            "operators": ["literalize"],
            "gtvh_lm": ["literalize", "exaggeration"],
            "funnygraph_fields": ["operator_priors.literalize"],
            "series_topics": ["operators", "punch"],
            "measured_data": "Louis technique mix: literalize 24% (highest single technique)",
        },
        # === STATUS & TARGET ===
        "status-invert": {
            "attardo_nodes": ["aggression-theory", "KR-TA", "power-solidarity", "politeness-theory"],
            "operators": ["status_invert", "character_violation"],
            "gtvh_lm": ["role_reversal"],
            "funnygraph_fields": ["operator_priors.status_invert", "status_model"],
            "series_topics": ["status", "target", "violate"],
            "measured_data": "Rock=above room, Louis=below, Lock=oscillating",
        },
        "target": {
            "attardo_nodes": ["KR-TA", "power-solidarity", "politeness-theory"],
            "operators": ["status_invert", "character_violation"],
            "gtvh_lm": [],
            "funnygraph_fields": [],
            "series_topics": ["target", "the-line", "violate"],
            "measured_data": "4 target types: self/powerful/species/victim. Self=safest.",
        },
        "benign-violation": {
            "attardo_nodes": ["incongruity", "resolution", "politeness-theory", "context-humor"],
            "operators": ["character_violation", "status_invert"],
            "gtvh_lm": [],
            "funnygraph_fields": ["operator_priors.character_violation"],
            "series_topics": ["violate", "edgy-gate", "the-line"],
            "measured_data": "BV r=+0.49 (strongest single predictor). 3 conditions: alt norm, weak commitment, distance.",
        },
        # === TIMING & PERFORMANCE ===
        "timing": {
            "attardo_nodes": ["timing-performance", "KR-NS", "release-theory"],
            "operators": [],
            "gtvh_lm": [],
            "funnygraph_fields": ["timing_profile", "sets[].timing_measured"],
            "series_topics": ["timing", "pause", "delivery"],
            "measured_data": "H1: 14x baseline pause. H3: HOLD 1.4-2x then SNAP 1.48x. Overlap 82% / Gap 18%.",
        },
        "pause": {
            "attardo_nodes": ["timing-performance", "release-theory"],
            "operators": [],
            "gtvh_lm": [],
            "funnygraph_fields": ["timing_measured.punch_pauses_s"],
            "series_topics": ["pause", "timing"],
            "measured_data": "31s Lee hold, 8.16s Louis confession, 1.7s Norm moth. 1.5-3.5s window for big swings.",
        },
        "delivery": {
            "attardo_nodes": ["prosody", "gesture-performance", "performance-of-humor", "KR-NS", "KR-LA"],
            "operators": [],
            "gtvh_lm": [],
            "funnygraph_fields": ["delivery_archetype", "modulator_range", "profile"],
            "series_topics": ["delivery", "timing", "voice"],
            "measured_data": "wpm spectrum 192-117 (Norm→Lee). Valence inversion: content/delivery OPPOSITE.",
        },
        # === STRUCTURE ===
        "setup": {
            "attardo_nodes": ["linear-organization", "script", "KR-SI", "grices-maxims"],
            "operators": ["rigidify"],
            "gtvh_lm": [],
            "funnygraph_fields": ["known_bits", "identity.premise"],
            "series_topics": ["setup", "premise"],
            "measured_data": "2.8:1 setup:punch ratio (335 KT sets). Rock premise rule.",
        },
        "escalation": {
            "attardo_nodes": ["linear-organization"],
            "operators": ["rigidify", "literalize"],
            "gtvh_lm": ["exaggeration"],
            "funnygraph_fields": ["known_bits"],
            "series_topics": ["escalate", "aab"],
            "measured_data": "Rozin AAB: 2 iterations before violation. 1,104 rule_of_three examples.",
        },
        "tag": {
            "attardo_nodes": ["jab-line"],
            "operators": ["repetition_variation"],
            "gtvh_lm": [],
            "funnygraph_fields": ["known_bits"],
            "series_topics": ["tag"],
            "measured_data": "First tag full, second half (diminishing returns). Tags ride overlap mode.",
        },
        "callback": {
            "attardo_nodes": ["linear-organization", "jab-line"],
            "operators": ["repetition_variation"],
            "gtvh_lm": [],
            "funnygraph_fields": ["known_bits"],
            "series_topics": ["callback"],
            "measured_data": "First invocation x1.5, second half, pure repeat zero. Needs mini-gap for retrieval.",
        },
        "button": {
            "attardo_nodes": ["resolution"],
            "operators": [],
            "gtvh_lm": [],
            "funnygraph_fields": [],
            "series_topics": ["button"],
            "measured_data": "Closed trajectory: ends near where it began. Silence AFTER belongs to the room.",
        },
        # === PERSONA & FRAME ===
        "persona": {
            "attardo_nodes": ["footing", "participation-framework", "comic-character"],
            "operators": ["identity_contradict", "expose_self_blindness"],
            "gtvh_lm": [],
            "funnygraph_fields": ["identity", "engine.delivery_archetype", "modulator_range"],
            "series_topics": ["persona", "sincerity", "frame"],
            "measured_data": "Stage persona ≠ person (literature-validated). 9-axis schema.",
        },
        "unreliable-narrator": {
            "attardo_nodes": ["unreliable-narrator-literature", "participation-framework", "footing"],
            "operators": ["split_knowledge", "expose_self_blindness", "mistake_identity"],
            "gtvh_lm": ["garden_path", "role_reversal"],
            "funnygraph_fields": ["identity.awareness"],
            "series_topics": ["frame", "persona", "confession"],
            "measured_data": "5 variants: disguise/collapse/constructed-innocence/faux-protected/honest-exhibitionist",
        },
        "confession": {
            "attardo_nodes": ["implicature", "release-theory"],
            "operators": ["expose_self_blindness", "split_knowledge"],
            "gtvh_lm": [],
            "funnygraph_fields": ["operator_priors.expose_self_blindness"],
            "series_topics": ["confession", "punch", "sincerity"],
            "measured_data": "Louis: 1.67s pauses, 19.6dB, literalize 24% + self_deprecation 16%",
        },
        "sincerity": {
            "attardo_nodes": ["meta-communicative-signal", "humor-signal"],
            "operators": [],
            "gtvh_lm": [],
            "funnygraph_fields": [],
            "series_topics": ["sincerity", "persona", "frame"],
            "measured_data": "Character never signals 'this is a joke'. Performer signals; character doesn't.",
        },
        # === VERBAL MECHANISMS ===
        "ambiguity": {
            "attardo_nodes": ["ambiguity-taxonomy", "saussurean-sign", "pun"],
            "operators": ["double_interpret", "literalize"],
            "gtvh_lm": ["garden_path", "cratylism"],
            "funnygraph_fields": [],
            "series_topics": ["punch", "formats", "voice"],
            "measured_data": "3 types: lexical (two meanings), structural (two parses), phonological (two transcriptions)",
        },
        "implicature": {
            "attardo_nodes": ["implicature", "grices-maxims"],
            "operators": ["split_knowledge", "double_interpret"],
            "gtvh_lm": [],
            "funnygraph_fields": [],
            "series_topics": ["punch", "misdirection", "confession"],
            "measured_data": "Punchline meaning often lives in implicature, not literal text.",
        },
        "aao": {  # AAB pattern
            "attardo_nodes": ["linear-organization"],
            "operators": ["rigidify", "repetition_variation"],
            "gtvh_lm": ["exaggeration"],
            "funnygraph_fields": [],
            "series_topics": ["aab", "escalate"],
            "measured_data": "Rozin 2006: minimum 2 iterations before violation. 1,104 examples in corpus.",
        },
    },
    "agent_write_packet_template": {
        "note": "What an agent receives when writing a set for comedian X",
        "fields": {
            "character_profile": "funnygraph/comedians/{id}/comedian-graph.json identity block",
            "operator_priors": "funnygraph operator_priors (which operators this comic favors)",
            "timing_profile": "funnygraph timing_profile (wpm, pause doctrine)",
            "known_bits": "funnygraph known_bits (what this comic has done)",
            "attardo_relevant_nodes": "from this bridge: which Attardo concepts apply",
            "series_resources": "from gcomedy/series/resources/: clips, craft-talk, data for relevant topics",
            "technique_mix": "from characters2: operator frequency for this comic type",
            "process_skill": "from characters2 SKILL-*.md: the writing process to follow",
        }
    }
}

# Fix the garden-path entry (had a bug)
BRIDGE["mappings"]["garden-path"]["attardo_nodes"] = ["isotopy-disjunction-model", "linear-organization", "grices-maxims"]

# Save
out = Path('/root/gcomedy/agent/unified_vocab.json')
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(BRIDGE, indent=1))
print(f"unified_vocab.json: {len(BRIDGE['mappings'])} mappings")
for k, v in BRIDGE['mappings'].items():
    print(f"  {k:25s} attardo={len(v['attardo_nodes'])} ops={len(v['operators'])} topics={len(v['series_topics'])}")
