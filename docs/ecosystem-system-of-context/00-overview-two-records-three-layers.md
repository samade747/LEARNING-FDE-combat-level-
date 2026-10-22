# 00 — Overview: System of Context Kya Hai, Aur Do Record Upar Teen Layers

## System of Context — Ek Line Ki Pehchaan

> **A System of Record decides what is true. A System of Context decides what arrives.**

Yeh poore chapter ka core hai. Tumhara record (Vertical SoR) batata hai profession ko kya chahiye.
Customer ke apps batate hain abhi kya ho raha hai. **System of Context** dono ko connect karta hai —
current task ke liye kya relevant hai dhoondta hai, kaun dekh sakta hai check karta hai, har source ka
label rakhta hai, aur ek **cited bundle** reasoning ke liye handover karta hai. Yeh **koi apni truth
nahi banata** — delivery iska poora kaam hai, aur honest delivery sochne se zyada mushkil hai.

**Term kahan se aaya:** "System of Context" khud ki coinage nahi hai — Glean (is category ki sab se
mashhoor company) yehi naam apni data layer ke liye use karti hai. Book yeh term deliberately leti hai,
kyunke jo buyer ye word pehle se use karta hai wahi word graduate ko bolna chahiye. Lekin book ka usage
narrower hai: yeh koi product nahi, ek **architectural position** hai — layer jo do Systems of Record
ke upar aur Worker ke neeche baithti hai, authority kabhi khud nahi rakhti. Purane naam (insight
engines, cognitive search, enterprise AI search) bhi yehi cheez thay — **layer seekho, label nahi.**

### Chaudah Zaroori Words (glossary table)

| Word | Plain meaning |
| --- | --- |
| System of Context | Layer jo sources connect karti hai aur current task ki zaroorat assemble karti hai |
| Authority | Source ka haq ek particular sawal settle karne ka |
| Authority routing | Decide karna kaunsa source kaunsa hissa govern karta hai, retrieval se pehle |
| Context packet | Temporary, cited bundle — ek actor, ek case, ek moment ke liye |
| Provenance | Item kahan se aaya, kiska hai, kaunsa version, kab parha gaya |
| Connector | Controlled path ek source tak — content + access rules dono carry karta hai |
| Indexed context | Content jo searchable index mein copy ho ke sync rehta hai |
| Live context | Abhi ka information jo task chalte waqt source se fetch hota hai |
| Permission inheritance | Har item ki access rules uske home system se har result tak carry hona |
| Governed truth | Record se aane wala content — citable, class/version/scope ke sath |
| Supporting context | Ungoverned source se content — evidence ke taur pe citable, governing rule ke taur pe kabhi nahi |
| Federated | Kai alag records, har ek apni authority rakhta hai, ek layer joda hai lekin merge nahi karta |
| Canonical | Original, official version — kisi bhi copy ke muqable |
| Chunking | Document ko chhote pieces mein katna taake search index store kar sake |

## Kyun Vertical System of Record Kaafi Nahi Hai

Tumhare paas do Systems of Record hain: **Agent Factory SoR** (shared method — architecture, FDE AF
Model, manufacturing discipline, har Worker ke standards — har customer pe identical) aur **Vertical
System of Record** (profession ka corpus, map, reflexes, invariants, source hierarchy, permissions,
checkers, evaluations — sirf tumhara).

Dono mein se koi bhi customer ki **operating situation** nahi jaanta, aur jaan hi nahi sakta. Ek
revenue-recognition Worker ko professional method chahiye (record se) **aur** signed contract, har
modification, delivery record, current billings, approval limits (customer se). Ek recruiting Worker
lawful screening method perfectly jaan sakta hai aur phir bhi open role, approved description, candidate
ki application, hiring manager ki authority nahi jaanta. Ek ledger Worker standard jaan ke bhi nahi jaan
sakta ke 2023 mein lease ko finance lease kyun treat kiya gaya — jis insaan ne decide kiya wo firm chhod
gaya.

Worker ko do alag sawalon ka jawab ek sath chahiye:

> **What does the profession require?** aur **What is true in this case, right now?**

Systems of Record pehle sawal ko govern karte hain (aur dusre ke authoritative hissay ko). **System of
Context dono ko mila ke assemble karta hai.** Is layer ko skip karo to Worker standard perfect cite karega
aur contract dhoondh hi nahi payega — brilliant graduate textbook pakre khada hai, building mein jahan
koi filing cabinet nahi dikhaya gaya.

## Do Kisam Ke Record, Aur Ek Layer Upar

"Record" word ab do alag cheezon ko cover karta hai — customer ka ERP **kya hua** ka record hai, tumhara
Vertical SoR **profession ko kya chahiye** ka record hai. Dono authoritative hain, koi bhi dusre ka
sawal jawab nahi de sakta. **System of Context record hi nahi hai.**

