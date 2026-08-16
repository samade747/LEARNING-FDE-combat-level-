# Fix Loop Demo (Project 4)

This project has one job: fix a real, planted bug in `discount.py` using a
maker-checker loop — never grade your own work.

**The checker is `python -m pytest test_discount.py -v`, run for real, every
time.** Never claim tests pass without running them. Never edit the test file
to make it pass — the test is the spec, not an obstacle.

Use the `fix-loop` skill (`.claude/skills/fix-loop/SKILL.md`) to run the full
maker-checker cycle. The `reviewer` subagent is the checker; it is read-only
and never edits files.
