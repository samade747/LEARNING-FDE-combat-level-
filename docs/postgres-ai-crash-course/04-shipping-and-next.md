# 04 — Parts 5-8: Worked Example + MCP Tool + Deployment + Agent

## Part 5 — Poora Worked Example

Ek task, shuru se aakhir tak: khali Neon project se working Q&A tak. Rhythm: **plan → review →
execute → evaluate → iterate.**

0. Docs ka home banao (10 markdown files — mini employee handbook)
1. **Plan karo** (strong model, plan mode) — poora RAG system propose karwao
2. **Plan parho** — Neon branch par? pgvector enabled? key environment se?
3. **Execute 3 checkpoints mein** (cheap model): database + worker → retrieval → generation
4. **Evaluate, iterate** — kamzor jawab retrieval ki galti hai ya generation ki, diagnose karo

Phir 4 tuning exercises **real mein chalao** (skip nahi karte, sab required hain):

5. **Index fast dekho** — throwaway branch par 100k+ synthetic vectors banao, `Seq Scan` se `Index Scan`
   ban'te hue dekho, `ef_search` se latency move karte dekho
6. **Filter by meaning aur condition** — category filter add karo, B-tree index confirm karo
7. **Exact term catch karo** — ek rare code (`EXP-2031`) hybrid search se pakro jo vector-only miss
   karta hai
8. **Ek tenant ko doosre se wall off karo** — RLS policy likho, **non-owner role** se test karo (yeh
   zaroori hai — owner role RLS bypass kar deta hai)

**Rhythm kabhi nahi badalta hard parts ke liye bhi** — sirf review ki cheez badalti hai.

## Part 6 — RAG Ko MCP Tool Ki Tarah Ship Karo

`search_quotes()` aur `answer_question()` ko **MCP server** mein wrap karo — ab yeh koi bhi agent
(Claude Code, OpenCode, Digital FTE) discover aur call kar sakta hai.

> **Do MCP servers, confuse mat karo:**
> - **Neon MCP server** — dev-time admin tool, stdio, local
> - **RAG MCP server** (yeh) — runtime product surface, Streamable HTTP, cloud mein hosted

```python
@mcp.tool()
def search_knowledge(query: str, limit: int = 5) -> list[dict]:
    """Search the knowledge base by meaning..."""
    return search_quotes(query, limit)

@mcp.tool()
def answer_question(question: str) -> str:
    """Answer a question grounded in the knowledge base."""
    return rag_answer(question)

mcp.run(transport="http", host="0.0.0.0", port=8000, stateless_http=True)
```

**2 zaroori cheezein:** docstring hi interface hai (calling agent isay parh kar decide karta hai kab
use kare); retrieval **read-only** rehta hai (read-only database role, tool argument kabhi data
mutate/leak nahi kar sakta).

**Deploy:** Stateless build karne ka fayda — **server mein deploy karne ke liye kuch nahi badalta.** Same
`server.py` kisi bhi Python-host par push karo (Cloud Run, Render, Railway, Fly), localhost ki jagah
public URL register karo.

> **Caution:** Read-only role, parameterized queries, multi-tenancy mein RLS se `tenant_id` enforce
> karo (tool argument se kabhi trust mat karo), aur sirf woh MCP configs trust karo jinhe aap jante ho.

## Part 7 — Yeh Kahan Chalta Hai

| Kahan | Best For |
| --- | --- |
| **Neon** (yeh course) | Pehli build se production tak — serverless, instant branching |
| **Neon branches** | Dev, preview, evals, benchmarks |
| **TigerData Cloud** | pgvectorscale native, StreamingDiskANN scale |

**Aap lock-in nahi ho** — plain Postgres + pgvector, worker database se bahar — same schema kisi bhi
Postgres host par chalta hai (Supabase, Xata, RDS, Azure).

> **Kya aapko dedicated vector database chahiye?** Usually nahi. Agar already Postgres chalate ho,
> pgvector vectors ko data ke paas rakhta hai — ek source of truth. HNSW ~100k-10M comfortably cover
> karta hai. **Zyada tar applications ke liye, Postgres hi vector database hai.**

## Part 8 — Agent Ko Sonpo

Yeh course retrieval banata hai; **Build AI Agents** course loop sikhata hai — `Agent` + `Runner`.
**Aapka RAG un tools mein se ek hai.**

**2 tareeqe connect karne ke:**
- **MCP server ki tarah** — Agents SDK MCP servers directly consume kar sakta hai
- **Function tool ki tarah** — `@function_tool` mein wrap karo

**Gehra bridge: memory vs knowledge.** Har agent 2 sawal ke around bana hai: kya draw kar sakta hai
(state), aur kya karne ki ijazat hai (trust). **Memory** = jo conversation se yaad hai (sessions handle
karte hain). **Aapka RAG** doosri kism deta hai: **knowledge** — durable, searchable context jo agent
**lookup** kar sakta hai, kisi bhi window se zyada data mein se.

## Yahan Se Aage

- **Reliable banao:** Eval-Driven Development Crash Course
- **Agent banao:** Build AI Agents (poora loop, guardrails, sessions, deployment)
- **Product banao:** Digital FTE

**Throughline kabhi nahi badalta:** sahi information, sahi waqt, irrelevant information bahar.

---
[⬅ Search Ko Achha Banana](03-making-search-good.md) · [⬆ Index](README.md)
