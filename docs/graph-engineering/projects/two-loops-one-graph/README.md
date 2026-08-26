# Graph Project 8 — Two Loops, One Graph (Capstone)

**Concept:** Everything · **Time:** A weekend, then a week of beats · **Difficulty:** Capstone

Two loops over one graph. A triage loop writes claims with real tool-output sources. A changelog loop
reads them through a bounded, 2-hop context builder — never a file dump. Both ground their verdicts. A
pre-commit-style guard enforces schema + append-only.

## Files

- `graph/SCHEMA.md`, `graph/entities.json`, `graph/claims.json`, `graph/runs.json` — a small starter
  graph: `test_payments_flaky` has **two live, conflicting** diagnoses (`tz_default_utc` from one
  triage run, `payment_gateway_timeout` from a later one) — neither supersedes the other, on purpose
- `evidence/run_log.txt` — the raw `pytest` output both diagnosis claims point to
- `precommit_check.py` — schema (required fields, resolvable `supersedes`, real source or honest
  inference) + **append-only** enforcement (given an old + new version, blocks any mutation or deletion
  of a previously-committed claim)
- `context_builder.py` — Concept 9's bounded subgraph: resolve entities from a task string, expand 1-2
  hops, prioritize recent/non-inference claims, **surface conflicts instead of hiding them**, cap the
  result, keep stable claim ids for citing
- `bad-mutated-claims-example.json` — a deliberately broken next-version (mutates one claim, deletes
  another) to prove the guard catches both
- `AGENTS.md` / `CLAUDE.md` — guardrail pointer for the two loops operating here

## Setup

Python 3 only.

## Test It (Verified)

```bash
cd docs/graph-engineering/projects/two-loops-one-graph

# 1. Schema + append-only guard
python precommit_check.py graph/claims.json                                        # OK to commit
python precommit_check.py bad-mutated-claims-example.json --against graph/claims.json  # BLOCKED, 2 issues

# 2. Bounded context for a real task
python context_builder.py "why does test_payments_flaky fail?" --max-claims 10
```

The context builder call returns 4 claims (2 hops from `test_payments_flaky`: the 2 diagnoses, its
`involved_in` link to `checkout_service`, and that service's `depends_on` link to `payment_gateway`)
**and a `conflicts` entry** naming both diagnosis claims — exactly what a grounded reviewer needs to
demand a real resolution instead of silently trusting whichever claim came first.

## Apna Kaam Karo (The Real Capstone)

1. Wire an actual **triage loop** that writes new claims here from real tool output (reuse
   `loop-engineering/projects/daily-triage-demo/` or your own), guarded by `precommit_check.py` before
   any commit.
2. Wire an actual **changelog loop** that calls `context_builder.py` for its task and writes a
   changelog entry — it must never read `graph/claims.json` directly.
3. Give the triage loop's throughput (claims written per day) a **counter-metric** a second loop
   watches (e.g. "% of claims later superseded" — a high number means the triage loop is writing
   claims too fast to verify, Concept 12's gaming failure).
4. Resolve the `test_payments_flaky` conflict for real: add a `claim_0005` with real evidence deciding
   between `tz_default_utc` and `payment_gateway_timeout` (or both, if both are partially true) —
   append-only, never edit `claim_0001`/`claim_0002`.

## Done Jab (Self-Check)

- [ ] `precommit_check.py` passes on the good graph, blocks the bad-mutated example with both violations named
- [ ] `context_builder.py` returns the conflict for `test_payments_flaky`, not a silently-picked answer
- [ ] Real triage + changelog loops wired, guarded by the pre-commit check
- [ ] Changelog loop correctly reports a fix it never witnessed, because the graph carried it
- [ ] **You can walk from a changelog line back through the claim, the run, and the captured tool
      output** (`evidence/run_log.txt`) **to something no model wrote.** When that walk succeeds, you
      have built shared memory with anchors.

---
[⬆ Practice Projects Index](../../08-practice-projects.md)
