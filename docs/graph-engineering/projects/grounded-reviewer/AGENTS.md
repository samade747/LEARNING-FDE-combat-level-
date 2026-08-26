# Rules — grounded-reviewer

Guardrail pointer for any agent operating in this folder. See root `AGENTS.md`/`CLAUDE.md` for repo-wide
rules; this file is scoped to this practice project only.

- A reviewer verdict is **not done** until `validate_verdict.py` returns exit 0 against it.
- Never hand-wave a PASS. Every factual claim in a verdict needs a `grounded_in` id that resolves in
  `claims.json` and is not `source.kind: "inference"`.
- Do not edit `claims.json`'s existing entries. New evidence is a new claim (with `supersedes` if it
  replaces something), never a mutation of an existing one (Concept 8, invariant 4).
