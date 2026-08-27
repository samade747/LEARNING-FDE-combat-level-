# 05 — 8 Failure Modes + Ayesha Ka Worked Example

## The Failure Modes

Aath tareeqe jin se yeh method galat ho sakta hai — jaldi pehchano taake waqt par cure lag sake:

1. **The document dump.** Sainkron files + semantic search, koi hierarchy/owners/versions nahi. Yeh
   searchable content hai, System of Record nahi. Cure: [source hierarchy](02-three-bin-sort-and-hierarchy.md#the-source-hierarchy--kaunsi-authority-jeette-hai).
2. **The AI-readable SOP.** Purani procedure Markdown mein convert kar di, purani duplication aur
   handoffs intact rakhte hue — pichla era, sirf faster. Cure: [three-bin sort](02-three-bin-sort-and-hierarchy.md#the-three-bin-sort).
3. **Technology first.** Vector database aur agent framework, outcome aur invariants se pehle. Technology
   kaam karti hai; professional system nahi karta. Cure: [outcome se shuru karo](01-outcome-and-archaeology.md).
4. **Rules hidden in prompts.** Important controls sirf system prompt ke jumlon ki tarah exist karte hain
   — unversioned, untested, unenforced. Cure: [rules/judgment/permissions alag rakho](04-decisions-rules-exceptions-reflexes.md#rules-judgment-aur-permissions--teen-alag-cheezein).
5. **Authority before evidence.** Worker ko submit/send/paisa move karne diya, uski knowledge evaluations
   pass karne se pehle. Cure: [thin slice + uska proof](04-decisions-rules-exceptions-reflexes.md#build-one-thin-slice-and-prove-it).
6. **The happy-path demo.** Ek clean example, kisi ne missing evidence ya wrong jurisdiction test nahi
   kiya. Trust edges par banta hai. Cure: [exceptions pehle design karo](04-decisions-rules-exceptions-reflexes.md#exceptions-ko-normal-path-se-pehle-design-karo).
7. **First-principles theater.** Sabse bold failure: Bin 1 delete kar dena kyunke woh purani habit lag
   rahi thi, phir customer ki compliance meeting mein pata chalna ke woh law thi. Cure: sort ki pehli
   warning — jab shak ho, Bin 1.
8. **The unmarked textbook.** Poore lesson chapters citable authority ki tarah load ho gaye, ya
   orientation chupke se course ban gayi. Worker ab rules ki jagah explanations retrieve karta hai, aur
   paraphrases authority ban jate hain jo drift kar sakti hain. Cure: [do content classes](03-authority-vs-orientation.md)
   — authority cite hoti hai, orientation marked aur short rehti hai.

## Ayesha Apni Khala Ka Checklist Sort Karti Hai

Poore page ko ek real artifact par chalte dekho. Ayesha ki khala usay firm ki working-paper checklist
deti hain: 41 items, 20 saal mein refine hui. Ayesha usay Accounting System of Record mein waisa hi load
nahi karti jaisa hai. Aur notice karo yeh kab ho raha hai: khala ne sign kar diya hai, licensing jawab
likhit mein hain, aur abhi koi customer nahi hai. Yeh checklist uska ekmatra raw material hai, aur woh
ise jo bhi banayegi, pehle buyer tak wahi le kar jayegi.

**Pehle outcome, sort se pehle likha gaya:** *ek complete working paper produce karo jo apne conclusion
ko applicable standards ke tehat support kare, har material conclusion ko sufficient evidence se link
kare, unresolved exceptions list kare, aur reviewer approval ke liye ready ho.* Phir archaeology: 5 real
files khala ke sath, jisme ek fail hui file bhi shamil hai. Aur woh sawal jo unwritten layer unlock karta
hai: *tum kya check karti ho jo checklist nahi kehti?*

**Phir sort:**

| Purana Element | Bin | Faisla Aur Wajah |
| --- | --- | --- |
| Supporting invoices ko photocopy kar ke file mein rakhna | 3 | Delete. Worker sources digitally attach karta hai, hash ke sath. |
| Har balance ledger se tick-and-tie karna | 2 | Redesign. Purpose (completeness) invariant banta hai; mechanism poora automated check ban jata hai + exception report. Reviewer 400 lines tick karne ki bajaye 5 exceptions parhta hai. |
| Junior prepares, senior reviews, manager reviews | Split | Har level apne purpose se sort hota hai. Standard/quality-policy-required review Bin 1 hai, rehta hai. Arithmetic/missing-references/incomplete-file catch karne wala review Bin 2 hai — Worker + checker ab yeh poora karte hain. |
| Partner ka going-concern judgment par sign-off | 1 | Untouched. Standards yeh judgment named human ko assign karte hain — firm ke clients isi signature ko khareed rahe hain. |

**Derived reflex**, khala ki apni voice mein likha: Worker period aur standard confirm karta hai, har
balance gather + tie karta hai, har source attach karta hai, checker chalata hai, aur insaano ke liye do
cheezein produce karta hai — exception report aur judgment file. Reviewer exceptions aur judgments review
karta hai, arithmetic nahi. Har sort decision apni reason ke sath System of Record mein record hota hai.
**Chaar ghante chalis minute ban jate hain.** Aur chalis minute poora us kaam par kharch hote hain jo sirf
insaan sign kar sakta hai.

Notice karo Ayesha ne abhi kya kiya: usne poora first-principles loop ek checklist par chala diya —
assumptions archaeology se likhe gaye, sachaiyan sort se separate hui, kaam un sachaiyon se rebuild hua,
aur result us ek review ke against test hua jo matter karta hai.

**Un chaar ghanton ke baare mein aakhri baat:** yeh khala ka number hai, khala ki practice se, aur yehi
hai jo Ayesha ne design against kiya. **Yeh abhi baseline nahi hai.** Jab Chicago ke ek firm ka partner
uska working-paper page parhta hai aur usay batata hai uske apne juniors per-file kitna kharch karte hain
— **wahi baseline hai**, aur tabhi contract of success draft ho sakta hai.

---
[⬅ 04 — Decisions, Rules, Exceptions](04-decisions-rules-exceptions-reflexes.md) · [Agla: 06 — Templates ➡](06-templates.md) · [⬆ Index](README.md)
