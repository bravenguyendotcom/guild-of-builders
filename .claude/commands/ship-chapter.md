Ship the latest chapter: log it and commit it. Do NOT write or edit chapter content.

Chapters are authored elsewhere (in claude.ai, in canon) and pasted in by Brave.
Your ONLY job here is logging + committing. Never generate or rewrite story text.

Steps:
1. Run `git status` and `git diff` to find new/modified files under `manuscript/`.
2. Read the changed chapter file(s) — just enough to know the volume, chapter number,
   title, and what concept it teaches.
3. Update the logs, matching the EXISTING format already in each file:
   - Append a new top row to the Session log table in `docs/ROADMAP.md`
     (columns: Date | Session goal | Donut delivered | Next).
   - Add a newest-first line to `CHANGELOG.md`.
4. Show me the diffs for `docs/ROADMAP.md` and `CHANGELOG.md`. Wait for my OK.
5. On my OK only:
   `git add -A && git commit -m "Vol <V> Ch<N>: <title>" && git push`

Guardrails:
- Never edit anything under `manuscript/` — you log and commit, you don't author.
- Only touch `docs/ROADMAP.md` and `CHANGELOG.md` without asking; anything else, ask first.
- Never force-push. Never rewrite history.
- If nothing under `manuscript/` changed, say so and stop — don't invent a commit.
