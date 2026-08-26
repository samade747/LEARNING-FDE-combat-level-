# graph/SCHEMA.md — Contract for This Capstone's Graph

Same 3 files as Part 6: `entities.json` (nodes), `claims.json` (edges-with-receipts), `runs.json`
(which beat wrote what). Plus `evidence/run_log.txt` — raw tool output claims point to, never edited.

## entities.json

`{"id": str, "type": str, "description": str}` — types used here: `Service`, `Test`, `RootCause`.

## claims.json

Same fields as the other projects' `graph-SCHEMA.md`: `id`, `subject`, `predicate`, `object`,
`source` (`kind` + `ref`/`command`, or `inference`), `produced_by`, `supersedes`, `created`.

**Write rules enforced by `precommit_check.py`:**

1. **Append-only.** A commit may add new claims or have a new claim `supersedes` an old one. It may
   **never** mutate or delete a claim that was already committed.
2. **Every claim resolvable.** `supersedes` (if not null) must name a claim id that exists.
2. **Real source or honest inference.** No claim ships without `source.kind`.

## runs.json

`{"id": str, "loop": str, "created": str}` — which loop, which beat, wrote which claims (cross-check
against `claims[].produced_by`).

## Two Loops Sharing This Graph

- **triage loop** — writes claims from real tool output (pytest, CI logs) into `claims.json`
- **changelog loop** — reads a **bounded subgraph** (`context_builder.py`), never the whole file,
  and reports fixes it never directly witnessed because the graph carried them
