# Cheatsheets — Summary

"Claude Code Workflow Cheatsheet (2026 Edition)" — 16 dense panels, prose nahi. Fetched: Zia Tutor AI
generation 82, single window (complete), 2026-10-22.

## 00 — Getting Started & CLAUDE.md Memory (Panels 1-4)

- Install: `curl` (Mac/Linux/WSL) ya `irm` (Windows PowerShell). `/init` codebase scan karta hai,
  CLAUDE.md auto-banata hai. `claude login`, `claude --version`.
- CLAUDE.md = persistent memory, WHAT/WHY/HOW framework.
- Memory hierarchy: `~/.claude/CLAUDE.md` (global) → `CLAUDE.md` (project) → `.claude/CLAUDE.md`
  (project alt) → `./src/CLAUDE.md` (subfolder, **append karta hai, overwrite nahi**). 200 lines se
  kam rakho.
- Project structure: `.claude/{settings.json (shared), settings.local.json (personal, gitignored),
  skills/, commands/, agents/}`.

## 01 — Skills, Hooks & Permissions (Panels 5-7)

- **Skills:** `.claude/skills/name/SKILL.md`, `description` field **critical** for auto-activation.
  Explicit: `/skill-name`.
- **Hooks:** PreToolUse/PostToolUse/Notification. Exit codes: **0=allow, 2=block**. Input via
  stdin/POST body.
- **Permissions:** `Tool:arg:glob` pattern, allow/deny lists, `defaultMode` (plan/auto/default).

## 02 — Architecture & Daily Workflow (Panels 8-9)

- **4-Layer Architecture:** L1 CLAUDE.md → L2 Skills → L3 Hooks → L4 Agents.
- **Daily pattern (8 steps):** cd+claude → Plan Mode (Shift+Tab) → describe intent → Auto Accept →
  `! git status` → `/compact` → Ctrl+B (background) → Esc Esc (rewind).

## 03 — Models, CI/CD & MCP Servers (Panels 10-12)

- Models: `claude-opus-4-6` (deep reasoning), `claude-sonnet-4-6` (balanced daily), `claude-haiku-4-5`
  (fastest/cheapest). Context up to 1M tokens, auto-compression.
- Non-interactive: `claude -p "..." --output-format json --allowedTools Read,Grep`. CI auth via
  `ANTHROPIC_API_KEY`.
- MCP: `.mcp.json` (project, shared) vs `~/.claude.json` (personal).

## 04 — Multi-Agent Work & Git/PR Workflows (Panels 13-14)

- Subagents (isolated parallel workers) vs Agent Teams (team lead + shared task list + mailbox).
  `/loop 5m` repeats on interval.
- Git: auto commit messages, branches, PRs via `gh`, **secret scanning blocks commits with API
  keys/tokens**.

## 05 — Cost Management & Quick Reference (Panels 15-16)

- `/compact` first, `/clear` if still off. `/cost` checks spend. Fresh sessions every ~20 turns.
- Quick-reference tables: core commands, key shortcuts, "when to use" (interactive/`-p`/plan
  mode/Agent Teams/`/loop`/`/rc`/extended thinking).

## 06 — Test Your Understanding

- 15-question self-authored scenario quiz, grounded only in panels 00-05 (no book quiz block in
  source) + `quiz.md` answer key.

No `projects/` folder — pure reference card, no exercises to scaffold.
