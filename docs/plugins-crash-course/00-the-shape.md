# 00 — Part 1: The Shape (Concepts 1-3)

## Concept 1 — Aap Agent Extend Karte Ho, Own Nahi

Plugin koi program nahi jo aap chalate ho. Yeh pieces ka set hai jo ek **host** load kar ke chalata hai.
Host — Claude Code ya OpenCode — agent loop (decide-act-repeat) own karta hai, model laata hai, user ke
machine par chalta hai. Aapka plugin capabilities aur rules contribute karta hai jo host pick karta hai.

**Pleasing twist:** aap ek coding agent ko **coding agents ke liye plugin** banane ka direct karte ho.
Jo cheez banati hai aur jo cheez extend hoti hai — dono same kism ka tool hain.

## Concept 2 — 2 Hosts, Ek Idea

- **Claude Code** — **declarative bundle**: folder + chota manifest. Aap config/scripts likhte ho.
- **OpenCode** — **code module**: JS/TS file jo agent ke events mein hook karti hai.

**Zyada tar pieces port hote hain, ek nahi:** Skill sirf ek `SKILL.md` hai — Claude Code, OpenCode, Codex
sabhi isay native padhte hain. Instructions same markdown hain. MCP server sirf ek URL hai. **Hooks
exception hain:** Claude Code hooks JSON + shell script hain, OpenCode hooks ek JS module hai jo throw
karta hai — koi shared format nahi.

**Yeh split 2 families tak scale hoti hai:** Aapka Claude Code plugin **Claude Cowork** aur **claude.ai**
mein bhi load hota hai. Aapka OpenCode plugin **OpenWork** mein bhi. Skills dono families ke paar jati
hain (OpenClaw, Codex, Cursor).

## Concept 3 — Bundle Share Karne Ke Liye, Configure Rakhne Ke Liye Nahi

Dono hosts plugin ke bina bhi customize hone dete hain — Claude Code `.claude/` folder parhta hai;
OpenCode `.opencode/`. Yeh sahi tool hai jab customization personal ho, ek repo mein rahe. **Plugin tab
chahiye jab customization travel kare** — teammates tak, projects ke paar, community tak, versions ke
sath.

> **Test "plugin banau?":** *kya karta hai* nahi — **kaun aur isay chahiye.** Ek developer, ek project:
> `.claude/` folder. Team, kai projects, ya strangers: plugin.

Plugin skills/commands plugin ke naam se **namespaced** hain — `repo-tools` plugin mein `hello` skill
`/repo-tools:hello` se invoke hoti hai. Yeh 2 installed plugins ko naam clash se bachata hai.

---
[⬆ Index](README.md) · [Agla: Capability Levers ➡](01-capability-levers.md)
