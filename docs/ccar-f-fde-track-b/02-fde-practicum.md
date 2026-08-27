# 02 — FDE Practicum: Building a Vertical System of Record (P1-P13)

## Kya Banate Ho

Har student ek **working Vertical System of Record** apni chuni hui domain mein leke nikalta hai: ek
governed knowledge corpus, do projections ke sath — **human-readable** (site) aur **agent-readable**
(MCP). "Kya banayen aur kaise design karein" ka poora method [[ecosystem-designing-the-vertical-sor]]
mein hai (first-principles method: outcome contract, workflow archaeology, three-bin sort, source
hierarchy, thin-slice-and-prove) — yeh practicum uska **schedule + runnable scaffold** hai.

## Technology Baseline

| Piece | Tool |
| --- | --- |
| Governed knowledge framework | **KSoR** — `docs/status.md` implementation authority hai |
| Human projection | KSoR ka reference site: **Next.js + Fumadocs**, static export supported |
| Agent projection | **MCP revision 2026-07-28** — stateless protocol core + MRTR |
| Environment | Node.js 24+, pnpm, uv |

**Honest gap note (rule 3 compliance):** book (`context-layer-crash-course`) **stateless MCP** ka core
idea confirm karti hai — Streamable HTTP mein stateless mode default hai (har call independent
request/response, session koi nahi, `FastMCP("name")` + `mcp.run(transport="http", stateless_http=True)`)
taake server ko load-balancer ke peeche multiple copies mein chalaya ja sake. Lekin **MRTR** (Multi-
Round-Trip mechanism: `input_required`, `inputRequests`, opaque `requestState`, `inputResponses`) book
ke corpus mein **abhi nahi hai** — yeh MCP spec 2026-07-28 ka apna detail hai, jo is syllabus ki apni
"Sources of Truth" table mein alag se authority ki tarah listed hai. `projects/p6-p7-stateless-mcp/`
scaffold isi wajah se stateless core (book-confirmed) ko fully implement karta hai, aur MRTR ko
concept-level demonstrate karta hai — spec ke exact field-names ke against verify karna practicum ka
apna kaam hai jab live spec available ho.

KSoR evolving hai — har module se pehle `docs/status.md` check karo. Shipped `ksor` commands use karo
jahan exist karte hon; warna surface directly build karo published structure mein.

## Week by Week

| Week | Focus | Kya karna hai |
| --- | --- | --- |
| **P1** | FDE, SoR Thesis, Setup | *FDE AF Model* + *System of Record* parho. Likho durable product governed knowledge kyun hai, chatbot kyun nahi. 3 candidate verticals list karo. Node 24+/pnpm/uv install |
| **P2** | Choose the Vertical | Knowledge intensity, regulatory weight, source availability, willingness-to-pay, personal access apply karo. Ek vertical commit karo, source register shuru karo |
| **P3** | Design the Vertical SoR | Scope, ownership, authoritative sources, conflict handling, review process, knowledge boundary define karo. Decisions log kholo, abstention policy likho |
| **P4** | Fumadocs I: Corpus to Site | KSoR human projection banao (Claude Code se). Pehle 3 real source documents ko reviewed Markdown + provenance mein convert karo — scaffold: [`projects/p4-p5-fumadocs-corpus-to-site/`](projects/p4-p5-fumadocs-corpus-to-site/README.md) |
| **P5** | Fumadocs II: Structure + Deploy | Hierarchy, navigation, search, static deployment add karo. **Milestone 1:** live human surface, 5+ governed docs |
| **P6** | Stateless MCP I | 2026-07-28 stateless core seekho: no `initialize/initialized` handshake, per-request metadata, optional `server/discover`, standard HTTP scaling. Ek tool call build+inspect karo — scaffold: [`projects/p6-p7-stateless-mcp/`](projects/p6-p7-stateless-mcp/README.md) |
| **P7** | Stateless MCP II: Schemas + MRTR | Pydantic/Zod se schema conversion trace karo. `input_required` + `inputRequests` + opaque `requestState` + `inputResponses` implement karo. `requestState` untrusted treat karo, handler re-entrant banao |
| **P8** | Agent Surface, Hand-Built | Search, retrieve, cited-answer tools governed corpus par. Knowledge boundary application logic mein enforce karo. **Milestone 2:** working MCP agent surface — scaffold: [`projects/p8-agent-surface/`](projects/p8-agent-surface/README.md) |
| **P9** | KSoR I: One Source, Multiple Projections | Current KSoR structure adopt karo: `knowledge/`, `instance.md`, `system/site/`, `.agents/`. Same governed corpus se human+agent projections derive karo |
| **P10** | KSoR II: Governance + Provenance | Knowledge lifecycle implement karo, provenance build karo (deployed answer → corpus version → reviewed source traceable) |
| **P11** | KSoR III: Proving Behaviour | 3-class evaluation set banao: answerable-with-citation / requires-governed-rule+operational-fact / outside-boundary→abstain. Project 2's support agent ko SoR se connect karo. **Milestone 3:** governed KSoR + eval set — scaffold: [`projects/p11-proving-behaviour/`](projects/p11-proving-behaviour/README.md) |
| **P12** | Capstone Sprint | Corpus deepen karo, eval failures ko sahi layer par fix karo, dono projections polish karo, architecture brief finish karo |
| **P13** | Demo Day | Governed answer with source trace demonstrate karo, ek correct abstention, ek MRTR interaction, decisions log. **Milestone 4:** capstone Vertical SoR |

## Milestones

| Milestone | Week | Evidence |
| --- | --- | --- |
| 1. Live human surface | P5 | Deployed site; 5+ governed docs with provenance |
| 2. Working agent surface | P8 | Stateless MCP search/retrieve/cite interface |
| 3. Governed KSoR + evaluation | P11 | Decisions log + 3-class evaluation |
| 4. Capstone Vertical SoR | P13 | Demo + brief + repository |

**Scope reminder:** is repo ke `projects/` scaffolds **local** hain (Milestones ka "deployed"/"live"
wording demonstrate karte hain apne machine par — `localhost` par chalne wala site/server — asal public
deployment nahi). Har project README mein real deployment ke commands reference ki tarah note hain.

---
[⬅ Architect Strand](01-architect-strand.md) · [Agla: Required Projects + Assessment ➡](03-required-projects-and-assessment.md) · [⬆ Index](README.md)
