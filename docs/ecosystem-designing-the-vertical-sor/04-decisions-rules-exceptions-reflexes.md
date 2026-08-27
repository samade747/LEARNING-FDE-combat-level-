# 04 — Decisions, Rules/Judgment/Permissions, Exceptions, Rebuild Reflexes

## Map Decisions, Not Departments

Common mistake: builder 5 departments dekhta hai, 5 agents design karta hai — yeh org chart copy karta
hai, kaam behtar nahi karta. Customer ne handoffs ko kabhi value nahi diya, customer completed outcome ko
value deta hai.

Isliye outcome ke **decisions** map karo, purani desks nahi. Invoice review ke liye: supplier valid hai?
purchase order exist karta hai? goods receive hue? quantities/prices match karte hain? coding sahi hai?
duplicate hai? approval threshold cross karta hai? evidence payment ke liye kaafi hai? Yeh decisions
departments se zyada der tak zinda rehte hain — customer inhe alag teams ko de sakta hai, professional
logic reusable rehti hai.

Har decision ke 4 cheezein jaano: kaunsi evidence chahiye, kaunsa source govern karta hai, rule hai ya
judgment, aur kaun/kya decide kar sakta hai.

## Rules, Judgment, Aur Permissions — Teen Alag Cheezein

**Rules:** clear condition + clear result ("limit se upar approval chahiye"). Automatic checks ban jate
hain — asaan hissa.

**Judgment:** interpretation chahiye ("evidence kaafi hai?", "exception material hai?"). Support karo:
authoritative sources, expert guidance, examples/counterexamples, stated uncertainty, escalation boundary.
**Judgment ko lambe prompt mein chupao mat aur usay rule mat kaho.** Naam do, expert ki voice mein
sikhao, test karo.

**Permissions:** decide karti hain Worker conclusion ke baad kya *kar* sakta hai — Read, Search,
Calculate, Draft, Recommend, Request information, Prepare (undoable), Execute (undoable), Execute
(irreversible) — sab **alag grants**. Ek Worker jo payment prepare karta hai woh khud release nahi kar
sakta. Regulated domains mein safe start: Worker prepare + recommend karta hai, ek named human approve +
act karta hai. Zyada authority evaluations + customer governance se **kamaai** jaati hai, kabhi assume
nahi hoti. High-risk rules sirf words se nahi — **tool permissions, approval gates, policy checks** se
bhi enforce hoti hain, taake Worker ke sabse bure din bhi rule qaim rahe.

## Exceptions Ko Normal Path Se Pehle Design Karo

Routine cases demonstrate karna asaan hai. **Exceptions decide karti hain Worker trust ke laayak hai ya
nahi.** Standard reflex finish karne se pehle failure shapes list karo: missing evidence, conflicting
evidence, outdated sources, jurisdiction uncertainty, low-confidence conclusions, tool failures, deadlines
jo miss nahi ho sakte, customer instructions jo professional rules se conflict karein.

Har ek ke liye 4 cheezein define karo: kaise detect hoti hai, Worker kya kar sakta hai/nahi kar sakta,
escalation kisay milti hai, escalation mein kya hona chahiye. **Bar simple hai:** escalation insaan ka
kaam kam kare, chahe Worker complete na kar paye.

- Useless: *"main aage nahi badh sakta."*
- Useful: *"invoice payment ke liye recommend nahi ho sakta kyunke receipt proof missing hai; purchase
  order aur supplier record valid hain, amount tolerance ke andar hai; sirf receiving evidence open
  requirement hai; supervisor approval chahiye aage badhne ke liye."*

Pehla ek problem naam deta hai. Doosra insaan ko **ready-to-make decision** deta hai.

## Reflexes Rebuild Karo

Yeh poore method ka first-principles moment hai. Sawal classic hai: sirf outcome, invariants, aur Worker
kya kar sakta hai jaante hue — kaam kaise flow hona chahiye? Naye procedures expert ki apni voice mein
likho. Har reflex outcome + Bin 1 invariants ke around banao. Bin 2 ke honest purposes ko Worker
capabilities + checks ki tarah redesign karo. **Kuch bhi sirf isliye carry mat karo kyunke "hamesha se
aisa hi hota tha."**

Do purane design sawalon ke fresh jawab chahiye:
1. **Batch ya event?** Purana Friday review isliye tha kyunke insaani aankhein scarce thin. Poocho: Worker
   ko act karna chahiye jab document aaye, threshold cross ho, ya deadline nazdeek aaye? Batch sirf tab
   rakho jab real deadline require kare.
