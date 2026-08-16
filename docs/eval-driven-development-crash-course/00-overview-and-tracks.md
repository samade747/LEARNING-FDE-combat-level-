# 00 — Course Ka Naqsha: 15 Concepts, 4 Tracks

## Ek Idea, Plain Lafzon Mein

Pichle 6 courses mein aap ne AI agents banaye jo kaam karte hain: conversations hold karte hain, tools
use karte hain, documents draft karte hain, customer issues route karte hain, doosre agents hire karte
hain, owner ki taraf se act karte hain. Yeh course woh sawal jawab deta hai jo woh courses khula chor
gaye: **aapko kaise pata chalega ke agent sahi kaam kar raha hai?**

Yeh "code chala ki nahi" nahi hai (aap already yeh test karte ho), aur "agent ne reply diya ki nahi"
bhi nahi (aap already yeh log karte ho). Yeh hai: kya agent ne sahi tool chuna, sahi arguments ke sath
call kiya, sahi source mein apna jawab ground kiya, aur zaroorat par escalate kiya? Unit tests,
integration tests, aur ek acha demo yeh jawab nahi dete. **Evals dete hain. Eval ek test hai jo code
ke bajaye behavior measure karta hai.**

Poora course ek line mein: agar test-driven development (TDD) ne SaaS teams ko apne code par confidence
diya, to eval-driven development (EDD) agent teams ko apne agents ke behavior par confidence deta hai.
Code deterministic hai, tests usay verify karte hain. Behavior probabilistic hai, evals usay verify
karte hain. Ek serious team dono practice karti hai.

> **3 terms pehle jaan lo:**
> - **Agent** — software jo plain language task diye jane par decide karti hai kya karna hai: functions
>   call karti hai, dhoondti hai, kaam handoff karti hai, phir respond karti hai. Chatbot baat karta
>   hai; agent act karta hai.
> - **Tool** — ek function jo agent call kar sakta hai, jaise `customer_lookup(email)` ya
>   `refund_issue(account_id, amount)`.
> - **Trace** — ek run ka complete record: har model call, tool call, handoff, guardrail check, order
>   mein. Agent ka audit log. "Trace grading" matlab ek AI grader us log ko parh kar judge kare agent
>   ne sahi kaam kiya ya nahi.

## Yeh Kis Ke Liye Hai, Aur Kaise Parhna Hai

Yeh course Courses 3-8 ne jo banaya usme discipline wrap karta hai, isliye best tab lagta hai jab woh
kar chuke ho. Lekin unhe deploy karne ki zaroorat nahi — companion base mein `maya-stub.py` ship hota
hai, ek chota agent-under-test jo exact trace shapes emit karta hai jo eval suites grade karti hain.

### 4 Learning Tracks — Apna Chuno

| Track | Waqt | Kya Complete Karte Ho | Kis Ke Liye |
| --- | --- | --- | --- |
| **Reader** (pure conceptual) | ~3-4 ghante, koi lab nahi | Concepts 1-4 + Concept 14 + Part 6 closing | Leaders, strategists, non-engineers jo discipline samajhna chahte hain |
| **Beginner** | ~1 din | Reader + Decision 1 (golden dataset) + Decision 2 (DeepEval output evals) + ek tool-use eval | Engineers naye agentic-AI evaluation mein |
| **Intermediate** | ~2 din | Beginner + Decision 3 (trace grading) + Decision 5 (Ragas RAG evals) + poora Part 2 | Teams jo 4-layer pyramid aur 3 frameworks wire karna chahti hain |
| **Advanced** | ~3 din | Intermediate + Decision 4 (safety evals), Decision 6 (CI/CD), Decision 7 (Phoenix) + Part 5 | Production teams poori discipline ship kar rahi hain |

**Track-fork guidance:** Curious-but-non-engineer readers aur decision-making leaders Reader track se
shuru karein. Beginners ko pehli baar mein Advanced complete karne ka pressure nahi lena chahiye —
discipline iterative hai: teams typically ek sprint mein Reader → Beginner, weeks mein Beginner →
Intermediate, aur mahino mein Intermediate → Advanced graduate karti hain.

### Aakhir Mein Kya Milega (Concrete Deliverables)

- **20-50 case golden dataset** (Decision 1, Beginner+): task type se categorized, difficulty se
  stratified, version-controlled
- **DeepEval mein output evals** (Decision 2, Beginner+): answer relevancy, faithfulness, hallucination,
  task-completion metrics
- **Kam az kam ek tool-use eval** (Beginner+): sahi tool, sahi arguments verify karna
- **Ek trace-based eval** (Decision 3, Intermediate+): OpenAI Agent Evals se trace grading
- **Ek RAG eval** (Decision 5, Intermediate+): Ragas ka 5-metric framework, TutorClaw par
- **Ek CI gate** (Decision 6, Advanced): GitHub Actions workflow jo critical metrics regress hone par
  PRs block kare
- **Ek Phoenix dashboard** (Decision 7, Advanced): production observability, trace-to-eval pipeline

## 4-Tool Stack

- **OpenAI Agent Evals (+ trace grading)** — OpenAI ka hosted agent-evaluation platform
- **DeepEval** — open-source, pytest-style framework, repo mein chalta hai, CI/CD mein fit hota hai
- **Ragas** — open-source RAG-specific eval framework
- **Phoenix** — open-source observability + evaluation platform, production traces ke liye
- **Braintrust** — Phoenix ka commercial alternative (Decision 7 mein upgrade path)

## 15 Concepts Cheat Sheet

| # | Concept | Part | Ek-Line Summary |
| --- | --- | --- | --- |
| 1 | Traditional tests kyun kaafi nahi | 1 | Probabilistic, multi-step, tool-using systems ko behavior measurement chahiye, code measurement nahi |
| 2 | TDD analogy aur uski limits | 1 | Loop shape carry hoti hai; determinism assumption tootta hai |
| 3 | "Behavior" ka matlab | 1 | Final answer ≠ trace ≠ path |
| 4 | 9-layer evaluation pyramid | 2 | Unit → integration → output → tool-use → trace → RAG → safety → regression → production |
| 5 | Output evals | 2 | Accessible starting point; correctness/format/hallucination pakarte hain, process failures miss karte hain |
| 6 | Tool-use aur trace evals | 2 | Tool-using agent ke liye path bhi result jitna matter karta hai |
| 7 | RAG evals | 2 | Retrieval, grounding, citation — teeno ka apna metric |
| 8 | Trace-eval layer per runtime | 3 | Phoenix Claude-runtime ke liye, OpenAI Agent Evals OpenAI-runtime ke liye |
| 9 | DeepEval | 3 | Pytest-for-agent-behavior |
| 10 | Ragas + Phoenix | 3 | Knowledge layer evaluate + production observe |
| 11 | Golden dataset construction | 5 | Sabse undervalued artifact; eval quality dataset quality se bound hai |
| 12 | Eval-improvement loop | 5 | Define → run → capture trace → grade → identify failure → improve → rerun |
| 13 | Production observability | 5 | Traces ko eval examples mein badalna ek operational discipline hai |
| 14 | Evals kya measure nahi kar sakte | 5 | Pattern behavior evaluable hai; novel-edge alignment nahi, poori tarah |
| 15 | EDD as foundational discipline | 6 | EDD, TDD ke sath foundational reliability discipline ban jati hai |

---
[⬆ Index](README.md) · [Agla: The Discipline (Concepts 1-3) ➡](01-the-discipline.md)
