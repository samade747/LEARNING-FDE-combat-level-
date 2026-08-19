# Building a Digital FTE — Summary

15 Concepts + worked build. Pichle course ka agent (streaming chat agent) terminal band karte hi sab
bhool jata tha, tools Python-hardwired the. **Yeh course "agent se AI Worker" ka pehla real qadam** —
2 moves + wire: **Abilities → Skills**, **Restart-forgotten state → Postgres (system of record)**, **MCP
= wire jo agent ko store tak leti hai.**

## 00 — Quick Win (~15 min)

- 2 planes: **Coding agent** Neon MCP se database **banata/inspect** karta hai; **Worker** apna khud ka
  tool (`@function_tool`) runtime write ke liye use karta hai — Neon MCP kabhi running app mein wire nahi
  hota (Neon ke apne docs: "development aur testing" only).
- Steps: base prep → Neon tools list confirm → 2-table store (`notes`, `audit_log`) banao → console mein
  dekho → Worker scaffold (OpenAI Agents SDK) → `save_note` tool (ek transaction mein dono tables) →
  win: id-shared row dono tables mein. Chota MCP server tab chahiye jab: doosra consumer, tighter scope,
  ya process isolation chahiye ho (Concept 14).

## 01 — Skills (Concepts 1-5)

- **Concept 1 — Skill Kya Hai:** folder + `SKILL.md` (optional scripts/references/assets), Anthropic open
  standard, koi bhi agent parh sakta hai. Startup par sirf `name`+`description` load hota hai.
- **Concept 2 — Progressive Disclosure (3 Stages):** Discovery (~100 tokens/skill, sab load) → Activation
  (poora body load, match hone par) → Execution (referenced files on-demand). Description Stage 1 mein
  fire hoti hai — poora khel description ki hai; body tight rakho, depth references/ mein.
  Zyada tar 500-2000 tokens body.
- **Concept 3 — Description Hi Trigger Hai:** 2 hisse — YAML frontmatter (contract) + markdown body
  (instructions). Achhi description: kya produce, kab reach, keywords (jo users kabhi bolte nahi bhi),
  do-NOT line. Self-check: obvious keyword hata kar bhi trigger clear ho.
- **Concept 4 — Packaging:** `.claude/skills/` rule — Claude Code parhta, OpenCode fallback karta, SDK
  seedha point karta. Table: project-level vs user-level paths dono tools ke liye.
- **Concept 5 — Compose Karna (Ek Bari vs Kai Chhoti):** ek skill jab tightly coupled+kabhi-reuse-nahi;
  kai skills jab step akela call ho sake. **2-3 steps ke baad separation usually jeetta hai.** Filesystem
  se chain karo (tmp files), conversation se nahi. Bridge: draft = tmp/, action = system of record mein.

## 02 — Neon Postgres + pgvector System of Record (Concepts 6-10)

- **4 Kism Ka Data:** business records, reference library (documents+embeddings), state (conversations),
  trace (audit_log).
- **Concept 6 — Managed Postgres Kyun:** ek DB/transaction/auth-boundary, Postgres already hard parts
  karta hai, MCP servers har layer par exist karte hain. Neon: scale-to-zero, branches, official MCP.
  Dedicated vector DB tab jeetta hai jab search-by-meaning khud product ho ya scale extreme ho.
- **Concept 7 — Worker Ka Schema:** 4 tables (conversations, documents+embeddings, audit_log) + optional
  `capability_invocations`. Ek embeddings table dono ke liye (CHECK constraint). audit_log BIGSERIAL not
  UUID. Transcript SDK khud rakhta hai; conversations row (cover sheet) aap likhte ho.
- **Concept 8 — pgvector Basics:** `VECTOR(n)`, stored+query **same model** hona chahiye. 3 operators:
  `<=>` cosine (text default), `<->` straight-line (image), `<#>` dot product (rare). Indexes: HNSW
  (right default), IVFFlat (build-speed priority), DiskANN (huge indexes).
- **Concept 9 — Embedding Pipeline:** Chunk → Embed → Store → Query. Chunking: natural breaks, few hundred
  words, overlap. Re-embed kab: source badla, model badla, chunk size badla. Trap: documents+conversations
  ek table mein mix ho to source-filter zaroori.
