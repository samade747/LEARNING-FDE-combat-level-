# 04 — Part 4: The Lab — Setup Aur Decisions 1-3

Part 4 discipline ko concretely assemble karti hai. **7 Decisions**, har ek Claude Code ya OpenCode
session ke liye ek briefing — kabhi hath se type ya edit nahi karte. Aakhir mein Maya ki customer-
support company ke paas ek eval suite hoti hai jo output, tool-use, trace, RAG, safety, regression, aur
production observability sab cover karti hai — har layer CI/CD aur ek observability dashboard mein
wired.

> **Coding agent ki model strength par note:** har Decision 6-8-step structured brief hai jo assume
> karta hai aapka coding agent reliably plan mode mein jaega, plan file mein save karega, review ke
> liye pause karega, phir step-by-step execute karega. Yeh Claude Sonnet/Opus, GPT-5-class, Gemini 2.5
> Pro par cleanly kaam karta hai; weaker models par stochastic hota hai.

> **2 completion modes, shuru karne se pehle chuno:**
> 1. **Full implementation** — real Course 5-8 deployment par 4 eval frameworks wire karo, real traces
>    par evals chalao. Waqt: 6-10 ghante lab.
> 2. **Simulated** (default) — `maya-stub.py` (base ke sath shipped agent-under-test) plus prompts se
>    generated fixtures grade karo. Waqt: 2-3 ghante lab. Output: EDD ki poori samajh + ek working
>    local lab jo demonstrate ki ja sake.

> **3 runtime paths:** Path A — Claude Managed Agents (Maya ke Tier-1/Tier-2/Manager-Agent/Legal
> Specialist/Claudia sab yahan, lab ka primary path); Path B — OpenAI Agents SDK; Path C — doosre
> runtimes (LangChain, LlamaIndex, custom loops). Discipline transfer hoti hai, tooling adapt hoti hai.

## Lab Setup: Decision 1 Se Pehle

**Companion base** `eval-driven-development/` folder mein hai (`panaversity/agentfactory-manufacturing`
repo). Base deliberately bare hai:
- `AGENTS.md` — standing brief: 12-tool registry, golden-dataset schema, eval-tool API pins,
  per-Decision done-when
- `.mcp.json` — Neon, Context7, local `phoenix` MCP, sab keyless
- `.env.example` — OpenAI/Anthropic key ke liye (LLM-as-judge backend), lab ka ekaltha secret
- `maya-stub.py` — agent-under-test, 3 OpenTelemetry trace shapes emit karta hai (clean refund, broken
  wrong-customer refund, Claudia ki delegated-governance decision)
- `corpus/` — 5 book excerpts TutorClaw ke retrieval ke liye (Decision 5)

Base **nahi** ship karta: `evals/` suite, 50-row `golden.json`, trace fixtures, vector store, pinned
`requirements.txt` — yeh sab lab ke load-bearing exercises hain, aapka agent inhe har Decision ke
prompts se banata hai.

---

## Decision 1 — Eval Workspace Setup Aur Pehla Golden Dataset

*Ek line mein: DeepEval, Ragas, OpenAI Agent Evals client install karo; `evals/` directory scaffold
karo; agent ke sabse common task categories cover karta 50-example golden dataset banao.*

Har cheez jo neeche ati hai us dataset par depend karti hai jo asal mein agent ke production traffic
ko represent kare. **Bad dataset, bad evals** — frameworks kitne bhi ache hon. **Decision 1 lab ka
sabse undervalued step hai.**

**Requirements:**
1. Python dependencies pin karo: `deepeval`, `ragas`, `openai`, `pytest`, `python-dotenv`
2. Project structure banao: `datasets/`, `evals/{output,tool_use,trace,rag,safety}/`, `reports/`,
   `docs/`
3. **Pehla golden dataset:** 50 examples, Tier-1 Support agent ke common task categories cover karte
   hue. Har example: `task_id`, `category`, `input`, `customer_context`, `expected_behavior`,
   `expected_tools`, `expected_response_traits`, `unacceptable_patterns`, `difficulty`
4. Distribution: ~40% refund_request, 20% account_inquiry, 15% technical_issue, 15%
   escalation_request, 10% policy_question — har category mein easy/medium/hard mix
