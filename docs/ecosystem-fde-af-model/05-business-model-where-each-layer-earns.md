# 05 — Business Model: Har Layer Kahan Kamata Hai

Layers ek saaf commercial map dete hain, aur yeh do maps ek saath hain: platform kya kamata hai, aur
graduate kahan kamata hai.

## Platform Layers Panaversity Ki Hain

Layers 0 aur 1 ecosystem ke foundation ki tarah own aur operate ki jati hain, aur inka revenue platform
ka hai. Layer 1 **Systems of Record as a Service** se kamati hai — jo company apna khud ka governed
source chahti hai (policy manual, product catalog, procedures), usay kernel ka hosted instance milta
hai, ya support ke saath apna khud chalati hai.

Layer 2 education bhi platform ke liye revenue banata hai. Yeh sainkron learners tak bohot kam LLM
inference cost par pohanch sakta hai kyunke [connector-native apps](../connector-native-apps/README.md)
users ko apna khud ka AI model subscription laane dete hain. Platform storage, embeddings, authentication,
aur operations ke liye pay karti hai — lekin har learner ka main LLM usage bill nahi deti, jo scale ko
cap karne wali aam wajah hai.

## Graduate Ki Earning Layer 1 Se Shuru Hoti Hai, Aur Chadhti Hai

**Layer 1 par**, ek graduate ek client ke liye customized content System of Record banata hai. Client ka
domain content (manuals, standards, procedures) kernel mein load karta hai, governance set up karta hai,
aur build/upkeep ke liye charge karta hai. Kernel Panaversity ki rehti hai; service aur fee graduate ki
hain.

> Ek clarification: graduate ka apna pehla governed build aksar kisi client ke liye nahi hota. Yeh uski
> apni vertical ka thin slice hota hai, apne expert ke saath derive kiya, kisi ke liye paid nahi — aur
> yehi Layer 4 conversation ko mumkin banata hai. Client builds isi rung par paisa kamate hain. Unpaid
> slice vertical ladder kholti hai.

**Layer 2 par**, graduate Zia Developer AI ko Mode 2 mein use karta hai clients ke liye AI Workers aur
AI-native solutions manufacture karne ke liye. Generic tools deployed aur istemal ke liye free hain,
client outcome ke liye pay karta hai.

**Layer 3 par**, graduate apni khud ki domain startup banata hai. Ek domain expert ke saath partner karo,
vertical launch karo, aur teen tareeqon se kamao:

1. **Partnership** — expert apni approved persona aur rights-cleared authored material startup ko license
   karta hai. Startup expert twin bechta hai jo us license par bani hai, aur expert ke saath revenue
   share karta hai.
2. **Domain education** — domain SoR us domain ke crash courses bhi carry karti hai, to wahi asset jo
   expert twin ko power deta hai profession ko bhi sikhata hai.
3. **Domain products** — domain builder se startup ready-made, domain-specific AI Workers, aur poori
   AI-Native Company blueprints manufacture karti hai, aur unhe domain ki kai companies ko bechti hai:
   ek baar banao, kai baar becho.

**Layer 4 par**, startup FDE engagements chalati hai: discovery aur outcome design, deployment, aur
recurring revenue managed operation, governance, aur continuous improvement se. Domain builder shared aur
versioned hai, to har customer domain ke improvements updates ki tarah paata hai. Retainer (monthly fee)
Workers kharidta hai jo behtar hote rehte hain, sirf chalte nahi rehte.

## Kya Charge Karein, Aur Kis Basis Par

**Market ne hamara unit of sale naam kiya.** Agent pricing frameworks ab agent-based model include karte
hain, jo agent ko ek full-time employee ke replacement ki tarah price karta hai — yehi hai **Digital
FTE**, ek hire ki tarah measure kiya hua.

**Market ne hamara contract naam kiya.** Outcome-based pricing ek result ke liye charge karti hai,
activity ke liye nahi. Isko yeh chahiye: ek agreed starting number, ek target, aur acceptance criteria
jo ek reviewer check kar sake — yehi **contract of success** hai, jo yeh model hamesha se mandatory
bana raha hai.

**Market ne hamara structure naam kiya.** Hybrid pricing (base fee plus variable component) ab sabse aam
arrangement hai. Layer 4 par yeh bilkul wahi hai: engagement plus retainer.

**Aur premium ka bees saal ka proof hai.** Kevin Bai ke mutabiq, Fortune 500 ko serve karne wale public
SaaS companies mein, average contract value se ranked, Palantir number 1 hai (~$4 million), ServiceNow
agla (~$1.2 million), Workday (~$600,000). Discipline jo outcome pricing ko mumkin banati hai, wahi hai
jisne ek vendor ko do dahaakon tak going rate se kai guna zyada charge karne diya.

| Kya Bechte Ho | Kis Ke Against Price | Kahan |
| --- | --- | --- |
| Engagement | Contract of success: baseline, target, acceptance criteria | Layer 4 |
| Managed operation | Woh Workers jo chalate ho aur unhe milne wale improvements | Layer 4 retainer |
| Ready-made Workers aur blueprints | Ek baar banaya, domain ki kai companies ko becha | Layer 3 products |

Do cautions: **Outcome pricing risk aap par daalti hai** — agar aap result ke liye charge karo, agar
Worker result na de to cost aap uthate ho. Yeh sirf tab affordable hai jab checker real ho aur evaluation
set awkward cases cover kare. Aur **guardrails zaroori hain** — har main number dishonestly produce ho
sakta hai. Contract of success ke guardrails aapki pricing model ko customer ko nuqsan pahunchane se
rokte hain.

## Malikiyat, Pehle Se Agreed

| Kya | Kis Ki Hai |
| --- | --- |
| Foundation aur generic components (Layers 0–2) | Panaversity, jo platform chalati hai |
| Vertical corpus aur expert twin (Layer 3) | Graduate ki domain startup, expert ke saath jointly |
| Ek customer ka apna SoR corpus (Layer 1 instance) | Customer ka content customer ka rehta hai; kernel Panaversity ka |
| Domain builder (ek per domain, versioned) | Woh vertical jo isay maintain karti hai — sab customers ke darmiyan shared, kabhi fork nahi |
| Customer data aur confidential ontology (Layer 4) | Customer retain karta hai |
| Ek generalized capability jo neeche promote hui | Platform ya vertical, contract mein agreed promotion rights ke saath |

Model ek fair sawal ka jawab bhi deta hai: graduate ki startup Panaversity ke maalik kernel par depend
karti hai, agar platform ke terms badlein ya platform fail ho jaye, kya protect karta hai? **Structural
portability** — corpus plain, versioned Markdown use karta hai; retrieval standard Postgres/pgvector use
karti hai; content open MCP protocol se serve hoti hai. Vertical ke assets (corpus, expert ki license,
customer relationships) partnership ki hain aur portable design ki hain. Contractually, ek vertical ke
platform terms partnership agreement mein launch se pehle set hote hain, aur ek chalti hui business ke
neeche se badalte nahi.

---
[⬅ The One Law](04-the-one-law-and-agent-readable-base.md) · [⬆ Index](README.md) · [Agla: Limits Aur Shuru Kahan Se ➡](06-limits-and-where-to-start.md)