- **Concept 10 — Audit Trail:** truth khud (business records) vs audit trail (kya kiya). Test: conversation
  + waqt diya jaye to bina model dobara chalaye reconstruct ho sake — warna sirf logs hain. Action+record
  **ek transaction mein**. Fixed vocabulary (CHECK constraint). "Legible hona hi Worker ko sellable banata
  hai."

## 03 — MCP: Agent Ko System of Record Se Wire Karna (Concepts 11-15)

- **Concept 11 — MCP Kya/Nahi:** open client/server protocol ("USB-C for AI tools"). 3 Primitives: Tools
  (most used), Resources, Prompts. 3 Transports: stdio (local), Streamable HTTP (remote, recommended), SSE
  (legacy). MCP nahi hai: framework, service, security boundary, `@function_tool` replacement.
- **Concept 12 — Neon MCP Server:** development plane, **kabhi production nahi** — `run_sql` koi bhi SQL
  chala deta hai, live DB par door ban jata hai. Finished Worker ko custom MCP ya direct connection chahiye.
- **Concept 13 — SDK Se Connect:** built-in MCP client — local/remote/legacy. Model MCP tool aur local
  function tool mein farq nahi karta. 4 zaroori: clean open/close, production mein tool-list cache, servers
  stack hote hain, dangerous tools approval-gated.
- **Concept 14 — Custom MCP Servers Kab:** Neon MCP generic hai; custom **narrow** (koi general run_sql
  nahi). Decision table: function-tool vs custom-server 6 scenarios. Deta hai: process isolation, scope,
  reusability. Trade-off: operational complexity — reuse/scoping/isolation-safety chahiye ho tabhi banao.
- **Concept 15 — MCP Under Load:** local subprocess ek machine ke liye theek; remote transport jab scale.
  Setup cost baar baar mat do (boot par connect, cache, pool). Ceilings: steps cap, retries limited,
  rate-limit, trace boundary-paar follow kare.

## 04 — Poora Worked Example: Customer Support Worker

- Brief: 3 Skills on-demand, Neon 5-table SoR, pgvector semantic search, scoped `customer-data` MCP
  server (kabhi Neon MCP/direct asyncpg nahi), audit row apne direct connection se (MCP boundary jaan-
  boojh kar bypass — audit khud us system se starve na ho jise audit kar raha hai).
- **9 Decisions:** (1) AGENTS.md rules, (2) plan schema+skills (push back vague descriptions, over-broad
  MCP inputs), (3) Neon provision+migrate (9 tables), (4) pehli Skill (skill-creator ko trigger criteria),
  (5) embedding pipeline+seed (direct connection, MCP nahi), (6) `customer-data` MCP — sirf 3 tools
  (lookup_customer, find_similar_resolved_tickets, issue_refund — 1 transaction mein), (7) audit logging
  har jagah (on_tool_start/end), (8) end-to-end verify (trace: message_received→skill_activated→
  capability_invoked→message_sent), (9) `issue_refund` human-approval-gated (aakhri isliye — untestable
  theatre jab tak Worker end-to-end kaam na kare).
- **Decision 10 (Optional):** paused approval restart survive kare — `run_states` table, idempotent
  issue_refund, per-conversation lock.

## 05 — Yeh Course Kahan Chhodta Hai + Quick Reference

- **Cost shape:** model inference ~poora bill (prompt caching sabse bara lever), embeddings cents,
  Postgres aksar $0 (free tier), sandbox $0 local.
- **Swap Guide:** Postgres host, vector storage, embedding model, sandbox, agent runtime — sab swappable.
  MCP protocol/Skills format/audit-trail habit **nahi** swap hote — "aap seams own karte ho, substrate nahi."
- **7 Invariants mein se 2 satisfy:** Engine + System of Record. Baaki 5 (human principal, personal delegate,
  workforce manager, policy-expandable, nervous system) agle courses cover karte hain.
- **How to debug:** skill na fire ho → description quality; data invent → MCP call nahi ho raha; audit
  incomplete → same code path nahi; pgvector irrelevant → chunking/model mismatch; MCP slow → pool/cache.
- Order: system of record pehle, phir Skill, phir MCP boundary. Decision 4 ke baad kaam shape badalta hai
  — description review asli craft ban jati hai.
- **Quick Reference:** sab 15 concepts ek-line mein.
