# Eval-Driven Development for AI Employees — Summary

Yeh course Mode 2 ka Chapter 6/9 hai: pichle courses (3-8) ne AI agents banaye jo kaam karte hain; yeh
course sikhata hai **kaise pata chale agent sahi kaam kar raha hai** — Test-Driven Development (TDD)
ka agentic-AI version, jise **Eval-Driven Development (EDD)** kehte hain. 15 concepts, 4 learning
tracks (Reader/Beginner/Intermediate/Advanced), 4-tool stack (OpenAI Agent Evals, DeepEval, Ragas,
Phoenix), aur ek 7-Decision hands-on lab.

## 00 — Course Ka Naqsha: 15 Concepts, 4 Tracks

- **3 zaroori terms:** Agent (plain-language task le kar act kare), Tool (function jo agent call kare),
  Trace (run ka complete audit log — model calls, tool calls, handoffs, guardrails).
- **Core thesis:** TDD ne code par confidence diya; EDD agent **behavior** par confidence deta hai. Code
  deterministic hai (tests verify karte), behavior probabilistic hai (evals verify karte).
- **4 Tracks:** Reader (~3-4h, concepts only), Beginner (~1 din, golden dataset + DeepEval output evals
  + tool-use eval), Intermediate (~2 din, + trace grading + Ragas + poora Pyramid), Advanced (~3 din, +
  safety evals + CI/CD + Phoenix). Adoption curve: sprint → weeks → months.
- **Deliverables:** 20-50 case golden dataset, DeepEval output evals, tool-use eval, trace-based eval
  (OpenAI Agent Evals), RAG eval (Ragas, TutorClaw par), CI gate (GitHub Actions), Phoenix dashboard.
- **4-Tool Stack:** OpenAI Agent Evals (+trace grading), DeepEval (pytest-style, CI), Ragas (RAG-specific),
  Phoenix (production observability); Braintrust commercial alternative hai.
- **15 Concepts cheat sheet** table diya gaya hai jo pura course ek-line summaries mein map karta hai.

## 01 — Part 1: The Discipline (Concepts 1-3)

- **Concept 1 — Traditional tests kyun kaafi nahi:** Agent 5 tareeqon se mushkil hai — probabilistic,
  multi-step, tool-using, context-sensitive, external-systems-connected. Traditional tests obsolete nahi
  (tools/durability/API par zaroori rehte hain) lekin ek naya layer chahiye jo agent ka **behavior**
  measure kare.
  - **Maya example:** Tier-1 Support agent sab traditional tests pass karta hai lekin production mein
    **galat customer** ko refund deta hai (similar email, alag account) — koi traditional test yeh nahi
    pakarti kyunki har component individually sahi tha.
  - PRIMM jawab: aisi test suite production failures ka sirf **10-30%** pakregi — agent-reasoning
    failures majority banate hain jo unpakri reh jati hain.
- **Concept 2 — TDD analogy aur uski limits:** Carry hota hai — loop shape, regression net, CI/CD, dataset
  as artifact, team discipline. Tootta hai — determinism (distribution grade hoti hai, single point
  nahi), drift (model retrain se behavior badalta), context-dependent correctness, cost, grader
  subjectivity, moving threshold.
- **Concept 3 — "Behavior" ka matlab:** 3 levels — Level 1 Final output (output evals), Level 2 Tool-use
  record (tool-use evals), Level 3 Full trace (trace evals). Sirf final response evaluate karna exam ka
  aakhri paragraph parh kar grade dene jaisa hai. Teeno levels ek stack hain, alternatives nahi.

## 02 — Part 2: The Evaluation Pyramid (Concepts 4-7)

- **Concept 4 — 9-Layer Pyramid:** 3 groups — Foundation (1. Unit tests, 2. Integration tests),
  LLM/Agent evaluation (3. Output, 4. Tool-use, 5. Trace, 6. RAG/knowledge), Operational reliability
  (7. Safety/policy, 8. Regression, 9. Production). Har layer un failures pakarta hai jo neeche wali
  layers ke liye invisible hain — layered defense, redundant nahi. Ek dataset row har layer se grade ho
  sakti hai, alag scores ke sath.
