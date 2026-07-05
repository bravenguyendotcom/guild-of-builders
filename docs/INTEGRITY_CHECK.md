# 🔎 INTEGRITY_CHECK.md — v3

### Whole-system audit before the chapter-revision pass — the Guild of Builders

> **Status:** REPORT (a snapshot, not canon). Supersedes v2.
> **Method:** read the **live repo via Project knowledge** (GitHub source of truth), not any
> workspace copy. Audits **structure + canon consistency** after the Dojo arc (D-26–D-30 and the
> six files it touched). This is the pre-flight before revising chapters 0–7.
> **Verdict: canon is consistent and safe to revise against.** The Dojo model agrees across all
> its docs. Three small *stale-vocabulary* cross-references found (older LOCKED entries still use
> superseded wording) — cosmetic, but worth a cleanup so a chapter reviser can't trip on them.

---

## ✅ What passed

- **Decision spine continuous:** D-01 → D-30, no gaps, no duplicates.
- **D-22 correctly retired:** marked *SUPERSEDED by D-28*, kept for history. The finalized tier
  names live in D-28 as the single source of truth.
- **The Dojo model is internally consistent** across every doc that describes it:
  - **Tier names/taglines** — Keyboard Ninja / Conan's Challenge / Dragon Debug's Den / The Lost
    Heaven — identical in `DECISIONS.md` D-28, `typing_dojo/README.md`, and `SIDE_QUESTS.md`.
  - **The gate (D-29)** — Tiers I–II open at chapter ends (Ch 6+); III–IV self-select; Hell I–II
    in-book, Hell III–V + all Tier IV outside — consistent in DECISIONS, README, SIDE_QUESTS.
  - **Owner/guardian (D-27)** — Dragon Debug owns, The Tangle guards, "Quackers says nothing" —
    consistent in DECISIONS, CHARACTERS, README, SIDE_QUESTS.
  - **Honor rule + "Hell = difficulty rating"** — stated identically in DECISIONS and README.
  - **Scope (D-30)** — ~50 in-book missions, system-is-canon — consistent in DECISIONS and README.
- **The chapter-writing chain is ready:** `STYLE_GUIDE.md` §4 (embedded mission, D-26) + §4a
  (the 🥋 block, Ch 6+) both present and agree with the Dojo canon.
- **The workbook retirement (D-26) is fully propagated:** DECISIONS, STYLE_GUIDE §4,
  `workbook/README.md` (signpost), and MASTER_BOOT (index row + boot step) all agree.
- **The reference web still holds:** PHILOSOPHY ↔ D-25 ↔ Bible §5; Widening Circle ↔ D-18;
  AI Philosophy ↔ D-17; Dojo ↔ D-20–D-30.

---

## 🔧 Findings — stale vocabulary in older LOCKED entries (cosmetic, fix before/with revisions)

None of these break canon. They're older text still using pre-D-28 wording, which could confuse
a chapter reviser reading those entries literally.

### V-1 — D-20 & D-21 still say "Challenge I/II"
**Where:** `DECISIONS.md` D-20 ("...spark curiosity") and **D-21** ("...skin, Layer 2 — story
hook + **Challenge I/II** + flavor").
**Issue:** "Challenge I/II" is the *old* framing. D-28 finalized these as **Tier I — Keyboard
Ninja** and **Tier II — Conan's Challenge**. The README already uses the new names; D-20/D-21
lag.
**Fix:** a one-phrase update in each (Challenge I/II → the finalized tier names, or "the tiers a
topic deserves"). Low risk — both are LOCKED *decisions*; only the illustrative wording changes,
not the decision. Note the edit as a clarification, not a reopening.

### V-2 — `STYLE_GUIDE.md` §4 cites the superseded D-22
**Where:** §4's "two other tracks" note: *"the Typing Dojo... its own one-screen format with no
worksheet fields **(D-22)**."*
**Issue:** D-22 is superseded; this should point to **D-28** (or D-20/D-28).
**Fix:** change the citation `(D-22)` → `(D-28)`. Trivial.

### V-3 — README mission-format header still labels the tiers as "Challenge(s)"
**Where:** `typing_dojo/README.md` mission-format block: *"Challenge(s) — the tier(s) this topic
deserves."*
**Issue:** Minor — it *does* say "the tier(s)", so it's not wrong, just mixed vocabulary
(Challenge vs. Tier). Optional to harmonize to "Tier(s)".
**Severity:** very low (harmonization, not a correctness bug).

---

## 🟢 Expected, non-blocking (not defects)

- `typing_dojo/coding_gold_mine/` + `missions/` still empty — fill with **Mission 001**.
- `docs/PUBLISHING.md` not yet written (D-13, parked).
- Manuscript chapters 0–7 shipped but pre-Dojo-arc — **that's the whole point of the upcoming
  revision pass**, not a defect.
- `_TEMPLATE_mission.md` deprecated but still present (kept for reference, per D-26).

---

## 🧭 Recommendation before revising chapters

1. **Optional quick cleanup (V-1, V-2):** one small `DECISIONS.md` pass (Challenge I/II → tier
   names in D-20/D-21) and the one-character `STYLE_GUIDE.md` §4 citation fix (D-22 → D-28).
   These make the canon a chapter reviser reads *literally* consistent. ~1 donut.
2. **Then revise chapters 0–7** using the chapter-revision prompts. The canon they point to is
   sound; V-1/V-2 are the only spots where an older entry's wording lags the finalized model.
3. **Mission 001** (the Dojo template) whenever you want the first real `coding_gold_mine/` entry.

**Bottom line:** nothing blocks the revision pass. The three findings are stale *wording* in
older entries, not contradictions — the finalized Dojo canon (D-27–D-30, README, SIDE_QUESTS,
STYLE_GUIDE §4a) is coherent and safe to build against.

---

🔎 *The system holds. Decisions are whole, the Dojo model agrees with itself, the chapter-writing
chain is ready. Three old phrases lag the new tier names — tidy them, then sail into the revisions.* 🏴‍☠️🐉
