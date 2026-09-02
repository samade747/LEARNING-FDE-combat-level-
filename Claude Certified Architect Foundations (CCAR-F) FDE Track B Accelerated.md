# Forward Deployed Engineer Training — Track B: Accelerated

## One-Quarter Syllabus (13 Weeks) Preparing for PCAR-F and CCAR-F

**Accuracy checked:** 26 August 2026. Re-check the sources-of-truth section before each cohort because certification and product details can change.

### At a glance

| | Track B |
| --- | --- |
| Audience | Learners with computing and basic AI experience |
| Duration | 13 weeks |
| Instructor-led time | 4.5 hours/week: 3-hour architect class + 1.5-hour FDE practicum |
| Contact hours | 58.5 |
| Guided practice | 5–7 hours/week |
| Typical weekly commitment | **10–12 hours minimum; 12–15 in project/capstone weeks** |
| Estimated total effort | About **120–150 hours** |
| Role trained | Vertical Forward Deployed Engineer (FDE) |
| Certification focus | **PCAR-F / CCAR-F — Architect Foundations** |
| Primary text | *The AI Agent Factory* + five required Claude courses |

### Entry contract

Track B is for learners who are **new to Claude architecture, not new to computing**. Before Week 1, a student can:

- work from a terminal and navigate files/folders,
- use Git at a basic level,
- read simple Python,
- explain an API request/response,
- prompt an AI assistant with structure and intent, and
- use Claude Code or another coding agent at beginner level, including first exposure to plan mode.

If only the Python requirement is missing, complete *Python in the AI Era* before the quarter. If only Claude Code is missing, complete the *Agentic Coding Crash Course* first. Students missing more than two entry items should take Track A.

### What students finish with

By the end of the quarter, a successful student has:

- four CCAR-F-aligned architect projects,
- a deployed Vertical System of Record,
- practice across all six official CCAR-F scenarios,
- a trade-off notebook showing architectural reasoning, and
- two full-length mock results used for the PCAR-F readiness decision.

Track B compresses experience through required building. It is intentionally demanding. Track A reaches the same architect destination at a more forgiving pace.

## Purpose

A Forward Deployed Engineer works inside a customer's business to understand real operating constraints, design agentic systems, and make those systems reliable. The certification is evidence of that judgment, not a replacement for it.

Track B therefore combines certification preparation with a practicum that produces a governed Vertical System of Record. The architect and practicum strands connect in Week 11, when the student's support agent consumes their own governed knowledge.

### CCAR-F exam facts used by this syllabus

This syllabus follows the **Claude Certified Architect – Foundations Exam Guide, Version 1.0, effective July 2026**.

| Item | Current guide |
| --- | --- |
| Exam code | **CCAR-F** |
| Items | **60** |
| Item types | Multiple-choice and multiple-response |
| Structure | **4 scenarios drawn from a bank of 6** |
| Time | **120 minutes** |
| Passing score | **720 scaled**, on a 100–1,000 scale |
| Delivery | Proctored; online and/or test centre according to programme policy |
| Typical candidate | About **6+ months of practical Claude experience** |

The guide describes the *typical* candidate; it does not make six months a formal prerequisite. The purpose of these tracks is to build the practical judgment the exam expects.

Because **PCAR-F is Panaversity's exam aligned to the CCAR-F blueprint**, the architect strand uses the official CCAR-F domain and task-statement numbering throughout.

### Exam blueprint

| Domain | Weight |
| --- | ---: |
| 1. Agentic Architecture and Orchestration | **27%** |
| 2. Tool Design and MCP Integration | **18%** |
| 3. Claude Code Configuration and Workflows | **20%** |
| 4. Prompt Engineering and Structured Output | **20%** |
| 5. Context Management and Reliability | **15%** |
| **Total** | **100%** |

## Two Scopes in One Programme

The programme deliberately combines two related scopes:

- **Architect / certification scope:** the Claude architecture, tooling, prompting, context, and reliability knowledge mapped to the current CCAR-F blueprint.
- **FDE formation scope:** the Vertical SoR practicum, including KSoR, Fumadocs, deployment, and current stateless-MCP implementation work.

Do not confuse the two. The practicum makes the learner a stronger FDE, but not every practicum topic is tested on CCAR-F. For example, the current exam guide explicitly places MCP hosting/infrastructure details outside the exam scope.

## Weekly Delivery Model

### Architect class: 3 hours

