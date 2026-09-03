# 01 — Roles We Are Training For

*Source: `roles-this-book-trains` — https://agentfactory.panaversity.org/docs/roles-this-book-trains
(Zia Tutor AI, corpus gen 62). Deep notes: [`docs/roles-this-book-trains/`](../../roles-this-book-trains/README.md).*

---

## A. Harari Ka Sawal + Book Ka Jawab

- **Sawal (Yuval Noah Harari):** pehli baar humein nahi pata 10 saal mein job market kaisa hoga →
  aaj naujawano ko kya sikhayein? Purana jawab "code sikhao" toot raha hai — AI khud code seekh raha
  hai, ek saal mein zyada tar code insaano se behtar likh sakta hai.
- **Book ka jawab:** syntax-writers mat banao. Woh log banao jo **machine ke upar** khare hain — jo
  **specify** karte hain kya banana hai, AI Workers ko **supervise** karte hain, aur jo wapas aya
  usay **verify** karte hain.

### Kaam teen hisson mein bat gaya

| Hissa | Kya | Kaun own karta hai |
| --- | --- | --- |
| **Intent** | kya banana hai, "correct" ka matlab | Human (Outcome Architect) |
| **Execution** | asal banana | AI Worker |
| **Verification** | jo aaya usay check karna | Human + checker systems |

> Syntax automate ho sakta hai. **Judgment, specification, deployment** nahi — yeh machine ke chadhne
> ke sath upar sarakte hain.

## B. Teen Levels, Ek Line

> Book tumhe **AI Workers (Digital FTEs)** banana sikhati hai, aur unhe jorr kar ek **company jo unpe
> chalti hai (AI-Native Company)**. Jo insaan yeh poora kar sakta hai, market usay **Forward Deployed
> Engineer (FDE)** kehti hai.

- **Person** = tum · **Unit** = AI Worker jo tum banate ho · **Enterprise** = un Workers ka jorr

## C. Baseline + 2 Modes

- **Foundations floor** — har reader browser tab se: prompting, do document languages (Markdown/HTML),
  "code you never write", skills & connectors, how to think in AI era. Koi install nahi. **Title
  nahi, farsh hai.**
- **Mode 1 Practitioner** — general agent se **apna** kaam tez karna (reason, write, code, analyze,
  plan, ship, session band). **Title nahi, proficiency.** Engineers → Claude Code / OpenCode; domain
  experts → Claude Cowork / OpenWork. Seven Principles of General Agent Problem Solving ke tehat.
- **Mode 2** — AI Workers **manufacture** karna. **Yahan job titles rehte hain.**

## D. The Generalist Core — Ek Pipeline (intent → production)

| Role | Owns | Kaam |
| --- | --- | --- |
| **Outcome Architect** | *what* | intent own karta hai, spec likhta hai, "correct" define karta hai, decide karta hai kaunse Workers banenge |
| **Digital FTE Builder** | *build* | **book ka primary graduate** — spec-driven dev, SKILL.md, agent architecture, tools/MCP, evaluation, human oversight, ship |
| **AI-Native Company Architect** | *system* | poori enterprise design (Two-Layer Model, management layer, workforce, nervous system, system of record). Agent Factory = process; AI-Native Company = product. Architect track ka credential. |
| **Cloud AI Engineer** | *run* | Workers + management layer + nervous system real cloud pe deploy/scale — Azure Container Apps (ship), Inngest (durable execution), Dapr + Kubernetes (scale) |

**The intent bottleneck:** pehle ~1 PM : 8 engineers. Agentic coding se har engineer ka output ~×5 →
wahi 1 insaan ab ~20 ka kaam feed karta hai. **Building scale hui, deciding nahi** → deciding hi
bottleneck. Book isay parhti hai: yeh woh lamha hai jab **Outcome Architect sabse ahm seat** ban
jaati hai.

## E. Forward Deployed Engineer (FDE)

- FDE = **wahi 4-role pipeline ek client ki company ke andar, end-to-end, ek embedded engineer se.**
- **"FDE batata hai tum kahan kaam karte ho, kya jaante ho woh nahi."** Apni company mein = 4 roles.
  Client ke andar = FDE. Client seedha hire kar le = **AI-Native Company Architect** (usually Cloud AI
  Engineer bhi). Sirf **vendor-neutral** FDE yeh trip kar sakta hai.
- Anthropic is role ko **"Applied AI Engineer"** kehta hai.

### History

- Palantir ne early 2010s mein banaya, pehle **"Deltas"**. ~2016 tak Palantir ke paas regular
  engineers se **zyada FDEs** the.
- Regular dev = *one capability, many customers*. FDE = *one customer, many capabilities*.
- Microsoft ne 2026 mein apni 6,000-person FDE unit launch karte hue **Palantir ko title ka credit**
  diya.

