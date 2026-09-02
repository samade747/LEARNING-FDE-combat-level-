# 03 — Exam Domains: At A Glance

**Poori domain-weight table + book-coverage mapping ab har certification ke apne folder mein hai** —
yeh file sirf quick-glance comparison + index hai. Gen 61 (1 Sep 2026) pe book ne **CCAO-F, CCDV-F
aur CCAR-P ke full blueprints apne per-exam pages pe bhi publish kar diye** — sab per-cert folder ki
PDF-derived tables se match karte hain.

## Sab 8 Certifications, Ek Nazar Mein

| Code | Full Name | Issuer | Path role (gen 61) | Price | Questions | Domain Detail |
| --- | --- | --- | --- | --- | --- | --- |
| [PCAO-F](pcao-f/README.md) | Panaversity Certified Associate: Foundations | Panaversity | **FDE gate — first** | Free (2 attempts) | — | matches CCAO-F; sample 10 Sep, live 18 Sep 2026 |
| [PCAR-F](pcar-f/README.md) | Panaversity Certified Architect: Foundations | Panaversity | **FDE gate — second** | Free (2 attempts) | — | matches CCAR-F; sample "coming soon" |
| [PCDV-F](pcdv-f/README.md) | Panaversity Certified Developer: Foundations | Panaversity | Additional credential | Free (2 attempts) | — | matches CCDV-F; sample "coming soon" |
| [PCAR-P](pcar-p/README.md) | Panaversity Certified Architect: Professional | Panaversity | Capstone (pair ke baad) | Free (2 attempts) | — | matches CCAR-P; sample "coming soon" |
| [CCAO-F](ccao-f/README.md) | Claude Certified Associate: Foundations | Anthropic | **FDE pair — first** (optional) | $99 | 60 | **Output Evaluation & Validation 21%** heaviest |
| [CCAR-F](ccar-f/README.md) | Claude Certified Architect: Foundations | Anthropic | **FDE pair — second** (optional) | $125 | 60 | **Agentic Architecture & Orchestration 27%** heaviest |
| [CCDV-F](ccdv-f/README.md) | Claude Certified Developer: Foundations | Anthropic | Additional credential | $125 | 53 | **Applications & Integration 33.1%** heaviest |
| [CCAR-P](ccar-p/README.md) | Claude Certified Architect: Professional | Anthropic | Senior capstone | $175 | 63 | **Integration 19%** heaviest (flat spread) |

*Saare prices + counts (60/60/53/63) gen 61 pe official-guide-confirmed. **CCAR-P 63 + blueprint
resolved** — 28 Aug ka "independent-only" caveat wapas official ho gaya. Anthropic exams optional
hain (Stage Two).*

## CCAR-F — 5 Domains (Gen 61 Ki Refined Names)

| Domain | Weight |
| --- | ---: |
| **Agentic Architecture & Orchestration** | **27%** |
| Claude Code Configuration & Workflows | 20% |
| Prompt Engineering & Structured Output | 20% |
| Tool Design & MCP Integration | 18% |
| Context Management & Reliability | 15% |

*Book page inko weight-descending order mein list karta hai; official Exam Guide PDF ka apna
numbering: D1 Agentic Arch (27), D2 Tool Design/MCP (18), D3 Claude Code Config (20), D4 Prompt Eng
(20), D5 Context Mgmt (15) — dekho [`ccar-f/01-domain-blueprint.md`](ccar-f/01-domain-blueprint.md).*

**6 published production scenarios** (exam din 4 draw hote hain): Customer Support Resolution Agent ·
Code Generation with Claude Code · Multi-Agent Research System · Developer Productivity with Claude ·
Claude Code for Continuous Integration · Structured Data Extraction. Poori detail
[`ccar-f/02-scope-scoring-and-exam-format.md`](ccar-f/02-scope-scoring-and-exam-format.md).

## CCAO-F — 7 Domains (Guide's Own Numbering)

| # | Domain | Weight |
| --- | --- | ---: |
| 1 | Prompting and Task Execution | 14% |
| 2 | **Output Evaluation and Validation** | **21%** |
| 3 | Product and Model Selection | 12% |
| 4 | Workflow Integration and Solution Design | 16% |
| 5 | Configuration and Knowledge Management | 12% |
| 6 | Governance, Risk, and Responsible Use | 15% |
| 7 | Troubleshooting and Optimization | 10% |

**Domain 2 + 4 + 6 = 52%.** Sab se bara domain prompt-likhna nahi — output evaluate karna hai.

## CCDV-F — 8 Domains (Bohat Uneven)

| Domain | Weight |
| --- | ---: |
| **Applications and Integration** | **33.1%** |
| **Model Selection and Optimization** | **16.8%** |
| Agents and Workflows | 14.7% |
| Prompt and Context Engineering | 11.0% |
| Tools and MCPs | 10.6% |
| Security and Safety | 8.1% |
| Claude Code | 3.1% |
| Eval, Testing, and Debugging | 2.6% |

Top 2 = ~50%. Gen 61 pe **Applications & Integration ka sub-objective breakdown bhi book page pe**:
Claude Application Design 8.6% · Software Engineering Foundations 7.4% · Claude API Mechanics 6.8% ·
Configuration Management 4.1% · Understanding Requirements 3.4% · Systems Life Cycle 2.8%. Book:
*"This is a software engineering exam with an LLM in it, not an LLM exam with some code attached."*

## CCAR-P — 7 Domains (Gen 61 Pe Wapas Published)

| Domain | Weight |
| --- | ---: |
| **Integration** | **19%** |
| Solution Design & Architecture | 17% |
| Evaluation, Testing & Optimization | 16% |
| Governance, Safety & Risk Management | 14% |
| Stakeholder Communication & Lifecycle Management | 14% |
| Claude Models, Prompting & Context Engineering | 13% |
| Developer Productivity & Operational Enablement | 7% |

Flattest spread of any exam. Governance + stakeholder together = 28%, prompting/model-selection ka
double. Book: *"not asking whether you can drive the product. It is asking whether you can own a
system in front of people who did not build it."* Sirf ek domain title vendor ka naam leta hai.

## FDE Path Ka Focus

Recommended FDE pair: **CCAO-F → CCAR-F** (aur inke Panaversity-aligned gate, **PCAO-F → PCAR-F**).
CCDV-F/PCDV-F "additional technical credential". CCAR-P/PCAR-P senior capstone.

## Study Priority (Domain Weight Se)

- **PCAO-F/CCAO-F** (pehla exam): Output Evaluation (21%) → Workflow Integration (16%) → Governance
  (15%) = 52%. [CCAO-F folder](ccao-f/01-domain-blueprint.md).
- **PCAR-F/CCAR-F** (doosra exam, is repo ka main study target): Agentic Architecture (27%) → Claude
  Code Config + Prompt Eng (20% + 20%) → Tool Design/MCP (18%) → Context Management (15%).
  [CCAR-F folder](ccar-f/README.md).
- **CCDV-F** (agar aage jao): Applications and Integration (33.1%) + Model Selection (16.8%) = ~50%.
  [CCDV-F folder](ccdv-f/README.md).

## Root README Staleness (Alag Se Nota)

Domain→book-coverage mapping banate waqt pata chala ke root `README.md` ka status table stale hai —
kai chapters already documented hain lekin table 🔲 dikhata hai. Har cert folder mein ✅/🔲 markers is
repo ke **actual disk state** ke against verify kiye gaye hain.

---
[⬅ Index](README.md) · [Peechay: Stage Two](02-stage-two-anthropic.md) ·
[Agla: Gaps + Study Plan ➡](04-gaps-and-study-plan.md)
