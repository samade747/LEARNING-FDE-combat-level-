# Designing the Vertical System of Record — Summary

Traditional Systems of Record (ERP/CRM/HRIS) answer "what's true right now." AI agents need a second
kind of authoritative source — one for **institutional knowledge**: policies, rules, methods, thresholds.
KSoR (`panaversity/ksor`) is the open-source SDK that builds this: governed, provenance-tracked
knowledge, served identically to humans (a website) and AI agents (MCP) — "Same Truth." Package is at
`0.0.0` — a name-reserving placeholder; everything below is design, not yet implemented.

## 00 — Kyun Aur Definition

- Enterprises ko dashak se Systems of Record chahiye rahe hain (ledger jeetta hai, spreadsheet nahi) —
  lekin AI agents ek naya sawal poochte hain: "kaunsi policy lagu hoti hai, kaunse rules govern karte hain?"
- KSoR = authoritative, governed source jahan se insaan aur agents dono samajhte/faisla karte/amal
  karte hain. Traditional SoR "abhi kya sach hai" batata hai; KSoR "hum kya jaante hain, kaise operate
  karna hai" batata hai
- Knowledge base sirf store karta hai; KSoR **authority** establish karta hai — ownership, provenance,
  versioning, review, conflict-handling, abstention sab architecture ka hissa hain, optional nahi

## 01 — 7 Principles + Kya Bana Sakte Hain

- "One Source, Two Surfaces": Human Surface (website) aur Agent Surface (MCP) — dono ek hi governed
  source ke projections
- 7 principles: One Authoritative Source, Humans+Agents First-Class, Provenance Matters, Citation
  Before Confidence, Abstention Is a Feature, Governance Before Retrieval, Vendor Neutrality
- 3 types: Organizational KSoR, Domain KSoR, Product/Method KSoR — Vertical KSoR sirf ek application
  hai. Accounting KSoR misaal: policy cite karta hai, cover na ho to khud policy nahi banata

## 02 — Architecture Aur Tooling

- CLI: `init`, `dev`, `build`, `serve` (abhi design, exit code 2 deta hai — implement nahi hue)
- Project structure: `knowledge/` (plain Markdown corpus), `instance.md`, `site/`, `.agents/skills/`
- Knowledge as Code: authored→reviewed→version-controlled→validated→tested→built→published→consumed.
  `build.lock.json` se Build Provenance chain: AI Answer → Passage → Document → Build → Git Commit →
  Reviewed Source
- Agent Surface = MCP (interoperability boundary, model-agnostic). KSoR vs RAG: RAG "context mein kaise
  dalein," KSoR "kaunsi knowledge itni authoritative hai ke operate kiya ja sake" — RAG KSoR ka chhota
  hissa hai. KSoR vs CMS: content ek input hai, institutional knowledge asal asset hai

## 03 — Governance Aur AI-Native Role

- Governance flow: Source→Draft→Review→Approved→Authoritative→(Human+Agent Surface)→Superseded
- 3 knowledge-boundary types: in-scope (jawab+source), requires-reasoning (governed rule + operational
  facts jorna), outside-the-KSoR (guess nahi, mana kar dega)
- AI-native architecture mein KSoR ("kaise operate karein") aur Operational SoRs ("abhi kya sach hai")
  dono milkar Decision→Action ke liye context dete hain
- Agent-First Development: repo khud knowledge ka artifact bhi hai aur agents ke kaam karne ki working
  context bhi. Human-readable by default, vendor-free by design
- Deployment: static site (Vercel/Netlify/GitHub Pages/self-host), agent interface security boundary ke
  andar — third-party SaaS par publish karne ka koi majboori nahi

## 04 — Applications, Design Goals, Status

- Agent Factory KSoR (shared method) + Vertical KSoR (domain truth) mil kar domain-specific agent
  kaam karte hain — same `ksor` SDK se
- KSoR CRM/ERP/HRIS ki jagah nahi leta, sirf knowledge layer add karta hai
- 11 design goals: Authoritative, Governed, Traceable, Inspectable, Portable, Agent-readable,
  Human-readable, Versioned, Reproducible, Composable, Extensible
- Status: active development, purane VSOR implementation se evolve ho raha hai; MCP agent surface abhi
  sirf design hai. Apache 2.0, npm package `@panaversity/ksor`

---
[⬅ Chapter Index](README.md)
