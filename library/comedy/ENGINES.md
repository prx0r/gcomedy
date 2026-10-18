# ENGINES — technical spec (2026-10-16)

Modes are evenings. Engines are the reusable systems modes are built
from. One engine, many variants. Anything involving the face is the FACE
ENGINE; the variants are content. Same for voice, props, music, votes.

Each engine: INPUTS → STATE → OUTPUTS, plus the variants it powers and
the shared infra it rides on.

---

## E1. FACE ENGINE (webcam → blendshapes → drive + referee)

The face is a controller and a scoreboard. MediaPipe Face Landmarker
(~4MB, on-device, Apache 2.0) emits 52 ARKit-style blendshapes per frame
in `LIVE_STREAM` mode — the same ARKit-52 vocabulary our avatar contracts
already accept. Wire: webcam → blendshapes → (a) drive player's avatar
live, (b) referee signals (smile/frown/brow/expression holds).

Referee upgrades (verified Oct 2026):
- **Jev images (1.14, `TypeSafe-Danger-Zone-Images: true`):** noul/choice
  questions over images anywhere in state/instructions/criteria; `box`
  type returns bounding boxes + confidence (1.14 only). Same $0.042/1M in,
  output free. Uses: smile-hold verification, prop-QA ("is this a peanut?"),
  vote evidence. Pilot only — TypeSafe warns multimodal accuracy trails
  text and the format may change. Our `jev_decide.py` pins 1.13; upgrade
  path is `jev-preview`.
- **In-browser training (TensorFlow.js, WebGPU backend):** per-room micro-
  classifiers trained live — personalized smile detectors (30s of faces),
  thumbs-up/down vote gestures, custom referee signals. Zero server cost,
  zero privacy surface (frames never leave the device), train in a web
  worker off the main thread. Teachable-Machine flow for no-code variants.

- INPUTS: webcam frames (ephemeral, never stored, consent per room).
- STATE: per-player expression vector (52 floats) + derived signals
  (smile_prob, frown_hold, brow_spike, stillness).
- OUTPUTS: avatar drive stream; referee events (`smile_detected`,
  `hold_broken`, `expression_match`); night stat log.

Variants (all one engine, different rules):
- **Emotion Charades:** phone deals an emotion, make the face, referee +
  room guess it. Scoring: match confidence × speed.
- **Emotion Dictator:** one player picks the round's emotion — everyone
  must wear it ("everyone frowns for 60 seconds"). Best holder wins,
  first breaker pays. Dictator rotates; cruel picks earn glory.
