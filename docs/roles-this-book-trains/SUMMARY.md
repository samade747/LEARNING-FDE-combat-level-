# The Roles This Book Trains — Summary

Front Matter Chapter 3/12. Harari ke sawal ka jawab: syntax-writers train mat karo, un logon ko train
karo jo machine se upar khare hain — specify karte, supervise karte, verify karte. Chapter ek core
pipeline ke ird gird ghumta hai (Outcome Architect → Digital FTE Builder → AI-Native Company Architect →
Cloud AI Engineer) aur uska vendor-neutral field version: **Forward Deployed Engineer (FDE)**.

## 00 — The Question Behind Every Title

- **Harari ka sawal:** pehli baar history mein nahi pata das saal baad job market kaisi hogi — purana
  jawab ("code sikhao") toot raha hai kyunki AI khud code seekh raha hai. Jawab: judgment, specification,
  deployment automate nahi ho sakte.
- **3 levels:** insan (aap) → unit (AI Worker jo aap banate ho) → enterprise (company jo Workers se bani
  hai). "FDE" batata hai aap **kahan** kaam karte ho, kya jaante ho yeh nahi.
- **Baseline:** Foundations (prompt, document languages, code jo khud nahi likhte, skills/connectors, AI-
  era thinking) — koi mode/role/install nahi, poore naqshe ka floor. Mode 1 Practitioner: title nahi,
  proficiency — general agent se apna kaam tez karna, Seven Principles of General Agent Problem Solving
  ke tehat.

## 01 — The Generalist Core

- **4 core roles, ek pipeline:** Outcome Architect (kya) → Digital FTE Builder (build) → AI-Native
  Company Architect (system) → Cloud AI Engineer (run).
- **Outcome Architect:** intent ka malik, execution ka nahi. Product managers ka ratio (1:8 se ab
  1:20+) barh gaya hai kyunki building scale hui, deciding nahi — deciding bottleneck ban gayi.
  Book yeh spec-driven development se train karti hai.
- **Digital FTE Builder:** market "AI Engineer" kehti hai; book ka sharper naam Digital FTE — unit jis
  se company assemble hoti hai. Spine: spec-driven dev, SKILL.md authoring, agent architecture, tool/MCP
  interfaces, evaluation, human oversight.
- **AI-Native Company Architect:** poora enterprise design karta hai (Two-Layer Model, management layer,
  workforce, nervous system, system of record). Agent Factory = process; AI-Native Company = product.
  Credential: 5-quarter Certified Agentic AI Architect program.
- **Cloud AI Engineer:** production mein chalata hai (Azure Container Apps, Inngest, Dapr/Kubernetes) —
  prototype se dependable company tak.

## 02 — The FDE: Why Palantir Needed It

- FDE = customer ki asal workplace mein embed, on-site working software banata hai — demo/slide-deck
  nahi. Palantir ne 2010s mein banaya ("Deltas"); 2016 tak normal engineers se zyada FDEs. Regular
  developer = ek capability, kai customers; FDE = ek customer, kai capabilities.
- **Kevin Bai's "FDE 101":** software bechna problem nahi thi — outcome becho, hours nahi. Contract
  value proof: Palantir ~$4M avg vs ServiceNow ~$1.2M vs Workday ~$600K.
- **2×2 test:** technical product/non-technical buyer = **sirf yehi cell** FDE zaroori karta hai (3/4
  cells ko forward deployment chahiye nahi).
- FDE vs Solutions Architect: SA advise/demo karta hai (deal close hote hi khatam); FDE production tak
  rehta hai. Example: OpenAI + John Deere See & Spray — 70% chemical use reduction, planting calendar
  par kaam.
- Hiring test: engineering bar par akela hire ho jaye AND customer ke saamne bhi bhej sako.

## 03 — The FDE: Market Demand and the Services Industry

- **Demand numbers:** FDE postings 800%+ barhin 2025 Q1-Q3; Salesforce dedicated team; OpenAI Deployment
  Company (~$4B backed); AWS $1B commit + Microsoft $2.5B/6,000 log — ek hafte mein $3.5B combined.
- **MIT Project NANDA (2025):** ~95% custom enterprise AI pilots koi measurable return nahi dete — fit
  karna mushkil hai, AI ki kami nahi. Outside partners ~67% deployment tak pohanchte vs in-house ~33%.
  Vendor-neutral "teesra column" abhi almost-empty.
- **Salary numbers:** Indeed postings 643→5,330 (April 2025→2026, 729% izafa), bands $170-200K+,
  Anthropic $200-300K, market median ~$190K, senior/staff frontier labs $450-600K. Supply gap: postings
  800%+, candidate pool ~50%. Koi role sales-quota wala nahi.
- **Services industry:** Sanjeev Aggarwal — ~100 FDEs se $100M business (70-90% gross margins) jo
  traditional IT services 2,000-2,500 logon se karta tha; "India can be the FDE factory for the world."
  PwC (Paul Griggs) billable-hour se hat kar PwC One (6 automated services) — naya cage bhi.
- **Cursor's playbook (Pauline Brunet):** Fit test (immature customer + deep customization), staff-
  augmentation red flag, directional scope (6-week plans, na open-ended na fixed-waterfall), ROI 3
  questions (revenue/cost/risk).
