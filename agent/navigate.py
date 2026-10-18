#!/usr/bin/env python3
"""AGENT NAVIGATOR — load character + theory + data → write packet.

The endgame tool: an agent navigates a comedian's profile, the Attardo
knowledge graph, historical data, and series resources to produce a
write-ready packet. Feed this into agent_harness.py.

Usage:
  python3 agent/navigate.py --comedian louis-ck
  python3 agent/navigate.py --comedian stewart-lee --topic confession
  python3 agent/navigate.py --comedian norm-macdonald --operator garden_path
  python3 agent/navigate.py --list-topics
  python3 agent/navigate.py --query "how does the punch work"
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from collections import defaultdict

GCOMEDY = Path("/root/gcomedy")
FUNNYGRAPH = Path("/root/funnygraph")
CHARACTER2 = Path("/root/characters2")

def load_attardo():
    return json.loads((GCOMEDY / "library/comedy/attardo-graph/graph.json").read_text())

def load_vocab():
    return json.loads((GCOMEDY / "agent/unified_vocab.json").read_text())

def load_character(cid):
    gpath = FUNNYGRAPH / "comedians" / cid / "comedian-graph.json"
    if not gpath.exists():
        return None
    return json.loads(gpath.read_text())

def load_series_resources(topic):
    d = GCOMEDY / "series/resources" / topic
    if not d.exists():
        return None
    out = {}
    for f in ["CLIPS.md", "CRAFT_TALK.md", "DATA.md", "THEORY.md"]:
        p = d / f
        if p.exists():
            out[f] = p.read_text()
    return out

def load_characters2_skill(comic_type):
    """Load relevant SKILL file based on comic type."""
    skill_map = {
        "confessional": "SKILL-joke-writing.md",
        "deadpan": "SKILL-seinfeld.md",
        "storytelling": "SKILL-storytelling.md",
        "one-liner": "SKILL-setup-punch-tag-two-stories.md",
        "absurdist": "SKILL-joke-writing.md",
    }
    skill = skill_map.get(comic_type, "SKILL-joke-writing.md")
    p = CHARACTER2 / "theory" / skill
    return p.read_text() if p.exists() else ""

def navigate(cid, topic=None, operator=None):
    """Produce a complete write packet for a comedian."""
    # Load all sources
    attardo = load_attardo()
    vocab = load_vocab()
    char = load_character(cid)

    if not char:
        return {"error": f"No graph for '{cid}'"}

    # Extract character identity
    ident = char.get("identity", {})
    op_priors = ident.get("operator_priors", {})
    timing = char.get("timing_profile", {})
    known_bits = char.get("known_bits", [])
    archetype = char.get("engine", {}).get("delivery_archetype", ident.get("archetype", "?"))

    # Determine relevant Attardo topics
    # If topic specified, use it. Otherwise infer from operator_priors.
    if topic:
        relevant_topics = [topic]
    elif operator:
        # Find which vocab entries use this operator
        relevant_topics = [k for k, v in vocab["mappings"].items() 
                          if operator in v.get("operators", [])]
    else:
        # Infer from operator priors (top 3 operators)
        top_ops = sorted(op_priors.items(), key=lambda x: x[1] if isinstance(x[1], (int,float)) else 0, reverse=True)[:3]
        relevant_topics = []
        for op, _ in top_ops:
            for k, v in vocab["mappings"].items():
                if op in v.get("operators", []):
                    relevant_topics.append(k)
        relevant_topics = list(dict.fromkeys(relevant_topics))[:5]  # dedupe, top 5

    # Gather Attardo nodes for relevant topics
    attardo_nodes = []
    for t in relevant_topics:
        mapping = vocab["mappings"].get(t, {})
        for nid in mapping.get("attardo_nodes", []):
            node = attardo["nodes"].get(nid)
            if node:
                attardo_nodes.append({
                    "id": nid,
                    "name": node["name"],
                    "definition": node.get("definition", "")[:200],
                    "key_insight": node.get("key_insight", ""),
                    "our_mapping": node.get("maps_to_our", ""),
                })

    # Gather series resources
    series = {}
    for t in relevant_topics:
        res = load_series_resources(t)
        if res:
            series[t] = {k: v[:500] for k, v in res.items()}

    # Gather relevant operators
    operators = []
    for t in relevant_topics:
        mapping = vocab["mappings"].get(t, {})
        for op in mapping.get("operators", []):
            if op not in operators:
                operators.append(op)

    # Gather relevant GTVH LMs
    lms = []
    for t in relevant_topics:
        mapping = vocab["mappings"].get(t, {})
        for lm in mapping.get("gtvh_lm", []):
            if lm not in lms:
                lms.append(lm)

    # Build the write packet
    packet = {
        "schema": "pogtown.write-packet.v1",
        "comedian_id": cid,
        "name": char.get("name", cid),
        "archetype": archetype,
        "tier": char.get("tier", "?"),

        # IDENTITY (from funnygraph)
        "identity": {
            "deal": ident.get("deal", ""),
            "premise": ident.get("premise", ""),
            "misinterpretation_rule": ident.get("misinterpretation_rule", ""),
            "contradictions": ident.get("contradictions", []),
            "modulator_range": ident.get("modulator_range", []),
            "operator_priors": op_priors,
        },

        # TIMING (from funnygraph measured data)
        "timing": {
            "doctrine": timing.get("doctrine_hypothesis", ""),
            "status": timing.get("status", ""),
            "measured_sets": timing.get("measured", []),
        },

        # KNOWN BITS (from funnygraph)
        "known_bits": [
            {"title": b.get("title"), "why_it_works": b.get("why_it_works", "")[:200]}
            for b in known_bits[:5]
        ],

        # THEORY (from Attardo graph via vocab bridge)
        "theory": {
            "relevant_topics": relevant_topics,
            "attardo_nodes": attardo_nodes,
            "operators": operators,
            "gtvh_lms": lms,
        },

        # SERIES RESOURCES (from gcomedy)
        "series_resources": series,

        # WRITE CONSTRAINTS (from Attardo + our experiments)
        "write_constraints": {
            "setup_punch_ratio": "2.8:1 (335 KT sets)",
            "pause_before_punch": "1.4-2x baseline (H3: HOLD then SNAP)",
            "punch_delivery_rate": "1.48x faster than setup (H3)",
            "aab_minimum": "2 iterations before violation (Rozin)",
            "punch_word_position": "LAST — nothing follows the flip word",
            "linear_organization": "punch must use setup material, not new info",
            "target_safety": "self=safest, powerful=needs distance, victim=needs license",
            "gricean_rule": "appear to follow maxims, violate one while cooperating",
        },

        # ANTI-PATTERNS (from NoSlop)
        "anti_patterns": [
            "definitional copula: 'I'm not X. I'm Y.' (NoSlop #1 tell)",
            "three-item lists without variation",
            "jagged rigid rhythm (uniform short sentences)",
            "clever reframe pull-back ('that's not murder, that's architecture')",
            "hedges: 'kind of', 'sort of', 'in a way'",
        ],
    }

    return packet

def query_attardo(query):
    """Search the Attardo graph by keywords."""
    attardo = load_attardo()
    keywords = [w for w in query.lower().split() if len(w) > 2]
    results = []
    for nid, n in attardo["nodes"].items():
        text = f"{nid} {n.get('name','')} {n.get('definition','')} {n.get('maps_to_our','')}".lower()
        score = sum(1 for kw in keywords if kw in text)
        if score > 0:
            results.append({"id": nid, "name": n["name"], "chapter": n.get("chapter"),
                          "score": score, "definition": n.get("definition","")[:150]})
    results.sort(key=lambda x: -x["score"])
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--comedian", "-c", help="Comedian ID")
    parser.add_argument("--topic", "-t", help="Force a specific topic")
    parser.add_argument("--operator", "-o", help="Force a specific operator")
    parser.add_argument("--query", "-q", help="Query the Attardo graph")
    parser.add_argument("--list-topics", action="store_true")
    parser.add_argument("--format", choices=["json", "summary"], default="summary")
    args = parser.parse_args()

    if args.list_topics:
        vocab = load_vocab()
        print("Available topics:")
        for k in sorted(vocab["mappings"].keys()):
            m = vocab["mappings"][k]
            print(f"  {k:25s} operators={m.get('operators',[])}")
        return

    if args.query:
        results = query_attardo(args.query)
        print(f"Query: '{args.query}' — {len(results)} results")
        for r in results:
            print(f"  {r['id']}: {r['name']} (Ch{r['chapter']})")
            print(f"    {r['definition']}...")
        return

    if not args.comedian:
        print("Usage: navigate.py --comedian <id> [--topic T] [--operator O]")
        print("       navigate.py --query 'how does the punch work'")
        print("       navigate.py --list-topics")
        return

    packet = navigate(args.comedian, args.topic, args.operator)

    if "error" in packet:
        print(f"ERROR: {packet['error']}")
        return

    if args.format == "json":
        print(json.dumps(packet, indent=1))
    else:
        print(f"\n{'='*60}")
        print(f"WRITE PACKET: {packet['name']} ({packet['comedian_id']})")
        print(f"{'='*60}")
        print(f"Archetype: {packet['archetype']}  Tier: {packet['tier']}")
        print(f"\nDEAL: {packet['identity']['deal'][:120]}")
        print(f"PREMISE: {packet['identity']['premise'][:120]}")
        print(f"\nOPERATOR PRIORS: {packet['identity']['operator_priors']}")
        print(f"\nTIMING: {packet['timing']['doctrine'][:150]}")
        if packet['timing']['measured_sets']:
            for s in packet['timing']['measured_sets'][:2]:
                print(f"  measured: {s.get('set_id')}: wpm={s.get('wpm')} max_pause={s.get('max_pause_s')}s")
        print(f"\nRELEVANT TOPICS: {packet['theory']['relevant_topics']}")
        print(f"OPERATORS: {packet['theory']['operators']}")
        print(f"GTVH LMs: {packet['theory']['gtvh_lms']}")
        print(f"\nATTARDO NODES:")
        for n in packet['theory']['attardo_nodes'][:5]:
            print(f"  {n['name']}: {n['definition'][:100]}")
        if packet['known_bits']:
            print(f"\nKNOWN BITS:")
            for b in packet['known_bits'][:3]:
                print(f"  {b['title'][:60]}")
        print(f"\nWRITE CONSTRAINTS:")
        for k, v in packet['write_constraints'].items():
            print(f"  {k}: {v}")
        print(f"\nANTI-PATTERNS:")
        for a in packet['anti_patterns']:
            print(f"  ✗ {a}")

if __name__ == "__main__":
    main()
