# Plugins for AI Agents: One Bundle, Your Whole Team

*Source: The AI Agent Factory — "Plugins for AI Agents: One Bundle, Your Whole Team" (Panaversity)*
*URL: https://agentfactory.panaversity.org/docs/plugins-crash-course*
*Group: Mode 2 — Manufacturing, Phase 1 · Building Blocks (Chapter 5 of 6)*

---

## Yeh Course Kis Baare Mein Hai

**13 Concepts, 80% of Real Use.** Bina kuch extra ke, Claude Code ya OpenCode jaisa coding agent ek
capable generalist hai — kisi bhi project mein kaam kar sakta hai, lekin **aapka** tareeqa nahi jaanta.
**Plugin** ek install mein yeh fix karta hai: skills (playbooks), subagents (specialists), MCP servers
(reach), instructions, aur hooks (rules jo skip nahi ho sakte) — sab bundle. Yeh bundle ek generic agent
ko **aapka** bana deta hai, aur jo teammate install kare usay bhi wahi milta hai.

**Real example:** `claude plugin marketplace add anthropics/knowledge-work-plugins` phir
`claude plugin install finance@knowledge-work-plugins` — 2 commands, aur blank Claude finance specialist
ban jata hai.

## Parts

1. [The Shape — Aap Agent Extend Karte Ho, Own Nahi (Concepts 1-3)](00-the-shape.md)
2. [Capability Levers — Skills, Subagents, MCP Servers (Concepts 4-6)](01-capability-levers.md)
3. [Deterministic Lever — Hooks (Concepts 7-8)](02-deterministic-lever.md)
4. [Ship It — Manifest, Marketplace, Trust (Concepts 9-11)](03-ship-it.md)
5. [OpenCode Plugins + Worked Example + Capstone (Concepts 12-13)](04-opencode-worked-example-capstone.md)

---

## 4 Non-Negotiables

Poori baat ek fact se nikalti hai: **aap ek aisa agent extend kar rahe ho jo aapka nahi hai.** Host
(Claude Code/OpenCode) loop, model, aur machine own karta hai. Aapka plugin sirf pieces deta hai jo host
load kare.

1. **Bundle share karne ke liye.** Sirf ek repo ke liye chahiye to `.claude/` folder banao, plugin nahi.
2. **Sahi lever sahi kaam ke liye.** Skill = knowledge jo choice se use hoti hai; subagent = delegated
   kaam; MCP server = reach; hook = code jo khud chalta hai fixed moments par.
3. **Must-always ek hook hai, instruction nahi.** Skill ya `CLAUDE.md` mein likhi cheez model skip kar
   sakta hai. Agar zaroori hai, hook banao.
4. **Plugin user ke trust mein chalta hai.** Yeh installer ki machine par code execute karta hai —
   least privilege, kya touch karta hai batao.

*Yeh summary poore course (The Shape + Capability Levers + Deterministic Lever + Ship It + OpenCode +
Worked Example + Capstone) ka overview hai.*