2. **Sequence?** Purana order org chart follow karta tha. Naya order **evidence aur risk** follow kare.

Har reflex ko itna chhota rakho ke **poora load ho sake** — ek outcome, ek reflex. Jo bhi lamba ho, reflex
usay corpus mein point kare, Worker on-demand retrieve kare.

**Phir naye ko purane ke against test karo** — loop ka step four. Contract of success apna baseline purani
duniya se leta hai (jaisa expert ne measure kiya), lekin signed contract ka baseline customer ka apna hai,
uske apne workflow mein measured. Design against expert's world; contract against customer's. Proof phir
**naye world** mein chalta hai, aur customer ke apne reviewers ko Worker ka output din-1 se accept karna
chahiye. Agar redesigned reflex woh kaam produce kare jo reviewers reject karein, **reflex galat hai,
reviewers nahi.**

## Build One Thin Slice, And Prove It

Poori profession attempt mat karo. Ek complete, trusted **slice** banao: ek outcome, uska outcome
contract, source hierarchy ka uska hissa, ek map, ek poori tarah derived reflex, ek permission list, ek
exception list, ek checker, ek evaluation set, ek governance process. Publish karo ek source ki tarah do
readers ke liye. **10 incomplete procedures kuch prove nahi karte. Ek procedure jo real professional
review se guzar jaye, poori architecture prove karti hai.**

**Do shabd, sirf breadth ke baare mein:** ek outcome wali SoR **thin** hai. Kai outcomes wali **thick**
hai — dono outcomes count karte hain, corners kabhi nahi. Har present outcome poora covered hai, chahe
kisi bhi state mein ho — governance pehle hafte se shuru hoti hai, baad mein nahi. Ek slice jo sirf clean
cases handle karta hai woh thin **nahi** hai — **unfinished** hai. Thin draft nahi hai, prototype nahi hai,
chhota corpus nahi hai — ek outcome poori standard + 3 regulator interpretations khich sakta hai, kyunke
size jo bhi decisions require karein wahi hai. Thick bhi kabhi "finished" nahi hoti, kyunke law badalti
rehti hai aur naye outcomes aate rehte hain.

**Thin kya khareedta hai?** Yeh ek slice sponsor conversation mein le jaane layak hai. Buyer apni profession
ka ek governed page parhta hai (top par plain words, neeche uske apne rules cited) — pitch nahi sun raha.

Evaluation set mein clean cases se zyada chahiye: incomplete cases, conflicting evidence, wrong-jurisdiction
sources, escalation cases, forbidden-action requests, aur cases jahan sahi jawab hai "evidence kaafi nahi
hai." Judge karo: sahi authority/version/jurisdiction use hui? Claims grounded hain, citations exact hain?
Har required check hui? Permissions ke andar raha? Non-routine cases pakri? Escalations ne reviewer ka
kaam kam kiya? Uncertainty honestly admit ki? Doosra reviewer record se result rebuild kar sakta hai?
**Polished demo proof nahi hai. Expert-reviewed passing evaluation set proof ki shuruaat hai.**

Governance content ke **saath hi hafte mein** banti hai, baad mein nahi — har source/map/reflex ko owner,
review, approval state, version milta hai. Har change ka **impact record**: kya badla, kyun, kisne approve
kiya, konse maps/reflexes/evaluations affected hue — is chain ke bina corpus current reh sakta hai jabke
reflex chupke se pichle saal ka rule apply kar raha ho.

**Coverage register** ([Template 7](06-templates.md)) mein state likho — fact hai, feeling nahi. Do engines
isay fill karte hain: naya outcome expert ke sath derive karo, ya customer customization 3+ customers mein
repeat ho aur promotion review pass kare. Naya jurisdiction naya build hai, apni coverage phir ek outcome
se shuru karta hai.

**3 cheezein SoR ko bara karti hain, thick nahi:** Agent Factory SoR se copy kiya method content (retrieval
noise + doosra version maintain karna), Layer 4 se upar move kiya customer content (contamination), aur
poore course mein grown orientation (unmarked textbook). **Sirf ek completed outcome thicken karta hai.
Baaqi sab weight hai.**

---
[⬅ 03 — Authority Vs Orientation](03-authority-vs-orientation.md) · [Agla: 05 — Failure Modes + Ayesha ➡](05-failure-modes-and-ayesha.md) · [⬆ Index](README.md)
