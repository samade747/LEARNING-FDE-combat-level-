# 05 — Part 5: The Deployment Lab (Decisions 0-9)

Parts 1-4 ne architecture aur surfaces cover kiye. Part 5 poori cheez banata hai: **10 Decisions** jo
khaali folder se ek deployed, observable, eval-gated harness tak le jate hain. Companion download ka
`AGENTS.md` project rules, architecture, aur verified API shapes rakhta hai, isliye har brief chota
rehta hai.

> **2 tareeqe lab complete karne ke:** **Full build** (Intermediate/Advanced) — cloud par deploy karo.
> **Simulated** (Reader/Beginner) — companion code parho, kuch provision kiye bina. Harness sirf
> `OPENAI_API_KEY` ke sath locally boot hoti hai.

## Decision 0 — SDK Probe Aur Brief Reconcile Karo

*SDK install karo, installed version print karo, live sandbox docs fetch karo, companion `AGENTS.md`
ko unke against reconcile karo. **Live docs jeetein.***

SDK tezi se ship hoti hai — names, signatures, defaults releases ke darmiyan badalte hain. `AGENTS.md`
"aaj ka known-good" hai, "hamesha ka" nahi. 5 minute yahan ek ghanta bacha lete hain "yeh attribute
exist kyun nahi karta" jaisi confusion se.

**Done jab:** installed `openai-agents` version report hoti hai (0.17.x expect), koi differing names
"What changed since the brief" note mein likhe jate hain.

## Decision 1 — Harness Scaffold Karo

*FastAPI app agent, state layer, aur storage layer ke sath, jo missing key par gracefully degrade ho,
`OPENAI_API_KEY` akele par boot ho.*

**Done jab:** `uv run uvicorn maya_harness.main:app` bina error ke start ho, `GET /health` bare
`OPENAI_API_KEY`-only boot par `postgres`/`sandbox`/`r2` sab `false` report kare, `GET /docs`
auto-generated API dikhaye.

> **Quick Win:** Yeh boot poore course ka early win hai. Kisi cloud account, Docker, ya database se
> pehle, aapke paas ek real agent harness hai jo `/health` par apni laptop se jawab de rahi hai.

## Decision 2 — Harness Containerize Karo

*Chota, reproducible container image jo laptop aur cloud par same chale.*

`python:3.12-slim` + `uv` reproducible install ke liye. Dependencies cached layer mein install hoti
hain source copy hone se pehle. Port 8000 expose, `uvicorn ... --proxy-headers` (cloud TLS terminate
karti hai ingress par).

**Done jab:** image bina error build ho, container locally chale, `GET /health` `ok` de andar se,
source file change karke rebuild karna fast rahe (dependency layer cached rahe).

## Decision 3 — Azure Container Apps Par Deploy Karo

*Managed cloud runtime provision karo, image cloud mein build karo, harness deploy karo taake woh
public internet se HTTPS par jawab de.*

Resource group + container registry banao. `az acr build` se cloud mein image build karo (local Docker
nahi chahiye). Container Apps environment banao, `--ingress external`, `--target-port 8000`,
`--min-replicas 0` (scale-to-zero). `OPENAI_API_KEY` named secret ki tarah store karo, `secretref:` se
reference karo — kabhi image mein baked nahi.

**Done jab:** deploy script public `*.azurecontainerapps.io` URL print kare, phone se `/health` khole
to `ok` de, quiet spell ke baad app zero par scale ho aur agli request chand seconds mein cold-start
wake ho.

> **Aage carry karo:** Decisions 4-9 isi app par redeploy karke har backend add karte hain. `az group
> delete` mat chalao jab tak lab khatam na ho.

## Decision 4 — Neon Postgres: Durable State Wire Karo

*Serverless Postgres provision karo, harness ko point karo — sessions/runs/traces restart survive
karein.*

5-table schema (sessions, runs, traces, artifacts, audit_log), `public.*` schema-qualified. **1 rule
optional nahi hai:** running app ke liye **pooled endpoint**, migrations ke liye **direct (non-pooled)
endpoint** — pooled endpoint `search_path` silently drop karta hai, isliye har statement
schema-qualified hai. (`channel_binding=require` DSN mein hone se `asyncpg` par koi farq nahi parta —
yeh sirf tidiness ke liye trim hota hai, footgun nahi.)

**Done jab:** `/health` `"postgres": true` report kare, `POST /runs` ek row likhe jo Neon se wapis parhi
ja sake, container restart par run history rahe.

## Decision 5 — Cloudflare R2: Files Aur Artifacts Wire Karo

*Object storage provision karo, specific files ke short-lived links harness ko do — agent ke outputs
storage password share kiye bina download hon.*

