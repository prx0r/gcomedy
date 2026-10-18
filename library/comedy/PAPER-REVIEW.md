# PAPER REVIEW — computational humor research, what it means for us

Catalog of every paper touched this session + the standing repo sources.
Each entry: finding → lesson → what it changes for our stack. This is
the raw material for `theory/research/theory-graph.json`.

---

## A. Transferability & portability (the "would this bit work elsewhere" cluster)

### A1 — Turgeman, Shani & Shahaf (2025). "One Joke to Rule them All?
On the (Im)possibility of Generalizing Humor." arxiv:2508.19402
- **Finding:** Humor types form a transfer hierarchy. Dad Jokes (short,
  structural, wordplay) enable strong transfer TO all types but are hard
  to learn FROM. Sarcastic headlines and one-liners are easy sources,
  poor targets. Transfer is asymmetric. Trained LLMs reach 75% on unseen
  humor datasets; diversity helps 1.88–4.05%.
- **Lesson:** Portability is a measurable property of joke *structure*,
  not just topic. Short/structural jokes are the "hub" of humor space.
- **For us:** Predicts Hedberg (one-liner) bits score high on
  persona-lock-in-text but low on persona-NEED — anyone could say them.
  Predictes Chappelle's identity stories are the least portable. Our
  portability axes (E16-E23) get a transfer-learning grounding.
- **Maps to:** bit portability classifier, A10 persona-lock.

### A2 — Baranov, Kniazhevsky & Braslavski (2023). "You Told Me That
Joke Twice: Transferability and Robustness of Humor Detection." EMNLP.
- **Finding:** Humor detectors trained on one dataset transfer unevenly.
  Diversity of training sources matters more than dataset size.
  Unfun.me (smallest) transfers best (macro-F1 0.73); PotD (larger)
  worst (0.27). Models overfit or learn non-specific "humorness."
- **Lesson:** A classifier trained on our 7-comedian corpus may learn
  "stand-up-ness" not "Rock-ness." Topic control is mandatory (StyloSpeaker
  confirms this below).
- **For us:** When training the attribution classifier, control for
  topic (regress out topic-signature rates or train within-topic) or the
  persona-lock number will be inflated by topic overlap.

### A3 — StyloSpeaker (2025). "A stylometric analysis of speaker
attribution from speech transcripts." arxiv:2512.13667
- **Finding:** Speaker attribution from transcripts works via stylometric
  features (character/word/token/sentence/style). Performance highest
  under topic-control condition. Normalized transcripts help except
  when topic is already controlled.
- **Lesson:** Text-fingerprint is real and measurable, but topic is the
  main confound — exactly the negative-space finding we already have
  (Louis never says fame; Seinfeld never says self).
- **For us:** Validates the attribution classifier design. Use topic
  signatures as control variables. Our 15,825-bit corpus is larger than
  most attribution benchmarks.

---

## B. What makes a winning joke (text-only quality)

### B1 — HumorGen (2026). "Cognitive Synergy for Humor Generation."
arxiv:2604.09629
- **Finding:** Among LLM-judged winning jokes (556 matches), feature
  prevalence: Surprise 80%, Absurdity 74.8%, Wordplay 51.3%,
  Incongruity 49.8%, Narrative 32.7%, Sarcasm 15.8%, Irony 15.5%,
  Dark 14.0%. Also: standard SFT loss conflicts with surprise needed
  for comedy; DPO with Elo-ranked pairs helps; process distillation
  (reasoning traces) beats joke-only training.
- **Lesson:** Surprise and absurdity are the text-level necessary
  conditions. Wordplay and incongruity are the mechanism layer.
  Narrative (story bits) are a minority of "wins" by count — consistent
  with one-liners being overrepresented in joke corpora, not standup.
- **For us:** Text-side quality rubric for generated bits: must contain
  surprise + absurdity; mechanism must be one of our 25 theories. The
  Elo-ranking + DPO loop is the shape of our RL plan.

### B2 — Romanowski, Valois & Fukui (2025). "From Punchlines to
Predictions." arxiv:2504.09049 (CMCL @ NAACL)
- **Finding:** LLMs max 51% at identifying humorous punchlines from
  standup transcripts; humans score 41%. Prompt engineering doesn't fix
  it. High subjectivity.
