# 02 — Scope, Scoring & Exam Format

*Source: Official exam guide, section 5 (Exam Scenarios), section 10 (How the Exam Is Scored), section
17 (Appendix — Technologies/In-Scope/Out-of-Scope).*

## 6 Exam Scenarios (4 Randomly Drawn Each Sitting)

Exam scenario-based hai. Har scenario ek realistic production context present karta hai jo ek set of
questions frame karta hai. Exam ke waqt, **6 scenarios ke pool mein se 4 randomly present hote hain.**

### Scenario 1 — Customer Support Resolution Agent
Aap Claude Agent SDK se ek customer-support resolution agent bana rahe ho. Agent high-ambiguity
requests handle karta hai (returns, billing disputes, account issues) — backend systems tak access
custom MCP tools se (`get_customer`, `lookup_order`, `process_refund`, `escalate_to_human`). Target:
**80%+ first-contact resolution**, saath saath yeh jaante hue kab escalate karna hai.
**Primary domains:** Agentic Architecture & Orchestration, Tool Design & MCP Integration, Context
Management & Reliability

### Scenario 2 — Code Generation with Claude Code
Aap Claude Code use kar rahe ho software development accelerate karne ke liye — code generation,
refactoring, debugging, documentation. Development workflow mein integrate karna hai custom slash
commands, CLAUDE.md configurations ke sath, aur plan mode vs direct execution samajhna hai.
**Primary domains:** Claude Code Configuration & Workflows, Context Management & Reliability

### Scenario 3 — Multi-Agent Research System
Aap Claude Agent SDK se ek multi-agent research system bana rahe ho. Coordinator agent specialized
subagents ko delegate karta hai — ek web search karta hai, ek documents analyze karta hai, ek findings
synthesize karta hai, aur ek reports generate karta hai. System topics research karta hai aur
comprehensive cited reports produce karta hai.
**Primary domains:** Agentic Architecture & Orchestration, Tool Design & MCP Integration, Context
Management & Reliability

### Scenario 4 — Developer Productivity with Claude
Aap Claude Agent SDK se developer-productivity tools bana rahe ho. Agent engineers ko unfamiliar
codebases explore karne, legacy systems samajhne, boilerplate generate karne, aur repetitive tasks
automate karne mein madad karta hai — built-in tools (Read, Write, Bash, Grep, Glob) use karte hue aur
MCP servers ke sath integrate karte hue.
**Primary domains:** Tool Design & MCP Integration, Claude Code Configuration & Workflows, Agentic
Architecture & Orchestration

### Scenario 5 — Claude Code for Continuous Integration
Aap Claude Code ko CI/CD pipeline mein integrate kar rahe ho. System automated code reviews chalata
hai, test cases generate karta hai, aur pull requests par feedback deta hai. Prompts design karne hain
jo actionable feedback dein aur false positives minimize karein.
**Primary domains:** Claude Code Configuration & Workflows, Prompt Engineering & Structured Output

### Scenario 6 — Structured Data Extraction
Aap Claude se ek structured-data-extraction system bana rahe ho. System unstructured documents se
information extract karta hai, output JSON schemas se validate karta hai, aur high accuracy maintain
karta hai. Edge cases gracefully handle karna hai aur downstream systems ke sath integrate karna hai.
**Primary domains:** Prompt Engineering & Structured Output, Context Management & Reliability

**Note:** Official sample-question set (dekho [03 file](03-how-to-prepare-and-sample-questions.md))
sirf Scenarios 1, 2, 3, aur 5 se questions carry karta hai — Scenarios 4 aur 6 blueprint mein hain lekin
official guide ke 12 sample questions mein directly represent nahi hote.

## How the Exam Is Scored

**Criterion-referenced assessment** — har candidate ek fixed performance standard ke against measure
hota hai, doosre candidates ke against nahi. Aap pass karte ho blueprint mein defined knowledge/skills
demonstrate kar ke, kisi percentage of peers ko outperform kar ke nahi.

**Passing standard:** Passing score ek formal standard-setting study se establish hui — trained
subject-matter experts ne minimally-qualified-candidate ke expected performance level judge kiya.
Score 100–1,000 ke scaled range par report hota hai, cut score **720** hai. Scaled scoring models
different exam forms ke across scores equate karne mein madad karte hain jinki difficulty thodi alag ho
sakti hai.

**Result reporting:** Result pass/fail status + 100–1,000 scaled score ki tarah report hota hai. Score
report har content domain mein sahi answers ka percentage bhi dikhata hai. **Section-level percentages
sirf performance samajhne ke liye hain — pass/fail decide nahi karte**, jo total scaled score par based
hota hai.

## In-Scope Topics (Official Guide Appendix)

- Agentic loop implementation: `stop_reason`-based control flow, tool-result handling, loop-termination
  conditions
