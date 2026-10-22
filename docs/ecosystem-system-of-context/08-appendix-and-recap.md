# 08 — Appendix: End-to-End Example + Architecture Recap + Where to Go

## Appendix: One Cross-Domain Request, End to End

Ayesha ki firm mein — 6 mahine baad, usko apna accounting Vertical SoR hai, sales doosre se khareeda.
Partner message forward karta hai: *"20% discount approve kar sakte hain, aur June mein revenue book
kar sakte hain?"*

**Step 1 — Identify:** Partner poochh raha hai, customer client firm, case renewal contract, task
recommendation (**approval nahi**).
**Step 2 — Decompose+Route:** Discount authority mein? → Sales. Terms enforceable? → Legal.
Recognisable kab? → Accounting (Ayesha ka apna). Client ne kya agree kiya? → koi record nahi,
supporting context. Last invoice posted? → traditional record, live.
**Step 3 — Retrieve 3 modes mein:** Sales rule + Ayesha ka recognition reflex discovery index se,
record confirm karne ke baad. Client messages SharePoint se, permission-checked. Billing state live.
**Step 4 — Filter:** Partner sab dekh sakta hai. Junior hota to pricing history nahi dikhti.
**Step 5 — Assemble:** Ek packet — rules (apna record naam rakhte hue), time-stamped facts, client
messages (supporting context), 1 missing item (deliverable 2 ki acceptance evidence nahi), permission
envelope: **prepare+recommend only.**
**Step 6 — Conflict notice:** Sales rule 20% ko contract-size par permit karti hai. Accounting rule
kehti hai June mein recognisable nahi (acceptance evidence nahi). **Dono sahi — resolved by scope.**
**Step 7 — Reason+recommend:** Worker discount approve karne ki, June recognition **against**
recommend karta hai. Dono alag cite karta hai. Missing document naam karta hai. **Dono ko blend nahi
karta.**
**Step 8 — Act+record:** Partner discount approve karta hai. Sales record authority confirm karti
hai. CRM likhta hai+approver naam karta hai. Recognition sawal open rehta hai, conclusion+evidence
governed case record mein jati hai.

**Kya kabhi nahi hua:** koi record merge nahi hua, koi indexed copy cite nahi hui, koi live number
index se nahi aaya, kuch bhi partner-ki-permission-se-bahar nahi dikha, disagreement smooth nahi
hua.

## The Architecture in One Sentence

> **Kai domains. Kai Vertical Systems of Record. Ek System of Context unhe connect karta hai bina
> authority flatten kiye. Records truth own karte hain, layer relevance assemble karti hai, Worker
> permission ke andar reason+act karta hai, evidence us record tak wapis jati hai jiska result hai.**

Pehle truth banao (Agent Factory + Vertical record), phir context connect karo (customer systems,
identities, permissions, provenance), task assemble karo (authority+facts+support+gaps+citations),
Worker operate karo (governed tools+human approval), result record karo (jahan truth belongs).

## Where to Go From Here

Yeh page record aur engagement ke beech baithta hai. [Designing the Vertical SoR](../ecosystem-designing-the-vertical-sor/README.md)
ne governed truth banayi; hands-on build [Building the Context Layer](../context-layer-crash-course/README.md)
usay running software mein badalta hai — Onyx Standard deploy karta hai, 4 source classes connect
karta hai, record ko MCP par serve karta hai, permission gate prove karta hai. Phir: [Skills &
Connectors](../skills-connectors-crash-course/README.md) (MCP, OpenAPI, connector, typed-query
paths), [Eval-Driven Development](../eval-driven-development-crash-course/README.md) (proof — conflict
cases ke around evaluation set), [Building a Digital FTE](../digital-fte-crash-course/README.md),
[Human-Agent Teams](../human-agent-teams-crash-course/README.md).

> Yeh plumbing hai, aur **yehi point hai.** Koi plumbing nahi khareedta, lekin har building mein hoti
> hai. Asset jo client-to-client carry hota hai: governed profession + Layer 3 pattern. Fitting jo
> usay usable banati hai: company ke andar. Vertical FDE jo record ko customer ki real information se
> connect nahi kar sakta, woh "ek beautiful kitab un room mein pakde khada hai jahan koi shelf tak
> nahi pahonch sakta."
>
> **Record tumhe hire-worthy banata hai. Connecting layer tumhe keep-worthy banata hai.**

Yeh is wajah se Ecosystem group mein **sab se aakhir** aata hai.

## The Page on One Poster

Sharing/teaching/quick-revision ke liye — poori architecture ek poster par: 4 source classes (Agent
Factory SoR + Vertical SoR sealed-gold, customer systems sealed, working context unsealed-terra) → 7
operations (connect, identify, retrieve, filter, rank, assemble, deliver) → 3 gold control bands
(authority routing, permission-before-retrieval, provenance+citations) → temporary context packet (8
compartments, expiry stamp) → human+Worker (reason+act through governed tools) → evidence+result
record tak wapis. 3 lines: relevance ≠ authority; packet inherits authority+permissions+expires;
disagreement reviewable banta hai, ghaib nahi hota.

---
[⬅ Failure Modes, Templates, DoD](07-failure-modes-templates-dod.md) · [Agla: Test Your Understanding ➡](09-test-your-understanding.md)