- **Concept 5 — Output evals:** Sabse accessible/asaan starting point. Achi tarah pakarte: format
  violations, unnecessary refusals, factual errors, hallucinations, tone. Systematically miss karte:
  process failures with correct output, unnecessary tool calls, lucky correctness, post-hoc
  rationalization se chupi reasoning failures.
- **Concept 6 — Tool-use aur trace evals:** Tool-use evals ke 4 metrics — tool-selection,
  argument-correctness, response-interpretation, efficiency. Trace evals poora execution path check
  karte hain — reasoning failures beech mein, handoff failures, guardrail bypasses, retry storms.
  Claudia ka signed-delegation example: teen layers, teen alag failure modes, ek hi decision par.
- **Concept 7 — RAG evals:** 3 failure modes — retrieval failure, grounding failure, citation failure.
  Ragas 5 metrics: Context Relevance, Faithfulness, Answer Correctness, Context Recall, Context
  Precision. TutorClaw (lab ka naya knowledge-agent) is layer ko exercise karne ke liye introduce hota
  hai kyunki Maya ke support agents primarily RAG nahi hain.

## 03 — Part 3: The Stack (Concepts 8-10)

- **Concept 8 — Trace-eval layer per runtime:** Phoenix Claude Managed Agents (OpenTelemetry-native) ke
  liye; OpenAI Agent Evals + Trace Grading OpenAI Agents SDK ke liye. Discipline runtime-independent
  hai, dono equivalent eval suites produce karte hain. Maya ka setup: Path A (Claude Managed Agents) —
  DeepEval + Phoenix + Ragas.
- **Concept 9 — DeepEval:** "Pytest for agent behavior" — repo-level, CI/CD mein. Built-in metrics:
  answer relevancy, faithfulness, hallucination, contextual precision/recall, tool-correctness, task
  completion, bias/toxicity. `deepeval test run` critical metric regress hone par merge block karta hai.
- **Concept 10 — Ragas aur Phoenix:** Ragas dev-time knowledge-layer loop close karta hai (May 2026 tak
  agent-specific metrics bhi ship kar chuka: Tool Call Accuracy, Tool Call F1, Agent Goal Accuracy,
  Topic Adherence). Phoenix production-time loop close karta hai — trace visualization, experiment
  management, trace-to-eval pipeline. Braintrust commercial alternative — migration signals: 3+ agent
  products, maintenance cost > subscription cost, collaborative annotation chahiye.

## 04 — Part 4: The Lab — Setup Aur Decisions 1-3

- **Setup:** Companion base `eval-driven-development/` (`panaversity/agentfactory-manufacturing` repo) —
  `AGENTS.md`, `.mcp.json`, `.env.example`, `maya-stub.py` (3 trace shapes), `corpus/` (5 book excerpts).
  2 completion modes: Full implementation (6-10h) vs Simulated (2-3h, default). 3 runtime paths: A
  (Claude Managed Agents, primary), B (OpenAI Agents SDK), C (other runtimes).
- **Decision 1 — Eval workspace + golden dataset:** Dependencies pin karo, `evals/` scaffold, 50-example
  golden dataset — distribution ~40% refund/20% inquiry/15% technical/15% escalation/10% policy, sab
  easy/medium/hard mix. **Sabse undervalued step** — bad dataset, bad evals.
- **Decision 2 — Output evals (DeepEval):** `evals/output/test_tier1_support.py`, LLM-as-judge backend
  agent-running-model se **alag** rakho (self-grading bias avoid), 4 metrics
  (AnswerRelevancy/Faithfulness/Hallucination/TaskCompletion), baseline commit, GitHub Actions wire.
- **Decision 3 — Trace evals (OpenAI Agent Evals + trace grading):** Golden dataset JSONL upload, 3
  trace-level rubrics (tool_selection, reasoning_soundness, handoff_appropriateness) + 3 output-level
  rubrics. Claude Managed Agents sidebar: same outcome Phoenix evaluator framework se milta hai — sirf
  platform badalta hai, discipline nahi.

## 05 — Part 4: The Lab — Decisions 4-7

- **Decision 4 — Tool-use aur safety evals (Claudia envelope check):** `claudia-delegation.json` (40
  examples min), custom `EnvelopeRespectMetric`, confidence-vs-action consistency check, audit-trail
  consistency, red-team set (8-10 adversarial examples, 3+ genuine violations — agar model 100% pass
  kare, set bohat asaan hai).
