# 😄🧩🎨 GUILD_EXTRAS_SOURCE.md

### The distilled extras catalog — read THIS, never the raw brainstorm again

> **Status:** SOURCE catalog (distilled, not the final content). Purpose: the raw material for
> the Guild Extras (D-34), pulled out of the 1,485-line Gemini brainstorm into one tight line
> each, so a writer never re-reads the transcript 50 times.
> **How to use:** pick the item that fits a chapter's topic, then **write it fresh in our voice
> and cast** (D-19/D-34) — never paste the source. The line here tells you the *gag/mechanic* and
> the *re-skin*; the actual jokes/riddles/art get composed clean, in-Guild.
> **Rotation (D-34):** 😄 Joke → 🧩 Riddle → 🎨 Art, one per chapter from Ch 1.

---

## Re-skinning key (foreign → ours) — apply everywhere

| Source character (Gemini) | Re-skin to (ours) |
|---|---|
| Monty the Python (snake) | drop the "snake" framing; if a host is needed use **Maestro Monty** (showman) or **Dragon Debug** |
| Glitch / Lord Glitch (gremlin) | **Bug Monster** (external, friendly) or a **Fog Creature** (if inner) |
| Dunder the Dragon | **Dragon Debug** |
| Pip the Penguin | drop, or **Ninja Cat** |
| Cal the Calculator / Dr. Byte-Size | drop; use **Sir Boolean** (logic) or **Pycasso** (art) |
| Prf. Pycasso | **Professor Pycasso** (already ours) — saying: *"Every child is an artist, every terminal is a canvas."* |
| generic "rubber duck" | **Professor Quackers** |

**Never import foreign names. Public-domain programmer jokes are fine, rewritten in our voice.**

---

## 😄 JOKES (short, no code — for Joke slots)

*One-liners; pick and polish to our voice. CS topic in brackets = what it quietly reinforces.*

- **J01** — A byte is a Python's favorite snack. [data sizes]
- **J02** — Programmers prefer the dark because light attracts bugs. [bugs]
- **J03** — Python is like a very clean room: one thing out of place and the whole system screams. [indentation]
- **J04** — Variables are cardboard boxes: put anything in, label it what you like. [variables]
- **J05** — A guitar string and a Python string both love to be joined (concatenated). [strings]
- **J06** — 7 broke up with 3 because 7 % 3 left a remainder and it felt too crowded. [modulo]
- **J07** — Index [0] goes first in line — in Python land we count from zero. [indexing]
- **J08** — Why programmers are bad liars: their errors always print in bright red. [error output]
- **J09** — The forest was full of logs, so that's where the programmer went. [logs/debugging]
- **J10** — Real programmers count from 0. [indexing]
- **J11** — To understand recursion, you must first understand recursion. [recursion]
- **J12** — The glass isn't half full or empty — it's twice as large as it needs to be. [efficiency]
- **J13** — A snake's favorite jewelry: a neck-list (list). [lists]
- **J14** — What did the string say to the integer? "Look at all the letters I have!" [types]
- **J15** — The computer was cold because it left its Windows open. [pun / OS]

---

## 🧩 RIDDLES (interactive "run it → reveal the punchline" — for Riddle slots)

*Each is a tiny runnable program whose output IS the joke. Re-skin, keep it one-screen, show
expected output. Topic = the concept it teaches by osmosis.*

