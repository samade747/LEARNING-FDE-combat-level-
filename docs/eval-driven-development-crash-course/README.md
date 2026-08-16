# Eval-Driven Development for AI Employees

*Source: The AI Agent Factory — "Eval-Driven Development for AI Employees: A Multi-Track Crash Course" (Panaversity)*
*URL: https://agentfactory.panaversity.org/docs/eval-driven-development-crash-course*
*Group: Mode 2 — Manufacturing, Phase 3 · Scale the Workforce (Chapter 6 of 9)*

---

## Yeh Course Kis Baare Mein Hai

Pichle 6 courses ne AI agents banaye jo kaam karte hain. Yeh course sawal jawab deta hai jo woh khula
chor gaye: **aapko kaise pata chalega ke agent sahi kaam kar raha hai?** Test-driven development (TDD)
ne software teams ko code par confidence diya; eval-driven development (EDD) agent teams ko unke
agents ke **behavior** par confidence deta hai. 15 concepts, 4 learning tracks (Reader, Beginner,
Intermediate, Advanced), 4-tool stack (OpenAI Agent Evals, DeepEval, Ragas, Phoenix).

## Parts

1. [Course Ka Naqsha: 15 Concepts, 4 Tracks](00-overview-and-tracks.md)
2. [Part 1 — The Discipline (Concepts 1-3)](01-the-discipline.md)
3. [Part 2 — The Evaluation Pyramid (Concepts 4-7)](02-evaluation-pyramid.md)
4. [Part 3 — The Stack (Concepts 8-10)](03-the-stack.md)
5. [Part 4 — The Lab: Setup Aur Decisions 1-3](04-the-lab-part1.md)
6. [Part 4 — The Lab: Decisions 4-7](05-the-lab-part2.md)
7. [Part 5 — Honest Frontiers (Concepts 11-14)](06-honest-frontiers.md)
8. [Part 6 — Closing (Concept 15) + Aage Kya](07-closing.md)

---

## 9-Layer Evaluation Pyramid, Ek Nazar Mein

| Foundation | LLM/Agent Evaluation | Operational Reliability |
| --- | --- | --- |
| 1. Unit tests | 3. Output evals | 7. Safety/policy evals |
| 2. Integration tests | 4. Tool-use evals | 8. Regression evals |
| | 5. Trace evals | 9. Production evals |
| | 6. RAG/knowledge evals | |

**Poora point:** buildable trustworthy nahi hai. Har layer un failures ko pakarta hai jo neeche wali
layers ke liye invisible hain — yehi wajah hai serious team output evals par nahi rukti.

*Yeh summary poore course (Discipline + Pyramid + Stack + Lab + Frontiers + Closing) ka overview hai.*