- **Lesson:** Text-only punchline detection is near-ceiling low. Confirms
  our failed laugh predictor (cv R²=-0.18) isn't our bug — it's the
  task. Timing/audio is where the signal is (DPV).
- **For us:** Never trust text-only funny-labels. Our bit classifier
  must label MECHANISM (which theory fired) not FUNNINESS. GTVH tagging
  not laugh prediction.

### B3 — "Not All Jokes Land" (2025). arxiv:2506.01819
- **Finding:** (from abstract scan) LLM joke evaluation needs better
  than binary labels; land/no-land is gradient and context-dependent.
- **Lesson:** Our laugh scores (Ali Wong 0-3.5) were the right
  granularity; binary would have been worse.

### B4 — HumorBench (2025). arxiv:2507.21476
- **Finding:** LLMs trained on STEM reasoning transfer well to humor
  COMPREHENSION (New Yorker caption contests). Reasoning, not
  knowledge, drives explanation quality. Test-time scaling mixed results.
- **Lesson:** The Jev delivery decoder's failure (0.19 emo acc) is a
  domain-transfer failure, not a reasoning-capability failure. It needs
  comedy-specific calibration (which our SPEC-JEV-DELIVERY loop already
  does).

### B5 — "Comparing Apples to Oranges" (2025). EMNLP Findings 505.
- **Finding:** 600 jokes across 4 types (puns, non-topical Reddit,
  topical Reddit). LLM explanation quality: accuracy + completeness
  rubric. Larger models better (β=1.707, p<0.001). Topical jokes
  hardest (need esoteric knowledge).
- **Lesson:** Explanation difficulty scales with required world
  knowledge. Our graph's `knowledge.knows` field is the right structure
  for making a persona's topical bits explainable.

---

## C. Identity & persona (the "only they can say it" cluster)

### C1 — "Not Human, Funnier" (2026). arxiv:2602.12763
- **Finding:** Expert interviews + 58-video content analysis of identity
  standup. Audiences decode standup through layered identification:
  comedian identity, joke targets, perceived intended audience.
  Anecdotes (38 instances) dominate identity-based strategy. Three
  strategies: construct content of comedian identity, [others in paper].
- **Lesson:** Persona-dependence is a real audience-decoding layer, not
  our invention. Anecdote-form is the identity delivery vehicle — which
  matches Louis (anecdote NS) and Chappelle (anecdote/character-chain).
  Seinfeld's monologue-list is the identity-ABSENT form (auditor).
- **For us:** Our identity_contradiction theory already cites this paper
  (arxiv:2602.12763 in graph evidence). The layered-identification frame
  becomes the audience-side model for our graphs.

### C2 — Freud techniques (pogpet theories.json, from Jokes and Their
Relation to the Unconscious ch.2-5)
- **Finding:** Six technical mechanisms (condensation, same_word_switch,
  displacement, bogus_logic, opposite_says_it, degrading_analogy) +
  superiority (tendentious jokes need: butt, blocked insult, audience
  alliance). Each with depends_on/fails_when conditions.
- **Lesson:** Freud operationalized = a classifier with preconditions.
  The conditions are checkable in text (mostly). These are the oldest
  "what makes it work on paper" theories and they're already in our
  registry with judge questions.
- **For us:** The theory-judge pass over 15,825 bits can run Freud's
  conditions as the prompt rubric. `bogus_logic` = Norm's archetype
  already validated against the registry.

### C3 — Bergson rigidity (pogpet theories.json, Laughter 1911)
- **Finding:** Mechanically following a rule after reality makes it
  absurd is inherently comic.
- **Lesson:** Seinfeld's home mechanism (rigidify prior 0.95) is
  Bergson. His bit anatomy (hold custom to literal rule until it breaks)
  IS the 115-year-old theory, executed.
- **For us:** The rigidity theory node gets a measured exemplar. The
  Seinfeld graph is the theory's living proof-of-concept.

---

## D. GTVH & computational structure

### D1 — "Navigating the Joke Space" (CHum 2026). Amir, Ngo, Toplyn,
Hickerson
- **Finding:** GTVH topic handles (key nouns capturing SO+LM) + PMI
  against 1M-joke Reddit corpus quantifies joke originality. Handle-level
  PMI + Sentence-BERT novelty correlate with comedian-rated originality
  on 400 LLM jokes + 80 Witscript jokes.