- **R01 The Infinite Loop** — a `while True` counts to a target then `break`s to reveal the punchline. [while/break]
- **R02 The Secret Decoder** — index into a string (`word[0]`, `word[2]`…) to spell the answer. [strings/indexing, 0-based]
- **R03 The Remainder Mystery** — `input()` a number, `% 12`, branch on the leftover. [modulo/input]
- **R04 The Lunch Box** — `.append()` to a list to "double the snake's size." [lists/append]
- **R05 The Joke Machine** — a `def` that must be *called* to run ("called by its friends"). [functions]
- **R06 The Honest Guard** — booleans (`is_lying == False and has_cookie == True`) open the punchline. [booleans/and]
- **R07 The Fork in the Road** — `if/elif/else` on LEFT/RIGHT input picks the joke. [conditionals]
- **R08 The Bug Exterminator** — loop a list, `if "Error" in bug` → squish it. ["in", loops]
- **R09 The Wizard's Chest** — a dict; guess the key to unlock the value. [dicts]
- **R10 The 0.1+0.2 Surprise** — float math ≠ 0.3, reveals the "lost point" gag. [floats]
- **R11 The Ghost Variable** — `None`; `if x is None` → "BOO, nothing here." [None]
- **R12 The Type Scanner** — `type()` a value, branch on `str`/`int`. [types]
- **R13 The Shout String** — `.upper()` turns a whisper into a shout. [string methods]
- **R14 The Safety Net** — `try/except ZeroDivisionError` catches 10/0. [exceptions]
- **R15 The Error Decoder** — a function that explains SyntaxError/NameError/TypeError kindly. [reading errors]
- **R16 The Break Train** — a runaway `while` loop; type STOP to `break`. [while/break/input]
- **R17 The Laughter Multiplier** — `"Ha!" * n` shows string repetition. [string * int]
- **R18 Decomposition Cake** — call `take_a_bite()` 3× to "eat" a big problem. [decomposition/CT]
- **R19 Pattern Footprints** — loop a list of L/R steps, spot the repeat. [pattern recognition/CT]
- **R20 The Gas Pedal** — a `def` hides the messy math; you "just drive." [abstraction/CT]
- **R21 The Shoe Algorithm** — steps out of order = socks on your ears. [algorithm order/CT]
- **R22 The Typo Hunt** — a `NameError` from `my_power_lever` vs `my_power_level`. [debugging/CT]
- **R23 The Lazy Genius** — `1234567 * 9876543` in a blink → "math is a cheat code." [why-math/big multiply]
- **R24 The Fortune Teller** — `(level > 3) and has_sword` predicts the fight. [logic + comparison]
- **R25 The Army Spawner** — `10 ** 4` clones an army → multiplication as power. [exponents/scale]
- **R26 The Jump Math** — change `y` coordinate to make a character "jump." [coordinates]

---

## 🎨 CODE ART (Run it → Hack it → Own it — for Art slots)

*Each gives a small runnable engine with "knobs" the child changes to make it theirs (never
copy-to-mimic, D-34). Show expected output. Topic = the math/loops it teaches.*

- **A01 The Triangle Spark** — `print` 3 lines of `*` → grow it into a tree/rocket. [print/shape]
- **A02 The Wallpaper Lever** — `MY_PAINT = "❀"; print(MY_PAINT * 10)` → change one variable, repaint all. [variables/string*]
- **A03 The Block Monster** — loops + spacing math build a boxy monster; eyes placed by math. [loops/layout]
- **A04 The Pyramid Builder** — `"#" * (floor*2)` with spaces → a stepped pyramid. [loops/multiplication]
- **A05 The Wavy Snake** — a `wave_pattern` list of indents + `time.sleep` = motion. [lists/animation]
- **A06 The Abstract Art Generator** — nested loops + `random.choice(symbols)` = a grid masterpiece. [nested loops/random]
- **A07 The Code Cat** — 3 string variables (ears/eyes/mouth) → a CLI cat; remix the face. [strings/variables]
- **A08 The Pixel Puppy** — 4 string lines → a CLI dog; hack the ears/nose. [strings/variables]
- **A09 The Alien Inventor** — modular parts (horns/eyes/mouth/legs) to mix into your own alien. [variables/creativity]
- **A10 The Glitch-Art Canvas** — 3 "levers" (symbol/width/speed) disrupt a wave into chaos-art. [variables/animation]
- **A11 The Exploding Star** — change `BOOM_FACTOR` to scale a `*` starburst. [math scaling]
- **A12 The World Generator** — random sky + ground lists build a landscape scene. [random/lists/CT]
- **A13 The Word-Pool Spell** — 3 lists + `random.choice` combine into a silly spell/poem. [lists/random]
- **A14 The Moving Canvas** — a `wave_steps` list + `time.sleep` animates a brush; change rhythm/speed. [animation/lists]

---

## Coverage note & the ~50-chapter math

- **This catalog: 15 jokes + 26 riddles + 14 art = 55 items** (the ~44 headline ideas plus close
  variants distilled from the brainstorm). Comfortably covers a ~50-chapter rotation with room to choose.
- **Advanced 3D/motion art** (Matrix Rain, Rocket, Moon, Starfield, Sphere, Donut) is **separate**
  — it lives in `PYCASSO_GALLERY_ADVANCED.md` (skill-gated, later volumes), NOT in this rotation.
- **The rotation is Joke→Riddle→Art from Ch 1** (D-34). Match each pick to the chapter's topic
  where possible (e.g. a modulo joke near the modulo chapter) — distribute *mindfully*, not blindly.
- **Grows like the Dojo:** more extras can be added over time; this is the seed catalog, not a cap.

> Next: the **build kit / Sonnet prompt** (a separate donut) points writers at this file so they
> compose each extra fresh in our voice — never re-reading the raw brainstorm.
