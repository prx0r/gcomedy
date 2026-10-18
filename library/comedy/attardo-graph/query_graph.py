#!/usr/bin/env python3
"""Query the Attardo knowledge graph.

Usage:
  python3 query_graph.py node punchline
  python3 query_graph.py operator garden_path
  python3 query_graph.py topic punch
  python3 query_graph.py chapter 7
  python3 query_graph.py edge punchline
  python3 query_graph.py neighbors punchline
  python3 query_graph.py search "script opposition"
  python3 query_graph.py punch-formula
"""
import json, sys
from pathlib import Path

GRAPH = Path(__file__).parent / "graph.json"
G = json.loads(GRAPH.read_text())

def show_node(nid):
    n = G['nodes'].get(nid)
    if not n:
        print(f"Node '{nid}' not found. Available: {sorted(G['nodes'].keys())[:20]}...")
        return
    print(f"\n=== {n['name']} ===")
    print(f"Type: {n.get('type')}  Chapter: {n.get('chapter')}  Page: {n.get('page','?')}")
    print(f"\nDefinition: {n.get('definition','')}")
    if n.get('our_operators'):
        print(f"\nOperators: {', '.join(n['our_operators'])}")
    if n.get('series_topics'):
        print(f"Series topics: {', '.join(n['series_topics'])}")
    if n.get('maps_to_our'):
        print(f"Maps to our: {n['maps_to_our']}")
    if n.get('examples'):
        print(f"\nExamples:")
        for e in n['examples'][:3]:
            print(f"  - {e}")
    if n.get('key_insight'):
        print(f"\nKey insight: {n['key_insight']}")
    if n.get('key_rule'):
        print(f"\nKey rule: {n['key_rule']}")
    # Edges
    out_edges = [e for e in G['edges'] if e['from'] == nid]
    in_edges = [e for e in G['edges'] if e['to'] == nid]
    if out_edges:
        print(f"\nOutgoing ({len(out_edges)}):")
        for e in out_edges[:8]:
            to_name = G['nodes'].get(e['to'], {}).get('name', e['to'])
            print(f"  → {e['type']}: {to_name}  ({e.get('label','')})")
    if in_edges:
        print(f"\nIncoming ({len(in_edges)}):")
        for e in in_edges[:8]:
            from_name = G['nodes'].get(e['from'], {}).get('name', e['from'])
            print(f"  ← {e['type']}: {from_name}  ({e.get('label','')})")

def show_operator(op):
    nids = G['indexes']['by_operator'].get(op, [])
    print(f"\n=== Operator: {op} ===")
    print(f"Nodes ({len(nids)}):")
    for nid in nids:
        n = G['nodes'][nid]
        print(f"  {nid}: {n['name']} (Ch{n.get('chapter')})")

def show_topic(topic):
    nids = G['indexes']['by_series_topic'].get(topic, [])
    print(f"\n=== Series topic: {topic} ===")
    print(f"Nodes ({len(nids)}):")
    for nid in nids:
        n = G['nodes'][nid]
        print(f"  {nid}: {n['name']} (Ch{n.get('chapter')})")

def show_chapter(ch):
    nids = G['indexes']['by_chapter'].get(str(ch), [])
    print(f"\n=== Chapter {ch} ===")
    print(f"Nodes ({len(nids)}):")
    for nid in nids:
        n = G['nodes'][nid]
        print(f"  {nid}: {n['name']} — {n.get('definition','')[:80]}...")

def show_edge(nid):
    edges = [e for e in G['edges'] if e['from'] == nid or e['to'] == nid]
    print(f"\n=== Edges involving '{nid}' ({len(edges)}) ===")
    for e in edges:
        frm = G['nodes'].get(e['from'], {}).get('name', e['from'])
        to = G['nodes'].get(e['to'], {}).get('name', e['to'])
        print(f"  {frm} --{e['type']}--> {to}  ({e.get('label','')})")

def search(query):
    q = query.lower()
    results = []
    for nid, n in G['nodes'].items():
        if q in nid.lower() or q in n.get('name','').lower() or q in n.get('definition','').lower():
            results.append(n)
    print(f"\n=== Search: '{query}' ({len(results)} results) ===")
    for n in results[:15]:
        print(f"  {n['id']}: {n['name']} (Ch{n.get('chapter')}) — {n.get('definition','')[:80]}...")

def punch_formula():
    print("\n=== THE PUNCH FORMULA ===")
    print("punch = SO-switch + LM-resolution, timed by NS, in LA words, about TA, in SI world")
    print()
    for kr in ['KR-SO','KR-LM','KR-SI','KR-TA','KR-NS','KR-LA']:
        n = G['nodes'].get(kr, {})
        print(f"{n.get('name','?')}:")
        print(f"  {n.get('definition','')[:120]}")
        print(f"  Operators: {', '.join(n.get('our_operators',[]))}")
        print()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    cmd = sys.argv[1]
    arg = sys.argv[2] if len(sys.argv) > 2 else ''
    if cmd == 'node': show_node(arg)
    elif cmd == 'operator': show_operator(arg)
    elif cmd == 'topic': show_topic(arg)
    elif cmd == 'chapter': show_chapter(arg)
    elif cmd == 'edge': show_edge(arg)
    elif cmd == 'search': search(arg)
    elif cmd == 'punch-formula': punch_formula()
    else: print(__doc__)
