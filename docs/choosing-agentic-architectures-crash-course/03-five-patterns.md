# 03 — Part 3: The Five Patterns In Depth (Concepts 9-13)

Har pattern ke liye: pattern kya hai, characteristic implementation shape (SDK primitives), deployment
topology, aur eval signals jo bataye pattern misapplied hai. **Cost discipline:** sequential workflow
sandbox aur bridge-Worker tier poori tarah skip karta hai; multi-agent sabse zyada infrastructure
expansion maangta hai — yehi decision tree ki cost discipline visible hoti hai.

## Concept 9 — Sequential Workflow

**Kya hai:** fixed pipeline jahan har step ka output agle ko feed hota hai. Path known aur stable
(Q1=yes, Q2=yes). LLM calls sirf un steps ke liye jo genuinely interpretation/generation maangte hain.

**SDK shape:** 2 narrow `Agent` instances, har ek ek LLM-only job (extraction `output_type=Invoice`,
notification writing `output_type=NotificationMessage`), koi tools/handoffs nahi. `Runner.run()` har
LLM-step ke liye alag call hota hai; baaki plain Python (validate, store — koi LLM nahi). **Insight:**
har `Agent` "agentic" nahi hoti — `output_type=` wali bina-tools `Agent` sirf typed LLM call hai.

**Deployment:** sabse chota cloud stack subset. FastAPI on ACA (yes), Neon (yes, idempotency ke liye),
R2 (maybe, files ho to), **Sandbox aur bridge Worker — nahi.** Sequential workflows agent-generated
code nahi chalate.

**Eval signals:** extraction misreads (output schema validation fail, DeepEval), validation logic gap
(production case slip through), notification off-tone/wrong (Phoenix inline eval), workflow un-designed
case handle kare (DeepEval edge-case suite). **Key insight:** step-level correctness test karo, agent
reasoning quality nahi — path fixed hai.

**Operational envelope:** Inngest ka sabse direct fit. Har workflow step = 1 `ctx.step.run` call. 5-step
invoice intake = 5 `step.run` calls. Step 3 par crash ho to steps 1-2 memoized return hote hain.
**Sequential workflow + Inngest curriculum ka simplest production-ready deployment hai** — kai
"agentic systems" mistake se Inngest functions honi chahiye thi with `step.run` checkpoints.

## Concept 10 — Single Agent + ReAct + Tools

**Kya hai:** agent reason karta hai apni current state par, action leta hai (tool call), result observe
karta hai, repeat karta hai. Path unknown (Q1=no), structure articulable nahi (Q3=no).

**SDK shape:** ek `Agent` multiple `@function_tool`s ke sath (`lookup_account`, `lookup_transactions`,
`issue_refund`, `escalate_to_human`), `Runner.run(agent, input, max_turns=25)` se call hota hai. SDK
reason-act-observe loop internally chalati hai — hand-rolled loop nahi likhte. `max_turns` step budget
hai; hit hone par `MaxTurnsExceeded` raise hoti hai. **Yeh exactly Maya ke Tier-1 Support agent ka
pattern hai.**

**Deployment:** poora cloud stack: harness (yes), Neon (critical — reasoning trace primary debugging
artifact hai), R2 (agent files handle kare to), **Sandbox + bridge Worker (yes agar code-executing
tools hon)**, background worker pattern (yes, ReAct loops 30+ seconds le sakti hain).

**Eval signals:** agent loops/solved work revisit kare (trace-length anomaly, Phoenix flag),
nonexistent tools invoke kare (SDK tool-call validation, DeepEval), premature termination (kam steps
mein hi give up), reasoning actions se diverge kare (Phoenix tool-correctness evaluator), tool latency
cascade (OTel timing). **Key insight:** ReAct evals ko reasoning trace capture karna zaroori hai, sirf
input/output nahi. **Step budgets kabhi infinity default mat karo** — 25 reasonable default hai.

**Operational envelope:** 1 `step.run` poore agent loop ke liye standard hai (SDK internally loop
chalati hai — Inngest ke liye yeh ek durable step hai). Escalation tool `step.wait_for_event` se HITL
implement karta hai. `concurrency=[Concurrency(limit=10, key="customer_id")]` ek customer ke burst se
doosron ko starve hone se bachata hai.

## Concept 11 — Planning + ReAct Execution

**Kya hai:** 2-layer pattern: planning agent explicit plan produce karta hai (stages + dependencies)
execution shuru hone se pehle; ReAct + tools har stage ke andar kaam handle karta hai. Path step-level
unknown (Q1=no) lekin structure stage-level articulable (Q3=yes).

**SDK shape:** planner `Agent(output_type=Plan)` bina tools ke, structured `Plan` (stages list, har
stage: id, description, role, dependencies, step_budget) produce karta hai. Har stage matching
specialist `Agent` se `Runner.run()` hota hai. Plan Neon ke `runs` table mein persist hoti hai.
**Insight:** structured-output `Agent` + tool-using `Agent` planning+ReAct ke 2 halves hain.

**Deployment:** ReAct wali sab requirements + plan persistence Neon mein (`plan_id`, content, stage-
by-stage progress). 5-10 minute end-to-end runs normal hain — background worker mandatory.

**Eval signals:** plan-execution divergence (planned vs actual stages compare karo), missing stages
(golden-dataset plans se compare), stage handoffs context lose karein (stage N stage M ka critical
output reference na kar sake), plan over-detailed (har stage 1-2 ReAct steps mein khatam), plan
under-detailed (ek stage 50+ ReAct steps chale). **Key insight:** plan quality ko execution quality se
alag measure karo — inhe conflate karna false diagnoses deta hai.

