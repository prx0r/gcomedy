# SCENES 00–07 — Silence, Premise, Cold Open, Jazz Experiments

> Script = tightened speakable version of essayhuman.md blocks (owner's words
> kept). Visuals = specific builds. Tech = exact repo + method. Voice =
> louis_reference_lab throughout v1 unless noted.
> Fish s2.1-pro-free supports [bracket] emotion cues + emphasis via caps.

---

## SCENE 00 — SILENCE (new open, ~90s)

**SCRIPT:**
[No narration for 10 seconds. Then, whispered:]
"silence."
[2s pause]
"Everything you are about to see comes from here. And returns here.
Nothing in this film ever leaves."

**VISUAL DIRECTION:**
- 0:00–0:10 black, true silence. No title, no sound.
- 0:10 whisper "silence" → hard cut to white, word SILENCE in black ink
  center frame, hold 2s → slow fade back to black.
- 0:15–0:25 single thin white line draws across black (audio wave), plays
  one sine tone, dissolves downward. Then two waves, a small chord. Each:
  painted, sounding, dissolving. No narration over this.
- 0:25 narration enters over black.

**VISUALS:** canvas line animation (waveform draw + dissolve), white-flash
title card, black field.

**TECH:** HyperFrames composition (seek(t) canvas lines, same pattern as
laptop scene-03a). Dissolve via shaders `NoiseDissolve`. Tones via earshot
procedural sine + envelope (same data drives line + audio). Verify with
`earshot critique` (expect: sparse flagged — this silence is deliberate,
mark as intentional stop-down).

**FISH VOICE DIRECTION:** louis_reference_lab. Whisper register
(`[whispering]` cue). "silence." at ~90 WPM, half normal pace. The second
line at normal pace, flat affect — no performance, just statement. 2s
silence after "here." is part of the take, not edited in.

---

## SCENE 01 — PREMISE PROLOGUE (~2 min)

**SCRIPT:**
"If you know anything about comedy, you know about the importance of a
good premise. Chris Rock put it like this: [CLIP] 'A lot of comedians have
great jokes, and they don't — why isn't this working? It's not working
because the audience does not understand the premise.'

A premise is a situation. A starting point, shared between an audience and
a performer, that is instantly understood.

Take Autumn Leaves. [MUSIC: head, 8 bars] You hear that, and you know the
key. The scale. You remember other renditions. It gives you a shared
fundamental structure to enter into together. For a moment, each person in
the audience leaves their world — and chooses to enter this shared world.
Or premise.

The premise of this video is: what is important in comedy?"

**VISUAL DIRECTION:**
- Rock quote: clip (fair-use excerpt, 8s max) → freeze on "premise", word
  isolates in kinetic type.
- Autumn Leaves: Bill Evans head, chord symbols overlay (Dm7–G7–Cmaj7...)
  drawing in real time as played. Then a second rendition (different artist)
  same symbols — shared structure, different performance.
- "Leaves their world": audience silhouettes (pixabay/openverse) dissolving
  at edges into the chord symbols. Entering the shared world = silhouettes
  reforming around the music.
- Final line on black. Hard cut to disclaimer.

**VISUALS:** chord-symbol overlay animation, silhouette dissolve, kinetic
type ("premise", "shared fundamental structure").

**TECH:** HyperFrames composition. Chord data hand-authored (8 bars,
verified against recording). Dissect-style word timing for the Rock clip.
openverse API for audience silhouettes (CC, attribute in credits).

**FISH VOICE DIRECTION:** louis, conversational 150 WPM. Punch words:
"INSTANTLY understood", "LEAVES their world", "SHARED world". The final
question ("what is important in comedy?") — genuine interrogative lift,
not rhetorical flatness. This question is the premise being installed;
it must sound open, not answered.

---

## SCENE 02 — DISCLAIMER + QUESTION + DELIVERY (essayhuman blocks 2–5, ~45s)

**SCRIPT:**
"Firstly — this is an AI voice. So if you have a problem with that, or you
are attracted to men, please click off the video.

What is the most important thing in comedy?

[10 seconds black]

Delivery."

