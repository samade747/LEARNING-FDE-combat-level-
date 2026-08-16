# 06 — Part 6-7: Honest Frontiers Aur Closing (Concepts 13-17)

## Concept 13 — Cloud Agent Harness Ki Cost Economics

Cloud cost woh dimension hai jo zyada tar courses skip karte hain. Bill ki **5 layers**, ek layer sab
par haavi:

| Layer | Bill Ka Hissa |
| --- | --- |
| Model API (OpenAI) | 90-98% har scale par |
| Sandbox execution | high volume par baqiyon mein sabse bara |
| Harness compute (ACA) | chota; scale-to-zero idle hone par near-zero rakhta hai |
| Durable state (Neon) | chota; free tier light use cover karta hai |
| File storage (R2) | chota; egress free hai |

**Rough ranges:** Small scale (~100 runs/din) — poora bill ~$100-some/month, model API ~90%. Medium
scale (~10,000 runs/din) — low tens of thousands/month, model API ~98%. Large scale (~1 million
runs/din) — seven figures/month, almost sab model API. **Infrastructure layers poore waqt 5% se neeche
rehte hain.**

**4 takeaways:**
- **Model optimize karo, infrastructure nahi** — sasta model simple decisions ke liye, prompt caching,
  chote system prompts
- **Infrastructure cost predictable hai**, roughly linear traffic ke sath
- **R2 ki free egress** file-heavy workloads ke liye sabse zyada matter karti hai, text-heavy (jaise
  Maya) ke liye kam
- **Sandbox cost execution time ke sath scale karti hai**

## Concept 14 — Multi-Region Considerations

Yeh recipe deliberately ek region tak deploy hoti hai. Multi-region active-active bohat harder problem
hai, zyada tar deployments ko zaroorat nahi. **3 reasons jab chahiye:** latency (users globally spread
hon), availability (99.99%+ uptime commitment), compliance (data-residency rules).

- **R2 aur sandbox** already Cloudflare ke network par global hain — extra kaam nahi chahiye
- **ACA** per-environment single-region hai — multi-region matlab kai environments ek global load
  balancer ke peeche
- **Neon** doosre regions mein read replicas support karta hai, lekin writes primary par hi jate hain

Honest recipe: zyada environments, read replicas, global front door — har region ke sath operational
cost barhti hai. Agar users ek region mein hon, uptime target 99.9% ho, aur ek region data rules
satisfy kare, **single-region sahi jawab hai** — jo complexity chahiye nahi usay pay mat karo.

## Concept 15 — Recipe Se Kab Migrate Karna Hai

Yeh recipe opinionated hai aur ek specific size/shape fit karti hai. **5 triggers:**

- **Sustained heavy concurrency** ~25 ACA replicas se upar — harness ko Kubernetes par le jao (app
  code same rehta hai)
- **Multi-region active-active** — Concept 14 ke mutabiq
- **Specialized compute** (GPU work) — GPU-native sandbox provider, portable Manifest sath jata hai
- **In-cloud-only sandbox** compliance rule se — SaaS sandbox rule out, bring-your-own provider
- **Postgres se aage nikalna** bohat high write volumes par — distributed SQL/split storage, sabse
  invasive change

## Concept 16 — Deployment Kya Solve Nahi Karta

**6 gaps jo explicitly naam lene layak hain:**
- **Compliance certification** — technical controls milte hain, lekin certification third-party audit
  aur mahino ka evidence maangti hai
- **Incident-response program** — runbook technical remediation cover karta hai, kaun page hota hai
  ya post-mortems kaise chalte hain woh nahi
- **Agent ke actions ki legal liability** — audit log kya hua record karta hai, legal framework abhi
  ban raha hai
- **Behavior-level prompt injection** — harness/sandbox split injected code ko secrets se door rakhta
  hai, lekin crafted message se agent ka reply steer hona nahi rokta — guardrails, input checks,
  red-teaming chahiye
- **Model upgrades** — deployment inhe test nahi karti; eval suite hi discipline hai naye model ko vet
  karne ki
- **Cost runaway** — monitoring spike ghanton mein pakarti hai, daily caps aur kill switches extra
  defenses hain

## 5 Cheezein Jo Nahi Karni Chahiye

1. **Agent-generated code harness ke andar mat chalao** — `exec(model_output)` harness process mein
   SQL injection se bhi bura hai, attack surface poora model ka reasoning hai
2. **Root credentials Manifest mein mat daalo** — Manifest mein jo bhi ho sandbox tak jata hai. Sirf
   presigned URLs aur short-lived tokens boundary cross karein
3. **Development mein scale-to-zero skip mat karo** — 24/7 warm dev app, logon/services ke across
   multiply hokar, chupke se sainkron dollars/month idle compute ke liye kharch karta hai
4. **Eval suite wire kiye bina deploy mat karo** — sabse mehnga shortcut. Changes code review pass
   karte hain, behavior regress karte hain, hafton baad complaints ki tarah surface hote hain
5. **Rate limiting ke bina harness mat chalao** — day-one deployments bina isके ek viral mention ke
   baad ek din mein model provider ko fortune pay kar chuke hote hain

## Concept 17 — Deployed Harness: Realization

