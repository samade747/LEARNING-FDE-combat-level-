# 03 — Context Packet, aur Kya Index Ho Sakta Hai

## What the Layer Assembles: The Context Packet

System of Context **har matching paragraph** ko prompt mein nahi daalta — ek **controlled package**
banata hai. **7 operations:** **Connect** (controlled interface, content+identity+sync-state+access-
rules sab sath), **Identify** (actor, Worker, customer, case, jurisdiction, date, action — bina
identity/scope retrieval guessing hai), **Retrieve** (jo method fit kare — semantic/lexical/
structured/tool-based), **Filter** (jo reader nahi parh sakta, jo scope/jurisdiction/version se bahar
hai), **Rank** (sirf similarity nahi — authority, applicability, freshness, case-identity, confidence,
completeness), **Assemble**, **Deliver** (aur jo follow ho wo record karo).

> ⚠️ **Compression ki warning:** Token budget ki wajah se layer select/compress/summarize karti hai —
> yeh legitimate hai. Lekin yahi sab se zyada jagah hai jahan **invariant 5 (provenance)** toot jata
> hai. Version stamp drop karna, 2 sources ko ek sentence mein merge karna — tokens nahi bachaya,
> **evidence ko text mein convert kiya hai. Prose compress karo, provenance kabhi nahi.**

**Packet ke 8 hisse:** Request, Governing authority, Current facts, Supporting context, Conflicts,
Missing evidence, Permission envelope, Citations.

**Packet temporary hai, aur yehi design hai.** 3 rules iska constitution hain:
1. **Packet authority inherit karta hai.** Kabhi create nahi karta.
2. **Packet permissions inherit karta hai.** Kabhi widen nahi karta.
3. **Packet expire hota hai.** Current facts refresh hote hain jab freshness answer badal sakti ho.

**Durable cheezein** source aur task ke baad likhi gayi evidence hain. Packet sirf **working view**
hai.

## What May Be Indexed, and What Must Be Asked

| Information | Kaise reach hoti hai |
| --- | --- |
| Company ka ordinary working context | Permission-aware indexing |
| Stable governed knowledge (record se) | Discovery index, record confirm kare istemal se pehle |
| Current records, applicable versions, koi action | Live query (MCP/API) |

> **Index working context. Discover governed knowledge. Query current truth live.**

**Working context** freely search ho sakta hai (permissions inherited) — koi authority nahi.

**Governed knowledge: discover, phir confirm.** Do alag jobs:
- **Discovery** poochti hai: relevant info kahan ho sakti hai? Recall/similarity/speed optimize karti
  hai. Output: **ek pointer** ("look here").
- **Confirmation** poochti hai: kaunsa source officially applicable hai? Domain/authority-class/
  jurisdiction/version/effective-date/approval-status check karti hai. Output: **ek answer** ("this
  governs").

Sequence fixed hai: Search discovers → Layer routes → Record confirms → Worker cites → Checkers
validate → Tools act+record.

**Current state hamesha poochho, kabhi index mat karo.** Balances/transactions/approval-state kabhi
authored nahi hoti, kabhi stable nahi, **hamesha exact.** Index karo to purana ho jata hai, aur Worker
confidently ghalat jawab deta hai.

> **Agar stale value conclusion/permission/payment/filing/customer-action badal sakti hai, live fetch
> karo.**

Ek hi source ko kabhi do modes chahiye hote hain: contract clauses ke liye indexed, lekin version
active hai ya nahi confirm karne ke liye live query.

**Ungoverned ungoverned rehta hai.** Customer ka working material sirf isliye governed nahi ban jata
ke customer ne banaya — koi owner assign nahi hua, version record nahi hua. **Supporting context**
ki tarah enters, **wahi rehta hai**. Promotion law ke zariye hi move hota hai (3+ customers mein
pattern repeat ho, de-identified ho, review pass ho, expert apni voice mein rewrite kare).

### Chunking Jahan Governance Ghaib Ho Jati Hai

Vertical SoR ki ek entry **12 cheezein** carry karti hai (stable ID, domain, authority class,
jurisdiction, version, effective date, approval status, applicability, owner, superseded-by,
checker, permission boundary). Generic indexing pipeline **sirf sentence** rakhti hai — "Revenue may
be recognised when control transfers." Words bach gaye, **saari 12 controls gayab** — aur retrieved
text mein kahin nahi likha ke yeh gayab hain.

**Cure:** indexing rokna nahi — har search hit ko **pointer** samjho, kabhi answer nahi, aur har
synchronized item apni canonical identity rakhe taake confirmation step check kar sake.

⚠️ **Ek bara shortcut jo refuse karna hai:** ek vector database jo chat messages + purana contract
draft + sales rule + accounting policy sab mila kar rakhe **System of Context nahi hai** — ek unsorted
pool hai jahan: chat message standard ko outrank kar sakta hai, purani policy nayi ko, sales rule
accounting sawal ka jawab de sakta hai, ek country ka rule doosre mein apply ho sakta hai. Yeh **ek
accidental shadow System of Record** ban jata hai jo kisi ne banane ka faisla nahi kiya tha.

---
[⬅ Authority Scoped + Three Paths](02-authority-scoped-and-three-paths.md) · [Agla: Permission, Provenance, Conflict ➡](04-permission-provenance-conflict.md)
