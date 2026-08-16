# Building a Digital FTE: A 4-Hour Crash Course

*Source: The AI Agent Factory — "Building a Digital FTE: A 4-Hour Crash Course" (Panaversity)*
*URL: https://agentfactory.panaversity.org/docs/digital-fte-crash-course*
*Group: Mode 2 — Manufacturing, Phase 2 · Build Workers (Chapter 2 of 3)*

---

## Yeh Course Kis Baare Mein Hai

**15 Concepts + ek worked build: Skills, system of record, aur unke beech MCP wire.** Pichle course
mein aap ne ek agent banaya. Yeh course pehla real qadam hai **agent se AI Worker tak.** Woh agent
(Build AI Agents se) ek streaming chat agent tha, sessions/guardrails/tracing ke sath. Woh kaam karta
tha. Lekin terminal band karte hi sab bhool jata tha, aur uska har tool uski Python mein hard-wired tha.

**AI Worker** wahi chat agent hai, bara ho gaya. Log isay **AI Employee** ya **Digital FTE** bhi kehte
hain. Yeh course uski **foundation** banata hai: ek agent jo barh sake, yaad rakhe, aur jise aap own
karo.

**Do moves, plus unke beech ka wire:**
- **Abilities → Skills** — chote folders jo agent khud dhoondta aur load karta hai, Python mein
  hard-wired tools ki jagah
- **Restart par bhoolne wali cheezein → Postgres** — uska **system of record**: ek authoritative store
  jispar Worker chalta hai
- **MCP** — open standard jo agent ko us store tak pahunchati hai, wire ki tarah

## Parts

1. [Quick Win — 15 Minute Mein Pehla Real Build](00-quick-win.md)
2. [Skills — Portable Capability Folders (Concepts 1-5)](01-skills.md)
3. [Neon Postgres + pgvector System of Record (Concepts 6-10)](02-system-of-record.md)
4. [MCP: Agent Ko System of Record Se Wire Karna (Concepts 11-15)](03-mcp-wiring.md)
5. [Poora Worked Example: Customer Support Worker (Part 4)](04-worked-example.md)
6. [Yeh Course Kahan Chhodta Hai + Quick Reference (Part 5)](05-where-this-leaves-off.md)

---

## 15 Concepts Ka Map

| # | Concept | Layer |
| --- | --- | --- |
| 1-5 | Skill kya hai, progressive disclosure, SKILL.md likhna, packaging, composing | **Skills** |
| 6-10 | Kyun managed Postgres, schema, pgvector basics, embedding pipeline, audit trail | **System of Record** |
| 11-15 | MCP kya hai/nahi, Neon MCP server, SDK se connect, custom MCP servers, load | **MCP** |

*Yeh summary poore course (Quick Win + Skills + System of Record + MCP + Worked Example + Where This
Leaves Off) ka overview hai.*
