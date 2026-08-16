# 10 — Quick Reference

## 7 Principles, Ek Ek Line Mein

**5 Doing-Principles** (kaam kaise hota hai):

1. **Bash is the Key.** Haathon ko brief karo, dimagh ko nahi.
2. **Code as Universal Interface.** Shape specify karo; prose ki ambiguity khatam karo.
3. **Verification as a Core Step.** "Looks right" hi failure mode hai. Check force karo.
4. **Small, Reversible Decomposition.** Atomic units. Har ek verify karo. Har ek commit karo.
5. **Persisting State in Files.** Conversation volatile hai. Files memory hain.

**2 Operating Principles** (discipline real projects mein kaise survive karta hai):

6. **Constraints and Safety.** Constraints autonomy ko enable karte hain, limit nahi.
7. **Observability.** Aap sirf woh direct kar sakte ho jo dekh sakte ho.

## Four-Phase Workflow

```text
EXPLORE   → read & summarize (read-only)
PLAN      → structured plan banao, save karo, review karo
IMPLEMENT → chote steps, har ek verify, har ek commit
COMMIT    → final verification, summary, rules file update
```

## 5 Failure Patterns

| Pattern | Reach For |
| --- | --- |
| The Drift (brief se bhatakta hai) | Persistence (P5) |
| The Confident Wrong (plausible lekin galat) | Verification (P3) |
| The Big Bang (ek change ghanto barbaad kare) | Decomposition (P4) |
| The Scope Creep (unauthorized cheezein chhue) | Constraints (P6) |
| The Black Box (pata nahi kya hua) | Observability (P7) |

## Autonomy Ladder

```text
Watching closely → Ambient supervision → Walk away → Act without asking → Scheduled
```

Har task type ke liye ek rung, track record ke sath. Task type badle to **neeche utro.**

## Principles Har Tool Mein Kahan Milte Hain

| Principle | Claude Code | OpenCode | Cowork | OpenWork |
| --- | --- | --- | --- | --- |
| 1. Bash | Terminal | Terminal | Local Linux VM | Local Linux VM |
| 2. Code-as-Interface | Code blocks, schemas | Same | Templates, .xlsx schemas | Same |
| 3. Verification | Tests, hooks | Tests, plugins | Rubric pass, cross-model | Same |
| 4. Decomposition | Git commits, `Esc Esc` | Git commits, `/undo` | Numbered versions | Numbered versions, `/undo` |
| 5. Persistence | `CLAUDE.md` | `AGENTS.md` (+`CLAUDE.md` fallback) | `CLAUDE.md` | `AGENTS.md` |
| 6. Constraints | `.claude/settings.json` | `opencode.json` | Folder/connector/approval | Same |
| 7. Observability | Terminal stream | Terminal stream | Execution view | Execution view timeline |

## Jab Kuch Ghalat Mehsoos Ho

```text
Agent bina progress apologize kar raha hai, wahi cheez baar baar likh
raha hai, pehle wali constraint se contradict kar raha hai, aisi scope
propose kar raha hai jo mangi nahi thi?
    → Context poison ho chuka hai. Type karna band karo. Reset karo aur
       ek file se continue karo. Naye prompt se fix karne ki koshish mat karo.
```

---
[⬅ Worked Example + Capstone](09-worked-example-capstone.md) · [⬆ Index](README.md)
