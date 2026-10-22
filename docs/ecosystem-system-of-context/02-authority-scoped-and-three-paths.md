# 02 — Authority Scoped Across Records, Teen Sawal Teen Raaste

## Authority Is Scoped Across Many Records

**Koi ek document har sawal nahi jeetta.** Company ek waqt mein kai governed records chalati hai —
sales, accounting, legal, sab apni apni authority ke sath. **Federated** ka matlab: kai records, har
ek apni authority rakhta hai, ek layer joda hai lekin merge nahi karta.

| Source | Kya govern karta hai | Kya nahi |
| --- | --- | --- |
| Agent Factory SoR | Shared architecture, method, standards | Customer facts, profession ka law |
| Vertical SoR (kai ho sakte hain) | Ek profession ke rules, hierarchy, reflexes | Doosri profession, ya kya morning mein delivery hui |
| Signed contract | Parties ki obligations, prices, rights | Accounting/professional method |
| Traditional SoR (ERP/CRM/ledger) | Current state apne scope mein | Us state ka professional matlab |
| Approved customer policy | Customer-specific thresholds | Law, binding standards |
| Working documents/messages | Explanation, intent, clues | Final authority (jab tak formally approved) |

**8 sawal** request ki shape resolve karte hain: (1) Kaunsi profession yeh sawal rakhti hai? (2) Kaun
poochh raha hai? (3) Kaunsa customer/case? (4) Kaunsa task? (5) Kaunsi jurisdiction/date? (6) Kaunsa
source kaunsa fact/rule rakhta hai? (7) Insaan/Worker kya parh sakta hai? (8) Kaunsi action follow
kar sakti hai? **Sawal 1 sabse pehle hai** — isay skip karo to baaqi sab galat ladder par chal jata
hai.

> **Relevance authority nahi hai. Retrieval candidates dhoondti hai. Governance decide karti hai kya
> count hota hai.**

**3 rules:** (1) Ek vertical ki methodology apni seam cross nahi karti (sales qualification rule
revenue-recognition sawal ka jawab nahi deti, chahe words overlap karen). (2) **Do records ko kabhi
ek corpus mein merge mat karo** — blended page kisi bhi profession mein cite nahi ho sakta. (3)
**Tumhara asset compose hota hai** — ek profession deeply jaano, layer usay doosron ke sath unmerged
rakhti hai. Isi liye kai Vertical SoRs hain lekin **sirf ek** Agent Factory SoR (method shared hai).

**Example:** customer "20% discount + is quarter revenue" poochta hai — yeh ek sentence, **8 alag
sawal** (qualified? authority mein? enforceable? compliance pass? kab recognisable? tax? kya discuss
hua (koi record nahi, supporting context)? delivered/invoice ho sakta hai? live record)। Layer 4 kaam
karta hai: todo, route karo, fetch karo, **ek packet banao jahan har finding apne source ka naam
rakhti hai.** Alternative (sab kuch ek search mein daal kar top passage se jawab) **ek alag
architecture hai, jahan koi authority nahi.**

**Seams hi interesting disagreements rakhte hain:** Sales "deal June mein close hui" (sahi), Accounting
"revenue abhi recognisable nahi" (bhi sahi) — dono alag sawal ka jawab de rahe hain, **resolved by
scope.**

## The Three Questions, and the Three Paths

Worker sirf **3 kism ke sawal** poochta hai:

| Sawal | Source | Raasta | Kya wapis aata hai |
| --- | --- | --- | --- |
| Rule kya hai? | Vertical/Agent Factory SoR | Retrieval, governed pages | Governed truth, citable, class/jurisdiction/version ke sath |
| Number kya hai? | Jo system number owns karta hai | Typed query over MCP | Exact current value, ya honest failure |
| Case ke baare mein kya kaha gaya? | Customer ki applications | Retrieval, ungoverned corpus | Supporting context — evidence, kabhi rule nahi |

Pehle do paths upar wale dono record-kisam ki taraf jate hain. **Teesra raasta kahin bhi authoritative
nahi jata** — isi liye isay sab se tight handling chahiye. Jo Worker yeh pehchan nahi sakta ke kaunsa
sawal poochha ja raha hai, teenon ko same tareeqe se jawab dega, aur teesra raasta chup-chaap pehle do
ko **swallow** kar lega.

---
[⬅ The One Law + Model Not a Source](01-authority-never-moves-model-not-source.md) · [Agla: Context Packet + Indexing Rules ➡](03-context-packet-and-indexing-rules.md)
