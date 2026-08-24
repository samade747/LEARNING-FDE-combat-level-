# 01 — Domain Blueprint (Full Detail)

*Source: Official Exam Guide, Section 6 — "Exam Content Outline (Blueprint)". Weights job-task-analysis
aur content-validation surveys se aaye hain; percentages har domain se draw hue scored items ka
approximate proportion batate hain.*

## Domain Weights

**Weights bohat uneven hain — study time equally split mat karo.**

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

## Detailed Objectives Per Domain (Sub-Skill Weights)

### Domain 1 — Agents and Workflows (14.7%)

- **Agent Architecture (4.5%)** — workflow vs agent decision criteria, manager/supervisor hierarchy
  structure, subagents ka role task execution improve karne mein
- **Agent Construction with Claude (5.3%)** — Claude Agent SDK, custom agent loops/harnesses,
  managed agent deployment models (self-hosted vs Anthropic-hosted), hooks for deterministic actions
- **Agent Patterns and Frameworks (4.9%)** — tool-use loops, sub-agents, memory, context-window
  management, agentic abstraction frameworks (Strands, LangGraph, PydanticAI)

### Domain 2 — Applications and Integration (33.1%)

- **Understanding Requirements (3.4%)** — functional + infrastructure requirements business
  requirements aur solution architecture ke against
- **Systems Life Cycle (2.8%)** — systems life cycle management concepts/frameworks (develop,
  implement, operate, maintain IT systems)
- **Claude API Mechanics (6.8%)** — messages, tools, streaming, vision, thinking, caching, third-party
  vendors ke zariye invoke karna, Messages API data-access patterns, batch API use, realtime-vs-batch
  tradeoffs
- **Software Engineering Foundations (7.4%)** — REST APIs, JSON, async programming, version control,
  SDLC integration, code review, small/large-scale refactoring
- **Claude Application Design (8.6%)** — Claude instructions ko interfaces ke across kaise interpret
  karta hai (Claude Code, Desktop, claude.ai, API, SDKs), content boundaries, schema design, session
  hygiene, plugin management
- **Configuration Management (4.1%)** — CLAUDE.md files, settings.json, model version pinning, prompt
  versioning, plugin dependencies

### Domain 3 — Claude Code (3.1%)

- **Claude Code Operation (3.1%)** — core components (Rules, Skills, Commands, Agents, Agent Memory),
  features (session management, built-in/custom slash commands, headless mode, streaming mode,
  auto-mode), CLAUDE.md hierarchy, repository initialization, settings.json configuration

### Domain 4 — Eval, Testing, and Debugging (2.6%)

- **Debugging and Error Handling (2.6%)** — error-type identification, recovery-strategy selection,
  trace analysis se failure modes identify karna, integration-layer vs model-output problem-origin
  isolation

### Domain 5 — Model Selection and Optimization (16.8%)

- **LLM Fundamentals (5.2%)** — tokens, context windows, sampling, non-determinism, next-token
  generation; model options (fast mode, extended thinking, adaptive thinking, effort levels);
  fundamental prompting (zero-shot, single-shot, multi-shot)
- **Technical Fundamentals (6.1%)** — SDKs jo REST APIs wrap karte hain, websockets integrate karna
- **Model Selection and Tradeoffs (2.7%)** — Opus vs Sonnet vs Haiku use cases, adaptive-thinking
  support, quality/latency/cost tradeoffs, model releases ke across breaking behavior changes
- **Cost and Token Management (2.8%)** — token usage tracking, cost modeling, caching techniques
  (prompt caching, cache check-pointing)

### Domain 6 — Prompt and Context Engineering (11.0%)

- **Context Engineering (3.8%)** — context-window management, context drift/bloat prevention (tool
  output pruning, compaction), subagents/multi-step workflows se context isolation
- **Prompt Engineering (4.6%)** — instruction clarity, few-shot examples, system-vs-user placement,
  output constraints, components ke across prompt placement, iterative refinement, prompt adjustment,
  input sanitization
- **Output Handling (2.6%)** — structured output patterns, response validation, defensive parsing,
  confident output ke against skepticism

### Domain 7 — Security and Safety (8.1%)

- **AI Application Security (3.2%)** — prompt-injection awareness/mitigation, jailbreak defense,
  untrusted-input handling, data-leakage prevention, PII handling, auth/authz/confidentiality/privacy/
  integrity
- **Guardrails and Safe Deployment (2.3%)** — content policy, guardrail layering, secure-by-design
  (privacy, IAM, least privilege)
- **Claude Hooks (1.0%)** — hooks se guardrails/safety controls, destructive actions prevent karna
- **Identity, Secrets, and Key Management (1.6%)** — secrets/credentials/API keys manage karna dev +
  production environments mein, identity validation, access approval/level verification, authorized
  access monitoring

### Domain 8 — Tools and MCPs (10.6%)

- **Tool Implementation (4.4%)** — tool use + function calling, external-system-interaction
  configuration, tool description writing, error handling, usage patterns (agentic harness dispatch,
  client-side vs server-side, approval patterns), tool-set construction best practices
- **MCP Server Development (2.1%)** — server authoring, deployment, Claude applications ke sath
  integration, MCP resources/tools/prompts, communication patterns (stdio, sockets, client vs server)
- **Agentic Customization (4.1%)** — built-in Tools vs custom Tools vs Skills vs MCPs tradeoffs, sahi
  approach select karna given use case ke liye

---
[⬅ 00 — Quick Facts & Audience](00-quick-facts-and-audience.md) · [Agla: 02 — Scope & Gaps ➡](02-scope-and-gaps.md)
