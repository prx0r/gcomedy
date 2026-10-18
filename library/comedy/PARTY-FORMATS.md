# PARTY FORMATS — canon (2026-10-16)

Three levels + cross-cutting modifiers. **Modes** are evenings (progression
→ champion). **Round formats** are single games (one prompt → perform →
vote). **Slots** are atomic freeze prompts ("who walks in?"). **Modifiers**
cut across everything. A **pack** ships modes the way Jackbox ships 5 games.

## TAXONOMY (locked)

```
PACK (e.g. FREAK NIGHT ONE: 5 modes)
 └─ MODE (evening: qualifiers → bracket/final → champion)
     ├─ ROUND FORMAT (one game: prompt → perform → vote)
     │    └─ SLOT (atomic freeze prompt: who/object/note/door)
     └─ MODIFIERS (callback bonus, roast injection, heckler powers,
                    genre constraints — apply inside any round)
```

- Modes own progression and champions. Rounds are portable: a roast
  exchange can appear inside Freeze Night, Stone Face halftime, or Last
  Jester Standing without changing its rules.
- Slots are content, not code: new games = new slot questions, not new
  systems. Backlog target: 50 slot concepts, ship 5 modes per pack
  (Jackbox's ratio).

## MODIFIER: CALLBACK BONUS (runs all night, every mode)

Every tagged event (ending, walk-in, object, dub line, roast hit, nonsense
verdict) enters the night archive with an ID. Any later performance can
invoke it — declared ("callback to #12") or auto-detected (text/delivery
similarity vs archive).

- Payout: score multiplier on the round (×1.5 first invocation) + a
  dedicated audience button: "I CAUGHT THAT" (recognition vote, separate
  from funny vote — catching is its own skill, with its own mini-board).
- Anti-spam (callbacks, not replays): each event pays ONCE per night;
  second invocation pays half; pure repetition (no transformation) pays
  zero. The bonus rewards recontextualization.
- Night-end: "Best Callback" awarded from the archive graph (most-invoked
  event = the night's running gag, crowned on screen).

## MODIFIER: WHEEL OF SHAME (loser punishments, every mode)

Every elimination, failed dare, or last-place finish spins the wheel on
the big screen. 12 segments, audience-weighted (chat can vote segments
heavier mid-spin). Loser performs immediately, filmed for the edit.

- Starter segments: Australian-accent apology to a houseplant (30s) ·
  Internal Monologue about yourself in sports-commentator voice ·
  Eulogize the object that just beat you · Let the room write your next
  3 texts (read aloud) · Wear the Dunce Avatar for 3 rounds · Defend the
  worst take in the room as your own · Slow-motion replay of your failure
  with nature-doc narration · Swap voices with the winner for one round ·
  Read your last search history in a Shakespearean accent · 15s BE IT
  possession chosen by chat · Compliment every player, escalating eye
  contact · Callback tax: invoke 3 earlier-night events in 30 seconds.
- Rules: wheel never repeats within a night (segments burn). Punishments
  are performances — the room votes "served" or "double it". Served =
  shame cleared + career stat. Doubled = spin again, stakes stack.
- Assets: the wheel UI (one component); punishments reuse every renderer
  (TTS, avatar, monologue, eulogy). Cheapest content in the pack: a list.

## PORTABLE ROUND: ROAST EXCHANGE (appears inside any mode)

Two exchanges, head-to-head. A deals a roast (≤30 words), B answers with a
counter or a redirect at someone else (Hot Potato variant: 10s to redirect
or wear it). Audience votes per exchange. Damage tracked on avatars (cracks,
soot) for the night.

- Fits: King of the Hill bouts, Freeze Night walk-in roasts ("roast the
  newcomer"), Last Jester duels, Stone Face halftime, Court halftime.
- Constraints dealt per bout (genre, must-include word, 10-word cap).
- JINX rule (stolen): identical lines cancel, neither scores.
- Safety line (stolen): stuck? The engine writes your line for half points.

## JACKBOX STEALS (proven, adopt wholesale)

- **One task at a time.** Never ask a phone for two inputs at once: pick,
  draw, OR type. Pacing beats features (the Jack Principles).
- **Host with a voice.** Every mode needs its Schmitty — ours is Ella
  (interviewer stack) or a per-mode host persona. The host reads prompts
  aloud, reacts to specific answers, keeps the room moving.
- **Escalating rounds.** R1 normal → R2 double points → final round shared
  prompt, triple points, 3 votes to spread (Last Lash shape). Every mode
  ends bigger than it starts.
- **Sweep bonus.** Unanimous vote = bonus (Quiplash). Landslide callbacks
  pay extra.
- **Audience as second electorate.** Room votes + chat/audience votes
  tracked separately; audience majority can swing (People's Champ award for
  losing the room but winning the crowd).
- **Custom episodes.** Rooms save prompt/slot decks with share codes; VIP
  curates. Best decks get featured. Our callback mine IS the deck builder.
- **Extended timers + moderation.** Streamer settings: longer input timers,
  family filter, manual censor (VIP). Boring but required for real rooms.
- **New games are remixes.** Drawful = Fibbage + drawing; Joke Boat =
  evolved Quiplash. Our new modes should remix slots, not invent systems.

---

## GAME MODES (the unit that matters)

### M1. STONE FACE (try-not-to-smile championship)

The killer. Every player's face-avatar lives on screen in a grid — avatars
mirror the room live. Minutes are weapons: before the night, each player
prompts/builds a standup minute. Minutes play on the TV one at a time while
webcams watch the watchers. First to smile is out.

- The crack-predictor gag: each avatar shows the room's read on its human —
  as smile probability rises, the avatar starts to crack BEFORE the human
  does (trembling lip, watering eyes). The audience watches avatars to call
  cracks early. "CRACK IMMINENT on seat 3."
- Structure: qualifiers (everyone survives 3 minutes or not) → survival
  bracket (head-to-head, one screen split) → final (last two stone faces,
  champion's minute vs challenger's minute).
- Two leaderboards: best stone face (survival time) + most lethal minute
  (smile timestamps credited to the minute's builder).
- Inputs: minute prompts pre-night; live webcam frames (ephemeral, consent,
  camera-off = spectator).
- Assets: per-player minute audio; avatar grid (Mixamo rigs or portrait
  fallback); smile signal (omni frames ~1fps or local classifier).

### M2. FREEZE NIGHT (improv evening)

A cast plays one long evening of scenes. Any scene can freeze at any beat:
door opens, pocket reached for, phone rings, note discovered. Freeze slots
dealt to the room ("who walks in?", "what's in the pocket?", "what does the
note say?"). Winner's prompt unfreezes the scene. Walk-ins become recurring
cast; pocket objects persist in inventory; callbacks compound all night.

- Structure: 4–6 scenes a night; each scene runs 5–8 min with 2–3 freezes.
  Night champion = most winning prompts + best audience-rated moment.
- Round formats inside: #1 Funnier Ending, #2 Pocket Object, #3 Freeze
  Frame (any slot variant), Callback Hell overtime (final scene must
  include 3 earlier-night jokes).
- Assets: quickfire TTS per winning beat; Blender still per winning prop;
  transcript mine all night.

### M3. COURT OF NONSENSE (jester trial season)

Repeat format with seasons. Players are jesters; each trial they deliver
maximum-nonsense sets, rated as code (non-sequitur rate, semantic distance,
literalization count). Reigning Nonsense Champion defends weekly with
escalating constraints (must include 3 dealt words, must rhyme the verdict).

- Structure: trials → season table → champion defense. Loser wears the
  Dunce Avatar for a week (portrait overlay, career record).
- Round formats inside: #5 Court sets, #6 Least Funny Answer (halftime),
  Translator exhibitions (gibberish testimony).

### M4. DUB-OFF (tournament)

Bracket dub tournament. Clip dealt, two contestants dub it, room + chat
vote mid-dub (performers see votes move and adjust). Winners advance;
clips get harder (noir stare → daytime soap → security footage).

- Structure: 8-seed bracket, quarter/semifinal/final. Final clip is
  always the same cursed standby (the owl) — house tradition.
- Round formats inside: #4 Dub the Clip; halftime #12 Wrong Answers Only.

### M5. KING OF THE HILL ROAST

One throne, one mic. Reigning monarch takes challengers one at a time;
each bout is 2 roast exchanges. Audience votes; winner holds the hill.
Avatar shows battle damage (cracks, soot) per successful hit taken.

- Structure: open challenge queue (phones), first to 5 defenses = night
  champion, dethroned monarch drops to challenger queue.
- Round formats inside: roast exchanges; #11 Genre Swap championship
  bouts (roast in genre X).

### M6. LAST JESTER STANDING (battle royale)
Everyone performs 30 seconds. Audience votes one OFF per round. Shrinking
cast, rising pressure, final two duel with 60 seconds each.

- Structure: N players → N−1 → … → 2 → champion. Any material allowed
  (standup bit, dub, eulogy, nonsense). Fastest mode (whole game ~20 min).
- The twist: eliminated players join the "heckler balcony" — their chat
  votes count double in later rounds (dead have power).

### M7. WOULD I LIE TO YOU (truth panel)

Each round, one player (or agent) states a bizarre claim about themselves
("I once sued a pigeon and won"). Panel interrogates, then votes TRUE or
LIE. Points for fooling the panel (liar) or calling it (panel). AI players
are terrifying here — an LLM invents plausible lies AND delivers true
stories suspiciously.

- Structure: everyone takes the claim seat once → panel scores → highest
  fool-rate wins. Final: champion liar vs room, one claim, triple points.
- Round format inside: CLAIM + CROSS-EXAMINATION (2 min interrogation,
  interviewer stack runs the questioning) + VERDICT vote.
- Truth sourcing: humans use real life; agents draw from their canon lore
  (persona.facts = true claims, generated riffs = lies). The panel never
  knows which deck the claim came from.
- Assets: none (pure dialogue). Cheapest dialogue mode.

### M8. MAFIA AFTER DARK (social deduction + confessional edit)

The vendored mafia pack, but the mode owns TIMINGS and the EDIT. Day/night
cycles with strict clocks; between rounds, players are pulled "outside the
room" for 20-second confessionals ( webcam, one prompt: "who do you trust
right now?"). At night's end the engine compiles confessionals + kills +
vote reveals into a highlight video.

- Structure: existing mafia states (LOBBY → NIGHT → DISCUSSION → VOTE →
  REVEAL → ENDED) + CONFESSIONAL interludes. Comedy casting: roles get
  joke briefs (the Doctor must justify every save as malpractice).
- The edit is the product: auto-cut highlight reel (kill reveals synced to
  the victim's earlier "I feel safe" confessional = comedy gold, free).
- Assets: confessional clips (webcam), kill stings, final compile render.
- Agents play identically to humans (pack already specs this).

### M9. PICTIONARY AFTER DARK (draw + guess, funny decks)

Classic draw-guess loop with cursed decks (NSFW-ish toggle, "things your
therapist said," "banned children's books"). Drawer draws on phone canvas;
room guesses; artist's agony is the show. AI artist variant: prompter
describes, image gen draws, room guesses the prompt.

- Structure: rotating drawer, 60s draws, 3 rounds + final (whole room draws
  one prompt, best/worst galleries).
- Decks are content: NSFW toggle, themed packs, audience-submitted prompts
  (moderated). Worst Drawing Hall of Fame persists.
- Assets: phone canvas (no new tech); AI-artist variant reuses image gen.
- Scoring: guessers split for correct guesses; drawer paid per guesser who
  got it (teaches clarity); bonus for funniest wrong guess (consolation
  prize = the real game).

### M10. HEADBANDZ / CHARADES (act it out)
Card on forehead (phone shows everyone-but-you) or acted clue. Webcam +
avatar mirror the acting — the avatar exaggerates every gesture, so bad
acting becomes great TV. NSFW/funny decks same as M9.

- Structure: 60-second turns, pass/skip tokens, team or free-for-all.
  Final: lightning round, 10 cards, one actor, whole room shouting.
- Avatar gag: the mirror avatar over-acts (confidence-mapped exaggeration:
  hesitant human = wildly committed avatar). The worse you are, the
  funnier the screen.
- Assets: card decks (content); webcam + avatar mirror (shared with M1).
- Scoring: cards cleared; bonus for guesses that arrive via the avatar
  doing something the human definitely didn't do.

### M11. SOUNDTRACK (music night)
Lyrics are cheap, sung audio is rented — so music night leads with words
and steals Jackbox's Mad Verse City shape (game writes your first line,
you write the rhyming killer, robot performs, room votes).

- **Rap battle (Mad Verse City port):** each player gets a seed word
  ("occupation"), engine writes line one ending on it, player writes line
  two (must rhyme, should wound). TTS robot performs both verses head to
  head. Room votes + cheer/boo buttons. Bracket to a champion. Misheard
  robot pronunciations are a feature, not a bug.
- **"What does X fuck to":** a character/situation is dealt ("a divorced
  magician", "this exact party in 40 minutes"). Players pitch the
  soundtrack: title + one lyric + why. No audio needed — the pitch IS the
  performance. Vote for most inevitable song.
- **Finish the lyric:** engine writes 2 bars of a cursed song (sea shanty
  about HR violations, power ballad for a parking warden), room completes
  it on phones, best completion performed (spoken, then sung when the
  render budget allows). Shared-prompt final, Last-Lash style.
- Assets: lyrics (free, text models now); TTS robot voices (have it);
  sung renders later (ACE-Step-class, rented per winner, not per round).
- Scoring: battle wins + soundtrack pitches + lyric completions feed one
  board. Night ends with the champion's verse actually sung (rent ONE
  render — the prize budget).

### M12. JOKERS (impractical-jokers night)

Secret earpiece TV. Each round, one player is secretly jokered: their
phone (earpiece in, screen hidden) feeds them instructions NO ONE else
sees — TTS whisper, text flash, or a rival player's live-typed command.
They must execute it inside whatever else is happening (a scene, a
trial, dinner) without breaking cover. Refuse or get caught = punishment.
Survive = points + the room never knew.

- The private-channel principle (Jackbox's best trick): phones show
  unique info. Jokered players get a red dot ONLY they see; everyone
  else's phone shows "find the joker" with a live suspect vote.
- Dares deck: social ("agree with everything for 2 minutes, escalating"),
  verbal ("work the word 'moisturizer' into every sentence"),
  physical ("mirror whoever speaks to you"), nested (two jokers, opposite
  orders, neither knows). AI-dealt dares adapt to the live transcript.
- Punishment ladder: fail a dare → punishment drawn from the Humiliation
  Ritual deck, performed immediately, filmed for the edit. Three
  punishments = Jester's Shame (avatar wears it all night).
- The reveal: night ends with the joker reel — every secret instruction
  replayed over the footage of the victim doing it. Best unaware moment
  wins its own award.
- Assets: phones + earpieces (players' own); TTS whispers (Fish); suspect
  board; joker reel compile (production rule). Secret-role infra shared
  with M8 mafia.
- Scoring: survived dares (joker) + correct suspect IDs (room) + best
  punishment performance (victim — losing pays!).

---

## SETS: SPLAT ROOMS AS STAGES (Marble Atlas beta)

Party modes play IN places, not on blank screens. Marble Atlas generates
posed set views from text/image prompts at explicit target cameras —
generate once per set, cache forever, cut between cached views.

- **Set pipeline:** `atlasTextToImage` (or a splat-room still) → seed view
  → `images2PosedRGBD` (camera + depth) → `atlasGenerate` at our 4 camera
  plots (wide/medium/close/side = target cameras) → cached set (4 views +
  depth). Optional `splats2Mesh` → GLB for 3D stage/AR use.
- **Themed sets per mode:** western saloon (Freeze Night), dungeon cell
  (Mafia), hearth hut (Court of Nonsense), BA cabin (Dub-Off green room),
  stand-up club (Stone Face finals), spaceship bridge (Vs-Agents debates).
  New set = one prompt + 4 camera generations. Sets persist as venues.
- **Freeze-frame + Atlas:** freeze the scene → `atlasMasked` paints the
  winning walk-in/object INTO the set views → unfreeze with the thing
  already in the room. The pocket object doesn't just get described —
  it's sitting on the table in the wide shot.
- **Camera discipline:** cuts log per beat (existing director rule);
  depth maps allow avatar compositing + subtle parallax. Pure-rotation
  rigs rejected by the API — plots must translate (dolly, not just pan).
- **Naming note:** Atlas "splats" = Gaussian splat scenes (→ GLB mesh),
  NOT our /root/splat ambient-video rooms. Both feed stages: Atlas sets
  for scenes, splat reels for lobby ambience + venue skins.
- **Needs:** `WLT_API_KEY` (user has beta access) + per-set generation
  budget (pennies per set, cached forever).

## PRODUCTION RULE: EVERY MODE SHOOTS ITS EDIT

- Confessionals: M8's interlude mechanic is portable — any mode can pull
  players aside for 20s between rounds. Prompt dealt by the host.
- Highlight compile: night-end auto-edit (kills, cracks, winning callbacks,
  best heckles) rendered from the event log. The log already timestamps
  everything; the edit is a playlist, not a project.
- Careers: wins, kills, cracks, nonsense titles persist per player across
  nights (party records). Champions defend; losers wear overlays.

---

## ROUND FORMATS (games modes playlist)

## 1. FUNNIER ENDING (the killer)

Scene setup dealt (2 lines premise + 2 characters). Scene plays to the
freeze point. Each side submits an ending on their phone. Both endings
performed (TTS voices). Room votes. Winner's ending is canon.

- Input: ending text (≤60 words), optional tone tag.
- Assets: none (voices only). Cheapest format in the pack.
- Advance: next scene, scores persist. Loser's ending archived (callback mine).
- Repeat hook: callback league — old losing endings resurface as prompts.

## 2. POCKET OBJECT ("it's beautiful")

Freeze variant. Scene freezes as a character reaches into their pocket.
Slot: "what does he pull out?" Each side prompts an object. Winner's
object gets a procedural Blender still (`bpy`: primitives + materials from
prompt adjectives, one hero render for the big screen). Scene unfreezes:
"it's beautiful" — cut to the object.

- Input: object prompt (≤20 words) + optional vibe word (cursed, triumphant).
- Assets: one Blender still per round, load one at a time while room votes.
- Refinement rounds: "make it more cursed" = parameter tweak, voted on phones.
- Advance: object persists in scene inventory, can be called back later.

## 3. FREEZE FRAME / WHO WALKS IN

Scene freezes as someone enters (door opens, phone rings, car pulls up).
Slot: "who walks through the door?" Winner's character walks on with a
generated entrance line in their voice. Scene unfreezes around them.

- Input: character prompt (≤20 words: who + one trait + what they want).
- Assets: one voice + one entrance line per round. Avatar optional (portrait fallback).
- Variants (free games, same code): "what's on the news?", "what does the
  note say?", "who does she call?", "what's in the box?"
- Advance: walk-ins become recurring cast; track entrances per character.

## 4. DUB THE CLIP

A silent/generic clip plays (reusable library: nature doc, security cam,
soap opera stare). Contestants improvise the dialogue — live mic or
quickfire TTS. Expressive mouth movement on the avatar sells it (visemes
from the audio we already time). Room votes the better dub.

- Input: live voice OR 1-tap quickfire lines fed to TTS.
- Assets: clip library (one-time), per-round audio only.
- Live-to-chat variant: stream the dub to chat, chat votes in real time.
- Advance: best dubs saved as clips; clip leaderboard persists.

## 5. COURT OF NONSENSE (jester trial, repeat format)

You and your friends are jesters at the Court of Nonsense. Each round,
write or prompt a set AS NONSENSE AS POSSIBLE — the goal is maximum
nonsense density, not sense. Scored on nonsense ratings; runs on our
standup logic (setup/punch/tag structure, pause ladder, delivery arcs —
but the material must be gloriously senseless).

- Nonsense rating (cheap, runs as code): non-sequitur rate, semantic
  distance per punch (Humicroedit/CHum insight: distance = funny),
  literalization count, callback-to-nothing rate. No GPU, no judge model.
- Input: 45–60s set (written or prompted + refined).
- Assets: standard standup render (voice + captions). Repeat format:
  weekly nonsense leaderboard, reigning Nonsense Champion defends.
- Advance: nonsense priors per player (their best mechanisms), champion
  gets a harder constraint next round (must include 3 random words).

## 6. LEAST FUNNY ANSWER (inverted game)

Question on screen. Everyone submits the LEAST funny answer they can.
Room votes for worst-best. Inverts taste calibration — and secretly
trains the judge on what unfunny looks like (golden negatives).

- Input: answer text (≤30 words).
- Assets: none. Pure text, fastest round in the pack.
- Scoring: most votes for "least funny" wins the round; track who is
  reliably unfunny (their "funny" answers get a handicap multiplier).
- Advance: winner's answer archived as judge-model negative.

## 7. TRY NOT TO SMILE (Mixamo + webcam + live minute)

Before the round, each player prompts a standup minute (their own
material or AI-assisted). Minutes play on the TV, one at a time. Players
on camera — first to smile loses. Smile detection watches the webcam
feed (omni vision frames at ~1fps, or a tiny local smile classifier;
Mixamo-rigged avatars mirror the room for the big screen).

- Flow: prompt minute → minutes queue → watch party on TV → webcam
  watches watchers → smile = elimination, last stone face wins.
- Input: minute prompt (premise + target + tone). Minutes pre-generated
  so playback never stalls.
- Assets: per-player minute audio; webcam frames (ephemeral, never stored);
  Mixamo avatars optional flavor (room mirrored as characters).
- Scoring: survival. Smile timestamp logged per minute = the minute's
  builder gets credit (their minute broke someone). Two leaderboards:
  best stone face + most lethal minute.
- Privacy: frames processed live, discarded. Consent per room, camera
  off = auto-spectator.

## 8. POWERPOINT KARAOKE

AI deals a cursed slide deck (chart with no axes, disappointed owl stock
photo). Contestant presents it deadpan, zero prep, 60 seconds. Phones vote.

- Input: none from players (deck is the prompt). Optional: audience
  picks the presenter + deck seed.
- Assets: 3–5 slides per round (image gen, one-time per deck, reusable).
- Advance: presenter Elo; deck retired after 3 uses.

## 9. TWO-HEADED EXPERT

Human + agent (or two humans) answer an audience question alternating
ONE WORD AT A TIME. Classic improv game; AI is hilariously bad-good at it.

- Input: audience question (phone). Live play, no generation.
- Assets: none. Transcript archived (great callback mine).
- Scoring: room votes per answer; track unbroken streaks (no hesitation).

## 10. EULOGY FOR A THING

Procedural Blender object rendered (free prop pipeline from #2).
Contestant delivers its eulogy — or its roast. 45 seconds.

- Input: none (object is dealt) or audience picks eulogy vs roast.
- Assets: one prop still per round.
- Advance: eulogist Elo; objects enter the memorial hall (gallery page).

## 11. GENRE SWAP

Same 4-line scene performed twice in different genres (noir vs nature
doc vs hostage negotiation). Delivery engine already swaps modulators;
the format frames it as a vote.

- Input: audience picks the two genres (phone vote from 4 dealt).
- Assets: two renders of one script (same audio timing, different direction).
- Advance: genre-pair records (which genres produce the funniest gaps).

## 12. WRONG ANSWERS ONLY

Question on screen. Everyone submits the worst answer. Vote for
worst-best. Pure text, infinite replayability, best phone game.

- Input: answer text (≤30 words).
- Assets: none.
- Advance: question deck grows from audience submissions (moderated);
  per-player worst-answer streaks.

## 13. HUMILIATION RITUAL (renamed — was Someone Else's Script)

The phone is a teleprompter with a cruelty setting. The ritual has three
decks for variety; every round draws from one (escalating cruelty through
the night):

- **ACT IT** (method/charades): a direction with no words — "grieve a
  parking ticket like it's a fallen comrade", "realize mid-handshake the
  hand is fake". Pure physical, 15 seconds.
- **SAY IT** (evil lines): words + manner — "read this breakup text like a
  weather report", "deliver this apology in an Australian accent to a
  houseplant". Written by friends, AI-sharpened on request.
- **BE IT** (possession): a 15-second state — "you are a GPS that has given
  up", "you are soup that achieved consciousness". The performer stays in
  it while the room throws one-line prompts at them.

The self-landing rule: dares CAN land on yourself. Drawing your own
script is not a pass — it's a double-or-nothing moment (glory pays 2×,
bottling it pays the room). Self-destruction is the bravest television.

- Flow: write (90s, simultaneous; AI-sharpen optional) → assign (shuffled,
  self-landing possible) → perform (directions on phone + big screen,
  webcam/avatar mirror on) → PASS/FAIL vote (did they commit?) →
  author-guess vote (Fibbage-style) → scores.
- The incentive matrix (every role scores every round — nobody can check
  out):
  - PERFORMER: pass vote pays big; self-landing pass pays 2×. Bottling it
    still pays the room a laugh — failure is content, never dead air.
  - AUTHOR: paid when their performer PASSES (good material is performable)
    + perfect-crime bonus (nobody guessed them). Cruel-but-doable is the
    meta; impossible directions starve their own author.
  - GUESSERS: split for correct author ID.
  - ROOM: "I CAUGHT THAT" callback button rides along — smuggled callbacks
    pay on top.
- Verification (no faking it): two layers. The room's PASS/FAIL vote
  disposes (human judgment, vibes count). Beneath it, the omni referee
  proposes: did they say the words? hold the accent? stay in the state
  the full 15s? Referee scores show on screen BEFORE the vote — the room
  can overrule, and overrules are the funniest arguments of the night.
  (Model proposes, humans dispose — house rule.)
- The cruelty economy: meanest direction per night tracked ("while
  maintaining aggressive eye contact with a houseplant"). Cruelty Hall of
  Fame persists. Authors who deal impossibilities get the Dunce Avatar.
- Assets: phones only (+ avatar mirror, shared with M1/M10). Humans are
  the renderers; omni is the referee. Cheapest physical-comedy format in
  the pack.

## 14. INTERNAL MONOLOGUE (the killer — real improv game "Little Voice")

One player is put in a situation (a frozen scene, their own ritual
performance replayed back, "your boss says 'we need to talk'"). The room
prompts their INTERNAL monologue: the voice in their head, in a dealt
style (noir narrator, nature documentary, auctioneer, sports commentator,
their own mother). Performed live via TTS in a contrasting voice while the
player must keep a straight face — displayed on screen as subtitles under
their webcam/avatar. The gap between the face and the voice IS the game.

- Stagecraft (stolen from the real game): the voice speaks only in the
  actor's pauses, never over dialogue. The actor cannot acknowledge the
  voice except physically (a flinch, a sip of water, a dying smile).
  Voice must deepen the situation, never derail it ("terrified of losing
  this friendship" yes; "secretly a spy" no). Best voices reveal genuine
  vulnerability, then twist it.
- Flow: situation dealt → room prompts monologues (style + 1 line each,
  simultaneous) → winner performed live over the scene (or over the
  replay) → room votes: funniest voice + best flinch (actor's physical
  tell).
- Situations deck: scene freezes, real party moments ("X just got roasted
  — internal monologue?"), confessionals replayed with hostile narration.
- Stone Face pairing: run it INSIDE M1 — the monologue is a weapon aimed
  at the stone faces. Surviving your own internal monologue read in your
  mother's voice is the final boss.
- Scoring: voice authors paid in votes; actors paid per suppressed smile
  (flinch without breaking = bonus); "I CAUGHT THAT" for callbacks
  smuggled into monologues.
- Assets: one TTS voice per winning monologue (contrasting voice ID,
  dealt style = prompt prefix); subtitles on screen; situation deck
  (content). Peep Show proved the TV grammar; we just let the room write it.

## 15. BODY RELAY (webcam physical games, three variants)
No words (or barely). Webcam + avatar mirror is the whole stage — avatars
exaggerate every move, so bad bodies make great TV. All three fit anywhere
as palate cleansers between word games.

- **POSE TELEPHONE:** player 1 holds a pose 5s (webcam captures, avatar
  mirrors). Player 2 sees ONLY player 1's avatar (not the human) and must
  reproduce it. Down the line; final pose vs first pose side by side.
  Degradation is the scoring — biggest drift wins "Most Traveled Pose".
- **STATUE GARDEN:** a prompt is dealt ("historians 300 years from now
  reenacting this party"). Everyone freezes simultaneously on the host's
  count. Omni referee + room vote: best statue, most committed, first to
  move (loser). Pairs with Stone Face (stillness league tables merge).
- **DANCE RELAY:** each player adds 5 seconds to a growing routine, in
  order, full routine replayed each turn. Last to reproduce the whole
  chain cleanly wins. Avatars perform it simultaneously in exaggerated
  unison — the mirror cast is funnier than the humans by round 4.
- Assets: webcams + avatar mirror (shared M1/M10/M13 infra). Pose capture
  = stills, not mocap — cheap by design. No generation, no TTS.
- Scoring: drift (telephone), commitment (statue), chain survival (dance).
  Losers' highlights auto-cut into the night edit.

## 16–19. MUSIC GAMES, COPYRIGHT-CLEAN

The unlock: we synthesize vocals and beats SEPARATELY (lyrics→TTS/sung
voice, style prompt→instrumental), so lyric×beat mixing is free — play any
vocal over any beat, swap either side, no stems or separation needed. The
browser mixes two audio elements; the stage mixes stems.

Copyright rules (the whole section lives inside these):
- Original lyrics + generated beats = clean, always. The default.
- Public-domain material only: folk, hymns, shanties, nursery rhymes,
  classical melodies (published 1929 or earlier as of 2026). No Beatles,
  no showtunes, no exceptions — the deck enforces it.
- Chord progressions, grooves, styles, genres are NOT copyrightable —
  only melody + lyrics are. "Same 4 chords, new song" is the legal sweet
  spot and a whole game (see #18).
- Parody has fair-use protection (Campbell v. Acuff-Rose) but the rooms
  don't rely on it: original/PD inputs keep every render shippable.

## 16. LYRIC × BEAT (the mixer)

Write original bars, then perform them over a dealt beat CONTRARY to
their content: love song over drill, eulogy over sea shanty, tax advice
over power ballad. Both sides generated clean (your words + style-prompt
instrumental). Room votes the most cursed combination.

- Flow: lyrics in (or dealt seed) → beats dealt (3 style prompts, room
  picks yours) → mix plays (vocal + instrumental together) → vote.
- Assets: lyrics (free text), beats ($0.05–0.15/track, cached — the beat
  library grows every night and never re-renders).
- Scoring: combination vote + lyric vote (split ballots: best words,
  best mismatch).

## 17. GENRE TRANSPLANT

One original lyric, N genres. Same words sung as noir jazz, gabber,
Gregorian chant, yacht rock. The lyric is fixed; the transplant is the
performance. Vote per round, transplant champion per night.

- Assets: one lyric + N instrumental renders (or N TTS direction passes
  for the $0 version — spoken-word genre parody with zero music spend).
- Scoring: per-transplant votes feed a genre leaderboard (which genres
  produce the funniest gaps — shared with #11 Genre Swap).
- **PD × GENRE night (the "Kumbaya as EDM" format):** slot machine deals
  a PD song × a modern genre (sailor shanty × UK drill, Kumbaya × EDM,
  nursery rhyme × gabber). Two leagues per round — FAITHFUL (same PD
  words, new beat) and CORRUPT (rewrite the lyric in the genre's voice).
  Flow: 5s music-box original → transplant performed (chant + beat mix
  live, $0) → vote → winner gets the FULL sung render (~$0.10, the prize
  budget) → archived to the songbook as a canonical transplant with
  share link. Every night grows a permanent, shippable, copyright-clean
  catalog — the highlights ARE the retention engine. First canonical
  entry, by acclamation: Row Row Row Your Boat, UK drill.

## 18. FOUR CHORDS (the legal sweet spot)

Everyone gets the same 4-chord loop (I–V–vi–IV, 12-bar, boom-bap) —
progressions can't be owned. Write an original song on it in 5 minutes:
any melody, any words. Same harmony, wildly different songs. The round
PROVES the law while being hilarious.

- Flow: loop dealt (one cached instrumental, reused all night) → write
  (5 min, phones) → perform (voice over the shared loop) → vote.
- Assets: ONE instrumental per night. Cheapest music format possible.
- Variants: same loop, forced topic ("the loop is joyful, your song is
  about parking fines"); key-change round (loop modulates mid-song,
  singers survive or don't).

## 19. PD JUKEBOX (name it / finish it / corrupt it)

Public-domain songbook only (shanties, hymns, folk, nursery rhymes —
deck-checked). Three games, one songbook:

- **Name That Hymn:** 5 seconds of melody (generated music-box render),
  name it. Speed round, streaks pay.
- **Finish It:** PD lyric stops mid-verse, room completes it wrong on
  purpose. Shared-prompt final shape.
- **Corrupt It:** keep the PD melody, rewrite the lyric about tonight's
  party (the roastomotiv: last night's callback winner becomes verse 2).
  Best corruption performed + archived; winners enter the songbook as
  authorized parodies of PD originals.

---

## 20–26. MUSIC ROUNDS (all M11, all deck + twist)

New shared mechanic: **SPEED-WEIGHTED GUESSES.** Guessing rounds pay by
speed — fastest correct gets most, decaying to a floor. Buzzer UX
(press-and-hold to lock, release to chicken out). Applies anywhere a room
guesses (liar hunts, walk-in IDs, soundscape matches).

## 20. GUESS WHO (carousel song)

Genre carousel spins, stops on one. Prompt: a person in the room (dealt
secretly, never named). Write + perform a 30s song about them IN that
genre. It plays; everyone locks in WHO. Quickest correct wins big,
slow correct wins small, wrong pays nothing.

- Flow: genre spin → secret subject dealt → write (3 min) → perform
  (chant + beat, $0) → lock-in race → reveal.
- Scoring: speed-weighted (1st = 100, decaying to 20 floor); subject gets
  10 per correct guesser (being known is its own prize).

## 21. INTERNAL SONG (feeling → track)

Dealt a tough emotion/situation ("told 'we need to talk' at 9am",
"rain, no umbrella, job interview in 20"). Your song must BE your
internal reaction — not describe it, embody it. The room feels it, then
votes: most felt wins. Internal Monologue's musical twin.

## 22. BREAK IT TO THEM (intervention song)

"What does this player need to hear?" Dealt a truth about someone in the
room (kind, or not). Break it to them IN A SONG. Sweetкод: the meaner the
truth, the sweeter the melody must be (deal the genre against the message).
Room votes: best delivery + bravest truth (split ballots).

## 23. SOUNDSCAPE SLEUTH (8 scenarios)

8 scenarios on screen. One player secretly gets scenario #N and builds
its ideal 30s soundscape (beat + texture + one vocal line, TTS/hummed).
Room guesses WHICH scenario. Wavelength meets sound design.

- Flow: scenarios dealt (visible all) → secret assignment → build (3 min)
  → play blind → lock-in race → reveal.
- Scoring: speed-weighted guesses; builder paid per correct guesser
  (clarity pays) + bonus if NOBODY gets it but the vote says it slapped
  (beautiful-but-opaque prize).

## 24. WALKOUT ROYALE (best entrance song)

A character (or player) is dealt. Each contender pitches + performs a
15s walkout song. Winner's song becomes their actual entrance music for
the rest of the night (played every time they score). Stakes compound.

## 25. DUB THE SCORE (movie scene music)

Silent/generic scene plays (soap stare, security cam, nature doc).
Contenders compose the score live (beat pick + direction: "ominous but
horny"). Best dub wins; winning score sticks to the clip in the library
(clips accumulate canonical scores — the library gets funnier forever).

## 26. More in the bloodline (backlog)

- **Tempo trap:** mid-song the beat halves/doubles; singers survive or
  drown. Last standing wins.
- **Lullaby for adults:** terrifying topic, soothing melody. Sweetest
  dread wins.
- **Mashup roulette:** two PD songs dealt, fuse into one. Best seam wins.
- **Silence tax:** one layer drops each verse (drums, then bass, then
  dignity). Keep performing. First to stop loses.
- **Wrong trailer:** mundane event (parking fine, dentist), epic score.
  Most disproportionate wins.

## 27–30. VOICE ROUNDS (lipsync + AI prompting)

House rule first: **only volunteered voices get cloned.** A player opts a
voice in (15s sample, Fish), and only opted voices enter any voice game.
Jokers can't clone the unknowing; the room can't either. Fictional + opted
voices only — the decks enforce it.

The tech unlock: our LipSync adapter already turns live audio into visemes
(analyser → mouth), so any voice performance drives any avatar for free.
Voice games are lipsync games with different prompt shapes.

## 27. DUB THE SCRIPT (lipsync showdown)

A script is dealt (or it's your own winning line from another round).
Perform it — your live voice drives the avatar's mouth in real time.
Variants: WRONG VOICE (your line, mismatched dealt voice — eulogy in a
game-show host), SAME LINE (everyone dubs one line, best delivery wins),
VOICE SWAP DEBATE (mid-argument your voices swap — argue as them, in
their opted voice; identity chaos, first to break loses).

- Scoring: delivery votes + sync bonus (omni referee: word accuracy via
  ASR — did you actually say the line?) + break penalties.
- Assets: opted voice IDs + LipSync drive (exists). $0 per round.

## 28. EARPIECE (AI-assisted cold read)

The director in your ear. AI feeds your next line live (earpiece text or
TTS whisper a beat before you speak) — you perform words you're reading
for the first time, inside a live scene you can't control. Comedy from
latency + commitment + the moments the line makes no sense and you sell
it anyway.

- Variants: WHISPER GAME (partner gets AI lines via earpiece, must smuggle
  them into natural conversation unnoticed — room spots the plants);
  HOSTILE PROMPTER (the prompter is trying to break you; surviving 60s
  wins); TRANSLATOR (you speak gibberish with total conviction, partner
  "translates" deadpan — the room votes the translation).
- Scoring: commitment votes (never broke) + spot-the-plant (whisper game)
  + best save (worst line, best sell).
- Assets: live line feed (text models, pennies) + earpiece (player's own
  phone + bud). The cheapest AI-in-the-loop format: one inference per line.

## 29. VOICE ROULETTE + ACCENT LADDER

Every line you speak arrives in a randomly dealt opted voice (roulette) —
hold a conversation while your voice betrays you. Ladder variant: each
round ADDS an accent/emotion constraint (joyful + Australian + whisper);
last intelligible performer standing wins, omni referee judges
intelligibility via ASR match rate.

- Scoring: survival rounds (ladder) or delivery votes (roulette);
  intelligibility floor enforced by referee (below 50% match = out).
- Assets: opted voice pool + constraint deck. $0.

## 30. AUDIO TELEPHONE + AUCTIONEER (accuracy games)

- **Audio Telephone:** TTS whispers a line to player 1's earpiece; they
  repeat what they heard aloud; chain to the end. Human-ASR degradation
  scored like pose telephone (drift wins "most traveled line").
- **Auctioneer:** read the terms & conditions (or tonight's callback
  list) as fast as possible; omni ASR verifies word accuracy; fastest
  clean read wins. Speed + precision, one dial each.
- **ASMR vs DEATH METAL:** same text, opposite delivery genres, room
  votes. The contrast IS the game (delivery-contrast engine, shared with
  Wrong Emotion: eulogy joyful, love song furious — Jev deals the mismatch).

## 31–34. CLONED-VOICE GAMES (opted voices only)

Design principle: **system randomness authors, humans commit.** Independently
random voice × line × emotion collides into moments no writer would pitch
(nan reading drill lyrics). Authored jokes are the fallback; the slot
machine is the headliner. All games require opted-in voices (15s sample,
per-night consent, per-line kill switch where another human drives).

## 31. VOICE LOTTERY (the slot machine)

Three reels spin: WHOSE VOICE × WHAT LINE × WHAT EMOTION. All independent,
all random. You perform the collision cold. Nan × drill verse × furious.
The room votes commitment (did you sell the unsellable?).

- Flow: spin (public, big screen) → 10s stare → perform → vote.
- Scoring: commitment votes + "most cursed combo" side prize (room
  nominates the spin itself — the machine gets credit).
- Assets: opted voice pool + line deck (room-written filth welcome) +
  emotion deck. $0 (TTS only).

## 32. DRIVE MY VOICE (possession)

Opt-in toggle: "let X drive my voice this round." They type, YOUR clone
speaks — through your avatar, on the big screen, in front of everyone.
Per-line kill switch (one tap repossesses your voice). Driver scores for
chaos caused; owner scores for composure kept.

- Variants: CHAIN POSSESSION (A drives B drives C — telephone with
  bodies); HOSTILE TAKEOVER (Jokers prize: 60 seconds in someone's voice).
- Scoring: chaos votes (driver) + composure votes (owner) — split
  ballots, both winnable.
- Safety: opt-in per round, kill switch always visible, room-authored
  lines pass the family filter when set. Revocation is instant and total.

## 33. CONFESSIONS OF YOU (room-authored sins)

Your clone confesses things you'd never say — written by the room about
you (kind, mostly). EULOGY BY THE DECEASED (your clone buries you),
SLEEP TALK (your voice reveals what you "said in your sleep"), ALIBI
(your voice alibis you for something the room just convicted you of).

- Flow: accusation/confession prompt → room writes 1 line each about the
  target → best performed by target's clone (target must sit stone-faced
  through their own sins — Stone Face pairing) → vote.
- Scoring: sin votes (best line) + composure (target's face) — two boards.

## 34. More in the bloodline (backlog)

- **Wrong number:** your clone leaves a voicemail for the wrong person
  (dealt). Room hears both sides.
- **Last words:** your clone delivers your last words. You object in your
  real voice. Argument ensues (both voices, one body).
- **Acceptance speech:** your clone accepts an award you didn't win, thanks
  people you hate, cries on cue. Grace under pressure, scored.

---

## Shared infrastructure (build once, all formats reuse)

1. **Freeze/prompt/perform/vote loop** — the mode skeleton (create/input/views/advance).
2. **Fish TTS voice stack (the voice backend, everything speaks through it)** —
   `s2.1-pro-free` ($0, same SOTA model, Fair Use) default; paid fallback
   $15/1M bytes (≈$0.75 for a whole 50k-char party night). Per-beat emotion
   cues + emphasis tags, exact pause stitching. Voice cloning from 10–30s
   samples (persistent IDs for cast, instant clones for one-offs like
   Internal Monologue contrasting voices). 83 languages. Serves every
   format with audio.
3. **Procedural Blender prop renderer** — prompt adjectives → primitives +
   materials → one still. Serves #2, #7 (memorial), #10.
4. **Music render routing (M11)** — lyrics via text models (free); full
   songs $0.05–0.15/track via aggregator APIs (Suno-class) or MiniMax
   Music 3 open weights (self-host, attribution). One sung render per
   night max (champion's prize). Walkouts + intro stings: generate once,
   cache forever (freaktown pattern).
5. **Nonsense rater (code, no model)** — non-sequitur rate, semantic
   distance, literalization count. Serves #5, doubles as judge negatives (#6).
6. **Webcam smile signal** — omni frames or local classifier, live-only,
   never stored. Serves M1.
7. **Callback mine** — every losing ending, walk-in, transcript archived
  with tags; resurfaces as future prompts. Serves #1, #3, #9.
8. **Onboarding: photo + voice + adjectives = contestant** — selfie →
   portrait/avatar (three.ws GLB or portrait fallback + avatar.json
   capability contract); 15s audio → Fish clone; 3 adjectives → walkout
   sting + persona seed. Renderer-independent packs mean video rigs slot
   in later without touching content.

## Honest tech notes (don't oversell)

- **Mixamo = bodies, not faces.** Auto-rig + mocap retarget for gesture;
  faces are ARKit blendshapes / VRM expressions / viseme jaw. Portrait
  fallback until rigs exist. The avatar.json capability contract already
  degrades gracefully — new renderers slot in, content never changes.
- **Video: deferred, deliberately.** Nothing today beats the cost curve;
  packs stay renderer-independent so whatever lands (Wan-class, HappyOyster-
  class, browser puppet) plugs into the same delivery.json beats.
- **Fish free tier is Fair Use, not a contract.** Paid fallback is pennies
  per night — budget $1/night and never think about it again.
