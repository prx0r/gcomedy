# ATTARDO CLASSIFICATION — what the book says our classifier must do

Source: Attardo, *The Linguistics of Humor: An Introduction* (OUP 2020),
Chapter 7 (GTVH), read in full from
`library/comedy/ATTARDO-LINGUISTICS-OF-HUMOR-2020.pdf`.
This file is the bridge from the book to our classifier design.

## The punchline finding (literally)

**GTVH's founding question is our classification question.** Attardo &
Raskin (1991) created the theory to answer "when are two jokes the
same joke?" Six Knowledge Resources, organized hierarchically — and the
hierarchy order = degree of perceived similarity between jokes
(confirmed empirically by Ruch et al. 1993):

```
Script Opposition      ← most similarity-determining
Logical Mechanism
Situation
Target
Narrative Strategy
Language                ← LEAST similarity-determining
```

## Why our classifier gets 40% — it only sees the weakest KR

Our TF-IDF + logistic regression operates ENTIRELY on the **Language**
KR (surface features: words, bigrams, frequencies). Attardo explicitly
places Language LAST in the similarity hierarchy. We're classifying on
the one dimension that matters least for "are these the same joke."

That's the quantitative answer to "what is the classifier testing for
Louis": his vocabulary texture (fucking, kid, mouth, father, like/just
filler). It is NOT testing his Script Opposition (caring/cruel on the
self), his Logical Mechanism (garden_path + perspective_shift), his
Target (self), his Narrative Strategy (anecdote), or his Situation
(road/parenting/hotel macro-scripts). Those are where Louis's
similarity-to-himself actually lives.

## The six KRs as feature families (the upgrade plan)

Each KR becomes a feature block. Ranked by the hierarchy — build SO
features first:

### 1. Script Opposition features (highest value)
Raskin reduces all SOs to three abstract oppositions: good/bad,
normal/abnormal, actual/non-actual. Each joke instantiates one into a
text-specific local opposition. Di Maio's intermediate level bridges
(text-specific → intermediate → abstract).

**Measurable features:**
- SO-abstract-class per bit (which of the three)
- SO-text-specific label (via LLM judge or pattern)
- Number of jab-line SOs vs one final punch-SO (Tsakona 2003: many
  jokes have multiple SOs along the body — jab lines)

Our graphs already hypothesize SO per comedian (louis=caring/cruel,
seinfeld=normal/absurd, carlin=sacred/profane). The classifier should
test whether bits MATCH their comedian's hypothesized SO.

### 2. Logical Mechanism features
LM is optional (absurd humor may lack resolution) but empirically real
with neurological correlates (Chen et al. 2017). Our gtvh.py
LM_OPTIONS are the vocabulary.

**Measurable features:**
- LM-class per bit (garden_path, rigidify, literalize, false_analogy...)
- LM-present vs LM-absent (absurdity without resolution)
- The 25-theory registry's technique families map here (Freud's 6 +
  Attardo's LM catalogue)

### 3. Situation features (macro-scripts)
The background script / mental space. Hempelmann & Attardo (2011):
**backgrounded incongruity** (talking animals, stereotypes — suppressed
via willing suspension of disbelief) vs **focalized incongruity** (the
active one the punch resolves). This is the mechanism behind our
topic-signatures: the Situation is the macro-script the comedian
operates in (road for Louis, word-playroom for Carlin, object-world
for Hedberg).

**Measurable features:**
- Backgrounded-incongruity count (impossible premises accepted without
  comment — a talking moth, a fairy with a bill)
- Focalized-incongruity presence (does the punch resolve one specific
  incongruity?)
- Macro-script class (already our topic-signatures, relabeled)

### 4. Target / Orientation features
Priego-Valverde et al. (2018) extension: humor ORIENTATION
(1st/2nd/3rd person) is distinct from TARGET (which requires
aggression). Scogin & Pollio: ~66% of humor is targeted, ~34%
non-directed.

**Measurable features:**
- Orientation class: first-person (self-deprecating) / second-person
  (hearer) / third-person (other) / situation
