# P3-FDEAGA — Night-Before One-Pager

*Exam raat sirf yeh parho. 100 MCQ / 140 min / 70% pass. Do-pass method, absolute options se
hoshiyar, layer-sawal pehle poocho.*

---

## M1 — Roles We Are Training For

- **Harari:** 10 saal ka job market pata nahi → syntax mat sikhao, **judgment + specification +
  deployment** sikhao.
- **Kaam 3 hisse:** Intent (human/Outcome Architect) · Execution (**AI Worker**) · Verification (human).
- **3 levels:** person → unit (AI Worker / Digital FTE) → enterprise (AI-Native Company).
- **Core pipeline:** Outcome Architect (what) → Digital FTE Builder (build) → AI-Native Company
  Architect (system) → Cloud AI Engineer (run).
- **FDE** = wahi pipeline **client ke andar**, vendor-neutral. "Batata hai tum **kahan** kaam karte ho."
  Hire kar lo → **AI-Native Company Architect**. Anthropic isay **"Applied AI Engineer"** kehta hai.
- **Bai 2×2:** sirf **technical product + non-technical buyer** ko FDE chahiye. Agentic turn ne har
  vendor ko us cell mein dhakela.
- **MIT NANDA 2025:** ~**95%** enterprise AI pilots ka koi measurable return nahi (**integration**,
  AI nahi). Outside partners ~67% deploy vs in-house ~33%.
- **2 Systems of Record FDE carry karta hai:** (1) **method** (yeh book, diya gaya, identical) (2)
  **profession/vertical SoR** (khud banaya, ek vertical + jurisdiction). **Build first, sell second.**
- **Palantir "Deltas" (early 2010s)** · postings **+729%** · median **~$190K** · koi sales quota nahi.
- Baaki roles: **SME as Skill Author** (SKILL.md) · **Connector & Plugin Engineer** (dono ke neeche
  **MCP server**) · Evals Engineer · AI Governance Officer (rules kya hon) · Digital FTE Supervisor
  (audit trail par naam).
- Book **rukti hai:** foundation-model pre-training, runtime-building, general data engineering.

## M2 — Agent Factory Ecosystem

- **SoR** = official version ki ek jagah (ledger jeetta hai). Book ne knowledge par lagaya, **agents
  first-class reader**.
- Bare AI chat as teacher **4 failures:** answers badalte · koi start/end · koi learner record · koi
  method.
- **Ladder 4 rungs:** URL paste → SoR connector (grounded, par **content ≠ teaching**) → **Zia Tutor
  AI** (SoR + teacher, 4 records: Knowledge/Identity/Learner/Profile) → Zia Developer AI.
- **Wiring:** audiences → **thin gateways** → component packages (content/learning/pedagogy/builder) →
  **one Git + one Postgres**. Naya product = ek aur thin gateway; **source kabhi nahi badalta**.
- **Vertical equation:** Agent Factory SoR + Vertical SoR = complete governed knowledge.
- **80/20** = product divide (shared core + customization; 20% FDE deliver karta) · **10-80-10** = ek
  task divide (intent/execute/judgment). **Nest karte hain.**
- **FDE AF Model 5 layers:** 0 Foundation (MCP/Markdown/pgvector/Better Auth) · 1 SoR kernel · 2
  Teaching+dev (Zia Tutor + Zia Developer, generic) · 3 Vertical ecosystems (**domain trio**: SoR +
  expert twin + builder) · 4 Customer instances. **Panaversity 0–2 chalata hai.**
- **SoR 3 scopes:** machinery / kernel / instance. **Domain knowledge 3 forms:** corpus (find + cite)
  / map (always available, rules) / reflexes (load + follow).
- **The One Law:** jo ek layer par repeat ho usay **neeche wale layer mein promotion ke liye
  evaluate** karo. Repetition **review** shuru karti, automatic promotion nahi (6 conditions).
  Clean-room + opt-in + rewarded.
- **4 business rules:** never lock in · **proof replaces the pitch** (deployment = sales motion) ·
  carry your own suitcase · select vertical then go deep.
- **Layer 4 order:** expert → thin slice → sponsor → baseline → **contract of success** (baseline +
  target + acceptance criteria) → engagement → thicker SoR. **Proof in production:** KPI + adoption +
  agent evals.

