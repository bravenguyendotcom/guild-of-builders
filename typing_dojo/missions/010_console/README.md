# 🥋 Mission 010 — The Ship's Console

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

This is the last mission of the voyage — and it's the whole ship in one small screen.

Recruit your crew. Muster them on deck. Then give the order to set sail.

A menu that loops. A list that remembers. A word that ends it.

You built this shape once already, for your quests. Now it steers the whole game.

---

## 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Open **`challenge_1.py`**.

Type it out. Run it. Recruit a few of your own crew — friends, heroes, the ship's cat.

Any error is *probably your own typo* — hunt it, fix it, smile.

### Expected output

```
=== CAPTAIN BYTE'S CONSOLE ===
1) Recruit a crew member
2) Muster the crew
3) Set sail
Orders, Captain? 1
Name the recruit: Sir Boolean
Sir Boolean signs the ship's book.

=== CAPTAIN BYTE'S CONSOLE ===
1) Recruit a crew member
2) Muster the crew
3) Set sail
Orders, Captain? 1
Name the recruit: Ninja Cat
Ninja Cat signs the ship's book.

=== CAPTAIN BYTE'S CONSOLE ===
1) Recruit a crew member
2) Muster the crew
3) Set sail
Orders, Captain? 2
Crew aboard: 2
- Sir Boolean
- Ninja Cat

=== CAPTAIN BYTE'S CONSOLE ===
1) Recruit a crew member
2) Muster the crew
3) Set sail
Orders, Captain? 3
Anchors aweigh! The voyage begins.
```

*(It's the Quest Log from Chapter 12, wearing a captain's hat. Same menu loop, same*
*`.append()`, same `break`. The capstone didn't need a new trick — just the ones you kept.)*

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

Same console — but **three typos** slipped in. No logic is broken. Only fingers.

Two of them will stop the ship cold, and Python will point right at them.

The third won't. It sails just fine and still isn't spelled the way you'd spell it.

Retype it, run it, fix what you find — and don't stop at two.

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 15
    if choice == "1"
                    ^
SyntaxError: expected ':'
```

**Excellent. Now the conversation begins.** 🦑

---

## CS Seeds

`menu loop` · `while True` / `break` · `list.append()` · `list state` *(echo 007)*

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Captain Byte recruits a pizza as his first mate. No one has the heart to stop him.

Professor Quackers says nothing — but signs the ship's book. 🦆

---

## Related Missions

This is **Mission 007, promoted to captain.** Same menu loop, now steering the whole game.

You've reached the end of the first voyage — every engine in this deck, you can now type by heart.

*Version 1 beats perfect. And you just built your first one.* 🏴‍☠️

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 010 · `Title:` The Ship's Console · `Type:` 🔁 **Echo of Mission 007** (D-23) ·
`Engine:` `coding_gold_mine/010_console.py` — *new combined code.* Like Mission 009 (and unlike
Mission 006, which reused Engine 001 verbatim), a menu's labels live in the code, so the reskin is
new canonical code and lives as its own engine under D-21. *Flagged for the log: the backlog listed
this as "`007` (new skin)."*
· `CS Seeds:` menu loop · while True/break · list.append() · list state (echo 007)
· `Prerequisites:` Chapter 12 (menu loop, `.append()`) — all skills already owned · `Tiers:` I–II
· `Related:` Mission 007 (its origin); closes the Volume I ladder.

**Tier II typo palette (D-28), adapted for an Echo (see note).** Three distinct categories, two
fresh vs Mission 009 (indentation / operator / function-name); and deliberately none of Mission
007's slips (007 used the missing colon on `while True`, `.apend`, and an over-indent):
1. **Operator/symbol slip (common / menu dispatch):** `if choice == "1":` → `if choice == "1"` —
   missing colon (line 15), the first clue.
2. **Keyword slip (echoed signature):** `break` → `braek` (line 25).
3. **Variable-name slip (echoed signature, consistent):** `crew` → `craw` at all four uses (lines 5,
   17, 20, 21) — bash-confirmed to run clean **and** correct on its own, per the D-28 guardrail.

**Bash-verified cascade:** first `SyntaxError: expected ':'` (line 15); then, on choosing "set sail,"
`NameError: name 'braek' is not defined` (line 25); then a clean, correct run (the `craw` slip is
silent). Fixing exactly the three reproduces `challenge_1.py` byte-for-byte; the fully-fixed file
compiles clean.

**On "new surface" for Echo missions (open canon question — third and final Vol I occurrence).** An
Echo (D-23) has no new Python surface, so the D-28 "two on the new surface" clause is read here as
**"two on the echoed engine's signature surface"** (the `break` exit, the `crew` list). Same
adaptation as Missions 006 and 009. Having now fired three times across Volume I, this is the point
to lock it as a one-line D-28 addendum.</sub>
