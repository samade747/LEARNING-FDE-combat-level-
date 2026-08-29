<!-- progress.md — base loop ki memory. Dreaming loop isay parhta hai (read-only). -->

## Done

- 2026-08-05: Set up the `daily-triage` skill in this repo. First run: read ISSUES.md, fixed the
  `greet_all` off-by-one on branch `claude/fix-greet-all`, reviewer PASS, 3/3 tests green. No issues.

- 2026-08-08: Added `format_report` helper + tests. Run was clean — worktree isolated, reviewer PASS
  on first round. progress.md updated.

- 2026-08-10: Fixed the `discount` rounding bug (`/1000` → `/100`) on `claude/fix-discount`. Tests
  passed. **Problem:** committed before running `ruff` — the reviewer caught 4 lint errors
  (unused import, bare except) and sent it back for a second round. Wasted a review cycle.

- 2026-08-13: Ran the fix-loop for the `parse_date` crash. **Problem:** the reviewer subagent was
  handed `main` instead of the `claude/fix-parse-date` worktree branch, so it "reviewed" code that
  didn't have the fix and returned a confused PASS. Had to re-run the reviewer against the right
  branch. Second run was fine.

- 2026-08-16: Fixed `total_price` currency bug on `claude/fix-total-price`. **Problem:** again
  committed without `ruff` first — 2 lint errors (line too long, f-string without placeholder)
  bounced back from review. One extra round.

- 2026-08-18: Added retry logic to the HTTP client. Clean run, reviewer PASS, tests green.

- 2026-08-21: Fixed the `pagination` off-by-one on `claude/fix-pagination`. **Problem:** reviewer
  subagent pointed at the previous branch (`claude/fix-total-price`), graded stale code, PASS was
  meaningless. Re-pointed at the correct branch and re-ran.

- 2026-08-23: Fixed `slugify` unicode handling on `claude/fix-slugify`. **Problem:** committed
  without running `ruff` — reviewer caught an unused variable and a shadowed builtin, second round
  needed.

- 2026-08-26: Refactored `config_loader` into two functions. Clean run. Reviewer PASS first round,
  tests green, progress.md updated.

## Open / needs a human

- 2026-08-18: The public JSON response shape change (issue #7) is a breaking change — escalated,
  not touched. Needs a human decision on versioning.
