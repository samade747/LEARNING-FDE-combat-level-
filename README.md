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
| 1 | About: What is this thing I'm holding? | ✅ [`docs/about`](docs/about/README.md) |
| 2 | How to Learn from This Book | ✅ [`docs/how-to-learn-from-this-book`](docs/how-to-learn-from-this-book/README.md) |
| 3 | The Roles This Book Trains *(FDE ki definition yahan hai)* | ✅ [`docs/roles-this-book-trains`](docs/roles-this-book-trains/README.md) |
| 4 | Preface: Why now, what's at stake | ✅ [`docs/preface-agent-native`](docs/preface-agent-native/README.md) |
| 5 | AI Is Non-Negotiable: Answering the Objections | ✅ [`docs/why-ai-is-non-negotiable`](docs/why-ai-is-non-negotiable/README.md) |
| 6 | Thesis: The Architectural Argument | ✅ [`docs/thesis`](docs/thesis/README.md) |
| 7 | The Operating Layer: The Interface Argument | ✅ [`docs/the-agent-is-the-operating-layer`](docs/the-agent-is-the-operating-layer/README.md) |
| 8 | What You Carry In: The Ownership Argument | ✅ [`docs/what-you-carry-in`](docs/what-you-carry-in/README.md) |
| 9 | Getting Paid as a Vertical FDE | ✅ [`docs/how-to-get-paid`](docs/how-to-get-paid/README.md) |
| 10 | Selling as a Vertical FDE | 🔲 not started |
| — | Courses & Certifications | ✅ [`docs/certifications`](docs/certifications/README.md) (+ [CCAR-F Track B chapter](docs/ccar-f-fde-track-b/README.md), local-runnable practicum scaffolds) |
| — | Glossary | 🔲 not started — bara reference chapter (~36K tokens, 15 term-category sections) |

### The Ecosystem (Platform + Business Model)

