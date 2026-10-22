# 06 — Reference Implementation, Kab Zaroorat Nahi, Ayesha Ka Pehla Customer

## The Open Reference Implementation

Yeh page **idea** sikhati hai, product nahi — lekin practice ke liye kuch real chahiye.

> **Onyx** is book ka open reference implementation hai System of Context ka. **Glean** best-known
> commercial example hai. Doctrine product-independent hai.

Hands-on build: [Building the Context Layer](../context-layer-crash-course/README.md). Student
multiple sources connect kar sakta hai, sync dekh sakta hai, ek request ko identity se routing se
packet tak trace kar sakta hai, citations inspect kar sakta hai, conflict test kar sakta hai.

**4 interfaces open rehna chahiye**, chahe koi bhi product deploy karo (yehi layer ko replaceable
banate hain): (1) **MCP** (agent-facing knowledge+tools), (2) **OpenAPI** (governed capabilities), (3)
**Connectors/ingestion APIs**, (4) **Source-owned identifiers+citations**.

⚠️ **Onyx Community Edition** connectors/indexing/retrieval/citations/agents sikhane ke liye kaafi
hai — **lekin production permission fidelity prove karne ke liye kaafi nahi.** Permission-sync
connectors, user-groups, RBAC — Onyx ki apni docs Enterprise Edition features batati hai. Isi liye
student labs public/synthetic/class-authorized data use karte hain jab tak permission gate pass na
ho.

## When You Do Not Need One

**Har vertical ko yeh layer nahi chahiye** — jaldi banana ek quarter waste karne ka real tareeqa hai.
Zaroorat nahi jab governed record + customer ke operational systems mil kar har sawal ka jawab de
dete hain (jaisa tax practice jiska kaam code+filings+ledger se defined hai).

Zaroorat hai jab "why was it done this way" ka jawab **har governed system se bahar** rehta hai —
audit firms (20 saal working papers), legal practices (matter files), consultancies (reasoning decks/
threads mein). **Institutional memory** deliverable ka hissa ho to layer apni cost deserve karti hai.

> **Ek gate non-negotiable hai: System of Context mat banao jab tak thin slice khatam na ho aur
> pehla Worker usay cite na kare.** Connecting layer jiske paas connect karne ko kuch governed na ho,
> **ambitions wala search box** hai.

## Two Temperaments, One Layer

Design page ko 2 poore worked examples chahiye the (Sales vs Ledger) kyunke **record** har profession
mein genuinely alag hota hai. Yeh layer **almost nahi badalti** — 8 invariants, 3 sawal, indexing
rules sab identical.

| | Sales | General Ledger |
| --- | --- | --- |
| Ungoverned material kahan hai | Center mein — transcripts/emails deal-file ka evidence base |
| Sab se heavy connection | Conversation records, indexed |
| Sawal 3 kya poochta hai | Buyer ne kya kaha, kab |
| Characteristic mistake | Offhand remark confirmed field ban jati hai |
| Permission failure ki cost | Confidentiality breach |

(Ledger: edge mein, accounting system live query, "yeh pehle kyun treat hua", stale indexed balance
current ki tarah answer, access review jhooti picture certify karti hai)

**Sales uncomfortable case hai** — call transcript ek hi waqt supporting-context aur deal-file ki
primary evidence hai. 6-evidence-states discipline isay hold karti hai. **Ledger sharper lesson** hai
— permission failure sirf information expose nahi karti, entitlement model se bahar effective access
deti hai jisay firm ki access review certify karti hai.

## Ayesha Connects Her First Customer

Chicago firm ka partner Ayesha ki working-paper page parh kar engagement sign karta hai — ab uska
record room mein **sab se chhoti cheez** hai. Firm ke paas 22 saal ke working papers (SharePoint),
engagement letters (email), senior manager ke zehan mein reasoning, trial balance (hourly badalta
system) hai.

**Woh authority route karti hai kuch connect karne se pehle:** "Going-concern evidence ke liye
standard kya chahta hai?" = Vertical SoR (governed, cited). "Account 1200 ka closing balance abhi
kya hai?" = typed query, **kabhi index nahi**. "Henderson lease 2023 mein finance lease kyun treat
hua?" = SharePoint — **yehi wajah hai yeh firm ko context layer chahiye.**

**Phir woh permissions test karti hai answers test karne se pehle.** First-year junior ki tarah login
karti hai, compensation policy poochti hai — correct result **kuch nahi** hona chahiye. Engagement
manager, partner — teenon test karti hai. Tab doosra source connect karti hai.

**Ek line likhti hai engagement design record mein:** *"Firm ka apna material is client ke baare mein
evidence hai. Profession ki requirements record se aati hain. Worker dono ko kabhi confuse nahi
karega."*

6 hafte baad, Worker lease classification prepare karta hai: standard cite karta hai, 2023 memo alag
se attach karta hai (firm's prior treatment), **report karta hai ke dono disagree karte hain**,
kaunsa authority test apply hua batata hai, partner ko escalate karta hai. Partner agree karta hai —
3-saal purani treatment correct ho jati hai. **Ordinary similarity search yeh khud nahi karti** — yeh
design+test karna parta hai.

---
[⬅ Read-Reason-Act, Invariants, Placement](05-read-reason-act-invariants-placement.md) · [Agla: Failure Modes, Templates, Definition of Done ➡](07-failure-modes-templates-dod.md)
