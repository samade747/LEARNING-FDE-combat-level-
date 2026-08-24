# 00 — KSoR Kyun Banaya Gaya, Aur Kya Hai

*Source: GitHub repo `panaversity/ksor` ka README, PDF `Read` tool se poora parha (2026-08-25) —
user-provided `KSoR-Complete-Guide (1).pdf` se.*

## 1. KSoR Kyun Banaya Gaya

Enterprises dashak se **Systems of Record** use karte aa rahe hain — accounting system (financial
transactions ke liye authoritative), CRM (customer records), HRIS (employee records). Agar spreadsheet
aur accounting ledger mein farq ho, to **ledger jeetta hai** — wahi authoritative hai. Yeh systems is
sawal ka jawab dete hain: **"Business ki asal operational state kya hai?"**

AI Agents ek naya masla laate hain — unhe yeh bhi jaanna hota hai:

- Kaunsi policies lagu hoti hain?
- Is decision par kaunse rules govern karte hain?
- Kaunsi procedure follow karni chahiye?
- Organization is term ka kya matlab leta hai?
- Kaunse thresholds approved hain?
- Kaunsi methodology use honi chahiye?
- Kya exceptions maujood hain?
- Is jawab ke peeche kaunse sources hain?
- Agar jawab maloom na ho to agent kya kare?

Yeh jaankari aksar bikhri hoti hai — documents, wikis, PDFs, slides, websites, manuals, repos, employee
ke zehan mein, prompts mein, RAG indexes mein. Koi authoritative jawab nahi hota ke "AI ko kaunsi
knowledge par bharosa karna chahiye?" — **KSoR isi masle ko hal karne ke liye bana hai.**

## 2. KSoR Ki Definition

**Knowledge System of Record (KSoR)** — wo authoritative, governed source hai jahan se insaan aur AI
agents dono **samajhte, faisla karte, aur amal karte hain**. Ismein aa sakta hai: domain knowledge,
policies, procedures, rules, standards, methods, definitions, decision criteria, thresholds, specifications,
controls, examples, exceptions, workflows, provenance (asal source), aur supporting material.

> Maqsad sirf information ko searchable banana nahi hai — maqsad yeh establish karna hai: **"Yeh wo
> knowledge hai jis se hum operate karte hain."**

### Traditional SoR vs Knowledge SoR

| | Traditional System of Record | Knowledge System of Record |
| --- | --- | --- |
| Asal maqsad | Operational state record karna | Institutional knowledge record karna |
| Content | Transactions, balances, customers, inventory | Rules, policies, methods, standards, definitions |
| Misaal systems | ERP, CRM, HRIS, accounting | KSoR |
| Bunyadi sawal | Abhi kya sach hai? | Hum kya jaante hain, kaise operate karna hai? |
| Kis ke liye behtar | Applications aur business processes | Insaan aur AI agents |
| Badalne ka tareeqa | Transactions | Review, governance, versioning |
| AI ka role | Sirf tool consumer | First-class knowledge consumer |

Ek capable enterprise agent KSoR se policy padh sakta hai, CRM se current account data le sakta hai,
governed rule apply kar sakta hai, action le sakta hai, aur result wapas traditional SoR mein likh sakta hai.

## 3. KSoR Sirf Knowledge Base Se Zyada Hai

Ek knowledge base sirf information **store** karta hai. KSoR **authority** establish karta hai — yehi
farq zaroori hai. Aam knowledge base sirf storage, search, retrieval, similarity, ya question-answering
par focus karta hai. KSoR ko in sawalon ka bhi jawab dena hota hai:

- Is knowledge ka malik kaun hai?
- Yeh kahan se aayi?
- Kaunsi version authoritative hai?
- Kya isay review kiya gaya?
- Iska scope kya hai?
- Jab sources aapas mein takrayen to kya hoga?
- Kya AI evidence aur apni guess mein farq kar sakta hai?
- Kya jawab wapas apne source tak trace ho sakta hai?
- Agar KSoR mein jawab hi na ho to kya hoga?

Isi liye KSoR **governance, provenance, citations, versioning, aur abstention** (jawab na dena jab maloom
na ho) ko architecture ka zaroori hissa manta hai — optional feature nahi.

---
[⬅ 00 se shuru] · [Agla: 01 — Principles aur Kya Bana Sakte Hain ➡](01-principles-and-what-you-can-build.md)
