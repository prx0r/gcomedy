# Chapter 2: The Five Components of Laughter

*Tymoczko showed that music rests on five components of tonality: conjunct melodic motion, acoustic consonance, harmonic consistency, limited macroharmony, and centricity. Comedy rests on the same five. But the geometry inverts in one critical place.*

---

## The setup is the setup

A comedian walks on stage. Before the first punchline, the audience already has a model of what's about to happen. The comedian's reputation, their posture, the first sentence — all of it builds a prediction. The brain is a Helmholtz machine (Friston, 2010): it constructs hypotheses about what comes next and minimizes surprise by confirming them. Comedy exploits this ruthlessly.

A joke is not a surprise. A joke is a *controlled violation of a specific prediction*. The prediction must exist before the violation is funny. This is why random humor fails — a drummer playing completely random beats is as unfunny as a comedian saying completely random sentences. There is no pattern to break.

Paul Rozin and colleagues demonstrated this in 2006. Across music genres and repetitive jokes, the dominant pattern is AAB: two similar events, then a third that breaks the pattern. Their experiments confirmed that AAB is maximally effective for humor. The minimum of two iterations establishes the pattern; the third violates it at the moment of maximum efficiency.

This is the first component of comedy geometry: **the setup must be predictable enough that the punch can violate it cleanly**.

We tested this. Using 154 scored comedy bits from 10 comedians (collected through the jokegate scoring pipeline), we had a language model rate each setup's predictability (1-10) and each punchline's surprisal (1-10). The result was striking and unexpected:

Setup predictability correlated positively with comedy score (r = +0.33). More predictable setups were funnier.

This is the *opposite* of what happens in music. Cheung et al. (2019) showed that musical pleasure comes from the interaction of uncertainty and surprise: high surprise following low uncertainty produces the most pleasure. In music, uncertainty is the engine. In comedy, predictability is.

Why? Because comedy and music are solving different problems. Music is continuous — it unfolds in time, and the listener's pleasure comes from the ongoing tension between expectation and resolution across many events. Comedy is discrete — it has a setup and a punch, two events with a specific relationship. The setup's job is not to create uncertainty. The setup's job is to establish a *stable platform* from which the punch can launch its violation. If the platform is unstable, the violation has nothing to violate.

This is Tymoczko's conjunct melodic motion, restated for comedy: **the punch barely moves from the setup**. Not in words — word overlap between setup and punch is uncorrelated with score (r = +0.04, our Exp 2). The movement is in interpretation. The setup establishes one reading of the world. The punch establishes a second reading. The distance between them is the violation. And like Tymoczko's voice-leading geodesics, the funniest violations are the *minimal* ones — the smallest move from one interpretation to another that still produces a different world.

We measured this. Punchline length correlated negatively with score (r = -0.32): shorter punchlines are funnier. This matches the 2009 acoustic finding that punchlines are delivered at lower pitch and slower speech rate than the setup — the punch is a descent, not an explosion. It's a downward voice-leading move: barely different in volume, distinctly lower in pitch, distinctly shorter in duration.

---

## Acoustic consonance = benignity

Tymoczko's second component is acoustic consonance — the "click" of a chord that sounds right. Comedy's version is the benign violation (McGraw & Warren, 2010): a joke is funny when it is simultaneously a violation and benign. Something is wrong, but it's okay. Tickling is a mock attack. A pun violates linguistic norms but spells a real word. A roast targets power, not vulnerability.

We tested this on the same 154 bits. The jokegate pipeline had already scored each bit's violation level (0-1) and benignity level (0-1). The benignity metric was the single strongest text-based predictor of comedy score we found (r = +0.49). And benignity showed an inverted-U relationship with score (B + B²: R² = 0.185): not too benign (boring), not too threatening (unfunny), sweet spot in the middle.

This is the same inverted-U that Witek et al. (2014) found for rhythmic syncopation in music. Moderate syncopation produces maximum pleasure and desire to move. Moderate violation produces maximum laughter. Too little is dull. Too much is dangerous. The geometry has a valley of maximum pleasure, and it's the same shape in both domains.

The benignity metric is comedy's acoustic consonance. It measures the *fit* between the violation and the audience's tolerance. A violation that fits the audience's world — that threatens something they can afford to lose — is consonant. A violation that doesn't fit is dissonant. The comedian's job is to find the consonant violations: the ones that threaten norms the audience holds loosely, or targets they can distance themselves from.

