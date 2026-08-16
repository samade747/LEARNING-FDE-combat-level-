# 02 — Part 3: Search Ko Fast Banana — Indexes (Concepts 10-11)

## Concept 10 — Vector Index Kab Chahiye (Aur Kab Nahi)

Bina index ke, similarity search har row se query vector compare karta hai — **exact** nearest-neighbor
scan. Chota table hote waqt yeh bilkul theek hai. Bare hote hote slow ho jata hai.

Fix: **approximate** search — thori si accuracy ki qeemat par bara speed-up. Vector index woh data
structure hai jo yeh approximation achha banata hai.

**Threshold jo over-engineering se bachata hai:** taqreeban **100,000 vectors** se neeche, exact search
aksar kaafi fast hoti hai — aur hamesha correct. Real threshold dimensions, compute size, filters,
concurrency par shift karta hai — isliye agent se **benchmark karwao** index add karne se pehle, default
mein nahi.

## Concept 11 — Kaunsa Index, Aur Kaise Tune Karein

| Index | Best For | Plus | Minus |
| --- | --- | --- | --- |
| **IVFFlat** | Medium sets, low memory | Low memory, full scan se tez | Recall data barhne se drift karti hai; mostly superseded |
| **HNSW** (Neon default) | ~100k-10M vectors | Strong speed/accuracy balance, rebuild ke bina updates | RAM-bound, cost memory se scale karta hai |
| **StreamingDiskANN** (TigerData native) | 10M+, heavy filtered search | Best accuracy with WHERE filters, billion+ scale | Longer first build time |

Neon par live choice **HNSW** hai. Ek column sirf **ek** vector index type rakh sakta hai — either/or
hai.

```sql
CREATE INDEX ON quotes_embedding USING hnsw (embedding vector_cosine_ops);
```

`vector_cosine_ops` index ko aapke queries ke **distance function** se match karna zaroori hai (`<=>`
→ cosine). Mismatch ho to index chupke se kaam nahi karega.

**Kaise decide karein: benchmark karo.** HNSW ke 2 build-time settings hain — `m`, `ef_construction`.
Yaad nahi karte, agent se real workload par **measure** karwate ho, throwaway branch par, phir branch
discard kar dete ho.

**Query-time knob jo roz kaam ata hai: `ef_search`.** Jitna high, utni behtar recall aur slower query.

```sql
SET LOCAL hnsw.ef_search = 100;   -- barhao zyada recall, ghatao zyada speed
```

**`EXPLAIN ANALYZE` se prove karo index kaam kar raha hai:**

```text
✅ GOOD — index kaam kar raha hai
->  Index Scan using quotes_embedding_hnsw_idx
 Execution Time: 0.8 ms

❌ BAD — index use nahi hua, har row scan hui
->  Seq Scan on quotes_embedding (rows=2000000)
 Execution Time: 52.4 ms
```

`Seq Scan` matlab index use nahi ho raha — usually query ka distance operator index se match nahi karta,
ya koi index exist hi nahi karta.

## 5 Failure Modes Review Mein Pakarne Wale

- **Dimension mismatch** — column ke dimensions embedding model ke output se match nahi karte
- **Vector type client mein registered nahi** — worker/search code ko `register_vector` call karna
  zaroori hai, warna vectors chupke se plain text ki tarah round-trip karte hain
- **Koi index nahi** jab zaroorat ho — silent slowdown, koi error nahi
- **Operator/index mismatch** — query `<->` use kare lekin index cosine ho
- **Poore documents, chunks nahi** — Concept 7 ki galti
- **`EXPLAIN ANALYZE` skip karna** — koi in mein se kuch pakarta hi nahi jab tak users pakarein

> **Filtered-search trap:** HNSW `WHERE` clause ko **apne fixed candidate budget** ke baad apply karta
> hai. Selective filter aapko `LIMIT` se kam rows de sakta hai aur real matches chupke se miss kar sakta
> hai. Fix: `ef_search` barhao, ya per-filter-value partial HNSW index banao.

---
[⬅ Pehla RAG](01-first-rag.md) · [⬆ Index](README.md) · [Agla: Search Ko Achha Banana ➡](03-making-search-good.md)
