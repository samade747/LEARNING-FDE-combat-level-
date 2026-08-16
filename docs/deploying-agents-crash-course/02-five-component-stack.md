# 02 — Part 2: The Five-Component Stack (Concepts 4-7)

## Concept 4 — FastAPI Bataur Harness Web Layer

Harness ko long-running HTTP service hona hai. Chuna FastAPI hai — specific reasons:

- **Async story** — OpenAI Agents SDK `asyncio` ke around bani hai. FastAPI async-native hai, `async
  def` handlers `await` seedhe SDK ko karte hain, thread-pool workarounds ke bina
- **Schema story** — FastAPI handlers ke type hints se OpenAPI schema generate karta hai. Eval suite
  checked requests se hit kar sakti hai, typed client libraries generate ho sakti hain, API team ke
  liye documented ho jati hai
- **Pydantic story** — FastAPI request/response data check karne ke liye Pydantic use karta hai, SDK
  bhi internally Pydantic use karti hai — ek hi library, boundary par ek hi baar validation

**Kya FastAPI nahi hai:** general web framework nahi (HTML rendering ke liye galat choice), queue
nahi (request se lambi task queued hoti hai, client wapis check karta hai). Lab `POST /runs` endpoint
ke around yehi pattern setup karta hai.

## Concept 5 — Azure Container Apps (ACA) Bataur Harness Runtime

Harness ek containerized FastAPI service hai jo continuously chale, traffic ke sath scale ho, secrets
safely rakhe, host fail hone par survive kare. Chuna Azure Container Apps hai.

**5 capabilities jo harness ko chahiye:**
1. **Public address** — ACA managed HTTPS address certificates ke sath deta hai
2. **Autoscale** — traffic ke rules par copies scale karta hai. **Scale-to-zero cost lever hai:** koi
   traffic nahi to zero copies chalti hain, pay nahi karte; quiet spell ke baad pehli request chand
   seconds wait karti hai
3. **Secrets** — name se reference kiye jate hain, actual values kabhi config/image mein nahi ate
4. **Revisions** — har deploy immutable revision banata hai, traffic kisi bhi percentage mein split ho
   sakta hai — blue/green deploys aur rollback built-in
5. **Observability** — logs, metrics, traces Azure ke monitoring tools mein feed hote hain

**ACA specifically kyun, Cloud Run/Fly.io/raw Kubernetes nahi:** Microsoft isi profile ke liye ACA
position karta hai; revisions/traffic splitting first-class hain; scale-to-zero honest hai (asal mein
zero copies chalti hain, kuch "managed" services ek copy warm rakhte hain aur bill karte hain).

**ACA galat choice kab hai:** peak par 25+ copies chahiye ho (full Kubernetes better fit); active-
active multi-region chahiye ho (Concept 14 isay honestly naam deta hai).

## Concept 6 — Neon Postgres: Durable State Ke Liye

**Postgres kyun, Redis ya document store nahi:** harness ki state relational shape mein hai (sessions
→ runs → traces/artifacts, foreign keys/joins), transactional integrity chahiye ("run complete mark
karo, trace insert karo, session timestamp update karo" — sab ya kuch nahi), relational reads ("last
10 runs with traces" ek textbook SQL query hai).

**Neon specifically kyun:** **serverless** (compute khud scale up/down, idle hone par near-zero — cost
model baaki stack se match karta hai), **branching** (per-developer copies, per-PR test databases
seconds mein), **real Postgres** (SQL/client libraries same rehte hain, migrate karna connection-string
change hai).

**Harness ka schema — 5 tables:** `sessions` (user ka ongoing context), `runs` (har agent task),
`traces` (poora SDK trace), `artifacts` (R2 mein files ke pointers), audit log (immutable record, eval
suite aur compliance ke liye).

> **Neon ka footgun (lab handle karta hai):** pooled endpoint `search_path` server settings silently
> drop karta hai, isliye harness har statement schema-qualify karta hai (`public.runs`), aur schema
> direct/non-pooled endpoint ke against chalti hai. (`channel_binding=require` parameter jo Neon ki
> connection string mein hoti hai, `asyncpg` ke liye harmless hai, koi asal problem nahi.)

**Connection pooling optional nahi hai** — harness kai copies mein scale hota hai, Postgres kuch sau
connections ke upar gir jata hai. Neon ka pooled endpoint thousands harness connections ko chand real
Postgres connections mein multiplex karta hai.

## Concept 7 — Cloudflare R2: Files Aur Artifacts Ke Liye

**Object storage kyun, database ya container disk nahi:** files relational database ke liye galat
shape hain (Postgres mein bara file column mein rakhna backups ko phula deta hai); container ka local
disk restart par gayab ho jata hai. Object storage sahi shape hai jab files kisi ek container se zyada
zinda rahein aur kai copies se reachable hon.

**R2 specifically kyun, S3/GCS nahi:** **egress story.** Apni files R2 se read karna **free** hai. S3/
GCS/Azure Blob egress ke liye charge karte hain (~5-12 cents/GB). Terabytes-scale harness S3 par
hundreds of dollars egress mein kharch karta, R2 par zero. R2 S3 API bhi bolta hai — endpoint URL badal
kar migrate ho sakte ho. April 2026 SDK R2 ko supported Manifest mount source ki tarah list karta hai.

**Bucket ke 3 prefixes:** `inputs/` (user uploads), `outputs/` (agent ke produced files), `knowledge/`
(long-lived knowledge content).

**Presigned URLs** — sandbox ko access root credentials ke bina milta hai. Harness root credentials
rakhta hai (kuch bhi read/write kar sakte hain), sandbox ke sath share nahi karta. Uski jagah ek
specific object ke liye presigned URL mint karta hai, short expiry ke sath. Sandbox sirf woh access kar
sakta hai jo URL allow kare; sandbox marne par URL bekaar ho jati hai. **Concept 2 ki credential
separation concrete ban jati hai:** compromised sandbox buckets list nahi kar sakta ya doosre user ka
data reach nahi kar sakta.

**Lifecycle policies** storage ko write-only graveyard banne se rokti hain — lab `outputs/` par 30-din
cleanup set karta hai, curated `knowledge/` par koi nahi.

---
[⬅ The Deployment Problem](01-the-deployment-problem.md) · [⬆ Index](README.md) · [Agla: The Execution Plane ➡](03-execution-plane.md)
