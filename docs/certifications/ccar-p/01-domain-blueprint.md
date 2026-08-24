# 01 — Domain Blueprint (Full Detail, Section 6 Se)

*Source: Official exam guide, Section 6 — "Exam Content Outline (Blueprint)". Weights job-task-analysis
se aayi hain — "relative importance of each domain to competent performance."*

## Domain Weights

| Domain | Content Domain | Weight |
| --- | --- | --- |
| 1 | Solution Design & Architecture | 17% |
| 2 | Claude Models, Prompting & Context Engineering | 13% |
| **3** | **Integration** | **19%** |
| 4 | Evaluation, Testing & Optimization | 16% |
| 5 | Governance, Safety & Risk Management | 14% |
| 6 | Stakeholder Communication & Lifecycle Management | 14% |
| 7 | Developer Productivity & Operational Enablement | 7% |
| | **Total** | **100%** |

**Study priority:** Integration (19%) → Solution Design (17%) → Evaluation/Testing (16%) →
Governance (14%) + Stakeholder Comm (14%) combined = 28% → Models/Prompting (13%) → Dev
Productivity (7%, sab se halka).

## Detailed Objectives Per Domain (Official Guide, Full Bullets)

### Domain 1 — Solution Design & Architecture (17%)

- Business problems ko Claude-based AI solutions mein **translate** karna
- End-to-end architectures design karna (input → processing → output → **feedback loops**)
- Appropriate architectural patterns select karna (**workflow, agentic, augmented LLM**)
- Multi-agent systems aur orchestration strategies design karna
- Complex problem solving ke liye decomposition techniques apply karna
- Solutions ko business value pillars ke sath align karna (efficiency, transformation, productivity,
  cost, performance SLAs)

### Domain 2 — Claude Models, Prompting & Context Engineering (13%)

- Tradeoffs ke basis pe appropriate Claude models select karna
- System prompts, templates, aur guardrails design karna
- Prompt engineering techniques apply karna (zero-shot, few-shot, chain-of-thought)
- Context windows optimize karna aur token usage manage karna
- Prompt reuse strategies implement karna (**caching, modular prompts, Skills**)

### Domain 3 — Integration (19%, sab se bara domain)

- Tool/agent configuration ko **capability bloat** ke liye evaluate karna
- Authentication aur authorization requirements analyze karna security gaps identify karne ke liye
- Accuracy-latency tradeoffs evaluate karna aur configuration decisions justify karna
- Observability challenges analyze karna aur scale pe monitoring strategies select karna
- **RAG pipeline design** karna appropriate chunking aur indexing strategies ke sath
- Retrieval strategies apply karna jo data shape aur query pattern se match karein
- Connection protocols evaluate karna aur appropriate integration mechanism select karna
  (**MCP, API/CLI, agent-to-agent**)
- Progressive discovery vs. monolithic context strategy evaluate karna

### Domain 4 — Evaluation, Testing & Optimization (16%)

- Evaluation metrics define karna (accuracy, latency, cost, safety, security)
- Evaluation datasets aur test frameworks design karna **mixed methodologies** use karke
- A/B testing conduct karna aur iterative improvements karna
- System issues diagnose karna (prompt failure, hallucinations, model mismatch)
- Token usage, latency, aur cost-performance tradeoffs optimize karna
- Logging aur observability tools se system performance monitor karna

### Domain 5 — Governance, Safety & Risk Management (14%)

- Guardrails aur safety controls implement karna
- LLM systems ke risks, limitations, aur failure modes identify karna
- Human-in-the-loop validation strategies apply karna
- Regulations ke sath compliance ensure karna (jaise **GDPR, HIPAA, FedRAMP**)
- Ethical AI considerations address karna (bias, fairness, transparency)

### Domain 6 — Stakeholder Communication & Lifecycle Management (14%)

- Structured discovery aur requirement gathering conduct karna
- Architectural decisions aur tradeoffs communicate karna
- Stakeholder feedback loops aur expectation alignment manage karna (SLAs sameet)
- Architectures document karna aur implementation guidance provide karna
- Lifecycle phases support karna (discovery, design, handoff, monitoring, iteration)

### Domain 7 — Developer Productivity & Operational Enablement (7%, sab se halka)

- Teams ke liye Claude tools aur environments configure karna (jaise Claude Code)
- AI-assisted tooling se developer workflows improve karna
- Debugging aur operational issue resolution support karna

## CCAR-F Se Farq

CCAR-F ka poora content foundation hai — uska Domain 1 (Agentic Architecture & Orchestration, 27%) hi
yahan **"Solution Design & Architecture"** (17%) ban jata hai, thoda broader framing ke sath (business
problem → solution, business-value pillars).

**Do naye domains jo CCAR-F mein bilkul nahi thay** — combined **28% of exam**:

- **Governance, Safety & Risk Management (14%)** — compliance frameworks (GDPR/HIPAA/FedRAMP)
  explicit hain; CCAR-F mein "guardrails via hooks" tak scope tha, regulatory compliance nahi
- **Stakeholder Communication & Lifecycle Management (14%)** — discovery, architectural
  decision-communication, SLA alignment, poori lifecycle support; CCAR-F mein stakeholder-facing
  skills bilkul tested nahi hote

**Integration (19%)** yahan sab se bara domain hai — CCAR-F ke "Tool Design & MCP Integration" (18%)
se milta-julta hai lekin scope wider hai: RAG pipeline design, observability-at-scale, aur protocol
selection (MCP vs API/CLI vs agent-to-agent) explicit objectives hain.

---
[⬅ 00 — Quick Facts](00-quick-facts-and-audience.md) · [Next: 02 — Book Coverage & Scope ➡](02-book-coverage-and-scope.md)
