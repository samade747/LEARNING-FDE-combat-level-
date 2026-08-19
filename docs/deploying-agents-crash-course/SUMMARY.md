# Deploy Your Agent Harness to the Cloud — Summary

17 Concepts, 4 tracks, 9 (10) deployment decisions. Ab tak jitne agents banaye sab laptop par chalte the —
yeh course real cloud service banata hai: brain FastAPI on Azure Container Apps, memory Neon Postgres,
files Cloudflare R2, risky code E2B/Cloudflare Sandbox. **Core idea: harness control plane hai jo aap own
karte ho; sandbox execution plane hai jo throwaway hai.**

## 00 — Overview: Quick Win, Tracks, Stack Primer

- **3 terms:** Harness (brain+controls, secrets, state, agent loop — generated code nahi chalata), Sandbox
  (isolated workspace jahan generated code chalta hai, harness secrets tak access nahi), Manifest (workspace
  description — kya mount karna, kya on karna).
- April 2026 OpenAI Agents SDK update ne harness ko sandbox se first-class alag primitive banaya.
- **Quick Win (~15 min):** `GET /health` → `{"status":"ok","model":..., "backends":{postgres:false,
  sandbox:false, r2:false}}` — har agla decision ek flag `true` karta hai.
- **4 Tracks:** Reader (3-4hr, no cloud), Beginner (1-2 din, local Docker), Intermediate (3-5 din, cloud
  deploy+state+storage+observability, sandbox stubbed), Advanced (7-10 din, poori discipline).
- **Advanced sprint (10 din):** scaffold → containerize+deploy → Neon → R2 → ⭐shippable checkpoint (Din 5)
  → sandbox → observability → eval suite (2 din) → production checklist.
- **Rough edges:** Python-only, code companion se traceable, ek cloud/sandbox/DB/storage (principles
  transferable), cost real, no multi-region.
- **Stack Primer:** Docker (container=throwaway, data nahi), FastAPI (async-native, Pydantic), Neon
  Postgres (table/schema/migration/pooling), Cloudflare R2 (bucket/object/presigned URL/lifecycle). Kya
  nahi chahiye: Kubernetes, IaC, service mesh, message broker.

## 01 — The Deployment Problem (Concepts 1-3)

- **Concept 1 — "Works On My Machine" Deployment Nahi:** laptop assumptions (single process, local file
  state, same-process code execution) production ke 6 properties se tootti hain (multi-user, restart-
  surviving state, isolated code execution, secrets out of reach, observable/auditable runs). Honest
  jawab: ek ya zero properties minor changes se milti hain.
- **Concept 2 — Harness/Sandbox Split:** Harness = brain (requests, agent loop, durable state, secrets).
  Sandbox = hands (workspace, shell/file/code execution, koi secrets access nahi siwaye Manifest-mounted).
  Boundary = network+security boundary. **4 wajah:** security, durability (harness sandbox-death survive
  kare), scalability (alag scale needs), observability (harness record own karta hai). **2 anti-patterns:**
  harness ko sandbox ke andar chalana, agent-generated code ko harness ke andar chalana ("original sin").
- **Concept 3 — 5 Surfaces:** long-running HTTP service (FastAPI/ACA), durable state (Neon), file/artifact
  storage (R2), isolated execution (sandbox), orchestration (SDK khud). Poori composition ek diagram mein
  di gayi hai. Python-only tak April 2026.

## 02 — The Five-Component Stack (Concepts 4-7)

- **Concept 4 — FastAPI:** async-native (SDK bhi asyncio), OpenAPI schema auto-generate, Pydantic shared
  library SDK ke sath. General web framework nahi, queue nahi.
- **Concept 5 — Azure Container Apps:** 5 capabilities — public address, autoscale (scale-to-zero cost
  lever), secrets, revisions (blue/green built-in), observability. ACA vs Cloud Run/Fly/K8s — revisions/
  traffic-splitting first-class, honest scale-to-zero. Galat choice: 25+ replicas ya active-active
  multi-region chahiye ho.
- **Concept 6 — Neon Postgres:** relational shape + transactional integrity + relational reads. Neon:
  serverless, branching, real Postgres. 5-table schema (sessions, runs, traces, artifacts, audit log).
  **Footgun:** pooled endpoint `search_path` silently drop karta hai — schema-qualify karo (`public.runs`).
  Connection pooling optional nahi.
- **Concept 7 — Cloudflare R2:** files relational DB ke liye galat shape; container disk restart par
  gayab. R2 vs S3/GCS: **egress free** (apni files read karna free). 3 prefixes: inputs/, outputs/,
  knowledge/. **Presigned URLs** — sandbox root credentials ke bina scoped access. Lifecycle policies
  (30-din cleanup outputs par, knowledge par nahi).

## 03 — The Execution Plane (Concepts 8-10)