- **Lesson:** GTVH is computationally operational for ORIGINALITY
  scoring, not just classification. PMI against a big corpus = "is this
  joke structure already worn out."
- **For us:** We can score originality of generated bits the same way:
  extract the topic handle (our GTVH LM+SO), PMI against our 395k-word
  corpus + the 1M Reddit corpus if we get it. The technique-index
  mapping.json already bridges LM→theory.

### D2 — GTVH Analyzer (github iamahmadyasin/gtvh-analyzer, cited in
RESEARCH-multimodal-comedy.md)
- **Finding:** Staged pipeline (segment → detect humorous lines →
  annotate KRs) outperforms single-pass GTVH annotation.
- **Lesson:** Our bit-segmentation (15,825 bits) + per-bit theory-judge
  IS the staged pipeline. We're already built correctly.
- **For us:** Justifying the two-step: segment first (done), then
  annotate each bit (next).

### D3 — Attardo & Raskin GTVH (1991; Attardo 2020 OUP) + Raskin SSTH
(1985) — in repo via audition/gtvh.py
- **Finding:** Joke = {SO, LM, SI, TA, NS, LA}, hierarchical. SO
  determines most; LA least. Similarity = shared low KRs.
- **For us:** The KR tuple is our per-bit label format. similarity()
  already implemented. The 25-theory registry's attardo-lm family
  (garden_path, figure_ground, exaggeration) are LM options.

---

## E. Timing & multimodal (the delivery layer, already in repo)

### E1 — DPV "Timing is Everything" (arxiv 2605.00143)
- **Finding:** Temporal features substantially outweigh semantic
  incongruity for audience appreciation (828 Chinese pro sets). Timing
  GATES cognitive access.
