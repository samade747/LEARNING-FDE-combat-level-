# 04 — Gaps + Six-Week Study Plan

## Claude-Specific Coverage Abhi Development Mein Hai

Ek **7-course Claude-specific sequence** design ho chuki hai jo missing platform material cover karegi
— abhi under development, progressively publish hogi.

| Missing Tha | Cover Karega (Under Development) |
| --- | --- |
| Messages API loop, `stop_reason`, tool results | **The Loop by Hand** |
| Structured output, schemas, Message Batches | **Structured Extraction Pipelines** |
| Claude Agent SDK | **Claude Agent SDK** |
| Claude Code configuration team-scale pe | **Claude Code for Teams** |
| Claude Code unattended, headless, CI mein | **Claude Code as a CI Worker** |
| Scheduled/event-driven Claude automation | **Claude Code Routines** |
| Anthropic ka hosted agent harness | **Claude Managed Agents** |

**28 Aug 2026 update — in mein se 5 exam-relevant hain, 2 nahi:**

| Course | Exam mein? |
| --- | --- |
| The Loop by Hand — agentic loop, `stop_reason`, tool results | ✅ CCAR-F (Agentic Architecture) |
| Structured Extraction Pipelines — schemas, validation/retry, batching | ✅ CCAR-F (Prompt Engineering) |
| Claude Agent SDK — subagents, hooks, permissions, escalation, context | ✅ CCAR-F (Agentic Architecture — 3 of 5 rows; sab se important single course) |
| Claude Code for Teams — `CLAUDE.md` scoping, path rules, skills, precedence | ✅ CCAR-F (Claude Code Config, 20%) |
| Claude Code as a CI Worker — headless, CI, pipeline output | ✅ CCAR-F (Claude Code Config) |
| **Claude Code Routines** | ❌ har current blueprint se bahar — "for the work, not the exam" |
| **Claude Managed Agents** | ❌ har current blueprint se bahar — "for the work, not the exam" |

Agar aap date ke against study kar rahe ho, aakhri 2 skip karo.

- **Claude Code Configuration CCAR-F ka 20% hai** — Teams aur CI courses wahan rehta hai
- **CCAO-F ka product-terminology gap:** exam Claude features (Projects, Artifacts, research mode,
  connectors, model types, context/memory behaviour) ko Anthropic ki apni exact vocabulary mein
  naam se poochta hai — ideas aap already jante ho, terminology alag job hai (dekho gap #3)

## 3 Narrower Gaps Jo Sequence Ke Baad Bhi Rahenge

1. **Claude model-selection economics** — current Opus/Sonnet/Haiku trade-offs (quality, latency,
   price), token budgeting, prompt caching + batch pricing ka effect. **Model Selection and
   Optimization CCDV-F ka 16.8% hai.**
2. **Baaqi Messages API surface** — The Loop by Hand loop aur `stop_reason` handling cover karega,
   lekin **vision/multimodal input, extended thinking, prompt-caching mechanics, ya Bedrock/Vertex/
   Foundry ka provider-specific behavior abhi book mein nahi hai.**
3. **Anthropic ka product surface, Anthropic ki apni language mein** — sab se zyada **CCAO-F** ke liye
   matter karta hai. Exam claude.ai features (Projects, Artifacts, research mode, connectors, custom
   instructions) ko naam se poochta hai. Book yeh capabilities sikhati hai, lekin aksar open-source
   alternatives ke sath — **exam se pehle Anthropic ki exact product terminology seekho.**

In teenon gaps ke liye, neeche wale free Anthropic Academy courses sab se fast supplement hain.

## Free Six-Week Study Plan

6 hafte, **5-8 ghante/week**. Book aur neeche wale Academy courses dono free hain.

### Weeks 1-2: Associate Foundations Blueprint Se Shuru Karo

**PCAO-F/CCAO-F blueprint** ke areas pehle: prompting, output evaluation + validation, workflow
integration, governance + responsible use, Claude product capabilities, troubleshooting, aur
appropriate human review. **Isay vocabulary exam ki tarah mat treat karo** — sab se bare Associate
domains judgment reward karte hain: kya aap ek weak answer spot kar sakte ho, validate kar sakte ho,
decide kar sakte ho kab verification chahiye, aur Claude ko real workflow ke andar sahi jagah rakh
sakte ho? Phir matching free Anthropic Academy courses:

| Aapka Exam | Highest-Value Free Courses |
| --- | --- |
| CCAO-F | Claude 101 · AI Capabilities and Limitations · aapke role ke liye AI Fluency track |
| CCAR-F | Building with the Claude API · MCP: Advanced Topics · Claude Code 101 · official docs (agents, context management, tool design) |
| CCDV-F (optional next) | Building with the Claude API · Introduction to MCP · Claude Code in Action · Introduction to agent skills · Introduction to subagents |
| CCAR-P (advanced) | CCAR-F row + Bedrock/Vertex AI agar cloud se deploy karte ho |

**Free training:** [Anthropic Academy](https://anthropic.skilljar.com/) — **Certification
registration:** [Partner Academy](https://anthropic-partners.skilljar.com/).

### Weeks 3-4: Architect Foundations + Kuch Banao

Architect Foundations mein move karo: agentic architecture, Claude Code configuration, prompt
engineering, tools/MCP, context management. **Ek chhoti application banao** jo: API call kare, kam se
kam ek tool/MCP server use kare, prompt/context engineering apply kare, aur ek basic eval include kare.

**Ek weekend project jo kai domains touch kare, passive video ke 10 aur ghanton se zyada value deta
hai.** Scenario questions aasan ho jate hain jab aap trade-offs khud already bana chuke ho.

### Week 5: Practice — PCAO-F Pehle, PCAR-F Baad Mein

Free sample tests exam conditions mein do, apni weakest domains drill karo real attempt use karne se
pehle. Explanations use karo yeh samajhne ke liye ke **sahi trade-off sahi kyun hai.**

### Week 6: Panaversity Gate Complete Karo

Apni weakest domains dobara test karo, **PCAO-F pehle, phir PCAR-F.** Dono pass hone ke baad aur **FDE
Internship Program & partner access** milne ke baad, material fresh rakho aur **CCAO-F pehle, CCAR-F
baad** ki taraf move karo.

Poori sequence:

```
PCAO-F → PCAR-F → FDE Internship Program & partner access → CCAO-F → CCAR-F
```

**Jab tak practice results na batayein ke zaroorat hai, dobara scratch se study cycle shuru mat
karo.**

---
[⬅ Index](README.md) · [Peechay: Exam Domains](03-exam-domains.md) ·
[Agla: Registration, Costs, Mistakes ➡](05-registration-costs-mistakes.md)
