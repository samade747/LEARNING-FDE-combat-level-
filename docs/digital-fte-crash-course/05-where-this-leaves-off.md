# 05 — Part 5: Yeh Course Kahan Chhodta Hai + Quick Reference

## Worker Ka Cost Shape Estimate Karna

Dollar totals yahan jaan-boojh kar nahi hain — prices monthly badalti hain. Jo lasting hai woh
**method** hai.

**1. Model inference (poora bill almost yehi hai).**
```
input tokens/month ≈ conversations/day × turns/conversation × tokens/turn × 30
```
Sabse bara lever: **prompt caching.** `AGENTS.md`, system prompt, Skills metadata har turn same hote
hain — stable prefix cache hota hai, fraction ki qeemat par. `AGENTS.md` ko din mein churn mat karo.

**2. Embeddings.** Cents, dollars nahi — jab tak poori conversation histories continuously re-embed na
karo.

**3. Postgres (Neon).** Aksar $0 — free tier ek low-volume Worker cover karta hai, scale-to-zero idle
hours free rakhta hai.

**4. Sandbox compute.** $0 local sandbox par; production mein container-minutes.

## Swap Guide: Architecture Invariant Hai, Products Nahi

| Layer | Swap | Kya Kho Dete Ho |
| --- | --- | --- |
| Postgres host | Neon → Supabase, RDS, self-hosted | Branching, scale-to-zero (Neon-specific) |
| Vector storage | pgvector → Pinecone/Weaviate/Qdrant | Ek database ka fayda, do stores sync karne parte hain |
| Embedding model | OpenAI → Cohere/Voyage/BGE-small | Ek constant + dimension badlo, re-embed karo |
| Sandbox | Local → Cloudflare/E2B/Modal/Docker | Kuch nahi — `SandboxAgent` backend-agnostic hai |
| Agent runtime | OpenAI Agents SDK → LangGraph/CrewAI | MCP boundary survive karta hai, har framework ka MCP client hai |

**Jo aasani se swap nahi hota:** MCP protocol khud, Skills format spec, audit-trail habit. Yehi woh
hisse hain jo aap products ke paar carry karte ho.

> **"Owned" ka matlab owned-by-composition hai:** Yeh Worker Neon ke cloud, vendor models, coding-agent
> client, third-party skills par chalta hai. **Aap seams own karte ho, substrate nahi.**

## Yeh Course Abhi Kya Cover Nahi Karta

Aapka Worker thesis ke 7 Invariants mein se 2 satisfy karta hai (Engine + System of Record). Baaki 5:

- **Invariant 1** — Human principal hai (specs, approval gates, budget)
- **Invariant 2** — Har insan ko ek delegate chahiye (personal agent — OpenClaw)
- **Invariant 3** — Workforce ko manager chahiye (orchestrator — Paperclip)
- **Invariant 6** — Workforce policy ke under expandable hai (Claude Managed Agents)
- **Invariant 7** — Workforce ek nervous system par chalta hai (triggers — Inngest, Claude Code Routines)

## How to Actually Get Good At This

- "Skill fire kyun nahi ho rahi" → description quality (Concept 3)
- "Agent aisi data invent kyun kar raha hai jo database mein hai hi nahi" → MCP server actually call
  nahi ho raha — trace check karo
- "Audit log incomplete kyun hai" → audit write action ke sath same code path mein nahi hai
- "pgvector results irrelevant kyun hain" → chunking galat, ya insert/query models mismatch
- "MCP server load ke neeche slow kyun hai" → connection pool chota hai, ya tools list cache nahi hui

**Architecture ek waqt mein ek piece banao.** Ek weekend mein Skills + system of record + MCP sab mat
karo. System of record pehle (Decisions 3-5), phir Skill (Decision 4), phir MCP boundary (Decision 6).

### Kya Badalta Hai Jahan Aap Waqt Lagate Ho

Decision 4 ke baad, aapka kaam shape badalta hai. Code likhna agent ko brief karna ban jata hai;
description review karna asli craft ban jata hai. Ek description jo 30 minute lagi likhne mein, 200
lines ke MCP server code se zyada architectural kaam karti hai — kyunki description hi routing surface
hai jo model **har turn** parhta hai.

## Quick Reference — 15 Concepts, Ek Line Mein

1. **Agent Skill ek folder hai** — SKILL.md + optional scripts/references/assets
2. **Progressive disclosure** — startup par metadata → activation par full body → on-demand references
3. **SKILL.md = frontmatter + body** — name, description, phir instructions
4. **Skills files ki tarah travel karti hain** — same SKILL.md Claude Code aur OpenCode dono mein
5. **Filesystem handoff se compose karo** jab isolation orchestration simplicity se zyada matter kare
6. **Postgres + pgvector alag vector DB se behtar hai** zyada tar agent workloads ke liye
7. **5 tables minimum schema hain** — conversations, documents, embeddings, audit_log,
   capability_invocations
8. **pgvector basics** — `VECTOR(1536)` + `<=>` cosine + HNSW index, same model dono taraf
9. **Embedding pipeline** — semantic boundaries par chunk karo, batch-embed karo
10. **Audit logging nahi hai** — har meaningful action same transaction mein row likhta hai
11. **MCP protocol hai, service nahi** — 3 primitives, 3 transports
12. **Neon MCP server development ke liye hai** — production runtime ke liye nahi
13. **Agents SDK ka built-in MCP client hai** — `async with` use karo, production mein cache karo
14. **Custom MCP servers scope/isolation/reusability se apna kharch nikalte hain**
15. **MCP under load** — remote ke liye streamable HTTP, tools cache karo, connections reuse karo

---
[⬅ Worked Example](04-worked-example.md) · [⬆ Index](README.md)
