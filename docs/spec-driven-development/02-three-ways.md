# 02 — Three Ways: claude.ai, Claude Code, OpenCode

Wahi constitution, wahi 4 phases, 3 jagah chalane ki.

## Concept 9: Way 1 — claude.ai (Main Method)

**2 building blocks:** **Projects** (persistent workspace, custom instructions) aur **Artifacts**
(editable documents chat ke bagal mein).

**Setup:** Project banao ("Smart Notes"), constitution custom instructions mein daalo, research/docs
Project knowledge mein upload karo.

**4 phases, har ek Artifact banati hai:**
- **Research** → findings Artifact
- **Specify** → `spec.md` Artifact, panel mein directly edit karo
- **Clarify** → interview prompt paste karo, jawab spec Artifact mein fold ho jate hain
- **Build** → `plan.md` → `tasks.md` → task-by-task implement, har code file apni Artifact

> **Project zaroori kyun:** Constitution + spec har chat mein loaded rehte hain — fresh conversation
> khol kar implementation kar sakte ho bina dobara explain kiye.

**ChatGPT/Gemini bhi same discipline chalate hain:** ChatGPT — Projects (constitution) + Canvas
(documents). Gemini — Gem (constitution) + Canvas.

> **Ehtiyat:** Private source code, customer data, secrets **kisi bhi web assistant mein paste mat
> karo.** Sensitive kaam ke liye repo-based agent apne approved environment mein use karo.

## Concept 10: Way 2 — Claude Code (Repo Mein Discipline)

- **Constitution ek file hai jo Claude har session parhta hai** — `CLAUDE.md`, `/init` chalao phir trim
  karo
- **Plan mode Specify/Clarify gate hai, enforced** — `Shift+Tab` read-only mode, code nahi likh sakta
  jab tak approve na karo
- **Subagents parallel research karte hain** bina main context pollute kiye
- **Agent apni task list khud maintain karta hai** — aap supervise karte ho, review karte ho, har step
  ke baad commit karte ho (clean rollback point)

Sab 4 artifacts **plain files** hain — spec version control mein hai, PR mein review kar sakte ho.

## Concept 11: Way 3 — OpenCode (Koi Bhi Model)

Sab kuch Concept 10 jaisa: `AGENTS.md` constitution, **Plan** mode (`Tab`), subagents research, git-backed
`/undo`. **Ek naya cheez: model choice** — spec/plan phases strong reasoning model chahte hain, agreed
task list build karna sasti model (`deepseek-v4-flash`) pe theek chalta hai.

---
[⬅ The Method](01-the-method.md) · [Agla: Complete Worked Example ➡](03-worked-example.md)
