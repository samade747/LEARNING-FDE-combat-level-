# Certifications — Notes (Roman Urdu + English)

Ye notes **"Certifications: Proof You Can Carry In"** section ka easy explainer hain, Panaversity ke
**The AI Agent Factory** book se (Zia Tutor AI connector ke zariye).

Source: https://agentfactory.panaversity.org/docs/certifications

**Re-fetched 2026-09-02 from the Zia Tutor AI connector (corpus generation 61, page "Version note":
updated 1 September 2026).** Pichla sync 2026-09-01 (gen 47, 28 Aug 2026) ka tha.

## ⚠️ Gen 61 Ke Bare Changes (2026-09-02)

1. **Structure — ab ek page nahi, ek section hai.** Pehle `certifications` ek single top-level
   Front-Matter doc tha (position #13). Ab `certifications-proof-you-can-carry-in` ek **group** hai
   (position #13) jismein **5 pages** hain: ek overview + **har Panaversity exam ka apna dedicated
   book page** (PCAO-F, PCAR-F, PCAR-P, PCDV-F — isi order mein). Har exam page pe: official domain
   weights, us exam ka study guide, ek sample "pehle baith", aur proctored seat kaise book karo.
2. **Anthropic exams ab explicitly OPTIONAL.** Book ki nayi line: *"Sitting the Anthropic exams is
   optional, and the choice is yours. The Panaversity credentials and the internship stand on their
   own."* Panaversity internship participants ki registration mein **"assist"** karta hai — pehle
   framing "yehi ek raasta hai" thi, ab softer.
3. **PCAO-F ke live dates (NAYE):** Panaversity ka **PCAO-F sample exam 10 September 2026** ko, aur
   **proctored PCAO-F exam 18 September 2026** ko live hota hai. PCAR-F / PCDV-F / PCAR-P ke samples
   abhi "coming soon" — koi date nahi. **User ki 2026-10-05 deadline ab bohat tight hai** — dekho
   [`07-practice-log.md`](07-practice-log.md).
4. **"Same blueprint, one level up" framing.** Har Panaversity exam matching Anthropic blueprint ko
   **poora** examine karta hai (published weights pe), **phir aage jaata hai** — vendor-neutral +
   professional coverage add karta hai (Claude + ChatGPT/other vendors side by side). "CCAR-F is the
   credential the market recognises; PCAR-F sits beneath it and holds it up."
5. **CCAR-P blueprint wapas published + 63-question count official confirmed** — pehle repo ne ise
   "independent-reported, uncertain" flag kiya tha (28 Aug book page ne walk back kiya tha). Gen 61
   pe: *"Every price and every count above comes from Anthropic's published exam guides."* Resolved.
6. **CCAO-F / CCDV-F ke full domain blueprints ab book page pe hain** (pehle sirf per-cert folder
   mein PDF se). Domain weights unchanged.
7. **Scaled-score clarity har page pe:** 720 = scaled score (100–1000 range), **72% nahi**.
   Per-domain % score report pe informational hai, pass/fail decide nahi karta. "No per-domain
   minimum."
8. **Study-guide course slugs ab live links hain** (pehle "not links yet") — Loop by Hand, Claude
   Agent SDK, Structured Extraction, Claude Code for Teams, CI Worker, Skills & Connectors,
   Governance/Risk, Workflow Design & Diagnosis, Code You Never Write, waghera. Dekho
   [`04-gaps-and-study-plan.md`](04-gaps-and-study-plan.md).

Domain weights aur fees phir bhi "subject to change without notice" hain — exam book karne se pehle
current guide download karo.

## ⚡ P3-FDEAGA — GIAIC Final Graduation Exam (separate, time-critical)

GIAIC ka apna **Final Graduation Exam** (Sindh Governor House, first week Sept 2026) — is cert-ladder
se alag hai. **100 MCQ / 140 min / 70% pass.** Syllabus = 8 book modules (Roles, Ecosystem, Local AI &
Agentic Coding, Loop Eng, Harness Eng, Trusting the Checker, Leaving the Laptop, General Agents Web).
Dedicated cram pack: **[`p3-fdeaga/`](p3-fdeaga/README.md)** — per-module cheat sheets + MCQ + 60-Q
mock + night-before one-pager.

## Index — Shared Pathway Files

*Yeh files sab certifications pe apply hoti hain — pathway, logistics, study plan.*

1. [00 — Overview: Do Stages, Ek Pathway (Anthropic optional)](00-overview.md)
2. [01 — Stage One: Panaversity Qualification (PCAO-F → PCAR-F)](01-stage-one-panaversity.md)
3. [02 — Stage Two: Anthropic Certification (CCAO-F → CCAR-F, + CCDV-F, CCAR-P)](02-stage-two-anthropic.md)
4. [03 — Exam Domains: At A Glance (index into per-cert folders)](03-exam-domains.md)
5. [04 — Gaps + Six-Week Study Plan](04-gaps-and-study-plan.md)
6. [05 — Registration, Retakes, Costs, 6 Mistakes](05-registration-costs-mistakes.md)
7. [06 — Sample Tests + Official Exam Guides (index into per-cert folders)](06-sample-tests.md)
8. [07 — Practice Log (meri apni PCAO-F → PCAR-F push, deadline 2026-10-05)](07-practice-log.md)
9. [08 — Test Your Understanding (14 Scenario-Based Questions)](08-test-your-understanding.md)
10. [Quiz — Self-Contained (same 14 questions)](quiz.md)

## Book Ke 5 Pages → Is Repo Ke Folders Ka Mapping

| Book page (gen 61) | URL | Is repo mein |
| --- | --- | --- |
| Certifications overview | `/docs/certifications` | [00](00-overview.md)–[06](06-sample-tests.md) shared files |
| PCAO-F | `/docs/certifications/pcao-f` | [`pcao-f/`](pcao-f/README.md) |
| PCAR-F | `/docs/certifications/pcar-f` | [`pcar-f/`](pcar-f/README.md) |
| PCAR-P | `/docs/certifications/pcar-p` | [`pcar-p/`](pcar-p/README.md) |
| PCDV-F | `/docs/certifications/pcdv-f` | [`pcdv-f/`](pcdv-f/README.md) |

*4 Anthropic folders (`ccar-f/`, `ccdv-f/`, `ccao-f/`, `ccar-p/`) official Anthropic Exam Guide PDFs
se banaye gaye (2026-08-24, `Read` tool se poore parhe) — book ke naye per-exam pages inhi PDFs ko
mirror karte hain, to woh folders authoritative rehte hain.*

### Panaversity (Stage One — FDE gate = PCAO-F **phir** PCAR-F)

| Folder | Exam | Status (per book, gen 61, 1 Sep 2026) |
| --- | --- | --- |
| [`pcao-f/`](pcao-f/README.md) | Panaversity Certified Associate: Foundations | **Required FIRST** — sample 10 Sep, proctored **live 18 Sep 2026** |
| [`pcar-f/`](pcar-f/README.md) | Panaversity Certified Architect: Foundations | **Required SECOND** — sample "coming soon", is repo ka current target |
| [`pcdv-f/`](pcdv-f/README.md) | Panaversity Certified Developer: Foundations | Additional technical credential (FDE gate ka hissa nahi) |
| [`pcar-p/`](pcar-p/README.md) | Panaversity Certified Architect: Professional | Capstone, pair ke baad |

*Har Panaversity exam ka 720/1000 pass, Panaversity students ko 2 free attempts. Book ab har exam ko
apna page deti hai (weights + study guide + sample + seat request).*

### Anthropic (Stage Two — optional; recommended FDE pair = CCAO-F **phir** CCAR-F)

| Folder | Exam | Price · Qs | FDE Path Focus? |
| --- | --- | --- | --- |
| [`ccao-f/`](ccao-f/README.md) | Claude Certified Associate: Foundations | $99 · 60 | ✅ **Yes — pehla** (recommended FDE pair ka Step 1; broad judgment) |
| [`ccar-f/`](ccar-f/README.md) | Claude Certified Architect: Foundations | $125 · 60 | ✅ **Yes — doosra** (system design; counts toward partner tier) |
| [`ccdv-f/`](ccdv-f/README.md) | Claude Certified Developer: Foundations | $125 · 53 | Additional — build/ship proof after the pair (counts toward partner tier) |
| [`ccar-p/`](ccar-p/README.md) | Claude Certified Architect: Professional | $175 · 63 | Nahi (senior capstone; counts toward partner tier) |

*63 (CCAR-P) ab **official-guide-confirmed** hai — gen 61 ne pichla "independent-only" caveat resolve
kar diya. Sabhi prices/counts book ke published exam guides se.*

**Note:** CCAO-F Claude Partner Network **tier eligibility mein count nahi hota** — sirf CCDV-F /
CCAR-F / CCAR-P count hote hain. Lekin FDE learning progression ke liye CCAO-F pehla step hai.

## Ek Line Mein Poori Cheez

> **Poora path (gen 61, 1 Sep 2026):** PCAO-F → PCAR-F → **FDE Internship Program** → *(optional)*
> CCAO-F → CCAR-F. **Stage One** (PCAO-F + PCAR-F) Panaversity ka apna readiness-gate hai — students
> ko 2 free attempts, khud proctor karte hain, 720/1000 pass. **Stage Two** (CCAO-F + CCAR-F, =
> $224) Anthropic ke official Pearson-VUE exams hain — **optional**; jinke liye partner-organisation
> email chahiye, jo internship se milta hai, aur Panaversity registration mein assist karta hai.
> Logic: **use AI well → evaluate it → govern it → design the system.**

## Is Repo Ka Apna Goal (2026-08-24, path-update 2026-09-01, dates-update 2026-09-02)

User ka personal challenge: **2026-10-05 tak PCAR-F pass karo**. ⚠️ **Ab do constraints:** (1) book
ne pathway badla — PCAO-F PCAR-F se PEHLE aata hai (do exams); (2) gen 61 pe **PCAO-F proctored sirf
18 Sep se live**, PCAR-F sample abhi date-less. Deadline se pehle window bohat chhoti hai — revised
plan aur risk analysis: [`07-practice-log.md`](07-practice-log.md).

**Fuller reference (2026-08-26):** root
[`Claude Certified Architect Foundations (CCAR-F) FDE Track B Accelerated.md`](../../Claude%20Certified%20Architect%20Foundations%20%28CCAR-F%29%20FDE%20Track%20B%20Accelerated.md)
Panaversity ka apna official 13-week Track B syllabus hai (user ne khud add ki). Dono strands cover
karta hai: **architect** (12-week class, CCAR-F blueprint tak granular) aur **FDE practicum**
(Vertical System of Record banana — KSoR, Fumadocs, stateless MCP). [`07-practice-log.md`](07-practice-log.md)
mein iska cross-check + gap-analysis hai.

## Certification vs Baaqi Repo Se Farq

Baaqi is repo ke chapters (`docs/loop-engineering`, `docs/harness-engineering`, waghera) **skills**
sikhate hain — kaise banayen. Yeh section **proof** ke baare mein hai — ek stranger ko kaise pata chale
ke aap wo skill rakhte ho, bina unke aapka code parhe ya aapki baat pe yaqeen kiye. Dono zaroori hain:
skill pehle, phir uska proctored evidence.