Each teaching week uses the same rhythm:

1. **60 minutes — concepts and architecture.** In the architect quarter, every major concept is tied to the CCAR-F blueprint.
2. **90 minutes — guided lab.** Students build, break, diagnose, or redesign a system. Many exam distractors are plausible approaches that fail under pressure, so students see those failures rather than only hearing about them.
3. **30 minutes — scenario practice.** Students answer 10–15 scenario-style items and explain:
   - why the selected answer is best,
   - why the alternatives are weaker, and
   - which architectural principle the item is testing.

### FDE practicum: 1.5 hours

The practicum builds a **Vertical System of Record (SoR)**: governed knowledge published to a human-readable surface and an agent-readable MCP surface. The architect strand teaches how agents consume knowledge and tools; the practicum builds the governed knowledge and tools worth consuming.

### Trade-off notebook

Every architect lab ends with three short answers:

1. What trade-off did I face?
2. What did I choose?
3. Why were the plausible alternatives worse here?

This is graded. It practices the reasoning the certification exam demands across its scenario items.

## Architecture Decision Framework

Students use this framework from the start of the architect quarter. It is a set of defaults, not a substitute for reading the scenario.

- **Required behaviour** → deterministic control: code, hooks, permissions, gates, validation.
- **Preferred behaviour** → prompt guidance.
- **Fixed, predictable stages** → workflow or prompt chaining.
- **Unknown next steps** → adaptive agent.
- **Independent work that can proceed separately** → parallel subagents.
- **Large or attention-heavy work** → decomposition and focused passes.
- **Tool-selection failure** → inspect names, descriptions, schemas, and scope before adding routing complexity.
- **Expensive mistakes** → add an explicit human-review or approval boundary.
- **Failure diagnosis** → fix the root cause, not the visible symptom.
- **Every tool grant** → least privilege.

## Architect Class — Week by Week

### Week 1: Foundations Sprint and Thinking Like a Claude Architect

This is the only architect week that differs from Track A. It verifies the entry contract and installs the decision framework at speed.

- **Read before class:** *The Roles This Book Trains* · *The FDE AF Model* · *Agentic Coding Crash Course* (review) · *The Four Layers* · *Is This an Agent Problem?* · *Choosing Agentic Architectures*
- **Hour 1 — verify the entry skills:** send one raw Claude Messages API request from Python and explain the response; complete one Claude Code task and defend plan mode versus direct execution.
- **Hour 2 — architecture:** architecture versus implementation; deterministic versus probabilistic behaviour; workflow versus agent; root cause versus symptom.
- **Hour 3 — classification lab:** classify six business problems as a direct call, workflow, single agent, multi-agent system, Claude Code workflow, or human-agent workflow. Name the enforcement mechanism and failure mode for each.
- **Notebook:** the problem you almost classified incorrectly, and the clue that corrected you.

From **Week 2 onward**, the Track B architect content is the same as Track A Weeks 15–26.

### Week 2: The Agentic Loop by Hand

- **Required course:** *The Loop by Hand*
- **Exam mapping:** Task 1.1; `tool_choice` concepts used in Tasks 2.3 and 4.3
- **Learn:** Messages API statelessness; content blocks; `stop_reason`; `tool_use`; `tool_result`; `tool_use_id`; `end_turn`; parallel tool calls; `tool_choice` as `auto`, `any`, or a forced tool.
- **Decision rule:** use the protocol's control signals. Do not infer completion by parsing prose or by checking whether a response happens to contain text.
- **Lab / Project 1:** build a two-tool agentic loop with no agent framework. The instructor introduces missing history, a lost tool result, incorrect stop handling, repeated tool calls, and premature termination. Students diagnose each failure from its symptoms.
- **Homework:** explain what the Claude Agent SDK will now do for you that you just implemented by hand.

### Week 3: Claude Agent SDK I — Tools, Permissions, and MCP

- **Required course:** *Claude Agent SDK*, Parts 1–2
- **Exam mapping:** Tasks 2.1, 2.2, 2.3, 2.5
- **Learn:** Agent SDK versus raw client loop; sessions; built-in tools; Grep versus Glob; Edit versus Read+Write; tool scope; permissions; MCP tools; structured tool errors.
- **Tool design:** Claude chooses tools from the full tool definition and surrounding context. **Detailed descriptions are one of the strongest routing signals**, so descriptions must state what the tool does, its inputs and outputs, when to use it, and when not to use it.
- **Error design:** distinguish transient, validation, business, and permission failures. A successful empty result is different from an access failure.
- **Exam/live terminology bridge:** Claude API tool results use `is_error`; MCP and the CCAR-F guide use `isError` in their respective contexts.
- **Lab:** create two deliberately overlapping tools, measure misrouting across 20 prompts, then improve the descriptions. If ambiguity remains, repair the interface by renaming, splitting, or consolidating tools as appropriate.

