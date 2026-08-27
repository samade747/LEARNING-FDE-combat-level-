# 08 — Appendix B: General Ledger System Of Record, End To End

**Ek boundary pehle**, aur accounting mein yeh dugna matter karti hai, kyunke profession pehle se hamara
term use karti hai. Accountants general ledger ko khud "**the system of record**" kehte hain, aur woh
sahi hain. ERP books hold karta hai, aur yehi kaam wo rakhta hai. Yeh page jo Vertical System of Record
banata hai, alag cheez hai — woh govern karta hai ke close **kaise** hota hai. Kaunsi evidence balance
reconcile karti hai. Kaunse rules kaunse period par apply hote hain. Sirf controller kya approve kar
sakta hai. Worker kya prepare kar sakta hai. **ERP numbers hold karta hai. System of Record profession
hold karta hai.**

## Accounting Outcome

**Weak outcome:** *month-end close automate karo.* **Derived outcome:** ek entity ke liye complete
month-end close file produce karo — har balance-sheet account supporting evidence se reconciled, har
adjusting journal entry supported aur approved, har unexplained difference apni amount aur age ke sath
materiality ke against listed, controller sign-off ke liye ready.

Outcome contract, filled in. **Trigger:** period end nazdeek aata hai, reconciliation events poore mahine
chalte hain. **Main number:** days to close (expert ki apni practice: aath working days, teen design
target hai; har customer ka apna starting value usi customer par measure hota hai). **Guardrails** — aur
close ka apna inflation risk hai: post-close adjustments na barhein, audit findings worse na hon, aur
unexplained-difference total na barhe. Worker ko **kabhi fast close ke liye reward nahi milna chahiye jo
slow problems chhupaye**.

**Forbidden actions:** Worker kabhi journal entry post nahi karta, kabhi period open/close nahi karta,
kabhi master data change nahi karta. **Final authority:** controller close sign karta hai. **Record:**
close file, har reconciliation/entry/support/approval ke sath.

## Accounting Archaeology

Purana close, ek real finance department se. Trial balance download karo. Har account ke liye Excel
reconciliation banao. Bank statement PDFs ke against balances tick karo. Sub-ledger owners ko email se
chase karo. Approval emails attached journal vouchers prepare karo. Sub-ledger totals dobara trial
balance workbook mein type karo. Sab kuch close-checklist spreadsheet mein track karo. Aath din, zyada
tar apne hi numbers mein digging karte hue.

Unwritten layer: senior accountant jaanta hai kaunse accounts hamesha misbehave karte hain, aur kaunse
sub-ledger owner ko teen reminders chahiye. Woh jaante hain kaunsi chhoti differences carry karna safe
hai, aur kaunsi ek real problem ki pehli nishani hai. Archaeology domain ki well-known bad habit bhi
dhoondti hai: differences force-match ki jati hain, aur chhote unexplained items mahino tak carry forward
hote hain jab tak koi unhe question hi nahi karta. **Suspense account** aise balances hold karta hai jo
investigate hone chahiye thay aur kabhi nahi hue. Sab kuch sort mein Bin 2 mechanisms ki tarah jata hai
— inka honest purpose, **har difference investigated ya visibly aged**, invariant ban jata hai.

## Accounting Sort

| Purana Element | Bin | Faisla Aur Wajah |
| --- | --- | --- |
| Bank statements print aur file karna | 3 | Delete. Statements digitally attach hote hain, hashed. |
| Har account ke liye monthly Excel reconciliation | 2 | Redesign. Reconciliation continuously chalta hai jaise transactions post hoti hain; close results dig karne ki bajaye assemble karta hai. |
| Journal entry ka preparer aur approver alag hone chahiye | 1 | Keep, exactly. Segregation of duties ek core control invariant hai, control framework aur audit standards require karte hain. |
| Close-checklist spreadsheet | 2 | Redesign. Checklist live close state ban jati hai, hamesha visible. |
| Controller har reconciliation review karta hai | 1 purpose, 2 mechanism | Control (materiality oversight) rakha jata hai; mechanism badalta hai: threshold se upar exceptions controller ko route hoti hain, aur har entry jo mandatory-review account (cash, revenue, equity, related parties, late/unusual entries) chhue, chahe amount kuch bhi ho. |
| Month-end batch | Split | Reporting deadline Bin 1 hai — period ek legal reality hai. Kaam ko month-end mein batch karna Bin 2 hai — kaam poore mahine spread hota hai, deadline jald poori hoti hai. |
| Sub-ledger totals workbook mein dobara type karna | 3 | Delete. Systems ab baat karte hain. |

