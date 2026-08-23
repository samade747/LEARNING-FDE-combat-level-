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

Yeh 7 titles abhi links nahi — jaise jaise live hote hain, link ban jayenge. Table ko **sequence** ki
tarah parho, menu ki tarah nahi.

Yeh sequence do exams ke liye sab se zyada matter karti hai:

- **Claude Code Configuration CCAR-F ka 20% hai** — Teams aur CI courses isay seedha address karenge
- **Applications and Integration CCDV-F ka 33.1% hai** — The Loop by Hand aur Structured Extraction us
  domain ka bara hissa cover karenge

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

### Weeks 1-2: Architect Foundations Blueprint Se Shuru Karo

PCAR-F/CCAR-F blueprint download karo, domain weight ke hisaab se time allocate karo — architecture is
pathway mein pehle aati hai. **Ek 33% domain ko roughly ek-tihai study time milna chahiye.** Phir
matching free Anthropic Academy courses use karo:

| Aapka Exam | Highest-Value Free Courses |
| --- | --- |
| CCAR-F | Building with the Claude API · MCP: Advanced Topics · Claude Code 101 · official docs (agents, context management, tool design) |
| CCDV-F | Building with the Claude API (84 lectures, backbone) · Introduction to MCP · Claude Code in Action · Introduction to agent skills · Introduction to subagents |
| CCAO-F | Claude 101 · AI Capabilities and Limitations · aapke role ke liye AI Fluency track |
| CCAR-P | CCAR-F row ki har cheez, plus Bedrock/Vertex AI agar cloud platform se deploy karte ho |

**Free training:** [Anthropic Academy](https://anthropic.skilljar.com/) — **Certification
registration:** [Partner Academy](https://anthropic-partners.skilljar.com/).

### Weeks 3-4: Developer Foundations + Kuch Banao

Developer Foundations material mein move karo aur **ek chhoti application banao** jo: API call kare,
kam se kam ek tool/MCP server use kare, prompt/context engineering apply kare, aur ek basic eval
include kare.

**Ek weekend project jo 5 domains touch kare, passive video ke 10 aur ghanton se zyada value deta
hai.** Scenario questions aasan ho jate hain jab aap trade-offs khud already bana chuke ho.

### Week 5: Practice — PCAR-F Pehle, PCDV-F Baad Mein

Free sample tests exam conditions mein do, apni weakest domains drill karo real attempt use karne se
pehle. Explanations use karo yeh samajhne ke liye ke **sahi trade-off sahi kyun hai.**

### Week 6: Panaversity Gate Complete Karo

Apni weakest domains dobara test karo, **PCAR-F pehle, phir PCDV-F.** Dono pass hone ke baad aur **FDE
Internship Program & partner access** milne ke baad, material fresh rakho aur **CCAR-F pehle, CCDV-F
baad** ki taraf move karo.

Poori sequence:

```
PCAR-F → PCDV-F → FDE Internship Program & partner access → CCAR-F → CCDV-F
```

**Jab tak practice results na batayein ke zaroorat hai, dobara scratch se study cycle shuru mat
karo.**

---
[⬅ Index](README.md) · [Peechay: Exam Domains](03-exam-domains.md) ·
[Agla: Registration, Costs, Mistakes ➡](05-registration-costs-mistakes.md)
