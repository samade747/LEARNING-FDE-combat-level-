# Deploy Your Agent Harness to the Cloud

*Source: The AI Agent Factory — "Deploy Your Agent Harness to the Cloud: A Multi-Track Crash Course" (Panaversity)*
*URL: https://agentfactory.panaversity.org/docs/deploying-agents-crash-course*
*Group: Mode 2 — Manufacturing, Phase 3 · Scale the Workforce (Chapter 7 of 9)*

---

## Yeh Course Kis Baare Mein Hai

Ab tak jitne agents banaye sab sirf laptop par chalte the. Yeh course agent ko real cloud service
banata hai jo internet par reachable ho: brain managed cloud runtime par (FastAPI on Azure Container
Apps), memory database mein (Neon Postgres), files object storage mein (Cloudflare R2), risky code
alag locked-down sandbox mein (E2B/Cloudflare Sandbox). **Poora core idea: harness control plane hai
jo aap own karte ho; sandbox execution plane hai jo ek baar use karke phenk dete ho.** 17 concepts, 4
learning tracks, 9 deployment decisions.

## Parts

1. [Overview: Quick Win, Tracks, Aur Stack Primer](00-overview-and-stack-primer.md)
2. [Part 1 — The Deployment Problem (Concepts 1-3)](01-the-deployment-problem.md)
3. [Part 2 — The Five-Component Stack (Concepts 4-7)](02-five-component-stack.md)
4. [Part 3 — The Execution Plane (Concepts 8-10)](03-execution-plane.md)
5. [Part 4 — Observability Aur Evals As Architectural Surfaces (Concepts 11-12)](04-observability-and-evals.md)
6. [Part 5 — The Deployment Lab (Decisions 0-9)](05-the-lab.md)
7. [Part 6-7 — Honest Frontiers Aur Closing (Concepts 13-17)](06-honest-frontiers-and-closing.md)

---

## 5-Component Stack, Ek Nazar Mein

| Surface | Component | Kya Karta Hai |
| --- | --- | --- |
| HTTP service | FastAPI on Azure Container Apps | Harness ko host karta hai |
| Durable state | Neon Postgres | Sessions, runs, traces, audit log |
| File/artifact storage | Cloudflare R2 | Inputs, outputs, knowledge — free egress |
| Isolated execution | E2B / Cloudflare Sandbox | Agent-generated code safely chalata hai |
| Orchestration | OpenAI Agents SDK | Sab kuch jorta hai |

**Discipline ek sentence mein:** *Recipe se deviate karna theek hai. Architecture se deviate karna
theek nahi.* Harness aur sandbox ko separate planes mein chalao, 4 surfaces se observe karo, behavior
ko production se badhne wali eval suite ke against grade karo — architecture kaam karta hai chahe
kaunse bhi cloud components chuno.

*Yeh summary poore course (Deployment Problem + 5-Component Stack + Execution Plane + Observability/
Evals + Lab + Honest Frontiers + Closing) ka overview hai.*