5. Examples **realistic patterns se** source karo, imagination se nahi — Simulated track par Concept
   11 ke patterns se generate karo; Full-Implementation track par `activity_log` se sample karo
6. Dataset validate karo: sab required fields, `expected_tools` sirf valid tools reference kare, koi
   duplicate `input` nahi, category distribution ±5%
7. Dataset conventions `datasets/README.md` mein document karo — API contract ki tarah treat karo

> **Bottom line:** golden dataset woh artifact hai jispar har eval depend karti hai. **Isay skip mat
> karo interesting frameworks ki taraf jaldi jane ke liye.** Ek khoobsurat eval framework ek bure
> dataset par galat cheez ko rigor ke sath measure karta hai.

## Decision 2 — Output Evals: DeepEval Par Tier-1 Support Agent

*Ek line mein: DeepEval test suite likho output evals ke liye — answer relevancy, faithfulness,
hallucination, task-completion metrics — CI/CD mein integrate karo.*

**Requirements:**
1. DeepEval test runner banao `evals/output/test_tier1_support.py` par — pytest-style, har test
   function ek task category
2. LLM-as-judge backend configure karo (Claude Opus ya GPT-4-class) — **agent chalane wale model se
   alag rakho** (self-grading bias avoid karne ke liye)
3. 4 metrics implement karo: `AnswerRelevancyMetric(0.7)`, `FaithfulnessMetric(0.8)`,
   `HallucinationMetric(0.3)`, custom `TaskCompletionMetric`
4. Dataset loader fixture likho jo `golden.json` parhe
5. Agent ko test runner mein chalao, response aur context capture karo, sab 4 metrics assert karo
6. Baseline generate karo — `reports/baseline.md` mein commit karo
7. GitHub Actions mein wire karo — critical metric regression merge block kare
8. Critical metrics document karo `docs/critical-metrics.md` mein

**Decision 2 ke baad, har prompt/tool/model change eval suite chalati hai, aur regressions merges
block karti hain — yehi woh moment hai jab EDD concept se enforced practice ban jati hai.**

## Decision 3 — Trace Evals: OpenAI Agent Evals (Trace Grading Ke Sath)

*Ek line mein: OpenAI Agent Evals + trace grading setup karo, tool-selection, reasoning-soundness,
handoff-appropriateness rubrics chalao.*

**Decision 3 wahi jagah hai jahan Concept 3 ka wrong-customer refund CI mein catchable ban jata hai,**
audit-time par detectable hone ke bajaye.

**Requirements (11 steps, summary):**
1. Golden dataset OpenAI Files API par upload karo (JSONL, har line `{"item": {...}}` wrapped)
2. Eval aur run schema define karo (`/v1/evals`, `data_source_config.item_schema`)
3. 3 trace-level rubrics banao: `tool_selection`, `reasoning_soundness`, `handoff_appropriateness`
4. 3 output-level rubrics bhi add karo: answer correctness, format compliance, tone-appropriateness
5. Grader filters map karo, routing document karo
6. Graders configure karo (`gpt-4.1-mini`/`gpt-4o-mini`, cost ke liye; variance zyada ho to upgrade)
7. Eval chalao, scores collect karo
8. Scores aggregate karo `reports/openai-baseline.md` mein
9. CI mein wire karo — har PR par nahi, jo prompts/model/tools touch kare us par
10. Model-comparison workflow setup karo (naya model upgrade → dono par full suite → diff)
11. "Trace eval debug" workflow add karo — failing trace rubric → Trace Grading dashboard link

> **Claude Managed Agents sidebar:** Agar aapke Workers Claude Managed Agents par hain (OpenAI Agents
> SDK ki jagah), same Decision 3 outcome **Phoenix ke evaluator framework** se milta hai — same 3
> rubrics, Phoenix evaluator definitions ki tarah stored, same LLM-as-judge backend, same CI wiring
> pattern. **Sirf platform badalta hai, discipline nahi.**

---
[⬅ The Stack](03-the-stack.md) · [⬆ Index](README.md) · [Agla: The Lab — Decisions 4-7 ➡](05-the-lab-part2.md)
