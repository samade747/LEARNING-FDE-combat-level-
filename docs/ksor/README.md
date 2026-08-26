# KSoR — Knowledge System of Record (Complete Guide)

*Source: GitHub repo `panaversity/ksor`'s README — `KSoR-Complete-Guide (1).pdf` (user-provided, PDF
`Read` tool se poora parha 2026-08-25, WebFetch nahi). Standalone reference folder — poora tafseeli
KSoR breakdown, kisi ek book-chapter tak mehdood nahi.*

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

## Ek Line Mein Poori Cheez

> **Traditional System of Record AI agent ko batata hai business ke baare mein kya sach hai; Knowledge
> System of Record usay batata hai organization kya jaanta hai aur usay kaise operate karna chahiye.**
> Ek governed source, do surfaces (Human + Agent via MCP) — "Same Truth." Abstention ek feature hai:
> agar KSoR mein jawab nahi hai, sahi jawab hai "yeh maloom nahi," guess karna nahi.

## Is Repo Mein Kahan Aur Fit Hota Hai

Panaversity ki **The AI Agent Factory** book Ecosystem chapter #7, *"Designing the Vertical System of
Record from First Principles,"* isi KSoR SDK ko concrete example ki tarah use karti hai — dekho
[`../ecosystem-designing-the-vertical-sor/`](../ecosystem-designing-the-vertical-sor/README.md) (book
ki apni chapter-numbering ke sath). **Yeh folder** wahi content standalone reference ki tarah rakhta hai
— agar sirf KSoR SDK khud samajhna ho, kisi book-chapter context ke bina.

Doosre related content:

- [Agent Factory System of Record](../ecosystem-system-of-record/README.md) — is book ki apni SoR, jo
  Zia Tutor AI/Zia Developer AI ko serve karti hai (KSoR ka pattern isi se generalize hua)
- [The FDE AF Model](../ecosystem-fde-af-model/README.md) — "ek component, kai corpora" framing
- [Graph Engineering](../graph-engineering/README.md) — KSoR ka "Knowledge Graph" idea Part 3 (Facts Ka
  Graph) se seedha overlap karta hai — dono provenance ko non-negotiable maante hain

---
[⬅ Docs Index](../../README.md)
