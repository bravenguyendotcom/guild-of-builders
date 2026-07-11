# 🥋 Mission 009 — The Vault

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

Two locks. One door. No way around it.

First the vault checks your password — long enough, and not something silly.

Get past that, and it makes you *crack the combination,* one guess at a time.

You've stood at both of these locks before. Just never stacked on top of each other.

Tonight you pick them both.

---

## 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Open **`challenge_1.py`**.

Type it out. Run it. Try a silly password first, then a real one — then crack the combo.

Any error is *probably your own typo* — hunt it, fix it, smile.

### Expected output

```
Vault password: abc
Too short. The vault won't even listen.
```

```
Vault password: password
Really? 'password'? The vault laughs at you.
```

```
Vault password: dragon-tea-42
Combination (1-20): 10
Lower.
Combination (1-20): 5
Higher.
Combination (1-20): 8
CLUNK! The vault opens in 3 tries.
```

*(The top half is the bouncer from Chapter 7. The bottom half is the guessing game from*
*Chapter 6. Nothing here is new — that's the point. You already own both halves.)*

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

Same vault — but **three typos** slipped in. No logic is broken. Only fingers.

Fix one, run again, and the next clue steps forward. Keep going until the vault opens clean.

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 7
    password = input("Vault password: ")
IndentationError: unexpected indent
```

**Excellent. Now the conversation begins.** 🦑

---

## CS Seeds

`len()` / `==` check *(echo 002)* · `while` / `!=` / counter / `random` *(echo 001)* · `integration`

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Sir Boolean guards the top lock; the Cave guards the bottom. Old friends, one door.

Professor Quackers says nothing. Professor Quackers never does. 🦆

---

## Related Missions

This is **Mission 002 and Mission 001, working the same door.**

The bouncer checks you in; the guessing game makes you earn the treasure.

*Coming next: everything you've built, tied together with a single menu.* 🗝️

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 009 · `Title:` The Vault · `Type:` 🔁 **Composite Echo of Missions 001 + 002** (D-23) ·
`Engine:` `coding_gold_mine/009_vault.py` — *new combined code.* Unlike Mission 006 (which reused
Engine 001 verbatim, no new file), the Vault is a new canonical program that composes the two
echoed engines, so under D-21 it lives as its own engine. *Flagged for the log: this adds an engine
the backlog listed as "`001`+`002` skin."*
· `CS Seeds:` len/== (echo 002); while/!=/counter/random (echo 001); integration
· `Prerequisites:` Chapters 6 + 7 (all skills already owned) · `Tiers shipped:` I–II
· `Related:` Missions 001, 002; leads into Mission 010 (capstone console).

**Tier II typo palette (D-28), adapted for an Echo (see note).** Three *distinct* categories, two
fresh vs Mission 008 (keyword / function-name / variable); three distinct error types:
1. **Indentation slip (common):** a stray leading space on `password = input(...)` (line 7) —
   `IndentationError: unexpected indent` (the first clue).
2. **Operator/symbol slip (echoed-guesser signature):** `!=` → `=!` on `while guess =! secret:` —
   `SyntaxError: invalid syntax`.
3. **Function-name slip (echoed-bouncer signature):** `len` → `lenn` on `if lenn(password) < 8:` —
   `NameError: … Did you mean: 'len'?`.

**Bash-verified cascade:** IndentationError (line 7) → SyntaxError (`=!`) → NameError (`lenn`) → clean
run. Fixing exactly the three reproduces `challenge_1.py` byte-for-byte; the fully-fixed file
compiles clean.

**On "new surface" for Echo missions (open canon question, second occurrence).** An Echo (D-23) has
no new Python surface, so the D-28 "two typos on the chapter's new surface" clause is read here as
**"two typos on the echoed engines' signature surfaces"** (the bouncer's `len`, the guesser's `!=`).
This is the same adaptation used in Mission 006. *Still recommend locking it as a one-line D-28
addendum — it applies again at Mission 010.*</sub>
