# 04 — Example Applications, Design Goals, Project Status

## 15. Example Applications

**Agent Factory KSoR** — ek shared methodology jo AI-native implementations mein use hoti hai:
architecture, principles, FDE methodology, governance, agent patterns, evaluation standards,
implementation methods, operating model.

**Vertical KSoR** — ek profession/industry ke liye khaas knowledge — jaise Government Contract
Accounting KSoR: accounting rules, FAR requirements, contract structures, indirect rates, revenue
recognition, billing, compliance, workflows, decision criteria.

```
Agent Factory KSoR (Shared Method) ─┐
                                      ├──▶ AI Agent
     Vertical KSoR (Domain Truth) ───┘
```

Agents dono ko mila kar domain-specific kaam kar sakte hain — dono ek hi `ksor` SDK se banaye ja sakte
hain. Yeh isi book ke [FDE AF Model](../ecosystem-fde-af-model/README.md) ke "ek component, kai
corpora" idea se seedha jurta hai.

### KSoR Kya Replace Nahi Karta

KSoR aapke CRM, ERP, accounting system, HRIS, transactional database, data warehouse, ya operational
APIs ki jagah nahi leta — yeh systems apni operational state ke liye authoritative rehte hain. KSoR sirf
woh **knowledge layer** add karta hai jo agents ko us state ko samajhne aur us par amal karne ke liye
chahiye.

## 16. Design Goals (11 Usool)

| Usool | Matlab |
| --- | --- |
| Authoritative | Ek saaf canonical source ho |
| Governed | Knowledge ka malik aur controlled change ho |
| Traceable | Zaroori jawab evidence tak wapas jayen |
| Inspectable | Insaan dekh sakein agent kya padh raha hai |
| Portable | Kisi ek vendor mein phansi na ho |
| Agent-readable | AI agents corpus ko programmatically use kar sakein |
| Human-readable | Log wahi knowledge browse aur samajh sakein |
| Versioned | Institutional truth mein history ho |
| Reproducible | Deployed KSoR ek khaas corpus/version se traceable ho |
| Composable | Kai KSoRs saath mil kar use ho sakein |
| Extensible | Organizations apni zaroorat ke hisaab se adapt kar sakein |

## 17. Project Status

KSoR abhi **active development** mein hai — purane **VSOR** implementation se general Knowledge
System of Record architecture ki taraf evolve ho raha hai. VSOR ne pehle hi kuch foundations prove ki
thin: Markdown-based source, generated documentation sites, scaffolding, local dev, static builds, build
provenance, agent-oriented instructions, testing, deployment.

> ⚠️ MCP-based agent surface **abhi sirf design hui hai, implement nahi**. License: Apache 2.0. npm
> package: `@panaversity/ksor` (command `ksor` hi rehta hai).

## 18. Ek Jumle Mein Poori Baat

> **Traditional System of Record AI agent ko batata hai business ke baare mein kya sach hai;
> Knowledge System of Record usay batata hai organization kya jaanta hai aur usay kaise operate karna
> chahiye.** KSoR is knowledge ko authoritative, governed, traceable, human-readable, agent-readable,
> aur vendor-neutral banata hai.

*Ye notes GitHub repo `panaversity/ksor` ke README par mabni hain. Asal aur live details ke liye dekhen:
[github.com/panaversity/ksor](https://github.com/panaversity/ksor)*

---
[⬅ 03 — Governance aur AI-Native Role](03-governance-and-ai-native-role.md) · [⬆ Index](README.md)
