# 📖 MANUSCRIPT_AUDIT.md

### Canon audit — Volume I, Chapters 0–7

> **Status:** REPORT (a snapshot, not canon). Supersede with a newer audit as chapters ship.
> **Method:** each shipped chapter read **in full from the live repo** (Project knowledge) and
> checked against `CHARACTERS.md` (voice), `STYLE_GUIDE.md` (accessibility + chapter structure
> + the 🏗️ box), `CURRICULUM.md` (concept order), and `SERIES_OUTLINE.md` (chapter map).
> **Scope:** chapters 0–7. (8+ not yet written.)
> **Verdict: the manuscript is in excellent shape.** The voice is consistent, the pedagogy is
> genuinely strong, accessibility holds throughout. Findings are small and mostly optional.

---

## ✅ What's working beautifully (keep doing this)

- **Character voice is rock-solid and on-canon.** Dragon Debug's *"Interesting"* = "lean in";
  his three-line calm; Captain Byte charging ahead and creating the bug; Quackers silent then
  one settling *"Quack"*; the tea and pizza running jokes — all present and true to `CHARACTERS.md`.
- **"Errors are conversations" is lived, not stated.** Every chapter earns *"Excellent. Now the
  conversation begins."* through a **real, honest bug** the reader would actually hit
  (`"3" * 2 == "33"`, `int("1.5")` ValueError, the infinite loop, the blurry `and`-guard letting
  `"password"` through). This is the strongest pedagogical thread in the book.
- **Accessibility is exemplary.** Short lines, one-idea-per-line, generous whitespace, plain
  words. Teppy is clearly being cared for on every page.
- **Chapter structure is consistent** and matches `STYLE_GUIDE.md`: story → riddle → Toolbox
  Card → 🏗️ In the Real World → Dragon's Wisdom → Achievement Unlocked → cliffhanger. The
  cliffhangers chain cleanly (each chapter's ending sets up the next).
- **The 🏗️ "In the Real World" box (D-14) is present and correctly used** — after the story,
  short, real vocabulary in bold (*state*, *user*, *module/library*, *validation*, *George Boole*),
  never a lecture.
- **TommyBot is introduced well** (Ch 1: *"TommyBot is you, by the way"*) — the reader-avatar
  role from `CHARACTERS.md` lands.

---

## 🔧 Findings

### M-1 — Chapter numbering vs. SERIES_OUTLINE is off by one *(worth a decision)*
**Severity:** medium — not wrong, but a real inconsistency two docs disagree on.
The **shipped chapters** and the **`SERIES_OUTLINE.md` map** have drifted apart:

| Shipped chapter | SERIES_OUTLINE says that number is... |
|---|---|
| Ch 3 — The Age Machine (`if`/`elif`/`else`) | "The Fork in the Tide" (Sir Boolean debut) |
| Ch 4 — Ninja Health Check (`float`, `round`) | "Numbers of the Sea" (modulo) |
| Ch 6 — The Secret Treasure (`while`) | "The Guessing Cave" |
| Ch 7 — Safe Password Checker (Sir Boolean **debuts here**) | "The Locked Gate" |

The manuscript is internally consistent and flows well — but the **outline no longer matches
what was actually written** (e.g. the outline debuts Sir Boolean at Ch 3/"Fork in the Tide";
in the real manuscript he debuts at **Ch 7**). **Fix:** update `SERIES_OUTLINE.md`'s Volume I
section to match the shipped chapters (the map should follow the territory). *One donut, later.*

### M-2 — CURRICULUM "story order" lists modulo before the shipped chapters use it
**Severity:** low.
`CURRICULUM.md` skills list has integer division & modulo early (Level 1, "Pirate Gold
Exchange"), but the shipped Ch 4 is the Ninja Health Check (`float`/`round`), and modulo hasn't
appeared yet by Ch 7. Not an error — the manuscript reordered sensibly — but CURRICULUM's
"in story order" note is now slightly ahead of the real order. **Fix:** a light CURRICULUM pass
to match shipped reality (same donut as M-1, ideally).

### M-3 — Verify the intentional teaching-bugs actually run *(process check, per STYLE_GUIDE)*
**Severity:** low (likely already fine) — flagged because the Style Guide **requires** it.
The chapters lean on deliberately-broken code that must fail *exactly* as narrated:
- Ch 2: `print("Double that!", slices * 2)` → `Double that! 33` ✅ (correct — string repetition)
- Ch 4: `int(input(...))` on `1.5` → `ValueError: invalid literal for int() with base 10: '1.5'`
  ✅ (message matches real Python)
- Ch 6: the infinite-loop version (guess read once, before the loop) → loops forever ✅
- Ch 7: `if len(password) >= 8 and password != "pizza"` accepts `"password"` ✅ (8 chars, ≠ pizza)

All four *read* correct on inspection. **Fix:** none needed if Codie/Brave already run them per
`STYLE_GUIDE.md` ("all code tested via bash before it appears"). Noted only so the audit trail
shows they were checked for narrative accuracy.

### M-4 — Chapter 0 not re-read this pass *(coverage honesty)*
**Severity:** none.
Ch 0 (Welcome) is confirmed shipped and is story-only (no syntax), per the CHANGELOG and
SERIES_OUTLINE. I audited its *role and placement* but did not re-read its full prose this pass.
**Fix:** none needed; flagged for completeness.

---

## 🧭 Recommended follow-ups (priority order)

1. **M-1 — reconcile `SERIES_OUTLINE.md` (and lightly `CURRICULUM.md`) to the shipped chapters.**
   The map should match the territory. One clean donut.
2. **M-3 — confirm the four teaching-bugs are bash-run** (if not already), per Style Guide.
3. Nothing blocks continued writing — Chapter 8 (Recycling Robot) is clear to proceed.

---

## Coverage note

Chapters 1–7 read in full from the live repo this pass; Ch 0 verified for role/placement only.
This audits **story, voice, structure, accessibility, and concept order** — not a line-by-line
runtime test of every snippet (that's the author's bash step, M-3).

---

📖 *A genuinely lovely manuscript. The teaching is invisible and the bugs are honest — exactly
the goal. The only real gap is that the map (SERIES_OUTLINE) drifted behind the territory (the
shipped chapters); everything the child actually reads is in strong shape.* 🏴‍☠️🐉
