# KSoR — Knowledge System of Record (Complete Guide)

*Source: GitHub repo `panaversity/ksor`'s README — `KSoR-Complete-Guide (1).pdf` (user-provided, PDF
`Read` tool se poora parha 2026-08-25, WebFetch nahi). Standalone reference folder — poora tafseeli
KSoR breakdown, kisi ek book-chapter tak mehdood nahi.*

> **Note (2026-08-27):** Is folder ki poori conceptual/methodology depth — 7 templates, source
> hierarchy, three-bin sort, authority-vs-orientation, do end-to-end appendices (Sales SoR, General
> Ledger SoR) — ab book ke apne (Zia Tutor AI se fetch kiye) chapter mein hai:
> [`docs/ecosystem-designing-the-vertical-sor/README.md`](../ecosystem-designing-the-vertical-sor/README.md).
> Woh chapter book ke `ecosystem-designing-the-vertical-sor` lesson se banaya gaya hai — is `docs/ksor/`
> folder ka **koi zikr book mein nahi hai** (naam-similarity ittefaqi hai). **Yeh folder** SDK
> implementation reference ke liye hai — `panaversity/ksor` open-source package khud (CLI, project
> structure, MCP agent surface) — agar tumhe woh SDK samajhna hai, yahin raho; agar method/methodology
> chahiye (kisi bhi vertical ke liye), upar wale link par jao.

## Yeh Folder Kis Baare Mein Hai

**KSoR (Knowledge System of Record)** — `panaversity/ksor` — ek open-source SDK hai jo governed,
authoritative knowledge systems banata hai, insaanon aur AI agents dono ke liye. Traditional Systems of
Record (ERP/CRM/HRIS) batate hain "abhi kya sach hai." KSoR batata hai "hum kya jaante hain, aur kaise
operate karna hai" — policies, rules, methods, thresholds — ek governed source se, insaan (website) aur
AI agents (MCP) dono ko "Same Truth" serve karte hue.

*(Zaroori: package abhi `0.0.0` par hai — naam-reserve placeholder, CLI commands design hain, implement
nahi hue.)*

## Index

1. [00 — KSoR Kyun Banaya Gaya, Aur Kya Hai](00-why-ksor-and-definition.md)
2. [01 — 7 Core Principles, Aur Kya Bana Sakte Hain](01-principles-and-what-you-can-build.md)
3. [02 — Quick Start, Project Structure, Knowledge as Code, Agent Surface (MCP)](02-architecture-and-tooling.md)
4. [03 — Governance Model, AI-Native Architecture, Agent-First Development](03-governance-and-ai-native-role.md)
5. [04 — Example Applications, Design Goals, Project Status](04-applications-design-goals-and-status.md)
6. [05 — Test Your Understanding (12-Question Quiz)](05-test-your-understanding.md) · standalone [`quiz.md`](quiz.md)

## Practice Projects

[`projects/`](projects/README.md) — 3 runnable scaffolds: corpus-to-site skeleton (structure +
validator), a stub stateless MCP tool call, aur ek governance/provenance record + validator.

## Ek Line Mein Poori Cheez

> **Traditional System of Record AI agent ko batata hai business ke baare mein kya sach hai; Knowledge
> System of Record usay batata hai organization kya jaanta hai aur usay kaise operate karna chahiye.**
> Ek governed source, do surfaces (Human + Agent via MCP) — "Same Truth." Abstention ek feature hai:
> agar KSoR mein jawab nahi hai, sahi jawab hai "yeh maloom nahi," guess karna nahi.

## Is Repo Mein Kahan Aur Fit Hota Hai

**Correction (2026-08-27):** pehle yahan likha tha ke book ka Ecosystem chapter isi KSoR SDK ko concrete
example ki tarah use karta hai — yeh galat tha. Book ke apne lesson `ecosystem-designing-the-vertical-sor`
mein `panaversity/ksor` ya "KSoR" ka **koi zikr nahi hai** (verified: poora lesson fetch kar ke check
kiya). Dono folders sirf naam mein similar hain kyunke dono galat tarike se ek hi PDF/SDK-README source se
bana diye gaye thay — asal mein yeh do **alag-alag cheezein** hain: book ka chapter ek generic
first-principles method hai (kisi bhi vertical ke liye), aur `panaversity/ksor` ek specific open-source
SDK hai jo koi bhi team implement kar sakti hai — ek doosre ko reference nahi karte.

- [Designing the Vertical System of Record from First Principles](../ecosystem-designing-the-vertical-sor/README.md)
  — book ka apna chapter, is folder se independent

Doosre related content:

- [Agent Factory System of Record](../ecosystem-system-of-record/README.md) — is book ki apni SoR, jo
  Zia Tutor AI/Zia Developer AI ko serve karti hai (KSoR ka pattern isi se generalize hua)
- [The FDE AF Model](../ecosystem-fde-af-model/README.md) — "ek component, kai corpora" framing
- [Graph Engineering](../graph-engineering/README.md) — KSoR ka "Knowledge Graph" idea Part 3 (Facts Ka
  Graph) se seedha overlap karta hai — dono provenance ko non-negotiable maante hain

---
[⬅ Docs Index](../../README.md)
