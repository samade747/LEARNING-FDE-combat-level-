# CCAR-P — Claude Certified Architect: Professional

*Source: Official **Claude Certified Architect – Professional Exam Guide v1.0** (effective July 2026,
exam code CCAR-P), PDF read in full 2026-08-24. Also cross-checked against
[Certifications](https://agentfactory.panaversity.org/docs/certifications) (book page).*

## Quick Facts

| Field | Detail |
| --- | --- |
| **Full name** | Claude Certified Architect – Professional |
| **Price** | $175 USD (before partner discount) |
| **Questions** | 63 — multiple-choice + multiple-response |
| **Time limit** | 120 minutes |
| **Delivery** | Pearson VUE — online proctored ya test center |
| **Passing score** | Scaled 720 / (100–1,000 range), criterion-referenced |
| **Validity** | 12 months; on-time renewal free |
| **Panaversity-aligned exam** | [PCAR-P](../pcar-p/README.md) — **planned**, abhi available nahi |
| **FDE path focus** | **Nahi** — is book ke initial FDE path (CCAR-F → CCDV-F) ka hissa nahi, senior capstone hai |

## Kya Test Hota Hai

Validate karta hai ke koi individual **production-grade AI solutions design, build, aur deliver** kar
sakta hai — poori lifecycle ownership ke sath: solution design/prototyping, model/architecture/API
pattern selection, prompt+context strategy, enterprise integration, evaluation/monitoring/
observability, security/compliance/governance, aur **cross-functional stakeholder communication**.

## Intended Audience / MQC

**Mid- to senior-level** solution architects, AI/ML engineers, technical leads jo business problems ko
scalable AI-driven solutions mein translate karte hain, stakeholder engagement + architectural
decisions lead karte hain (security/legal/executive discussions sameet). Industries: financial services,
healthcare, retail, technology, education, government.

**Recommended experience:**
- Software engineering best practices (modular design, separation of concerns, scalability)
- **3+ saal** systems architecture/platform engineering
- **6+ months** hands-on Claude ya comparable LLM systems **production mein**
- End-to-end delivery experience (discovery se deployment/operationalization tak)

**Not intended for:** entry-level developers, casual users, ya sirf prompt-writing tak limited roles.

## Domain Weights + Objectives (Official Guide Se, Full Detail)

| Domain | Weight | Key Objectives |
| --- | --- | --- |
| **Integration** | **19%** | Tool/agent config capability-bloat ke liye evaluate karna; auth/authz security gaps analyze karna; accuracy-latency tradeoffs; observability at scale; RAG pipeline design (chunking/indexing); connection protocol selection (MCP vs API/CLI vs agent-to-agent); progressive discovery vs monolithic context |
| **Solution Design & Architecture** | **17%** | Business problems → Claude solutions translate karna; end-to-end architecture (input→processing→output→feedback); pattern selection (workflow/agentic/augmented LLM); multi-agent orchestration; decomposition; business-value alignment (efficiency, cost, SLAs) |
| **Evaluation, Testing & Optimization** | **16%** | Metrics define karna (accuracy, latency, cost, safety, security); eval datasets + mixed-methodology test frameworks; A/B testing; system-issue diagnosis; token/latency/cost optimization; logging/observability |
| **Governance, Safety & Risk Management** | **14%** | Guardrails/safety controls implement karna; risks/limitations/failure modes identify karna; human-in-the-loop validation; **compliance (GDPR, HIPAA, FedRAMP)**; ethical AI (bias, fairness, transparency) |
| **Stakeholder Communication & Lifecycle Management** | **14%** | Structured discovery/requirement gathering; architectural decisions/tradeoffs communicate karna; feedback loops + SLA alignment; documentation + implementation guidance; lifecycle support (discovery→design→handoff→monitoring→iteration) |
| **Claude Models, Prompting & Context Engineering** | **13%** | Model selection tradeoffs; system prompts/templates/guardrails design; prompting techniques (zero-shot, few-shot, chain-of-thought); context-window optimization; prompt reuse (caching, modular prompts, Skills) |
| **Developer Productivity & Operational Enablement** | **7%** | Teams ke liye Claude tools/environments configure karna (Claude Code); AI-assisted tooling se dev workflows improve karna; debugging/operational-issue support |

**CCAR-F se farq:** Integration (19%) yahan sab se bara domain hai — CCAR-F ka "Agentic Architecture"
27% yahan "Solution Design & Architecture" (17%) ban jata hai, aur do naye domains add hote hain:
**Governance/Safety/Risk (14%)** aur **Stakeholder Communication/Lifecycle (14%)** — compliance
frameworks (GDPR/HIPAA/FedRAMP) aur stakeholder-facing skills yahan explicit hain.

## Yeh Book Kahan Cover Karti Hai

**CCAR-F ka poora mapping yahan bhi apply hota hai** (dekho [CCAR-F folder](../ccar-f/README.md)),
plus:

| Exam Area | Yeh Book Padho |
| --- | --- |
| Stakeholder communication | Selling as a Vertical FDE *(🔲, `how-to-sell/` khaali hai)*, [Getting Paid as a Vertical FDE](../../how-to-get-paid/README.md) *(partial)* |
| Operating model and handover | [Human-Agent Teams](../../human-agent-teams-crash-course/README.md), [Designing Agent Experiences](../../designing-agent-experiences-crash-course/README.md) |
| Lifecycle and iteration | [Eval-Driven Development](../../eval-driven-development-crash-course/README.md), [Deploy Your Agent Harness](../../deploying-agents-crash-course/README.md) |
| Governance and access | [AI Identity](../../ai-identity-crash-course/README.md) |

## Sample Questions (Illustrative, Official Guide Se)

3 sample questions, domains 3/2/4 se — misaal (Domain 3, Integration): *ek customer-support agent
tickets read, replies draft, refunds issue, aur accounts delete kar sakta hai — support staff sirf read/
draft use karte hain. Least-privilege apply karke risk sab se zyada kaise kam ho?* → **Sahi jawab:
refund/delete tools agent ke config se poori tarah remove karo** (logging ya confirmation prompts
"detective/compensating" controls hain, actual privilege removal nahi).

## How to Prepare (Official Guide, Section 7)

- Exam blueprint self-assess karo
- Anthropic docs review karo (Claude API, models, prompting, MCP, Skills)
- **Kam se kam ek end-to-end Claude solution banao aur operate karo** — RAG, evaluation, observability
  sameet
- Architectural decision-making practice karo: model selection, integration protocols, security
  tradeoffs

## Exam Policies (Summary)

Same as [CCAR-F](../ccar-f/README.md#exam-policies-summary) — ID match, max 4 retakes/12mo (waits
14/30/90 din), 24h reschedule window, NDA required, free on-time renewal.

## Document Control

| Version | Change | Date |
| --- | --- | --- |
| 1.0 | Initial publication | July 2026 |

## Prep Resources

- **Official exam guide (full PDF, read 2026-08-24):** [Claude Certified Architect – Professional Exam Guide v1.0](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542810/Claude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf)
- **Free sample test:** [CCAR-P, Architect Professional](https://flashgenius.net/sample-tests/ccar-p)
- **Free Academy courses:** CCAR-F row ki har cheez, plus Bedrock/Vertex AI agar cloud platform se
  deploy karte ho

## Is Repo Ka Apna Push

Is repo ka current goal PCAR-F/CCAR-F hai (dekho [`../07-practice-log.md`](../07-practice-log.md)) —
CCAR-P ek later, senior-level capstone hai, abhi priority nahi.

---
[⬅ Certifications Index](../README.md)
