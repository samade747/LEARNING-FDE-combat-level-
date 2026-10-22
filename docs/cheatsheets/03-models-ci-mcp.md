# 03 — Modes & Models, Non-Interactive/CI, MCP Servers (Panels 10-12)

Yeh file teen alag concerns cover karti hai: konsa model kab use karo, Claude Code ko scripts/CI mein
kaise chalao, aur external tools ko MCP se kaise connect karo.

## Panel 10: 🧠 Modes & Models

Teen models available hain, har ek ka apna trade-off:

| Model | Kab Use Karo |
|---|---|
| `claude-opus-4-6` | Most capable — deep reasoning |
| `claude-sonnet-4-6` | Balanced — daily coding |
| `claude-haiku-4-5` | Fastest — quick tasks, lowest cost |

**Context window:** up to **1M tokens**, with **auto-compression** (khud context ko compress karta
hai jab zaroorat ho).

**Shortcuts aur commands:**

- **⌥P** (Alt+P) — model switch karo, **context preserved** rehta hai
- **⌥T** (Alt+T) — extended thinking toggle karo
- `/rc` — **remote control**: claude.ai web se CLI ko control karo
- `/fork` — conversation ko **branch** karo, alternatives explore karne ke liye

## Panel 11: 🤖 Non-Interactive & CI

Claude Code scripts/pipelines mein bhi chal sakta hai, `-p` flag (print/single-shot mode) ke zariye:

```
claude -p "add error handling"
```

Content pipe bhi kar sakte ho:

```
cat logs.txt | claude -p "summarize errors"
```

Scripting ke liye JSON output:

```
claude -p "list TODOs" --output-format json
```

CI mein tools restrict karna ho:

```
claude -p "review" --allowedTools Read,Grep
```

**CI auth:** `ANTHROPIC_API_KEY` environment variable set karo. **Exit code 0** success pe milta hai
— isliye pipelines mein fit ho jata hai (standard CI convention). Use cases: **GitHub Actions**,
**pre-commit hooks**, **build scripts**.

## Panel 12: 🔌 MCP Servers

MCP = **Model Context Protocol** — external tools ko ek standardized interface ke zariye connect
karne ka tareeqa.

```json
{
  "mcpServers": {
    "example": {
      "command": "npx",
      "args": ["-y", "@example/mcp-server"]
    }
  }
}
```

**Locations:**

- **Project:** `.mcp.json` (project root) — git ke zariye team ke sath shared
- **User:** `~/.claude.json` — `mcpServers` block ke andar, personal setup

MCP servers databases, APIs, browsers, cloud services sab ko connect karte hain — community mein
**hundreds** of servers available hain.

---
[⬅ Prev](02-architecture-and-workflow.md) · [Next ➡](04-multi-agent-and-git.md)