- Multi-agent orchestration: coordinator-subagent patterns, task decomposition, parallel subagent
  execution, iterative refinement loops
- Subagent context management: explicit context passing, structured state persistence, manifest-based
  crash recovery
- Tool interface design: effective descriptions likhna, split vs consolidate tools, ambiguity kam karne
  wala tool naming
- MCP tool + resource design: content-catalog resources, action-tools, adoption ke liye description
  quality
- MCP server configuration: project vs user scope, env-var expansion, multi-server simultaneous access
- Error handling + propagation: structured error responses, transient vs business vs permission errors,
  escalation se pehle local recovery
- Escalation decision-making: explicit criteria, customer preferences honor karna, policy-gap
  identification
- CLAUDE.md configuration: hierarchy (user/project/directory), `@import` patterns, glob-pattern
  `.claude/rules/`
- Custom commands + skills: project vs user scope, `context: fork`, `allowed-tools`, `argument-hint`
  frontmatter
- Plan mode vs direct execution: complexity assessment, architectural decisions, single-file changes
- Iterative refinement: input/output examples, test-driven iteration, interview pattern, sequential vs
  parallel issue resolution
- Structured output via `tool_use`: schema design, `tool_choice` configuration, nullable fields
  hallucination prevent karne ke liye
- Few-shot prompting: ambiguous-scenario targeting, format consistency, false-positive reduction
- Batch processing: Message Batches API appropriateness, latency-tolerance assessment, `custom_id`
  failure handling
- Context-window optimization: verbose tool outputs trim karna, structured fact extraction,
  position-aware input ordering
- Human review workflows: confidence calibration, stratified sampling, document-type/field accuracy
  segmentation
- Information provenance: claim-source mappings, temporal data handling, conflict annotation,
  coverage-gap reporting

## Out-of-Scope Topics (Explicitly Excluded)

- Claude models ko fine-tune ya custom models train karna
- Claude API authentication, billing, ya account management
- Specific programming languages/frameworks ki detailed implementation (tool/schema config se
  zyada)
- MCP servers deploy/host karna (infrastructure, networking, container orchestration)
- Claude ki internal architecture, training process, ya model weights
- Constitutional AI, RLHF, ya safety-training methodologies
- Embedding models ya vector-database implementation details
- Computer use (browser automation, desktop interaction)
- Vision/image-analysis capabilities
- Streaming API implementation ya server-sent events
- Rate limiting, quotas, ya API pricing calculations
- OAuth, API-key rotation, ya authentication-protocol details
- Specific cloud-provider configurations (AWS, GCP, Azure)
- Performance benchmarking ya model-comparison metrics
- Prompt-caching implementation details (bas iska existence jaanna kaafi hai)
- Token-counting algorithms ya tokenization specifics

## Technologies + Concepts Reference (Exam Mein Aa Sakte Hain)

- **Claude Agent SDK** — agent definitions, agentic loops, `stop_reason` handling, hooks (`PostToolUse`,
  tool-call interception), `Task` tool se subagent spawning, `allowedTools` configuration
- **Model Context Protocol (MCP)** — MCP servers/tools/resources, `isError` flag, tool descriptions, tool
  distribution, `.mcp.json` configuration, env-var expansion
- **Claude Code** — CLAUDE.md hierarchy (user/project/directory), `.claude/rules/` (YAML frontmatter
  path-scoping), `.claude/commands/`, `.claude/skills/` (`context: fork`, `allowed-tools`, `argument-hint`),
  plan mode, direct execution, `/memory`, `/compact`, `--resume`, `fork_session`, Explore subagent
- **Claude Code CLI** — `-p`/`--print` non-interactive mode, `--output-format json`, `--json-schema`
- **Claude API** — `tool_use` + JSON schemas, `tool_choice` options, `stop_reason` values, `max_tokens`,
  system prompts
- **Message Batches API** — 50% cost savings, 24-hour window, `custom_id` correlation, polling, no
  multi-turn tool calling
- **JSON Schema** — required vs optional fields, enums, nullable fields, "other"+detail patterns, strict
  mode
- **Pydantic** — schema validation, semantic validation errors, validation-retry loops
- **Built-in tools** — Read, Write, Edit, Bash, Grep, Glob — purposes + selection criteria
- **Few-shot prompting / prompt chaining** — ambiguous-scenario targeting, sequential decomposition
- **Context-window management** — token budgets, progressive summarization, lost-in-the-middle,
  scratchpad files
- **Session management** — resumption, `fork_session`, named sessions, session-context isolation
- **Confidence scoring** — field-level confidence, labeled-validation-set calibration, stratified sampling

---
[⬅ 01 — Domain Blueprint](01-domain-blueprint.md) · Next → [03 — How to Prepare + Sample Questions](03-how-to-prepare-and-sample-questions.md)
