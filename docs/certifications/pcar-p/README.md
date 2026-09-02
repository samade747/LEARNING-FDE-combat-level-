# PCAR-P — Panaversity Certified Architect: Professional

*Source: book page **[`/docs/certifications/pcar-p`](https://agentfactory.panaversity.org/docs/certifications/pcar-p)**
(gen 61 pe PCAR-P ka apna dedicated page — pehle sirf ek table row tha). Re-fetched 2026-09-02
(Zia Tutor corpus gen 61).*

## Quick Facts

| Field | Detail |
| --- | --- |
| **Full name** | Panaversity Certified Architect: Professional |
| **Matches** | [CCAR-P](../ccar-p/README.md) — $175, **63 items** (ab official-guide-confirmed), 120 min |
| **Role in path** | **Capstone** — FDE gate ka hissa nahi (gate = PCAO-F → PCAR-F). Pair ke baad. |
| **Sample / proctored** | "coming soon" — koi date nahi |
| **Pass score** | 720 / 1000 (scaled score, 72% nahi) |
| **Cost** | Free — Panaversity students: 2 free attempts; 3rd+ fee TBA. External: proctoring fee TBA |

## Kis Ke Liye

Book: *"You have already designed a system somebody depended on... then stayed with the thing after
launch while it drifted and had to be fixed."* Yeh exam architecture ke bahar wale hisse ko examine
karta hai: discovery conversation, ek decision jo non-builder ko justify karna, handover, aur uske
baad ka saal. **Entry-level developers / casual users / prompt-writing-only roles ke liye nahi.**

## "Same Blueprint, One Level Up"

PCAR-P **poora CCAR-P blueprint** (7 domains, published weights) examine karta hai — phir vendor-neutral
aage. Book: saat domain titles mein **sirf ek** vendor ka naam leta hai, baaqi already architecture
ki tarah likhe hain — isliYe Panaversity sitting exam ko widen karta hai bina distort kiye.

## Domain Weights (CCAR-P Blueprint — Gen 61 Pe Wapas Published)

| Domain | Weight |
| --- | ---: |
| **Integration** | **19%** |
| Solution Design & Architecture | 17% |
| Evaluation, Testing & Optimization | 16% |
| Governance, Safety & Risk Management | 14% |
| Stakeholder Communication & Lifecycle Management | 14% |
| Claude Models, Prompting & Context Engineering | 13% |
| Developer Productivity & Operational Enablement | 7% |

**Flattest spread of any exam.** Integration = tool/agent config, authn/authz, accuracy vs latency,
observability at scale, RAG pipelines, retrieval strategy, MCP vs API/CLI vs agent-to-agent.
Governance + stakeholder together = **28%** (prompting/model-selection ka double). Developer
productivity (jahan Claude Code baithta hai) sirf 7%. Book: *"not asking whether you can drive the
product. It is asking whether you can own a system in front of people who did not build it."*

*⚠️ Pichli repo note ("book ne CCAR-P blueprint table hata di, sirf theme rakha") ab **stale** hai —
gen 61 pe full weighted table wapas hai.*

## Study Guide (Book Page)

CCAR-F study guide sab apply hota hai, plus system ke around ka kaam:

| Exam area | Read (book) |
| --- | --- |
| Everything in CCAR-F | Architect Foundations study guide |
| Stakeholder communication | Selling as a Vertical FDE · Getting Paid as a Vertical FDE |
| Operating model + handover | Human-Agent Teams · Designing Agent Experiences |
| Lifecycle + iteration | Eval-Driven Development · Deploy Your Agent Harness |
| Governance + access | AI Identity |

Ek area book current docs pe chhorti hai: **model-selection economics** (live price-latency-quality
trade across Claude tiers, caching/batching ka asar) — book karne wale hafte seekho.

## The Anthropic Twin (CCAR-P)

$175 · 63 items · 120 min · Pearson VUE proctored · 720 scaled · 12-month validity · free on-time
renewal. **Recommended experience:** 3+ saal systems architecture / platform engineering + 6mo+
hands-on Claude in production. Prerequisites: none.
[CCAR-P Exam Guide v1.0](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542810/Claude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf).
Full breakdown: [`../ccar-p/README.md`](../ccar-p/README.md).

## Is Repo Ka Apna Push

Is repo ka current goal PCAR-F/CCAR-F hai (dekho [`../07-practice-log.md`](../07-practice-log.md)) —
PCAR-P uske aur pair ke baad ka capstone hai.

---
[⬅ Certifications Index](../README.md)
