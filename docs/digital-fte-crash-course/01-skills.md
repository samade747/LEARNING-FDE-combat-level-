# 01 — Part 1: Skills — Capability Portable Folders Ki Tarah (Concepts 1-5)

## Concept 1 — Agent Skill Kya Hai

**Skill** ek folder hai `SKILL.md` file ke sath (plus optional `scripts/`, `references/`, `assets/`).
Yeh Anthropic ka open standard hai jo koi bhi agent parh sakta hai — Claude Code, OpenCode, aur OpenAI
Agents SDK Worker jo aap bana rahe ho.

```markdown
---
name: hello-skill
description: Greets the user by name and time of day. Use when the user says hello or asks to be greeted.
---

# Hello skill

1. Check the local time of day.
2. Greet the user warmly, by name if known, in under 25 words.
```

Koi code nahi, koi deploy nahi. Chunki yeh disk par ek file hai, skill version, travel, aur review hoti
hai jaise koi text — Python object ya API endpoint jaisi nahi.

**Startup par agent kya load karta hai?** Sirf `name` aur `description` — poora body nahi. Yehi
**progressive disclosure** hai (Concept 2).

## Concept 2 — Progressive Disclosure: 3-Stage Loading

Ek sath 50 skills load karna model ko instructions mein dabaa dega jo usay chahiye hi nahi. Isliye skill
3 stages mein load hoti hai:

**Stage 1, Discovery.** Startup par agent har skill ka `name` + `description` load karta hai (~100
tokens each). 50 skills = ~5,000 tokens per turn.

**Stage 2, Activation.** Jab model task ko description se match kare, poora `SKILL.md` body load hota
hai (~5,000 tokens se kam rakho; zyada tar 500-2,000). Sirf un turns par pay hota hai jo skill use karte
hain.

**Stage 3, Execution.** Body jo files reference kare (`scripts/`, `references/`) sirf tab load hoti hain
jab agent unhe reach kare.

**2 cheezein jo yahan se nikalti hain:** **`description` hi Stage 1 mein fire hoti hai**, isliye woh sab
kuch decide karti hai; aur **lambi bodies har matching turn par cost karti hain**, isliye `SKILL.md`
tight rakho, depth `references/` mein daalo.

## Concept 3 — `description` Hi Trigger Hai, Aur Woh Ek Cheez Jo Aap Own Karte Ho

`SKILL.md` ke 2 hisse: **YAML frontmatter** (contract jo model parhta hai) aur **markdown body**
(instructions jo follow karta hai). Sirf 2 fields required hain: `name`, `description`.

**Description hi poora khel hai.** Scaffold aksar circular likhta hai: *"Summarizes a ticket. Use when
the user wants to summarize a ticket."* Yeh "summarize this ticket" par fire karega lekin "TL;DR this
thread," "handoff note" jaisi real phrasings miss kar dega.

**Achhi description 4 cheezein karti hai:**
- **Kya** produce karti hai (actual output naam lo)
- **Kab** reach karo (real situations)
- **Keywords** jo users type karte hain — **including woh jo obvious lafz kabhi nahi bolte**
- **Ek do-NOT line** look-alikes ke liye jo chup rehne chahiye

**Self-check:** Description se obvious keyword ("summarize") delete karo. Ab bhi bata rahi hai kab fire
karna hai? Nahi to woh bohat narrow hai.

**Body convention se:** imperative ("Read the full thread. List what was tried."), 1-2 real examples
(description se ~5x zyada steering ke liye), aur 2-3 edge cases jo real mein toot chuke hain.

## Concept 4 — Packaging: Skills Kahan Rehti Hain, Kaise Travel Karti Hain

**Ek rule poore course ke liye:** apni skills `.claude/skills/` mein rakho. Claude Code isay parhta hai,
OpenCode fallback karta hai, aur aapke Worker ka SDK seedha isay point karta hai
(`LocalDir(src=".claude/skills")`).

| Tool | Project-level | User-level |
| --- | --- | --- |
| Claude Code | `.claude/skills/<name>/SKILL.md` | `~/.claude/skills/<name>/SKILL.md` |
| OpenCode | `.opencode/skills/<name>/SKILL.md` (phir `.claude/` fallback) | `~/.config/opencode/skills/...` |

Skill folder mein 1 required file + 3 optional folders, relative paths se reference hoti hain (skill ke
apne folder se resolve hoti hain, jahan agent chal raha hai wahan se nahi).

## Concept 5 — Skills Compose Karna: Ek Bari Vs Kai Chhoti

"Weekly customer-health report" ek skill ho sakti hai (research, draft, format, review sab) ya 4 skills
jo filesystem ke through handoff karein.

- **Ek bari skill:** discover karna aasan, ek activation. Lekin har step ek context mein chalta hai,
  kuch reusable nahi, beech mein fail ho to model stale context ke sath recover karta hai
- **Kai chhoti skills:** har ek test/replace/reuse ho sakti hai, failure localized hai, **har step fresh
  activate hota hai**. Cost: zyada discovery entries aur unhe chain karne ka intezam

> **Ek skill likho** jab steps tightly coupled hon aur kabhi akele reuse na hon. **Kai likho** jab koi
> step akela call ho sakta ho, ya clean context wiring se zyada matter kare. **2-3 steps ke baad
> separation usually jeetta hai.**

**Filesystem se chain karo, conversation se nahi.** Skill A `tmp/research-{id}.md` likhti hai, Skill B
isay parh kar `tmp/draft-{id}.md` likhti hai. Conversation sirf final result dekhti hai; beech ke steps
disk par rehte hain — agent, aap, aur audit trail ke liye.

> **Part 2 ka bridge:** Kuch handoffs temp file mein nahi jate — **system of record** mein jate hain. Jo
> skill `tmp/` mein likhe woh draft hai; jo system of record mein likhe woh **action** hai.

---
[⬅ Quick Win](00-quick-win.md) · [⬆ Index](README.md) · [Agla: System of Record ➡](02-system-of-record.md)
