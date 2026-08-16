# 05 — Part 4: The Lab — Decisions 4-7

## Decision 4 — Tool-Use Aur Safety Evals (Claudia Ka Envelope Check)

*Ek line mein: tool-use correctness aur envelope-respect evals likho Claudia ke signed-delegation
decisions ke liye; verify karo envelope check violations pakarti hai.*

Course 8 ka envelope check (Claudia apne delegated envelope ke andar rehti hai?) Course 9 ki vocabulary
mein ek **safety eval** hai. **Claudia ki eval suite envelope violations ko production tak pahunchne
se pehle pakarti hai** — bilkul jaise Paperclip ka runtime check execution time par pakarta hai.

**Requirements:**
1. Approval requests ka dataset banao (`claudia-delegation.json`) — refunds ceiling ke neeche, ceiling
   par (edge case), ceiling ke upar (surface hona chahiye), envelope-extension hires, terminations —
   40 examples minimum
2. **Tool-use correctness metric** — Claudia ne kaunse tools call kiye (polling, instruction
   retrieval, signing, posting)? Expected sequence se compare
3. **Envelope-respect safety eval** — custom `EnvelopeRespectMetric`: request + decision + envelope
   JSON leke pass/fail deta hai — **yehi eval envelope violations ko ship hone se pehle pakarta hai**
4. **Confidence-vs-action consistency check** — low-confidence decisions surface honi chahiye,
   autonomously approve nahi
5. Audit-trail consistency verify karo — `activity_log` aur `governance_ledger` dono rows exist aur
   consistent hon
6. CI integration — safety evals critical metrics hain, koi exception nahi
7. **Red-team set:** 8-10 adversarial examples, kam az kam 3 genuinely envelope violations inject
   karein — prompt-injection, social-engineering framing, type-misclassification bait, multi-turn
   drift, history-vs-rule conflict. **Agar model 100% red-team set pass kare, set bohat asaan hai.**

## Decision 5 — RAG Evals: Ragas Par TutorClaw

*Ek line mein: TutorClaw introduce karo (knowledge-agent jo Agent Factory book se retrieve karke jawab
deta hai); Ragas ke 5 metrics setup karo; knowledge-agent golden dataset par chalao.*

Lab ka ekaltha naya agent: **TutorClaw**. Maya ke customer-support agents primarily RAG agents nahi
hain; TutorClaw hai. Wajah: Ragas ke specialized metrics ko ek aisa agent chahiye jo unhe genuinely
exercise kare.

**Requirements:**
1. TutorClaw banao `agents/tutorclaw/` par — question receive kare, `corpus/` se chunks retrieve kare,
   grounded answer generate kare. Full-Implementation track par pgvector-on-Neon, Simulated track par
   simple local retriever
2. TutorClaw golden dataset banao (`tutorclaw-golden.json`, 30 examples): single-chapter answerable,
   cross-chapter synthesis, book-doesn't-cover ("I don't know" honest hona chahiye), subtle-difference
   grounding tests
3. 5 Ragas metrics implement karo: Context Relevance, Faithfulness, Answer Correctness, Context
   Recall, Context Precision
4. Ragas chalao dataset par, scores collect karo
5. **Diagnostic playbook:**
   - `context_recall=0` + `context_precision=0` = OOD (out-of-domain) canary — sabse reliable signal
   - `context_recall` low + `answer_correctness` low = retrieval ne key facts miss ki (fix chunking/
     top-k)
   - `context_recall` high + `faithfulness` low = agent ne invented claims di (fix grounding prompt)
   - `context_precision` low = retrieval ne noise di (fix embedding model/chunk size/reranker)
   - `answer_correctness` helpful refusals ko literal ground_truth ke against punish karta hai — OOD
     rows ke liye retrieval-side metrics ko primary gate rakho
6. CI integration
7. Diagnostic playbook document karo

## Decision 6 — Regression Evals Aur CI/CD Wiring

*Ek line mein: Decisions 2-5 ki sab eval suites ek unified CI/CD workflow mein connect karo jo har PR
par chale, baseline se compare kare, critical metrics regress hone par merges block kare.*

**Yeh Decision "hamare paas evals hain" ko "hum confidence ke sath ship karte hain" mein badalti hai.**

**Requirements:**
1. Regression check define karo — critical-metric score jo baseline se >5% (configurable) kam ho
2. Unified runner banao (`scripts/run-all-evals.sh`) — Decisions 2-5 ki suites sequence mein chalata
   hai
3. Regression comparator banao (`scripts/check-regressions.py`)
4. GitHub Actions mein wire karo, 6 stages: traditional tests → DeepEval output evals → trace evals
   (prompts/models/tools touch karne wale PRs par) → safety evals (hamesha, critical) → Ragas evals
   (knowledge agents touch karne par) → regression check
5. Baseline management — jaan-boojh kar improvement par reviewer explicit approval de
6. Eval cost budget — soft warning $5/run, hard cap $20/run
7. Merge-blocking rule — critical metric regression merge block kare; maintainer stated reason ke
   sath override kar sakta hai

## Decision 7 — Production Observability: Phoenix

*Ek line mein: Phoenix install karo, agent runtimes se OpenTelemetry traces receive karo, agent
health/cost-latency/drift summary scripts banao, trace-to-eval feedback loop setup karo.*

**Aakhri Decision loop close karti hai. Phoenix production dekhti hai, production failures future eval
examples ban jate hain, suite waqt ke sath sharper hoti jati hai.**

**Requirements:**
1. Phoenix install karo — Quick Win path: `pip install arize-phoenix`, `px.launch_app()` — UI
   `localhost:6006` par. Multi-user team workspaces ke liye Docker service
2. Trace export wire karo — OpenTelemetry exporter agent runtime se Phoenix collector tak
3. **3 health summaries compute karo:** agent health (pass rates per role/category/metric), cost aur
   latency (p50/p95, outliers), drift detection (trailing 7-day avg vs 30-day baseline, >10% drift par
   alert)
4. Trace sampling configure karo: har error trace, har user-feedback-flagged trace, random 1% normal
   traces
5. Production-to-eval pipeline banao (`scripts/promote-trace-to-eval.py`) — sampled trace → candidate
   example → human review → accept/reject
6. **Promotion ritual schedule karo** — hafte mein ek baar, pichle 7 din ke sampled traces review karo
7. Operational discipline document karo — kya sample hota hai, kya promote hota hai, kaun review karta
   hai

> **Phoenix → Braintrust migration** mechanical hai kyunki dono OpenTelemetry-compatible traces
> consume karte hain: trace dataset export karo, Braintrust workspace provision karo, dashboards port
> karo, exporters reconfigure karo, promotion pipeline port karo, 2 hafte parallel chalao, phir Phoenix
> decommission karo.

---
[⬅ The Lab — Setup Aur Decisions 1-3](04-the-lab-part1.md) · [⬆ Index](README.md) · [Agla: Honest Frontiers ➡](06-honest-frontiers.md)
