# 05 — Context & Cost Management, Quick Reference (Panels 15-16)

Aakhri file: context lamba ho jaye to kya karna hai, aur phir poori cheatsheet ka ek consolidated
quick-reference.

## Panel 15: 💰 Context & Cost Management

Teen commands context/cost manage karne ke liye:

- `/compact` — context lamba ho jaye to **summarize aur compress** karo
- `/clear` — session **confused** ho jaye to **full reset**
- `/cost` — kabhi bhi session ka **spend check** karo

System **auto-compresses** jab token limits ke qareeb pohonchte ho. Best quality ke liye **~20 turns**
har session mein fresh session start karne ki practice rakho.

**Rule of thumb:** pehle `/compact` try karo; agar phir bhi off lage, to `/clear` kar ke dobara shuru
karo.

## Panel 16: 📌 Quick Reference

### Core Commands

| Command | Kaam |
|---|---|
| `/init` | Generate CLAUDE.md |
| `/compact` | Compress context |
| `/clear` | Reset conversation |
| `/cost` | Session spend |
| `/fork` | Branch conversation |
| `/rc` | Remote from claude.ai |
| `/loop 5m` | Repeat on interval |
| `/btw` | Side question, ephemeral |
| `/diff` | Review pending changes |
| `/agents` | List agent definitions |

### Key Shortcuts

| Shortcut | Kaam |
|---|---|
| ⌥P / Alt+P | Switch model |
| ⌥T / Alt+T | Extended thinking |
| Ctrl+G | Text editor |
| Ctrl+B | Background task |
| Ctrl+T | Toggle task list |
| Shift+Tab | Cycle mode |
| Shift+Down | Cycle teammates |
| Esc Esc | Rewind last turn |
| `!` | Bash mode inline |

### When to Use

| Scenario | Use |
|---|---|
| Exploring, debugging, learning | Interactive |
| CI/CD, automation, scripts | `-p` flag |
| Complex features, unclear scope | Plan mode |
| Multi-file parallel work | Agent Teams |
| Monitoring, polling, recurring | `/loop` |
| Control CLI from web UI | `/rc` |
| Hard bugs, architecture | ⌥T thinking |

---

*"Claude Code Workflow Cheatsheet — Created 2026 — Anthropic's agentic coding CLI & IDE extensions."*
— yeh footer note khud source cheatsheet mein hai.

---
[⬅ Prev](04-multi-agent-and-git.md) · [Next ➡](06-test-your-understanding.md)
