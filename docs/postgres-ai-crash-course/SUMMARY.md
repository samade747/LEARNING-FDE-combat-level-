# Give Your AI Searchable Context: RAG on Postgres with pgvector — Summary

Yeh chapter sikhata hai RAG (Retrieval-Augmented Generation) Postgres + pgvector par banana — 15 concepts,
core idea: agent ko sahi information sahi waqt par dena, baaki bahar rakhna, aur zyada tar applications
ke liye **Postgres hi AI database hai** (alag vector DB ki zaroorat nahi).

## 00 — Foundations (Concepts 1-4)

- **Concept 1 — Aapka job:** ML team nahi chahiye, sara SQL khud nahi likhna — agent ko precise
  instruction do, output verify karo, architecture choices khud decide karo. **System of Record:** agents
  ko authoritative ground truth chahiye warna hallucinate karte hain — RAG on Postgres yehi deta hai.
- **Concept 2 — Vectors/Embeddings:** Vector = numbers ki list; embedding model content ko usme convert
  karta hai; similar-meaning texts paas-paas hote hain. Vector database yeh lists store + nearest-match
  dhoondta hai.
- **Concept 3 — Extensions (Neon):** **pgvector** (hamesha, Neon pre-installed) = `vector` type +
  distance operators + HNSW/IVFFlat indexes. **pgvectorscale** (TigerData native / Neon graduate-tier) =
  StreamingDiskANN, compression. Ek-database payoff: similarity search + `WHERE` filter ek hi query,
  ek hi source of truth. Embedding worker database se bahar likha jata hai (source → chunk → embed →
  save → search).
- **Concept 4 — Neon connect:** Neon = serverless Postgres, pgvector built-in, agent Neon MCP server se
  operate karta hai (OAuth, no API key). Plan check: branch par kaam (production nahi), pgvector
  `CREATE EXTENSION`, worker Neon se bahar. Neon MCP **dev-only** hai, production ke liye nahi.

## 01 — Pehla RAG (Concepts 5-9)

- **Concept 5 — Schema:** Vectors data ke saath, companion table mein — ek source of truth.
- **Concept 6 — Embeddings worker:** bina-vector rows dhoondo → chunks todo → vector mango → save karo.
  Companion table (`quotes_embedding`) mein har chunk apni row, foreign key se source ki taraf. Embedding
  model ek dafa decide (Gemini `gemini-embedding-001` free ya OpenAI `text-embedding-3-small`, 1536-dim).
  Sync: simple poll (schedule re-run) ya trigger "dirty" mark kare.
- **Concept 7 — Chunking:** poora doc ek vector = mush. Chunks size (kuch sau tokens common) + overlap
  (10-20%, boundary-orphan se bachata hai). Chunking **recall ceiling** set karti hai — jawab kabhi ek
  clean chunk mein na ho to koi model recover nahi kar sakta.
- **Concept 8 — Semantic search:** query → query vector; distance operator `<=>` (cosine) se sort. Meaning
  se match hota hai, exact lafz zaroori nahi.
- **Concept 9 — RAG (retrieve then generate):** 2 stages — retrieve (Postgres, top-k~5) + generate (app,
  prompt = system + chunks + question → LLM). Sloppy retrieval = bura jawab, "AI" blamed hota hai (zyada
  tar galti retrieval ki hoti hai). "RAG is dead" myth: mechanism wahi hai, packaging badli — agents/tool
  calls isi retrieve-then-generate loop **ke upar** baithte hain. `answer_question()` ek tool hai jo
  agent call karta hai.

## 02 — Search Ko Fast Banana (Concepts 10-11)

- **Concept 10 — Index kab chahiye:** bina index exact scan, chota table theek. ~100,000 vectors se neeche
  exact search usually kaafi fast + correct — threshold benchmark se decide karo, default se nahi.