### Week 4: Claude Agent SDK II — Multi-Agent Architecture

- **Required course:** *Claude Agent SDK*, orchestration section
- **Exam mapping:** Tasks 1.2, 1.3, 1.6
- **Learn:** coordinator-subagent architecture; task decomposition; explicit context passing; parallel delegation; scoped tools; prompt chaining versus adaptive decomposition; gap detection and re-delegation.
- **Context rule:** subagents do not inherit the parent conversation automatically. Pass the context they need explicitly.
- **Exam snapshot note:** CCAR-F v1.0 refers to the delegation tool as **`Task`** and tests `allowedTools` accordingly. Live SDK naming can change; students should know the exam terminology and verify the installed SDK when building.
- **Lab:** reproduce the guide's “creative industries” failure, where a narrow decomposition covers only visual arts. Repair the decomposition, then add a narrowly scoped `verify_fact` capability for simple verification.

### Week 5: Claude Agent SDK III — Trust, Hooks, Sessions, and Context

- **Required course:** *Claude Agent SDK*, enforcement and context sections
- **Exam mapping:** Tasks 1.4, 1.5, 1.7, 5.1, 5.2
- **Core rule:** if a business invariant **must not be violated**, do not rely on prompt wording alone. Enforce it in code, permissions, or hooks.
- **Learn:** prerequisite gates; `PreToolUse` and `PostToolUse`; output normalization; approval boundaries; structured human handoffs; explicit escalation criteria; session resume and fork; stale context versus a fresh summary; persistent case-facts blocks.
- **Escalation:** escalate on an explicit request for a human, a policy gap/exception, or inability to make meaningful progress. Sentiment and self-reported model confidence are not reliable substitutes.
- **Lab / Project 2:** build the governed customer-support agent with four well-described tools, structured errors, programmatic refund controls, explicit escalation rules, and persistent case facts. Test it adversarially.

### Week 6: Claude Code Architecture and Iterative Refinement

- **Read:** *Agentic Coding Crash Course* and *Spec-Driven Development*, revisited at architect depth
- **Exam mapping:** Tasks 3.4 and 3.5
- **Plan versus direct:** use direct execution for small, well-understood, isolated changes. Use plan mode for architectural, multi-file, uncertain, or multi-approach work. Use an Explore subagent when verbose discovery should stay out of the main context.
- **Refinement techniques:** 2–4 targeted examples when prose is interpreted inconsistently; test-driven iteration using concrete failures; the interview pattern before building in an unfamiliar domain; interacting issues together and independent issues separately.
- **Lab:** solve one task with each refinement technique and compare the before/after result. Include one large-codebase exploration using a subagent and a scratchpad.

### Week 7: Claude Code for Teams

- **Required course:** *Claude Code for Teams*
- **Exam mapping:** Tasks 3.1, 3.2, 3.3
- **Learn:** managed, user, project, and local instruction scopes; nested/directory `CLAUDE.md`; `@import`; `.claude/rules/` with `paths` globs; `/memory`; skills; project versus user MCP configuration; environment-variable expansion.
- **Current Claude Code:** `allowed-tools` in a skill **pre-approves** listed tools; it does not by itself remove every other tool. Use permission deny rules or other enforcement when you need restriction.
- **Exam snapshot:** CCAR-F v1.0 uses both “custom commands” and “skills” terminology. Current Claude Code has converged custom command files and skills into the same slash-command experience, while older `.claude/commands/` files remain supported.
- **Lab:** diagnose a team rule placed in the wrong scope, move it to a repository-shared scope, and verify from a clean clone. Then run a `context: fork` skill and confirm the work stays isolated from the main conversation.

### Week 8: Claude Code as a CI Worker

