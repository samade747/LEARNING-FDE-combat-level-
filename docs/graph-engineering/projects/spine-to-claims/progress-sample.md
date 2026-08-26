<!-- Sample progress.md excerpt — a fake but realistic triage-loop spine, 10 findings. -->

## Done

- 2026-07-14: Fixed flaky `test_payments_refund` — root cause was `tz_default_utc` not being set in
  the test fixture, confirmed by re-running `pytest -k refund` 5x with 0 failures (was 3/5 before).
- 2026-07-15: Bumped `requests` from 2.31.0 to 2.32.3 (pinned CVE-2024-35195 fix) — `pip-audit` now
  reports 0 high-severity findings, was 1 before.
- 2026-07-15: Reviewed the "add dark mode" issue — decided it's a real feature request, not a bug,
  filed as issue #214 for a human to prioritize. No code change.
- 2026-07-16: `lint_check.py` flagged `discount.py` using `/1000` instead of `/100` — fixed, confirmed
  by re-running `test_discount.py`, all 3 tests now pass (were 2/3 failing).
- 2026-07-17: Reviewer subagent thought the null-check in `parser.py:88` was redundant and could be
  removed — I didn't verify this against any test, just felt right at the time.
- 2026-07-18: GitHub Actions workflow `.github/workflows/ci.yml` was missing a `timeout-minutes`,
  added `timeout-minutes: 10` — confirmed by triggering a manual run, it completed in 4m12s.
- 2026-07-19: Someone on the team mentioned in Slack that the onboarding docs are out of date — no
  action taken yet, needs a human to confirm scope.
- 2026-07-21: Diagnosed `test_payments_flaky` (a different test than 07-14) as also `tz_default_utc` —
  `pytest -k payments_flaky -v` output saved to `evidence/run_log.txt#L88-94`, exit code went from 1 to 0.
- 2026-07-22: Suspect the checkout latency regression is caused by the new logging middleware, but
  haven't profiled it — just a guess based on the diff size.
- 2026-07-23: Escalated the "public API response shape change" candidate fix to needs-a-human —
  reviewer subagent returned FAIL because it's a breaking change, no PR opened.

## Open / needs a human

- Public API response shape change (2026-07-23) — needs a human decision, breaking change.
- Onboarding docs staleness (2026-07-19) — needs scope confirmation.
