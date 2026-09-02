# 07 — Practice Log (Meri Apni PCAR-F Push)

*Yeh file baaqi files se alag hai. Woh files batati hain **"exam kya hai, kaise structured hai"**. Yeh
file record karti hai **"maine khud kya kiya"** — apna prep, week-by-week, checkbox ke sath. Isi
pattern par jo [Loop Engineering](../loop-engineering/11-practice-log.md) aur
[Harness Engineering](../harness-engineering/11-practice-log.md) ki practice logs mein use hua.*

**Goal (2026-08-24 ko set hua):** 2026-10-05 tak **PCAR-F** (free Panaversity internal exam) pass
karo — FDE path ka concrete step.

> ⚠️ **Path change (2026-09-01, gen 47):** pathway restructure — **PCAO-F PEHLE, phir PCAR-F**
> (do exams, ek nahi). PCDV-F/CCDV-F gate se hat gaye.
> `PCAO-F → PCAR-F → FDE Internship Program → (optional) CCAO-F → CCAR-F`
>
> ⚠️⚠️ **Timing constraint (2026-09-02, gen 61):** book ne PCAO-F ke **live dates** publish kiye:
> - **PCAO-F sample: 10 September 2026**
> - **PCAO-F proctored exam: 18 September 2026 se live**
> - **PCAR-F: sample aur proctored dono "coming soon" — koi date nahi**
>
> **2026-10-05 deadline ab realistically at-risk hai.** PCAR-F ke liYa to seat 5 Oct se pehle
> available ho jaye (uncertain), ya deadline slip kare. Neeche risk analysis.

### Deadline Risk Analysis (2026-09-02)

| Scenario | PCAR-F seat by ~1 Oct? | Deadline outcome |
| --- | --- | --- |
| **A — both live in time** | PCAO-F 18 Sep + PCAR-F seat late Sep | Tight but possible: PCAO-F ~18–22 Sep, PCAR-F ~28 Sep–4 Oct. Har exam ke 2 free attempts, koi retake-wait cushion nahi |
| **B — PCAR-F slips past 5 Oct** | Nahi | PCAO-F to ho jaye (pass by ~25 Sep). PCAR-F jab bhi seat aaye. Deadline PCAO-F tak re-scope karo, PCAR-F ko "seat ke intzaar mein, prep done" |
| **C — nothing bookable** | Nahi | Dono ki full prep + samples complete rakho; sit karo jaise hi live ho |

**Practical stance:** prep ko treat karo jaise deadline 5 Oct hai (dono blueprints ready, samples
75%+), lekin **actual sitting book/seat pe depend karta hai jo abhi Panaversity ke control mein hai,
tumhare nahi.** Yeh honest re-scope hai, scope-cut nahi.

Deadline se ~5 hafte hain — [04-gaps-and-study-plan.md](04-gaps-and-study-plan.md) ka 6-week plan
compress karo (Associate + Architect ek saath, kyunki dono blueprints ka bara hissa is repo mein
already cover hai).

**Rule:** ek week ka checkbox tab hi tick hota hai jab uska "Done jab" criteria khud dekh liya ho.

---

## Progress Checklist (revised 2026-09-01 — Associate pehle)

