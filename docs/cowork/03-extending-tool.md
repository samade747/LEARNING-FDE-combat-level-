# 03 — Tool Extend Karna

**Decision tree:** Specific procedure follow karwani hai? **Skill.** External service parhna/likhna
hai? **Connector.** Role ke liye skills+connectors ka bundle? **Plugin.** Richer surface chahiye?
**MCP server.**

## Concept 9: Skills

Skill ek **playbook** hai jo co-worker shelf pe rakhta hai — title (kab uthana hai), procedure (kya
karna hai), optional bundled tools. Folder hai jismein `SKILL.md` file hai. **Dono tools same format use
karte hain** — ek tool ke liye likhi skill dusre mein bina badle chalti hai.

```markdown
---
name: weekly-brief
description: Generate the user's weekly status brief from a folder of meeting notes
---
1. List files modified in the last 7 days...
2. Read each meeting-notes file...
5. Save as weekly-brief-YYYY-MM-DD.md
```

**Description sab se zaroori field hai** — spine jo agent decide karne ke liye parhta hai.

**3 tareeqe skills ane ke:** Catalog se (Cowork: Customize > Skills, OpenWork: Settings > Skills > Hub),
**chat mein generate** (`/skill-creator` — sab se sasta pehli custom skill ka rasta), ya **manually
author** karo.

> **Security warning:** Skills **trusted code** hain jo aapke agent environment mein chalti hain,
> kabhi third-party packages install karne ki permission ke sath. Sirf trusted sources se install karo.

## Concept 10: Connectors

**Cowork:** broad catalog (mail, drive, chat, notes, calendar) — Customize > Connectors se. **OpenWork:**
leaner catalog — Settings > Extensions ka "Available apps" grid, ya Custom App.

**Connectors ki asal power combinations mein hai:**
> *"Pichle hafte ka Slack thread Acme deal pe pull karo, Notion page ke sath cross-reference karo, aur
> follow-up email draft karo."* — 3 connectors ek task mein.

**Discipline:** naya connector tab install karo jab **specific workflow** unlock ho raha ho. Speculative
install mat karo — har connector nayi prompt-injection vector kholta hai.

## Concept 11: Plugins

**Zaroori:** lafz "plugin" **dono tools mein alag matlab** rakhta hai. **Cowork plugin** = role bundle
(skills + connectors + slash commands + config, ek download mein — Marketing, Legal, Sales). **OpenCode
plugin** (OpenWork ki UI mein "Plugins (OpenCode)") = npm package with event hooks, engine extend karta
hai. **Ye interchangeable nahi hain.**

> **Real story:** Ek marketer ne 7 plugins ek dopahar mein install kar liye — agli subah `/` type karte
> hi 43 overlapping options mile, ek community plugin ne chup chaap ek MCP server install kar diya jo
> analytics tool tak reach kar rahi thi jo usay yaad hi nahi thi authorize ki. 2 ghante cleanup. **Lesson:
> plugins browser extensions ki tarah install karo — ek dafa mein ek, specific workflow ke sath, monthly
> audit.**

## Concept 12: Subagents

Jab task **parallel work** mein tootta hai, agent **subagents** spawn karta hai — parallel workers jo
har ek apna hissa handle karte hain. 20 contracts sequentially parhne ki bajaye, 4 subagents 5-5 contracts
parallel mein parhte hain. **Main session mein sirf result ata hai, raw documents nahi.**

**3 patterns jo reliably subagents trigger karte hain:**
- **Fan-out** — *"In N items mein se har ek ke liye X karo"* (12 deposition transcripts summarize karo)
- **Dimension** — *"X ko N dimensions mein analyze karo"* (indemnification, liability cap, IP...)
- **Compare** — *"A aur B compare karo"*

**Kab subagents mat use karo:** Genuinely sequential kaam (contract parho → redline draft karo → memo
banao — dependent steps). Chhote batches (3 files parallelize karne layak nahi, threshold ~5-7 items).
Jahan coherence throughput se zyada zaroori ho.

> **Debugging note:** Consistency rules **main task description** mein daalo, subagent prompts mein
> nahi — taake har subagent tak wo pohanchein.

---
[⬅ Rules Aur Instructions](02-rules-instructions.md) · [Agla: Safety Aur Autonomy Ladder ➡](04-safety-autonomy.md)
