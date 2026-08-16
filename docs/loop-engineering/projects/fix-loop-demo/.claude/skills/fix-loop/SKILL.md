---
name: fix-loop
description: >-
  Runs the Project 4 fix loop. Reads the failing test, drafts the smallest fix
  on an isolated branch, sends the diff to the reviewer subagent, and only
  reports success on a PASS verdict. Use this whenever asked to run the fix
  loop or fix the discount bug.
---

# Fix loop (Project 4 — A Fix Loop With a Real Checker)

You are the maker half of a maker-checker loop. Work through these steps in order.

## 1. Find the work

Run `python -m pytest test_discount.py -v` and read which tests fail and why.
This is the real bug — not a guess, not a memory of what the code "probably" does.

## 2. Draft the fix in isolation

Create an isolated checkout: a git worktree, or a fresh branch named
`claude/fix-discount-bug`. Draft the smallest fix that makes the failing tests
pass. Do not touch anything the tests do not exercise.

## 3. Send it to the reviewer — wait for the verdict

Invoke the `reviewer` subagent on your diff. Do not merge, commit to `main`,
or declare success until it replies.

## 4. Decide from the verdict

- **PASS**: report the fix is ready, on its branch, with the reviewer's
  one-line confirmation.
- **FAIL**: do NOT merge or report success. Say what the reviewer flagged and
  stop there — a human decides what happens next.

## Rules

- Never edit `test_discount.py` to make it pass. The test is the spec, not an
  obstacle.
- Never touch `main` directly. Only `claude/*` branches.
- The reviewer must actually run `python -m pytest test_discount.py` itself.
  A verdict without running the tests is not a real verdict.
