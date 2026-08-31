# Tool Diet Worksheet — daily-triage-demo

Filled 2026-09-01 while doing Harness Project 4, against
[`../../../loop-engineering/projects/daily-triage-demo/`](../../../loop-engineering/projects/daily-triage-demo/).

## Two surfaces, two lists

`daily-triage-demo` has **no `.claude/settings.json`** — so the main triage skill runs with the
default full tool set. The **`reviewer` subagent** is already scoped tight in its own front-matter.

### Surface 1 — main `daily-triage` skill (implicit full list)

| Tool | Actually used by the skill? | Keep? |
| --- | --- | --- |
| `Bash` | Yes — `pytest`, `git worktree`, `git branch`, `git diff` | ✅ keep |
| `Read` | Yes — `progress.md`, `ISSUES.md`, test files | ✅ keep |
| `Edit` / `Write` | Yes — drafts the smallest fix; rewrites `progress.md` | ✅ keep |
| `Task` (subagent) | Yes — calls the `reviewer` subagent | ✅ keep |
| `Glob` / `Grep` | Marginal — could find the failing test, but `pytest -v` already names it | 🔶 keep Grep, drop Glob |
| `WebFetch` / `WebSearch` | No — the demo is fully local, no external lookup | ❌ deny |
| `NotebookEdit` | No — no notebooks in this repo | ❌ deny |
| Any MCP connector (Gmail, Drive, …) | No — mock data only (`ISSUES.md`) | ❌ deny |

### Surface 2 — `reviewer` subagent (already lean)

| Tool exposed | Why it needs it |
| --- | --- |
| `Read` | Read the diff, the tests, `ISSUES.md` |
| `Bash`, restricted to `python -m pytest*` and `git diff*` | Run the suite itself; see the change. Everything else Bash = deny |
| `edit: deny` | It is read-only by contract — cannot "fix" what it reviews |

## After (trimmed list) — proposed `daily-triage-demo/.claude/settings.json`

```json
{
  "permissions": {
    "deny": [
      "WebFetch", "WebSearch", "NotebookEdit",
      "Glob",
      "mcp__*"
    ]
  }
}
```

## Week of runs

| Date | Run # | Wrong-tool incident? |
| --- | --- | --- |
| 2026-09-01 | 1 (Project 8 capstone, prior) | None — skill only used Bash/Read/Edit/Task |
| 2026-09-01 | 2 (Project 8 re-run, prior) | None — recognised already-done work, no tool calls |

*(Project 8 was already run twice in Loop Engineering practice — both beats stayed inside
Bash/Read/Edit/Task. No web or connector tool was ever attempted.)*

## Verdict

- Before count (main skill): ~11 tool types available (full default set)
- After count: ~6 (`Bash`, `Read`, `Edit`, `Write`, `Grep`, `Task`)
- Wrong-tool incidents before: **0** · after: **0**

**Result = the "already lean" case.** This particular loop never reached for a wrong tool because
its job (local files + pytest + git + one subagent) is narrow and the prompt is specific. The diet
is still worth applying as *defence in depth* — it removes the ability to exfiltrate via `WebFetch`
or a connector if a future prompt or injected issue tried to — but it did not fix an existing
misrouting problem here. The `reviewer` subagent is the better example of the principle already in
practice: `bash: "*": deny` with a 2-command allowlist.
