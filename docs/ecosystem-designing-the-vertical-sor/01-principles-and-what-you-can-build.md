# 01 — 7 Core Principles, Aur Kya Bana Sakte Hain

## 4. Ek Source, Do Surfaces

KSoR ka usool: **insaan aur AI agents ko organization ki knowledge ke alag-alag versions se kaam nahi
karna chahiye.** Ek governed source do surfaces banata hai:

- **Human Surface** — ek padhne wali website: search/browse, read/learn, review/share
- **Agent Surface** — MCP ke zariye: search/retrieve, cite/reason, abstain/act

Website alag se maintain nahi hoti, aur agent corpus website ki chhupi hui copy nahi hai — dono ek hi
**governed source** ke projections hain, isi liye **"Same Truth."**

## 5. Saat Core Principles

| # | Principle | Matlab |
| --- | --- | --- |
| 1 | One Authoritative Source | Knowledge ki ek hi canonical jagah honi chahiye — representations alag ho sakti hain, source ek hi rahe |
| 2 | Insaan aur Agents dono First-Class | Ab documentation sirf insaan ke liye nahi likhi jaati — AI assistants, agents, workflows sab consumers hain |
| 3 | Provenance Matters | Jawab kis document se aaya, kaunsi version, kab bana — yeh chain hamesha maloom honi chahiye |
| 4 | Citation Before Confidence | AI ka confident lehja proof nahi hai — jawab ko trace hona chahiye, model ki yaadasht par nahi |
| 5 | Abstention Is a Feature | Agar KSoR mein jawab nahi hai, to sahi jawab hai: "Yeh maloom nahi" — guess karna nahi |
| 6 | Governance Before Retrieval | Behtareen search bhi ungoverned knowledge ko tez retrieve karega — pehla sawal ye ho ke kya knowledge mein jaana chahiye, kaun badal sakta hai |
| 7 | Vendor Neutrality | Aapki knowledge kisi AI company ki milkiyat nahi honi chahiye — ChatGPT, Claude, ya kisi bhi model se kaam aaye |

## 6. KSoR Se Kya Bana Sakte Hain

KSoR jaan-boojh kar kisi khaas industry tak mehdood nahi — teen tarah ke KSoRs support karta hai:

| Type | Misaalein |
| --- | --- |
| **Organizational KSoR** | Agent Factory KSoR, Engineering KSoR, Product Management KSoR, Security KSoR, AI Governance KSoR |
| **Domain KSoR** | Accounting, Government Contracting, Healthcare, Legal, Banking, Insurance, Supply Chain, Sales |
| **Product/Method KSoR** | Design System, API Standards, Architecture, Implementation Method, Compliance Framework |

**Vertical KSoR** sirf KSoR ka ek application hai — kisi khaas profession/industry/domain ke liye
authoritative knowledge layer. (Isi liye is chapter ka naam "Designing the Vertical System of Record
from First Principles" hai — dekho [`../ecosystem-fde-af-model/README.md`](../ecosystem-fde-af-model/README.md)
ka vertical-per-profession framing.)

### Misaal — Accounting KSoR

Socho ek Accounting KSoR hai jismein revenue-recognition, capitalization, bad-debt policies; month-end
close aur journal-entry-review procedures; segregation-of-duties aur approval-thresholds controls;
glossary; aur examples hon.

Agar poocha jaye: *"Kya yeh $42,000 wala software implementation cost capitalize ho sakta hai?"* — agent
organization ki capitalization policy nikalega, criteria apply karega, source cite karega, aur farq karega
ke KSoR mein kya likha hai aur apna reasoning kya hai. **Agar policy is situation ko cover nahi karti, to
system khud se policy banayega nahi.**

---
[⬅ 00 — Kyun aur Definition](00-why-ksor-and-definition.md) · [Agla: 02 — Architecture aur Tooling ➡](02-architecture-and-tooling.md)
