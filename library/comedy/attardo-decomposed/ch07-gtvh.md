# Chapter 7: The General Theory of Verbal Humor

## The 6 Knowledge Resources (KR)

The GTVH characterizes every verbal joke by 6 KRs:

### 1. Script Opposition (SO)
Two semantic scripts that overlap but oppose. The foundational insight from Raskin's SSTH.

**Formal:** SO = (script₁, script₂, overlap_region, opposition_type)

**Types of opposition:**
- Truth/falsehood
- Normal/abnormal
- Expected/unexpected
- Cause/effect reversed

**Our operators:** double_interpret, split_knowledge, mistake_identity

### 2. Logical Mechanism (LM)
The reasoning that connects SO to the punchline. 12 mechanisms identified.

**The 12 LMs:**
1. **Garden path** — lead down one path, redirect
2. **Juxtaposition** — incompatible things side by side
3. **False analogy** — analogy that breaks
4. **Role reversal** — swap positions
5. **Perspective shift** — change viewing angle
6. **Figure-ground** — reverse what's figure/ground
7. **Exaggeration** — heighten beyond plausibility
8. **Cratylism** — word-sound = word-meaning
9. **Rigidify** — follow a rule past absurdity
10. **Displacement** — move to wrong context
11. **Literalize** — take figurative literally
12. **Other** — residual

**Our 12 GTVH LMs (gtvh.py) map 1:1 to these.**

### 3. Situation (SI)
The contextual setting — objects, participants, time, place.

**Formal:** SI = (location, participants, objects, activities, genre)

**Our mapping:** premise world, the "platform"

### 4. Target (TA)
Who/what the joke is about.

**Attardo notes:** TA can be self, other, group, or abstract. The choice of TA affects the "safety" of the joke.

**Our jokegate TARGETS:** self, powerful, species, victim

### 5. Narrative Strategy (NS)
How the joke is told — rhetorical structure, pace, rhythm.

**Attardo's subcategories:**
- Narration vs description
- Direct vs indirect discourse
- Pace and rhythm

**Our mapping:** timing doctrine, delivery shape

### 6. Language (LA)
The specific words — vocabulary, syntax, sound.

**Attardo's insight:** LA is the most "free" KR. The same joke can be told in many words. But LA matters for rhythm and emphasis.

**Our mapping:** word choice, syllable count, consonant selection

## The KRs are independent (mostly)

Changing any one KR produces a different joke:
- Same SO + different LM = different joke
- Same SO + different TA = different joke (same structure, different target)
- Same SO + different LA = same joke, different words

**This is why our operators work:** each operator changes one or more KRs:
- rigidify changes LM
- status_invert changes TA
- literalize changes LM + LA
- double_interpret changes SO

## The punchline as KR-switch

The punchline is where the KR switch happens:
- SO switches (script A → script B)
- LM provides the reasoning for the switch
- NS times the switch
- LA carries the switch in words

**The punch IS the SO switch + LM resolution, timed by NS, in LA words, about TA, in SI world.**

## Jab lines vs punch lines (Attardo 2001)

- **Punch line:** the humorous trigger at the END of the text
- **Jab line:** humorous triggers WITHIN the body of the text

**Our mapping:** punch = the main laugh point. Jab lines = tags, asides, secondary laughs. Long bits (like Louis specials) have many jab lines, not just one punch.
