# How to Run Track B — Operating Guide

*Yeh 13-week syllabus ko is repo mein kaise chalana hai. Ek baar padho, phir har session isi rhythm
se chalta hai.*

Syllabus (authority): [`../Claude Certified Architect Foundations (CCAR-F) FDE Track B Accelerated.md`](../Claude%20Certified%20Architect%20Foundations%20%28CCAR-F%29%20FDE%20Track%20B%20Accelerated.md)
Structured notes: [`../docs/ccar-f-fde-track-b/`](../docs/ccar-f-fde-track-b/README.md)

---

## 1. Do strands, har session dono

| Strand | Grade | Har week | Yahan folder |
| --- | ---: | --- | --- |
| **Architect** (exam prep) | 70% | 3-hour rhythm (neeche) | `week-NN-*/` |
| **FDE Practicum** (Vertical SoR) | 30% | P1-P13, 1.5 hr | `practicum/PNN-*.md` |

Har session: ek architect week + uska corresponding practicum week aage badhte hain. Week 1 ↔ P1,
Week 2 ↔ P2, ... Week 11 par dono milte hain (support agent apna governed knowledge consume karta hai).

## 2. Architect week ka 3-hour rhythm

Har week folder mein yehi 3 files banti hain:

| Hour | Kaam | File |
| --- | --- | --- |
| **1 — Concepts (60 min)** | Week ka topic + CCAR-F blueprint mapping. Reading notes. | `concepts.md` |
| **2 — Guided lab (90 min)** | Build / break / diagnose / redesign. Real code, real run. Kai exam distractors "plausible lekin fail hone wale" approaches hain — unhe fail hote dekho. | `<lab>.py` + `lab-notes.md` |
| **3 — Scenario practice (30 min)** | 10-15 scenario-style MCQ/MRQ. Har ek: (a) sahi jawab kyun best, (b) alternatives kyun kamzor, (c) kaunsa principle test ho raha. | `scenario-practice.md` |

**Har lab ke baad** → `../trade-off-notebook.md` mein entry (kya trade-off, kya choose kiya, alternatives
kyun kamzor). Yeh graded hai (7%).

## 3. Practicum week

`practicum/PNN-<slug>.md` — us week ke deliverables (thesis, source register, decisions log,
Fumadocs site, MCP surface, eval set...). Runnable scaffolds pehle se hain:
[`../docs/ccar-f-fde-track-b/projects/`](../docs/ccar-f-fde-track-b/projects/README.md) (P4-P5, P6-P7, P8, P11).

**Milestones:** P5 (live human surface, 5+ docs) · P8 (agent MCP surface) · P11 (governed KSoR + eval) ·
P13 (capstone demo + brief).

## 4. The 4 required architect projects

| Project | Week | Scaffold (pehle se bana) |
| --- | ---: | --- |
| 1. Agentic loop, no framework | 2 | [`../docs/certifications/ccar-f/projects/00-agentic-loop-no-framework/`](../docs/certifications/ccar-f/projects/00-agentic-loop-no-framework/README.md) |
| 2. Governed customer-support agent | 5 | [`../docs/certifications/ccar-f/projects/01-multi-tool-agent-escalation/`](../docs/certifications/ccar-f/projects/01-multi-tool-agent-escalation/README.md) |
| 3. Structured extraction pipeline | 10 | [`../docs/certifications/ccar-f/projects/03-structured-extraction-pipeline/`](../docs/certifications/ccar-f/projects/03-structured-extraction-pipeline/README.md) |
| 4. Multi-agent research system | 11 | [`../docs/certifications/ccar-f/projects/04-multi-agent-research-pipeline/`](../docs/certifications/ccar-f/projects/04-multi-agent-research-pipeline/README.md) |
| (Week 7 lab = official Exercise 2) | 7 | [`../docs/certifications/ccar-f/projects/02-claude-code-team-workflow/`](../docs/certifications/ccar-f/projects/02-claude-code-team-workflow/README.md) |

Har project apne week folder se link hota hai; kaam yahan CCA-F workspace mein hota hai, scaffold
sirf starting structure + tests deta hai.

## 5. Auth / environment

- **Auth:** claude-agent-sdk (Claude Code CLI login) — koi `ANTHROPIC_API_KEY` nahi. Jahan syllabus
  "raw Messages API" kehti hai, wahan hum by-hand loop ko ek **offline `FakeClient`** se chalate hain
  (mechanics teach karne ke liye) + ek real end-to-end run claude-agent-sdk se.
- **Env:** Python 3.13 · Node 24.18 · pnpm 9.12 · uv 0.6 — sab verified (P1).
- **Windows footgun:** har script ke top par `sys.stdout.reconfigure(encoding="utf-8")` — warna
  em-dash / non-latin text `?` ho jata hai.

## 6. Progress tracking (spine discipline)

| File | Kya |
| --- | --- |
| `TRACK-B-WORKLOG.md` | Is course ki spine — har session ke baad update (week status, decisions, blocked) |
| `trade-off-notebook.md` | Har architect lab ke 3 sawal (graded) |
| `../progress.md` + `../todolist.md` | Repo-level — har batch ke baad sync, phir `git push` (standing rule) |

## 7. Week 13 — readiness decision

Panaversity PCAR-F booking endorse karti hai jab: **80%+ on 2 full-length mocks · 75%+ har domain ·
sab 4 projects complete · missed questions ka principle explain kar sako.** (Real exam apna 720-scaled
cut score use karta hai — alag threshold.)

---

## Current position

| | Status |
| --- | --- |
| Week 1 — Foundations Sprint | ✅ |
| P1 — Thesis + Setup | ✅ |
| Week 2 — Agentic Loop by Hand | ✅ |
| P2 — Choose the Vertical | 🟡 scored — **needs your confirmation** (provisional: PK freelancer/software-house tax & FBR) |
| **Week 3 — Claude Agent SDK I** | ⏭ next |
| **P3 — Design the Vertical SoR** | ⏭ blocked on P2 confirmation |