- Aggression-present bool (orientation + aggression = target)
- Target class: self / peers / powerful / systems / code / objects
  (already our A4 axis — the graph's TA field)

Rodney Dangerfield = first-person orientation WITH self-target. Norm's
sympathy bits = third-person orientation, aggression toward the
audience's comfort (not a clean target). The orientation/target
distinction sharpens our A4.

### 5. Narrative Strategy features
Textual organization. Jokes are prototypically short stories ending in
punch line (Oring 1989: absence of final-position punch = the defining
difference between jokes and anecdotes). One-liners = compressed
stories; riddles = Q/A; lists = lists.

**Measurable features (pure text, no model needed):**
- **Punch-position:** 92% of punch lines occur in the last phrase of
  the last sentence (Attardo et al. 1994). Material after = semantically
  empty (repetitions, interjections, speaker-ID). VALIDATES our bit
  segmentation (punch-candidate = chunk-final sentence). Measurable:
  does the bit's final sentence carry the incongruity?
- **AAB three-step pattern:** Rozin et al. (2006) — AAB is more
  frequent AND funnier than AAAB or AB. "Repetition break." Countable:
  how many bits per comedian use AAB vs other patterns?
- **Jab-line density:** Tsakona (2003) — multiple SOs along the body.
  Jab lines per bit = mid-body laugh-points vs single final punch.
- **NS class:** narrative / qa / monologue-list / one-liner-chain
  (already our gtvh.py NS_OPTIONS — our graphs hypothesize it per
  comedian; the classifier can test it)

### 6. Language features (what we already have)
Attardo's own retrospective correction: this KR should be called
**"Semiotic Strategy"** — it handles phonology (puns), morphology, syntax,
lexicon, register, style, punch-line placement, AND prosody. Our TF-IDF
is a crude lexical subset of this one KR. Keep it, but stop pretending
it's the whole classifier.

## The Attardo-valid classification stack (v2 design)

```
bit text
  ├─ SO block    (LLM judge: abstract class + text-specific + jab count)
  ├─ LM block    (LLM judge: which mechanism; or pattern-match)
  ├─ SI block    (macro-script class + backgrounded/focalized count)
  ├─ TA block    (orientation + aggression + target class)
  ├─ NS block    (punch-position bool + AAB count + jab density + NS class)
  └─ LA block    (TF-IDF — what we have now)
        ↓
  similarity-weighted classifier (SO=6, LM=5, SI=4, TA=3, NS=2, LA=1)
```

Weight features by the KR hierarchy. A bit matching a comedian on SO
+ LM + TA should classify as them even if the vocabulary differs. This
is why the bogus-bit test failed: my fake Louis bits matched on LA
weakly and SO/LM not at all (I wrote the anatomy but the classifier
couldn't see the anatomy — it only saw words).

## Concrete feature specs (implementable now)

| Feature | KR | How to compute | Cost |
|---|---|---|---|
| punch_final_sentence_has_turn | NS | check if last sentence differs in register/word class from first (heuristic) or LLM | code / cheap LLM |
| aab_pattern_count | NS | count repeated-then-break structures (lemma-level) | code |
| jab_line_count | SO | LLM: how many laugh-points before the final punch? | LLM |
| so_abstract_class | SO | LLM: good/bad, normal/abnormal, actual/non-actual | LLM |
| lm_class | LM | LLM against gtvh.py LM_OPTIONS | LLM |
| orientation_class | TA | LLM: 1st/2nd/3rd/situation | LLM |
| aggression_present | TA | LLM | LLM |
| backgrounded_incongruity_count | SI | LLM: impossible premises accepted without comment | LLM |
| macro_script_class | SI | topic-signature argmax (already computed) | code |
| tfidf_vector | LA | what we have | code |

## The "what is Louis quantitatively" answer

Under this stack, Louis = the bit whose:
- **SO** is caring/cruel (self-directed) — abstract class good/bad
- **LM** is garden_path or perspective_shift
- **SI** is road/parenting/hotel macro-script, high backgrounded-
  incongruity tolerance (the van premise is accepted as real)
- **TA** is first-person orientation + self-target (aggression toward
  self, Scogin & Pollio's 66%-targeted category)
- **NS** is anecdote with jab-lines along the body + a final punch
  that is the meta-confession
- **LA** is the confessional lexicon (fucking, kid, mouth, father)

The current classifier only tests the last line. The upgrade tests all
six, weighted by what actually determines joke-identity per the
hierarchy Attardo & Raskin derived and Ruch et al. confirmed.

## Cherry-picking warning (Attardo's methodological admonition)

"Examine ALL instances of humor in a text, or a representative random
subset." Our 200-per-comedian light sample IS random (seeded). The full
12k run must also be stratified-random, not sequential. And we must
compare against a baseline (Attardo's punch-volume example: measuring
punch loudness is meaningless without baseline non-punch loudness).
For us: a comedian's SO/LM profile is meaningless without the corpus-
base rate of that SO/LM across all comedians.

## Sources (in-repo PDF)

- Attardo, S. (2020). *The Linguistics of Humor: An Introduction.*
  OUP. Ch. 7 (GTVH) read in full. PDF:
  `freaktown/data/comedy-theory/The Linguistics of Humor....pdf`
- Freud, S. *Jokes and their relation to the unconscious.* PDF same dir.
- Bergson, H. *Laughter* (1911). HTML:
  `freaktown/data/comedy-theory/bergson-laughter-4352-h.htm`
- Ruch et al. (1993) — KR hierarchy empirical confirmation (cited in ch7)
- Attardo et al. (1994) — 92% punch-position finding (cited in ch7)
- Rozin et al. (2006) — AAB three-step funniness (cited in ch7)
- Tsakona (2003) / Norrick (2010) — jab lines / compound jokes
- Hempelmann & Attardo (2011) — backgrounded incongruity
- Priego-Valverde et al. (2018) — orientation vs target
- Scogin & Pollio (1980) — 66% targeted humor
- Chen et al. (2017) — LM neurological correlates
