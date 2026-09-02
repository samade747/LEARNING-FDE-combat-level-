# PCDV-F — Panaversity Certified Developer: Foundations

*Source: book page **[`/docs/certifications/pcdv-f`](https://agentfactory.panaversity.org/docs/certifications/pcdv-f)**
(gen 61 pe apna dedicated page). Re-fetched 2026-09-02 (Zia Tutor corpus gen 61).*

## Role In Path

**PCDV-F FDE gate ka hissa NAHI hai** — gate = PCAO-F → PCAR-F. PCDV-F **"additional technical
credential"** hai: recommended pair ke baad, agar deeper build/ship proof chahiye. Sample + proctored
exam "coming soon".

Book: *"It proves you can build and ship, not only design."* Audience (guide se): AI/ML engineers,
technical leads, senior software engineers. **Non-technical users / no hands-on dev experience /
prompt-writing-only roles ke liye nahi** — un ke liye PCAO-F.

## "Same Blueprint, One Level Up"

PCDV-F poora CCDV-F blueprint (published weights) examine karta hai, phir vendor-neutral aage —
study guide mein **OpenAI Agents SDK aur open-weights models** Claude courses ke saath. Book: API
contract (na ek vendor ka Messages API), agent loop (na ek framework ka harness), evaluation
discipline (na ek product ka debugging view), secrets+identity obligation.

**CCDV-F is the credential that travels** (Anthropic issued, employer-verifiable, CV pe). **CCDV-F
Claude Partner Network tier eligibility mein count hota hai** (CCAO-F nahi).

## Quick Facts

| Field | Detail |
| --- | --- |
| **Full name** | Panaversity Certified Developer: Foundations |
| **Matches** | [CCDV-F](../ccdv-f/README.md) (Anthropic's official exam) |
| **Role in path** | **Additional credential** — ab FDE gate ka hissa nahi |
| **Proctored by** | Panaversity (independently) |
| **Pass score** | 720 / 1000 |
| **Cost** | **Free** — Panaversity students get 2 free attempts; 3rd+ attempt fee TBA. Everyone else pays proctoring fee (TBA) |
| **When** | Recommended pair complete karne ke baad, optional deeper credential |

## Kyun Ab Additional Hai

Developer Foundations prove karti hai ke aap architecture se implementation tak move kar sakte ho:
applications, integrations, agents, workflows, tools, MCP, security, testing, debugging. Book ne
faisla kiya ke FDE gate ke liye judgment (Associate) + system design (Architect) kaafi hain —
implementation proof optional next step hai. Blueprint aur book-coverage abhi bhi valid hain, sirf
path role badla.

## Domain Weights (CCDV-F Blueprint Se Aligned, Bohat Uneven)

| Domain | Weight | Yeh Book Kahan Cover Karti Hai |
| --- | --- | --- |
| **Applications and Integration** | **33.1%** | [Python in the AI Era](../../python-crash-course/README.md), [Deploy Your Agent Harness](../../deploying-agents-crash-course/README.md), [Claude Code and OpenCode](../../agentic-coding/README.md) |
| **Model Selection and Optimization** | **16.8%** | [The Four Layers](../../four-layers/README.md), [Open Source LLMs](../../open-source-llms/README.md) |
| Agents and Workflows | 14.7% | [Build AI Agents with the OpenAI Agents SDK](../../build-agents-crash-course/README.md), [Loop Engineering](../../loop-engineering/README.md), [Choosing Agentic Architectures](../../choosing-agentic-architectures-crash-course/README.md) |
| Prompt and Context Engineering | 11.0% | [AI Prompting in 2026](../../ai-prompting-2026/README.md), [Building the Context Layer](../../context-layer-crash-course/README.md), [RAG on Postgres](../../postgres-ai-crash-course/README.md) |
| Tools and MCPs | 10.6% | [Connector-Native Apps](../../connector-native-apps/README.md), Skills & Connectors *(🔲)*, [Give Your AI Agent a Nervous System](../../ai-agent-nervous-system-crash-course/README.md) |
| Security and Safety | 8.1% | [AI Identity](../../ai-identity-crash-course/README.md) |
| Claude Code | 3.1% | [Claude Code and OpenCode](../../agentic-coding/README.md) |
| Eval, Testing, and Debugging | 2.6% | [Trusting the Checker](../../trusting-the-checker/README.md), [Eval-Driven Development](../../eval-driven-development-crash-course/README.md) |

**Gen 61 pe book page bhi Applications & Integration (33.1%) ka sub-objective breakdown deta hai:**
Claude Application Design 8.6% · Software Engineering Foundations 7.4% · Claude API Mechanics 6.8% ·
Configuration Management 4.1% · Understanding Requirements 3.4% · Systems Life Cycle 2.8%. **Top 3
rows = exam ke sab se bare 3 single objectives.** Book: *"a software engineering exam with an LLM in
it, not an LLM exam with some code attached"* — REST/JSON/async/version-control/code-review apne
terms pe test hote hain.

**Poori sub-skill-weight-level detail** (official CCDV-F Exam Guide v1.0 se, 2026-08-24 ko poora
padha) [CCDV-F folder](../ccdv-f/README.md) mein hai — PCDV-F **usi blueprint** pe based hai.
Recommended experience (required nahi): 1–5 saal software engineering + 6mo+ hands-on Claude/LLM,
Python ya TypeScript, REST APIs + CLI.

## Prep Resources

- **Free sample test** (targets CCDV-F, is exam ke liye bhi valid): [CCDV-F, Developer Foundations](https://flashgenius.net/sample-tests/ccdv-f)
- **Official blueprint authority:** [CCDV-F Exam Guide v1.0](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf)

## Practice Projects

PCDV-F **CCDV-F ke bilkul usi blueprint** par based hai. CCDV-F guide (CCAR-F ke unlike) 4 numbered
exercises nahi deta — sirf "ek application banao" + 3 sample questions (Domains 2, 7, 8). Is repo
ka scaffold un teenon sample questions ko directly implement karta hai:
[`CCDV-F Projects — 00-integration-application`](../ccdv-f/projects/00-integration-application/README.md)
(batch-vs-realtime decision, prompt-injection guardrail, reusable MCP tool), 8 offline pytest tests.

## Test Your Understanding

- [`05-test-your-understanding.md`](05-test-your-understanding.md) — 10 scenario-based questions
  (Panaversity logistics + CCDV-F-blueprint domain weights + 3 sample questions)
- [`quiz.md`](quiz.md) — same 10 questions, standalone self-test version

## Is Repo Ka Apna Push

Yeh **PCAR-F ke baad** ka step hai. PCAR-F par current focus — dekho
[`../07-practice-log.md`](../07-practice-log.md).

---
[⬅ Certifications Index](../README.md)
