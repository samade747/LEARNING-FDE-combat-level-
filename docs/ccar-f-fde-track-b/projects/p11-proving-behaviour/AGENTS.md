# P11 — Proving Behaviour Scaffold

This project's one job: report evaluation results **per class**, never as one aggregate number. A
strong aggregate can hide a weak class — that is the exact failure this milestone exists to catch.

Do not collapse `eval_runner.py`'s per-class breakdown into a single pass/fail percentage. Do not add a
new eval case without also adding it to the correct one of the three classes in `eval_cases.json`.
