# Cheatsheets — Answer Key

1. **Exit code 2** — `0` allows, `2` blocks. (Only `2` actually stops the action.)
2. **`.claude/settings.local.json`** — personal overrides, gitignored, never shared with teammates.
3. **Appends scoped context; it never overwrites the root file** — subfolder CLAUDE.md files add to
   context, they don't replace what's above them.
4. **Rewrite the `description` field to be specific** — it's the field that drives auto-activation;
   vague descriptions mean Claude can't match the task to the skill.
5. **Team one in `.mcp.json` (project root, committed to git); personal one in `~/.claude.json`.**
6. **Add `"Read:env:*"` to the `deny` list** — deny always wins over ask/allow, and this blocks the
   whole `env` pattern deterministically, not just one file path.
7. **L3 — Hooks** — the only layer that deterministically blocks (exit code 2), not just suggests
   caution in a markdown file.
8. **`claude -p "review" --output-format json --allowedTools Read,Grep`** — `-p` for non-interactive,
   JSON output for parsing, `--allowedTools` restricts to read-only.
9. **It uses the `ANTHROPIC_API_KEY` environment variable** — no browser needed in CI.
10. **`/compact` first; only `/clear` if things are still off afterward** — the rule of thumb, not
    jumping straight to a full reset.
11. **Agent Teams, because they have a team lead, shared task list, and mailbox; subagents are
    isolated parallel workers** — subagents don't coordinate with each other by default.
12. **Secret scanning, which blocks commits containing API keys or tokens.**
13. **`claude-opus-4-6` for (a) [deep architecture tradeoff], `claude-haiku-4-5` for (b) [fast, cheap,
    low-stakes tweaks].**
14. **`/loop 10m`** — interval syntax takes a number plus a unit (s/m/h/d).
15. **Interactive for the bug** [exploring, debugging benefits from back-and-forth], **`/loop` for the
    polling** [recurring, unattended checks].
