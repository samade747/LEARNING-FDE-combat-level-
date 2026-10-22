# 04 — Multi-Agent Parallel Work & Git/PR Workflows (Panels 13-14)

Yeh file batati hai ke kaam ko parallel kaise chalaya jaye (multiple agents), aur Git/PR cycle mein
Claude Code kitna automate kar deta hai.

## Panel 13: 🤖 Multi-Agent Parallel Work

Teen tareeqe hain kaam parallel karne ke:

- **Subagents** — `Agent` tool ke zariye parallel workers, **isolated** context ke sath
- **Agent Teams** — ek team lead + teammates, **shared task list** aur **mailbox**
- `/loop 5m` — ek prompt ko interval pe repeat karo (unit `s`/`m`/`h`/`d` — second/minute/hour/day)

Subagent definition file `.claude/agents/reviewer.md` jaisi dikhti hai — frontmatter mein `name`,
`description`, `model`, `tools`; body mein review instructions:

```markdown
---
name: reviewer
description: Reviews code changes for correctness and style
model: claude-sonnet-4-6
tools: [Read, Grep, Bash]
---

Review the diff. Flag correctness bugs and style issues. Be concise.
```

**Zaroori notes:**

- **Worktrees** — har agent ko apni **isolated git copy** milti hai
- **Shift+Down** — Agent Teams mein teammates ke darmiyan cycle karo
- `/agents` — saari agent definitions list aur manage karo

## Panel 14: 🌿 Git & PR Workflows

Claude Code Git/PR cycle ke char hisson mein kaam automate karta hai:

- **Commits** — diff se conventional commit message **auto-generate** karta hai
- **Branches** — feature branches banata hai, upstream push karta hai
- **Pull requests** — `gh` ke zariye title, description, files likhta hai
- **Code review** — diffs parh kar structured feedback deta hai

**Safety net:** secret scanning un commits ko **block** karti hai jin mein API keys ya tokens ho.

**Natural-language examples** jo yeh workflows trigger karte hain:

- "commit these changes"
- "create a PR for this branch"
- "review the last 3 commits"

---
[⬅ Prev](03-models-ci-mcp.md) · [Next ➡](05-cost-management-and-quick-reference.md)