Manufacturing track ne AI-native company banayi aur measure ki: agent loop, system of record, workforce
layer, delegate, aur behavior-measurable discipline. **Yeh course usay ship karta hai.** Deployed
harness woh jagah hai jahan yeh sab ek real service ban jata hai jo users reach kar sakein, 4 surfaces
se observed, aur eval suite se continuously grade hota hai jo production traffic se seekhti hai.

**Poora course ek idea par khara hai:** harness control plane hai, sandbox execution plane hai, aur
yehi ek separation deployment ko safe, durable, aur scalable banati hai. **Recipe se deviate karna
theek hai. Architecture se deviate karna theek nahi.**

Iske baad ka design discipline jo build se pehle chalti hai: task ke liye kaunsa agent shape fit karta
hai chunna — [Choosing Agentic Architectures](../choosing-agentic-architectures-crash-course/README.md)
mein.

**3 aur frontiers, honestly named, abhi tak ship nahi hue:**
- **Agent-to-agent commerce** — agents payment protocols se economic actors ki tarah act karein
- **Owner-delegate agent ke liye deployment** — signed delegation aur governance ledger Worker se
  heavier hain
- **Deeper multi-cloud** — active-active multi-region, apna substantial topic hai

## Cheat Sheet — 17 Concepts, Ek Nazar Mein

| # | Concept | Key Takeaway |
| --- | --- | --- |
| 1 | "Works on my machine" deployment nahi | Production matlab agent ko harness+sandbox mein re-architect karna |
| 2 | Harness/sandbox separation | Backbone: harness secrets/state ke sath orchestrate karta hai; sandbox code execute karta hai |
| 3 | SDK ko infra se kya chahiye | 5 surfaces, har ek ek stack component se mapped |
| 4 | FastAPI harness web layer | Async-native, auto-generated schemas, Pydantic |
| 5 | ACA runtime | Ingress, autoscale (scale-to-zero), secrets, revisions |
| 6 | Neon durable state | Postgres relational state ke liye; Neon serverless scaling + branching |
| 7 | R2 files ke liye | Egress-free, S3-compatible, presigned URLs |
| 8 | Sandbox capabilities | Filesystem, shell, package install, mounted storage — isolated aur ephemeral |
| 9 | Sandbox provider chunna | E2B free path; Cloudflare paid primary |
| 10 | Harness-to-sandbox handoff | Manifest workspace declare karta hai; presigned URLs; root credentials kabhi cross nahi hote |
| 11 | Observability as surface | 4 surfaces, shared run_id se tied |
| 12 | Evals as surface | Traces (Neon + Phoenix) se mediated |
| 13 | Cost economics | Infrastructure <5%; model API 90-98% |
| 14 | Multi-region | Default single-region; sirf latency/uptime/compliance ke liye multi |
| 15 | Recipe se kab migrate karna | Heavy concurrency, multi-region, GPU, in-cloud sandbox, extreme write volume |
| 16 | Deployment kya solve nahi karta | Compliance certification, incident process, legal liability, prompt injection, model upgrades, cost runaway |
| 17 | Deployed harness as realization | Manufacturing track jo banaya woh ship karta hai |

## Quick Reference — Deployment Commands

```bash
# Local dev
uv sync
uv run uvicorn maya_harness.main:app --reload
# Pin: openai-agents>=0.17,<0.18
```

```bash
# Azure Container Apps
az group create --name maya-rg --location eastus
az acr create --resource-group maya-rg --name <acr-name> --sku Basic --admin-enabled true
az acr build --registry <acr-name> --image maya-harness:latest .
az containerapp env create --name maya-env --resource-group maya-rg --location eastus
az containerapp create --name maya-harness --resource-group maya-rg \
  --environment maya-env --image <acr-name>.azurecr.io/maya-harness:latest \
  --target-port 8000 --ingress external --min-replicas 0 --max-replicas 3 \
  --secrets "openai-api-key=$OPENAI_API_KEY" \
  --env-vars "OPENAI_API_KEY=secretref:openai-api-key"

# Tear-down (cost discipline)
az group delete --name maya-rg --yes
```

```bash
# Neon Postgres — pooled endpoint app ke liye, direct endpoint migrations ke liye
psql "$DIRECT_BRANCH_URL" -f schema.sql
```

## References (Chunay Hue)

- **OpenAI Agents SDK (Python):** `openai-agents>=0.17,<0.18`; `openai.github.io/openai-agents-python`
- **FastAPI:** `fastapi.tiangolo.com`
- **Azure Container Apps:** `learn.microsoft.com/en-us/azure/container-apps/`
- **Neon Postgres:** `neon.com`
- **Cloudflare R2:** `developers.cloudflare.com/r2/`
- **E2B:** `e2b.dev` (free Hobby tier)
- **OpenTelemetry:** `opentelemetry.io`
- **OWASP API Security Top 10:** `owasp.org/API-Security/editions/2023/en/0x11-t10/`

---

*"Yeh course manufacturing track ne jo banaya usay ship karta hai — harness, sandbox, observability,
aur eval suite composed."*

---
[⬅ The Deployment Lab](05-the-lab.md) · [⬆ Index](README.md)