| | **Traditional System of Record** | **Governed knowledge record** | **System of Context** |
| --- | --- | --- | --- |
| What it is | ERP, CRM, HRIS, general ledger, practice management system | Agent Factory SoR + har profession ka ek Vertical SoR, FDE AF Model se banaya | Connecting layer |
| What it owns | **State:** kya hua, balance kya hai, kisne approve kiya, kab | **Rules and method:** profession ko kya chahiye, kya evidence counts, kaunsa judgment escalate hota hai | **Koi apni truth nahi.** Connectors, indexes, routing policy, permission mappings, packet schemas, logs |
| It is authoritative over | Apne scope ke facts | Profession ki requirements aur build method | Kisi sawal pe nahi |
| What it decides | Truth ke baare mein kuch nahi | State ke baare mein kuch nahi | Filtering, routing, ranking, assembly |
| The question it answers | Number kya hai? | Rule kya hai? | Is task ke liye abhi relevant kya hai? |
| How a Worker reaches it | MCP pe typed query | Authored, governed pages pe retrieval, cited | Dono, plus ungoverned remainder |
| Who built it | Customer ne, decades mein | Tum ne, apne expert ke sath | Tum, har customer pe |
| What breaks without it | Business ruk jata hai | Har Worker profession improvise karta hai | Worker rules jaanta hai, file nahi dhoondh paata |

Teesri column ko exact kehna zaroori hai: **System of Context koi business fact, koi professional rule,
koi authoritative record nahi rakhta. Yeh sirf machinery rakhta hai jo unko locate, filter, route, aur
assemble karti hai.** Yeh din bhar real operational decisions leta hai — koi bhi decision truth ke
baare mein nahi hota.

**Pehle do records dono authoritative hain — alag kisam ki truth pe.** Ledger kabhi nahi batayega kya
treatment correct hai. Standard kabhi nahi batayega balance kya hai. Kisi se dusre ka sawal poocho, ek
confident lekin useless jawab milega.

### QuickBooks Data Rakhta Hai. Profession Nahi.

QuickBooks traditional accounting SoR hai — chart of accounts, har transaction, balances, invoices,
reconciliation state, kisne kab post kiya — sab rakhta hai, exactly sahi jawab deta hai, aur real
controls enforce karta hai (double-entry, period locking, user roles, audit trail). Yeh filing cabinet
nahi hai.

Ab poocho: kya Henderson lease ko current standard ke under finance lease classify hona chahiye tha?
Koi jawab nahi — kyunke yeh kabhi iska kaam nahi tha. Classification rule standard mein hai. Firm ka
threshold policy document mein hai. Is particular lease ka judgment partner ke zehan mein hai, ya kabhi
versioned na hui memo mein. **QuickBooks us judgment ka consequence faithfully record karta hai. Judgment
nahi rakhta, check nahi kar sakta.**

> **QuickBooks is authoritative about what was recorded. Your record is authoritative about whether it
> should have been recorded that way.** Dono ek working paper ke liye zaroori hain, aur connect karne se
> kisi ki bhi apni-sawal-pe authority nahi badalti — isi gap ki wajah se Vertical SoR exist karta hai.

Yehi sentence har vertical mein kaam karta hai: Salesforce deals rakhta hai, qualification method nahi.
Workday employment records rakhta hai, lawful screening standard nahi. Epic patient chart rakhta hai,
clinical guideline nahi. Har ek apne domain mein complete hai, profession ke baare mein khamosh — aur
yeh jaan-boojh kar design kiya gaya tha.

**Ek lafz ki ehtiyat:** vendor material yeh distinction ek biased word ke sath pesh karegi — traditional
record "sirf store" karta hai, context layer "interpret" karta hai. Neeche ka point sahi hai, lekin
phrasing meeting kharab kar degi. ERP ya practice system **sirf store nahi karta** — transactional
integrity, segregation of duties, approval limits, period control, audit trail enforce karta hai, aur
ye controls hi business ko chalne ki ijazat dete hain. Sahi aur zyada persuasive baat yeh hai: **gap scope
ka hai, seriousness ka nahi.** Jo buyer yeh sunta hai samajh jata hai ke tum uska trusted system replace
karne nahi aaye.

## Teen Layers, Teen Kaam

> Har layer ko sab teen kaam mat do. Records truth rakhte hain. Context layer relevant assemble karta hai.
> Worker reason aur act karta hai.

| Layer | Its question | Its job | What it must never become |
| --- | --- | --- | --- |
| **Systems of Record**, both kinds | What is officially true? | Facts, rules, versions, permissions, evidence govern karna | Ek loose search index |
| **System of Context** | What is relevant to this task, now? | Connect, route, retrieve, filter, rank, label, cite, assemble | Ek shadow source of truth |
| **Human or AI Worker** | What should be concluded or done? | Reason, authority ke andar decide, tools se act, evidence produce | Apna ungoverned policy maker |

Poori architecture iss ek distinction pe khadi hai, dobara parho: **System of Context Systems of Record
ke upar hai access mein. Authority mein nahi.** Yeh unke across dekh sakta hai, unko outrank nahi karta.
**Access upar jata hai. Authority wapas jaati hai.**

---
[Agla: Authority Kabhi Nahi Hilti, Model Source Nahi Hai ➡](01-authority-never-moves-model-not-source.md)
