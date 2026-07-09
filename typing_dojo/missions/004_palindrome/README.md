# 🥋 Mission 004 — Mirror, Mirror

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

The Mirror only opens for one kind of word —

one that reads exactly the same, forwards and backwards.

No shortcut tool. No `.reverse()` — strings don't carry one.

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

*(Watch `reversed_word` build itself backwards, one letter stacked in*
*front of the last — the same walk-the-thing move as Chapter 8's pile,*
*only now it's walking letters instead of items.)*

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

Same Mirror — but **three typos** slipped in. No logic is broken. Only fingers.

Retype it, run it, and fix each slip until it runs clean.

Run it once and Python hands you your first clue:

```
NameError: name 'inpt' is not defined. Did you mean: 'input'?
```

**Excellent. Now the conversation begins.**

Two more are hiding further down. Find them the same way. 🦑

---

## CS Seeds

`string iteration` · `string concatenation` · `==` comparison · `palindrome check`

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

The Mirror never blinks, never rushes, never grades a word twice.

The Tangle checks the loop for a stray `:` to trip over, finds none, and sulks off.

Professor Quackers says nothing. Professor Quackers never does. 🦆

---

## Related Missions

- **Chapter 9 — The Palindrome Mirror** (where you first *met* this Mirror).
- **Mission 003 — The Tally Machine** (the same walk-it-one-at-a-time move —
  a familiar friend, wearing letters instead of items).
- *Coming later:* the same character-by-character walk, hunting a Caesar cipher.
  *(Wait — shifting one letter at a time... where have you seen that before?)*

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 004 · `Title:` Mirror, Mirror · `Engine:` `coding_gold_mine/004_palindrome.py`
· `CS Seeds:` string iteration · string concatenation · == · palindrome check
· `Prerequisites:` Chapter 8 (`for` loop, walking a sequence one item at a time)
· `Tiers shipped:` I–II · `Related:` Ch 8 tally loop; future character-math/cipher engines (005).</sub>
