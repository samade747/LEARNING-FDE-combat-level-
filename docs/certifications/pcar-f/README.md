# PCAR-F — Panaversity Certified Architect: Foundations

*Source: book page **[`/docs/certifications/pcar-f`](https://agentfactory.panaversity.org/docs/certifications/pcar-f)**
(gen 61 pe PCAR-F ka apna dedicated page). Re-fetched 2026-09-02 (Zia Tutor corpus gen 61, book
"Version note": updated 1 September 2026). Yeh is repo ka **immediate goal** hai — dekho
[`../07-practice-log.md`](../07-practice-log.md).*

## ⚠️ Rollout (Gen 61)

**PCAR-F ka sample aur proctored exam dono "coming soon" — koi date nahi.** (PCAO-F: sample 10 Sep,
proctored 18 Sep 2026.) Interim rehearsal: book ka **CCAR-F Practice Exam** (`/docs/ccar-f-practice-exam`
— 60 items, 120 min, all 6 scenarios, per-domain scored). ⚠️ User ki 2026-10-05 deadline ab
seat-availability pe depend karti hai — risk analysis [`../07-practice-log.md`](../07-practice-log.md).

```
PCAO-F → PCAR-F → FDE Internship Program → (optional) CCAO-F → CCAR-F
```

## "Same Blueprint, One Level Up"

Book: PCAR-F **poora CCAR-F blueprint** (published weights pe) examine karta hai — **phir aage jaata
hai**, kyunki courses jaate hain: same judgment across vendors.

- **CCAR-F** ek vendor ke product surface ke andar architectural judgment test karta hai: Agent SDK
  hooks, `CLAUDE.md` hierarchy, plan mode, built-in tools.
- **PCAR-F** wahi + vendor-neutral half: "any coordinator handing work to any worker before that
  handoff is safe" kya hona chahiye; harness Claude Code nahi to standing instructions kahan; "who
  is accountable for the escalation that never happened".

> Book: *"A graduate stands in front of a customer who may run Claude, or may run something else, and
> has to be right either way."* **CCAR-F wo credential hai jo market recognise karta hai (Anthropic
> issued, koi bhi check kar sakta hai); PCAR-F uske neeche baith kar use hold karta hai.**

| | PCAR-F | CCAR-F |
| --- | --- | --- |
| Blueprint | Every CCAR-F domain at published weight, then vendor-neutral | The 5 published domains |
| Passing | 720 / 1000 | 720 / 1000 |
| Fee | Free (enrolled students, first 2 attempts) | $125 USD list price |
| Proctored by | Panaversity, independently | Pearson VUE, via Partner Academy |

## Quick Facts

| Field | Detail |
| --- | --- |
| **Full name** | Panaversity Certified Architect: Foundations |
| **Matches** | [CCAR-F](../ccar-f/README.md) — "launched March 2026, programme ka pehla exam" |
| **Role in path** | **Required second** ([PCAO-F](../pcao-f/README.md) ke baad) |
| **Proctored by** | Panaversity (independently) |
| **Pass score** | 720 / 1000 (scaled score, **72% nahi**) |
| **Cost** | Free — Panaversity students: 2 free attempts; 3rd+ fee TBA. Everyone else: proctoring fee TBA |
| **Unlocks** | Pass PCAO-F **+ PCAR-F** dono → Panaversity FDE Internship Program → (optional) CCAO-F → CCAR-F registration assist |
| **Partner tier** | **CCAR-F counts** toward Claude Partner Network tier eligibility; CCAO-F nahi |

## Domain Weights (CCAR-F Blueprint — Gen 61 Refined Names)

| Domain | Weight | Yeh Book Kahan Cover Karti Hai |
| --- | --- | --- |
| **Agentic Architecture & Orchestration** | **27%** | [Choosing Agentic Architectures](../../choosing-agentic-architectures-crash-course/README.md), [Loop Engineering](../../loop-engineering/README.md), [Harness Engineering](../../harness-engineering/README.md), [Graph Engineering](../../graph-engineering/README.md) + book ki *Claude Agent SDK* / *The Loop by Hand* |
| Claude Code Configuration & Workflows | 20% | [Claude Code and OpenCode](../../agentic-coding/README.md), [Plugins for AI Agents](../../plugins-crash-course/README.md) + book ki *Claude Code for Teams* / *CI Worker* |
| Prompt Engineering & Structured Output | 20% | [AI Prompting in 2026](../../ai-prompting-2026/README.md), [Spec-Driven Development](../../spec-driven-development/README.md) + book ki *Structured Extraction Pipelines* |
| Tool Design & MCP Integration | 18% | [Connector-Native Apps](../../connector-native-apps/README.md), Skills & Connectors, + *Claude Agent SDK* |
| Context Management & Reliability | 15% | [Building the Context Layer](../../context-layer-crash-course/README.md), [The Four Layers](../../four-layers/README.md), [RAG on Postgres](../../postgres-ai-crash-course/README.md) |

