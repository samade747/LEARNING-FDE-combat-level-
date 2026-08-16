# 01 — Part 2: Pehla RAG, Agent Se Bana Hua (Concepts 5-9)

Ek chota classic example banate hain: US shehron ke baare mein historical figures ke quotes ki table,
phir meaning se search, phir LLM se questions ka jawab.

## Concept 5 — Schema: Vectors Data Ke Saath Rehte Hain

Meaning-vectors kisi alag store mein nahi jate — **isi database** mein, companion table mein, jis data
ko woh describe karte hain uske bilkul paas.

```sql
CREATE TABLE quotes (
  id     bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  person text NOT NULL,
  city   text NOT NULL,
  quote  text NOT NULL
);
```

**Mental model:** ek source of truth. Quote, kisne kaha, city, aur (jald) uska meaning-vector — sab ek
hi database mein.

## Concept 6 — Embeddings Banana: Worker Jo Agent Banata Hai

`quotes` table text rakhti hai. Meaning se search ke liye har piece ko vector chahiye. Agent ek chota
program likhta hai — **embedding worker**: **bina-vector quotes dhoondo → lambe text ko chunks mein
todo → har chunk ka vector mango → vectors save karo.**

Vectors **companion table** mein jate hain — har chunk ki ek row, jo apne source quote ki taraf point
karti hai:

```text
quotes                             quotes_embedding
id | quote                         id | quote_id | chunk        | embedding
7  | a short quote        ────→    1  | 7        | whole quote  | [0.02,…]
8  | a long speech…        ──┬──→  2  | 8        | first piece  | [0.11,…]
                              └──→ 3  | 8        | second piece | [0.54,…]
```

**Embedding model choice:** ek dafa decide karne wali cheez, kyunki model badalna sab kuch re-embed
karwata hai. Default: Gemini's `gemini-embedding-001` (free) ya OpenAI's `text-embedding-3-small`, dono
1536 dimensions par.

```text
Create a companion table quotes_embedding with a foreign key to quotes,
the chunk text, and an embedding vector(1536) column. Then write a small
embedding worker that finds quotes with no current embedding, chunks the
quote text, embeds each chunk, and inserts the vectors. Run it once to
backfill.
```

**Done jab:** har quote ki `quotes_embedding` mein kam az kam ek row ho.

> **Sync mein kaise rehta hai:** Simple version poll karti hai — worker schedule par re-run hota hai.
> Change-driven chahiye? Trigger row ko "dirty" mark kar deta hai, worker agli baar pick kar leta hai.

## Concept 7 — Chunking: Woh Lever Jo Aapki Ceiling Set Karta Hai

Poora document ek vector mein embed karo to woh **mush** ban jata hai — sab kuch ka blurry average.
Isliye **chunks** mein todo, har chunk apna vector paye.

- **Size:** bara chunk = kai topics = unfocused vector. Chota chunk = context kho deta hai. Kuch sau
  tokens common starting point hai.
- **Overlap:** thora overlap (10-20%) sentence ko boundary par orphan hone se bachata hai.

**Yeh apna concept kyun deserve karta hai:** chunking aapki **recall ceiling** set karti hai. Agar sahi
jawab kabhi ek single chunk mein clean tarike se nahi landa, koi bhi embedding model usay recover nahi
kar sakta.

## Concept 8 — Semantic Search: Distance Se Order Karo

App phrase ko apna **query vector** banata hai, database stored chunks ko is se kitni door hain us se
sort karta hai. Sirf ek naya SQL piece: **distance operator** — `<=>` (cosine distance), is poore course
mein use hota hai.

```sql
SELECT q.person, q.city, q.quote
FROM   quotes_embedding e
JOIN   quotes q ON q.id = e.quote_id
ORDER  BY e.embedding <=> $1
LIMIT  5;
```

"the city that never sleeps" search karo, top results New York ke quotes hongi — chahe unmein "New York"
lafz na ho — kyunki **meanings** qareeb hain.

## Concept 9 — RAG: Retrieve, Phir Generate

Semantic search relevant text **dhoondti** hai. **RAG** ek qadam aage jata hai: retrieved chunks ko
prompt mein daalta hai aur LLM se aapke data mein grounded answer mangwata hai.

**Do stages:**
1. **Retrieve (Postgres mein):** top-k relevant chunks pull karo (k = 5 achi shuruaat)
2. **Generate (app mein):** prompt = system instructions + retrieved chunks + user question → LLM →
   answer

```text
Build a search_quotes(question) function: embed the question, run our
top-k semantic search, return matching chunks. Then run it and show me
what comes back.
```

Phir:

```text
Now build answer_question(question) on top: call search_quotes, format
chunks into a prompt, call the LLM, return the grounded answer.
```

**Agar retrieval sloppy hai** — galat chunks, bohat zyada, irrelevant — LLM bura jawab dega aur log "AI"
ko blame karenge. **Zyada tar waqt yeh retrieval hoti hai.**

> **"RAG is dead" ke baare mein:** Log kehte hain RAG mar chuka, phir agli saans mein aisa system
> describe karte hain jo documents index karta hai, queries embed karta hai, chunks retrieve karta hai,
> phir generate karta hai. **Yeh ab bhi RAG hai.** Jo badla woh mechanism nahi — packaging hai. Agents,
> tool calls, multi-step reasoning ab isi retrieve-then-generate loop ke **upar** baithte hain.

> **Yeh agent ke yaad rakhne ka tareeqa bhi hai:** `answer_question()` sirf chatbot backend nahi — yeh
> ek **tool hai jo agent call karta hai.** RAG woh searchable context hai jispar agent draw karta hai.

---
[⬅ Foundations](00-foundations.md) · [⬆ Index](README.md) · [Agla: Search Ko Fast Banana ➡](02-making-search-fast.md)
