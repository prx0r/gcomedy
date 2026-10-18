# CONCEPT MAP — Attardo GTVH → our operators → series topics

> The GTVH's 6 knowledge resources mapped to our 15 operators, 12 GTVH LMs,
> and series video topics. This is the bridge between Attardo's formal
> linguistics and our comedy engine.

## The GTVH 6 knowledge resources (Ch 7)

The GTVH says a joke is characterized by 6 knowledge resources:

### 1. Script Opposition (SO)
**Attardo:** Two semantic scripts that overlap in some region but oppose in another. The joke activates one script, then the punchline forces activation of an opposing script. (Raskin's SSTH foundation.)

**Our operators:** `double_interpret` (two readings), `split_knowledge` (audience knows X, persona pretends not to), `mistake_identity`

**Series topics:** punch, misdirection, setup

**Examples:**
- Lock: grounded script vs absurd script ("spongy bread feet" — logistics vs fantasy)
- Acaster: fictional script (undercover cop) vs real script (breakup)
- Louis: sincere script vs confession script

### 2. Logical Mechanism (LM)
**Attardo:** The reasoning that connects the SO to the punchline. The "how" of the incongruity resolution. 12 mechanisms identified.

**Our 12 GTVH LMs (from gtvh.py):**
| LM | Attardo description | Our operator |
|---|---|---|
| garden_path | Lead reader down one path, redirect | `garden_path` |
| juxtaposition | Two incompatible things side by side | `juxtapose` |
| false_analogy | Analogy that breaks on inspection | `false_analogy` |
| role_reversal | Swap roles/positions | `role_reverse` |
| perspective_shift | Change the viewing angle | `double_interpret` |
| figure_ground | Reverse what's figure and what's ground | `figure_ground` |
| exaggeration | Heighten beyond plausibility | `literalize` |
| cratylism | Word-sound = word-meaning | (phonetic humor) |
| rigidify | Follow a rule past absurdity | `rigidify` |
| displacement | Move to wrong context | `displacement` |
| literalize | Take figurative language literally | `literalize` |
| other | (residual) | — |

**Series topics:** gtvh, operators, punch, misdirection

### 3. Situation (SI)
**Attardo:** The contextual setting — objects, participants, time, place. The "world" of the joke.

**Our mapping:** `identity.problem_space`, premise world, the "platform"

**Series topics:** premise, setup

**Examples:**
- Louis Monopoly: SI = playing Monopoly with six-year-old daughter
- Lock recycling: SI = mundane household chore
- Rock White House party: SI = last Obama party

### 4. Target (TA)
**Attardo:** The "butt" of the joke — who or what is being mocked. Can be self, other, group, abstract concept.

**Our jokegate TARGETS:**
| Target | Safety math | Edge score |
|---|---|---|
| self | Safest (no victim) | Bonus |
| powerful | Needs distance | License required |
| species (humanity) | Medium | Distance helps |
| victim | Dangerous | Needs strong license |

**Series topics:** target, the-line, violate, edgy-gate

### 5. Narrative Strategy (NS)
**Attardo:** How the joke is told — the rhetorical structure. Includes: pace, rhythm, dramatic structure, use of reported speech.

**Our mapping:** timing doctrine, delivery shape, the 10-beat arc

**Series topics:** delivery, timing, pause, all the function topics

**Attardo's subcategories:**
- Narration vs description
- Direct vs indirect discourse
- Pace and rhythm (→ our timing doctrine)

### 6. Language (LA)
**Attardo:** The specific words chosen — vocabulary, syntax, sound. The "surface" of the joke.

**Our mapping:** word choice, syllable count (Seinfeld), consonant selection, vocabulary reservoir

**Series topics:** voice, delivery, rhythm-gate

**Attardo's insight:** LA is the most "free" KR — the same joke can be told in many different words. But the words matter for rhythm and emphasis.

## How the 6 KRs interact (the linear organization, Ch 4.3)

```
Setup activates SO (script A)
    ↓
Punchline forces SO switch (script B)
    ↓
LM provides the reasoning for the switch
    ↓
SI is the world where both scripts coexist
    ↓
TA is who the switch damages/ridicules
    ↓
NS controls the timing and pacing of the switch
    ↓
LA is the surface text that carries all of the above
```

**The punch IS the SO switch + LM resolution, timed by NS, in LA words, about TA, in SI world.**

## Isotopy Disjunction Model (Ch 4.3)

Attardo's model for how jokes are linearly processed:
1. Setup establishes an "isotopy" (semantic field, reading direction)
2. Punchline disjoins the isotopy (forces a different reading)
3. The resolution is the listener re-interpreting the setup under the new isotopy

**Maps to:** our "setup builds a prediction model, punch violates it" (DPV framework). The isotopy = the prediction model. The disjunction = the temporal+semantic violation.

## Cross-reference: our operators → Attardo's KRs

| Our operator | Primary KR | Secondary KR |
|---|---|---|
| rigidify | LM (rigidify) | NS (persistence) |
| literalize | LM (literalize) | LA (figurative→literal) |
| double_interpret | SO (two scripts) | LM (perspective_shift) |
| status_invert | TA (status swap) | NS (dramatic irony) |
| split_knowledge | SO (audience knows) | TA (self) |
| mistake_identity | SO (wrong script) | SI (confused setting) |
| character_violation | TA + SO | LM (exaggeration) |
| expose_self_blindness | TA (self) | NS (confessional) |
| false_analogy | LM (false_analogy) | SO (false mapping) |
| juxtapose | LM (juxtaposition) | SO (incompatible scripts) |
| role_reverse | LM (role_reversal) | TA (status swap) |
| unmask | SO (true script revealed) | NS (dramatic structure) |
| bisociate | SO (two frames) | LM (simultaneous) |
| repetition_variation | NS (rhythm) | LA (wordplay) |
| garden_path | LM (garden_path) | NS (misdirection timing) |
