---
name: daily-triage
description: >-
  Runs the capstone morning maintenance pass. Reads progress.md, gathers
  candidates from ISSUES.md and any failing tests, drafts safe fixes (checked
  by the reviewer subagent), reports what passed, and writes anything risky to
  progress.md for a human. Use this for Project 8, the daily-loop capstone.
---

# Daily triage (Project 8 capstone)

You are the morning maintenance loop, adapted from the book's own worked
example (Part 5) to run against local mock data instead of live CI/GitHub, so
this demo needs no external services. Work through these steps in order.

## 1. Read your memory first

Open `progress.md`. Read "In progress" and "Open / needs a human". Do not redo
anything already listed under "Done".

## 2. Find the work

Read `ISSUES.md`. It lists candidates the way real overnight CI failures and
GitHub issues would arrive.

## 3. Work each candidate

For each one, in an isolated branch (`claude/<short-slug>`):

- Run `python -m pytest tests/ -v` to see the actual failure, never guess it.
- Draft the smallest fix that solves the one problem.
- Send the diff to the `reviewer` subagent. Wait for its verdict.

## 4. Decide from the verdict

- **PASS, low risk** (no public behaviour change): report it as ready to merge
  from its branch. Title: `fix: <one short line>`.
- **FAIL, or the change touches public behaviour** (like issue #2's format
  change): do NOT fix it. Add an entry to "Open / needs a human" in
  `progress.md` explaining what it is and why it needs a person.

## 5. Update your memory last

Move finished items to "Done" with today's date. Save `progress.md`.

## Rules

- Never edit `tests/test_greeter.py` to make it pass — it is the spec.
- Never resolve issue #2 (the format change) yourself — it is a planted
  "always escalate" case. If your run auto-fixes it, that is a bug in your
  loop, not a correct pass.
- When in doubt, escalate.
