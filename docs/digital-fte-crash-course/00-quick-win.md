# 00 — 15-Minute Quick Win

15 concepts parhne se pehle, is architecture ka sabse chota working version banao. Iske baad hoga:

- Fresh Neon project, 2 tables (`notes`, `audit_log`) jo aap ne MCP se banaye aur console mein dekhe
- Minimal AI Worker jo apne `save_note` tool se dono mein ek transaction mein likhe
- Jawab "kya system of record ne asal mein kuch kiya mere liye?" — aapki note aur uski audit row, ek id
  share karti hui

## 2 Planes — Poora Mental Model

**Coding agent** (Claude Code/OpenCode) **Neon MCP** use karta hai database **banane aur inspect karne**
ke liye. **Aapka banaya Worker** apna **khud ka tool** use karta hai runtime par likhne ke liye. Worker
kabhi Neon MCP nahi chhuta — Neon ke apne docs saaf kehte hain: MCP server sirf "development aur
testing" ke liye hai, kabhi running app mein wire nahi hota.

## Steps

**1. Base download karo, agent kholo.** `digital-fte/` folder poore course ke liye — Quick Win aur Part
4 dono.

**2. Base prep karo (~3 min):**
```text
Read AGENTS.md, then get this base ready: install the skills it lists,
copy .env.example to .env, and tell me what you need to bring the Neon
and Context7 MCP servers online.
```

**3. Gate — confirm agent database tak pahunch sakta hai (~1 min):**
```text
List the Neon tools you can see.
```
**Gate open:** real Neon tool names ki list mile.

**4. Store banao, connection string lo (~3 min):**
```text
On a fresh Neon project, create two tables: notes and audit_log. Then
call get_connection_string and write that URL into my .env as
DATABASE_URL. Use the Neon tools for all of it.
```

**5. Apni ankhon se dekho (~1 min).** [console.neon.tech](https://console.neon.tech) kholo, **Tables**
dekho — `notes` aur `audit_log` khali pade hain.

**6. Worker scaffold karo, ek dafa chalao (~2 min):**
```text
Using uv, scaffold a minimal OpenAI Agents SDK project: a SandboxAgent
on a gpt-5-class model with no tools yet, run from the terminal on a
local sandbox, reading OPENAI_API_KEY from .env. Run it once with
"hello".
```

**7. Worker ko tool do, yaad rakhte dekho (~3 min):**
```text
Add a save_note tool to the Worker, written as a @function_tool, that
inserts a row into notes and a matching row into audit_log in a single
transaction, using DATABASE_URL. Then run the Worker and send it:
"Remember this: the production deploy needs a new env var before
Friday."
```

**Notice karo kya nahi hua:** Worker ne kabhi Neon MCP nahi chhua. Admin wire ne store banaya; Worker
apne narrow tool se use karta hai.

**8. Win: wapis parho (~2 min).** Neon console **Tables** view refresh karo — note ab `notes` mein ek
row hai, aur `audit_log` mein matching row `note_saved` record karti hai, **same id** se juri hui.

## Yeh Kya Sikhata Hai

Aap ne plain `@function_tool` use kiya kyunki **ek Worker ek store mein likhta hai** — yehi sahi default
hai, shortcut nahi. Chota MCP server tab chahiye jab: **doosra consumer** (dusra Worker/coding agent)
same `save_note` chahe, **tighter scope** enforce karna ho, ya **process isolation** chahiye. Yeh
decision Concept 14 hai.

Part 4 isi shape ko kai Skills, 5-table schema, aur embedding pipeline tak scale karta hai. Shape nahi
badalta: system of record, same transaction mein audit, aur admin wire vs Worker access ke beech saaf
line.

---
[⬆ Index](README.md) · [Agla: Skills ➡](01-skills.md)
