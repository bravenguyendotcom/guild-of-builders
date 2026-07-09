# 🥋 Mission 003 — The Tally Machine

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

The Recycling Robot found the treasure —

buried under a mountain of salvage.

Before it hands anything over, it wants a count:

*how many of that thing are in the pile?*

No shortcuts. It checks the heap **one item at a time.**

---

## 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Open **`challenge_1.py`**.

Type it out. Run it. Ask the robot to count different things.

Any error is *probably your own typo* — hunt it, fix it, smile.

### Expected output

The pile is always the same, so your counts will match these:

```
What should I count in the pile? bottle
I found 4 of those.
```

```
What should I count in the pile? wire
I found 2 of those.
```

```
What should I count in the pile? kraken
I found 0 of those.
```

*(Watch the `count` box climb, one loop at a time — the same counter you built in*
*Chapter 6, only now it's walking a whole pile.)*

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

Same robot — but **three typos** slipped in. No logic is broken. Only fingers.

Retype it, run it, and fix each slip until it runs clean.

Run it once and Python hands you your first clue:

```
NameError: name 'inpt' is not defined. Did you mean: 'input'?
```

**Excellent. Now the conversation begins.**

Two more are hiding further down. Find them the same way. 🦑

---

## CS Seeds

`list` · `for-loop` · `==` · `counter / accumulation` · `counting without .count()`

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

The Recycling Robot never rushes. It looks at *every* item — even the boot.

The Tangle checks the loop for a stray `:` to trip over, finds none, and sulks off.

Professor Quackers says nothing. Professor Quackers never does. 🦆

---

## Related Missions

- **Chapter 8 — The Recycling Robot** (where you first *met* this pile).
- **Mission 001 — Guess the Number** (its counter is the very one climbing here — a familiar
  friend in new work).
- *Coming later:* the same walk-the-list move, hunting palindromes and ciphers.
  *(Wait — a loop that visits every item... where have I seen that before?)*

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 003 · `Title:` The Tally Machine · `Engine:` `coding_gold_mine/003_tally.py`
· `CS Seeds:` list · for-loop · == · counter/accumulation · no-.count()
· `Prerequisites:` Chapter 8 (`for` over a list); counter from Chapter 6 · `Tiers shipped:` I–II
· `Related:` Ch 6 counter; Ch 8; future list-walking engines (004, 005).</sub>
