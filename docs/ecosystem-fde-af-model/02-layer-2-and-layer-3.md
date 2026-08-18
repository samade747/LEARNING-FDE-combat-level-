# 02 — Layer 2 Aur Layer 3: Teaching Ecosystem Aur Vertical Trio

## Layer 2 — The Teaching And Development Ecosystem

Plain words mein: yeh poora method sikhata hai aur banane ke tools deta hai. Aap [Zia Tutor AI](../ecosystem-zia-tutor-ai/README.md)
se seekhte ho aur [Zia Developer AI](../ecosystem-zia-developer-ai/README.md) se banate ho.

**Produce karta hai:** reusable components aur unhe combine karne ka ek standard tareeqa.

- **learning component** — progress aur memory store karta hai
- **pedagogy component** — kaise sikhana hai control karta hai
- **builder component** — users ko agents aur solutions banane mein madad karta hai

Har component MCP tools aur agent skills deta hai. Ek agent skill ek `SKILL.md` file hoti hai jisme
instructions aur judgment hote hain jise agent load aur follow kar sake. Chhote connectors, **MCP
gateways**, kai components ko ek product mein combine karte hain.

Jaise ek teaching gateway content source, pedagogy component, aur learner ki progress ko jorta hai — mil
kar ek tutoring product ban jata hai.

Layer 1 ki tarah, Layer 2 bhi already deployed hai. Agent Factory do reference products chalati hai AI
apps ke andar jo log already use karte hain: teaching ke liye Zia Tutor AI, development ke liye Zia
Developer AI.

Ek boundary rule zaroori hai: **yeh do products generic rehte hain.** Ek profession-specific vertical
Zia Tutor AI ya Zia Developer AI ko modify nahi karti. Iske bajaye woh wahi components reuse karke Layer
3 par apne khud ke gateways banati hai.

**Consume karta hai:** aaj ke learners, aur kal ka Layer 3, jo Layer 2 ko apni component library ki
tarah treat karta hai.

> *Yahin Ayesha ne training li: crash courses ne usay model sikhaya, Zia Tutor AI ne uske sawal ka jawab
> diya, aur Zia Developer AI ne uska pehla agent banane mein madad ki.*

## Layer 3 — Vertical Ecosystems

Plain words mein: yeh poori cheez ek profession ke liye package karta hai. Package mein us profession ki
knowledge, uska apna AI teacher, aur uska apna AI builder hota hai.

**Produce karta hai:** domain **trio**, ek har vertical ke liye (ek vertical ek industry ya profession
hai, jaise accounting ya healthcare). Trio ke teen parts:

1. **Domain System of Record** — regulations, procedures, catalogs, ya protocols ka authoritative corpus,
   Layer 1 kernel ke through serve hua.
2. **Domain expert twin** — Zia Tutor AI pattern mein ek gateway, wahi Layer 2 components se compose ki
   hui, jahan us domain ka expert apni voice mein sikhata hai. Expert twin expert ka real naam aur
   likeness use karta hai, unki documented consent se — kabhi synthetic substitute nahi.
3. **Domain builder** — Zia Developer AI pattern mein ek gateway, us domain ki architectures aur
   compliance constraints ke saath preloaded. Yeh vertical ka manufacturing tool hai — graduate isay
   Layer 4 par use karke us domain ke AI Workers (Digital FTEs) manufacture karta hai.

### Domain Knowledge Ki Teen Forms, Ek Governed Ghar

Jab aap ek vertical banate ho, ek profession ya industry ke liye ek AI system, aapko decide karna hota
hai ke agent har tarah ki domain knowledge kaise paayega. Knowledge ki teen forms hain, har ek ka apna
kaam:

**1. Corpus — evidence deta hai.** Ek bara, organized collection of trusted source material: regulations,
standards, manuals, policies, procedures. Yeh woh information rakhta hai jise agent **cite** kar sake.
Corpus knowledge ka collection hai, System of Record us knowledge ke gird governed system hai — ownership,
review, approval, versioning, access control, stable IDs, search, citation support. Agent do tareeqon se
pahunchta hai: meaning se search, ya ek **stable ID** se poora section fetch karna (jo update ke baad bhi
usi section ki taraf point karta rehta hai).

**2. Map — agent ko batata hai kya exist karta hai.** Map ek chhoti agent skill hai jo corpus ka overview
deti hai: main sections, har section mein kaunsi knowledge, kaise search karna hai, aur kab agent ko ek
particular source parhna **zaroori** hai. Map isliye zaroori hai kyunke search ki apni kamzori hai — agent
sirf woh dhoond sakta hai jo woh dhoondna janta hai. Map hamesha available rehta hai, to agent ko pata
hota hai kya exist karta hai. Map domain ke non-negotiable rules bhi batata hai (jaise: agent kabhi bina
human approval ke paisa move nahi kar sakta). High-risk actions ke liye likhe hue instructions kaafi nahi
— rules ko tool permissions, human approval gates, aur automated policy checks se bhi enforce karna hota
hai.

**3. Reflexes — agent ko batate hain kya karna hai.** Reflexes procedural skills hain jo agent sahi waqt
par load karta hai: ek checklist jo poora complete karna hai, ek required form ya template, ek checker
script, ek step-by-step procedure. Yeh incomplete pieces mein search se wapas nahi aane chahiye — agent
ko task shuru karne se pehle poora procedure milna chahiye.

Simple test: agar agent ko information **dhoondni aur cite karni** hai, corpus mein jati hai. Agar agent
ko information **load karke follow karni** hai task sahi karne ke liye, skill mein jati hai. Kuch
knowledge dono forms mein hoti hai — poori authoritative detail corpus mein, skill batati hai kab aur
kaise use karna hai. Skills bhi likhi, reviewed, approved, aur versioned hoti hain System of Record ke
andar hi.

### Ek Discipline Jo Layer 3 Ko Maintenance Nightmare Banne Se Rokti Hai

Har domain ka **ek builder hai, har customer ka apna nahi.** Wahi domain builder us domain ki har company
ke liye AI Workers manufacture karta hai. Jab builder behtar hota hai, yeh ek jagah update aur version
hoti hai, to har company ke Workers consistent rehte hain. Customer-specific cheezein customer ke Layer 4
instance mein rehti hain, builder ke andar kabhi nahi.

Agar aap har customer ke liye builder fork karo, aap wahi inherit karte ho jise promotion law rokna
chahti hai: kai builder versions, kai diverging Workers, hamesha maintain karne wale. Yeh Palantir ki key
move hai, ab graduate ke haath mein.

**Consume karta hai:** us domain ke professionals aur unke liye deploy karne wale FDEs.

Humari pehli vertical **sales** hai, uska founding corpus (FISTA Sales Book) complete hai. Doosri, abhi
validation mein, **accounting** ke liye ban rahi hai. Har vertical ko ek jurisdiction ke liye bhi adapt
karna hota hai — jaise US GAAP/IRS rules ke liye bana trio ek alag opportunity hai UK ya Gulf clients ke
liye. Kaunsi vertical aapko banani chahiye, iska apna method hai:
[Choosing Your Vertical](../ecosystem-choosing-your-vertical/README.md). Aur teeno forms ko fill karna
apna discipline hai, kyunke profession ka current workflow purane era ke human limits ke liye design hua
tha: [Designing the Vertical System of Record](../ecosystem-designing-the-vertical-sor/README.md).

> *Ayesha apni aunty ke saath partner hoti hai, jo bees saal se accountant hain: aunty expertise aur apni
> authored material laati hai, Ayesha uske gird trio banati hai.*

---
[⬅ Layer 0 Aur Layer 1](01-layer-0-and-layer-1.md) · [⬆ Index](README.md) · [Agla: Layer 4 ➡](03-layer-4-customer-instances.md)
