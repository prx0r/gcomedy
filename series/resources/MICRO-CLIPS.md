# MICRO-CLIPS — extreme examples per technique

> Signature moments: the longest pauses, fastest delivery, biggest callbacks.
> Each has a YouTube embed URL. Sources: measured timing data + transcript search.

## EXTREME PAUSES (the signature holds)

| Pause | Comedian | Set | Timestamp | What happens | Video |
|---|---|---|---|---|---|
| **31.24s** | Stewart Lee | Comedy Vehicle S1E5 | t=48s | Opening — room settles into silence | [OXo5_ihFkA0](https://youtube.com/watch?v=OXo5_ihFkA0) |
| **20.28s** | Stewart Lee | Comedy Vehicle S1E6 | t=38s | Religion setup — extended hold | [-SQIfEwAkcw](https://youtube.com/watch?v=-SQIfEwAkcw) |
| **15.67s** | Stewart Lee | Comedy Vehicle S1E4 | t=447s | Financial crisis — post-punch hold | [search: lee financial crisis] |
| **11.88s** | Stewart Lee | Comedy Vehicle S1E6 | t=249s | Religion — mid-bit silence | [-SQIfEwAkcw](https://youtube.com/watch?v=-SQIfEwAkcw) |
| **10.00s** | Simon Amstell | Do Nothing Live | t=40s | Opening — first laugh delayed | [K4mH6E0hMbI](https://youtube.com/watch?v=K4mH6E0hMbI) |
| **8.16s** | Louis CK | Road Rage | t=187s | The confession hold — "I don't like doing that" | [auHzTfeF64Y](https://youtube.com/watch?v=auHzTfeF64Y) |
| **4.40s** | Daniel Sloss | socio-2021 | t=521s | Post-reveal hold | [4ppYdCzLEJQ](https://youtube.com/watch?v=4ppYdCzLEJQ) |

**Why these matter for the overlay:** the 31s Lee hold is the extreme edge of gap-mode.
The 8.16s Louis hold is the Goldilocks confession moment. The 1.7s Norm hold is the anti-joke
beat. These three pauses span the entire timing spectrum.

## EXTREME SPEECH RATES

| Rate | Comedian | Style | Mode | Video |
|---|---|---|---|---|
| **192 wpm** | Norm Macdonald | Never-stop | Overlap | [RA0UjWA9iWU](https://youtube.com/watch?v=RA0UjWA9iWU) |
| **177 wpm** | Daniel Sloss | Energetic confessional | Overlap | [4ppYdCzLEJQ](https://youtube.com/watch?v=4ppYdCzLEJQ) |
| **171 wpm** | Louis CK | Confessional storyteller | Both | [auHzTfeF64Y](https://youtube.com/watch?v=auHzTfeF64Y) |
| **155 wpm** | Simon Amstell | Soft confessional | Gap | [K4mH6E0hMbI](https://youtube.com/watch?v=K4mH6E0hMbI) |
| **123 wpm** | Stewart Lee | Slow build meta | Gap | [7oyfkqD4UP8](https://youtube.com/watch?v=7oyfkqD4UP8) |
| **117 wpm** | Stewart Lee | Slowest measured | Gap | [-SQIfEwAkcw](https://youtube.com/watch?v=-SQIfEwAkcw) |

**The rate spectrum:** Norm (192) → Louis (171) → Amstell (155) → Lee (117).
Fast comics live in overlap mode. Slow comics live in gap mode. The rate IS the mode.

## MICRO-TECHNIQUES FOUND IN CORPUS

| Technique | Examples | Comedians | Example quote |
|---|---|---|---|
| rule of three | 1104 | 114 | "Like… [groans] And I’m like, “Whatever do you mean, Papa?” [laughter] And he goe..." |
| the turn | 696 | 113 | "[laughter] That actually sounds like a fucking nightmare.” [laughter] Admittedly..." |
| audience alignment | 355 | 102 | "Can we all agree that that is the worst age in the human existence?..." |
| antithesis | 322 | 96 | "Not my boots!” But I was thinking it, right?..." |
| timing cue | 234 | 89 | "I can’t wait to go vacation somewhere tropical, like the Arctic...." |
| callback marker | 118 | 59 | "[laughter] Remember when you were a kid and you would, like, open up a present, ..." |
| defamiliarize | 95 | 54 | "I don’t know what this is, but… What if this is sign language?..." |
| escalation list | 66 | 42 | "And then I bought a mattress and then it all went away.” It’s the same shit...." |
| concession then pivot | 32 | 26 | "Everything else I do is fine, but I have a f*cking temper and it just ruins sh!t..." |
| premise clarity | 26 | 22 | "The problem is you keep amping this thing up, getting that Mike singletary look ..." |
| repetition variation | 22 | 19 | "And I’m stoned, and they throw this dude on the TV, and it zoomed in on his face..." |
| absurd grounding | 5 | 5 | "I don’t know how to tell you this, but… your penis has been in my mouth.” [audie..." |

## EXTREME CLIP URLS (per technique)

- **lee 31s pause**: [Stewart Lee vs his Audience](https://youtube.com/watch?v=OXo5_ihFkA0) (71s)
- **lee religion**: [Stewart Lee Comedy Vehicle  - 1.6 Religion](https://youtube.com/watch?v=-SQIfEwAkcw) (1745s)
- **lee dead mouse**: [Stewart Lee Comedy Vehicle - Dead Mouse](https://youtube.com/watch?v=QXiiq1EUr7Q) (1749s)
- **amstell 10s**: [Simon Amstell - Do Nothing Live](https://youtube.com/watch?v=K4mH6E0hMbI) (3638s)
- **louis 8s**: [SHOTS FIRED AFTER MASSIVE FIGHTS AT MALL | Del Amo Mall, Tor](https://youtube.com/watch?v=ZggO2ZnQtY4) (252s)
- **norm fast**: [dos minutos of CLASSIC NORM DELIVERY](https://youtube.com/watch?v=RA0UjWA9iWU) (141s)
- **sloss**: [Daniel Sloss: SOCIO](https://youtube.com/watch?v=4ppYdCzLEJQ) (4396s)
- **rock tamborine**: [Jazzedelics Montage](https://youtube.com/watch?v=Ml2AuOCtvAk) (317s)
- **mulaney**: [John Mulaney Got Cheated Out of $120K | Netflix Is A Joke](https://youtube.com/watch?v=aiqKK4ysI7g) (302s)
- **carlin seven**: [George Carlin - 7 dirty words (best part)](https://youtube.com/watch?v=vbZhpf3sQxQ) (588s)

## WHAT THE OVERLAY CAN NOW SHOW

1. **Pause timer** — fires on every beat with pause_after >= 0.6s
2. **Hold sphere** — radius scales with pause duration (8.16s Louis = large sphere)
3. **Speed bar** — wpm per beat, colored by mode (overlap=green, gap=red)
4. **Laugh markers** — onset timestamps from transcript [laughter] markers
5. **Function labels** — SETUP/PUNCH/TAG/CALLBACK/BUTTON firing per beat
6. **Technique callouts** — rule-of-three counter, callback arrow, turn detector

## SOURCES

- Measured timing: funnygraph known_bits (39 pauses >=3s)
- Speech rates: 14 measured sets (117-192 wpm range)
- Micro-techniques: 2,971 examples across 119 characters2 transcripts
- Video URLs: yt-dlp search (free, no quota)