- **Vendor lock-in problem:** har FDE apne vendor ke platform mein client ko lock karta hai. Book
  vendor-neutral FDE train karti hai — optionality feature hai, bug nahi.
- **Strongest objection (Bai):** bina shared primitives, dozens unmaintained repos — maintenance cost
  profit khatam karti hai.

## 04 — What Fills the Pod: Two Systems of Record

- **2 Systems of Record travel karte hain:** (1) Method (jo khud nahi banaya) — book khud, MCP par
  serve, har graduate ke liye identical. (2) Profession (jo khud banaya) — vertical/jurisdiction ka
  governed corpus, kisi aur ke paas nahi.
- Dev-shop objection ka jawab: dono shared primitives hain, koi code fork nahi hoti — governed corpus
  maintain hota hai, code nahi.
- "Mota hona": jo generalize hota hai vertical System of Record mein jata hai (vendor platform mein
  nahi) — doosra client pehle se sasta serve hota hai.
- **Pod of one:** AWS ka 5-6-engineer pod (~45 din) ek graduate + Digital FTEs workforce mein simat jata
  hai. Risk: bus factor of one — test: 2 hafte unreachable ho to koi doosra repository se pick kar sake?
  Risk artifacts mein move hota hai (spec, evals, corpus, runbook), insan ke sar se nahi.
- **Teesra darwaza — Freelance FDE:** Upwork category — $2-5K first integration, $5-15K custom, $15K+
  enterprise, $4-10K/month retainer, $150-250/hr consulting; UK £600-750/din mid, £1,200-2,000/din
  principal. Category exists, supply nahi — opening hai. Native market vendor-neutral FDE ka, no border.
- **Directly hire:** client jab FDE ko hire kar le, naam "AI-Native Company Architect" ban jata hai —
  same skills, address badal jata hai, ek step khoye bina.

## 05 — The Skill Author, and the Connector/Plugin Engineer

- **Subject Matter Expert as Skill Author:** tacit judgment ko SKILL.md mein encode karna, agent ke
  decisions ko match karwana, revise karna. Digital FTE ka "knowledge engine". Market ne is role ko naam
  nahi diya. Example: Yousuf Imran — Google account exec (~$986K/saal commissions) ne resign kiya AI
  product lab banane ke liye — apni judgment factory apne paas rakhi.
- Do "unnamed" roles ek doosre ki zaroorat rakhte hain: vendor-neutral FDE ka doosra SoR skill author
  bina exist nahi ho sakta, aur skill author ko governed ghar chahiye.
- **Connector aur Plugin Engineer:** ek job, do addresses — MCP engineer/integrations/connector/plugin/
  agent-tooling engineer sab same. Connector-native app = claude.ai extend (remote MCP server, tools/
  state/sign-in). Plugin = coding agent extend (skills/subagents/hooks/MCP behind one install).
  Deterministic hook = "advice model skip kar sake" aur "rule jo har baar chale" ke darmiyan line.

## 06 — The Supporting Roles, and Where the Book Deliberately Stops

- **3 Supporting roles:** Evals Engineer (Worker ka crash-test), AI Governance Officer (limits set karta,
  industry regulations map karta), Digital FTE Supervisor (day-to-day accountable insan, worker ka
  banane wala nahi).
- **Jahan book jaan-boojh kar rukti hai:**
  - LLMOps Engineer — model tak, model khud nahi; fine-tune last resort hai (optionality khatam karta),
    default nahi; foundation model pre-training scope se bahar (commoditizing hai).
  - Harness Engineer — runtime use karte ho, banate nahi; portability discipline important, runtime
    khud banana job nahi.
  - AI Data Engineer — agent-facing data layer (Postgres/pgvector/MCP) adjacent hai, central nahi.

## 07 — The Second Axis: Your Type — Plus the FDE Résumé and Interview

- **Boris Cherny's 5 archetypes** (job function nahi): Prototyper, Builder, Sweeper, Grower, Maintainer —
  titles se bandhe nahi, zyada tar log 2-3 archetypes mein failte hain. Rough rhyme mapping: Outcome
  Architect=Prototyper, Digital FTE Builder=Builder, Evals Engineer=Sweeper, Cloud AI Engineer/Supervisor
  =Maintainer.
- **Appendix A — FDE Résumé, 6 Signals:** shipped production systems, quantifiable impact, direct
  customer exposure (kya deliver kiya); messy-data work, ownership under ambiguity, AI/LLM depth (kaise
  deliver karte ho). 3 rewrites: activity→outcome, "I" not "we", competitive-programming awards kaato
  (portfolio se replace: deployed Worker/shipped plugin/live connector). Lead item: governed slice of a
  profession.
- **Appendix B — FDE Interview:** 5-8 stages, 3-6 hafte — recruiter screen, hiring-manager screen,
  practical coding, system-design, **decomposition case study** (filter round — vague enterprise problem,
  60 min; jawab "seedha solve" karna sabse aam rejection; sequence hai clarify→stakeholders→data-map→
  decompose→skeleton), client simulation (2nd filter — 5 red flags), naya format "the live build" (3
  ghante: requirements→build→present, no LeetCode).
- **Appendix C — table:** har interview round book mein kahan train hota hai (spec-driven development,
  Python in the AI Era, RAG/agents/evals courses, Thesis Invariants, Human-Agent Teams, Claude Code/
  OpenCode, capstones).