## M3 — Local AI and Agentic Coding

- **Agent = harness + swappable brain. Harness kabhi nahi badalta — sirf address.**
- **3 tiers:** Ollama `localhost:11434` (1 laptop, free) · vLLM `localhost:8000` (50 concurrent, GPU) ·
  OpenRouter `openrouter.ai/api` (frontier, per-token).
- **2 walls:** capability (**strong model**, hardware se nahi) vs throughput (**GPU**, model se nahi).
- Ollama default context **4,096** (`num_ctx` barhao). vLLM: `--enable-auto-tool-choice`. Cloud: 3
  sawal — data bahar? mid-size reach? frontier chahiye?
- Inference engine (vLLM) ≠ gateway (LiteLLM — identity, budgets, records).
- **Agentic coding = context engineering** (model kya dekhe). **Karpathy:** ghost / jagged / trust =
  verifiable → **verification loop** (Attempt→Check→Fix→Repeat, no human).
- Plan mode 10min+ · strong-plan/cheap-execute · rules file: har line "agar hata doon kya AI galti
  karega?" · MCP: "standing connection ke qabil?" · hook **khud paste karo**.

## M4 — Loop Engineering

- **Loop vs Harness:** Loop = kab chalta + kya yaad. Harness = ek beat ke andar.
- **6 parts:** heartbeat · worktree · skill · subagents (**maker ≠ checker**) · connector (act) ·
  **spine — no spine, no loop** (pehla step hamesha repeat).
- **4 heartbeats:** in-session (session band = mar gaya) / conditional (checker) / scheduled (cloud) /
  event-driven.
- **3 stops:** success condition (**command-provable**) + limit + no-progress check.
- **`/goal` checker** sirf transcript parhta hai, commands nahi chala sakta → `show me both`.
- **In / On / Out:** in = approve each · **on = system runs, you watch + can stop** (loop eng) · out =
  failure mode (drift se banta hai).
- **Cost = frequency** (5/din ~$20/mo vs har-5-min ~$1,800/mo). Strong-plan/cheap-execute + low
  frequency + good spine.
- **Intent + accountability hamesha insaan ke.** Routine: `claude/` branches, daily cap.

## M5 — Harness Engineering

- **Agent = Model + Harness.** 4 parts: agent loop / tool interface / context mgmt / control.
- **5 verbs:** **Constrain · Inform · Verify · Correct · Escalate.**
- **Guardrail hamesha harness mein, prompt mein kabhi nahi.** (road sign puchta, barrier rokta)
- Allow/Ask/Deny — **blast radius se sort, frequency se nahi**. **Deny > Ask > Allow.** Deny = text
  match not meaning (tripwire); sandbox = asli deewar.
- **4 fences:** worktree / filesystem / network / branch. **Tool poisoning** = attack tool ki
  description mein → version-pinned MCP allowlist.
- **Hook = "refuse"** (model skip nahi kar sakta). `PostToolUse` undo nahi karta — error agent ke
  agle turn mein.
- **Typed output:** har field allowed values ke against validate — warna **escalate** (not retry, not
  guess).
- **Correct = recovery (fast) + ratchet (slow).** Hashimoto: "ghalti ko namumkin bana do."
- **4 failure classes → 4 verbs:** Context→Inform · Constraint→Constrain · Verification→Verify ·
  Planning→Structure(loop). **Resume not restart.**
- **3 limits:** capability-vs-control · harness coupling (contracts not behaviors) · rule debt
  (monthly review; secrets exempt).

## M6 — Trusting the Checker (Evals)

- **Test** = ek property verify. **Eval** = repeated runs par behavior estimate (**pass rate**). Ek
  green agent run agli ke baare mein kuch nahi batati. **"Demo mein chala" = sabse kamzor evidence.**
- **3 depths:** answer / actions (**deleted-test yahan** — diff) / trace. Rationale = kya kiya, not
  kya socha.
- **Judge bhi model hai:** leniency drift · self-preference · surface bias (costume grade) · drift
  ("ruler hili").
- **Golden set:** failures pehle (reachable) · **categories not volume** (20–40) · version-control.
- **Rubric** = anchored examples + **fact questions**. **Bar = decision** (false-green: "sab, hamesha").
- **Grade the grader:** sabse zaroori cell = **false pass**. Disagree → **rubric pehle fix**, model
  baad mein.
