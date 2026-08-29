# Rules — dreaming-loop-demo

Base loop (the `daily-triage` skill) follows these when fixing issues in this repo.

## Workflow

1. Work on a `claude/<short-description>` branch in an isolated worktree — never on `main`.
2. After a fix, hand the reviewer subagent the branch name explicitly.
3. Reviewer PASS + all tests green before a branch is marked ready-to-merge.
4. Risky or public-facing changes → escalate to a human, do not self-merge.
5. Update `progress.md` with a dated entry after every run.

## Style

- Keep functions under 40 lines.
- Always update `CHANGELOG.md` before committing a fix.
- Prefer standard library over new dependencies.

## Escalation

- A breaking change to any public interface is a human decision.
- If you cannot make progress in 3 review rounds, stop and escalate.
