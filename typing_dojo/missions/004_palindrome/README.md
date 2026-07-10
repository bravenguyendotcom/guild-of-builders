# 🥋 Mission 004 — Mirror, Mirror

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

The Mirror only opens for one kind of word —

one that reads the same forwards and backwards.

There's no shortcut. No `.reverse()` — strings don't carry one.

You build the reflection yourself, one letter at a time,

and let the Mirror judge what you made.

---

## 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Open **`challenge_1.py`**.

Type it out. Run it. Try a few words of your own.

Any error is *probably your own typo* — hunt it, fix it, smile.

### Expected output

```
Say a word for the Mirror: level
level is a palindrome. The Mirror agrees with itself.
```

```
Say a word for the Mirror: dragon
dragon is not a palindrome.
```

```
Say a word for the Mirror: kayak
kayak is a palindrome. The Mirror agrees with itself.
```

*(Watch `reversed_word` grow backwards — each new letter stacked in front*
*of the last. The same walk-it-one-at-a-time move as Chapter 8's pile,*
*only now it's walking letters.)*

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

Same Mirror — but **three typos** slipped in. No logic is broken. Only fingers.

Two of them will stop the program cold, and Python will point right at them.

The third won't. It runs just fine and still isn't how this chapter spelled things.

Retype it, run it, fix what you find — and don't stop at two.

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 8
    fro letter in word:
        ^^^^^^
SyntaxError: invalid syntax
```

**Excellent. Now the conversation begins.** 🦑

---

## CS Seeds

`string iteration` · `string concatenation` · `==` comparison · `palindrome check`

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

The Mirror never blinks, never rushes, never grades a word twice.

Professor Quackers says nothing. Professor Quackers never does. 🦆

---

## Related Missions

Chapter 9 is where you first met the Mirror.

Mission 003 walked a pile; this one walks a word — same move, new costume.

*Coming later: one letter, shifted just a little... and a secret appears.* 🗝️

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 004 · `Title:` Mirror, Mirror · `Engine:` `coding_gold_mine/004_palindrome.py`
· `CS Seeds:` string iteration · string concatenation · == · palindrome check
· `Prerequisites:` Chapter 8 (`for` loop, walking a sequence one item at a time)
· `Tiers shipped:` I–II · `Related:` Ch 8 tally loop; future cipher engine (005).

**Tier II typo palette (D-28) — three categories, two on Ch 9's new surface, none repeating a
prior mission:**
1. **Keyword slip (new surface):** `for` → `fro` on the string-walk loop (line 8).
2. **Variable-name slip (new surface, cosmetic):** `reversed_word` → `reversd_word`, misspelled
   *consistently* at all three uses (lines 7, 9, 11) — bash-confirmed to run clean **and** correct
   on its own, so it stays a pure typo, per the D-28 guardrail against inconsistent renames.
3. **Operator/symbol slip (common):** `==` → `=` on the `if` line (line 11).

**Bash-verified first traceback:** `SyntaxError: invalid syntax` at line 8 (`fro letter in word:`).
Second clue after fixing it: `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of
'='?`. Fixing exactly the three typos reproduces `challenge_1.py` byte-for-byte.</sub>
