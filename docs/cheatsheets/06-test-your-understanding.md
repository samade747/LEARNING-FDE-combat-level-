# 06 — Test Your Understanding (Scenario-Based Quiz)

Yeh quiz khud se likha gaya hai (book ka apna quiz widget nahi), lekin **sirf** upar wali 16 panels
(00 se 05 tak ki files) ke facts se grounded hai — koi bahar ka fact nahi mila. 15 scenario-based
questions, English mein (jaisa is repo ka convention hai). Answer key alag file `quiz.md` mein hai —
pehle khud try karo, phir check karo.

---

### Q1. Blocking a dangerous Bash call

**Q:** You've written a `PreToolUse` hook script that should stop Claude from running a destructive
Bash command. What exit code must the script return to actually block the action?

- Exit code 0
- Exit code 1
- Exit code 2
- Exit code 127

---

### Q2. Personal override that shouldn't leak to teammates

**Q:** You want to raise your own tool timeout locally without changing what your teammates get when
they pull the repo. Which file do you edit?

- `.claude/settings.json`
- `.claude/settings.local.json`
- `~/.claude/CLAUDE.md`
- `.mcp.json`

---

### Q3. A subfolder CLAUDE.md and the root CLAUDE.md disagree on nothing — they just both exist

**Q:** Your project has a root `CLAUDE.md` and a `./src/CLAUDE.md`. What is the relationship between
the two, according to the memory file hierarchy rules?

- The subfolder file overwrites the root file whenever both are loaded
- The subfolder file appends scoped context; it never overwrites the root file
- Only one CLAUDE.md can exist per repository, so this setup is invalid
- The subfolder file is ignored unless `/init` is re-run inside `src/`

---

### Q4. A Skill that never seems to auto-activate

**Q:** You wrote a `SKILL.md` with a short, vague `description` field, and Claude never seems to pick
it up automatically even when the task clearly matches. What's the most likely fix?

- Move the file from `.claude/skills/` to `.claude/commands/`
- Rewrite the `description` field to be specific — it's the field that drives auto-activation
- Add `allowed_tools: ["*"]` to the frontmatter
- Rename the skill folder to match the project name

---

### Q5. Sharing an MCP server config with the whole team vs. keeping one just for yourself

**Q:** You want a database MCP server available to everyone who clones the repo, and a separate
personal MCP server (your own API playground) available only on your machine. Where do these two
configs go, respectively?

- Both in `~/.claude.json`
- Team one in `.mcp.json` (project root, committed to git); personal one in `~/.claude.json`
- Team one in `.claude/settings.json`; personal one in `.mcp.json`
- Both in `.claude/settings.local.json`

---

### Q6. Reading `.env` by mistake

**Q:** You want to make sure Claude can never read your `.env` file, under any circumstance, without
being asked each time. Which permissions block entry accomplishes this?

- Add `"Read(./.env)"` to the `allow` list
- Add `"Read(./.env)"` to the `ask` list
- Add `"Read:env:*"` to the `deny` list
- Set `defaultMode` to `plan`

---

### Q7. Where does a safety gate "live" in the 4-layer architecture?

**Q:** You're deciding where to implement a rule that must deterministically stop a dangerous tool
call before it runs — not just suggest caution in a markdown file. Which layer of the 4-layer
architecture is this?

- L1 — CLAUDE.md
- L2 — Skills
- L3 — Hooks
- L4 — Agents

---

### Q8. Running Claude Code inside a GitHub Actions job

**Q:** You want to call Claude Code non-interactively inside a CI pipeline, restrict it to read-only
tools, and get output you can parse programmatically. Which combination of flags fits?

- `claude --init --json`
- `claude -p "review" --output-format json --allowedTools Read,Grep`
- `claude login --ci --readonly`
- `claude /loop 5m --ci`

---

### Q9. Authenticating Claude Code in a CI environment

**Q:** Inside the CI job from Q8, there's no browser available to run `claude login`. How does Claude
Code authenticate instead?

- It falls back to a device code flow printed in the logs
- It reads credentials from `.claude/settings.json`
- It uses the `ANTHROPIC_API_KEY` environment variable
- CI authentication isn't supported; only interactive sessions can run Claude Code

---

### Q10. Context is getting long mid-session

**Q:** You're deep into a long session and the context feels like it's dragging (slower, less
focused), but the conversation itself isn't confused or off-track yet. What's the recommended first
move, per the rule of thumb?

- `/clear` immediately, to be safe
- `/compact` first; only `/clear` if things are still off afterward
- Switch models with ⌥P
- Start a new project folder

---

### Q11. Parallel code review across five files with shared coordination

**Q:** You need five pieces of a feature worked on at once, with the workers sharing one task list
and able to message each other about overlaps. Subagents (via the `Agent` tool) or Agent Teams —
which fits, and why?

- Subagents, because they share a mailbox by default
- Agent Teams, because they have a team lead, shared task list, and mailbox; subagents are isolated parallel workers
- Neither — this requires `/loop 5m`
- Subagents, because Agent Teams can only have one teammate at a time

---

### Q12. A commit that would leak a secret

**Q:** A teammate accidentally stages a file containing a live API key and asks Claude Code to commit
it. What safety mechanism described in the Git & PR Workflows panel is supposed to catch this?

- The `defaultMode: plan` permission setting
- Secret scanning, which blocks commits containing API keys or tokens
- The `PostToolUse` hook, which always runs after every commit
- `/diff`, which must be run manually before every commit

---

### Q13. Picking a model for a deep architecture decision vs. a quick lookup

**Q:** You have two tasks today: (a) decide on a hard, multi-system architecture tradeoff, and (b) do
a dozen small, fast, low-stakes text tweaks. Which models fit (a) and (b) respectively?

- `claude-haiku-4-5` for (a), `claude-opus-4-6` for (b)
- `claude-opus-4-6` for (a), `claude-haiku-4-5` for (b)
- `claude-sonnet-4-6` for both, since it's the balanced default
- Model choice doesn't affect this; only ⌥T (extended thinking) matters

---

### Q14. Setting up a recurring status check every ten minutes

**Q:** You want Claude to re-run the same monitoring prompt every ten minutes without you re-typing
it. What's the correct command and interval syntax?

- `/loop 10m`
- `/loop --every=10`
- `/rc 10m`
- `/fork 10m`

---

### Q15. Choosing interactive vs. `-p` vs. Agent Teams vs. `/loop`

**Q:** Per the "When to Use" quick-reference table, which mode fits "exploring an unfamiliar bug
interactively," and which fits "polling a deploy status every few minutes until it finishes"?

- Interactive for both
- `-p` flag for the bug, Agent Teams for the polling
- Interactive for the bug, `/loop` for the polling
- Agent Teams for the bug, `-p` flag for the polling

---
[⬅ Prev](05-cost-management-and-quick-reference.md) · [Next ➡](quiz.md)