### Kevin Bai — "FDE 101"

- **2×2:** *product kitna technical* × *buyer kitna technical*. **Sirf ek cell ko FDE chahiye:
  technical product + non-technical buyer** (Palantir ka corner). Baaki teen: docs/devrel;
  self-serve; traditional sales-led.
- **Agentic turn:** har platform ab agentic → customizable → customer ko nahi pata product kitna door
  jaa sakta → **har vendor us ek cell mein**. Isi liye 2026 mein demand phati.
- **Contract value:** Palantir ~$4M average contract value (Fortune 500), ServiceNow ~$1.2M, Workday
  ~$600K, baaki koi public SaaS $500K se upar nahi. **Outcomes bechna seats bechne se alag price
  karta hai.**
- **Hiring test:** FDE = "customer-facing software engineer" — engineering bar par akele hire karo
  **aur** customer ke saamne trust karo. **Dono halves zaroori.**

### FDE ≠ Solutions Architect

| Solutions Architect | FDE |
| --- | --- |
| advise, demo, whiteboard, POC with sample data | **production code** customer ke infra pe, real data |
| deal close hone ke baad involvement wind down | **rukta hai jab tak customer ko real value na mile** |

**Test:** production mein customer-specific kaam chalana accountable = FDE. Product prove/explain
karna accountable = SA.

### Numbers (MCQ bait)

- **MIT Media Lab, Project NANDA (July 2025), "The GenAI Divide":** ~**95%** custom enterprise AI
  pilots ka koi **measurable return nahi** — AI kharab nahi, **integration into messy real-world
  systems** mushkil hai.
- Same report: outside partners ke sath ~**67%** deployment tak pahunchte hain vs in-house-only
  ~**33%** (report khud kehti hai: causation prove nahi hoti, preliminary, 6-month window).
- Postings **+729%** (Indeed: 643 → 5,330, April 2025 → April 2026). Median ~**$190K**; Anthropic FDE
  $200–300K; frontier-lab senior/staff $450–600K. **Koi sales quota nahi** — engineers ki tarah pay.
- Money on the table: OpenAI **"Deployment Company"** ~$4B · AWS **$1B** FDE unit (~45-day
  deployments, pods of 5–6) · Microsoft **Frontier Co. $2.5B / 6,000 log** (early: Unilever, Novo
  Nordisk) · McKinsey QuantumBlack Lead FDEs hire kar raha.
- **Aggarwal (Daksh/Fundamentum):** $100M business ~**100 FDEs** se (vs traditional 2,000–2,500),
  70–90% gross margin. "India can be the FDE factory for the world."
- **PwC:** billable-hour se hat raha, **"PwC One"** platform, 6 automated services.

### Vendor lock-in + "dev shop" objection

- Har vendor ka FDE us vendor ke platform pe build karta hai → **lock-in hi maqsad hai (vendor ke
  liye)**. Andrew Ng (The Batch): clients vendor-neutral FDE dhoondh nahi paate.
- Book **vendor-neutral FDE ka technical core** train karti hai. Consulting layer (discovery,
  prioritization, ROI framing, unrealistic ask par pushback) = **Business Strategist track**.
- **Objection (Bai ne khud uthaya):** bina shared primitives ke tum "dev shop of one" ho — har client
  pe bespoke code, maintenance margin kha jaayega.
- **Jawab — do Systems of Record jo FDE apne sath door se andar le jaati hai:**
  1. **The method** — yeh book, deep, already governed, website + MCP dono par. Har graduate ke paas
     **same**, har client par **identical** (Karachi accounting firm = Chicago accounting firm).
  2. **The profession / vertical System of Record** — **khud banati hai**: ek vertical, ek
     jurisdiction, committed domain expert se licensed (law, standards, derived procedures,
     invariants, decision map). **Engagement-dar-engagement motti hoti hai.** Sirf uske paas hai.
  - Dono **MCP bolte hain** → agent dono ek sath parhta hai. Koi integration kaam nahi.
- **Order:** *build first, sell second* — slice customer ka intezar nahi karti, woh customer
  **paida** karti hai. Portfolio = credential.

### Pod of one

- AWS pod = 5–6 log, ~45 din. Book compress karti hai: **1 human + Digital FTEs** (jo log pehle sath
  baithte the woh ab Workers hain).
- **Risk = bus factor of one** (Bai: single point of failure, chhutti pe gaya to engagement ruk
  gaya). Book ka jawab: **redundancy artifacts se, headcount se nahi** — spec, evals, governed
  corpus, deployed Worker + runbook. Test: 2 hafte tum ghayb, kya doosra graduate sirf tumhare repo
  se engagement uthaa le?

### Teesra darwaza — Freelance FDE