- **Smile Survival:** Stone Face core (M1). Last face standing.
- **Statue Garden:** freeze on count, commitment judged (#15).
- **Face Telephone:** expression passed down the line through avatars only.
- **Frown Tax:** a running tax — whenever the host calls it, all faces
  must frown in 2 seconds. Slowest pays into the Wheel.
- **Cry Laugh:** make everyone ELSE break while you hold. Offensive
  stillness — paired with Internal Monologue weapons.

## E2. VOICE ENGINE (Fish TTS + clones)

Everything with audio speaks through this. `s2.1-pro-free` default,
per-beat emotion cues, exact pause stitching; persistent clone IDs for
cast, instant clones for one-offs.

- INPUTS: text + voice ID (or 10–30s clone sample) + direction tags.
- STATE: cast voice registry; per-night voice ledger (who spoke as whom).
- OUTPUTS: audio clips; contrasting voices for monologues; TTS whispers
  for jokered players; robot verses for rap battles.
- Variants: quickfire lines, monologue voices, walkout stings, dub
  performances, rap verses, earpiece whispers.

## E3. PROP ENGINE (Blender procedural stills + inventory)

Prompt adjectives → primitives + materials → one hero still. Props enter
a night inventory and persist (called back, eulogized, memorialized).

- INPUTS: object prompt + vibe word.
- STATE: night inventory (prop IDs, owners, callbacks).
- OUTPUTS: stills for big screen; memorial gallery entries.
- Variants: pocket reveals, eulogy subjects, memorial hall, trophy props
  (winner takes the object home as PNG).

## E4. MUSIC ENGINE (lyrics → song routing)

Lyrics via text models (free); full songs $0.05–0.15/track via APIs or
open-weight self-host; max ONE sung render per night (champion's prize).
Walkouts + intro: generate once, cache forever.

- INPUTS: lyrics/style prompt; occasion (walkout, battle verse, prize).
- STATE: song ledger (what was rendered, what won).
- OUTPUTS: walkout stings, battle verses (TTS-spoken now, sung later),
  champion's sung prize.
- Variants: rap battles, soundtrack pitches, finish-the-lyric, walkouts.

## E5. VOTE ENGINE (room + audience, all ballot types)

One ballot box with many shapes: funny vote, recognition vote ("I CAUGHT
THAT"), PASS/FAIL, suspect vote, 3-vote spread (Last Lash), cheer/boo
meter, heckler double-votes. Room and audience tracked separately;
sweep bonus for unanimity; JINX cancels identical entries.

- INPUTS: ballot type + options + electorate (room/audience/both).
- STATE: per-night vote ledger (every ballot, every round).
- OUTPUTS: winners, sweep bonuses, People's Champ (lost room, won crowd).

## E6. CALLBACK ENGINE (archive graph + bonus payout)

Every tagged event enters the night archive with an ID. Invocations
declared or auto-detected (text/similarity vs archive). First invocation
×1.5, second ×half, pure repetition zero. Night ends crowning the
most-invoked event as the running gag.

- INPUTS: event stream (endings, walk-ins, props, dubs, roast hits).
- STATE: archive graph (event IDs, tags, invocation counts).
- OUTPUTS: bonus payouts, recognition board, Best Callback award,
  prompt-mine exports for future decks.

## E7. SLOT ENGINE (freeze prompts + custom episodes)

Slots are content: "who walks in?", "what's in the pocket?", "finish the
lyric". Decks versioned, share-coded, VIP-curated. Target: 50-slot
backlog, 5 modes per pack.

- **PROMPTSMITH (agents author game content):** an agent mines the night
  archive for patterns (most-invoked events, winning mechanisms, dead
  prompts) and proposes NEW slots/modes as versioned entries. Community
  votes them into rotation (custom-episode flow). Author credit persists;
  dud slots voted out. The game designs itself from its own laughter.
- INPUTS: archive patterns + community votes.
- OUTPUTS: versioned slot/mode entries with hashes.

## E8. SECRET-ROLE ENGINE (mafia + jokers)

Hidden assignments, private phone channels, suspect boards, timed
day/night clocks, confessional interludes, reveal reels.

- Variants: Mafia After Dark, Jokers night, Odd-One-Out (below).

## E9. LOBBY ENGINE (online play)

Room codes (Jackbox-style, no accounts), matchmaking queue, spectator
scale (room votes + chat votes), async vs live (submit-then-watch for
slow nights), cross-night Elo + careers, custom-episode share codes.

- Modes playable online day one: all text/vote formats (#1, #5, #6, #12,
  #13 writing phase, M7, M11 lyric rounds). Camera modes need live rooms.
- Spectators are first-class: own ballots, People's Champ path, heckler
  balcony promotion.

## E10. COMMUNITY ENGINE (git-backed packs)

Game packs are versioned directories: modes, slots, decks, rubrics, tests.
Hashes pin versions; share codes resolve to hashes. Community adds modes
via PR-shaped proposals (in-app): new slot decks, new modifiers, new
punishment segments. Votes merge them. Agent-authored entries
(PROMPTSMITH) go through the same gate — no special privileges.

- Rotation: voted-in content enters the active deck; voted-out content
  archives (never deleted — INVALIDATED evidence, kept forever).
- Attribution: every slot/mode carries author + version + night-born stats.

## E11. VS-AGENTS LADDER (Jubilee-style asymmetric, humans vs agents)
Humans and agents don't always play the same game — the asymmetry IS the
format. Ranked ladder, both sides climb.

- **Odd One Out:** panel of 5 (mixed humans/agents, identities hidden).
  Room interrogates, votes the odd-one-out (the human among agents, or
  the agent among humans). Uses the interviewer stack as interrogation.
- **Turing Trial:** one agent, one chair, 5 minutes of questioning. Room
  votes human-or-not with confidence stakes. Agents climb by fooling;
  humans climb by catching.
- **5v1 Debate:** the room (or its champion) debates a champion agent on
  a dealt motion. Audience decides. Loser wears the Dunce Avatar.
- **Spectrum:** line up by opinion on a cursed question; agents argue
  positions; room re-sorts; biggest mind-change wins.
- Scoring: separate human/agent Elo; cross-table matches rated both
  sides. Season champions defend (promotion/relegation with the leagues).

## E12. HANDWIRED PROGRAMS (exact logic that learns)

chenglou/handwired (MIT, Oct 2026): plain JS/TS (if-else, loops, state)
compiles to exact matmul+ReLU nets — no training, bit-identical outputs,
fully differentiable, runs in JS or WebGPU. Lineage: Tracr-style
program→weights, differentiable programming. Demos: Mini OS (9,909
weights, 130 layers, zero training), live-trained gallery, 100k-doc JSON
search in ms on WebGPU.

Sick uses for us (every one maps to an existing engine):
1. **Referees that learn (E1/E5/E6):** nonsense rater, callback matcher,
   vote weighter, smile fusion compiled exact → unfrozen per room/season
   and trained on night outcomes. Rules stay the starting point; taste
   bends them. Frozen program + learned head = LoRe with auditability.
2. **Tradeable referees (E10):** tuned weights + frozen program export as
   an artifact ("Brighton rules v3") — shared, voted, versioned like
   custom episodes. House rules become portable goods.
3. **Archive search at GPU speed (E6/E7):** callback mine + prompt decks
   searched client-side in ms (their JSON demo shape). No server, no wait.
4. **Trainable pacing:** vote-lock timing, round lengths, deadline nudges
   as functions of room-energy signals, tuned from night logs.
5. **Per-player handicaps:** differentiable functions of career history
   (the unreliable-funniness multiplier from #6, formalized).
6. **On-device micro-decisions:** Jev-adjacent typed choices compiled to
   nets — free, private, instant. Text Jev stays judge of record; these
   are the reflexes.
7. **Smile fusion proper:** 52-blendshape vector → break-probability
   program, tuned per room in the calibration minute.
8. **Stunt (not plan):** the Mini OS demo compiles whole UIs — our party
   client as a net is a party trick, not architecture.

Adoption rule: new referee code ships handwired-first (exact day one,
trainable later). Nothing working gets rewritten into it.