- **Decision 5 — RAG evals (Ragas par TutorClaw):** TutorClaw agent banao, 30-example golden dataset, 5
  Ragas metrics. **Diagnostic playbook:** context_recall=0 + context_precision=0 = OOD canary;
  context_recall low + answer_correctness low = retrieval miss; context_recall high + faithfulness low
  = invented claims; context_precision low = retrieval noise.
- **Decision 6 — Regression evals + CI/CD:** Critical-metric >5% drop se regression. Unified runner,
  6-stage GitHub Actions pipeline, baseline management, cost budget ($5 soft/$20 hard cap per run),
  merge-blocking rule with override.
- **Decision 7 — Production observability (Phoenix):** `pip install arize-phoenix`, OpenTelemetry
  export, 3 health summaries (agent health, cost/latency, drift detection >10% alert), trace sampling
  (errors, flagged, low-confidence, edge-of-envelope, random 1%), promotion pipeline (sample → triage →
  promote → threshold review), weekly promotion ritual. Phoenix→Braintrust migration mechanical hai
  (dono OpenTelemetry-compatible).

## 06 — Part 5: Honest Frontiers (Concepts 11-14)

- **Concept 11 — Golden dataset construction:** Sabse undervalued artifact. Quality order:
  representativeness (70% representative + 30% edge cases), difficulty stratification, ground truth
  quality, source diversity, version control. 5 failure patterns: Imagination Trap, Easy-Mode Bias
  (sabse "false confidence"), Single-Author Problem, Stale-Dataset Problem, Pass-Threshold Inflation.
  Recommended path: 50 se shuru, production promotion se organically 500-1000/saal.
- **Concept 12 — Eval-improvement loop:** 7 steps — define task, run agent, capture trace, grade
  behavior (poori suite), identify failure mode (sabse skip hota step — fix layer decide karta hai),
  improve (targeted), rerun (poori suite). Wrong-customer refund walkthrough: poora loop ~1 ghanta laga.
- **Concept 13 — Production observability + trace-to-eval pipeline:** 4 phases — sample, triage (yahan
  teams under-invest karti hain — named owner chahiye), promote, threshold review. "Phoenix bina owner
  ke decoration hai."
- **Concept 14 — Evals kya measure nahi kar sakte:** Achi tarah pakarte — pattern-matching, drift, named
  safety bounds, tool-use correctness. Limited — novel situations, value alignment at edge cases,
  subjective quality, long-tail edge cases, emergent long-conversation behavior, adversarial behavior.
- **5 Anti-Patterns:** output-only evals ko "safe" mat kaho, LLM-as-judge bina calibration mat use karo,
  bara dataset failure-categories samjhe bina mat banao, dashboards ko evals mat samjho, sirf launch se
  pehle evals mat chalao.

## 07 — Part 6: Closing (Concept 15) + Aage Kya

- **Concept 15:** EDD ab TDD ke sath foundational software-engineering discipline ban jati hai — "10
  saal baad, bina eval suite ke agent ship karna waisa hi lagega jaisa aaj bina unit tests ke SaaS ship
  karna."
- **8 architectural invariants + 1 cross-cutting discipline** — Agent Factory track structurally
  complete.
- **5 Frontiers (May 2026 tak):** auto-eval generation, eval-of-evals, alignment metrics beyond
  pattern-matching, multi-agent eval, eval portability across runtimes.
- **Cross-Course Summary table:** kaunsa course kya bana, Course 9 kahan usay eval karta hai (Course 3
  agent loop → output+trace evals; Course 4 system of record → RAG evals; Course 5 envelope → regression
  evals; Course 6 management layer → safety+tool-use evals; Course 8 owner Identic AI → trace+safety
  evals).
- **3 aage ke raste:** Operate, Extend, Contribute (open-source frameworks abhi TDD ke early-2000s
  adoption point par hain).
- **References:** OpenAI Agent Evals/Trace Grading docs, DeepEval, Ragas (+ EACL 2024 paper), Phoenix,
  Braintrust, foundational research (Kent Beck TDD, LLM-as-Judge paper, RAG paper, Hidden Technical Debt
  paper).
