# 🔎 INTEGRITY_CHECK.md

### Whole-project cross-reference audit — the Guild of Builders

> **Status:** REPORT (a snapshot, not canon). Run periodically; supersede with a newer check.
> **Method & honest caveat:** this audits the **reference web** — do the files point at each
> other correctly, are decisions continuous, is every citation real. It was run against the
> workspace copy plus the freshest synced files available. It does **not** re-verify prose that
> was shipped by Codie without passing back through chat; those are marked *(assumed synced)*.
> **Verdict up top: the project is in strong structural health.** Findings below are small.

---

## ✅ What passed (the good news)

- **Decisions are continuous:** D-01 → D-25, no gaps, no duplicates.
- **Every cited decision exists.** Every `D-xx` referenced anywhere in the repo resolves to a
  real entry in `DECISIONS.md`. No dangling citations.
- **Character canon is complete** for every named character cited across the project — the
  founding four, the supporting cast (Pycasso, Monty, Quizzalot, Sir Boolean, Ninja Cat,
  Bug Monster), and the Fog Creatures (incl. Snooze Kraken, Shortcut Serpent). *(One naming
  gap — see F-1.)*
- **The MASTER_BOOT index resolves:** every file the index lists exists in the repo.
- **The soul/decision web is whole:** `PHILOSOPHY.md` ↔ D-25 ↔ Bible §5; Widening Circle
  (Bible §6.5 ↔ D-18 ↔ Manifesto Part VII); AI Philosophy (Bible §12 ↔ D-17 ↔ Manifesto);
  Typing Dojo (`SIDE_QUESTS.md` → `typing_dojo/` → D-20–D-23). All pointers line up.

---

## 🔧 Findings (small, ordered by priority)

### F-1 — "The Tangle" is referenced but not in `CHARACTERS.md`
**Severity:** low-medium (canon gap).
The Typo-Squid **The Tangle** appears in `DECISIONS.md` (D-19), `SIDE_QUESTS.md`, and
`typing_dojo/README.md` — but it has **no entry in `CHARACTERS.md`**, the single source of
truth for characters. Every other named creature (incl. the Fog Creatures) lives there.
**Fix:** add a short DRAFT entry for The Tangle to `CHARACTERS.md` (a side-quest guardian, not
a story character — note the distinction, like Bug Monster vs. Fog Creatures). *One donut.*

### F-2 — `coding_gold_mine/` referenced but doesn't exist yet
**Severity:** none (expected).
`typing_dojo/README.md` and the index describe `typing_dojo/coding_gold_mine/` and
`typing_dojo/missions/`, but those folders aren't created yet (no content shipped).
**Fix:** none needed now — they arrive with **Mission 001**. Listed only so it's a known,
intentional gap, not a surprise.

### F-3 — `docs/PUBLISHING.md` referenced but doesn't exist yet
**Severity:** none (expected).
`DECISIONS.md` D-13 promises a future `docs/PUBLISHING.md` (the render pipeline). Correctly
still parked in the Treasure Chest.
**Fix:** none now — build when the publishing pipeline is chosen.

### F-4 — A few root files aren't in the MASTER_BOOT index
**Severity:** cosmetic.
`README.md` and `GIT_GUIDE.md` aren't listed in the index table. (`typing_dojo/` *is* indexed
as a folder; its README is covered by that row.)
**Fix (optional):** add two rows for completeness, or leave them — they're self-evident
top-level files. Author's call.

### F-5 — Manuscript / workbook are still scaffold only
**Severity:** none (expected — we're in orientation, not writing).
`manuscript/` and `workbook/` hold only READMEs and templates; the actual Volume I chapters
(0 & 1) live in *other conversations* and were intentionally not synced here.
**Fix:** none. Noted so a future audit doesn't mistake it for a gap.

### F-6 — Two open items still correctly parked (not problems)
- The 🏗️ **"In the Real World" box** is defined in `STYLE_GUIDE.md` but **not yet added to
  `_TEMPLATE_chapter.md`** (queued donut).
- The kid-facing **"Preparing for the Voyage"** pre-chapter (from `SETUP.md`) isn't written yet.
Both are known, tracked, and fine to leave until a writing session.

---

## 🧭 Recommended next donuts (in priority order)

1. **F-1 — add The Tangle to `CHARACTERS.md`.** The only true canon gap; quick fix.
2. **`_TEMPLATE_chapter.md`** — add the 🏗️ In-the-Real-World box (closes F-6a).
3. **Mission 001** — first Dojo content; creates `coding_gold_mine/` + `missions/` (closes F-2).
   *(Build/content donut — likely a build session, not orientation.)*

---

## Coverage note (what this audit could NOT fully verify)

Prose shipped by Codie without returning through chat (`CHARACTERS`, `STYLE_GUIDE`, `SETUP`,
`BUILDERS_LOGBOOK`, `HUMAN_AI_MANIFESTO`, `SIDE_QUESTS`, `DECISIONS`, `typing_dojo/README`) was
audited for **structure and cross-references**, not re-read line-by-line for prose drift. If a
deeper content audit is wanted, re-sync those files into a chat and I'll read them in full.

---

🔎 *Structure is sound. The web holds. One small canon gap (The Tangle), the rest is expected
work-in-progress. A healthy ship.* 🏴‍☠️🐉
