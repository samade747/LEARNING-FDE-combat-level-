# 05 — Read-Reason-Act, 8 Invariants, FDE AF Model Mein Jagah

## Read, Reason, Act, and Record

**Finding karna doing jaisa nahi hai.** Layer dhoondti hai. Worker sochta hai. Governing record rules
check karti hai. Tool action perform karta hai. Jis system ka result hai wo likh deta hai. **5 alag
jobs, hamesha isi order mein.**

Context layer **find + understand** support karti hai. Worker permitted reasoning + decision karta
hai. Vertical SoR rules/permissions/invariants validate karti hai. Tabhi governed tools action karte
hain, aur result-owner system record karta hai. Yeh middle step **drop karna aasan, lose karna
expensive** hai: discount approval sales-record se confirm hoti hai CRM likhne se pehle; journal entry
accounting-record se check hoti hai (preparer ≠ approver) ERP draft hold karne se pehle.

> **System of Context kabhi doosra transaction system nahi ban sakta, aur kabhi governed record ke
> around likhne ka tareeqa nahi ban sakta.**

**Ek source do surfaces expose kar sakta hai, alag risk:**

| Surface | Typical operation | Kya ghalat ho sakta hai |
| --- | --- | --- |
| Retrieval | Search, read, cite, compare | Information exposure |
| Calculation/Checking | Validate, classify, calculate | Ghalat conclusion |
| Preparation | Entry draft, form prepare | Ghalat proposed record |
| Execution | Send, post, release, pay | Real-world consequence |

> **System of Context access ko permission mein kabhi convert nahi karti.**

## The Eight Invariants of the Connecting Layer

**Yeh 8 rules badalte nahi** — har profession, har customer, har tool mein sach rehti hain:

| # | Invariant | Kyun |
| --- | --- | --- |
| 1 | Authority kabhi move nahi hoti — layer citations carry karti hai record tak, khud ya model kabhi cited source nahi ban sakte | Warna impact chain ek branch bana legi jisay koi govern nahi karta |
| 2 | Relevance authority nahi hai — routing retrieval se pehle hoti hai | Warna top-ranked passage chup-chaap rule ban jayega |
| 3 | Permission inherited hai, invented nahi, model se pehle enforced | Warna layer "sab se helpful data breach" ban jati hai |
| 4 | Freshness per-field decide hoti hai: index working context, discover governed knowledge, query live truth | Warna Worker exact sawalon ka jawab stale approximation se confidently deta hai |
| 5 | Provenance har item ke sath travel karti hai, summarizing kabhi strip nahi karti | Warna contract/policy/rumour same dikhne lagte hain |
| 6 | Conflict preserve+escalate hota hai, blend kabhi nahi | Warna system ek claim banati hai jo kisi source ne nahi kahi |
| 7 | Ungoverned chup-chaap governed nahi banta — promotion authorship hai, reviewed+recorded | Warna customer ki mistakes tumhari record mein tumhari stamp pehen leti hain |
| 8 | Discovery confirmation nahi hai — search hit pointer hai, governing record confirm karti hai | Warna indexed copy chup-chaap authority ban jati hai |

## Where It Sits in the FDE AF Model

System of Context **teesri SoR nahi hai**, aur permanent shared-kernel layer bhi nahi — [FDE AF Model](../ecosystem-fde-af-model/README.md)
ke **2 layers** mein spans karta hai.

- **Layer 3 pattern prepare karta hai.** Vertical ecosystem mein reusable pieces (koi customer data
  nahi): source classes, routing rules, packet schema, metadata/citation formats, connector
  templates, retrieval evaluations, conflict tests, permission patterns. **Yeh sab tumhara hai.**
- **Layer 4 customer bind karta hai.** Instance company ki apni applications, identity provider,
  contracts, policies, credentials, case-IDs, approvals supply karta hai. **Yahan System of Context
  real banta hai.**

Promotion law yahan bhi lagu hoti hai: pattern (3+ customers mein safely repeat ho) Layer 3 mein move
ho sakta hai. **Customer records/credentials/messages/private-evidence kabhi move nahi hotay.**

> Layer 3 pattern **asset** hai jo tum client-to-client carry karte ho. Layer 4 fitting **service**
> hai jo tum har client par karte ho. Farq decide karta hai tumhara kaam kitne ka hai.

## Consolidate by Default, Specialize Deliberately

Book ki infrastructure stance: **consolidate by default** — ek Postgres mein relational+documents+
search+vectors (scattered systems se behtar jo sync se bahar nikal jate hain). Yeh page opposite nahi
lagti, lekin opposite nahi hai.

> **Consolidation sahi hai jab ek set of invariants poora data govern karta ho. Specialization sahi
> hai jab 2 sets opposite directions mein pull karen.**

Record ko chahiye: exactness, versioning, audit trail, rights basis. Customer ki duniya ko chahiye:
breadth, freshness, permission fidelity (dusre dozen systems se). Dono ko force karo ek store mein,
aur record ki provenance uncertain ho jati hai, aur index ki permissions guesswork ban jati hain —
**dono worse ho jate hain.** Yeh stance ka exception nahi — **"deliberately" lafz isi ke liye reserved
tha.** Ek governed store profession ke liye. Ek connecting layer customer ki duniya ke liye.

---
[⬅ Permission, Provenance, Conflict](04-permission-provenance-conflict.md) · [Agla: Reference Implementation + Ayesha ➡](06-reference-implementation-and-ayesha.md)