**Month-end row is appendix ka best lesson hai:** ek purana element do bins mein split ho sakta hai.
Deadline invariant ki tarah survive karta hai. Uske peeche ka kaam nahi.

## Accounting Invariants

Close file ko teen states alag rakhne chahiye: reconciled with evidence, explained but not yet cleared,
aur unexplained. **Ek explained difference ko reconciled likhna accounting ka invented-citation version
hai.** Har balance in teen states mein se exactly ek rakhta hai, aur jo bhi poori tarah reconciled nahi
woh apni amount aur age ke sath exception list par jata hai.

Har journal entry ka support hota hai, aur uska approver preparer nahi hota. Koi posting closed period ko
controller approval ke bina touch nahi karti. Applied rules woh hain jo reporting period ke liye effective
hain — version correctness ka hissa hai. Missing statements ko kabhi reconciled nahi maana jata. Approval
ke baad amount/account/period/entity chhoone wala koi bhi change approval ko invalidate karta hai — entry
review se dobara guzarti hai, kyunke approval usi ko cover karta hai jo approve hua tha, jo woh ban gaya
usay nahi. **Worker sirf prepare aur recommend karta hai.**

## Accounting Hierarchy, Decisions, Aur Permissions

Hierarchy deep hai kyunke domain law-governed hai. Aur yahan main page ki ladders wali warning real ban
jati hai: accounting ki **ek ladder per question** hoti hai, ek overall ladder nahi. Worker pehle sawal
identify karta hai — financial reporting, tax, ya kuch aur — phir usi sawal ki ladder use karta hai
(yeh United States example hai; apni jurisdiction ke bodies substitute karo):

**Financial-reporting treatment:**
1. Applicable reporting framework (US GAAP / IFRS, licensing register ke zariye handle)
2. SEC accounting/disclosure requirements (ya apne desh ka securities regulator)
3. Firm ki accounting policy manual, jahan framework choice permit kare
4. Expert-authored close procedures, licensed rung
5. Client ka chart of accounts + thresholds — customer layer par rehte hain, shared vertical mein kabhi
   nahi jate
6. Prior close files, sirf examples ki tarah

**Tax treatment**, alag ladder: applicable federal/state/local tax law; official tax regulations/
interpretations; firm ki approved tax policy/advice. Tax law US GAAP/IFRS ko financial statements ke
andar outrank nahi karti — woh alag sawal govern karti hai.

Permissions Appendix A ka mirror hain: ledger/sub-ledgers/bank feeds parho. Reconciliations prepare karo,
entries draft karo. Recommend aur explain karo. **Aur kuch nahi.** Koi posting nahi, koi period control
nahi, koi master data nahi. Law-governed domain mein, **preparation boundary hi starting position hai**.

## Ek Accounting Exception, Ek Reflex

Exception: close ke pehle din bank feed fail ho jata hai. Worker account ko reconciled mark nahi karta,
aur chup chaap wait bhi nahi karta. Woh jitne accounts reconcile kar sakta hai karta hai, affected
accounts unke last-known state ke sath list karta hai, bank ko request draft karta hai, aur escalate
karta hai: *teen accounts reconcile nahi ho sake kyunke feed 30 tareekh ko ruk gayi; baaqi sab accounts
complete hain; affected balances pichle mahine 1% se kam move hue; bank ko request draft ho chuki hai;
agar feed Wednesday tak wapas aaye, close date qaim rehti hai.*

**Ek aur exception jo vertical ki spine test karti hai:** ek executive aisi entry maangta hai jo evidence
support nahi karti. Worker ka response **seniority se nahi, invariant se fix hota hai**: request record
mein preserve karo, entry routine ki tarah prepare mat karo, controller ko escalate karo. **Jo System of
Record rank ke liye bend ho jaye, woh system of record nahi hai.**

Close reflex, ek saans mein: jaise transactions post hon, match karo; jaise statements aayen, tie karo;
jaise differences dikhein, age karo; period end par, file assemble karo, adjusting entries citations ke
sath draft karo, checker chalao, exceptions materiality se route karo, aur controller ko woh close pesh
karo jo har jagah band ho chuki hai jahan insaan required nahi tha. **Aath din teen ban jate hain.**

---
[⬅ 07 — Appendix A: Sales SoR](07-appendix-sales-sor.md) · [Agla: 09 — Contrast, Poster, Aage Kya ➡](09-appendices-contrasted-and-next-steps.md) · [⬆ Index](README.md)