- **Concept 11 — Kaunsa index:** IVFFlat (medium/low-memory, mostly superseded), **HNSW** (Neon default,
  ~100k-10M, RAM-bound), StreamingDiskANN (TigerData, 10M+, filtered search). Ek column = ek index type.
  `vector_cosine_ops` query distance function se match hona zaroori. Build-time (`m`, `ef_construction`) —
  benchmark karo, yaad mat karo. Query-time `ef_search` (high = behtar recall, slower). `EXPLAIN ANALYZE`
  se prove karo (Index Scan vs Seq Scan). **5 failure modes:** dimension mismatch, vector type client mein
  register nahi hua, koi index nahi, operator/index mismatch, poore documents (chunks nahi), EXPLAIN
  ANALYZE skip karna. **Filtered-search trap:** HNSW `WHERE` fixed candidate budget ke baad apply karta
  hai — matches miss ho sakte hain; fix `ef_search` barhao ya partial index.

## 03 — Search Ko Achha Banana (Concepts 12-15)

- **Concept 12 — Eval-driven development:** dozen real questions pehle likho (eval set), har system change
  par re-run karo. Bad answer ko stages mein trace karo: retrieval (sahi chunks?) → context (kitne diye
  gaye?) → generation. 9/9 baar galti retrieval hoti hai, LLM nahi.
- **Concept 13 — Filtered search:** vectors data ke saath hain isliye bas `WHERE` clause — metadata filter,
  time filter, permissions filter (`clearance_level <= $user_level`).
- **Concept 14 — Hybrid search:** keyword + vector dono chalao, **Reciprocal Rank Fusion (RRF)** se merge
  (position-based, scale-mismatch se bachne ke liye). Concept+specific-term queries par sabse zyada jeetta
  hai. Default nahi — eval set par confirm karo.
- **Concept 15 — Multi-tenancy + text-to-SQL:** shared-table+tenant_id (weakest) / schema-per-tenant (SaaS
  sweet spot) / database-per-tenant (strongest). Boundary database mein enforce karo — **Row-Level
  Security (RLS)**, lekin RLS superuser/owner ko bypass kar jata hai, app non-owner role se connect ho.
  Text-to-SQL: clear naam + `COMMENT`s + example pairs, generated SQL hamesha review karo.

## 04 — Worked Example + MCP Tool + Deployment + Agent (Parts 5-8)

- **Part 5 — Worked example:** rhythm plan → review → execute → evaluate → iterate. Docs home (10 files)
  → plan (strong model) → review (branch? pgvector? env keys?) → execute 3 checkpoints (DB+worker,
  retrieval, generation) → evaluate/iterate. Phir 4 required tuning exercises: index fast dekho
  (100k+ synthetic, Seq→Index Scan, ef_search), filter add karo (B-tree), rare code hybrid search se
  catch karo, RLS se tenant wall-off (non-owner role se test — zaroori, warna owner bypass karta hai).
- **Part 6 — MCP tool ki tarah ship:** `search_quotes()`/`answer_question()` ko MCP server mein wrap karo
  (Streamable HTTP, cloud-hosted) — kisi bhi agent discover/call kar sake. 2 alag MCP servers: Neon MCP
  (dev-time admin, stdio, local) vs RAG MCP (runtime product, hosted) — confuse mat karo. Docstring hi
  interface hai; retrieval **read-only** rahe (read-only DB role). Deploy: stateless build, koi code
  change nahi chahiye (Cloud Run/Render/Railway/Fly).
- **Part 7 — Kahan chalta hai:** Neon (build se production tak), Neon branches (dev/preview/evals), Tiger
  Data Cloud (pgvectorscale scale). Lock-in nahi — plain Postgres+pgvector kisi bhi Postgres host par
  (Supabase, Xata, RDS, Azure). Dedicated vector DB usually zaroori nahi.
- **Part 8 — Agent ko sonpo:** yeh course retrieval banata hai, Build AI Agents course loop sikhata hai.
  Connect: MCP server ki tarah ya `@function_tool` wrap. **Memory vs knowledge:** memory = conversation se
  yaad (sessions), RAG = durable searchable **knowledge** jo agent lookup karta hai. Aage: Eval-Driven
  Development, Build AI Agents, Digital FTE. Throughline: sahi information, sahi waqt, irrelevant bahar.
