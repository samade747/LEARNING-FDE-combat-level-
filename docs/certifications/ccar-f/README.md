# CCAR-F — Claude Certified Architect: Foundations

*Source: Official **Claude Certified Architect – Foundations Exam Guide v1.0** (effective July 2026,
exam code CCAR-F), PDF read in full 2026-08-24. Also cross-checked against
[Certifications](https://agentfactory.panaversity.org/docs/certifications) (book page). Yeh is repo ke
FDE path ka **pehla Anthropic exam** hai — dekho [Stage Two](../02-stage-two-anthropic.md).*

## Quick Facts

| Field | Detail |
| --- | --- |
| **Full name** | Claude Certified Architect – Foundations |
| **Price** | $125 USD (before partner discount) |
| **Questions** | 60 — multiple-choice + multiple-response (har item batata hai kitne responses chunne hain) |
| **Exam structure** | **4 scenarios, ek bank of 6 mein se randomly chuni gayi** — har scenario ek set of questions frame karta hai |
| **Time limit** | 120 minutes |
| **Delivery** | Pearson VUE — online proctored ya test center |
| **Passing score** | Scaled 720 / (100–1,000 range) — criterion-referenced, doosre candidates se compete nahi karte |
| **Validity** | 12 months; on-time renewal free (non-proctored refresher) |
| **Launched** | March 2026 — programme ka pehla exam |
| **Panaversity-aligned exam** | [PCAR-F](../pcar-f/README.md) — free, same blueprint |

## Kya Test Hota Hai — Judgment, Recall Nahi

Exam **realistic scenarios** pe based hai jo actual customer use cases se liye gaye: customer-support
agents, multi-agent research pipelines, Claude Code ka CI/CD mein integration, developer productivity
tools, aur unstructured documents se structured data extraction. **Candidates ko conceptual knowledge
ke sath-sath practical judgment bhi dikhani hoti hai** — architecture, configuration, aur production
tradeoffs ke baare mein.

## Intended Audience / Minimally Qualified Candidate (MQC)

Ideal candidate ek **solution architect** hai jo Claude ke sath production applications design/implement
karta hai — hands-on experience ke sath:

- Claude Agent SDK se agentic applications banana (multi-agent orchestration, subagent delegation,
  tool integration, lifecycle hooks)
- Claude Code ko team workflows ke liye configure karna (CLAUDE.md, Agent Skills, MCP integrations,
  plan mode)
- MCP tool/resource interfaces design karna backend integration ke liye
- Reliable structured output ke liye prompts engineer karna (JSON schemas, few-shot, extraction)
- Context windows manage karna (long documents, multi-turn, multi-agent handoffs)
- Claude ko CI/CD pipelines mein integrate karna (automated review, test generation, PR feedback)
- Escalation/reliability decisions (error handling, human-in-the-loop, self-evaluation)

**Typical experience: 6+ months** Claude APIs, Agent SDK, Claude Code, aur MCP ke sath — model ki
capabilities aur limitations dono samajhte hue.

## Domain Weights + Task Statements (Official Guide Se, Full Detail)

| Domain | Weight | Yeh Book Kahan Cover Karti Hai |
| --- | --- | --- |
| **1. Agentic Architecture & Orchestration** | **27%** | [Choosing Agentic Architectures](../../choosing-agentic-architectures-crash-course/README.md), [Loop Engineering](../../loop-engineering/README.md), [Harness Engineering](../../harness-engineering/README.md), [Graph Engineering](../../graph-engineering/README.md) |
| 2. Claude Code Configuration & Workflows | 20% | [Claude Code and OpenCode](../../agentic-coding/README.md), [Plugins for AI Agents](../../plugins-crash-course/README.md) |
| 3. Prompt Engineering & Structured Output | 20% | [AI Prompting in 2026](../../ai-prompting-2026/README.md), [Spec-Driven Development](../../spec-driven-development/README.md) |
| 4. Tool Design & MCP Integration | 18% | [Connector-Native Apps](../../connector-native-apps/README.md), Skills & Connectors *(🔲)* |
| 5. Context Management & Reliability | 15% | [Building the Context Layer](../../context-layer-crash-course/README.md), [The Four Layers](../../four-layers/README.md), [RAG on Postgres](../../postgres-ai-crash-course/README.md) |

**Study priority:** Domain 1 (27%) → Domains 2+3 (20%+20%=40%) → Domain 4 (18%) → Domain 5 (15%).

### Domain 1 — Agentic Architecture & Orchestration (27%) — 7 Task Statements

1. **Design and implement agentic loops** — `stop_reason` ("tool_use" vs "end_turn") inspect karna,
   tool results ko conversation history mein append karna, loop-termination anti-patterns avoid karna
   (natural-language parsing, arbitrary iteration caps)
2. **Orchestrate multi-agent systems (coordinator-subagent patterns)** — hub-and-spoke architecture,
   subagents ka isolated context, dynamic subagent selection, iterative refinement loops
3. **Configure subagent invocation, context passing, spawning** — `Task` tool, `AgentDefinition`,
   explicit context passing (subagents parent context automatically inherit nahi karte), fork-based
   session management
4. **Multi-step workflows with enforcement/handoff patterns** — programmatic enforcement (hooks,
   prerequisite gates) vs prompt-based guidance, structured handoff summaries
5. **Apply Agent SDK hooks** — `PostToolUse` for data normalization, tool-call interception for
   compliance rules, hooks vs prompt-based enforcement
6. **Design task decomposition strategies** — prompt chaining (fixed sequential) vs dynamic adaptive
   decomposition
7. **Manage session state, resumption, forking** — `--resume <session-name>`, `fork_session`,
   informing resumed sessions about file changes

### Domain 2 — Claude Code Configuration & Workflows (20%) — 6 Task Statements

1. **Configure CLAUDE.md hierarchy** — user (`~/.claude/CLAUDE.md`) vs project (`.claude/CLAUDE.md`)
   vs directory-level; `@import` syntax; `.claude/rules/` for modular topic files
2. **Custom slash commands and skills** — project-scoped (`.claude/commands/`) vs user-scoped;
   `SKILL.md` frontmatter (`context: fork`, `allowed-tools`, `argument-hint`)
3. **Path-specific rules** — `.claude/rules/` YAML frontmatter `paths:` glob patterns for conditional
   convention loading
4. **Plan mode vs direct execution** — plan mode for architectural/multi-file changes, direct execution
   for well-scoped single-file changes, `Explore` subagent for verbose discovery
5. **Iterative refinement techniques** — concrete input/output examples, test-driven iteration,
   interview pattern
6. **Integrate Claude Code into CI/CD** — `-p`/`--print` flag, `--output-format json` +
   `--json-schema`, session context isolation (self-review vs independent review)

### Domain 3 — Prompt Engineering & Structured Output (20%) — 6 Task Statements

1. **Explicit criteria to reduce false positives** — vague instructions vs specific categorical criteria
2. **Few-shot prompting** — ambiguous-case demonstration, format consistency, hallucination reduction
3. **Enforce structured output via tool_use + JSON schemas** — `tool_choice` ("auto"/"any"/forced),
   nullable fields to prevent fabrication, enum + "other" patterns
4. **Validation, retry, feedback loops** — retry-with-error-feedback, limits of retry, `detected_pattern`
   tracking
5. **Efficient batch processing** — Message Batches API (50% savings, up to 24h window, no SLA,
   no multi-turn tool calling), `custom_id` correlation
6. **Multi-instance/multi-pass review architectures** — self-review limitations, independent review
   instances, per-file + integration passes

### Domain 4 — Tool Design & MCP Integration (18%) — 5 Task Statements

1. **Effective tool interfaces** — descriptions as the primary LLM tool-selection mechanism, avoiding
   ambiguous/overlapping descriptions
2. **Structured error responses for MCP tools** — `isError` flag, transient vs validation vs business vs
   permission errors, retryable metadata
3. **Distribute tools across agents + tool_choice** — too many tools degrades reliability (18 vs 4-5),
   scoped tool access, `tool_choice` options
4. **Integrate MCP servers** — project-scoped `.mcp.json` vs user-scoped `~/.claude.json`, env var
   expansion, MCP resources for content catalogs
5. **Built-in tools (Read, Write, Edit, Bash, Grep, Glob)** — selection criteria, Edit-fails-fallback to
   Read+Write

### Domain 5 — Context Management & Reliability (15%) — 6 Task Statements

1. **Manage conversation context across long interactions** — progressive summarization risks,
   "lost in the middle" effect, persistent "case facts" blocks
2. **Escalation and ambiguity resolution patterns** — appropriate triggers, unreliable proxies
   (sentiment, self-reported confidence)
3. **Error propagation across multi-agent systems** — structured error context, access failures vs
   valid empty results
4. **Context management in large codebase exploration** — scratchpad files, subagent delegation,
   crash-recovery manifests, `/compact`
5. **Human review workflows + confidence calibration** — stratified sampling, field-level confidence,
   accuracy by document type/field
6. **Information provenance in multi-source synthesis** — claim-source mappings, conflict annotation,
   temporal data handling

## 6 Exam Scenarios (4 Randomly Drawn Each Sitting)

1. Customer Support Resolution Agent (Domains 1, 4, 5)
2. Code Generation with Claude Code (Domains 2, 5)
3. Multi-Agent Research System (Domains 1, 4, 5)
4. Developer Productivity with Claude (Domains 4, 2, 1)
5. Claude Code for Continuous Integration (Domains 2, 3)
6. Structured Data Extraction (Domains 3, 5)

## In-Scope vs Out-of-Scope (Official Guide Appendix)

**In-scope highlights:** agentic loop implementation, multi-agent orchestration, tool interface design,
MCP server config, CLAUDE.md hierarchy, custom commands/skills, plan mode vs direct execution,
structured output via `tool_use`, batch processing, context-window optimization, human review
workflows, information provenance.

**Explicitly out-of-scope:** fine-tuning/training custom models, API auth/billing/account management,
Claude's internal architecture/training/model weights, Constitutional AI/RLHF, embedding models/vector
DB internals, computer use (browser/desktop automation), vision/image analysis, streaming API
implementation, rate limiting/pricing calculations, OAuth/key rotation details, cloud-provider-specific
config, benchmarking, prompt-caching implementation details, tokenization algorithms.

## How the Exam Is Scored

**Criterion-referenced** — fixed performance standard, doosre candidates se compete nahi karte. Cut
score 720 ek formal standard-setting study se aaya (subject-matter experts ne minimally-qualified
candidate ka performance level judge kiya). Score report **pass/fail + scaled score + domain-by-domain
percent-correct** deta hai — lekin domain percentages pass/fail decide nahi karte, sirf total scaled
score karta hai.

## Exam Policies (Summary)

- **ID:** government photo ID, registration name se exactly match honi chahiye
- **Retakes:** rolling 12 months mein max 4 attempts; waits 14/30/90 din (1st/2nd/3rd failure ke baad)
- **Reschedule:** 24h+ pehle free; andar forfeit
- **NDA:** exam shuru hone se pehle accept karna zaroori — decline = session end, no refund
- **Conduct:** webcam view mein rehna (online), clear workspace, koi communication nahi, content
  capture/reproduce mana hai
- **Renewal:** on-time free (non-proctored refresher); lapse hone par full exam dobara

## How to Prepare (Official Guide, Section 7) + 4 Hands-On Exercises

- Claude Agent SDK se agent banao: poora agentic loop, error handling, session management,
  subagent spawning
- Real project ke liye Claude Code configure karo: CLAUDE.md hierarchy, `.claude/rules/`, custom
  skills (`context: fork`, `allowed-tools`), MCP server integration
- MCP tools design + test karo: differentiated descriptions, structured errors, ambiguous-request
  testing
- Structured data extraction pipeline banao: `tool_use` + JSON schemas, validation-retry, batch
  processing
- **4 Preparation Exercises** (official guide mein full step-by-step): (1) Multi-Tool Agent with
  Escalation Logic, (2) Configure Claude Code for Team Workflow, (3) Structured Data Extraction
  Pipeline, (4) Multi-Agent Research Pipeline with Error Propagation

## Sample Questions (Illustrative, Official Guide Se)

Guide mein 12 sample questions hain, scenario-grounded, explanations ke sath. Misaal (Scenario 1 —
Customer Support): *"Agent 12% cases mein `get_customer` skip kar deta hai — sirf naam se
`lookup_order` call karta hai. Sab se effective fix?"* → **Sahi jawab: programmatic prerequisite jo
`process_refund`/`lookup_order` ko block kare jab tak `get_customer` verified ID na de** (prompt-based
"mandatory" instruction ya few-shot examples probabilistic hain, deterministic guarantee nahi dete).

## Document Control

| Version | Change | Date |
| --- | --- | --- |
| 1.0 | Formatting/layout updates | July 2026 |
| 0.2 | Draft revision | June 2026 |
| 0.1 | Initial draft | February 2026 |

## Prep Resources

- **Official exam guide (full PDF, read 2026-08-24):** [Claude Certified Architect – Foundations Exam Guide v1.0](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf)
- **Free sample test:** [CCAR-F, Architect Foundations](https://flashgenius.net/sample-tests/ccar-f)
- **Free Academy courses:** Building with the Claude API · MCP: Advanced Topics · Claude Code 101 ·
  official docs on agents, context management, and tool design
- **Registration:** [Architect Foundations Partner Academy page](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification)

## Is Repo Ka Apna Push

Yeh repo ka goal pehle **PCAR-F** (free, same blueprint) hai, 2026-10-05 tak — dekho
[`../07-practice-log.md`](../07-practice-log.md). CCAR-F usi ke baad, FDE Internship Program & partner
access milne ke baad aata hai.

---
[⬅ Certifications Index](../README.md)