- **For us:** The thesis behind E01 (8-second confession) and E02
  (six pauses). Text-only quality (this review's focus) is the
  INCOMPLETE picture; timing is the other half. Our portability
  framework keeps them separate axes deliberately.

### E2 — TIC-TALK (CHum 2026, arxiv 2603.21803)
- **Finding:** Kinetic energy r=-0.75 with laughter rate — stillness
  before punchline. Personal/bodily content > geopolitical. Laughter
  history dominates onset (hot room stays hot).
- **For us:** Body-dial pipeline already wired (MediaPipe). The
  "personal > geopolitical" finding matches our topic-signature:
  Louis's parenting/body rates are the highest on the roster.

### E3 — StandUp4AI (arxiv 2505.18903, EMNLP 2025 Findings)
- **Finding:** 3,617 videos, 7 languages, 334h, ~3M words, 130K+
  laughter labels. Word-level sequence labeling (not binary). Whisper/
  WhisperX timestamp discrepancies reveal missed laughs.
- **For us:** The master corpus when we get access. Word-level labeling
  is the right unit (matches our bit granularity).

### E4 — Laugh predictor failure (our result, this session)
- **Finding:** GradientBoosting on Ali Wong's 925 labeled captions:
  cv R² = -0.18. Surface text features explain nothing about laugh
  placement.
- **Lesson:** Matches B2 (humans 41%, LLMs 51% at punchline ID). Text
  alone cannot predict laughs. Our classifier must tag mechanism not
  funniness.

---

## F. Generation & RL (the "write novel bits" pipeline)

### F1 — HumorGen CSD + DPO (arxiv 2604.09629) [also B1]
- **Finding:** Process distillation (teacher reasoning + joke) beats
  joke-only SFT. Elo-ranked DPO pairs help. Alignment tax: next-token
  prediction conflicts with surprise.
- **For us:** When writing novel bits in a comic's style: distill the
  REASONING (which theory, why this mechanism for this persona) not just
  the text. Our graphs ARE the reasoning traces. Score candidates with
  Elo-style pairwise (our arena already does this for sets).

### F2 — Humor Mechanics (arxiv 2405.07280)
- **Finding:** One-liner generation via multistep reasoning —
  reconstruct the joke-creation process as steps, then generate.
- **For us:** Matches F1 process distillation. For Hedberg-style bits:
  generate the OBJECT first, then the TWIST (their anatomy), as steps.

### F3 — Plan2joke (SemEval 2026, abateam)
- **Finding:** Policy-driven two-pass generation with humor policies
  per type. SFT on merged datasets adjusted to policies.
- **For us:** Our "policies" are the persona constraints: topic-signature
  (what they'd never say), operator priors (which mechanisms they use),
  stylometry (sentence stats). Two-pass: plan the bit (theory selection)
  then write (persona-voice).

### F4 — "ChatGPT is fun but not funny" (arxiv 2306.04563)
- **Finding:** ChatGPT classifies joke-typical features well but
  generates predictably. Memorizes training jokes (replicated output).
  Joke-typical characteristics mislead classification.
- **Lesson:** "Joke-y-ness" features ≠ funniness. Our classifier must
  avoid the same trap: classifying "sounds like a joke" not "sounds
  like Rock."

---

## G. Metatheory & framing

### G1 — "A Little Metatheory" (AAAI 2012, Raskin)
- **Finding:** Optimal computational humor theory needs: body (main
  hypothesis), purview (domain), goals, falsification, justification.
  SSTH/GTVH have all five. Template fillers (LIBJOG, JAPE) generate but
  don't understand.
- **For us:** Our 25-theory registry has body (hypothesis) + evidence
  + conditions/fails_when (= falsification). We're missing explicit
  purview statements per theory. Worth adding later.

### G2 — "Re-defining Humor Data Objects" (arxiv 2605.25171)
- **Finding:** Binary funny/not labels insufficient. Need: social
  context, audience reaction, recovery attempts. LLM prompt must first
  judge whether TEXT ALONE supports the joke, then explain, then flag
  multimodal dependence. Models hallucinate explanations when context
  missing.
- **Lesson:** Text-sufficiency is a first-class judgeable property —
  literally our portability axis 4 (standalone-validity). The prompt
  design (assess-sufficiency-first) is our bit-judge prompt template.
- **For us:** The theory-judge pass over bits should output:
  {text_sufficient: bool, missing_context: str, theory: str, confidence}.

### G3 — Who's Laughing Now (arxiv 2509.21175, survey)
- **Finding:** Overview of computational humor gen+explanation. LLMs
  explain stylistic elements well (personification, wordplay) but fail
  esoteric/context-dependent humor. Lazy pun generation documented
  (both senses in one generation).
- **Lesson:** LLM explanation ≠ LLM generation. We can use LLMs to
  EXPLAIN/annotate our bits (theory-judge) even though generation
  needs the persona constraints (F1-F3).

---

## The synthesis — what it all means for us

1. **The classifier is pre-approved.** StyloSpeaker + Baranov et al.
   establish text-attribution works, topic is the confound, diversity
   of training helps. Our 15,825 bits + topic-signature controls = a
   better setup than most published benchmarks.

2. **Tag mechanism, not funniness.** B2 (51%/41%) + E4 (our R²=-0.18)
   agree: text cannot predict laughs. The classifier labels WHICH
   THEORY fired (GTVH/mechanism), never "is this funny." Funny lives
   in timing (DPV) and delivery (TIC-TALK) — separate axes.

3. **Portability is structural.** A1's hierarchy (Dad Jokes = hub,
   headlines = leaves) predicts our one-liner-vs-identity-story split.
   Short structural bits travel; identity anecdotes don't. Testable on
   our corpus via cross-comedian confusion matrix.

4. **Persona is a measurable layer the audience actually uses.** C1's
   layered-identification + C2/C3's mechanisms = our graphs are the
   right abstraction. The classifier confidence IS persona-lock.

5. **Originality is computable.** D1's topic-handle PMI against a big
   corpus gives us a novelty score for generated bits. Wire it after
   the classifier.

6. **Generation needs process, not just product.** F1+F2+F3 converge:
   distill reasoning (which theory for this persona), plan then write,
   score with Elo. Our graphs + arena + Jev = the exact stack.

7. **The bit-judge prompt is designed.** G2's assess-sufficiency-first
   pattern + B1's surprise/absurdity features + our 25-theory conditions
   = one prompt that outputs {text_sufficient, mechanism, missing_context,
  confidence} per bit.

8. **Topic-signature is load-bearing infrastructure.** It controls the
   classifier (A2/A3), constrains generation (F3 policies), and IS the
   negative-space essay material (E03). It earns its disk space.

## Priority order for the stack

1. Attribution classifier (persona-lock) — validates everything
2. Topic-controlled confusion matrix (which comics are text-neighbors)
3. Bit-judge pass (25-theory annotation, text-sufficiency per bit)
4. Originality scorer (topic-handle PMI)
5. Generation loop (plan → write → classify → Elo)