**Operational envelope:** har stage = 1 `step.run`. 6-stage run jo stage 4 par crash ho, stages 1-3
memoized rehte hain, sirf stage 4 retry. **Savings sabse bare kisi bhi pattern mein.** GPT-5-class
pricing par crashed run $0.50-$2.00 waste kar sakti hai — 1000 runs/din, 1-5% crash rate par $150-
$1000/month bachte hain.

## Concept 12 — Single Agent + Reflection (Additive Layer)

**Kya hai:** kisi bhi core pattern ke upar layer — output produce hone ke baad, critique pass explicit
criteria ke against evaluate karta hai; defects mile to agent refine/regenerate karta hai. Q4 (quality >
speed AND checkable criteria) se justify hoti hai.

**SDK ki 2 flavors:**
1. **`output_guardrail`** (validation-style, lightweight) — critic `Agent` (alag `model=`, blind-spot
   overlap avoid karne ke liye) `Runner.run()` hoti hai; `GuardrailFunctionOutput` tripwire fire karti
   hai agar unsafe ho. `OutputGuardrailTripwireTriggered` raise hoti hai
2. **Separate critic-and-refiner loop** (refinement-style) — generator output deta hai, critic critique
   deta hai, agar issues hon to generator refine karta hai, `max_refinements` tak

**Insight:** reflection SDK mein alag primitive nahi hai — yeh `Agent` + `Agent` ki composition hai;
`output_guardrail` sirf ek convention hai doosre agent ko output path mein wire karne ki.

**Deployment:** core pattern par depend karta hai — sequential/ReAct/planning mein 1-2 extra LLM calls
add hoti hain. **Naya consideration: model variety.** Critic agar alag model use kare (Claude critiquing
GPT ya vice versa), harness ko multi-provider support chahiye.

**Eval signals:** reflection output change na kare (rubber-stamping — pre/post outputs >80% identical
hon), refinement wrong direction mein kare (golden dataset ke against net-negative), critic-generator
same blind spots share karein (A/B test alag critics ke sath), criteria drift, refinement loops budget
exceed karein. **Key insight:** measure karo reflection net-positive hai ya nahi, sirf chalti hai ya
nahi nahi — rubber-stamp failure detect karna sabse mushkil hai.

**Operational envelope:** 3-4 `step.run` calls per run (generate, critique, 0-2 refine). Generator step
succeed ho aur critic transiently fail ho to sirf critic retry karta hai — generator output memoized
rehta hai. **HITL reflection:** subjective criteria ke liye, `step.wait_for_event` se human review
clean tarike se implement hoti hai.

## Concept 13 — Multi-Agent Specialist System

**Kya hai:** multiple agents distinct roles ke sath collaborate karte hain. Q5 se justify hoti hai:
specialization, context, ya scale real bottleneck banaye. **Multi-agent doosre patterns ka replacement
nahi, unki composition hai** — har specialist ka internal architecture sequential/ReAct/planning ho
sakta hai.

**3 SDK-native topologies:**
1. **Coordinator + specialists as tools** (`Agent.as_tool()`) — coordinator control mein rehta hai,
   specialists function tools ki tarah invoke hote hain
2. **Sequential handoff** (`handoff()`) — specialists conversation le lete hain, SDK context thread
   karta hai (researcher → writer → reviewer)
3. **Parallel specialists + synthesizer** — har specialist `asyncio.gather()` se independently
   `Runner.run()` hota hai, synthesizer outputs compose karta hai

**Deployment:** poora stack + critical additions: per-specialist runs/traces Neon mein (`parent_run_id`,
`agent_role`), routing audit logs (har routing decision log — multi-agent failures usually wrong-
routing ya lost-context-on-handoff), per-specialist cost tracking.

**Eval signals — 3 separate scoreboards zaroori:**
| Layer | Kya Catch Hota Hai |
| --- | --- |
| Specialist quality | Standard per-agent eval, har specialist standalone agent ki tarah |
| Routing accuracy | Coordinator sahi specialist chunta hai? Labeled routing examples chahiye |
| Integration quality | Specialists individually pass, end-to-end fail — integration problem hai |

Specialists disagree bina resolution ke (inconsistency detector), coordination overhead work value se
zyada ho (cost-per-correct-output — multi-agent 3x se zyada cost kare aur quality improvement <20% ho
to architecture apna overhead nahi kama raha).

**Key insight:** 95% specialist quality × 90% routing accuracy × 80% integration quality = **~68%
end-to-end** — bina separation ke pata nahi chalta kaunsi layer improve karni hai.

**Operational envelope (sabse extensive composition):** fan-out trigger pattern (coordinator N
specialist events fire karta hai, har ek independent parallel function), `step.run` per specialist (N
guna multiplied), per-key concurrency caps (`limit=5, key=tenant_id`), priority expressions (tier-based
fairness), `step.wait_for_event` specialists ke darmiyan (human-vetted handoffs), replay (3/5
specialists fail, 2 succeed → fix karo, replay karo, 2 successful memoized rehte hain).

**Quantified savings:** Inngest ke bina, custom routing/dispatch layer (~500-2000 lines), retry/dead-
letter handler (~200-1000), HITL approval queue (~500-1500), rate limiting (~300-800), replay tooling
(~500-2000) — **total 2,000-7,000 lines** jo test/debug/maintain karni parti hain. Inngest ke sath,
~50-200 lines trigger declarations + `step.run` calls.

---
[⬅ Decision Tree](02-decision-tree.md) · [⬆ Index](README.md) · [Agla: Failure Signals ➡](04-failure-signals.md)
