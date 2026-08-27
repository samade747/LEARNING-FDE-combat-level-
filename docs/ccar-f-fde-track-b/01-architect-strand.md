# 01 — Architect Strand: Week by Week (13 Weeks)

CCAR-F exam blueprint ka full domain-weight table already [`docs/certifications/ccar-f/01-domain-blueprint.md`](../certifications/ccar-f/01-domain-blueprint.md)
mein hai — yahan duplicate nahi kar rahe. Quick recap: **Agentic Architecture 27%**, Claude Code Config
20%, Prompt Engineering 20%, Tool Design/MCP 18%, Context Management 15%.

**Exam facts (v1.0, July 2026):** 60 items, 4 scenarios (bank of 6 se drawn), 120 min, 720/1000 passing.

## Week 1 — Foundations Sprint

Sirf yeh week Track A se differ karti hai (entry contract verify + decision framework install karti
hai speed se). Reads: *Roles This Book Trains*, *FDE AF Model*, *Agentic Coding* (review), *Four
Layers*, *Is This an Agent Problem?*, *Choosing Agentic Architectures* — sab already is repo mein
[[roles-this-book-trains]], [[ecosystem-fde-af-model]], [[agentic-coding]], [[four-layers]],
[[is-this-an-agent-problem]], [[choosing-agentic-architectures-crash-course]].

**Classification lab:** 6 business problems ko classify karo (direct call / workflow / single agent /
multi-agent / Claude Code workflow / human-agent workflow), har ek ka enforcement mechanism + failure
mode naam do.

Week 2 se Track B == Track A Weeks 15-26.

## Weeks 2-11 — Compressed Table

| Week | Topic | Exam Mapping | Lab / Project |
| --- | --- | --- | --- |
| 2 | The Agentic Loop by Hand — Messages API statelessness, content blocks, `stop_reason`, `tool_use`/`tool_result`, parallel calls, `tool_choice` | Task 1.1; 2.3/4.3 | **Project 1:** 2-tool loop, no framework — diagnose missing history, lost tool result, wrong stop handling, repeated calls, premature termination |
| 3 | Claude Agent SDK I — tools, permissions, MCP, structured tool errors (transient/validation/business/permission) | Tasks 2.1-2.3, 2.5 | 2 overlapping tools, measure misrouting across 20 prompts, fix descriptions |
| 4 | Claude Agent SDK II — coordinator-subagent, explicit context passing (subagents don't auto-inherit), `Task` delegation | Tasks 1.2, 1.3, 1.6 | Repair a narrow decomposition ("creative industries" failure); add scoped `verify_fact` |
| 5 | Claude Agent SDK III — hooks (`PreToolUse`/`PostToolUse`), approval boundaries, escalation criteria, session resume/fork | Tasks 1.4, 1.5, 1.7, 5.1, 5.2 | **Project 2:** governed customer-support agent — 4 tools, structured errors, programmatic refund controls, escalation, persistent case facts |
| 6 | Claude Code architecture — plan vs direct execution, refinement techniques (targeted examples, TDD iteration, interview pattern) | Tasks 3.4, 3.5 | One task, each refinement technique compared before/after |
| 7 | Claude Code for Teams — instruction scopes, nested `CLAUDE.md`, `.claude/rules/` globs, skills, project vs user MCP config | Tasks 3.1-3.3 | Wrongly-scoped rule diagnose + fix; `context: fork` skill isolation verify — **this is the Week-7 lab, aligns to official Exercise 2** (scaffold: [`docs/certifications/ccar-f/projects/02-claude-code-team-workflow/`](../certifications/ccar-f/projects/02-claude-code-team-workflow/README.md)) |
| 8 | Claude Code as a CI Worker — `-p/--print`, exit codes, `--output-format json`, `--json-schema`, bounded runs, prior-finding suppression | Tasks 3.6, 4.1, 4.6; Scenario 5 | PR review in CI, schema-validated findings, 3 intentional failures |
| 9 | Structured Output I — schema design (required/nullable, `other`+detail, `unclear`), few-shot for decision boundaries | Tasks 4.2, 4.3 | **Project 3 begins:** extraction schema vs missing/ambiguous/out-of-enum docs — absent info → `null`, never invented |
| 10 | Structured Output II — semantic validation, targeted retry, Message Batches (50% cost cut, up to 24h, no multi-turn loop inside one batch), confidence-routed review | Tasks 4.4, 4.5, 5.5 | **Project 3 completed:** validation + retry/resubmission + batch + confidence routing |
| 11 | Context, Reliability, Provenance — progressive summarization, lost-in-the-middle, key-facts blocks, manifests/crash recovery, claim-source mappings | Tasks 5.1, 5.3, 5.4, 5.6 | **Project 4:** multi-agent research system — parallel subagents, provenance, simulated timeout with partial results, conflicting sources with attribution |

**Naming note (exam-snapshot vs current):** CCAR-F v1.0 kuch jagah snapshot terminology use karti hai
jo live SDK se thoda alag ho sakti hai — jaise delegation tool ka naam `Task` (Week 4), ya "custom
commands" vs "skills" (Week 7, ab converged). Exam terminology yaad rakho, live tool verify karte
waqt current naming check karo.

## Week 12 — Six-Scenario Workshop + Mock One

Official 6 scenario frames: Customer Support Resolution Agent, Code Generation with Claude Code,
Multi-Agent Research System, Developer Productivity with Claude, Claude Code for CI, Structured Data
Extraction. Har item ke liye: clue, root cause, strongest response, distractor's trap, reusable rule.
**Mock One:** independent 60-item/120-min mock.

## Week 13 — Mock Two + Readiness Decision

Supervised 60-item mock (2 hrs) + debrief (1 hr). **Panaversity readiness standard:** 80%+ on 2 mocks,
75%+ every domain, sab 4 projects complete, missed questions ka principle explain kar sako. (Yeh
Panaversity ka apna threshold hai — real exam 720-scaled cut score use karta hai, alag hai.)

---
[⬅ Overview](00-overview-and-entry-contract.md) · [Agla: FDE Practicum ➡](02-fde-practicum.md) · [⬆ Index](README.md)