Bucket + scoped API credentials banao. boto3 S3 client R2 endpoint par point karo
(`https://<account_id>.r2.cloudflarestorage.com`, `region_name="auto"`). `save_artifact=true` par
reply bucket mein likho, short expiry (1 ghanta) ke sath presigned download URL return karo.

**Done jab:** `/health` `"r2": true` de, `save_artifact` wali `POST /runs` `artifact_url` de jo reply
download kare, expiry ke baad presigned URL kaam karna band kar de.

## Decision 6 — Sandbox Execution Wire Karo

*Isolated workspace attach karo jahan agent ka code chale, harness ke secrets/database ki access ke
bina.*

**Cost note:** Cloudflare (course ka primary) ko paid Workers plan + bridge Worker chahiye. **E2B
realistic free path hai** — free Hobby tier, first-class SDK client, koi bridge nahi. Companion isi
liye E2B default karta hai.

`SandboxRunConfig` sirf tab banao jab sandbox key set ho, `RunConfig` ke through attach karo, kabhi
`Runner.run` kwarg ki tarah nahi. 2 verified shapes: `SandboxRunConfig(client=E2BSandboxClient(),
options=E2BSandboxClientOptions(sandbox_type="e2b"))` — options object required hai; Manifest
`entries={}` se banta hai, koi `base_image=`/`mounts=[]` nahi.

**Done jab:** `/health` `"sandbox": true` de (E2B key set karne ke baad), `POST /runs` `"used_sandbox":
true` de, agent bina sandbox key ke bhi jawab deta rahe.

## Decision 7 — Observability Wire Karo

*4 observability surfaces wire karo, ek shared `run_id` se jorto — team kisi bhi symptom se cause tak
pahunch sake.*

OpenTelemetry se harness instrument karo (FastAPI, asyncpg, HTTP spans), Application Insights ko
export karo. Har surface par same `run_id` tag karo: OTel parent span, structured log lines, SDK trace,
Phoenix sample. Completed SDK traces Phoenix ko fire-and-forget stream karo (Phoenix down ho to log
karo aur continue karo — Neon durable record hai). ~10% successful runs sample karo, 100% failed runs,
`run_id` par deterministic.

**Done jab:** ek request ki OTel trace ~1 minute mein Application Insights mein dikhe, ek `run_id`
search karne se doosre surfaces mein matching record mile, Phoenix recent traces dikhaye.

## Decision 8 — Eval Suite Wire Karo

*Eval-Driven Development course ke 4 frameworks harness ki traces se connect karo — CI regression
gate, nightly behavior report, weekly trace-to-eval promotion ritual.*

1. **DeepEval CI regression gate** — har PR jo agent/prompts touch kare, staging `POST /runs` hit
   karke golden dataset ke against chalao, previously-passing case fail ho to merge block karo
2. **Nightly scheduled job** (Container Apps Jobs) — pichle 24 ghante ki traces Neon se parho, OpenAI
   Agent Evals se grade karo, Ragas retrieval-using traces par, report repo mein likho, Slack summary
   post karo
3. **Phoenix inline evaluators** — traces arrive hote hi chalein (hallucination, policy, tool-
   correctness), scores tag karein, runs block na karein
4. **Weekly ritual** — Phoenix ke flagged traces review karo, eval-worthy ones golden dataset mein
   promote karo

**Done jab:** behavior worsen karne wala PR DeepEval gate se block ho, nightly job report + Slack post
kare, Phoenix inline scores dikhaye, promotion ritual documented aur ek baar end-to-end chalaya gaya ho.

## Decision 9 — Production Checklist

*Operational discipline complete karo: secrets rotation, blue/green deploys, on-call runbook, backup/
recovery, rate limits.*

1. **Secrets rotation** — naya credential purane ke sath add karo, redeploy karo, verify karo, phir
   purana revoke karo
2. **Blue/green deploys** — nayi revision 0% traffic par banao, `/health` check karo, 10% shift karke
   Application Insights dekho, phir 100% shift karo, purani revision ek din rollback ke liye rakho
3. **On-call runbook** — 5 scenarios: high error rate, high latency, sandbox provider down, Neon
   unreachable, R2 unreachable — har ek ke investigation/remediation steps
4. **Backup/recovery** — Neon point-in-time recovery, R2 versioning, ACA revision rollback
5. **Per-user rate limits** — middleware layer par, limit se upar `429` + `Retry-After`
6. **Cost alerts** — daily spend recent average se zyada upar jump kare to fire hon

**Done jab:** sab secrets ki documented/tested rotation procedure ho, ek blue/green deploy end-to-end
chale, rate limiting kaam kare (429), cost alerts configured hon.

---
[⬅ Observability Aur Evals](04-observability-and-evals.md) · [⬆ Index](README.md) · [Agla: Honest Frontiers Aur Closing ➡](06-honest-frontiers-and-closing.md)
