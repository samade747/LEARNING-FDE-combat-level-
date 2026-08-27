# Reference Solution — Ayesha Sorts Her Aunt's Checklist

Yeh chapter ke [05 — Failure Modes + Ayesha](../../05-failure-modes-and-ayesha.md) ka worked example hai,
templates ke format mein dobara likha gaya — **compare karne ke liye, copy karne ke liye nahi.** Apna
worksheet fill karne ke baad isse check karo: kya tumhare invariants sach mein invariants hain? Kya
tumhara reflex "purani SOP ko markdown" nahi hai?

## Context

Ayesha ki khala (aunt) ek accounting firm chalati hain. Woh Ayesha ko firm ki working-paper checklist
deti hain — 41 items, 20 saal mein refine hui. Khala ne sign kar diya hai, licensing jawab likhit mein
hain, abhi koi customer nahi hai.

## Template 1: The Outcome Contract

| Field | Ayesha Ki Entry |
| --- | --- |
| Outcome | Ek complete working paper produce karo jo apne conclusion ko applicable standards ke tehat support kare, har material conclusion ko sufficient evidence se link kare, unresolved exceptions list kare, reviewer approval ke liye ready ho |
| Trigger | Period-end close ka schedule |
| Inputs | Ledger balances, bank statements, supporting invoices/contracts |
| Evidence | Har balance ka tie-out, har entry ka source document |
| Acceptance criteria | Reviewer conclusion ko evidence se trace kar sake, exceptions list ho |
| Main number | Hours per working paper (khala ki practice: 4 ghante — design-against number, baseline nahi) |
| Forbidden actions | Missing evidence ko confirmation ki tarah treat karna |
| Final authority | Partner (going-concern judgment ke liye) |
| Record | Sort record, exception report, judgment file |

## Template 2: The Sort Record (Sample Rows)

| Old element | Kyun exist karta hai? | Bin | Faisla | Reason |
| --- | --- | --- | --- | --- |
| Supporting invoices photocopy kar ke file mein rakhna | Purani technology, physical filing | 3 | Delete | Worker sources digitally attach karta hai, hash ke sath |
| Har balance ledger se tick-and-tie karna | Human attention limited, items miss ho sakte hain | 2 | Redesign | Purpose (completeness) invariant banta hai; mechanism automated check + exception report ban jata hai |
| Junior prepares, senior reviews, manager reviews | Split — kuch quality-policy-required, kuch arithmetic-catching | Split | Redesign (arithmetic hissa) / Keep (quality-required hissa) | Har level apne purpose se sort hota hai |
| Partner ka going-concern judgment par sign-off | Standards named human ko assign karte hain | 1 | Keep | Firm ke clients isi signature ko khareed rahe hain |

## Template 3: The Invariants List (Sample)

| # | Invariant | Source | Enforced by |
| --- | --- | --- | --- |
| 1 | Har conclusion traceable evidence se support hona chahiye | Audit standard / firm quality policy | Checker + reviewer sign-off |
| 2 | Missing evidence ko kabhi confirmation nahi maana jayega | Firm quality policy | Checker (blocks "reconciled" state bina evidence) |
| 3 | Going-concern judgment sirf partner sign kar sakta hai | Professional standard | Tool permission + approval gate |

## Derived Reflex (Khala Ki Voice Mein)

1. Period aur applicable standard confirm karo.
2. Har balance gather aur tie karo.
3. Har source digitally attach karo (hash ke sath).
4. Automated checker chalao — completeness aur balancing dono.
5. Exception report produce karo (jo bhi automated check fail hua).
6. Judgment file produce karo (going-concern aur doosre judgment-required items).
7. Partner ko sirf exceptions aur judgments route karo — arithmetic nahi.

**Result:** 4 ghante → 40 minute. 40 minute poore us kaam par kharch hote hain jo sirf insaan sign kar
sakta hai.

## Evaluation Set — Non-Happy-Path Cases (Sample)

**Case 1:** Ek balance ka supporting bank statement missing hai.
*Sahi jawab:* Checker isay "unexplained" mark kare (reconciled nahi), exception report mein amount +
age ke sath list ho.

**Case 2:** Ek junior ne ek chhota difference "immaterial" mark kar diya hai bina reason ke.
*Sahi jawab:* Worker materiality threshold check kare; agar threshold se upar hai, exception list mein
wapas jaye, immaterial mark accept na ho.

**Case 3:** Ek partner directly ek entry request karta hai jo evidence support nahi karti.
*Sahi jawab:* Request record mein preserve ho, entry routine ki tarah prepare na ho, aur controller/
doosra partner ko escalate ho — invariant seniority se nahi bend hoti.

## Ek Note Baseline Par

Khala ke chaar ghante **design-against number** hain — Ayesha ki practice ka apna estimate, jo design
ke liye kaafi hai. Yeh abhi **baseline nahi hai**. Baseline sirf tab milta hai jab ek real customer
(jaise Chicago ka partner) apna khud ka number bataye. Apne worksheet mein bhi yehi farq rakho: tumhara
"main number" ka estimate tumhare apne experience se aa sakta hai, lekin uska **starting value** sirf
real customer/real workflow measure kar sakta hai.

---
[⬅ Project README](README.md)
