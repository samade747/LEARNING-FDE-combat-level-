# Certifications — Notes (Roman Urdu + English)

Ye notes **"Certifications: Proof You Can Carry In"** page ka easy explainer hain, Panaversity ke
**The AI Agent Factory** book se (Zia Tutor AI connector ke zariye, `slug: certifications`, top-level
Front Matter doc, position #13).

Source: https://agentfactory.panaversity.org/docs/certifications

**Re-fetched 2026-09-01 from the Zia Tutor AI connector (corpus generation 47, page "Version note":
updated 28 August 2026) + a live WebFetch cross-check.** ⚠️ **Bara change:** book ne poora FDE pathway
restructure kar diya — ab **Associate pehle, Architect doosra** (neeche). Pehla verify 22 Aug 2026 ka
tha (PCAR-F → PCDV-F gate) — wo ab **stale** hai. Domain weights aur fees "subject to change without
notice" hain.

## Index — Shared Pathway Files

*Yeh files sab certifications pe apply hoti hain — pathway, logistics, study plan.*

1. [00 — Overview: Do Stages, Ek Pathway](00-overview.md)
2. [01 — Stage One: Panaversity Qualification (PCAO-F → PCAR-F)](01-stage-one-panaversity.md)
3. [02 — Stage Two: Anthropic Certification (CCAO-F → CCAR-F, + CCDV-F, CCAR-P)](02-stage-two-anthropic.md)
4. [03 — Exam Domains: At A Glance (index into per-cert folders)](03-exam-domains.md)
5. [04 — Gaps + Six-Week Study Plan](04-gaps-and-study-plan.md)
6. [05 — Registration, Retakes, Costs, 6 Mistakes](05-registration-costs-mistakes.md)
7. [06 — Sample Tests + Official Exam Guides (index into per-cert folders)](06-sample-tests.md)
8. [07 — Practice Log (meri apni PCAO-F → PCAR-F push, deadline 2026-10-05)](07-practice-log.md)
9. [08 — Test Your Understanding (14 Scenario-Based Questions)](08-test-your-understanding.md)
10. [Quiz — Self-Contained (same 14 questions)](quiz.md)

## Har Certification Ka Apna Folder

*Har folder mein us exam ki quick facts, domain-weight table + book-coverage mapping, aur prep
resources (official guide, free sample test) hain — is repo ke baaqi chapters ki `projects/[slug]/`
tarah, alag bas exam-level pe. 4 Anthropic folders (`ccar-f/`, `ccdv-f/`, `ccao-f/`, `ccar-p/`) ab
is repo ke baaqi chapters (`loop-engineering/`, `harness-engineering/`) jaisi hi numbered-file shape
mein hain: `README.md` (index) + `00`–`04` numbered files (quick facts/audience → domain blueprint
→ scope/scoring → how-to-prepare + full sample questions → policies/resources/doc-control) +
`SUMMARY.md` (condensed recap) — dekho [`03-exam-domains.md`](03-exam-domains.md).*

### Panaversity (Stage One — FDE gate = PCAO-F **phir** PCAR-F)

| Folder | Exam | Status (per book, 28 Aug 2026) |
| --- | --- | --- |
| [`pcao-f/`](pcao-f/README.md) | Panaversity Certified Associate: Foundations | **Required FIRST** — FDE gate ka pehla exam |
| [`pcar-f/`](pcar-f/README.md) | Panaversity Certified Architect: Foundations | **Required SECOND** — is repo ka current study target |
| [`pcdv-f/`](pcdv-f/README.md) | Panaversity Certified Developer: Foundations | Additional technical credential (ab FDE gate ka hissa nahi) |
| [`pcar-p/`](pcar-p/README.md) | Panaversity Certified Architect: Professional | Advanced / professional track |

*Har Panaversity exam ke 720/1000 pass, do free attempts (Panaversity students). Book ab exam-level
"Available/Planned" status nahi deta — sirf role batati hai; "PCAO-F planned" wali purani line hata di.*

### Anthropic (Stage Two — recommended FDE pair = CCAO-F **phir** CCAR-F)

| Folder | Exam | Price · Qs | FDE Path Focus? |
| --- | --- | --- | --- |
| [`ccao-f/`](ccao-f/README.md) | Claude Certified Associate: Foundations | $99 · 60 | ✅ **Yes — pehla** (recommended FDE pair ka Step 1; broad judgment) |
| [`ccar-f/`](ccar-f/README.md) | Claude Certified Architect: Foundations | $125 · 60 | ✅ **Yes — doosra** (system design; counts toward partner tier) |
| [`ccdv-f/`](ccdv-f/README.md) | Claude Certified Developer: Foundations | $125 · 53 | Additional — build/ship proof after the pair |
| [`ccar-p/`](ccar-p/README.md) | Claude Certified Architect: Professional | $175 · 63* | Nahi (senior capstone) |

*`*` CCAR-P ke 63 questions — book page (28 Aug) ise wapas "independent guides only, not
official-confirmed" keh rahi hai, jabke is repo ne 2026-08-24 ko official PDF khud padha tha. Neeche
02 mein flagged.*

**Note:** CCAO-F Claude Partner Network **tier eligibility mein count nahi hota** — sirf CCDV-F /
CCAR-F / CCAR-P count hote hain. Lekin FDE learning progression ke liye CCAO-F ab pehla step hai.

## Ek Line Mein Poori Cheez

> **Poora path (28 Aug 2026):** PCAO-F → PCAR-F → FDE Internship Program & partner access → CCAO-F →
> CCAR-F. **Stage One** (PCAO-F + PCAR-F) Panaversity ka apna readiness-gate hai — students ko 2 free
> attempts, khud proctor karte hain, 720/1000 pass. **Stage Two** (CCAO-F + CCAR-F, = $224) Anthropic
> ke official Pearson-VUE exams hain, jinke liye partner-organisation email chahiye — jo Stage One
> pass karne se milta hai. Logic: **use AI well → evaluate it → govern it → design the system.**

## Is Repo Ka Apna Goal (2026-08-24, path-update 2026-09-01)

User ka personal challenge: **2026-10-05 tak PCAR-F pass karo**. ⚠️ **Book ne pathway badla —
ab PCAO-F PCAR-F se PEHLE aata hai.** Isliye us deadline se pehle **do exams** hain (PCAO-F → PCAR-F),
ek nahi. Spine + revised plan: [`07-practice-log.md`](07-practice-log.md).

**Fuller reference (2026-08-26):** root
[`Claude Certified Architect Foundations (CCAR-F) FDE Track B Accelerated.md`](../../Claude%20Certified%20Architect%20Foundations%20%28CCAR-F%29%20FDE%20Track%20B%20Accelerated.md)
Panaversity ka apna official 13-week Track B syllabus hai (user ne khud add ki, book ke Zia Tutor
corpus se nahi — is folder ki tarah "book se nikala" content nahi, balke ek external curriculum doc
hai). Yeh dono strands cover karta hai: **architect** (12-week class, CCAR-F blueprint ke task
statements tak granular) aur **FDE practicum** (Vertical System of Record banana — KSoR, Fumadocs,
stateless MCP). [`07-practice-log.md`](07-practice-log.md) mein iska cross-check + gap-analysis hai.

## Certification vs Baaqi Repo Se Farq

Baaqi is repo ke chapters (`docs/loop-engineering`, `docs/harness-engineering`, waghera) **skills**
sikhate hain — kaise banayen. Yeh page **proof** ke baare mein hai — ek stranger ko kaise pata chale
ke aap wo skill rakhte ho, bina unke aapka code parhe ya aapki baat pe yaqeen kiye. Dono zaroori hain:
skill pehle, phir uska proctored evidence.
