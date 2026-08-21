# HARNESS.md — Model Swap Log (3 Nights)

Run your hardened loop (Project 7's fenced version, or `daily-triage-demo`) on a **different model**
for 3 nights. Log every break/shift, then move each fix from **behavior-coupling** (relies on this
model's habits) to **contract-coupling** (exit codes, schemas, tests — model-agnostic).

## Night 1 — [date], model: [name]

| What broke/shifted | Was it behavior-coupled (relied on old model's habits)? | Fix (contract-coupled) |
| --- | --- | --- |
| | | |

## Night 2 — [date], model: [name]

## Night 3 — [date], model: [name]

## Capstone Verdict

- [ ] Every failure moved to contract-coupling (exit codes / schemas / tests), not re-tuned prompts
- [ ] Loop runs clean on **both** models by the end — proof the harness belongs to you, not one model