| # | Chapter | Status |
| --- | --- | --- |
| 1 | The Agent Factory Ecosystem (overview) | ✅ [`docs/ecosystem-overview`](docs/ecosystem-overview/README.md) |
| 2 | Choosing Your Vertical | ✅ [`docs/ecosystem-choosing-your-vertical`](docs/ecosystem-choosing-your-vertical/README.md) |
| 3 | The Ecosystem Concept | ✅ [`docs/ecosystem-ecosystem-concept`](docs/ecosystem-ecosystem-concept/README.md) |
| 4 | **The Forward Deployed Engineer Agent Factory Model** | ✅ [`docs/ecosystem-fde-af-model`](docs/ecosystem-fde-af-model/README.md) |
| 5 | Agent Factory System of Record | ✅ [`docs/ecosystem-system-of-record`](docs/ecosystem-system-of-record/README.md) |
| 6 | The System of Context: Connecting the Records to Real Work | 🔲 not started |
| 7 | Designing the Vertical System of Record from First Principles | ✅ [`docs/ecosystem-designing-the-vertical-sor`](docs/ecosystem-designing-the-vertical-sor/README.md) (2026-08-27: rebuilt from the book's own lesson, not the PDF — full method, 7 templates, 2 appendices, 59-Q quiz, practice project) + standalone [`docs/ksor`](docs/ksor/README.md) reference (quiz + 3 practice scaffolds) |
| 8 | Zia Tutor AI | ✅ [`docs/ecosystem-zia-tutor-ai`](docs/ecosystem-zia-tutor-ai/README.md) |
| 9 | Zia Developer AI | ✅ [`docs/ecosystem-zia-developer-ai`](docs/ecosystem-zia-developer-ai/README.md) |

### Getting Started: Crash Courses

#### Group 1 — Foundations (Everyone)

| # | Chapter | Status |
| --- | --- | --- |
| 1 | What AI Actually Is: A Crash Course | ✅ [`docs/what-ai-actually-is-crash-course`](docs/what-ai-actually-is-crash-course/README.md) |
| 2 | AI Prompting in 2026: A Crash Course | ✅ [`docs/ai-prompting-2026`](docs/ai-prompting-2026/README.md) |
| 3 | Markdown In, HTML Out: A Crash Course | ✅ [`docs/markdown-html-crash-course`](docs/markdown-html-crash-course/README.md) |
| 4 | Claude and ChatGPT 101: A Crash Course | 🔲 not started |
| 5 | AI Fluency: A Crash Course | 🔲 not started |
| 6 | Code You Never Write: A Crash Course | 🔲 not started |
| 7 | Skills & Connectors: Teach AI Once, Connect It to Your Apps | 🔲 not started |
| 8 | How to Think in the AI Era: Crash Course | 🔲 not started |

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
| 10 | Graph Engineering | ✅ | [`docs/graph-engineering`](docs/graph-engineering/README.md) + root [`Graph-Engineering-Summary.md`](Graph-Engineering-Summary.md) |
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

*Audited 2026-08-25 against `outline_agent_factory` (live book structure) + actual disk state, corrected
2026-08-26 (Foundations-Everyone actually has 8 lessons not 6 — 2 more found: AI Fluency, Claude and
ChatGPT 101) — dekho [`progress.md`](progress.md) is audit ki poori detail ke liye.*

```
Front Matter (12 docs)              ██████████░░  10/12 ✅ + 2 🔲
The Ecosystem (9 docs)              ███████████░  8/9  ✅ + 1 🔲
Foundations — Everyone (8)          ████░░░░░░░░  3/8  ✅ + 5 🔲
General Agents (12)                 ████████████  12/12 ✅
Personal Agent Harnesses (2)        ████████████  2/2   ✅
Mode 1 — Problem-Solving (3)        ████████████  3/3   ✅
Mode 2 — Manufacturing (18)         ████████████  18/18 ✅
References & Companions (3)         ░░░░░░░░░░░░  0/3  🔲

TOTAL: 56 fully ✅ + 11 🔲 missing = 67 chapters
```

**Real gaps (11 chapters not started):**

| Group | Chapter | Gap |
| --- | --- | --- |
| Front Matter | Selling as a Vertical FDE | 🔲 not started |
| Front Matter | Glossary | 🔲 not started (~36K-token reference, 15 term categories) |
| The Ecosystem | The System of Context | 🔲 not started |
| Foundations | Claude and ChatGPT 101 | 🔲 not started |
| Foundations | AI Fluency | 🔲 not started |
| Foundations | Code You Never Write | 🔲 not started |
| Foundations | Skills & Connectors | 🔲 not started |
| Foundations | How to Think in the AI Era | 🔲 not started |
| References & Companions | Which AI Employees To Use in 2026?, Cheatsheets, Agentic Engineering Fundamentals | 🔲 all 3 not started |

**Poora Mode 1 + Mode 2 + General Agents + Personal Agent Harnesses group (35 chapters), plus 10/12 Front
Matter aur 8/9 Ecosystem chapters, ab is repo mein note ho chuke hain** — bas status table pehle stale
thi. Real remaining work 11 chapters hai (kai chhote reference/business-model pages). Thesis aur Getting
Paid dono 2026-08-26 ko poore hue (quiz sameet).

---

## 📁 Repo Structure

```
docs/[chapter-slug]/
  README.md          ← chapter overview + index of parts
  00-*.md, 01-*.md…  ← numbered concept-part files, book ke apne sections follow karte hue

Loop-Engineering-Summary.md      ← Loop Engineering ka aasan overview (root)
Loop-Engineering-Final-Prep.md   ← Loop Engineering ka poora prep guide, real code example ke sath
Graph-Engineering-Summary.md     ← Graph Engineering ka aasan overview (root)
docs/ksor/                        ← KSoR standalone reference (chapter-context ke bina, SDK khud)
docs/ccar-f-fde-track-b/          ← CCAR-F Track B syllabus ka apna chapter (README+numbered files+quiz)
                                    + 4 local-runnable practicum scaffolds (Fumadocs site, stateless
                                    MCP+MRTR server, agent surface, eval runner) — deploy nahi, sirf local
Claude Certified Architect Foundations (CCAR-F) FDE Track B Accelerated.md
                                  ← Panaversity ka apna 13-week Track B syllabus (external, user-provided,
                                    Zia Tutor se nahi) — architect strand + FDE practicum (Vertical SoR)
                                    dono ka authoritative week-by-week naqsha; dekho docs/certifications/07
progress.md                       ← is learning-journey ki apni spine (loop engineering se seekha pattern)
todolist.md                       ← active/done/backlog task list
```

Har doc mixed **Roman Urdu + English** mein hai, book ke Zia Tutor AI MCP connector se full content
nikaal kar likha gaya hai — training-knowledge se nahi, seedha book se.
