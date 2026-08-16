# 00 — Part 1: Foundations (Concepts 1-4)

## Concept 1 — Aap Kya Bana Rahe Ho (Aapka Job)

Sabse common misconception: AI applications ML team maangti hain. Nahi. Doosra misconception jo yeh
course fix karta hai: *aapko sara SQL khud likhna hoga.* Nahi. Aap ek agent ko direct karte ho jo
pgvector ke operators aur embedding workflow already jaanta hai.

Yeh badalta hai "material samajhna" ka matlab. Aap syntax yaad nahi kar rahe — itna mental model bana
rahe ho ke:

- Agent ko precise instruction do ("embedding wahi table mein rakho, cosine distance use karo, HNSW se
  index karo")
- Jo bane usay parh kar galti pakar sako
- Architecture choices khud decide karo jo agent nahi karega

> **Mindset shift:** "semantic search ki SQL kya hai" mat poocho. Kaho: "is table par semantic search
> banao; yeh mere constraints hain; pehle plan dikhao."

> **System of Record:** Jensen Huang ka argument hai agents ek system of record ki zaroorat khatam nahi
> karte — woh **usi par depend** karte hain. Authoritative ground truth ke bina agent hallucinate karta
> hai; uske sath, woh execute karta hai. RAG on Postgres hi woh tareeqa hai jisse aap agent ko woh
> ground truth dete ho.

## Concept 2 — Vectors Aur Embeddings, 1 Minute Mein

**Vector** sirf numbers ki ek list hai — `[0.021, -0.88, 0.14, …]`. **Embedding model** content (sentence,
paragraph) ko is list mein badalta hai. Trick: yeh list content ka **meaning** capture karti hai — do
similar-meaning texts ki lists paas paas hoti hain, chahe alfaz alag hon.

**Vector database** bas ek system hai jo yeh lists store karta hai aur di gayi list ke sabse qareeb
lists tezi se dhoondta hai. User sawal pooche, app us sawal ko vector banata hai, database se poochta
hai "kaunse stored vectors is se sabse qareeb hain?"

## Concept 3 — Extensions — Neon Par Kya Milta Hai

Postgres **extensions** se vector database banta hai. Poore course ke liye sirf ek seekhna hai:
**pgvector.** Yeh 3 cheezein add karta hai: `vector` type, distance operators, aur fast search ke liye
indexes. Neon par yeh **pre-installed** hai — ek statement se on ho jata hai.

| Extension | Kya Add Karta Hai | Kab Chahiye |
| --- | --- | --- |
| **pgvector** | `vector` type, distance operators, HNSW + IVFFlat indexes | Hamesha — Neon par pre-installed |
| **pgvectorscale** | StreamingDiskANN index, compression, large-scale filtered search | TigerData par native; Neon par graduate-tier |

**Ek-database ka payoff:** aapke vectors us row ke **saath** rehte hain jise woh describe karte hain —
to similarity search aur `WHERE price < 2000` filter **ek hi query** mein, **ek hi source of truth**
par. Koi doosra database nahi, koi sync pipeline nahi.

> **Embedding worker khud kyun likhte ho:** pgvector embeddings **banata** nahi — model call kar ke
> vectors likhna aapka kaam hai. Chota **worker** likha jata hai (agent likhta hai): source table →
> chunk → embed → embeddings table mein likho → pgvector se search karo. Yeh database se **bahar**
> rehna jaan-boojh kar hai — ek stateful system of record volatile external API par depend nahi karna
> chahiye.

## Concept 4 — Agent Ko Neon Se Connect Karo

Hum apna database nahi chalate. **Neon** — serverless Postgres, pgvector built-in — use karte hain, aur
agent isay **Neon MCP server** se operate karta hai. Aap kabhi Neon console ya `psql` khud nahi kholte.

**One-time wiring:** Course base se `.mcp.json`/`opencode.json` mein Neon MCP server already declared
hai — browser mein ek dafa authorize karo (OAuth), koi API key manage nahi karni.

```text
Using the Neon MCP server, create a project called agent-factory-rag and
enable the pgvector extension on it. Then create a branch called dev for
us to build on, and save that branch's connection string to .env as
DATABASE_URL. Show me the plan before you run anything.
```

**Plan check karo:**
- **Branch** par kaam ho raha hai, production par nahi? Branching Neon ki superpower hai — instant
  clone (**copy-on-write**: sirf badli hui cheez store hoti hai)
- pgvector ek statement se enable ho raha hai (`CREATE EXTENSION IF NOT EXISTS vector;`)
- Embeddings ke liye agent ek chota **worker** banata hai jo Neon se **bahar** chalta hai

> **Caution:** Neon MCP server **development** ke liye hai, production ke liye nahi. Har action jo
> agent propose kare, approve karne se pehle review karo.

---
[⬆ Index](README.md) · [Agla: Pehla RAG ➡](01-first-rag.md)
