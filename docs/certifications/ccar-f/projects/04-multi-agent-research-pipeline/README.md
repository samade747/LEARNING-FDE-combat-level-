# CCAR-F Exercise 4 — Design and Debug a Multi-Agent Research Pipeline

*Official exam guide, Section 8, Exercise 4 (see [`../../03-how-to-prepare-and-sample-questions.md`](../../03-how-to-prepare-and-sample-questions.md)). Also Track B syllabus's **Required Architect Project 4** (Week 11). Domains reinforced: 1 (Agentic Architecture & Orchestration), 2 (Tool Design & MCP Integration), 5 (Context Management & Reliability).*

A coordinator/subagent research pipeline covering the exercise's full 5-step shape: multiple
subagents dispatched in one turn, structured findings that keep content separate from metadata
(claim/evidence/source/date), a simulated subagent timeout that does not take down the whole run,
and synthesis that preserves conflicting sources instead of arbitrarily picking one. No real API
calls — every subagent is a plain Python function, so the coordinator's *control flow* is fully
testable offline.

## Files

- `research_pipeline.py` — `dispatch_subagents` (steps 1+2: runs every subagent task, catches a
  `SubagentTimeout` from any one of them without losing the others), `synthesize` (steps 3+5:
  groups findings by subject, marks a subject "contested" the moment two findings disagree, never
  silently resolves to one), `build_report` (step 4's second half: adds a `coverage_gaps` list
  naming every task that failed, so a partial run is never presented as complete).
- `test_research_pipeline.py` — 5 offline pytest tests, one per exercise step's success condition.

## Kaise Chalayein

```bash
pip install pytest
pytest test_research_pipeline.py -v
```

## Done Jab (Official Exercise's 5 Steps, Self-Check)

- [x] Coordinator dispatches ≥2 subagent tasks, each gets its own query directly (no reliance on
      automatic context inheritance) — `dispatch_subagents`, `pytest::test_parallel_dispatch_collects_all_findings`
- [x] Multiple tasks handled in one dispatch pass (the exercise's "parallel" is about the request
      shape — several `Task` calls in one coordinator turn — not literal OS threads; `elapsed_s` in
      the return value is where a real harness would report the measured latency win)
- [x] Structured findings separate content from metadata: `subject`/`claim`/`evidence_excerpt`/
      `source`/`published_date` on every finding, never collapsed to prose
- [x] Subagent timeout produces a structured error (`failure_type`, `attempted_query`,
      `partial_results`) and the coordinator proceeds with the other tasks' results —
      `pytest::test_timeout_produces_structured_error_and_preserves_other_tasks`
- [x] Final output is annotated with `coverage_gaps` for anything that failed —
      `pytest::test_report_includes_coverage_gaps_for_failed_tasks`
- [x] Conflicting sources preserved with attribution, never arbitrarily resolved — status is
      `"contested"` when claims disagree, `"well_established"` when they agree —
      `pytest::test_synthesis_preserves_conflicting_sources_without_picking_a_winner` +
      `pytest::test_synthesis_marks_agreeing_sources_well_established`

## Exam Connection

Step 5 is the trap this project is built around: two credible sources report different numbers for
the same subject, and the wrong move is picking one (even the "more recent" or "more authoritative"
one) and presenting it as settled. `synthesize()` structurally cannot do that — a subject's `status`
only reads `"well_established"` when every finding's `claim` is identical; any disagreement forces
`"contested"` and keeps every source visible to the reader.

---
[⬅ CCAR-F Projects Index](../README.md)
