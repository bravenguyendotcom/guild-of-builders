# 🥋 Mission 001 — Guess the Number

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

Captain Byte hid a number in a chest —

somewhere from **1 to 100** — then forgot it.

(Of course he did.)

Now the chest only says two things: **"Too low."** and **"Too high."**

Type the little machine that cracks it open.

---

## 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Open **`challenge_1.py`**.

Type it out. Run it. Play your own game.

Any error is *probably your own typo* — hunt it, fix it, smile.

You don't have to understand every line yet. You will.

### Expected output

The secret is random, so your game won't match this one exactly —

but it will *feel* like this:

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

*(Ask Dragon Debug's riddle later: what's the **fewest** guesses that can always win?)*

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

It's the same machine — but **three typos** slipped in.

No logic is broken. Only fingers. Retype it, run it, and fix each slip until it runs clean.

Run it once and Python hands you your first clue:

```
NameError: name 'secrit' is not defined. Did you mean: 'secret'?
```

**Excellent. Now the conversation begins.**

Two more are hiding. Find them the same way. 🦑

---

## CS Seeds

`while-loop` · `!=` · `random.randint` · `counter pattern` · `loop exit` · `reading a traceback`

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Somewhere in the rafters, The Tangle uncurls one lazy tentacle,

sniffing for sloppy typing — and finds none. It gets bored and drifts off.

Professor Quackers says nothing. Professor Quackers never does. 🦆

---

## Related Missions

- **Chapter 6 — The Secret Treasure** (where you first *met* this machine).
- *Coming later:* the same idea in a new costume — a dragon searching a spellbook.
  *(Wait — haven't I done this before?)*

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 001 · `Title:` Guess the Number · `Engine:` `coding_gold_mine/001_guess_the_number.py`
· `CS Seeds:` while · != · random.randint · counter · loop-exit · traceback-reading
· `Prerequisites:` Chapter 6 (`while`, `random`) · `Tiers shipped:` I–II · `Related:` Ch 6; future Binary-Search skins.</sub>