- **Concept 8 — Sandbox Capabilities:** filesystem, shell, package install, mounted storage, snapshot+
  resume. 3 production-grade properties: isolation (provider-enforced), ephemerality (task-fresh),
  fast provisioning (seconds). Sandbox nahi: long-lived VM, serverless function, Kubernetes.
- **Concept 9 — Sandbox Provider Chunna:** Cloudflare (paid Workers plan + bridge Worker; R2-proximity
  fast) vs **E2B (free Hobby tier, native SDK, no bridge — companion default)**. Alternatives: Modal (GPU
  ML), Daytona (data residency), Vercel, bring-your-own. "Ek chuno aur ship karo."
- **Concept 10 — Handoff:** Manifest = entries (path → file/dir/repo/storage mount). Capabilities:
  `Capabilities.default()` **replace** hoti hai passed list se (add karne ke liye concatenate karo) —
  real footgun. Sandbox `RunConfig` ke through attach hota hai, `Runner.run` argument nahi
  (`SandboxRunConfig`). Credential discipline: presigned URLs + short expiry, sandbox buckets enumerate
  nahi kar sakta. Run lifecycle: 5 steps (receive → manifest+provision → agent loop+trace → snapshot-
  resume on fail → R2/Neon persist + destroy).

## 04 — Observability Aur Evals As Architectural Surfaces (Concepts 11-12)

- **Concept 11 — Observability:** zyada tar production AI failures observability failures hain — feature
  nahi, architectural surface. **4 surfaces, alag sawal:** Application Insights (infra healthy?), OTel
  traces (request flow across services?), SDK traces (agent ne kya kiya is run mein?), Phoenix (behavior
  waqt ke sath kaise badla?). Overlap karte hain, replace nahi — shared `run_id` se interconnect.
- **Concept 12 — Evals As Surface:** Eval-Driven Development ke 4 frameworks yahan attach hote hain.
  Boundary = **traces** (Neon durable + Phoenix live sample). Run khatam → Neon synchronous write + Phoenix
  async stream. Attachment points: CI gate, scheduled nightly jobs, Phoenix inline checks. Plan karna
  zaroori hai pehle se — observability se pehle produce hui traces gayab ho jati hain.

## 05 — The Deployment Lab (Decisions 0-9)

- 2 tareeqe: Full build (cloud deploy) ya Simulated (companion parho, koi provision nahi).
- **D0** SDK probe/reconcile (live docs jeetein). **D1** Harness scaffold (`/health` graceful degrade).
  **D2** Containerize (python:3.12-slim, cached layers). **D3** ACA deploy (`az acr build`, scale-to-zero,
  named secrets). **D4** Neon wire (pooled vs direct endpoint rule). **D5** R2 wire (boto3, presigned URL,
  1hr expiry). **D6** Sandbox wire (E2B default, cost note on Cloudflare paid plan). **D7** Observability
  wire (OTel, shared run_id, ~10% sample successful + 100% failed). **D8** Eval suite wire (DeepEval CI
  gate, nightly job, Phoenix inline, weekly promotion ritual). **D9** Production checklist (secrets
  rotation, blue/green, on-call runbook 5 scenarios, backup/recovery, rate limits, cost alerts).

## 06 — Honest Frontiers Aur Closing (Concepts 13-17)

- **Concept 13 — Cost Economics:** 5 bill layers, model API **90-98%** har scale par; infrastructure <5%.
  Small (~100 runs/din) ~$100s/month; Medium (~10k/din) low tens-of-thousands; Large (~1M/din) seven
  figures. 4 takeaways: optimize model not infra, infra cost linear+predictable, R2 free-egress matters
  most for file-heavy, sandbox cost scales with execution time.
- **Concept 14 — Multi-Region:** default single-region. 3 triggers: latency, availability (99.99%+),
  compliance. R2+sandbox already global; ACA/Neon need extra work per-region.
- **Concept 15 — Recipe Se Migrate:** 5 triggers — 25+ ACA replicas, multi-region active-active, GPU
  compute, in-cloud-only sandbox, Postgres se aage (extreme write volume).
- **Concept 16 — Deployment Kya Solve Nahi Karta:** compliance certification, incident-response program,
  legal liability, behavior-level prompt injection, model upgrades (eval suite discipline hai), cost
  runaway. **5 Cheezein Jo Nahi Karni Chahiye:** exec(model_output) in harness, root creds in Manifest,
  skip scale-to-zero in dev, deploy without eval suite, no rate limiting.
- **Concept 17 — Realization:** deployed harness = Manufacturing track jo banaya usay ship karta hai.
  "Recipe se deviate karna theek hai. Architecture se deviate karna theek nahi." 3 unshipped frontiers:
  agent-to-agent commerce, owner-delegate deployment, deeper multi-cloud.
- **Cheat Sheet** — 17-concept one-liner table di gayi hai, plus quick-reference deployment commands (uv,
  az cli, psql).
