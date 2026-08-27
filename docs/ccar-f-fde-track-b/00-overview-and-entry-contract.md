# 00 — Overview + Entry Contract

## Kya Hai Yeh

**Track B** Panaversity ka **accelerated** (13-week) FDE syllabus hai, **Track A** ke muqable mein
tez. Dono ka destination same hai — **Vertical Forward Deployed Engineer (FDE)**, **PCAR-F/CCAR-F**
certification-ready — lekin Track B zyada demanding hai (10-15 hrs/week) kyunki poora syllabus 13
hafton mein compress hota hai.

| | Track B |
| --- | --- |
| Audience | Computing + basic AI experience wale learners |
| Duration | 13 weeks |
| Instructor-led time | 4.5 hrs/week (3-hr architect class + 1.5-hr FDE practicum) |
| Guided practice | 5-7 hrs/week |
| Total commitment | 10-15 hrs/week, ~120-150 hrs total |
| Certification focus | **PCAR-F / CCAR-F — Architect Foundations** |
| Primary text | *The AI Agent Factory* + 5 required Claude courses |

## Entry Contract — Week 1 Se Pehle Yeh Aana Chahiye

- Terminal se kaam, files/folders navigate karna
- Git basic level
- Simple Python parhna
- API request/response explain karna
- Structured prompting
- Claude Code (ya OpenCode) beginner level, plan mode ka first exposure

Agar sirf Python missing hai → *Python in the AI Era* pehle complete karo. Agar sirf Claude Code missing
hai → *Agentic Coding Crash Course* pehle. 2 se zyada items missing hon to Track A behtar hai.

## Quarter Ke End Tak Kya Milta Hai

- 4 CCAR-F-aligned architect projects
- Ek deployed Vertical System of Record
- Practice across sab 6 official CCAR-F scenarios
- Trade-off notebook (architectural reasoning ka record)
- 2 full-length mock results (PCAR-F readiness decision ke liye)

## Purpose — Architect + Practicum Kyun Sath

FDE customer ke andar kaam karta hai — real operating constraints samajhta hai, agentic systems design
karta hai, unhe reliable banata hai. Certification is judgment ka **evidence** hai, replacement nahi.

Isliye Track B do strands combine karta hai:
- **Architect / certification scope:** CCAR-F blueprint (architecture, tooling, prompting, context,
  reliability)
- **FDE formation scope:** Vertical SoR practicum (KSoR, Fumadocs, deployment, stateless MCP)

Dono confuse mat karo — practicum se FDE stronger banta hai, lekin har practicum topic exam par nahi
aata (jaise MCP hosting/infra detail CCAR-F scope se bahar hai, exam guide khud yeh kehti hai).

## Har Hafte Ka Rhythm

**Architect class (3 hrs):** 60 min concepts+architecture → 90 min guided lab (build/break/diagnose) →
30 min scenario practice (10-15 scenario items, "sahi jawab kyun, alternatives kyun kamzor, konsa
principle test ho raha hai")

**FDE practicum (1.5 hrs):** Vertical SoR banana — governed knowledge, human-readable + agent-readable
(MCP) surface dono

**Trade-off notebook:** har lab ke baad 3 sawal — kya trade-off tha, kya choose kiya, plausible
alternatives yahan kamzor kyun thay. Yeh graded hai, aur exact wahi reasoning practice karta hai jo exam
ke scenario items maangte hain.

## Architecture Decision Framework (Puri Quarter Mein Use Hota Hai)

| Situation | Default |
| --- | --- |
| Required behaviour | Deterministic control: code, hooks, permissions, gates, validation |
| Preferred behaviour | Prompt guidance |
| Fixed, predictable stages | Workflow / prompt chaining |
| Unknown next steps | Adaptive agent |
| Independent parallel work | Parallel subagents |
| Large/attention-heavy work | Decomposition + focused passes |
| Tool-selection failure | Pehle names/descriptions/schemas/scope inspect karo, tab routing complexity mat badhao |
| Expensive mistakes | Explicit human-review/approval boundary |
| Failure diagnosis | Root cause fix karo, symptom nahi |
| Har tool grant | Least privilege |

Yeh table [[harness-engineering]] ke "constrain" verb aur [[loop-engineering]] ke architecture choices
se directly overlap karti hai — Track B isi framework ko CCAR-F ki apni scenario-language mein serve
karti hai.

---
[⬅ Index](README.md) · [Agla: Architect Strand ➡](01-architect-strand.md)
