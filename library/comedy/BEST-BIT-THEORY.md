# WHAT MAKES THE BEST BIT ON PAPER — synthesis across the full library

Sources read in full or near-full this session:
- Freud, *Jokes and Their Relation to the Unconscious* ch2 (techniques + economy thesis)
- Bergson, *Laughter* (mechanical-encrusted core image + rigidity)
- Attardo 2020 ch7 (GTVH KR hierarchy) — see ATTARDO-CLASSIFICATION.md
- Hatzithomas 2024, Play-mirth theory (Frontiers in Psychology)
- Ajayi & Mitra 2026, HumorRank (arxiv 2604.19786)
- Hong et al. 2026, Multi-Agent Comedy Club (arxiv 2602.14770)
- Šuppa et al. 2026, RAGthoven / SemEval MWAHAHA (arxiv 2607.13189)
- Liang et al. 2026, Multimodal Humor survey (arxiv 2607.19011)
- HumorGen 2026 (arxiv 2604.09629) — winning-joke features
- Turgeman et al. 2025 (arxiv 2508.19402) — humor transfer hierarchy

## The convergence (this is the finding)

Six independent research programs, spanning 1905 to 2026, converge on
nearly the same recipe for a bit that works *on paper*:

```
ECONOMY (Freud 1905)
  × INCONGRUITY+RESOLUTION (Attardo GTVH; HumorRank wins)
  × CONCISENESS (HumorRank frontier; Freud economy restated)
  × ESCALATION/AAB (Rozin via Attardo; HumorRank specialists)
  × SURPRISE+ABSURDITY (HumorGen 80%/75%)
  × FINAL-PUNCH POSITION (Attardo 92%)
  × PLAYFUL KEYING (Play-mirth 2024)
  − CLICHE (HumorRank failure mode #1)
  − WEAK PUNCHLINE (HumorRank failure mode #2)
```

Every factor is text-side except delivery timing (which DPV/TIC-TALK
own). This document is the on-paper half of the theory.

## Factor 1 — ECONOMY (Freud's unifying thesis)

Freud's ch2 catalogues joke techniques (condensation, multiple use of
same material, double meaning) and then unifies them: **"All these
techniques are dominated by a tendency to compression, or rather to
saving. It all seems to be a question of economy. In Hamlet's words:
'Thrift, thrift, Horatio!'"**

The test he applies: strip the economy from any joke and it dies.
The Iron Front/Iron Crown joke loses everything if you spell out the
"boldness and lack of conscience" thought separately. Double meaning
saves the entire second sentence. Multiple use saves new material.

