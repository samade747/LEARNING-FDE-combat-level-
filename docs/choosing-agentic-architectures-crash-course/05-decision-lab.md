# 05 — Part 5: The Decision Lab (5 Decisions)

5 real tasks par decision tree walk karte hain. Har Decision: task, 5 sawal answered, resulting
pattern, deployment topology sketch, eval signals. **Point sahi jawab nahi hai; discipline apply hote
dekhna hai.**

## Decision 1 — Maya Ka Tier-1 Support Agent

**Task:** customer-support agent incoming queries handle karta hai — account/transaction/policy lookup,
knowledge base search, refunds authority limits ke andar, ambiguous cases escalate.

**Tree walk:** Q1 (path known?) **No** — queries bohat vary karti hain. Q3 (structure articulable?)
**No** — koi clear "stages" nahi, investigation jo complete hone tak chalti hai. Q4 (quality>speed?)
**Mixed, criteria checkable nahi** — reflection fit nahi karti. Q5 (bottleneck?) **Borderline, lekin
single agent sahi call hai** — categories overlap zyada hain, specialist routing zyada handoff friction
create karega.

**Pattern: Single Agent + ReAct + Tools** (Concept 10).

**Deployment:** poora stack — FastAPI on ACA, Neon (sessions/runs/traces), R2, Cloudflare Sandbox via
bridge Worker (`apply_patch` tool), background worker.

**Eval signals:** trace-length anomalies, tool-call duplication, reasoning-action divergence, premature
termination, step-budget exhaustion. **Sabse likely failure:** ambiguous refund cases par loop karega —
fix: explicit stop conditions ("3 lookups mein decide na kar sako to escalate karo").

**Operational envelope:** `TriggerEvent("customer/email.received")`, 1 `step.run` poore agent loop ke
liye, `escalate_to_human` tool `step.wait_for_event` se HITL (4-hour timeout), concurrency `limit=10
per customer_id, limit=50 global`.

## Decision 2 — Incident Response Agent

**Task:** on-call agent alerts receive karta hai, initial response chalata hai — service health check,
deploy correlation, root cause, remediation runbook, human escalation agar novel/severe ho.