- **Required course:** *Claude Code as a CI Worker*
- **Exam mapping:** Tasks 3.6, 4.1, 4.6; Scenario 5
- **Learn:** non-interactive `-p/--print`; exit codes; explicit permissions; `--bare`; `--output-format json`; `--json-schema`; bounded runs; reusable review criteria; prior-finding suppression.
- **Review architecture:** code generation and code review should use independent contexts. A fresh reviewer is better positioned to challenge assumptions made during generation.
- **Prompt quality:** explicit categories and severity rules beat vague instructions such as “be conservative” or “report only high-confidence issues.”
- **Lab:** run a pull-request review in CI and return schema-validated findings. Introduce three failures intentionally and record the observable symptom and repair.

### Week 9: Structured Output and Reliable Extraction

- **Required course:** *Structured Extraction Pipelines*, Parts 1–2
- **Exam mapping:** Tasks 4.2 and 4.3
- **Current API:** `output_config.format` provides schema-constrained structured output for successful responses. Students still check stop conditions such as refusal or truncation before parsing.
- **CCAR-F v1.0 snapshot:** the exam frames Task 4.3 through `tool_use` + JSON Schema and `tool_choice` (`auto`, `any`, forced tool). Students learn both the current API surface and the exam snapshot.
- **Schema design:** required versus nullable; `other` + detail; `unclear`; field descriptions; syntax validity versus semantic correctness.
- **Few-shot prompting:** use 2–4 targeted examples when they clarify decision boundaries, exact format, ambiguous cases, or varied document structures.
- **Lab / Project 3 begins:** design an extraction schema and test it against documents with missing, ambiguous, and out-of-enum information. The correct result for absent information is `null`, not an invented value.

### Week 10: Validation, Human Review, and Batch

- **Required course:** *Structured Extraction Pipelines*, Parts 3–4
- **Exam mapping:** Tasks 4.4, 4.5, 5.5
- **Learn:** semantic validation; `calculated_total` versus `stated_total`; `conflict_detected`; targeted retry with the original source, failed extraction, and specific validation error; when retries cannot help.
- **Batch design:** Message Batches provide a 50% cost reduction for suitable workloads, can take up to 24 hours with no latency SLA, use `custom_id` for correlation, and do not support a multi-turn tool loop inside one batch request.
- **Human review:** calibrate field-level confidence against labelled data; segment accuracy by document type and field; use stratified sampling so a strong aggregate score does not hide a weak segment.
- **Lab / Project 3 completed:** finish the structured extraction pipeline, including validation, selective retry/resubmission, batch handling, and confidence-routed review.

### Week 11: Context, Reliability, and Provenance

- **Read:** *Building the Context Layer*, *The Four Layers* (revisited), and the Agent SDK context/provenance material
- **Exam mapping:** Tasks 5.1, 5.3, 5.4, 5.6
- **Learn:** progressive summarization; lost-in-the-middle effects; key-facts blocks; trimming verbose tool results; scratchpads; manifests and crash recovery; structured error propagation; partial results; claim-source mappings; publication dates; conflict annotation and coverage gaps.
- **Reliability rule:** an access failure is not a valid empty result. Preserve what succeeded, report what failed, and give the coordinator enough structured context to decide whether to retry, reroute, or continue with a documented gap.
- **Lab / Project 4:** build the multi-agent research system with parallel subagents, structured provenance, a simulated timeout with partial results, and conflicting credible sources preserved with attribution and dates.

### Week 12: Six-Scenario Architecture Workshop and Mock One

The class works inside the six official scenario frames:

1. Customer Support Resolution Agent
2. Code Generation with Claude Code
3. Multi-Agent Research System
4. Developer Productivity with Claude
5. Claude Code for Continuous Integration
6. Structured Data Extraction

For every item, students identify:

- the clue in the scenario that matters,
- the root cause,
- the strongest architectural response,
- the distractor's trap, and
- the reusable decision rule.

**Mock One:** a full 60-item, 120-minute mock is completed independently after the workshop under exam discipline. Students bring overall and per-domain results to Week 13.

### Week 13: Mock Two, Debrief, and Readiness Decision

- **Hours 1–2:** supervised full-length mock: 60 items, four scenarios, 120 minutes, no notes.
- **Hour 3:** debrief both mocks by domain and by decision pattern. Build a remediation plan for any weak objective.
- **Internal readiness standard:** Panaversity endorses a PCAR-F booking when the student:
  - scores **80%+ on two different full-length mocks**,
  - scores **75%+ in every domain**,
  - completes all four required projects, and
  - can explain the architectural principle behind missed questions.