**VISUAL DIRECTION:** Disclaimer over black (white type, no image — the
voice IS the visual joke). Question as kinetic type, word by word. 10s
black (second level-5 silence of the film — the audience now knows what
black means). "Delivery." — single word, red, center.

**TECH:** motion-probe title cards. The 10s black is intentional (mark in
edit notes so the rendering agent doesn't "fix" it).

**FISH VOICE DIRECTION:** louis, deadpan 140 WPM for disclaimer (do NOT
play it for laughs — flat sells it). Question: slow to 110 WPM, each word
separated. "Delivery." — dropped an octave, final.

---

## SCENE 03 — DELIVERY CAKE + TIME (blocks 6–12, ~75s)

**SCRIPT:**
"But people often forget — when something goes out for delivery, it needs
to arrive on time. Otherwise you get a bit annoyed, right?

In order to deliver anything, there's always timing involved. Even first
class, you only get it the next day.

So timing is not apart from delivery. Timing is baked into what makes
delivery good. Delivery is a cake made up of: premise, structure, wording,
tempo, rhythm, emphasis, silence, voice, persona, physical expression, and
audience responsiveness.

So what is timing?

Actually — no. What is time?

Time — you got a watch? Or time to fuck your mother, am I right.

[beat] But seriously. Your mother is gorgeous."

**VISUAL DIRECTION:** Cake diagram builds ingredient by ingredient as named
(anatomy-style labeled figure). Timing highlighted last — not as an
ingredient but as the oven/pan (the frame, not a part). Watch gag: cheap
wristwatch stock → record scratch → mother joke delivered over a
tasteful portrait (pixabay, fully clothed, 1970s glamour — the joke is the
audacity, not the image).

**TECH:** anatomy figure pattern for the cake (labeled parts, same kit as
laptop). Cake→oven reveal is a layer opacity move.

**FISH VOICE DIRECTION:** louis, 155 WPM, playful. Cake list: metronomic,
one beat per ingredient (the list rhythm IS the demo). "What is TIME?" —
the swerve: pitch up, faster. Mother line: full send, then the pullback
("But seriously") dropped low and sincere — the sincerity after filth is
the joke's second half.

---

## SCENE 04 — TENSION → BRAIN → DOGS (blocks 13–18, ~90s)

**SCRIPT:**
"The most important thing in comedy is also the most important thing in
music, in film — and in making love.

[2s pause]

You see, in that statement I have created a tension. You now want me to
tell you what this important thing is.

The whole point is that as soon as I tell you, the whole game is over. And
if you have a good brain, then you have already realised it.

The most important thing is the human brain. Without that, none of this
would be possible.

You don't see dogs critiquing their social norms. They shit on your carpet
and hump your leg.

Now I'm sure some humans do that too. But at least they are capable of
more.

The way the human brain works is: we are constantly predicting what
happens next."

**VISUAL DIRECTION:** Tension line over black (callback to SEQ 2 grammar:
big claims live on black). Brain reveal: predictive-coding animation
(top-down predictions meet bottom-up signal). Dog clip 3s (pixabay). Final
line lands over a simple animated loop: waveform of expectation (flat) →
event (spike) → update (new flat). The film's first predictive-processing
diagram — keep it crude, it gets refined later.

**TECH:** HyperFrames canvas animation for the expectation loop. Brain
imagery: openverse CC (attribute).

**FISH VOICE DIRECTION:** louis, 150 WPM. "music, in film — and in making
love" — escalating list energy, pause before "making love," deliver it
straight (no wink in the voice; the audience winks for you). "The human
brain" — the reveal: lower, slower, final. Dogs paragraph at 165 WPM,
throwaway energy. Last line ("constantly predicting") — the thesis of the
whole film delivered as a plain fact, no emphasis. Let the animation carry it.

---

## SCENE 05 — HAPPY BIRTHDAY ×2 (blocks 19–20, ~3.5 min)

**SCRIPT:**
"Let me show you. Here's Happy Birthday, played straight in jazz. Listen
to the final note.

[PERFORMANCE: penultimate note held out — longer than comfortable — then
resolves. Hold on the resolution.]

That hold — that little extra silence — that's timing.

Now. You've seen it once. Your brain knows the game. You're thinking:
okay, I'm watching a video about misdirection and comedy, so I'm expecting
something to happen.

Here it comes again.

[PERFORMANCE: resolves completely normally. No tricks.]

See? Anything that happens now, you are subconsciously expecting."

**VISUAL DIRECTION:** Jazz trio performance (record or license ahopelessly
simple trio take — or perform: keys/bass/brushes). Waveform overlay showing
the held note stretching (the hold visualized as the line going flat and
staying flat). Second playing: same overlay, resolving on schedule. Split
comparison at the end: hold durations side by side (2.1s vs 0.4s — measure
the actual takes).

**TECH:** Performance recorded live (or licensed). Waveform overlay from
actual audio (measure the holds — real numbers on screen, teardown rule).
If recording: click track, two takes, keep the better hold.

**FISH VOICE DIRECTION:** Minimal narration by design — the music carries
it. Intro line at 140 WPM, warm. "That hold" — whispered, almost to self.
The "you've seen it once" passage at 150 WPM, conspiratorial (the narrator
and audience are now co-conspirators against the song). After the normal
resolution: 2s silence, then "See?" — quiet triumph.

---

## SCENE 06 — LICENSE + BORING EXPLANATION (block 21, ~2 min)

**SCRIPT:**
"And that opens up new doorways. The comedian now has a license to take you
wherever they want. Or even nowhere at all.

Because now you have accepted the premise. The premise is: Happy Birthday
is playing in jazz, and you are expecting some variation of it.

But what is actually happening is: I am boring you to death explaining a
joke instead of making one. Gradually the tension dissipates. You become
less invested in the bit. And I lose you.

[2s pause]

I go back to my sad life of eating cereal in front of the TV, wishing for
the cold embrace of death — while also being too cowardly to take action."

**VISUAL DIRECTION:** The film visibly deflates: color desaturates
gradually across the passage (grade animation), tempo of cuts slows,
waveform goes flat. Cereal/TV stock (bleak, funny-because-true). The
depression joke lands over the greyest frame in the film so far — then
HARD CUT to full-color Autumn Leaves (next scene). The cut itself is the
recovery.

**TECH:** Grade ramp in HyperFrames (saturation tween). Stock via
openverse/pixabay.

**FISH VOICE DIRECTION:** louis, visibly deflating: start 150 WPM, end
115 WPM. Energy drains across the passage ON PURPOSE (direct the TTS with
`[tired]` cue on the last two sentences). The "cold embrace of death"
line: flat, honest, no punch-up — the audience laughs because it's true,
not because it's performed. Then FULL energy snap back on Scene 07's first
line (contrast is the joke).

---

## SCENE 07 — AUTUMN LEAVES LONG-FORM (block 22, ~2.5 min)

**SCRIPT:**
"Like jazz, a comedian starts with a premise the way a musician starts with
Autumn Leaves. And after a few minutes, you are in a completely different
world.

[Bill Evans Trio, 15 seconds, no narration]

No two musicians' renditions of Autumn Leaves are the same. Yet it gives
you a similar base camp to return to. A place the audience recognises. The
art of the musician is playing with the tension between familiarity and
discovery — guiding the attention of the audience skillfully, taking them
to new places with them, and not losing them along the way.

So returning to the head acts as the resolution of tension. Oh wow. Okay.
So we are back here. After that ten-minute avant-garde bit that just
sounded like noise.

[20 seconds of the noise section. Let them sit in it. Full duration.]"

**VISUAL DIRECTION:** Journey map (base camp → departure → wilderness →
return) drawn progressively under the music. Two renditions compared:
same chord symbols, different performances (split screen, symbols synced).
Noise section: abstract visuals (shaders FlowField), NO narration, NO
subtitles — the audience is alone in the wilderness exactly as described.

**TECH:** Bill Evans clip (fair-use excerpt). Journey map: canvas animation.
Chord symbols hand-checked against recording.

**FISH VOICE DIRECTION:** louis, 140 WPM, warm — this is a love letter to
the music, not a lecture. "Oh wow. Okay. So we are back here." —
genuine relief, exhale audible (`[relieved]`). The noise section has NO
voice. Silence from the narrator is the point (level-3 charged silence).
