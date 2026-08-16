# 03 — Part 4: Search Ko Achha Banana (Concepts 12-15)

Working RAG **achha** RAG nahi hota. Yahan zyada tar projects atak jate hain.

## Concept 12 — Eval-Driven Development

Jo cheez shippable system ko lucky demo se alag karti hai. Zyada tar log build karte hain, phir eyeball
karte hain "theek lagta hai." Iski jagah: **sawalon se shuru karo.** Kuch bhi likhne se pehle, dozen real
questions likho jo users poochenge — ek file mein. Yeh aapka **evaluation set** hai.

Jab bhi system badlo — naya embedding model, alag chunking, naya filter — eval set dobara chalao aur
**effect dekho.**

**Doosra hissa: problem decompose karo.** Jawab kharab ho to "AI dumb hai" mat kaho — stages trace karo:

- **Retrieval:** sahi chunks return hue? (Aksar asal problem *inventory* gap hai — users aisi cheez poochte
  hain jo database mein hai hi nahi)
- **Context:** sahi chunks LLM ko diye gaye, ya bohat zyada/kam?
- **Generation:** achhe context ke bawajood model ne bura jawab diya?

**9 mein se 9 baar galti retrieval hoti hai, LLM nahi.**

```text
Read our source table and draft 12 eval questions... Note the expected
answer for each (or "not answerable"), and save them to
evals/questions.md for me to edit.
```

Phir:

```text
Build a small harness that runs each question... for each one show: the
chunks retrieved, the final answer, and whether it matches what I
expected.
```

## Concept 13 — Filtered Search: `WHERE` Aapka Dost Hai

Pure semantic search globally-most-similar rows deta hai. Aksar chahiye **most similar rows jo ek
condition bhi poori karein.** Chunki vectors data ke saath rehte hain, yeh bas ek `WHERE` clause hai.

| Pattern | Example | Clause |
| --- | --- | --- |
| Metadata filter | Multiple products ke docs | `WHERE product = 'CRM'` |
| Time filter | Recent articles | `WHERE published_at > now() - interval '7 days'` |
| Permissions filter | User sirf apni cleared cheez dekhe | `WHERE clearance_level <= $user_level` |

```text
Add an optional city filter to our semantic search. On a Neon branch,
add a B-tree index on the city column, show me before/after latency.
```

## Concept 14 — Hybrid Search: Meaning Aur Keywords Dono

Hybrid search sabse strong candidate upgrade hai (default nahi — eval set par confirm karo). Idea:
keyword search **aur** vector search dono chalao, phir merge karo. Vector search paraphrase samajhta hai
lekin rare exact terms (product code, naam) underweight karta hai; keyword search exact term pakarta hai
lekin meaning miss karta hai.

**Shape:** har side se over-fetch karo (top 20+20), phir **Reciprocal Rank Fusion (RRF)** se fuse karo —
position se merge karta hai, score se nahi (kyunki keyword scores aur cosine distances alag scales par
hain).

```sql
WITH kw AS (
  SELECT id, row_number() OVER (ORDER BY ts_rank_cd(ts, plainto_tsquery($1)) DESC) AS rank
  FROM quotes_embedding WHERE ts @@ plainto_tsquery($1) LIMIT 20
),
vec AS (
  SELECT id, row_number() OVER (ORDER BY embedding <=> $2) AS rank
  FROM quotes_embedding ORDER BY embedding <=> $2 LIMIT 20
)
SELECT id, SUM(1.0 / (60 + rank)) AS score
FROM (SELECT * FROM kw UNION ALL SELECT * FROM vec) r
GROUP BY id ORDER BY score DESC LIMIT 10;
```

Hybrid search un queries par sabse zyada jeetta hai jo concept + specific term mix karti hain — "Truman
Capote ne city ke baare mein kya kaha" ko naam **exact** match aur meaning **samajhna** dono chahiye.

## Concept 15 — Multi-Tenancy Aur Text-to-SQL

**Multi-tenancy:** SaaS banate ho to har customer ka data alag rehna chahiye.

| Approach | Isolation | Fit |
| --- | --- | --- |
| Shared table + `tenant_id` filter | Weakest | Internal tools |
| Schema per tenant | Good | Zyada tar SaaS ka sweet spot |
| Database per tenant | Strongest | High-security clients |

Rule Concept 13 se: boundary **database mein** enforce karo, sirf app code mein nahi. Cleanest mechanism:
**Row-Level Security (RLS)** — ek policy likho, Postgres har query par khud apply karta hai. **Catch:**
RLS superusers aur table owner ko **bypass** kar jata hai — app ko ordinary, non-owner role se connect
hona chahiye.

**Text-to-SQL:** User plain English mein poochta hai ("Q3 sales region-wise kya the?"), agent isay
correct SQL mein translate karta hai. Accuracy ke liye chahiye: clear naam, `COMMENT`s har table/column
par, kuch example question→query pairs. **Hamesha generated SQL review karo chalane se pehle.**

---
[⬅ Search Ko Fast Banana](02-making-search-fast.md) · [⬆ Index](README.md) · [Agla: Shipping ➡](04-shipping-and-next.md)
