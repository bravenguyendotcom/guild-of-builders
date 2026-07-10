# 🥋 Mission 005 — Secret Cipher

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

Every letter has a secret number.

`a` is one number, `b` is the next, and so on down the line.

Slide every number along by the same amount, turn them back into letters,

and your message turns to nonsense that only the Guild can read.

Slide it back the other way, and the secret returns.

---

## 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Open **`challenge_1.py`**.

Type it out. Run it. Try a few words of your own — then try shifting back to read them again.

Any error is *probably your own typo* — hunt it, fix it, smile.

### Expected output

```
Message to encode: hello
Shift by how many? 3
Encoded: khoor
```

```
Message to encode: dragon
Shift by how many? 3
Encoded: gudjrq
```

To *decode*, run it again on the secret with a **negative** shift:

```
Message to encode: khoor
Shift by how many? -3
Encoded: hello
```

*(`ord()` turns a letter into its number; `chr()` turns a number back into a letter.*
*The whole cipher is just counting — no magic, no shortcut.)*

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

Same cipher — but **three typos** slipped in. No logic is broken. Only fingers.

Retype it, run it, and fix each slip until it runs clean. Fix one, and the next clue appears.

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 13
    print("Encoded:", secret)
                             ^
IndentationError: unindent does not match any outer indentation level
```

**Excellent. Now the conversation begins.**

Straighten that line up, run again, and the next two clues are waiting — both hiding in the
Mirror's new trick, the little spells that turn letters into numbers and back. 🦑

---

## CS Seeds

`ord()` · `chr()` · `character math` · `string building` · `encoding`

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Captain Byte insists he can read any code by eye. *(He read `gudjrq` as "breakfast.")*

Professor Quackers says nothing. Professor Quackers never does. 🦆

---

## Related Missions

Chapter 10 is where you first sent a message in secret.

Mission 004 walked a word letter by letter; this one does the same, and gives each letter a number.

*Coming later: what if the shift changed with every letter?* 🗝️

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 005 · `Title:` Secret Cipher · `Engine:` `coding_gold_mine/005_caesar.py`
· `CS Seeds:` ord() · chr() · character math · string building · encoding
· `Prerequisites:` Chapter 9 (`for` over a string, string building); `int(input())` from Ch 2.
  *No modulo* — Ch 10 has no `%` yet, so the cipher does not wrap the alphabet (by design).
· `Tiers shipped:` I–II · `Related:` Ch 9 string walk; future Vigenère/echo cipher.

**Tier II typo palette (D-28) — categories fresh vs Mission 004 (which used keyword/variable/
operator); two of three on Ch 10's new surface:**
1. **Function-name slip (new surface):** `ord` → `odr` (line 10).
2. **Function-name slip (new surface):** `chr` → `crh` (line 11).
3. **Indentation slip (common):** a stray leading space on the final `print` (line 13).

**Bash-verified cascade:** first traceback `IndentationError: unindent does not match any outer
indentation level` (line 13); then `NameError: name 'odr' is not defined` (line 10); then
`NameError: name 'crh' is not defined` (line 11). Fixing exactly the three reproduces
`challenge_1.py` byte-for-byte; the fully-fixed file compiles clean.</sub>