- Upwork ki dedicated FDE category: ~$2–5K pehli integration, $5–15K custom, $15K+ enterprise,
  $4–10K/mo retainer, $150–250/hr consulting.
- **Vendor-neutrality yahan entry requirement hai, differentiator nahi** — vendor ka FDE freelance
  kar hi nahi sakta.
- Retainer tier = Digital FTE subscription model bahar se chalaya.
- **Koi border nahi** — same contract Karachi, Lagos, Bangalore se clear hota hai. (Constraint: remote
  embedding remote coding se mushkil — over-communicate, client timezone, kabhi on-site.)

## F. Doosra Axis — Cherny Ke 5 Archetypes

Boris Cherny (Claude Code creator), June 2026 — job function nahi, **5 archetypes**:

| Archetype | Kaam | Is map ki seat se "rhyme" |
| --- | --- | --- |
| **Prototyper** | naye ideas, zyada tar ship nahi hote | Outcome Architect |
| **Builder** | prototype → production, fast | Digital FTE Builder |
| **Sweeper** | system simplify, UI clean, unship, optimize | Evals Engineer |
| **Grower** | built product ko product-market-fit tak iterate | (honestly unmapped) |
| **Maintainer** | mature system — secure, reliable, fast as it scales | Cloud AI Engineer + Supervisor |

- Archetypes **titles se bandhe nahi** — Anthropic mein designer/engineer/PM sab archetypes mein
  phaile hue hain. Zyada tar log **2–3 archetypes** span karte hain; team ka mix product ke phase se
  badalta hai (pre-PMF → pehle 3; mature → aakhri 3).
- **Roles batate hain kaam kahan hai. Tumhare archetypes batate hain kaunsi seat lena.**

## G. Baaki Roles

- **Subject Matter Expert as Skill Author** — accountant/lawyer/supply-chain expert jo tacit judgment
  ko **SKILL.md** mein encode karta hai (plain-text file jo agent load karke follow karta hai), phir
  test karta hai agent ke calls uske calls se match karte hain, aur revise karta hai jab tak match na
  ho. FDE ki 2nd System of Record **bina author ke exist nahi kar sakti** — dono ek dusre ko chahiye.
  (Market signal: Yousuf Imran, Google AE, ~$986K/yr chhod kar Mangosteen Studio banaya.)
- **Connector and Plugin Engineer** — ek job, do addresses; dono ke neeche **MCP server**:
  - **connector-native app** — claude.ai chat app ko *end users* ke liye extend: remote MCP server,
    tools, stored state, real sign-in, fail-closed session gate. Ek pasted URL se stranger add karta
    hai; ab **model khud tumhara customer** hai.
  - **plugin** — coding agent (Claude Code, OpenCode) ko *builders* ke liye extend: skills,
    subagents, hooks, MCP servers — ek install ke peeche. Deterministic **hook** = advice (jo model
    skip kar sakta hai) aur rule (jo har baar chalti hai) ke beech ki line.
- **Supporting roles:**
  - **Evals Engineer** — Workers ko live jaane se pehle crash-test. Core curriculum, add-on nahi.
  - **AI Governance Officer** — company-level rules likhta hai: AI khud kya decide kare, kya human ko
    jaaye, kya kabhi na chhue; regulations ki mapping (fair lending, patient privacy, data
    residency). Architect **system banata hai jo rules enforce kare**; Governance Officer **rules
    kya hon** decide karta hai.
  - **Digital FTE Supervisor** — human-in-the-loop; reviewer/approver; **jiska naam audit trail par**
    jab kuch ghalat ho. Builder nahi — roz-marra chalane wala.

## H. Jahan Book Janboojh Kar Rukti Hai

| Role | Book kya karti hai | Book kya nahi |
| --- | --- | --- |
| **LLMOps Engineer** | fine-tuning hands-on — **last resort**, default nahi (ek model snapshot se bandh deta hai, optionality kha jaata hai) | **foundation model pre-training from scratch** — out of scope (commoditizing) |
| **Harness Engineer** | koi bhi runtime fluently use karna, portable rehna | runtime **build** karna |
| **AI Data Engineer** | agent-facing data layer (Postgres, pgvector, MCP as spine) | general pipeline / warehouse engineering |

## I. Appendix — FDE Résumé + Interview (exam mein aa sakta hai)

**6 résumé signals** — pehle 3 "kya tumne deliver kiya": shipped production systems · quantifiable
impact (numbers mein) · direct customer exposure. Aakhri 3 "kaise deliver karte ho": messy-data work
· ownership under ambiguity · AI/LLM depth (RAG, agents, evals).
Rewrites: activity → outcome ("built ETL" → "cut month-end close 5 days → 2"); "I" likho "we" nahi;
competitive-programming awards kaato, portfolio lagao.

