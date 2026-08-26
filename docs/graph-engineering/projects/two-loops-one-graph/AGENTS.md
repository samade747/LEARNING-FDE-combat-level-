# Rules — two-loops-one-graph (Capstone)

Guardrail pointer for any agent operating in this folder. See root `AGENTS.md`/`CLAUDE.md` for repo-wide
rules; this file is scoped to this practice project only.

- **Never edit an existing entry in `graph/claims.json` in place.** New evidence is a new claim, with
  `supersedes` pointing at the old one if it replaces it. Run `precommit_check.py <new> --against
  <old>` before treating any change as committed.
- **Never edit `evidence/run_log.txt` retroactively.** It is raw captured tool output — if a run was
  wrong, that itself becomes a new claim, not a silent edit to the log.
- The changelog loop reads **only** what `context_builder.py` returns for its task — never the full
  `graph/claims.json` file directly.
- If `context_builder.py` returns a `conflicts` entry, the changelog loop must surface both sides, not
  silently pick one.
