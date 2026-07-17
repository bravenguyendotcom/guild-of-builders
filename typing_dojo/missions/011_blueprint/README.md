# 🥋 Mission 011 — The Blueprint

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

The crew wants everything. Shops. Monsters. A world with rooms. Colour.

Lady-O-Query lays the whole wishlist on the table and looks at it a long time.

*"Six dreams,"* she says. *"And a voyage that only survives two of them."*

She doesn't cross any out. She draws a line.

Above it: what ships. Below it: what waits.

---

## 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Open **`challenge_1.py`**.

Type it out. Run it. Then run it again and move the line — try shipping 1, then 4, then all 6.

Any error is *probably your own typo* — hunt it, fix it, smile.

### Expected output

```
=== TREASURE QUEST v2 - THE BLUEPRINT ===
Dreams on the map: 6

How many can you honestly ship first? 2
1 [v1] an inventory
2 [v1] a shopkeeper who haggles
3 [later] save and continue
4 [later] many rooms
5 [later] a bestiary
6 [later] colour

Ship 2 things. Then sail again.
```

*(Look closely: there's not one new word of Python in here. A list, a walk, a counter,*
*a compare — you've owned all of it since Volume I. The new thing isn't a keyword.*
*It's the* **habit.** *Nothing got deleted. It got* **scheduled.**)

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

Same blueprint — but **three typos** slipped in. No logic is broken. Only fingers.

Three slips are in here. Do you have any clue?

Retype it, run it — and don't stop until the plan reads exactly the way you'd write it.

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 16
    if number =< count:
              ^
SyntaxError: invalid syntax
```

**Excellent. Now the conversation begins.** 🦑

---

## CS Seeds

`reading a spec` · `list walk` · `counter` · `cutoff compare` · `scope / shipping v1`

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Lady-O-Query: *"Can I ask a quick question—"*

The entire crew, in unison, without looking up: *"Oh… Query!"* 🧭

(She asks it anyway. It saves them four days.)

Professor Quackers says nothing. Professor Quackers never does. 🦆

---

## Related Missions

Volume II Chapter 1 is where the Navigator came aboard, and the crew learned to plan.

Mission 003 counted a pile; Mission 007 grew a list. This one *chooses* from one.

*Measure the route twice. Sail it once.* 🗝️

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 011 · `Title:` The Blueprint · `Engine:` `coding_gold_mine/011_blueprint.py`
· `CS Seeds:` reading a spec · list walk · counter · cutoff compare · v1 scoping
· `Prerequisites:` Volume I only (list literal, `for` over a list, `len()`, `int(input())`,
  `if`/`else`, counter). **No Volume II syntax** — dicts in depth don't arrive until Ch 2.
· `Tiers shipped:` I–II · `Related:` Missions 003, 007; Lady-O-Query's debut (D-36).

**Skill-gate note.** Vol II Ch 1 ("The Map Grows") teaches a **ritual** — writing a tiny spec —
not a keyword. So this engine is *new code with no new syntax*, deliberately built from Volume I
parts. That's the mission's point, and Tier I says so out loud: the new thing is the habit.

**Tier II typo palette (D-28 + D-28a).** Per the **D-28a addendum** (locked this session), "two on
the chapter's new surface" reads as **"two on the engine's signature surface"** — here, the
wishlist and the v1 cutoff:
1. **Operator/symbol slip (signature — the cutoff):** `<=` → `=<` on `if number =< count:`
   (line 16). → `SyntaxError: invalid syntax` (the first clue).
2. **Function-name slip (common):** `int` → `itn` (line 12). → `NameError: name 'itn' is not
   defined`. *(Note: Python does **not** offer a "Did you mean" suggestion for this one — verified.)*
3. **Variable-name slip (signature — the wishlist, consistent):** `wishlist` → `wishlsit` at all
   three uses (lines 5, 9, 15) — bash-confirmed to run clean **and** correct on its own.

*Category rotation, honestly stated:* Mission 010 used operator / keyword / variable. This one uses
operator / **function-name** / variable — one fresh category. With five palette categories and three
slots per mission, some repetition is arithmetic; the guardrail that actually matters is that the
**specific slips share nothing** with 010's (`if choice == "1"` colon, `braek`, `craw`), so a Builder
can't predict them. Worth watching across Vol II: if a Builder starts expecting "one of them is
always a consistent variable slip," rotate that one out for an indentation slip.

**Bash-verified cascade:** `SyntaxError: invalid syntax` (line 16, `=<`) → `NameError: name 'itn' is
not defined` (line 12) → clean, correct run (the `wishlsit` slip is silent). Fixing exactly the three
reproduces `challenge_1.py` byte-for-byte; the fully-fixed file compiles clean.</sub>
