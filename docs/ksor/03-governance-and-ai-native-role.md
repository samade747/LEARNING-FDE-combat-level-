# 03 — Governance Model, AI-Native Architecture, Agent-First Development

## 11. Governance Model

```
Source → Draft → Review → Approved → Authoritative KSoR
                                    ├── Human Surface
                                    └── Agent Surface
                                            → Superseded / Retired
```

Regulated ya high-risk knowledge ke liye organizations extra controls laga sakti hain: named knowledge
owners, approval requirements, effective dates, source citations, mandatory review periods, change
records, conflict resolution, separation of duties, audit history. **KSoR architecture deta hai, governance
policy khud organization ki zimmedari rehti hai.**

### Knowledge Boundaries — Teen Misaalein

| Type | Sawal | Kya Hoga |
| --- | --- | --- |
| In scope | "$50,000 se zyada purchases par kaunsa approval threshold lagta hai?" | Agar policy mein jawab hai, KSoR jawab + source deta hai |
| Requires reasoning | "Kya is khaas purchase ko CFO approval chahiye?" | Governed rule ko operational facts (kisi doosre SoR se) ke saath jorna padta hai |
| Outside the KSoR | "Agle saal kaunsi approval policy aayegi?" | Agar approved nahi hai to system guess nahi karega, mana kar dega |

Yeh teenon misaalein trustworthy agentic systems ke liye zaroori hain — **agent ko apni knowledge ki
seemayen pata honi chahiye.**

## 12. AI-Native Architecture Mein KSoR Ka Role

```
Human / AI Worker → Agent → ┬── KSoR (Policies/Methods) — "kaise operate karein"
                             └── Operational SoRs (CRM/ERP/HRIS, Ledger) — "abhi kya sach hai"
                                             ↓
                                    Decision → Action
```

KSoR agent ko batata hai **organization kaise operate karta hai**. Traditional SoR batata hai **abhi
kya sach hai**. Dono mil kar reliable enterprise action ke liye zaroori context dete hain — is repo ke
[Agent Factory System of Record](../ecosystem-system-of-record/README.md) ka role bhi isi
tarah "Layer 1 SoR kernel" hai, jo book ka apna content Zia Tutor AI/Zia Developer AI ko serve karta hai.

## 13. Agent-First Development

KSoR aise development duniya ke liye design hua hai jahan coding agents zyada tar mechanical kaam khud
karte hain. Scaffolded KSoR mein machine-readable instructions hoti hain jaise:

- "Is policy ko KSoR mein add karo"
- "In source documents ko governed Markdown mein convert karo"
- "Har page par missing provenance check karo"
- "Is section se ek quiz banao"
- "KSoR validate karo" / "Test suite chalao" / "Release taiyar karo" / "Deploy karo"

Isi liye repo do cheezein ban jata hai: **(1) khud knowledge ka artifact**, aur **(2) agents ke kaam karne
ki working context** — taake subject-matter experts aur software engineers isi governed source par mil
kar kaam kar saken.

**Human-Readable by Default:** KSoR yeh zaroorat nahi karta ke saari knowledge sirf vector database mein
gum ho jaye — canonical source hamesha inspectable rehta hai. Koi bhi isay khol sakta hai, padh sakta
hai, diff kar sakta hai, review kar sakta hai.

**Vendor-Free by Design:** Aapka KSoR in sab tabdeeliyon se bach kar chalna chahiye: LLM providers,
embedding models, vector stores, agent frameworks, cloud providers. Asal durable asset **governed
knowledge** hai — baaki sab replaceable hona chahiye.

## 14. Deployment Aur Firewall Ke Peeche Kaam

`ksor build` se banaya hua human surface ek **static site** hota hai — Vercel, Netlify, GitHub Pages,
static storage, ya khud ki internal servers par deploy ho sakta hai.

Kyunke KSoR mein aksar internal organizational knowledge hoti hai, isay is tarah design kiya gaya hai ke
knowledge organization ke control mein rahe, website self-host ho sake, aur agent interface security
boundary ke andar deploy ho sake. **KSoR kisi organization ko apni institutional knowledge third-party
SaaS par publish karne par majboor nahi karta.**

---
[⬅ 02 — Architecture aur Tooling](02-architecture-and-tooling.md) · [Agla: 04 — Applications, Design Goals, Status ➡](04-applications-design-goals-and-status.md)