This is why non-human personas are comedically powerful. A grey alien filing a complaint about Earth's emotional atmosphere, a reptilian middle-management executive filing cruelty as HR workflow — these characters get distance for free. The jokegate EDGY.md thesis states it directly: non-humans can't be canceled, so they explore, and humans laugh. Distance is the benignity dial that costs the comedian nothing.

---

## Harmonic consistency = thematic consistency

Tymoczko's third component is harmonic consistency: the chords in a passage should belong to the same harmonic world. Comedy's version is thematic consistency: the bits in a set should belong to the same comic world.

A comedian's set has a key — a worldview, a stance, a set of assumptions about reality. Ralph the reptilian middle-management files cruelty as HR workflow. Diogenes the tub cynic treats virtue as a haircut. Each character's misinterpretation rule is their key: the lens through which every joke is filtered. Jokes that fit the key sound right. Jokes that don't sound wrong — even if they're objectively funny, they modulate away from the character's center and break the harmonic consistency.

This is why character graphs matter. A character's persona (deal, facts, misinterpretation rule, operator priors) is their harmonic world. The same punchline voiced by two different characters is the same chord played in two different keys — it sounds different because the context is different. Comedy's timbre is character.

---

## Limited macroharmony = rasa range

Tymoczko's fourth component is limited macroharmony: a piece stays within a limited set of pitch classes. A song in D major uses D, E, F#, G, A, B, C#. It doesn't use every note.

Comedy's version is the rasa range. The nine Indian aesthetic flavors (Bharata's Natya Shastra, extended by Abhinavagupta) are: shringara (erotic), hasya (comic), karuna (compassionate), raudra (furious), veera (heroic), bhayanaka (terrifying), bibhatsa (odious), adbhuta (wondrous), shanta (peaceful).

Comedy is hasya — but hasya never lives alone. Roast is hasya + raudra (comic + furious). Deadpan is hasya + shanta (comic + peaceful). Absurdist comedy is hasya + adbhuta (comic + wondrous). Transgressive comedy is hasya + bibhatsa (comic + odious). Each comedian has a limited macroharmony — the set of rasa combinations they can voice without modulating away from their center.

A roast comic who tries to do deadpan is modulating to a distant key. It can work — modulation is a compositional resource — but it requires a transition, a bridge, a moment where the audience follows the comedian from one tonal center to another. Without that bridge, the modulation sounds like a mistake.

The room also has a macroharmony. A hostile room can't taste veera (heroic comedy needs trust). A sober room can't taste shringara (erotic comedy needs looseness). The room's rasa accessibility is its tonal center, and the comedian must work within it.

---

## Centricity = comic center

Tymoczko's fifth component is centricity: music has a gravitational center, a pitch class that everything orbits. D major orbits D. The D is always present, always felt, even when the melody moves away.

Comedy's centricity is the comedian's core stance — the thing they always return to. Ralph always returns to middle-management frustration. Diogenes always returns to contempt for convention. This is the pitch class of their comedy. Every joke orbits it. Even jokes that seem far away are pulled back by it.

The callback is comedy's version of centric return. A callback takes an earlier joke and returns to it — same idea, new voicing. The audience recognizes the return ("I caught that") and the recognition is its own pleasure. This is the harmonic return: the same chord voiced differently, coming home.

---

## The emerging equation

Combining the five components with our experimental results:

```
comedy_score ≈ predictability(setup) × benignity² × (1 / punch_length)
```

Where:
- **predictability(setup)** must be HIGH — establish the AAB pattern (r = +0.33)
- **benignity** must be MODERATE — inverted-U, sweet spot (R² = 0.185)
- **punch_length** must be SHORT — minimal displacement (r = -0.32)

This is not the music equation. Music: pleasure = uncertainty × surprise (Cheung et al., 2019). Comedy: score = predictability × benignity² / punch_length. The uncertainty term flips sign. Comedy needs stability before violation; music needs tension before resolution.

This is the geometry's first law: **the setup is the platform, the punch is the jump, and the platform must hold**.

---

*Next: Chapter 3 — Orbifolds of the Absurd. Why joke space wraps around itself, and how callbacks exploit the topology.*
