# AGENT GUIDE — how to query the Attardo knowledge graph

> For AI agents writing comedy, analyzing bits, or building video essays.
> This graph is the canonical linguistic baseline. Query it before inventing.

## Quick queries

```python
import json
G = json.load(open('library/comedy/attardo-graph/graph.json'))

# "What is X?"
G['nodes']['punchline']['definition']

# "Which operators implement X?"
G['nodes']['KR-LM']['our_operators']

# "What series topics does X map to?"
G['nodes']['timing-performance']['series_topics']

# "What connects X to Y?"
edges = [e for e in G['edges'] if e['from']=='punchline' and e['to']=='mirth']

# "What's in chapter N?"
G['indexes']['by_chapter']['7']  # GTVH chapter nodes

# "What maps to operator X?"
G['indexes']['by_operator']['garden_path']

# "What's in series topic X?"
G['indexes']['by_series_topic']['punch']
```

## The punch formula (the most important edge)

```
punch = SO-switch + LM-resolution, timed by NS, in LA words, about TA, in SI world
```

When analyzing or writing a punchline, check all 6 KRs:
1. SO: what two scripts are in opposition?
2. LM: what reasoning connects them?
3. SI: what's the world?
4. TA: who is the target?
5. NS: what's the timing strategy?
6. LA: what are the words?

## Operator → KR mapping (for bit analysis)

| If you see this operator fire | It's changing this KR |
|---|---|
| garden_path | LM (the mechanism) |
| literalize | LM + LA (figurative→literal) |
| double_interpret | SO (two scripts) |
| status_invert | TA (status swap) |
| split_knowledge | SO (audience knows) |
| character_violation | TA + SO |
| rigidify | LM (rule past absurdity) |
| juxtapose | LM (incompatible scripts) |
| false_analogy | LM (broken analogy) |
| role_reverse | LM (swap positions) |
| expose_self_blindness | TA (self) + NS (confessional) |

## For bit analysis: the 6-KR checklist

Given a bit transcript, extract:
```
SO: [script_A] vs [script_B] (overlap: [X], opposition: [Y])
LM: [which of the 12]
SI: [setting, participants]
TA: [self/powerful/species/victim]
NS: [pace, rhythm, direct/indirect]
LA: [key words, syllable count]
```

## For bit generation: the constraint set

To generate a joke that works:
1. Establish SO with 2+ iterations (Rozin AAB) in the setup
2. LM must use material already in setup (linear-organization rule)
3. TA determines safety math (self=safest, victim=needs license)
4. NS timing: pause 1.4-2x before punch, deliver 1.48x faster (H3)
5. LA: punch word LAST, hard consonants, 1-2 syllables (Seinfeld)
6. Resolution: full (classic) or partial (absurdist) — pick deliberately

## For video essays: the chapter → topic map

| Video topic | Primary Attardo chapters | Key concepts |
|---|---|---|
| joke | Ch 1, 7 | joke definition, GTVH overview |
| premise | Ch 6, 7 | scripts, SI |
| setup | Ch 4, 6 | isotopy, script activation |
| escalate | Ch 4 | linear organization |
| punch | Ch 4, 7 | incongruity-resolution, SO-switch |
| tag | Ch 7 | jab lines |
| callback | Ch 4 | linear organization, re-interpretation |
| button | Ch 4 | resolution, isotopy restoration |
| pause | Ch 10 | timing, performance |
| delivery | Ch 10 | prosody, gesture |
| timing | Ch 10, 4 | timing, IDM |
| status | Ch 3, 13 | aggression theory, power |
| target | Ch 7, 13 | KR-TA, power-solidarity |
| misdirection | Ch 4, 6 | IDM, script opposition |
| gtvh | Ch 7 | full GTVH |
| violate | Ch 3, 8 | aggression, context |
| the-line | Ch 8, 13 | context, power |

## Full chapter coverage (all 17)

| Ch | Topic | Key nodes |
|---|---|---|
| 1 | Definitions | humor, joke, punchline, mirth, laughter, meta-humor |
| 2 | Methodology | operationalization, corpus-methodology, level-of-analysis |
| 3 | Theories | release/incongruity/aggression + bisociation + complementarity |
| 4 | Incongruity-resolution | IDM, foregrounded/backgrounded, linear-organization |
| 5 | Semiotics | humor-signal, code |
| 6 | Semantics | script, script-opposition-SSTH |
| 7 | GTVH | GTVH, 6 KRs, jab-line |
| 8 | Pragmatics | relevance-theory-humor, context-humor |
| 9 | Verbal humor | pun, verbal-irony, sarcasm |
| 10 | Performance | prosody, timing, gesture, audience-co-performer |
| 11 | Conversation | adjacency-pair, preference-organization |
| 12 | Discourse | footing |
| 13 | Sociolinguistics | power-solidarity |
| 14 | Literature | narrative-humor, comic-character |
| 15 | Translation | untranslatability, kr-independence-evidence |
| 16 | Classroom | humor-pedagogy |
| 17 | Conclusion | complementarity-synthesis, future-directions |

## The complementarity principle (Ch 3)

When analyzing WHY something is funny, check all three theories:
- **Incongruity** (Ch 3.4): what expectation was violated?
- **Release** (Ch 3.3): what tension was discharged?
- **Aggression** (Ch 3.5): who was the target?

All three can fire simultaneously. A complete analysis needs all three.
