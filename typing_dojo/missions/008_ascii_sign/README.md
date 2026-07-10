# 🥋 Mission 008 — The Sign Painter

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

Pycasso never speaks. Pycasso *paints.*

And today Pycasso hands you a brush made of loops.

Pick a symbol. Pick a height. Then watch a picture climb the screen,

one row taller than the last, until your sign stands finished.

Loops don't just count anymore. Now they draw.

---

## 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Open **`challenge_1.py`**.

Type it out. Run it. Try a few symbols and heights of your own — `*`, `#`, `@`, a `4`, a `9`.

Any error is *probably your own typo* — hunt it, fix it, smile.

### Expected output

```
Paint with which symbol? *
How tall? 4
*
**
***
****
```

*(`range(1, height + 1)` counts the rows — 1, 2, 3, 4 — and `symbol * row` repeats the*
*symbol that many times to paint each line. Same loop you know, holding a paintbrush.)*

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

Same brush — but **three typos** slipped in. No logic is broken. Only fingers.

Two of them will stop the paint cold, and Python will point right at them.

The third won't. It paints just fine and still isn't spelled the way you'd spell it.

Retype it, run it, fix what you find — and don't stop at two.

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 8
    for row ni ragne(1, height + 1):
            ^^
SyntaxError: invalid syntax
```

**Excellent. Now the conversation begins.** 🦑

---

## CS Seeds

`range()` · `string repetition (symbol * n)` · `loops build shapes` · `for-loop`

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Pycasso says nothing, but paints a tiny dragon in the corner. It is, somehow, sipping tea.

Professor Quackers says nothing either. The two of them get along beautifully. 🦆

---

## Related Missions

Chapter 13 is where your loops picked up a paintbrush.

Mission 004 walked a word one letter at a time; this one *builds* rows one line at a time.

*Coming later: two loops, one inside the other — and the picture fills in both directions.* 🗝️

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 008 · `Title:` The Sign Painter · `Engine:` `coding_gold_mine/008_ascii_sign.py`
· `CS Seeds:` range() · string repetition · loops build shapes · for-loop
· `Prerequisites:` Chapter 8 (`for` loop); Chapter 13 introduces `range()` and string repetition
  (`symbol * n`). · `Tiers shipped:` I–II · `Related:` Ch 9 string walk; future nested-loop art.

**Tier II typo palette (D-28) — categories keyword / function-name / variable, two fresh vs
Mission 007 (operator / method-name / indentation); two of three on Ch 13's new surface:**
1. **Keyword slip (common):** `in` → `ni` on the `for` line (line 8) — a keyword not slipped before.
2. **Function-name slip (new surface):** `range` → `ragne` (line 8).
3. **Variable-name slip (new surface, consistent):** `symbol` → `symbl` at both uses (lines 5, 9),
   on the repetition line `symbl * row` — bash-confirmed to run clean **and** correct on its own,
   per the D-28 guardrail.

**Bash-verified cascade:** first `SyntaxError: invalid syntax` (line 8, `ni`); then
`NameError: name 'ragne' is not defined. Did you mean: 'range'?` (line 8); then a clean, correct
run (the `symbl` slip is silent). Fixing exactly the three reproduces `challenge_1.py`
byte-for-byte; the fully-fixed file compiles clean.</sub>
