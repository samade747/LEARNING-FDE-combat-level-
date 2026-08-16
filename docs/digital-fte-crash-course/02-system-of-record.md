# 02 — Part 2: Neon Postgres + pgvector System of Record (Concepts 6-10)

## 4 Kism Ka Data

Part 1 ne agent ko capabilities dein. Ab usay durable jagah chahiye jo bhoolna afford na kar sake:
customer record, policy library, past cases, aur uske actions ki trace.

- **Business records** — customers, orders, tickets (Part 4 mein banate hain)
- **Reference library** — meaning se search hone wali knowledge (`documents` + `embeddings`)
- **State** — live conversation (SDK ka **Session** khud banata hai; `conversations` row envelope hai)
- **Trace** — Worker ne kya kiya (`audit_log`)

## Concept 6 — Managed Postgres Kyun, Neon Kyun

**Dedicated vector database ki jagah Postgres kyun:**
1. **Ek database, ek transaction, ek auth boundary** — alag vector DB matlab do stores sync karna, do
   auth systems
2. **Postgres already hard parts karta hai** — transactions, indexes, foreign keys, row-level security
3. **Postgres ke liye MCP servers har layer par exist karte hain**

**Dedicated vector DB kab jeetta hai:** Jab search-by-meaning **khud product** ho, feature nahi — itne
vectors ke ek Postgres server mein memory mein na fit hon, ya bohat heavy search traffic.

**Neon kyun specifically:**
- **Scale to zero** — idle hone par kuch cost nahi
- **Branches** — seconds mein poori database copy, experiment karo, ghalat ho to branch delete karo
- **Official MCP server** — coding agent plain language mein projects/branches/migrations manage karta hai

## Concept 7 — Worker Ka Schema

**4 tables jo har Worker rakhta hai (shared spine):**

- **`conversations`** (state) — ek row per conversation, kiske sath, kab, summary
- **`documents`** + **`embeddings`** (reference library) — `documents` text rakhta hai; `embeddings`
  usay meaning-searchable banata hai
- **`audit_log`** (trace) — Worker ne kya kiya, order mein

**Ek optional (usage analytics):**
- **`capability_invocations`** — har skill/tool call ki row, kitna time laga, kaamyab hua ya nahi

**Design choices:**
- **Ek `embeddings` table dono documents aur conversations ke liye** — `CHECK` constraint ensure karta
  hai har row exactly ek ko point kare
- **`audit_log` `BIGSERIAL` use karta hai, `UUID` nahi** — rows tezi se jama hoti hain, integer key
  writes ko fast rakhta hai
- **Skills aur tools `capability_invocations` share karte hain** — ek column batati hai kaunsa

**Turn-by-turn messages kahan jate hain?** **Transcript** (har message) SDK khud likhta/rakhta hai —
aap kabhi nahi banate. **Cover sheet** (`conversations` row) aap likhte ho — session id se joda hua.

## Concept 8 — pgvector Basics

`VECTOR(n)` column ek pin rakhta hai — fixed list of `n` numbers. **Zaroori rule:** stored text aur
search query **same model** se guzarne chahiye — 2 alag models alag scale ke maps jaise hain.

**3 distance operators:**

| Operator | Naam | Kab Use Karo |
| --- | --- | --- |
| `<=>` | Cosine | **Text, hamara default** |
| `<->` | Straight-line | Image search |
| `<#>` | Dot product | Rare — jab vectors same length na hon |

**Indexes:**
- **HNSW se shuru karo** — fast searches, build slow, zyada memory. **Right default**
- **IVFFlat sirf tab jab build speed matter kare** search speed se zyada
- **DiskANN** bohat bare indexes ke liye jo memory mein fit na hon

```sql
CREATE INDEX idx_embeddings_hnsw ON embeddings USING hnsw (embedding vector_cosine_ops);
```

## Concept 9 — Embedding Pipeline

4 steps: **Chunk** (document ko chote pieces mein todo) → **Embed** (model call karo) → **Store**
(embeddings table mein) → **Query** (user ka sawal bhi embed karo, nearest points dhoondo).

**Chunking rules:** natural breaks par split karo (headings, paragraphs), kuch sau alfaz per chunk,
thora overlap rakho, jo already chota hai usay chunk mat karo.

**Kab re-embed karein:** (1) source text badla, (2) embedding model badla (**har purana point ab alag
map par hai** — no "close enough"), (3) chunk size badla.

> **Trap:** Documents aur past conversations dono ek hi `embeddings` table mein mix ho to search mixed
> results de sakta hai — **source se filter karo** search karte waqt, warna agent purani chat ko
> authoritative policy jaisa treat kar sakta hai.

## Concept 10 — Audit Trail Discipline

Har meaningful action database mein ek row chhodni chahiye. **2 cheezein confuse na karein:**

- **Truth khud** — abhi kya sach hai (business records mein)
- **Audit trail** — Worker ne truth ke sath **kya kiya** (`audit_log` mein) — replay-able record

**Test jo isay audit trail banata hai, sirf logs nahi:** Ek conversation aur waqt diya jaye, aap bina
model dobara chalaye Worker ne kya kiya reconstruct kar sako. Agar nahi, aapke paas logs hain.

**Action aur uski record ek transaction mein likho** — dono land hon ya koi nahi. Aadhi-likhi audit
trail poori na hone se bhi buri hai.

**Action names ke liye chota, fixed vocabulary rakho** (`CHECK` constraint se enforce karo). Naya verb
chahiye ho to migration hai, chupke se nahi.

> **Yehi sellability hai:** "Workers workforce ki tarah tab governable bante hain jab ek ledger unhe
> legible banata hai." Aapka `audit_log` **wahi ledger hai.** Legible hona hi Worker ko **sellable**
> banata hai — jo outcome aap prove nahi kar sakte, uska charge nahi le sakte.

---
[⬅ Skills](01-skills.md) · [⬆ Index](README.md) · [Agla: MCP Wiring ➡](03-mcp-wiring.md)