| Week | Focus | Status | Notes |
| --- | --- | --- | --- |
| 1 | **CCAO-F blueprint** — Output Evaluation 21% · Workflow Integration 16% · Governance 15% (= 52%). Judgment drills: [`ccao-f/projects/00-judgment-drills/`](ccao-f/projects/00-judgment-drills/README.md) | ⬜ Not started | Yeh naya step — pehle plan mein nahi tha |
| 2 | **CCAR-F blueprint** — Agentic Architecture & Orchestration 27% · Claude Code Config & Workflows 20% · Prompt Eng & Structured Output 20% · Tool Design & MCP 18% · Context Mgmt & Reliability 15%. Repo mein already strong (Loop/Harness/Graph Eng, Agent SDK notes). 6 CCAR-F scenarios memorize karo | ⬜ Not started | Domain names gen 61 pe refined |
| 3-4 | Ek chhoti application banao jo kai domains touch kare (API call + tool/MCP + prompt/context eng + basic eval) | ⬜ Not started | CCAR-F project scaffolds: [`ccar-f/projects/`](ccar-f/projects/README.md) |
| 5 | Samples exam conditions mein — **PCAO-F sample (10 Sep)** + **CCAR-F Practice Exam** (PCAR-F sample abhi nahi). Weak domains drill | ⬜ Not started | flashgenius.net + Anthropic Academy + book CCAR-F Practice Exam |
| 6 | **PCAO-F sit karo (18 Sep se live)**. PCAR-F: seat available hote hi sit karo — jab tak prep + samples 75%+ | ⬜ Not started | Dono 720/1000, 2 free attempts each. PCAR-F date Panaversity pe depend |

Status legend: ⬜ Not started · 🔶 In progress · ✅ Done

**Readiness (Track B ka standard, dono exams par apply):** har blueprint domain ka ek-line summary,
practice test pe domain-wise 75%+, missed questions ka principle explain kar sako.

---

## Week 1-2 — Blueprint + Domain-Weighted Study

**Kya karna hai:** [pcar-f/README.md](pcar-f/README.md) (ya [ccar-f/README.md](ccar-f/README.md) full
detail ke liye) ki domain table se weights confirm karo (Agentic Architecture 27%, Claude Code Config
20%, Prompt Engineering 20%, Tool Design/MCP 18%, Context Management 15%). Is repo mein jo already
cover hai wahan se revise karo — jo 🔲 hai (Skills & Connectors, Code You Never Write, How to Think in
the AI Era) uske liye Zia Tutor se fresh fetch karo ya Anthropic Academy free courses use karo.

### Done jab (self-check)
- [ ] Sab 5 CCAR-F domains ka apna ek-line summary likh sakta hoon
- [ ] Pata hai konsi domain is repo mein already strong hai (Agentic Architecture — 4 courses) aur
  konsi thin hai (Prompt Engineering, Tool Design/MCP — kuch gaps)

---

## Week 3-4 — Ek Chhoti Application Banao

**Kya karna hai:** ek weekend project jo API call kare, kam se kam ek tool/MCP server use kare,
prompt/context engineering apply kare, aur ek basic eval include kare. (Is repo mein already
[connector-native-apps](../connector-native-apps/README.md) aur
[trusting-the-checker](../trusting-the-checker/README.md) projects isi shape ke hain — reuse ya
extend karo.)

### Done jab (self-check)
- [ ] Project chalta hai aur kam se kam 3 CCAR-F domains touch karta hai
- [ ] Ek trade-off likh sakta hoon jo banate waqt khud decide kiya (batch vs real-time, agent vs
  workflow, MCP server vs custom tool)

---

## Week 5 — Practice Test + Weak-Domain Drill

**Kya karna hai:** [pcar-f/README.md](pcar-f/README.md) ke "Prep Resources" se CCAR-F sample test free
lo, exam conditions mein (120 min, no notes). Explanations parho — samjho **kyun** sahi trade-off sahi
hai, na sirf kya sahi hai.

### Done jab (self-check)
- [ ] Ek full practice attempt complete hua, score aur weak domains note kiye
- [ ] Weakest 1-2 domains ka targeted re-study hua

---

## Week 6 — PCAR-F Sit Karo

**Kya karna hai:** weak domains dobara test karo, phir **PCAR-F** book karo aur do (Panaversity ke
zariye, [01-stage-one-panaversity.md](01-stage-one-panaversity.md) dekho). Pass = 720/1000.

### Done jab (self-check)
- [ ] PCAR-F attempt complete hua
- [ ] Result (pass/fail + score) yahan note hua

---

## 2026-08-26 — Track B Accelerated Syllabus Cross-Check

