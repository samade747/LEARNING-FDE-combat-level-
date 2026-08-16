# 00 — Overview: Quick Win, Tracks, Aur Stack Primer

## Ek Idea, Poora Course

Ab tak jitne agents banaye, sab sirf aapke laptop par chalte the. Yeh course us agent ko real cloud
service banata hai jo users internet par reach kar sakein: uska brain managed cloud runtime par, uski
memory database mein, uski files object storage mein, aur uska risky code ek alag locked-down sandbox
mein.

**Poore course ka core idea:** **Harness woh control plane hai jo aap own karte ho aur chalate rehte
ho. Sandbox woh execution plane hai jo aap banate ho, ek baar use karte ho, phenk dete ho.** Harness
keys, state, aur audit log rakhta hai; sandbox in mein se kuch nahi rakhta aur risky kaam karta hai.
Har concept aur decision isi ek split ki elaboration hai.

> **3 terms jo poora course carry karte hain:**
> - **Harness** — agent ka brain aur controls: agent loop chalane wala code, tool decide karna, secrets
>   rakhna, runs ke darmiyan state rakhna. Agent ka generated code **nahi** chalata. Is course mein ek
>   FastAPI web app hai cloud mein.
> - **Sandbox** — ek separate, locked-down workspace jahan agent ka generated code asal mein chalta
>   hai. Files parhta hai, shell commands chalata hai, lekin harness ke secrets ya database tak access
>   nahi rakhta. Sasta banane ke liye, ek baar use, phir throw.
> - **Manifest** — chota description ke sandbox ko kya chahiye: kaunse files mount karne, kaunsa
>   storage attach karna, kaunsi abilities (shell, filesystem) on karni. Workspace ek baar describe
>   karte ho, SDK usay kisi bhi supported provider par chalata hai.

> **April 2026 mein kya badla:** OpenAI ne April 15, 2026 ko Agents SDK update ship ki jo harness ko
> sandbox compute se alag first-class primitive banati hai. Pehle teams model clients, container
> runtimes, credential isolation, state, tool routing sab hath se stitch karti thi. Ab yeh built-in
> primitive hai — isi wajah se yeh course ab teachable hai.

## Quick Win — Harness Apni Laptop Par ~15 Minute Mein Boot Karo

Cloud chune se pehle, prove karo harness aapki apni machine par chalti hai. Companion code download
karo (`deploying-agents/` folder, `panaversity/agentfactory-manufacturing` repo), coding agent mein
kholo, `AGENTS.md` parhwao.

**Coding agent ko paste karo:**
```text
Read AGENTS.md, then boot Maya's harness locally so I can see it run.
1. Run the SDK probe... 2. Install dependencies, copy .env.example to .env, no keys yet.
3. Start the harness (make run, serves on localhost:8000).
4. In a second shell, request GET /health and show me the exact response.
```

**Done jab:** `GET /health` yeh exactly wapis de:
```json
{"status": "ok", "model": "gpt-5.4-mini", "backends": {"postgres": false, "sandbox": false, "r2": false}}
```

Yeh response harness ki honest baat hai: zinda hai, apna model janta hai, koi optional backend abhi
wired nahi (sab `false`). Har agla decision ek flag ko `true` karta hai.

## 4 Learning Tracks

| Track | Waqt | Kya Complete Hota Hai |
| --- | --- | --- |
| **Reader** | ~3-4 ghante | Quick Win + sab 17 concepts + closing. Koi cloud accounts nahi |
| **Beginner** | ~1-2 din | Reader + SDK probe + scaffold + containerize. Harness locally Docker mein, OpenAI + local DB se baat karta hai |
| **Intermediate** | ~3-5 din | Beginner + cloud deploy + durable state + file storage + observability. Sandbox abhi stubbed |
| **Advanced** | ~7-10 din | Intermediate + sandbox + eval suite + production checklist. Poori discipline |

**Advanced sprint cadence (1 engineer, 4-6 ghante/din):**

| Din | Focus | Artifact |
| --- | --- | --- |
| 1 | Concepts 1-4 + scaffold | Local FastAPI app, stubbed `/runs` |
| 2 | Containerize + deploy | Public internet par reachable harness |
| 3 | Neon Postgres wire | Durable state |
| 4 | Cloudflare R2 wire | File storage |
| 5 | ⭐ **Shippable checkpoint** | Deployed harness, real users use kar sakte hain |
| 6 | Sandbox wire | Code execution safely |
| 7 | Observability wire | Alert se agent behavior tak fast navigate |
| 8-9 | Eval suite wire | Regression CI mein pakri jati hai |
| 10 | Production checklist + handoff | Production-ready harness + team jo isay operate kar sake |

## Tayyari Check

- Companion zip download kar chuke ho
- Command line par comfortable ho
- Python code parh sakte ho
- OpenAI API key with Agents SDK access (Beginner+)
- Azure account (Intermediate+)
- Neon account (Intermediate+)
- Cloudflare account with R2 enabled (Intermediate+)

## Rough Edges (Pehle Se Jaan Lo)

- Code companion se traceable hai — real `openai-agents` package ke against boot kiya gaya
- SDK tezi se badalti hai — lab ka pehla step ek probe decision hai (installed version confirm karo,
  live docs se reconcile karo)
- **Python only** — TypeScript support planned hai lekin undated
- Ek cloud, ek sandbox, ek database, ek storage provider — principles doosre clouds par transfer
  hote hain
- Cost real hai — low-traffic personal use ke liye chand dozen dollars/month, production traffic ke
  liye hundreds
- No multi-region — ek region tak deploy hota hai

## Stack Primer — 4 Chize Jo Jaanna Zaroori Hai

**1. Docker/Containers** — ek container aapki app + har cheez jo usay chalne ke liye chahiye ka sealed
bundle hai. "Works on my machine" problem solve karta hai. `Dockerfile` recipe hai, `base image`
starting point hai (harness `python:3.12-slim` se shuru), `multi-stage build` build tools ko runtime
image se alag rakhta hai, `registry` jahan images store hote hain. **Container throwaway hai; data
nahi.**

**2. FastAPI** — Python library web APIs banane ke liye. Async-native hai isliye SDK ke `await` calls
ke sath naturally kaam karti hai. `endpoint` (jaise `POST /runs`), `route handler`, `async def`/`await`,
`Pydantic models` (request/response shape check), `Uvicorn` (server jo app chalata hai).

**3. Neon Postgres** — serverless Postgres, branching ke sath. Harness ka data restart, scaling
survive kare — conversation state, run history, audit log. `table`, `schema`, `primary/foreign key`,
`migration`, `connection pooling` (Neon pooled endpoint deta hai).

**4. Cloudflare R2** — S3-compatible object storage, apni files read karna **free**. Agent ke files
(uploaded documents, generated reports) yahan rehte hain. `bucket`, `object` (key + bytes), `prefix`,
`presigned URL` (short-lived link ek specific file ke liye, root credentials share kiye bina),
`lifecycle policy` (purani objects delete karti hai).

> **Kya nahi chahiye:** Kubernetes, infrastructure-as-code, service mesh, message broker — managed
> services yeh sab operational machinery handle karte hain.

---
[⬆ Index](README.md) · [Agla: The Deployment Problem ➡](01-the-deployment-problem.md)
