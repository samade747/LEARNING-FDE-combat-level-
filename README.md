# LEARNING-FDE-combat-level-

*Mixed Roman Urdu + English notes on Panaversity's "The AI Agent Factory" book — end goal:
combat-level Forward Deployed Engineer (FDE).*

---

## 🎯 Yeh Repo Kis Baare Mein Hai

Yeh repo **[The AI Agent Factory](https://agentfactory.panaversity.org)** book se guzarte hue banayi
gayi study notes ka collection hai — har chapter ka apna `docs/[slug]/` folder (README index +
numbered concept-part files), mixed **Roman Urdu + English** mein, taake seekha hua content dobara
parhna aasan ho.

Book ka apna sawal yeh hai: **agar hume nahi pata agle 10 saal mein job market kaisi hogi, to aaj kya
sikhayein?** Iska jawab syntax nahi hai (AI khud code likhna seekh rahi hai) — jawab hai woh log jo
machine ke **upar** khare hote hain: jo specify karte hain kya banana hai, AI Workers ko supervise
karte hain jo usay banate hain, aur jo wapis aya usay verify karte hain. **Yehi discipline is repo ka
maqsad hai.**

## 🧑‍💻 Forward Deployed Engineer (FDE) Kya Hai

Zyada tar software engineers headquarters par product banate hain aur us customer se kabhi nahi milte
jo usay use karta hai. **FDE iska ulta karta hai:** customer ki asal workplace par jata hai, unke sath
baith kar unke real problems samajhta hai, aur **wahin, on-site**, unke platform par solution banata
hai — koi demo nahi, koi slide deck nahi, **real environment mein chalta hua software.**

> Doctor ki misal: ek doctor jo doosre shehar se aapka chart parhta hai, aur ek doctor jo room mein
> baith kar khud examine karta hai aur turant treatment shuru karta hai. **FDE doosra doctor hai.**

Yeh role Palantir ne 2010s ke shuru mein banaya (pehle "Deltas" kehte the) — unke customers (government
agencies, bare enterprises) ko koi chahiye tha jo on-site baith kar bureaucracy cut kar sake. Ab market
mein isi role ki demand explode ho rahi hai: **postings 1 saal mein 729% barhi hain, median pay ~$190K
ke qareeb hai.** Microsoft ne 2026 mein apni 6,000-person FDE unit launch ki, Palantir ko is title ka
credit dete hue. Anthropic isi role ko "Applied AI Engineer" kehta hai.

**Book ka poora curriculum isi ladder ke seats banata hai** — problem samajhna (Mode 1), phir agent
workforce manufacture karna (Mode 2) — taake aap "vendor-neutral" FDE ban sako: jo kisi ek company ke
platform tak limited nahi, balke poori discipline (harness, loop, eval, deployment, payments) apne
sath har client tak le ja sakta hai.

---

## 🗺️ Poori Book Ka Naqsha — Kya Cover Hua, Kya Baqi Hai

Book 3 bare hisson mein hai: **Front Matter** (why/what/roles), **The Ecosystem** (platform/business
model), aur **Getting Started: Crash Courses** (asal skill-building curriculum, 6 groups mein).
Neeche har chapter ka status hai — ✅ = is repo mein `docs/` ke andar poori tarah note ki gayi,
🔲 = book mein hai lekin abhi is repo mein nahi.

### Front Matter (Why This Book Exists)

| # | Chapter | Status |
| --- | --- | --- |
| 1 | About: What is this thing I'm holding? | 🔲 |
| 2 | How to Learn from This Book | 🔲 |
| 3 | The Roles This Book Trains *(FDE ki definition yahan hai)* | 🔲 |
| 4 | Preface: Why now, what's at stake | 🔲 |
| 5 | AI Is Non-Negotiable: Answering the Objections | 🔲 |
| 6 | Thesis: The Architectural Argument | 🔲 |
| 7 | The Operating Layer: The Interface Argument | 🔲 |
| 8 | What You Carry In: The Ownership Argument | 🔲 |
| 9 | Getting Paid as a Vertical FDE | 🔲 |
| 10 | Selling as a Vertical FDE | 🔲 |
| — | Courses & Certifications | ✅ [`docs/certifications`](docs/certifications/README.md) |
| — | Glossary | 🔲 |

### The Ecosystem (Platform + Business Model)

| # | Chapter | Status |
| --- | --- | --- |
| 1 | The Agent Factory Ecosystem (overview) | 🔲 |
| 2 | Choosing Your Vertical | 🔲 |
| 3 | The Ecosystem Concept | 🔲 |
| 4 | **The Forward Deployed Engineer Agent Factory Model** | 🔲 |
| 5 | Agent Factory System of Record | 🔲 |
| 6 | The System of Context: Connecting the Records to Real Work | 🔲 |
| 7 | Designing the Vertical System of Record from First Principles | 🔲 |
| 8 | Zia Tutor AI | 🔲 |
| 9 | Zia Developer AI | 🔲 |

### Getting Started: Crash Courses

#### Group 1 — Foundations (Everyone)

| # | Chapter | Status |
| --- | --- | --- |
| 1 | What AI Actually Is: A Crash Course | 🔲 |
| 2 | AI Prompting in 2026: A Crash Course | 🔲 |
| 3 | Markdown In, HTML Out: A Crash Course | 🔲 |
| 4 | Code You Never Write: A Crash Course | 🔲 |
| 5 | Skills & Connectors: Teach AI Once, Connect It to Your Apps | 🔲 |
| 6 | How to Think in the AI Era: Crash Course | 🔲 |

#### Group 2 — General Agents (12/12 ✅ Complete)

| # | Chapter | Status | Notes |
| --- | --- | --- | --- |
| 1 | General Agents on the Web | ✅ | [`docs/general-agents-web`](docs/general-agents-web/README.md) |
| 2 | Open Source LLMs | ✅ | [`docs/open-source-llms`](docs/open-source-llms/README.md) |
| 3 | Claude Code and OpenCode | ✅ | [`docs/agentic-coding`](docs/agentic-coding/README.md) |
| 4 | Cowork and OpenWork | ✅ | [`docs/cowork`](docs/cowork/README.md) |
| 5 | Made, Not Generated (Website Design) | ✅ | [`docs/website-design`](docs/website-design/README.md) |
| 6 | Spec-Driven Development | ✅ | [`docs/spec-driven-development`](docs/spec-driven-development/README.md) |
| 7 | The Four Layers: Prompt, Context, Harness, Loop | ✅ | [`docs/four-layers`](docs/four-layers/README.md) |
| 8 | Loop Engineering | ✅ | [`docs/loop-engineering`](docs/loop-engineering/README.md) + root [`Loop-Engineering-Summary.md`](Loop-Engineering-Summary.md) + [`Loop-Engineering-Final-Prep.md`](Loop-Engineering-Final-Prep.md) |
| 9 | Harness Engineering | ✅ | [`docs/harness-engineering`](docs/harness-engineering/README.md) |
| 10 | Graph Engineering | ✅ | [`docs/graph-engineering`](docs/graph-engineering/README.md) |
| 11 | Trusting the Checker (Evals) | ✅ | [`docs/trusting-the-checker`](docs/trusting-the-checker/README.md) |
| 12 | Leaving the Laptop (Runtime) | ✅ | [`docs/leaving-the-laptop`](docs/leaving-the-laptop/README.md) |

#### Group 3 — Personal Agent Harnesses (2/2 ✅ Complete)

| # | Chapter | Status | Notes |
| --- | --- | --- | --- |
| 1 | OpenClaw with General Agents | ✅ | [`docs/openclaw`](docs/openclaw/README.md) |
| 2 | Hermes with General Agents | ✅ | [`docs/hermes`](docs/hermes/README.md) |

#### Group 4 — Mode 1: Problem-Solving (3/3 ✅ Complete)

| # | Chapter | Status | Notes |
| --- | --- | --- | --- |
| 1 | Is This an Agent Problem? | ✅ | [`docs/is-this-an-agent-problem`](docs/is-this-an-agent-problem/README.md) |
| 2 | Problem Solving with General Agents | ✅ | [`docs/problem-solving-crash-course`](docs/problem-solving-crash-course/README.md) |
| 3 | From One-Off to Worker: The Handoff to Manufacturing | ✅ | [`docs/from-one-off-to-worker`](docs/from-one-off-to-worker/README.md) |

#### Group 5 — Mode 2: Manufacturing (18/18 ✅ Complete)

**Phase 1 · Building Blocks (6/6)**

| # | Chapter | Status | Notes |
| --- | --- | --- | --- |
| 1 | Python in the AI Era | ✅ | [`docs/python-crash-course`](docs/python-crash-course/README.md) |
| 2 | Connector-Native Apps (Remote MCP Server) | ✅ | [`docs/connector-native-apps`](docs/connector-native-apps/README.md) |
| 3 | RAG on Postgres with pgvector | ✅ | [`docs/postgres-ai-crash-course`](docs/postgres-ai-crash-course/README.md) |
| 4 | Building the Context Layer | ✅ | [`docs/context-layer-crash-course`](docs/context-layer-crash-course/README.md) |
| 5 | Plugins for AI Agents | ✅ | [`docs/plugins-crash-course`](docs/plugins-crash-course/README.md) |
| 6 | AI Identity: Human Sign-In and Agent Access | ✅ | [`docs/ai-identity-crash-course`](docs/ai-identity-crash-course/README.md) |

**Phase 2 · Build Workers (3/3)**

| # | Chapter | Status | Notes |
| --- | --- | --- | --- |
| 1 | Build AI Agents with the OpenAI Agents SDK | ✅ | [`docs/build-agents-crash-course`](docs/build-agents-crash-course/README.md) |
| 2 | Building a Digital FTE | ✅ | [`docs/digital-fte-crash-course`](docs/digital-fte-crash-course/README.md) |
| 3 | Give Your AI Agent a Nervous System | ✅ | [`docs/ai-agent-nervous-system-crash-course`](docs/ai-agent-nervous-system-crash-course/README.md) |

**Phase 3 · Scale the Workforce (9/9)**

| # | Chapter | Status | Notes |
| --- | --- | --- | --- |
| 1 | Human-Agent Teams | ✅ | [`docs/human-agent-teams-crash-course`](docs/human-agent-teams-crash-course/README.md) |
| 2 | Designing Agent Experiences | ✅ | [`docs/designing-agent-experiences-crash-course`](docs/designing-agent-experiences-crash-course/README.md) |
| 3 | Building a Workforce with Paperclip | ✅ | [`docs/workforce-with-paperclip-crash-course`](docs/workforce-with-paperclip-crash-course/README.md) |
| 4 | A Self-Expanding Workforce with Paperclip | ✅ | [`docs/dynamic-workforce-crash-course`](docs/dynamic-workforce-crash-course/README.md) |
| 5 | Build Your Identic AI Chief of Staff | ✅ | [`docs/identic-ai-crash-course`](docs/identic-ai-crash-course/README.md) |
| 6 | Eval-Driven Development for AI Employees | ✅ | [`docs/eval-driven-development-crash-course`](docs/eval-driven-development-crash-course/README.md) |
| 7 | Deploy Your Agent Harness to the Cloud | ✅ | [`docs/deploying-agents-crash-course`](docs/deploying-agents-crash-course/README.md) |
| 8 | Choosing Agentic Architectures | ✅ | [`docs/choosing-agentic-architectures-crash-course`](docs/choosing-agentic-architectures-crash-course/README.md) |
| 9 | Payment-Enabled Agents (ACP, AP2, x402, MPP) | ✅ | [`docs/payment-enabled-agents-crash-course`](docs/payment-enabled-agents-crash-course/README.md) |

#### Group 6 — References & Companions

| # | Chapter | Status |
| --- | --- | --- |
| 1 | Which AI Employees To Use in 2026? | 🔲 |
| 2 | Cheatsheets | 🔲 |
| 3 | Agentic Engineering Fundamentals (45-min crash course) | 🔲 |

---

## 📊 Overall Progress

```
Front Matter (12 docs)              █░░░░░░░░░░░  1/12
The Ecosystem (9 docs)              ░░░░░░░░░░░░  0/9
Foundations — Everyone (6)          ░░░░░░░░░░░░  0/6
General Agents (12)                 ████████████  12/12 ✅
Personal Agent Harnesses (2)        ████████████  2/2   ✅
Mode 1 — Problem-Solving (3)        ████████████  3/3   ✅
Mode 2 — Manufacturing (18)         ████████████  18/18 ✅
References & Companions (3)         ░░░░░░░░░░░░  0/3

TOTAL COVERED: 36 / 65 chapters
```

**Poora Mode 1 + Mode 2 + General Agents + Personal Agent Harnesses group (35 chapters) is repo mein
note ho chuka hai** — yehi book ka core skill-building spine hai (problem se worker tak, worker se
poori manufactured workforce tak). Plus **Courses & Certifications** (Front Matter ka `— |` row) —
PCAR-F/CCAR-F certification pathway, 2026-08-24 ko naye "pass PCAR-F by 2026-10-05" goal ki wajah se
priority mein note kiya gaya. Front Matter ke baaqi 11, The Ecosystem, Foundations, aur References &
Companions groups (29 chapters) abhi baqi hain — yeh zyada tar "why/business-model/reference" material
hai, core hands-on curriculum nahi.

> ⚠️ **Known staleness:** Is table ke Front Matter/Foundations rows abhi bhi kuch jagah 🔲 dikhate hain
> jab ke `docs/roles-this-book-trains/`, `docs/ai-prompting-2026/`, `docs/what-you-carry-in/`,
> `docs/what-ai-actually-is-crash-course/`, `docs/markdown-html-crash-course/` jaisi folders **already
> poori documented hain**. Yeh `docs/certifications/03-exam-domains.md` banate waqt discover hua —
> poora audit abhi baaqi hai (dekho `progress.md`).

---

## 📁 Repo Structure

```
docs/[chapter-slug]/
  README.md          ← chapter overview + index of parts
  00-*.md, 01-*.md…  ← numbered concept-part files, book ke apne sections follow karte hue

Loop-Engineering-Summary.md      ← Loop Engineering ka aasan overview (root)
Loop-Engineering-Final-Prep.md   ← Loop Engineering ka poora prep guide, real code example ke sath
progress.md                       ← is learning-journey ki apni spine (loop engineering se seekha pattern)
todolist.md                       ← active/done/backlog task list
```

Har doc mixed **Roman Urdu + English** mein hai, book ke Zia Tutor AI MCP connector se full content
nikaal kar likha gaya hai — training-knowledge se nahi, seedha book se.
