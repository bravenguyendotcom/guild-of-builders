Ship the latest chapter: log it and commit it. Do NOT write or edit chapter content.

Chapters are authored elsewhere (in claude.ai, in canon) and pasted in by Brave.
Your ONLY job here is logging + committing. Never generate or rewrite story text or mission code.

Steps:
1. Run `git status` and `git diff` to find new/modified files under `manuscript/` and
   `typing_dojo/`.
2. Read the changed chapter file(s) — just enough to know the volume, chapter number,
   title, and what concept it teaches. If a Dojo mission changed too, note its number/title.
3. Update the logs and tracking files, matching the EXISTING format already in each file:
   - Append a new top row to the Session log table in `docs/ROADMAP.md`
     (columns: Date | Session goal | Donut delivered | Next).
   - Add a newest-first line to `CHANGELOG.md`.
   - If a Dojo mission shipped: in `typing_dojo/MISSIONS_PLAN.md`, flip that mission's Status
     to `✅ built` and bump the next mission to `🔨`.
   - If the chapter was previously marked planned: in `docs/SERIES_OUTLINE.md`, change its tag
     from `*(planned)*` to `*(shipped)*`.
4. Show me the diffs for every file you changed. Wait for my OK.
5. On my OK only:
   `git add -A && git commit -m "Vol <V> Ch<N>: <title>" && git push`

Guardrails:
- Never edit anything under `manuscript/` or `typing_dojo/` content (chapters, engines,
  challenges, mission READMEs) — you log and commit, you don't author.
- Only touch `docs/ROADMAP.md`, `CHANGELOG.md`, `typing_dojo/MISSIONS_PLAN.md`, and
  `docs/SERIES_OUTLINE.md` without asking; anything else, ask first.
- Never force-push. Never rewrite history.
- If nothing under `manuscript/` changed, say so and stop — don't invent a commit.