- **Har system change → regression suite re-run.** Baseline sirf **neeche** written approval se.
- **Drift** = niche model update → scheduled measurement.
- **Goodhart:** measure = target → achha measure nahi. **Hold-outs** + production refresh + hide
  answer key.
- **Evals known territory par strong, unknown par khamosh — human gate NAHI hataate.**

## M7 — Leaving the Laptop (Runtime)

- Aakhri SPOF = **tumhara hardware.** Sort-sawal: **kaun control plane operate karta, kahan execution
  plane.**
- **4 homes:** 1 session (build + prove) · 2 cloud schedule (**sirf clock**, biggest payoff) · 3
  managed runtime (definition hand over; ~**8c/active-hr** + tokens; custody + visibility +
  portability dena parta) · 4 apna process (SDK, Mode 2).
- **Headless** = agent as command (already crossed in evals). **Green run status ≠ task succeeded.**
- **Unattended kit (6):** idempotency · missed-run detection · concurrency lock · credential
  discipline (never personal login) · time semantics · cost/execution limits.
- **Escalation channel TUM tak, desk tak nahi.**
- **Suitcase:** travel karta = spec/rubric/golden set/bars (decisions). NOT flags/paths/API code.
  Trust **re-earn** hoti hai (arrival protocol: poora set pehle, category se parho, bars hold,
  probation).
- **4 sawal per loop:** user kaun (tum → ghar 2 kaafi) · kya own karna zaroori · koi wait karta ·
  buri raat ki keemat (**speed limit, not destination**). **Healthy = 2–3 homes.**
- **Lock-in ek RATE** (leak) → **repo truth rakhta hai**. Ghar **kitna acha** nahi badalta.
- Aakhri unit = specified + guarded + measured + housed = **Digital FTE**.

## M8 — General Agents on the Web

- **Test:** "type karna band → kaam ruk jayega?" chat = haan, **agent surface = nahi** (delegated not
  synchronous).
- **Tab = window, not runtime** (kaam vendor servers par). Phone se = **wahi session**.
- **6 shared parts:** heartbeat · connectors · run-until-done loop · state spine · human gate · body.
  **Shape ek dafa seekho.**
- **3 file tiers:** task fs (**already lost**) / platform storage (**safe but hostage**) / **the exit
  (yours)**. **"Finished work exits the platform. Everything else may stay."**
- Connectors on web = reach **+ exit door**. **Read scope ≠ send scope.**
- Gate ab **phone par** — "doorbell ko move hona pada." Ek dafa test karo.
- **Delegation loop:** brief → **plan (tumhara akela intercept)** → approve (scope/order/reach/
  assumptions) → review.
- **Scheduled tasks 4 jawab** — brief gairhaziri survive kare. **Reporting OK; acting = Loop
  Engineering.** "Around 8am" = stagger.
- **Regulated data (PHI/privileged/financial): koi web surface nahi** jab tak compliance likhit.
- **Open path:** companies spine bech dete hain; open path tumhe banana parta hai (custody + choice).

---

## 10 Cross-Module Traps (yeh ratо)

1. **Loop = kab/kya-yaad; Harness = ek-beat-ke-andar.** Missing heartbeat ≠ missing deny-rule.
2. **Test = ek property; Eval = repeated runs (pass rate).**
3. **Guardrail harness mein, prompt mein kabhi nahi.**
4. **No spine, no loop.**
5. **Green run / PASS / demo = claim, not proof.** Human gate kabhi nahi hata.
6. **Permission buckets = blast radius se sort, frequency se nahi. Deny > Ask > Allow.**
7. **4 failure classes → 4 verbs** (Context→Inform, Constraint→Constrain, Verification→Verify,
   Planning→Structure).
8. **Finished work exits the platform** (Tier 3). Baaki sab reh sakta hai.
9. **Control plane vs execution plane** — runtime ka sort-sawal.
10. **Suitcase:** decisions travel karte hain (spec, rubric, bars); mechanics nahi (flags, paths, API).

---
[⬅ P3-FDEAGA Index](README.md) · [Full Mock ➡](quiz.md)
