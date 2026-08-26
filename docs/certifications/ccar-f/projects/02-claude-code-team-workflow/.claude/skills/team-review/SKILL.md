---
name: team-review
description: >-
  Runs the team's shared code-review checklist over the current diff and reports
  findings. Use whenever asked to review a PR, review the diff, or run team-review.
context: fork
allowed-tools: ["Read", "Grep", "Glob"]
argument-hint: "[optional: path or PR number]"
---

# Team review

Read-only review, isolated from the main conversation (`context: fork` — its exploration
output never pollutes the caller's context; `allowed-tools` is scoped to read-only tools so
this skill cannot edit files even by accident).

1. Find the changed files (`git diff --name-only` against the base branch, or the path given
   in `$ARGUMENTS`).
2. For each changed file under `src/api/`, check it against `.claude/rules/api-conventions.md`.
3. For each changed test file, check it against `.claude/rules/testing-conventions.md`.
4. Report findings as a short list: file, line, what's wrong, which convention it violates.
   No fixes — this skill only reports.
