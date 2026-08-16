# Daily Triage Demo (Project 8 Capstone)

This project is a self-contained rehearsal of the book's own Part 5
morning-triage loop — the same shape (skill → worktree → maker-checker →
spine → human gate), but pointed at local mock data (`ISSUES.md`) instead of
live CI/GitHub, so it needs no external services to try.

Run the `daily-triage` skill (`.claude/skills/daily-triage/SKILL.md`) to fire
one beat. The `reviewer` subagent is the checker — read-only, and it always
rejects the planted risky change (issue #2) on purpose, so you can watch the
human gate actually catch something.

Read `progress.md` first, write it last. Never skip it — it is this loop's
only memory between runs.
