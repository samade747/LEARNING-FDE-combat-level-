# 03 — Part 3: The Stack (Concepts 8-10)

## Concept 8 — Trace-Eval Layer: Phoenix (Claude Runtime) Aur OpenAI Agent Evals (OpenAI Runtime)

Trace-eval layer wahi hai jahan agent ka **runtime** sabse zyada matter karta hai. Maya ke worked
example agents Claude substrate par chalte hain, isliye **Phoenix ka evaluator framework natural fit
hai:** Claude Agent SDK ki OpenTelemetry traces seedhe consume karta hai. OpenAI Agents SDK wale agents
ke liye **OpenAI Agent Evals + Trace Grading tightest fit hai:** platform, grader, traces sab ek hi
ecosystem mein.

**Ek platform, do complementary capabilities:**
- **Agent Evals (platform)** — datasets, eval runs, grading workflows, model-comparison reports handle
  karta hai
- **Trace grading (capability)** — trace-aware extension jo poora execution path parhti hai (har model
  call, tool call, handoff, guardrail check) aur assertions chalati hai

**Dono kyun, ek nahi:** Agent Evals bina trace grading ke pyramid ka neecha hissa achi tarah cover karta
hai (output evals, dataset management) lekin trace layer ke liye blind hai jahan zyada tar agentic-AI
failures rehte hain. Trace grading bina broader platform ke individual traces grade kar sakta hai
lekin scale par dataset infrastructure nahi rakhta.

**2 paths, side by side:**

| Layer | Path A — Claude Managed Agents (lab ka primary) | Path B — OpenAI Agents SDK |
| --- | --- | --- |
| Trace eval surface | Phoenix evaluator framework | OpenAI Evals API (`/v1/evals`) + Trace Grading dashboard |
| Output evals | DeepEval | DeepEval (same) |
| Tool-use evals | DeepEval | DeepEval (same) |
| RAG evals | Ragas | Ragas (same) |
| Production observability | Phoenix | Phoenix (same) |

**Architectural truth:** eval discipline runtime par depend nahi karti. Phoenix Claude Managed Agents
ke liye natural surface hai kyunki OpenTelemetry-native tracing deliberate architectural choice thi;
OpenAI Evals OpenAI-native agents ke liye tightest fit hai kyunki traces already wahan rehte hain.
**Dono equivalent eval suites produce karte hain.** Jahan aapke agents already chalte hain wahan se
chuno.

**Maya ka setup (Path A):** Tier-1, Tier-2, Manager-Agent, Legal Specialist, Claudia sab Claude Managed
Agents par. DeepEval (output/tool-use) + Phoenix (trace evals + production observability) primary
stack hai, Ragas knowledge-layer ke liye. OpenAI Agent Evals + Trace Grading equally-supported
alternative hai Path B readers ke liye.

## Concept 9 — DeepEval: Repo-Level Eval Framework

**DeepEval repo-level layer handle karta hai: evals as code, project repository mein, CI/CD mein,
developer ke daily workflow mein.** Behavior evaluation ko wahan rehna chahiye jahan developers already
rehte hain, warna woh research activity ban kar reh jati hai jo shipping constrain nahi karti.

Ek line mein: **pytest, lekin LLM aur agent behavior ke liye.** Test cases, metrics, thresholds,
assertions, fixtures, CLI runs, CI integration.

**Built-in metrics library:**
- Answer relevancy — response sawal ka jawab deta hai?
- Faithfulness — claims provided context se supported hain?
- Hallucination — fabricated facts hain?
- Contextual precision/recall — retrieval-based components ke liye
- Tool-correctness — sahi tool, sahi arguments
- Task completion — user ka stated task poora hua?
- Bias aur toxicity

**Custom metrics** project-specific needs ke liye — grader prompt + threshold, pytest ki custom
fixtures jaisa.

**CI/CD integration load-bearing hai:** `deepeval test run` command `pytest` ki tarah kaam karta hai —
pass-rate reports, failure detail, GitHub Actions/GitLab CI integration. Prompt change jo critical
metric regress kare, merge block karta hai — yehi discipline TDD ne SaaS ko di thi, ab behavior par.

**Stack mein DeepEval kahan baithta hai:**
- OpenAI's trace grading ko complement karta hai (DeepEval output/tool-use evals CI mein; trace
  grading deep trace inspection ke liye)
- Ragas ke adjacent hai (light RAG evaluation DeepEval mein, knowledge-agent-heavy workloads ke liye
  Ragas)
- Phoenix se distinct hai (Phoenix production observability, DeepEval development-time grading)

## Concept 10 — Ragas (Knowledge Layer) Aur Phoenix (Production Observability)

**Ragas development-time loop close karta hai knowledge-layer agents ke liye; Phoenix production-time
loop close karta hai sab agents ke liye.**

**Ragas ke 5 metrics** Concept 7 mein cover hue. Note: May 2026 tak Ragas RAG-only nahi raha — recent
versions agent-specific metrics bhi ship karte hain (Tool Call Accuracy, Tool Call F1, Agent Goal
Accuracy, Topic Adherence). Course Nine Ragas ko primarily knowledge-layer tool ki tarah rakhta hai.

**Phoenix — production observability layer.** Yeh trace grading, DeepEval, Ragas se alag hai: yeh
agent ko _pehle aur development ke doran_ nahi, **production mein** observe karta hai aur observations
ko future eval dataset material mein badalta hai.

**Phoenix 3 categories mein kya deta hai:**
1. **Trace visualization at scale** — failing customer interaction ek clicked-through trace ban jati
   hai
2. **Experiment management** — 2 agent variants compare karo, drift track karo, regressions flag karo
3. **Trace-to-eval pipeline** — real traces sample karta hai aur eval dataset candidates ki tarah
   surface karta hai — **production failure ek future eval case ban jati hai**

Phoenix open-source aur self-hostable hai (container ki tarah chalta hai).

**Braintrust — commercial alternative.** Teams ke liye jo polished collaborative product chahte hain,
hosted infra ke sath: "Phoenix first, Braintrust later." 3 cheezein jo Braintrust add karta hai:
hosted collaborative workspace (multi-team default), polished experiment-comparison UI, managed
infrastructure. **Migration signals:** 3+ distinct agent products ka coordination overhead, Phoenix
maintenance cost commercial subscription se zyada, collaborative annotation workflows chahiye. Jab tak
in mein se koi true na ho, Phoenix sahi choice hai.

**4-Tool Stack Summary:**
- **OpenAI Agent Evals (+ trace grading)** — hosted agent-evaluation platform, OpenAI runtime ke liye
  primary
- **DeepEval** — repo-level evals, developer workflow mein, CI/CD discipline point
- **Ragas** — specialized RAG evaluation, retrieval-vs-reasoning diagnostic
- **Phoenix** — production observability, trace-to-eval feedback loop

**Stack layered hai, redundant nahi.** Sab 4 adopt karne wali team ko complete eval discipline milti
hai: output/tool-use evals har commit par (DeepEval), trace evals har prompt/model change par (OpenAI
Agent Evals trace grading), RAG evals knowledge agents ke liye (Ragas), continuous production
observability (Phoenix).

---
[⬅ Evaluation Pyramid](02-evaluation-pyramid.md) · [⬆ Index](README.md) · [Agla: The Lab — Setup Aur Decisions 1-3 ➡](04-the-lab-part1.md)
