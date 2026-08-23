# 03 — Exam Domains: At A Glance

**Poori domain-weight table + book-coverage mapping ab har certification ke apne folder mein hai** —
yeh file sirf quick-glance comparison + index hai.

## Sab 8 Certifications, Ek Nazar Mein

| Code | Full Name | Issuer | Status | Price | Questions | Domain Detail |
| --- | --- | --- | --- | --- | --- | --- |
| [PCAR-F](pcar-f/README.md) | Panaversity Certified Architect: Foundations | Panaversity | Available now | Free (2 attempts) | — | matches CCAR-F |
| [PCDV-F](pcdv-f/README.md) | Panaversity Certified Developer: Foundations | Panaversity | Available now | Free (2 attempts) | — | matches CCDV-F |
| [PCAO-F](pcao-f/README.md) | Panaversity Certified Associate: Foundations | Panaversity | Planned | — | — | matches CCAO-F |
| [PCAR-P](pcar-p/README.md) | Panaversity Certified Architect: Professional | Panaversity | Planned | — | — | matches CCAR-P |
| [CCAR-F](ccar-f/README.md) | Claude Certified Architect: Foundations | Anthropic | Live | $125 | 60 | **Agentic Architecture 27%** heaviest |
| [CCDV-F](ccdv-f/README.md) | Claude Certified Developer: Foundations | Anthropic | Live | $125 | 53 | **Applications & Integration 33.1%** heaviest |
| [CCAO-F](ccao-f/README.md) | Claude Certified Associate: Foundations | Anthropic | Live | $99 | 60 | **Output Evaluation & Validation 21%** heaviest |
| [CCAR-P](ccar-p/README.md) | Claude Certified Architect: Professional | Anthropic | Live | $175 | 63 | **Integration 19%** heaviest |

*2026-08-24 update: poore 4 official exam guide PDFs directly padhe (WebFetch ka PDF-text-extraction
kaam nahi kar raha tha aur hallucinate kar raha tha — Read tool se PDF seedha parha, verify kiya). Sab
counts/prices/domain-weights ab official-guide-confirmed hain, koi bhi "independent-report-only" figure
nahi bacha.*

## FDE Path Ka Focus

Is book ka recommended FDE pair sirf 2 hain: **CCAR-F → CCDV-F** (aur inke Panaversity-aligned gate,
**PCAR-F → PCDV-F**). CCAO-F aur CCAR-P alag roles ke liye hain (advising/selling, aur senior capstone
respectively) — abhi is repo ka focus nahi.

## Study Priority (Domain Weight Se)

**PCAR-F/CCAR-F ke liye** (is repo ka immediate target): Agentic Architecture (27%) → Claude Code
Config + Prompt Engineering (20% + 20%) → Tool Design/MCP (18%) → Context Management (15%). Poori
table [CCAR-F folder](ccar-f/README.md) mein.

**PCDV-F/CCDV-F ke liye** (agla step): Applications and Integration (33.1%) + Model Selection (16.8%)
= ~50% ka aadha exam. Poori table [CCDV-F folder](ccdv-f/README.md) mein.

## Root README Staleness (Alag Se Nota)

Domain→book-coverage mapping banate waqt pata chala ke root `README.md` ka status table stale hai —
kai chapters (`roles-this-book-trains`, `ai-prompting-2026`, `what-you-carry-in`, waghera) already
documented hain lekin table 🔲 dikhata hai. Har cert folder mein ✅/🔲 markers is repo ke **actual disk
state** ke against verify kiye gaye hain (root README ke against nahi).

---
[⬅ Index](README.md) · [Peechay: Stage Two](02-stage-two-anthropic.md) ·
[Agla: Gaps + Study Plan ➡](04-gaps-and-study-plan.md)
