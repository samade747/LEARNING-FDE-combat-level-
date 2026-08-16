# 04 — Part 4: Poora Worked Example — Customer Support Worker

Ek realistic build jo upar ke sab concepts use karta hai. Minimal chat agent se shuru karo, phir usay
customer-support Worker mein grow karo, ek waqt mein ek piece.

## Step 0 — Chat Agent Khada Karo (~1 minute)

```text
build me a small terminal chat agent with the OpenAI Agents SDK: a uv
project, a gpt-5-class model, on a local sandbox. Get it answering "hi".
```

## The Brief

Minimal chat agent ko is Worker mein badlo jo:
- 3 Skills on-demand load kare: `summarize-ticket`, `find-similar-cases`, `escalate-with-context`
- Neon Postgres system of record (5 tables) se read/write kare
- pgvector se past resolved cases par semantic search kare
- Business data ke liye **scoped custom MCP server** (`customer-data`) use kare — kabhi Neon MCP nahi,
  kabhi direct `asyncpg` nahi agent code mein
- Har meaningful action ke liye audit row likhe **apne khud ke direct connection** se — jaan-boojh kar
  MCP boundary bypass karta hai taake audit trail us system se starve na ho jise woh audit kar raha hai

## 9 Decisions

**Decision 1 — Rules file update karo.** `AGENTS.md` mein 3 rules: business data sirf MCP server se,
audit log apna direct connection use kare aur action + audit row same transaction mein, embeddings
store/search same model se.

**Decision 2 — Schema aur Skill set plan karo.** Plan mode mein poora design likho — 3 Skills, 5-table
schema + domain tables, MCP server ka tool list, audit-logging plan. **Push back** 2 common galtiyon
par: vague Skill descriptions, aur over-broad MCP tool inputs (`query: string` matlab chupa hua
`run_sql`).

**Decision 3 — Neon provision karo, schema migrate karo.** Project banao, pgvector on karo, schema
branch-first apply karo (9 tables), Worker ko `SQLAlchemySession` do taake yaad rakhe.

**Decision 4 — Pehli Skill banao, prove karo, wire karo.** `skill-creator` ko **trigger criteria** do
(kab fire ho, kab na ho) — woh khud build/test/tighten karta hai. Sirf description badalne se skill
"summarizes tickets" se real phrasings ("TL;DR this thread") tak pahunchti hai.

**Decision 5 — Embedding pipeline banao, document library seed karo.** Worker khud dozen+ resolved
tickets generate karta hai (Pydantic model se), phir unhe embed kar ke `documents`/`embeddings` mein
daalta hai. **Yeh direct connection hai, MCP nahi** — seed script infrastructure hai, aap khud chala
rahe ho, agent nahi.

**Decision 6 — `customer-data` MCP server define/build/connect karo.** `mcp-builder` skill se, **sirf 3
tools:** `lookup_customer`, `find_similar_resolved_tickets`, `issue_refund` (refund + order status +
audit row **ek transaction mein**). Koi general `run_sql` nahi.

**Decision 7 — Audit logging har jagah wire karo.** Agent-side actions (skill invocations, tool calls,
guardrail trips) `on_tool_start`/`on_tool_end` par record hote hain. **Zaroori:** `conversations` row
pehle likho (foreign key), sirf latest user message screen karo (poora session history nahi).

**Decision 8 — Poora Worker ek scenario par verify karo.** Ek real message chalao, `audit_log` trace
parho — `message_received` → `skill_activated` → `capability_invoked` → `message_sent`. **Yeh test hai
ke saari layers milkar kaam karti hain.**

**Decision 9 — Woh ek action harden karo jo paisa move karti hai.** `issue_refund` ko human approval ke
peeche gate karo. Approve → refund complete + audit row. Reject → koi refund nahi, decline record hoti
hai. **Yeh aakhri isliye hai** — approval gate tab tak untestable theatre hai jab tak Worker end-to-end
kaam na kare.

## Kya Hua

- **Capability code se bahar chali gayi** — 3 Skills `.claude/skills/` mein, version-controlled
- **Durable stores process se bahar chale gaye** — real Postgres schema
- **Runtime business access mediated hai** — sirf scoped MCP server se
- **Har action trace chhodta hai** — audit log kisi bhi conversation ko SQL se replay kar sakta hai
- **Dangerous action ka ek owner hai** — refund insan ke approval se pehle nahi chalta

Yeh Worker ki **foundation** hai. Yeh abhi tak always-on, proactive, ya managed workforce ka hissa nahi
hai — agle courses yeh add karte hain.

## Decision 10 (Optional Challenge): Paused Approval Ko Restart Survive Karwana

Real approvals aksar terminal par baithe hue nahi hote — manager ek ghante baad, doosri app se, doosri
machine se jawab de sakta hai. Paused run ko `run_states` table mein move karo (audit_log ya
`conversations` column mein nahi — apni table).

**5 Steps:** (1) `run_states` table banao, (2) refund pause ho to save karke turn free karo, (3) alag
"decide" command se approve/reject karo, (4) `issue_refund` idempotent banao (dedupe), (5) per-conversation
lock lagao (2 turns ek sath conflict na karein).

---
[⬅ MCP Wiring](03-mcp-wiring.md) · [⬆ Index](README.md) · [Agla: Where This Leaves Off ➡](05-where-this-leaves-off.md)
