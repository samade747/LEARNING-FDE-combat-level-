# CCDV-F — Claude Certified Developer: Foundations

*Source: Official **Claude Certified Developer – Foundations Exam Guide v1.0** (effective July 2026,
exam code CCDV-F), PDF read in full 2026-08-24. Also cross-checked against
[Certifications](https://agentfactory.panaversity.org/docs/certifications) (book page). Yeh is repo ke
FDE path ka **doosra Anthropic exam** hai — dekho [Stage Two](../02-stage-two-anthropic.md).*

## Quick Facts

| Field | Detail |
| --- | --- |
| **Full name** | Claude Certified Developer – Foundations |
| **Price** | $125 USD (before partner discount) |
| **Questions** | 53 — multiple-choice + multiple-response |
| **Time limit** | 120 minutes |
| **Delivery** | Pearson VUE — online proctored ya test center |
| **Passing score** | Scaled 720 / (100–1,000 range), criterion-referenced |
| **Validity** | 12 months; on-time renewal free |
| **Panaversity-aligned exam** | [PCDV-F](../pcdv-f/README.md) — free, same blueprint |

## Kya Test Hota Hai

Validate karta hai ke koi individual **production-grade applications, agents, aur workflows** bana,
integrate, aur ship kar sakta hai Claude platform pe — foundational level pe. Technical requirements ko
API integration, agent/tool construction, prompt/context engineering, evaluation, security, aur model
selection ke zariye working systems mein translate karna.

## Intended Audience / MQC

**AI/ML engineers, technical leads, senior software engineers** jo LLM-based production solutions
build/integrate/ship karte hain. Recommended experience:

- 1-5 saal software engineering, **6+ months hands-on Claude ya comparable LLM systems**
- Python aur/ya TypeScript proficiency, REST APIs + CLI tools fluency
- LLM fundamentals, agents, context management, MCP ki working understanding

**Prerequisites: koi mandatory nahi** — credential sirf exam performance pe award hota hai. **Not
intended for:** non-technical/casual Claude users, ya sirf prompt-writing tak limited roles.

## Domain Weights + Skill Breakdown (Official Guide Se, Full Detail)

**Domain weights bohat uneven hain — study time equally split mat karo.**

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

**Top 2 rows exam ka aadha hain** (33.1% + 16.8% ≈ 50%). Claude Code + Eval milkar 6% se kam.

### Sub-Skill Weights (Official Guide, Har Domain Ke Andar)

**Domain 1 — Agents and Workflows (14.7%):** Agent Architecture 4.5% (workflow vs agent decision
criteria, manager/supervisor hierarchies, subagents) · Agent Construction with Claude 5.3% (Agent
SDK, custom loops/harnesses, self-hosted vs Anthropic-hosted, hooks) · Agent Patterns and Frameworks
4.9% (tool-use loops, sub-agents, memory, Strands/LangGraph/PydanticAI)

**Domain 2 — Applications and Integration (33.1%):** Understanding Requirements 3.4% · Systems Life
Cycle 2.8% · **Claude API Mechanics 6.8%** (messages, tools, streaming, vision, thinking, caching,
batch API tradeoffs) · **Software Engineering Foundations 7.4%** (REST, JSON, async, version control,
SDLC, code review, refactoring) · **Claude Application Design 8.6%** (interfaces — Claude Code,
Desktop, claude.ai, API, SDKs; content boundaries; schema design; session hygiene; plugins) ·
Configuration Management 4.1% (CLAUDE.md, settings.json, model version pinning, prompt versioning)

**Domain 3 — Claude Code (3.1%):** Claude Code Operation 3.1% (Rules, Skills, Commands, Agents,
Agent Memory; session management; headless/streaming/auto-mode; CLAUDE.md hierarchy;
settings.json)

**Domain 4 — Eval, Testing, and Debugging (2.6%):** Debugging and Error Handling 2.6% (error-type
identification, recovery strategy selection, trace analysis, integration-layer vs model-output isolation)

**Domain 5 — Model Selection and Optimization (16.8%):** LLM Fundamentals 5.2% (tokens, context
windows, sampling, non-determinism; fast/extended/adaptive thinking; zero/single/multi-shot) ·
Technical Fundamentals 6.1% (SDKs wrapping REST APIs, websockets) · Model Selection and Tradeoffs
2.7% (Opus vs Sonnet vs Haiku, quality/latency/cost, breaking changes across releases) · Cost and
Token Management 2.8% (token tracking, cost modeling, prompt caching, cache check-pointing)

**Domain 6 — Prompt and Context Engineering (11.0%):** Context Engineering 3.8% (context window
management, drift/bloat prevention — pruning/compaction, subagent isolation) · Prompt Engineering
4.6% (instruction clarity, few-shot, system vs user placement, output constraints, iterative refinement,
input sanitization) · Output Handling 2.6% (structured output, response validation, defensive parsing)

**Domain 7 — Security and Safety (8.1%):** AI Application Security 3.2% (prompt injection, jailbreak
defense, untrusted input, PII, auth/authz/confidentiality/integrity) · Guardrails and Safe Deployment
2.3% (content policy, guardrail layering, least privilege) · Claude Hooks 1.0% (guardrails/safety via
hooks) · Identity, Secrets, and Key Management 1.6% (credentials, API keys, identity validation, access
monitoring)

**Domain 8 — Tools and MCPs (10.6%):** Tool Implementation 4.4% (function calling, tool descriptions,
error handling, client-side vs server-side, approval patterns) · MCP Server Development 2.1% (server
authoring, deployment, resources/tools/prompts, stdio/sockets) · Agentic Customization 4.1%
(built-in Tools vs custom Tools vs Skills vs MCPs tradeoffs)

## Gaps (Book Mein Abhi Nahi)

**Model Selection and Optimization (16.8%)** book ka sab se thin area hai. Current Opus/Sonnet/Haiku
trade-offs, token budgeting, prompt caching/batch pricing — dekho
[04-gaps-and-study-plan.md](../04-gaps-and-study-plan.md) ke "3 permanent gaps" section.

## Sample Questions (Illustrative, Official Guide Se)

3 sample questions diye gaye hain domains 2, 7, aur 8 se — misaal (Domain 7, Security): *ek agent web
pages summarize karta hai jinme hidden text ho system prompt reveal karne ki koshish kare — sab se
effective mitigation?* → **Sahi jawab: retrieved content ko untrusted input treat karo, trusted
instructions se separate rakho, guardrails/hooks se sensitive actions block karo.**

## How to Prepare (Official Guide, Section 7)

- Exam blueprint self-assess karo Section 6 ke against
- Official Anthropic docs review karo (Claude API, models, prompting, Claude Code, Skills, MCP)
- **Kam se kam ek Claude application banao** jo API exercise kare, 1+ tool integrate kare, basic
  prompt/context engineering apply kare, aur simple security/eval practices include kare
- Developer competencies practice karo: prompts/system instructions, agents/workflows, Claude Code
  config, token/cost management, guardrails, custom tools/MCP servers

## Exam Policies (Summary)

Same as [CCAR-F](../ccar-f/README.md#exam-policies-summary) — ID match, max 4 retakes/12mo (waits
14/30/90 din), 24h reschedule window, NDA required, free on-time renewal.

## Document Control

| Version | Change | Date |
| --- | --- | --- |
| 1.0 | Initial publication | July 2026 |

## Prep Resources

- **Official exam guide (full PDF, read 2026-08-24):** [Claude Certified Developer – Foundations Exam Guide v1.0](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf)
- **Free sample test:** [CCDV-F, Developer Foundations](https://flashgenius.net/sample-tests/ccdv-f)
- **Free Academy courses:** Building with the Claude API (84 lectures, backbone) · Introduction to MCP
  · Claude Code in Action · Introduction to agent skills · Introduction to subagents

## Is Repo Ka Apna Push

Yeh repo ka pehla real target **PCAR-F** hai (dekho [`../07-practice-log.md`](../07-practice-log.md)).
PCDV-F (aur phir CCDV-F) usi ke baad aata hai.

---
[⬅ Certifications Index](../README.md)