**Measurable on paper:** every word carries double duty (meaning AND
rhythm, as the Nerdwriter's 207-words-thesis said of Louis). A bit's
economy score = information density: how much of the setup survives
compression. This is testable: compress the bit by 20% — does it lose
the joke or improve it? A great bit compresses well (Attardo's
expanded-version test: adding explicitation often *reduces* funniness
because it lowers the mental processing the joke requires).

## Factor 2 — INCONGRUITY with PARTIAL RESOLUTION (Attardo + HumorRank)

Attardo's LM: the resolution is "partial, playful, non-serious" — it
may even introduce new incongruities. Nerhardt's weights experiment:
incongruity alone triggers laughter; resolution is optional (absurd
humor). But HumorRank's tournament data shows **Incongruity is the
winning mechanism for frontier models** (26.5% of GPT-5's wins), and
Incongruity maps to GTVH's LM — the deep-structure conflict.

**The paper-recipe:** conflicting scripts (SO) + a resolution attempt
that is playful not serious (LM). Seinfeld rigidifies a social custom
until it breaks = pure Attardo LM. Norm's bogus_logic = Freud's
sophistry = a "resolution" everyone sees through = the playful LM.

## Factor 3 — CONCISENESS (Freud economy, restated as tournament data)

HumorRank's frontier models win on Conciseness (31.1% of GPT-5's
wins) — "efficient buildup, comedic timing" tagged at the LA level.
This is Freud's economy measured by an LLM judge tournament. The
mid-tier specialists lead on Absurdity+Escalation instead — they
compensate for less-efficient buildup with bigger turns.

**For us:** concise bits (Hedberg, Seinfeld) compete on economy;
expansive bits (Norm, Chappelle) compete on escalation+absurdity.
Two valid strategies, measurable on paper, matching our timing
doctrines (surgical/reload vs never_stop/sermon).

## Factor 4 — ESCALATION & the AAB PATTERN

Rozin et al. 2006 (via Attardo): the three-step AAB pattern is more
frequent AND considered funnier than AAAB or AB. Loewenstein calls it
"repetition break." HumorRank specialists (HumorGen-7B) win on
Escalation (14.5% of wins). Our escalation operator (character_violation)
and repetition_variation are the registry names for this.

**Measurable:** count AAB structures per bit (we built this as an NS
feature). Rock's stammer-build = escalation. Hedberg's chain = pure
AB-restart, which Rozin says is LEAST funny alone — but Hedberg's
chains work because each AAB is complete inside one-liner. The unit
of analysis matters: AAB within a bit, not across the chain.

## Factor 5 — SURPRISE + ABSURDITY (HumorGen's win-rate data)

Among LLM-judged winning jokes: Surprise 80%, Absurdity 74.8%,
Wordplay 51.3%, Incongruity 49.8%, Narrative 32.7%. Surprise and
absurdity are the necessary conditions at the text level. Note:
Wordplay is only 51% — the weak-baseline over-index (Llama: 29.5%
of wins are wordplay, and they lose via Cliché 50.9%). Wordplay
alone is a losing strategy; wordplay IN SERVICE of surprise wins.

## Factor 6 — FINAL-PUNCH POSITION (Attardo's 92%)

92% of punch lines occur in the last phrase of the last sentence.
Material after is semantically empty. Oring: absence of
final-position punch is the defining difference between jokes and
anecdotes. This is why our bit segmentation takes the chunk-final
sentence as punch-candidate. Norm's moth: the punch ("because the
light was on") is final-position after 2 minutes of digression.
Louis's roadrage window: the meta-confession (b17) is the final beat.

## Factor 7 — PLAYFUL KEYING (Play-mirth theory, 2024)

Hatzithomas's experimentally-tested claim: humor requires TWO
simultaneous appraisals — (a) the stimulus is perceived as a
**playful turn** (serious→playful transition), and (b) the turn is
**consistent with the perceiver's motives** (appetitive→reward-humor
or aversive→relief-humor). Mirth is a distinct emotion from joy or
relief, with its own appraisal signature.

**Maps to our stack:** playful keying = the comic's register/modulator
(the room must appraise it AS comedy, not testimony or insult).
Motive-consistency = audience_alliance (split_knowledge) — the room
laughs when the turn serves THEIR motive (relief, superiority,
recognition). Louis's confessional works because the room's motive
(relief from the unsayable) is served by his turn (saying it). A
Louis bit keyed as serious testimony without the playful turn would
be unbearable, not funny — the appraisal fails.

## Factor 8 — the two failure modes (HumorRank's loser tags)

