# 🥋 Mission 007 — The Quest Log

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

Every Builder needs a place to keep their quests.

Not on a scrap of paper that blows away — in a program that *remembers.*

Show a menu. Wait for a choice. Add a quest, or list them all, or close the book.

Then loop back and do it again, for as long as you like.

This little shape — *menu, choice, remember, repeat* — is almost every program ever written.

---

## 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Open **`challenge_1.py`**.

Type it out. Run it. Add a few quests of your own, then list them.

Any error is *probably your own typo* — hunt it, fix it, smile.

### Expected output

```
QUEST LOG
1) Add a quest
2) Show all quests
3) Close the log
Choose: 1
New quest: Find the Sunstone
Added: Find the Sunstone

QUEST LOG
1) Add a quest
2) Show all quests
3) Close the log
Choose: 1
New quest: Befriend the dragon
Added: Befriend the dragon

QUEST LOG
1) Add a quest
2) Show all quests
3) Close the log
Choose: 2
You have 2 quests:
- Find the Sunstone
- Befriend the dragon

QUEST LOG
1) Add a quest
2) Show all quests
3) Close the log
Choose: 3
The log closes. Fair winds, Builder.
```

*(The list `quests` remembers everything between choices — that's* **state.** *`.append()` is*
*how you add to it. The menu keeps looping until you choose to* `break` *out.)*

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

Same log — but **three typos** slipped in. No logic is broken. Only fingers.

Fix one, run again, and the next clue steps forward. Keep going until the log opens clean.

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 7
    while True
              ^
SyntaxError: expected ':'
```

**Excellent. Now the conversation begins.** 🦑

---

## CS Seeds

`menu loop` · `while True` / `break` · `list.append()` · `list state` · `if / elif dispatch`

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Captain Byte adds three quests to his log. All three are just *"eat pizza."*

Professor Quackers says nothing. Professor Quackers never does. 🦆

---

## Related Missions

Chapter 12 is where your programs learned to *keep going* and *remember.*

Mission 003 counted a list; this one grows one — the log fills up as you play.

*Coming later: the log learns to cross quests off, and to save itself for tomorrow.* 🗝️

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 007 · `Title:` The Quest Log · `Engine:` `coding_gold_mine/007_menu.py`
· `CS Seeds:` menu loop · while True/break · list.append() · list state · if/elif dispatch
· `Prerequisites:` Chapter 8 (`for` over a list, `len()`); Chapter 12 introduces the menu loop
  (`while True` + `break`) and list mutation (`.append()`). · `Tiers shipped:` I–II
· `Related:` Ch 8 list read; future save/CRUD echoes (Vol II).

**Tier II typo palette (D-28) — three distinct categories, none repeating Mission 006
(keyword / name / variable); two of three on Ch 12's new surface:**
1. **Operator/symbol slip (new surface):** `while True:` → `while True` — missing colon on the menu
   loop (line 7).
2. **Method-name slip (new surface):** `.append` → `.apend` on the list (line 17).
3. **Indentation slip (common):** a stray over-indent on the `print("Added:", quest)` line (line 18).

**Bash-verified cascade:** first `SyntaxError: expected ':'` (line 7); then
`IndentationError: unexpected indent` (line 18); then, on adding a quest,
`AttributeError: 'list' object has no attribute 'apend'. Did you mean: 'append'?` (line 17).
Fixing exactly the three reproduces `challenge_1.py` byte-for-byte; the fully-fixed file compiles
clean.</sub>