**Tree walk:** Q1 **Partially** — standard structure hai lekin specific path input par depend karta
hai. Q3 (structure articulable?) **Yes** — triage → diagnose → remediate → report clear stages hain.
Q4 (quality>speed?) **Dono matter karte hain** — remediation steps par reflection justified hai ("yeh
remediation safe hai? symptoms se match karta hai?"). Q5 **No** — ek agent monitoring/deploy history/
runbook/remediation tools access ke sath kaafi hai.

**Pattern: Planning + ReAct Execution, Remediation Par Reflection Ke Sath** (Concepts 11 + 12).

**Deployment:** ReAct deployment + plan persistence. Naya Neon table: `incidents` (incident_id,
severity, plan, current_stage, remediation_history). Reflection separate agent (alag model
recommended). Background worker mandatory (5-15 min runs).

**Eval signals:** plan-execution divergence, reflection effectiveness (unsafe remediations pakri
gayi?), time-to-resolution, escalation accuracy. **Sabse likely failure:** planner simple incidents ke
liye over-detailed plans banata hai — fix: appropriate plan granularity ke examples se train karo.

**Operational envelope:** dual triggers (`TriggerCron` proactive health checks + `TriggerEvent`
reactive), per-stage `step.run`, remediation par HITL (`step.wait_for_event`, 15-min timeout — tight
kyunki incidents time-sensitive), replay bug-fix recovery ke liye.

## Decision 3 — Market Research Agent

**Task:** topic + research brief diye jane par report produce karta hai — sources identify, databases
search, documents extract/compare, findings draft, final report.

**Tree walk:** Q1 **No** — sources/competitors/analyses discover hote hain. Q3 **Yes** — gather →
analyze → synthesize → draft → review standard shape hai. Q4 **Yes, strongly** — decision-makers
parhte hain, criteria partially checkable ("sab claims sourced hain", "har competitor cover hua").
Q5 **Likely yes for context** — depth research bara source material load karta hai, ek agent ke context
mein reasoning degrade hoti hai.

**Pattern: Multi-Agent Specialist System, Top Layer Planning Ke Sath, ReAct Research Specialists Ke
Andar, Reflection Final Synthesis Par** (Concepts 11, 13, 12 ki composition).

**Self-check jo framework maangta hai:** senior engineer ka likely objection: *"Aap multi-agent par
jump kiye. Context windows ab bare hain, ek agent planning+reflection ke sath kyun nahi?"* Honest
jawab: single agent raw material hold **kar sakta hai**, lekin depth research degrade hoti hai jab ek
context raw sources + extraction notes + comparison + draft prose sab ek sath mix karta hai. Split
**context bottleneck** (Q5) se justify hoti hai, multi-agent thorough lagne se nahi.

**Deployment:** poora stack + multi-agent additions — parent-run + per-specialist run structure Neon
mein, routing audit logs, per-specialist cost tracking, shared Neon table jahan specialists summaries
deposit karein.

**Eval signals:** 3 scoreboards (per-specialist quality, routing accuracy, integration quality),
top-level plan-execution divergence, synthesis reflection effectiveness, cost-per-correct-output.
**Sabse likely failure:** specialists excellent individual briefs dete hain jo aggregator inconsistent
formats ki wajah se synthesize nahi kar pata — fix: structured handoff formats (Pydantic schemas)
enforce karo.

**Operational envelope (premier fan-out example):** coordinator N specialist events fire karta hai (1
per competitor), per-tenant concurrency cap (`limit=5`), har specialist ka apna `step.run`, aggregation
separate function ki tarah (events se decoupled), per-specialist cost visibility dashboard mein.

## Decision 4 — Enterprise Onboarding Agent

**Task:** naya enterprise customer sign up kare to tenant provision karo, seed data populate, admins
invite, kickoff schedule, welcome materials bhejo.

**Tree walk:** Q1 **Yes** — fixed sequence: provision → configure → seed → invite → schedule → send-
welcome, har baar isi order mein. Q2 **Yes** — har enterprise customer isi workflow se guzarta hai,
stable. **Q3-Q5 N/A — tree Q2 par terminate hoti hai.**

**Pattern: Sequential Workflow** (Concept 9).

**Deployment:** **minimal** cloud stack — FastAPI on ACA, Neon (onboarding state), R2 (welcome PDFs),
LLM calls sirf personalization steps par. **No sandbox, no bridge Worker, no background-worker pattern
long-running reasoning ke liye.** Yeh substantially sasta deployment hai.

**Eval signals:** step-level correctness, workflow completion rate, personalization quality (Phoenix
tone/factual accuracy), workflow steps galat inputs par apply hon (validation gaps). **Sabse likely
failure:** edge-case enterprise standard workflow mein fit nahi hota — fix: explicit branching add karo
(edge cases kam hon), ya ReAct par upgrade consider karo (edge cases proliferate karein).

**Operational envelope (cleanest example):** `TriggerEvent("customer/enterprise.signed_up")`, 6
`step.run` calls (provision, configure, seed, invite, schedule, welcome), **koi HITL nahi**,
`step.sleep` delayed follow-ups ke liye, cron pairing stalled onboardings sweep karne ke liye.

> **Yeh Decision negative example hai agentic patterns ke liye.** Task ko agentic reasoning chahiye
> hi nahi. Embedded LLM calls wala workflow sasta, reliable, debug karna asaan hai. Jahan workflow kaam
> kare wahan ReAct mat pakro — yeh sabse important discipline hai jo decision tree sikhati hai.

## Decision 5 — Coding Agent (Advanced Track)

**Task:** feature request diye jane par working implementation produce karta hai — codebase parhna,
change design karna, code likhna, tests likhna/chalana, failures fix karna, PR produce karna.

**Tree walk:** Q1 **No** — continuous discovery. Q3 **Partially** — clear high-level shape hai
(understand → design → implement → test → fix → PR) lekin design phase iterate kar sakta hai. Q4 **Yes,
very** — tests/type checks/linter checkable criteria hain. Q5 **Genuinely yes, dono specialization aur
context** — code generation, security review, documentation 3 distinct skill sets hain.

**Pattern: Multi-Agent Specialist System, Top Layer Planning, ReAct + Tools Specialists Ke Andar,
Explicit Reflection Coder Ke Output Par** (sab 4 doosre patterns ki composition — sabse hard case).

**Deployment:** poora stack + multi-agent extensions — coordinator (plan: design/code/review/document),
coder specialist (heavy sandbox use, bridge Worker mandatory), reviewer specialist (lighter sandbox),
documentation specialist (simpler, sequential ho sakta hai), reflection final PR par.

**Eval signals:** code-correctness (tests pass?), security-review effectiveness (vulnerabilities pakri
gayi? false-positive rate bhi), plan-execution divergence, cost-per-PR. **Sabse likely failure:**
reviewer specialist bottleneck ban jata hai (bohat strict ya bohat permissive) — fix: explicit criteria
+ separate eval jo reviewer ke judgments human reviewer se compare kare.

**Operational envelope (har primitive use karta hai):** `TriggerEvent` (GitHub issue assign) ya Slack
command, fan-out coordination (coding/specialist.code, .review, .docs events), per-file `step.run`
(multi-file edit crash par completed edits lose na hon), PR merge par `step.wait_for_event` (2-day
timeout), per-tenant concurrency (`limit=2` — coding expensive hai), priority tier-based fairness ke
liye, replay fixable rejections ke liye, `step.sleep` post-merge safety window ke liye (2-hour CI
stability check).

## Aapka Turn: 6wan Decision, Koi Answer Key Nahi

Apne kaam se ek real task lo. **Task ek sentence mein likho.** 5 sawal walk karo, har ek ka jawab
commit karo:
- Q1: solution path known hai? (Test: "bina LLM ke plain function ki tarah likh sakte ho?")
- Q2 (agar Q1 yes): fixed aur stable hai?
- Q3 (agar Q1 no): structure articulable hai?
- Q4: quality>speed checkable criteria ke sath?
- Q5: specialization/context/scale bottleneck naam le sakte ho aur measure kar sakte ho?

**Phir objection predict karo.** Senior engineer kya push back karega? Likho, aur apni choice defend
karo ya simplify karo. Predict/answer nahi kar sakte to abhi principled choice nahi ki.

---
[⬅ Failure Signals](04-failure-signals.md) · [⬆ Index](README.md) · [Agla: Honest Frontiers Aur Closing ➡](06-honest-frontiers-and-closing.md)
