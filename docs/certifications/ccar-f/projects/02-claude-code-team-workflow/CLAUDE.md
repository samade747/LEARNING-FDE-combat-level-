# Team Development Workflow — Coding Standards

*Project-level CLAUDE.md, Exercise 2 step 1. Applies to every developer on clone/pull —
version-controlled, not personal (`~/.claude/CLAUDE.md` is for that).*

## Coding standards

- TypeScript strict mode everywhere; no `any` without a `// justified:` comment.
- One export per file for anything under `src/api/`.
- Errors are returned as `{ errorCategory, isRetryable, message }`, never thrown bare strings.

## Testing conventions

- Every new function in `src/` needs a colocated `*.test.*` file.
- Tests must not hit the network — mock external calls.
- Run `npm test` before claiming a change is done; never assert tests pass without running them.

## Directory map

- `src/api/` — HTTP handlers. See `.claude/rules/api-conventions.md` for path-specific rules.
- `src/web/` — frontend. No special rules yet.

See `.claude/rules/` for path-scoped conventions and `.claude/skills/team-review/` for the
team's shared review skill.