When bits LOSE in the tournament, the tags are: **Cliché** (worn
structure, the audience predicts the turn) and **Weak Punchline**
(the final-position turn doesn't land). These are the anti-factors.
Our ChatGPT-not-funny finding (memorization trap) is the cliché
mechanism: LLMs over-predict the likely turn, producing the audience's
first guess. A bit avoids cliché by: novel SO instantiation (same
abstract opposition, text-specific surprise), or escalation past the
expected stop, or economy that hides the turn until the last phrase.

## Factor 9 — BERGSON's core image (the ontological ground)

"Something mechanical encrusted on the living" is Bergson's central
comic image. Rigidity or momentum: the muscles continue the movement
when circumstances call for something else. And: "a comic character
is generally comic in proportion to his ignorance of himself. The
comic person is unconscious."

This grounds everything above. Why does rigidify work (Seinfeld)?
Because rigidity-encrusted-on-living is the primal comic. Why does
self-awareness matter (our awareness axis)? Because the unconscious
comic is funnier — UNLESS the persona runs the Norm/Hedberg trick
(constructed innocence = performed unconsciousness over real
awareness). Bergson predicts the two-kinds-of-comic split our graphs
already show: the unaware comic (Louis's performed simplicity is the
surface) vs the aware comic who weaponizes the gap (Norm).

## The on-paper bit rubric (score 0-1 per factor, weighted)

```
paper_score(bit) =
    0.20 × economy         # compressibility test; double-duty words
  + 0.15 × incongruity_lm  # conflicting scripts + playful partial resolution
  + 0.15 × surprise_turn   # final phrase violates the built expectation
  + 0.12 × escalation_aab  # pattern-repeat-break present
  + 0.10 × punch_position  # turn in final phrase of final sentence (Attardo 92%)
  + 0.10 × absurdity       # physical/social expectation broken
  + 0.08 × playful_keying  # room appraises as play (register)
  + 0.05 × motive_fit      # turn serves the room's motive (alliance)
  + 0.05 × conciseness     # efficient buildup, no wasted setup
  − penalties:
      − 0.20 if clichéd    # audience's first guess = the turn
      − 0.25 if weak_punch # final-position turn doesn't land
      − 0.15 if explicitation_attardo  # expanded version funnier = original was under-processed
```

Weights are hypotheses from the convergence: economy weighted highest
(Freud's unifying claim + HumorRank conciseness + Attardo's
explicitation test all point at information efficiency as the master
variable). To be calibrated against HumorRank's tournament outcomes
or our own bit-judge pass when it runs.

## How each comedian scores (qualitative prediction)

| | economy | incongruity | escalation | punch_pos | notes |
|---|---|---|---|---|---|
| **Hedberg** | 0.95 (one-liner = max compression) | 0.8 (literalize) | 0.3 (chain-restart, not AAB) | 0.95 (always final) | loses nothing to cliché if the object is novel |
| **Seinfeld** | 0.9 (50-150 load-bearing words) | 0.95 (rigidify = Bergson's core image) | 0.5 (riff-variations) | 0.9 | the Bergson candidate |
| **Carlin** | 0.7 (lists are expansive) | 0.85 (sacred/profane SO) | 0.9 (list escalation) | 0.85 | economy in the KEYWORD, not the list |
| **Rock** | 0.75 | 0.8 (status/double) | 0.95 (stammer-build) | 0.9 | escalation-strategy comic |
| **Louis** | 0.8 (story earns length) | 0.85 (garden_path) | 0.85 (confessional escalation) | 0.7 (window ended mid-meta) | the full special's punch is the arc |
| **Norm** | 0.5 (deliberately uneconomical) | 0.7 (bogus_logic) | 0.6 (digression, not AAB) | 0.95 (payoff worth it) | economy inverted: length IS the mechanism (DPV) |
| **Chappelle** | 0.7 | 0.85 (split) | 0.8 | 0.75 | the hold does work economy can't |

Note the Norm row: his on-paper score is LOW on economy by design.
This is consistent — Freud's economy is the dominant on-paper factor,
but DPV (timing) can substitute for it in performance. Norm is the
proof that the paper recipe and the stage recipe are not identical:
he fails factor 1 and wins anyway via timing. That's the paper-vs-
stage split our whole framework predicts.

## What this means for the pipeline

1. **The rubric is implementable now** for economy (compression test),
   punch_position (already coded), AAB (already coded), cliché
   (PMI against our 395k corpus + the 1M Reddit corpus per HumorRank's
   topic-handle method). Incongruity/surprise need the bit-judge LLM.
2. **The bit-judge prompt writes itself:** for each bit, output the
   rubric factors + text_sufficiency (dataobjects) + mechanism tag
   (GTVH) + failure-mode tag (HumorRank's cliché/weak-punch).
3. **The two-strategy finding** (conciseness vs escalation) is a new
   plottable axis: paper-economy vs paper-escalation. Matches our
   timing doctrines but is measurable from text alone.
4. **Norm is the control case** for the paper-vs-stage gap: score him
   low on paper, measure him high on stage (DPV). Any bit-judge that
   scores Norm's moth highly on economy is wrong.

## Sources (all on disk)

- Freud PDF: freaktown/data/comedy-theory/Jokes and their relation...pdf
- Bergson HTML: freaktown/data/comedy-theory/bergson-laughter-4352-h.htm
- Attardo PDF: freaktown/data/comedy-theory/The Linguistics of Humor...pdf
  (ch7 → theory/research/ATTARDO-CLASSIFICATION.md)
- HumorRank: papers/humorrank-2604.19786.pdf
- Multi-Agent Comedy Club: papers/multi-agent-comedy-club-2602.14770.pdf
  (reception feedback: discussion wins 75.6% — the RL-loop validation)
- RAGthoven: papers/ragthoven-semeval2026-2607.13189.pdf
  (4-stage Planner/Writer/Reflector/Judge + RAG from corpus; agentic
  scaffolding doesn't beat simple pipeline with strong model — matches
  our Jev-simple-vs-complex finding)
- Play-mirth: papers/play-mirth-theory-2024.pdf
- Multimodal survey: papers/multimodal-humor-survey-2607.19011.pdf
  (visual humor; our stack is audio-first so lower priority)
- HumorBench: papers/humorbench-2507.21476.pdf (reasoning transfers)
- Plus the papers already in PAPER-REVIEW.md (HumorGen, Turgeman,
  Romanowski, StandUp4AI, DPV, TIC-TALK)
