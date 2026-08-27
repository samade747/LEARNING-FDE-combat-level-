# P11 — KSoR III: Proving Behaviour

*Practicum week P11, [`../../02-fde-practicum.md`](../../02-fde-practicum.md). **Milestone 3:** governed
KSoR + a three-class evaluation set.*

## The Three Classes

1. **`answerable_with_citation`** — a governed source directly answers the question.
2. **`requires_rule_plus_fact`** — needs a governed rule (a threshold) **and** a live operational fact
   (an order's amount) together. Neither half alone is enough.
3. **`outside_boundary_abstain`** — nothing in the corpus or operational facts covers it; the agent
   must abstain, not guess.

## Files

- `agent_under_test.py` — the tiny agent being evaluated: one governed rule (`POLICY-REFUND-001`, a
  $500 threshold), a small operational-facts lookup (order amounts), and `answer(case)` that routes to
  the right behaviour for each class.
- `eval_cases.json` — 7 cases across the 3 classes, including one `requires_rule_plus_fact` case whose
  operational record doesn't exist (`order-999`) — that one must abstain, not crash or guess.
- `eval_runner.py` — runs every case, reports **pass/fail per class**, not one aggregate score. A class
  with all cases passing is `[PASS]`; any failure in a class marks that whole class `[FAIL]` with the
  specific failing case IDs listed.

## Kaise Chalayein

```bash
cd docs/ccar-f-fde-track-b/projects/p11-proving-behaviour
python eval_runner.py
```

**Break it on purpose:** edit `eval_cases.json`, change C2's `expect_needs_approval` from `true` to
`false` (wrong on purpose), re-run, confirm `requires_rule_plus_fact` reports `[FAIL]` with `C2` named
— then revert.

## Done Jab (Self-Check)

- [x] All 3 classes present in `eval_cases.json`, each with 2+ cases
- [x] `eval_runner.py` reports pass/fail **per class**, not one number
- [x] The missing-operational-record case (`order-999`) abstains instead of crashing or guessing
- [ ] You ran the "break it on purpose" step and saw the named failing case

---
[⬅ Practicum Index](../../02-fde-practicum.md) · [⬆ Chapter Index](../../README.md)
