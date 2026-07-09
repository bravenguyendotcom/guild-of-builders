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
  File "challenge_2.py", line 12
    print(word, "is a palindrome. The Mirror agrees with itself.)
                ^
SyntaxError: unterminated string literal (detected at line 12)
```

**Excellent. Now the conversation begins.**

Close that quote, run it again, and a second clue appears — Python pointing right at the
Mirror's own `for` line, asking for something small it's missing.

The third typo is sneakier. It won't crash anything — the Mirror will run just fine and still
judge every word correctly. But look closely at the letter the loop walks with. Does it match
what this chapter taught you to call it? A good detective notices what *doesn't* cause trouble
too. 🦑

---

## CS Seeds

`string iteration` · `string concatenation` · `==` comparison · `palindrome check`

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

The Mirror never blinks, never rushes, never grades a word twice.

The Tangle checks the loop for a stray `:` to trip over, finds none the second time, and sulks off.

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
· `Tiers shipped:` I–II · `Related:` Ch 8 tally loop; future character-math/cipher engines (005).
· `Tier II typo palette (D-28):` missing-quote slip (line 12, common) · missing-colon slip on the
  `for` header (operator/symbol, new-surface) · consistent `letter`→`lettr` rename (variable-name,
  new-surface, cosmetic-only — bash-confirmed to run clean and correct on its own, per the D-28
  guardrail against inconsistent variable renames). Bash-verified first traceback: `SyntaxError:
  unterminated string literal (detected at line 12)`.</sub>
