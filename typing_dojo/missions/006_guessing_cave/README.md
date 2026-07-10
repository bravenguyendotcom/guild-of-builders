# 🥋 Mission 006 — The Guessing Cave

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

*"Laaadies and gentle-Builders!"* Maestro Monty throws back the curtain.

*"Behold — the Cave of a Thousand Secrets! It hides a number between 1 and 100,*

*and it will yield to NO ONE!"*

Sir Quizzalot nods gravely. *"A challenge of unthinkable difficulty. I, personally, have never—"*

He stops. He squints at it. So do you.

*Haven't we... met this cave before?*

---

## 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Open **`challenge_1.py`**.

Type it out. Run it. Play a round or two against the Cave.

Any error is *probably your own typo* — hunt it, fix it, smile.

### Expected output

The Cave picks a new number each time, so your game won't match this one exactly —

but it will *feel* like an old friend:

```
Guess my number (1-100): 50
Too high.
Guess my number (1-100): 25
Too low.
Guess my number (1-100): 37
Too low.
Guess my number (1-100): 43
Too high.
Guess my number (1-100): 40
Too low.
Guess my number (1-100): 41
Too low.
Guess my number (1-100): 42
You got it in 7 guesses!
```

*(If your fingers already knew where this was going — that's the whole point.*
*You didn't just learn this game once. You* **kept** *it.)*

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

Same Cave — but **three typos** slipped in. No logic is broken. Only fingers.

Two of them will stop the program cold, and Python will point right at them.

The third won't. It runs just fine and still isn't spelled the way you'd spell it.

Retype it, run it, fix what you find — and don't stop at two.

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 11
    whlie guess != secret:
          ^^^^^
SyntaxError: invalid syntax
```

**Excellent. Now the conversation begins.** 🦑

---

## CS Seeds

`while-loop` · `!=` · `random.randint` · `counter pattern` · `loop exit` · *recognition*

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Sir Quizzalot: *"A true knight never guesses. ...He guesses* **boldly.** *Fifty!"* (It was too high.)

Professor Quackers says nothing. Professor Quackers never does. 🦆

---

## Related Missions

You've stood in this cave before — it was a treasure chest, back in Chapter 6.

Same machine, new costume. That flash of *"wait, I know this"* **is** computer science.

*Coming later: the Cave grows a door, and a bouncer, and asks for both at once.* 🗝️

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 006 · `Title:` The Guessing Cave · `Type:` 🔁 **Echo of Mission 001** (D-23) ·
`Engine:` `coding_gold_mine/001_guess_the_number.py` (reused unchanged — no new engine).
· `CS Seeds:` while · != · random.randint · counter · loop-exit · recognition
· `Prerequisites:` Chapter 6 (`while`, `random.randint`, counter) — all prior skills · `Tiers:` I–II
· `Related:` Mission 001 (its origin); future Vault echo (009).

**Tier II typo palette (D-28), adapted for an Echo — see the note below.** Categories fresh vs
Mission 005 (function-name + indentation) and vs Mission 001's originals (`secrit`/`imput`/`pirnt`):
1. **Keyword slip:** `while` → `whlie` (line 11).
2. **Name slip (throws):** `random.randint` → `randon.randint` (line 7); `import random` left correct.
3. **Variable-name slip (consistent, cosmetic):** `attempts` → `attemps` at all three uses (lines 9,
   13, 19) — bash-confirmed to run clean **and** correct on its own, per the D-28 guardrail.

**Bash-verified cascade:** first `SyntaxError: invalid syntax` (line 11, `whlie`); then
`NameError: name 'randon' is not defined. Did you mean: 'random'?` (line 7); then a clean, correct
run (the `attemps` slip is silent). Fixing exactly the three reproduces `challenge_1.py` byte-for-byte.

**On "new surface" for Echo missions (author note / open canon question):** an Echo (D-23) reuses a
prior engine and by definition has *no* new Python surface. This mission therefore reads the D-28
"two typos on the chapter's new surface" clause as **"two typos on the echoed engine's signature
surface"** (the guessing-loop machinery this mission drills). All three typos here land on that
signature surface. *Recommend locking this as a one-line D-28 addendum so every future Echo (009,
010, and the Volume II+ echoes) is unambiguous.*</sub>