**Book ka #1 study advice:** *Build AI Agents with the Claude Agent SDK* 5 mein se 3 rows mein
appear karta hai — agar time kam hai, wahi. #2: Claude Code Config ka 20% (Teams + CI Worker;
"CI is where most candidates are thinnest").

Spread 15%–27% — **koi domain skip nahi, koi domain carry nahi karega.** Poori task-statement-level
detail (official CCAR-F Exam Guide v1.0 se, 2026-08-24) [CCAR-F folder](../ccar-f/README.md) mein —
PCAR-F **usi blueprint** pe based hai.

## 6 Published Production Scenarios (Exam Din 4 Draw Hote Hain)

1. **Customer Support Resolution Agent** — high-ambiguity support agent, custom MCP tools, kab escalate
2. **Code Generation with Claude Code** — generation/refactoring/debugging/docs, team workflow ke andar
3. **Multi-Agent Research System** — coordinator → search/analysis/synthesis/reporting subagents
4. **Developer Productivity with Claude** — unfamiliar codebase explore (built-in tools + MCP servers)
5. **Claude Code for Continuous Integration** — automated review + test-gen, false positives = dushman
6. **Structured Data Extraction** — unstructured docs → JSON-schema-validated extraction

*4 randomly draw hote hain, isliye ek weak domain aapke draw pe over-represented ho sakta hai.*

## CCAR-F Out-Of-Scope List (Guide Appendix — "Ek Study Week Bacha Deta Hai")

Fine-tuning · authentication & billing · MCP hosting/infrastructure · Constitutional AI & RLHF ·
embeddings & vector databases · computer use · vision · streaming · rate limits & pricing math ·
OAuth & key rotation · cloud-provider configuration · benchmarking · prompt-caching implementation ·
tokenization — **sab CCAR-F ke bahar.**

## Prep Resources

- **Interim rehearsal:** [CCAR-F Practice Exam](https://agentfactory.panaversity.org/docs/ccar-f-practice-exam) (book-hosted; 60 items, 120 min, all 6 scenarios, domain-scored, har answer explained) — **PCAR-F sample nahi**, score PCAR-F result nahi
- **Free sample test:** [flashgenius.net/sample-tests/ccar-f](https://flashgenius.net/sample-tests/ccar-f) (independent, not Anthropic-affiliated)
- **Free Anthropic Academy:** Building with the Claude API · MCP: Advanced Topics · Claude Code 101 · official docs (agents, context management, tool design)
- **Official blueprint authority:** [CCAR-F Exam Guide v1.0](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf)
- **Real-attempt rule:** samples pehle, real PCAR-F attempt exam-conditions practice ke baad hi — sirf 2 free attempts

## Practice Projects

PCAR-F **CCAR-F ke bilkul usi blueprint** par based hai — [CCAR-F ke 5 project scaffolds](../ccar-f/projects/README.md)
(agentic-loop, multi-tool-escalation, team-workflow, structured-extraction, multi-agent-research)
hi PCAR-F ki asal hands-on prep hain, sab offline pytest se tested. Book: *"Reading is not enough for
a scenario exam"* — ek chhota system banao jo API call kare, ek tool/MCP use kare, basic eval ho.

## Test Your Understanding

- [`05-test-your-understanding.md`](05-test-your-understanding.md) — 10 scenario-based questions
- [`quiz.md`](quiz.md) — same 10 questions, standalone self-test

## Is Repo Ka Apna Push

**Yeh wahi exam hai jo user ne 2026-10-05 tak pass karne ka target rakha hai.** Gen 61 pe date
uncertainty ki wajah se — prep deadline-ready rakho, sitting jab seat aaye. Week-by-week plan aur
live checklist: [`../07-practice-log.md`](../07-practice-log.md).

---
[⬅ Certifications Index](../README.md)