User ne root mein Panaversity ka apna
[`Claude Certified Architect Foundations (CCAR-F) FDE Track B Accelerated.md`](../../Claude%20Certified%20Architect%20Foundations%20%28CCAR-F%29%20FDE%20Track%20B%20Accelerated.md)
add ki — ek official 13-week syllabus (architect strand + FDE practicum, dono). Zia Tutor ke
`outline_agent_factory` + `search_agent_factory` se cross-check kiya taake pata chale is repo ka
current state us syllabus ke against kahan khara hai.

**Achi khabar — Week 1, 6, aur 11 ke required reads is repo mein already maujood hain** (pehle
audit mein iska explicit confirmation nahi tha):
- Week 1: *Roles This Book Trains* (`docs/roles-this-book-trains`), *The FDE AF Model*
  (`docs/ecosystem-fde-af-model`), *Agentic Coding Crash Course* (`docs/agentic-coding`), *The Four
  Layers* (`docs/four-layers`), *Is This an Agent Problem?* (`docs/is-this-an-agent-problem`),
  *Choosing Agentic Architectures* (`docs/choosing-agentic-architectures-crash-course`) — sab ✅
- Week 6: *Spec-Driven Development* (`docs/spec-driven-development`) — ✅
- Week 11: *Building the Context Layer* (`docs/context-layer-crash-course`) — ✅ (pehle "gap" list
  mein galti se nahi tha, woh list stale thi is folder ke liye)

**Confirm hua (koi change nahi, `04-gaps-and-study-plan.md` ka 2026-08-24 wala finding sahi hai):**
syllabus ke Weeks 2-5, 9-10 ke "required Claude courses" — *The Loop by Hand*, *Claude Agent SDK*,
*Claude Code for Teams*, *Claude Code as a CI Worker*, *Structured Extraction Pipelines*, *Claude
Code Routines*, *Claude Managed Agents* — abhi bhi **"not links yet"** hain Zia Tutor corpus mein
(book ki apni `certifications` page khud confirm karti hai). In par direct kaam nahi ho sakta jab tak
Anthropic/Panaversity publish na karein — is table ko periodically dobara check karna hai.

**Naya, genuinely actionable gap jo is cross-check se mila:** syllabus ka **FDE Practicum strand
(P1-P13)** ek **actually deployed** Vertical SoR maangta hai — Next.js+Fumadocs human-readable site +
stateless MCP (2026-07-28) agent-readable surface, live. Is repo ke paas KSoR/SoR ke **concept docs**
already hain (`docs/ksor/`, `docs/ecosystem-designing-the-vertical-sor/`, `docs/certifications`
khud) lekin koi real Fumadocs project ya MCP server abhi tak nahi bana/deploy hua — Milestones 1
("live human surface, 5+ governed docs") aur 2 ("working stateless MCP search/retrieve/cite
interface") is repo mein currently unmet hain. Yeh PCAR-F pass karne ke liye **zaroori nahi** (Week
3-4 ka "chhoti application" self-check kaafi hai), lekin CCAR-F/FDE-Internship ki taraf agla concrete
practicum kaam hai — [`todolist.md`](../../todolist.md) mein backlog ki tarah note kiya.

## Open Note — Root README.md Stale Hai

Is chapter ke domain-mapping ([03-exam-domains.md](03-exam-domains.md)) banate waqt pata chala ke
root `README.md` ka status table **stale hai**: `docs/roles-this-book-trains/`, `docs/ai-prompting-2026/`,
`docs/what-you-carry-in/`, `docs/what-ai-actually-is-crash-course/`, `docs/markdown-html-crash-course/`
jaise folders **poore documented hain** (README + numbered files + SUMMARY.md), lekin README.md ka
Front Matter (12) aur Foundations (6) sections abhi bhi "0/12" aur "0/6" dikhate hain. Yeh separate
audit/fix hai — is task ke scope se bahar, lekin flag kar diya taake bhoola na jaye.