- **Important:** these percentages are Panaversity readiness thresholds, not conversions of Anthropic's scaled score. The real exam applies its own **720 scaled** passing score.
- **Next step:** take the free sample test before using a PCAR-F attempt, then follow the Panaversity access pathway described in this syllabus.

## Four Required Architect Projects

| Project | Track B week | Official preparation exercise alignment |
| --- | ---: | --- |
| **1. Agentic loop, no framework** | 2 | Loop-control foundation used by Exercise 1 |
| **2. Governed customer-support agent** | 5 | Exercise 1 — Multi-Tool Agent with Escalation Logic |
| **3. Structured extraction pipeline** | 10 | Exercise 3 — Structured Data Extraction Pipeline |
| **4. Multi-agent research system** | 11 | Exercise 4 — Multi-Agent Research Pipeline |

The official team-development configuration exercise is completed as the **Week 7 lab**, aligning to **Preparation Exercise 2**.

## FDE Practicum — Building a Vertical System of Record

### What students build

Every student leaves the quarter with a working **Vertical System of Record** in a chosen domain: one governed knowledge corpus with a human-readable projection and an agent-readable MCP projection.

### Technology baseline

- **KSoR:** governed knowledge framework; `docs/status.md` is the implementation authority.
- **Human projection:** KSoR's reference site uses **Next.js + Fumadocs** and supports static export.
- **Agent projection:** **MCP revision 2026-07-28**, including the stateless protocol core and MRTR.
- **Environment:** **Node.js 24+**, **pnpm**, and `uv`.

KSoR is evolving. Check `docs/status.md` before each KSoR module. Use shipped `ksor` commands when they exist; otherwise build the relevant surface directly in the published project structure. Do not teach a designed command as implemented.

### Practicum week by week

**P1 — FDE, SoR Thesis, and Setup.** Read *The FDE AF Model* and *System of Record*. Define why the durable product is governed knowledge rather than a chatbot. List three candidate verticals. Install Node.js 24+, pnpm, and `uv`.

**P2 — Choose the Vertical.** Apply knowledge intensity, regulatory weight, source availability, willingness to pay, and personal access. Commit to one vertical and begin the source register.

**P3 — Design the Vertical SoR.** Define scope, ownership, authoritative sources, conflict handling, review process, and the knowledge boundary. Open the decisions log and write the abstention policy.

**P4 — Fumadocs I: Corpus to Site.** Build the KSoR human projection with Claude Code. Convert the first three real source documents into reviewed Markdown with provenance.

**P5 — Fumadocs II: Structure and Deploy.** Add hierarchy, navigation, search, and a static deployment. **Milestone 1:** live human surface with at least five governed documents.

**P6 — Stateless MCP I.** Learn the 2026-07-28 stateless core: no `initialize/initialized` handshake or protocol-level session; per-request metadata; optional `server/discover`; standard HTTP scaling. Build and inspect one tool call.

**P7 — Stateless MCP II: Schemas and MRTR.** Trace schema conversion from Pydantic/Zod. Implement `input_required` with `inputRequests`, opaque `requestState`, and `inputResponses`. Treat `requestState` as untrusted and make the handler re-entrant.

**P8 — Agent Surface, Hand-Built.** Build search, retrieve, and cited-answer tools over the governed corpus. Enforce the knowledge boundary in application logic. **Milestone 2:** working MCP agent surface.

**P9 — KSoR I: One Source, Multiple Projections.** Adopt the current KSoR structure: `knowledge/`, `instance.md`, `system/site/`, `.agents/`. Derive human and agent projections from the same governed corpus.

**P10 — KSoR II: Governance and Provenance.** Implement the knowledge lifecycle and build provenance so a deployed answer can be traced back to a corpus version and reviewed source.

**P11 — KSoR III: Proving Behaviour.** Build a three-class evaluation set: answerable with citation; requires governed rule + operational fact; outside boundary → abstain. Connect Project 2's support agent to the SoR. **Milestone 3:** governed KSoR + evaluation set.

**P12 — Capstone Sprint.** Deepen the corpus, fix evaluation failures at the correct layer, polish both projections, and finish the architecture brief.

**P13 — Demo Day.** Demonstrate a governed answer with source trace, a correct abstention, an MRTR interaction, and the decisions log. **Milestone 4:** capstone Vertical SoR.

### Practicum milestones

