# 03 — Exam Domains: At A Glance

**Poori domain-weight table + book-coverage mapping ab har certification ke apne folder mein hai** —
yeh file sirf quick-glance comparison + index hai.

## Sab 8 Certifications, Ek Nazar Mein

| Code | Full Name | Issuer | Path role (28 Aug 2026) | Price | Questions | Domain Detail |
| --- | --- | --- | --- | --- | --- | --- |
| [PCAO-F](pcao-f/README.md) | Panaversity Certified Associate: Foundations | Panaversity | **FDE gate — first** | Free (2 attempts) | — | matches CCAO-F |
| [PCAR-F](pcar-f/README.md) | Panaversity Certified Architect: Foundations | Panaversity | **FDE gate — second** | Free (2 attempts) | — | matches CCAR-F |
| [PCDV-F](pcdv-f/README.md) | Panaversity Certified Developer: Foundations | Panaversity | Additional credential | Free (2 attempts) | — | matches CCDV-F |
| [PCAR-P](pcar-p/README.md) | Panaversity Certified Architect: Professional | Panaversity | Advanced track | — | — | matches CCAR-P |
| [CCAO-F](ccao-f/README.md) | Claude Certified Associate: Foundations | Anthropic | **FDE pair — first** | $99 | 60 | **Output Evaluation & Validation 21%** heaviest |
| [CCAR-F](ccar-f/README.md) | Claude Certified Architect: Foundations | Anthropic | **FDE pair — second** | $125 | 60 | **Agentic Architecture 27%** heaviest |
| [CCDV-F](ccdv-f/README.md) | Claude Certified Developer: Foundations | Anthropic | Additional credential | $125 | 53 | **Applications & Integration 33.1%** heaviest |
| [CCAR-P](ccar-p/README.md) | Claude Certified Architect: Professional | Anthropic | Senior capstone | $175 | 63* | Stakeholder communication + lifecycle beyond CCAR-F |

*Prices + 60/60/53 counts official-guide-confirmed. `*` CCAR-P 63 — book page (28 Aug 2026) ab
"independent guides only" keh rahi hai (repo ne 2026-08-24 ko official PDF padha tha — conflict, dekho
[02](02-stage-two-anthropic.md)). CCAR-P "Integration 19% heaviest" wali purani line hata di — book
page us breakdown ka blueprint table nahi deta, sirf "stakeholder communication + lifecycle" theme.*

## FDE Path Ka Focus (28 Aug 2026)

Recommended FDE pair: **CCAO-F → CCAR-F** (aur inke Panaversity-aligned gate, **PCAO-F → PCAR-F**).
CCDV-F/PCDV-F ab "additional technical credential" hain — pair ke baad, agar deeper build/ship proof
chahiye. CCAR-P senior capstone hai.

## Study Priority (Domain Weight Se)

**PCAO-F/CCAO-F ke liye** (ab pehla exam): Output Evaluation & Validation (21%) → Workflow Integration
& Solution Design (16%) → Governance/Risk (15%) — yeh teen = 52% of the exam. Poori table
[CCAO-F folder](ccao-f/01-domain-blueprint.md) mein.

**PCAR-F/CCAR-F ke liye** (doosra exam, is repo ka main study target): Agentic Architecture (27%) →
Claude Code Config + Prompt Engineering (20% + 20%) → Tool Design/MCP (18%) → Context Management (15%).
Poori table [CCAR-F folder](ccar-f/README.md) mein.

**CCDV-F ke liye** (agar aage jao): Applications and Integration (33.1%) + Model Selection (16.8%)
= ~50% ka aadha exam. Poori table [CCDV-F folder](ccdv-f/README.md) mein.

## Root README Staleness (Alag Se Nota)

Domain→book-coverage mapping banate waqt pata chala ke root `README.md` ka status table stale hai —
kai chapters (`roles-this-book-trains`, `ai-prompting-2026`, `what-you-carry-in`, waghera) already
documented hain lekin table 🔲 dikhata hai. Har cert folder mein ✅/🔲 markers is repo ke **actual disk
state** ke against verify kiye gaye hain (root README ke against nahi).

---
[⬅ Index](README.md) · [Peechay: Stage Two](02-stage-two-anthropic.md) ·
[Agla: Gaps + Study Plan ➡](04-gaps-and-study-plan.md)
