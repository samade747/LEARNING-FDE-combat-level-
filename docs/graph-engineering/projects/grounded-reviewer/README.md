# Graph Project 6 — The Grounded Reviewer

**Concept:** 10, Part 6 (grounding, the reviewer) · **Time:** 1-2 hrs, then 5 beats · **Difficulty:** Hard

"Triple not found" beats "seems off." This project makes a checker demand a real edge instead of an
impression, using exactly the book's own vendor_x / component_z / incident_y example.

## Files

- `entities.json`, `claims.json` — a tiny graph: `vendor_x supplied component_z`, `component_z
  involved_in incident_y` (both `tool_output` sourced), plus one decoy inference-only claim
- `reviewer_schema.json` — verdict shape (decision, reason, `grounded_in` for a PASS, `required_evidence`
  for a REVISE/FAIL)
- `validate_verdict.py` — checks the verdict is not just shaped right, but **actually grounded**: every
  `grounded_in` id must resolve in `claims.json` AND must not be `source.kind: "inference"`
- `sample_good_verdict.json` — PASS citing both real claims (the full 2-hop path)
- `sample_bad_verdict.json` — PASS citing the inference-only decoy **and** a claim id that doesn't
  exist at all (fabricated citation)
- `AGENTS.md` / `CLAUDE.md` — guardrail pointer for an agent wired into this folder

## Setup

Python 3 only.

## Test It

```bash
cd docs/graph-engineering/projects/grounded-reviewer
python validate_verdict.py sample_good_verdict.json   # expect: GROUNDED, exit 0
python validate_verdict.py sample_bad_verdict.json     # expect: NOT GROUNDED, 2 issues, exit 1
```

The bad sample fails for 2 independent reasons at once — worth reading both: a fabricated claim id
("claim_zzz" doesn't exist), and an honest-but-insufficient one (the decoy claim exists but is
`inference`-sourced, so it cannot ground a PASS by itself).

## Apna Kaam Karo (Wire Into a Real Loop)

1. Pick a loop you already run (e.g. `loop-engineering/projects/daily-triage-demo/` or your own).
2. Give its reviewer subagent this folder's `claims.json` as its evidence, and require it to return
   `reviewer_schema.json`-shaped verdicts.
3. Run 5 real beats. For at least one, engineer a claim with no real supporting edge and confirm the
   reviewer returns REVISE with a named `required_evidence`, not a vague "seems off."
4. Pipe every verdict through `validate_verdict.py` before trusting it.

## Done Jab (Self-Check)

- [ ] Good and bad samples both give the expected `validate_verdict.py` result
- [ ] Wired into a real loop, 5 beats run
- [ ] At least one beat came back REVISE with a named missing edge (not a shape-only "no")
- [ ] Maker's next attempt either produced the real evidence (a new claim in `claims.json`) or withdrew
      the claim — either way, the graph changed, not just the report

---
[⬆ Practice Projects Index](../../08-practice-projects.md)