| Milestone | Week | Evidence |
| --- | --- | --- |
| 1. Live human surface | P5 | Deployed site; 5+ governed documents with provenance |
| 2. Working agent surface | P8 | Stateless MCP search/retrieve/cite interface |
| 3. Governed KSoR + evaluation | P11 | Decisions log + three-class evaluation |
| 4. Capstone Vertical SoR | P13 | Demo + brief + repository |

## Assessment

The final grade is **70% architect strand / 30% practicum**.

### Architect strand — 70%

| Component | Weight |
| --- | ---: |
| Scenario practice | 7% |
| Projects 1–4 | 28% |
| Mock One (Week 12, independent) | 7% |
| Mock Two (Week 13, supervised) | 21% |
| Trade-off notebook | 7% |
| **Architect subtotal** | **70%** |

### Practicum — 30%

| Component | Weight |
| --- | ---: |
| Milestones 1–2 | 10% |
| Milestone 3 — governed KSoR + evaluation | 8% |
| Capstone / Milestone 4 | 12% |
| **Practicum subtotal** | **30%** |

The Vertical SoR is the programme's primary portfolio artifact for FDE Internship review.

## Certification Path and Sources of Truth

### Panaversity route to the official Anthropic exams

This syllabus prepares the **Architect Foundations** content.

> ⚠️ **Route updated 2026-09-02** against the Agent Factory certifications section (Zia Tutor MCP,
> corpus generation 61, book "Version note": updated 1 September 2026). The original route line below
> (written 26 Aug 2026) is superseded.

**Current route:** **PCAO-F → PCAR-F → FDE Internship Program → *(optional)* CCAO-F → CCAR-F**

~~Original (26 Aug 2026, stale): Track B → PCAR-F → PCDV-F preparation → pass PCDV-F → FDE Internship
Program + partner access → CCAR-F → CCDV-F~~

Important distinctions:

- **PCAO-F and PCAR-F are Panaversity requirements for this route, not Anthropic prerequisites.**
  **PCAO-F (Associate) now comes first** — it establishes the judgment/evaluation/governance
  foundation; PCAR-F (Architect) builds system design on top of it.
- **PCDV-F is no longer part of the FDE gate** — it is an "additional technical credential" taken
  after the pair, if deeper build/ship proof is wanted.
- **Stage Two (the Anthropic exams) is now explicitly optional.** The book: *"Sitting the Anthropic
  exams is optional… The Panaversity credentials and the internship stand on their own."* Panaversity
  assists internship participants with registration.
- This syllabus prepares **PCAR-F/CCAR-F architecture content**. It does **not** prepare the
  **PCAO-F** associate exam's judgment/evaluation focus — prepare that separately (Agent Factory
  `/docs/certifications/pcao-f`, or `docs/certifications/pcao-f/` in this repo).
- Each Panaversity exam is now **"same blueprint, one level up"**: the full matching Anthropic
  blueprint at published weights, then additional vendor-neutral / professional coverage.
- **Rollout (gen 61):** PCAO-F sample 10 Sep 2026, proctored 18 Sep 2026; **PCAR-F sample and
  proctored exam are "coming soon" with no date yet** — interim rehearsal is the book's CCAR-F
  Practice Exam.
- Vertical specialization begins during this practicum and deepens during internship; it does not
  start only after certification.
- Claude Certification Program registration requires an **eligible organisational account** (personal
  email not accepted); registration begins in Anthropic Partner Academy.

### Sources of truth

| Topic | Authority |
| --- | --- |
| CCAR-F blueprint, format, task statements | **Claude Certified Architect – Foundations Exam Guide, v1.0 (July 2026)** |
| Anthropic scheduling/retakes/Partner Academy route | **Pearson VUE Claude Certification Program page** |
| Panaversity qualification sequence, attempts, per-exam rollout dates | **Agent Factory certifications section** — per-exam pages `/docs/certifications/{pcao-f,pcar-f,pcar-p,pcdv-f}` (Zia Tutor MCP, gen 61) |
| MCP protocol | **Model Context Protocol specification 2026-07-28** |
| KSoR shipped functionality | **`panaversity/ksor` → `docs/status.md`** |
| KSoR runtime requirement | Current KSoR README/status |
| Fumadocs runtime/setup | **fumadocs.dev** |

**Version discipline:** re-check the current CCAR-F guide, Pearson programme page, KSoR status, MCP specification, and Fumadocs requirements before each cohort. Product and certification details can change.