**Interview loop** (5–8 stages, 3–6 hafte). Do rounds faislе karte hain:
- **Decomposition case study** — vague enterprise problem (60 min). **Sabse aam rejection = jawab dena.**
  Score karta hai: goal clarify, stakeholders + success metric, data map + owners, subproblems by
  risk, thinnest end-to-end skeleton first, assumptions loud, failure modes unprompted. = **spec-driven
  development verbally.**
- **Client simulation** — interviewer frustrated/non-technical customer role-play karta hai; buri
  khabar deni hai, governance-compromising request par pushback, "100% accuracy promise nahi kar
  sakte" bina jargon.
- **5 red flags:** solving before clarifying · cost/constraints ignore · thin deployment story (API
  fail hui to kya) · regulated domain mein zero compliance vocabulary · no customer instinct.

---

## MCQ Practice (jawab neeche)

1. Harari ke sawal ka book ka core jawab kya hai?
   a) Sabko Python sikhao b) Syntax ke bajaye judgment/specification/deployment sikhao
   c) Sirf FDE banao d) AI par bharosa mat karo

2. Kaam ke teen hisson mein AI Worker kaunsa own karta hai?
   a) Intent b) Execution c) Verification d) Teenon

3. "Intent bottleneck" ka matlab:
   a) AI slow hai b) Building scale hui lekin deciding-what-to-build nahi → decide karna bottleneck
   c) Engineers ki kami d) Prompts lambe ho gaye

4. Core pipeline ka sahi order (intent → production):
   a) Builder → Architect → Outcome Architect → Cloud AI Engineer
   b) Outcome Architect → Digital FTE Builder → AI-Native Company Architect → Cloud AI Engineer
   c) Cloud AI Engineer → Builder → Outcome Architect → Architect
   d) Outcome Architect → Cloud AI Engineer → Builder → Architect

5. "FDE" asal mein kya describe karta hai?
   a) Ek skill set b) Ek certification c) Tum kahan kaam karte ho (embedded inside a client)
   d) Ek programming language

6. Bai ke 2×2 mein FDE sirf kis cell mein zaroori hai?
   a) Technical product + technical buyer b) Configurable product + technical buyer
   c) Configurable product + non-technical buyer d) Technical product + non-technical buyer

7. MIT NANDA ka ~95% figure kis baare mein hai?
   a) AI models jo kaam nahi karte b) Custom enterprise AI pilots jinka koi measurable return nahi
   c) FDEs jo fail hote hain d) Companies jo AI use nahi kartin

8. Vendor-neutral FDE ki do Systems of Record:
   a) Do alag models b) The method (diya gaya) + the profession/vertical SoR (khud banaya)
   c) Do clients d) Code repo + docs

9. "Dev shop of one" objection ka core kya hai?
   a) FDE akela kaam nahi kar sakta b) Bina shared primitives ke har client pe bespoke code →
   maintenance margin kha jaata hai c) Clients FDE ko pasand nahi karte d) FDE bahut mehnga hai

10. Solutions Architect aur FDE ka sabse saaf farq-test:
    a) Salary b) Degree c) SA product prove/explain karta hai; FDE production mein customer-specific
    kaam chalana accountable hai d) SA remote, FDE on-site

11. Book fine-tuning ke baare mein kya kehti hai?
    a) Default approach b) Kabhi mat karo c) Last resort — sirf jab prompting/context/tools/retrieval
    genuinely kam pad jayein d) Sirf Architect track mein

12. Anthropic FDE role ko kya title deta hai?
    a) Forward Deployed Engineer b) Solutions Engineer c) Applied AI Engineer d) Deployment Architect

13. Cherny ke 5 archetypes ke baare mein sahi:
    a) Yeh job titles hain b) Har banda exactly ek archetype hai c) Titles se bandhe nahi, zyada tar
    log 2–3 span karte hain, mix product phase se badalta hai d) Sirf engineers ke liye

14. AI Governance Officer vs AI-Native Company Architect:
    a) Same role b) Governance Officer rules kya hon decide karta hai; Architect system banata hai jo
    unhe enforce kare c) Architect rules likhta hai d) Governance Officer code likhta hai

15. Connector-native app aur plugin dono ke neeche kaunsa artifact hai?
    a) REST API b) MCP server c) GraphQL d) Webhook

### Jawab Key

1‑b · 2‑b · 3‑b · 4‑b · 5‑c · 6‑d · 7‑b · 8‑b · 9‑b · 10‑c · 11‑c · 12‑c · 13‑c · 14‑b · 15‑b

---
[⬅ 00 — Exam Facts + Plan](00-exam-facts-and-plan.md) · [Agla: 02 — Agent Factory Ecosystem ➡](02-agent-factory-ecosystem.md)
