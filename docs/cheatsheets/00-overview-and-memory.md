# 00 — Getting Started & CLAUDE.md Memory (Panels 1-4)

Yeh pehla file hai "Claude Code Workflow Cheatsheet" (2026 Edition) ka — jo book ke "References &
Companions" group mein ek dense, 16-panel reference card hai, prose nahi. Yahan panel 1 se 4 cover
hote hain: install karna, CLAUDE.md samajhna, memory file hierarchy, aur project file structure.

## Panel 1: ⚡ Getting Started

Install native CLI do tareeqon se hota hai, platform ke hisaab se:

- **Mac/Linux/WSL** — `curl` based installer
- **Windows PowerShell** — `irm` based installer

Install hone ke baad flow simple hai:

```
cd your-project && claude
```

Pehli baar project mein `/init` chalao — yeh poora codebase scan karta hai aur apne se ek
`CLAUDE.md` bana deta hai. Authentication `claude login` se hoti hai (browser ke zariye). Agar IDE
mein kaam karna ho to **VS Code** aur **JetBrains** dono ke apne extensions maujood hain. Install
sahi hua ya nahi, yeh confirm karne ke liye:

```
claude --version
```

## Panel 2: 🧠 Understanding CLAUDE.md

`CLAUDE.md` Claude Code ki **persistent memory** hai — har session ke start mein yeh file load hoti
hai, is wajah se usay dobara context dena nahi parta. Isay likhne ka framework teen hisson mein
bata hai:

- **WHAT** — tech stack, directory map, architecture
- **WHY** — module ka purpose, design decisions (kyun yeh raasta chuna gaya)
- **HOW** — build/test commands, workflows, gotchas (jo cheezein baar baar ghalat ho jaati hain)

Misaal ke tor pe, cheatsheet ek `# Project: MyApp` wala block dikhati hai jo FastAPI + React +
Postgres stack describe karta hai, npm commands list karta hai, aur architecture tree deta hai —
kuch is tarah ka shape:

```markdown
# Project: MyApp

## What
- Stack: FastAPI (backend) + React (frontend) + Postgres (db)
- Directory map: /api, /web, /db

## Why
- FastAPI chosen for async perf; Postgres for relational integrity

## How
- `npm run dev` — start frontend
- `npm test` — run frontend tests
- Gotcha: migrations run manually, not auto-applied
```

Yeh sirf shape samjhane ke liye hai — asal CLAUDE.md har project ka apna hota hai, lekin WHAT/WHY/HOW
teeno hisse hamesha hone chahiye.

## Panel 3: 📂 Memory File Hierarchy

CLAUDE.md sirf ek jagah nahi rehta — chaar levels hain, har ek apna scope:

| File | Scope | Note |
|---|---|---|
| `~/.claude/CLAUDE.md` | Global | sab projects pe lagu |
| `CLAUDE.md` | Project | git pe shared |
| `.claude/CLAUDE.md` | Project | alternative location |
| `./src/CLAUDE.md` | Subfolder | scoped context |

**Rules jo follow karni hain:**

- Har file **200 lines se kam** rakho
- Subfolder files **append** karti hain context, kabhi **overwrite** nahi karti
- Git mein commit karo taake poori team share kar sake

## Panel 4: 📁 Project File Structure

Ek typical project ka `.claude/` layout is tarah dikhta hai:

```
CLAUDE.md
.claude/
  settings.json
  settings.local.json
  skills/
    code-review/SKILL.md
    testing/SKILL.md
  commands/
    deploy.md
  agents/
    reviewer.md
.gitignore
```

**Kya kahan rehta hai:**

- `settings.json` — **shared team config**, git mein commit hoti hai
- `settings.local.json` — **personal overrides**, `.gitignore` mein hoti hai (kabhi commit nahi)
- `commands/` — custom slash commands jo team share karti hai
- `agents/` — custom subagent definitions

---
[⬅ Index](README.md) · [Next ➡](01-skills-hooks-permissions.md)
