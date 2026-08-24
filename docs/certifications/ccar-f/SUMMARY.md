# CCAR-F — Chapter Recap

Claude Certified Architect – Foundations: solution architects ke liye jo Claude Agent SDK, Claude Code,
MCP, aur structured-output prompting se production Claude apps design/implement karte hain. $125,
60 questions (4 scenarios ek bank-of-6 se), 120 min, scaled-720 cut score, 12-month validity. Sab detail
`Read` tool se PDF se nikala gaya 2026-08-24 (5 numbered files mein poora expand hua hai, ismein sirf
top-level recap hai).

## 00 — Quick Facts + Intended Audience

- $125 · 60 Qs (MCQ + multi-response) · 120 min · Pearson VUE proctored · scaled 720/1000 pass ·
  12-month validity, on-time renewal free
- Exam **realistic scenarios** pe based hai actual customer use cases se — candidates ko conceptual
  knowledge + practical judgment dono dikhani hoti hai architecture/config/tradeoffs ke baare mein
- MQC: solution architect jo Claude Agent SDK (multi-agent, subagents, hooks), Claude Code (CLAUDE.md,
  Skills, MCP, plan mode), MCP tool design, structured-output prompting, context management, CI/CD
  integration, aur escalation/reliability decisions mein hands-on ho — **typical 6+ months** experience

## 01 — Domain Blueprint (Full Task Statements)

- 5 domains: **1 Agentic Architecture & Orchestration 27%** (loops, coordinator-subagent, Task tool,
  hooks, decomposition, session mgmt) → **3 Claude Code Config 20%** aur **4 Prompt Engineering 20%**
  (tied) → **2 Tool Design & MCP 18%** → **5 Context Mgmt & Reliability 15%**
- **Correction:** original single-file README ne Domain 2/3/4 ka numbering PDF se mismatch kiya tha
  (Claude Code ko "2" likh diya tha) — ab official order use hota hai
- Har domain 5-7 task statements carry karta hai, har ek Knowledge-of + Skills-in bullets ke sath — file
  01 mein full text hai (yeh sab se lamba file hai is folder mein)

## 02 — Scope, Scoring & Exam Format

- 6 scenarios (Customer Support, Code Gen with Claude Code, Multi-Agent Research, Dev Productivity,
  CI/CD, Structured Extraction), 4 randomly drawn per sitting — full production-context paragraphs +
  primary-domain mapping ab file mein hain
- Sample questions sirf Scenarios 1/2/3/5 se hain — 4 aur 6 blueprint mein hain lekin official
  sample-set mein represent nahi hote
- Scoring **criterion-referenced** hai — fixed standard ke against, doosre candidates se compete nahi
  karte. Cut score 720 formal standard-setting study se aaya
- Full in-scope (18 bullets) + out-of-scope (16 bullets) lists ab dono verbatim hain, plus poora
  Technologies/Concepts appendix reference table

## 03 — How to Prepare + Sample Questions

- Official "How to Prepare" ke 7 bullets + 4 hands-on Preparation Exercises **poori tarah expand** hue
  hain (objective + har exercise ke 4-5 concrete steps + domains-reinforced) — pehle sirf naam the
- **Sab 12 sample questions ab poore hain** (pehle sirf 1 tha): full A-D options + correct answer +
  explanation, 4 scenarios mein grouped (Customer Support Q1-3, Code Gen Q4-6, Multi-Agent Research
  Q7-9, CI/CD Q10-12)
- Signature pattern har jawab mein: probabilistic fixes (prompts, few-shot, confidence scores,
  sentiment) almost kabhi correct answer nahi hote jab deterministic guarantee chahiye ho

## 04 — Policies, Resources & Document Control

- Registration: Anthropic Partner Academy → Pearson VUE account → schedule; 24h+ free
  reschedule
- ID must exactly match registration name; accommodations Pearson VUE se **pehle** approve honi
  chahiye
- Retakes: max 4/12-months, waits 14/30/90 din (1st/2nd/3rd fail ke baad)
- Exam-day conduct: webcam view mein rehna, clear workspace, no communication, no content capture —
  violation se credential revoke + ban ho sakta hai
- NDA accept karna mandatory hai exam shuru hone se pehle — decline = session end, no refund
- Renewal: 12-month validity, on-time free non-proctored refresher; lapse ho to full exam dobara
- Appeals: 14-din window, lekin standard-setting outcome + individual items appeal-proof hain
- Document control: v1.0 (July 2026) ← v0.2 (June 2026) ← v0.1 (Feb 2026)
- Is repo ka current goal PCAR-F pehle hai (2026-10-05 tak), CCAR-F uske baad

---
[⬅ CCAR-F Index](README.md)
