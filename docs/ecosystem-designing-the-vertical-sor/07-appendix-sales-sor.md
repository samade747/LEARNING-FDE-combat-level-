# 07 — Appendix A: Sales System Of Record, End To End

Do worked examples yeh page band karte hain, aur har ek first-principles loop ka full-scale run hai:
current reality capture hui, sachaiyan Bin 1 mein sort hui, kaam un ke around rebuild hua, aur result
purani duniya ke numbers ke against proof hua. In dono ko contrast ke liye chuna gaya hai. **Sales**
(yahan enterprise B2B software sales, lightly-regulated setting mein) **trust-governed** hai — hierarchy
shallow aur policy-driven hai, Worker zyada autonomy kamata hai. **General ledger accounting**
**law-governed** hai — hierarchy deep hai, Worker preparation boundary ke peeche rehta hai. Dono parho aur
tumne method ke dono extremes dekh liye.

**Ek boundary pehle**, kyunke sales ke paas ek famous existing system hai: **CRM Sales System of Record
nahi hai.** CRM woh hi rehta hai jo hai — accounts, contacts, aur opportunities ki database. System of
Record woh cheez govern karta hai jo CRM ne kabhi nahi hold ki: Worker ko jo CRM mein hai usay kaise
samajhna aur uspar amal karna chahiye. Qualification evidence kya count hoti hai. Kaunse claims buyer tak
pahonch sakte hain. Stage kab advance ho sakti hai. Sirf insaan kya decide kar sakta hai. **CRM deals hold
karta hai. System of Record profession hold karta hai.**

## Sales Outcome

**Weak outcome:** *follow-ups automate karo.* **Derived outcome:** har open opportunity ke liye ek
complete, evidence-backed deal file maintain karo — buyer aur problem identified, budget aur decision
process evidenced, buyer ko diya har commitment documented, next step scheduled, aur file mein har claim
ek identified source record tak traceable.

Outcome contract, filled in. **Trigger:** naya opportunity pipeline mein aata hai, ya buyer interaction
hoti hai. **Main number:** active opportunities ka woh share jinki deal file ek material buyer interaction
ke ek ghante ke andar evidence-complete hai (expert ka apna floor: files call ke 2-3 din baad complete
hoti hain, aur aksar kabhi nahi; har customer ka apna starting value usi customer par measure hota hai).
**Guardrails** — aur yahan sales ko ek special guardrail chahiye: reply quality complaints na barhein,
forecast accuracy na girey, aur false-qualification rate na barhe. Sales Worker ko **kabhi pipeline
inflation ke liye reward nahi milna chahiye**. Zyada opportunities, zyada stage advances, zyada activity —
yeh sab numbers Worker ek dollar bhi value banaye bina produce kar sakta hai. Guardrails isliye hain taake
speed sach ki khidmat kare.

**Forbidden actions:** Worker kabhi pricing nahi bhejta, kabhi terms negotiate nahi karta, kabhi naye
prospect ko approved sequence ke bahar contact nahi karta. **Final authority:** account executive har deal
decision ka owner hai. **Record:** complete deal file, apni evidence ke sath.

## Sales Archaeology

Purana workflow, ek real sales floor se. Rep account ko haath se research karta hai. Rep discovery call
chalata hai, phir partial notes baad mein CRM mein likhta hai — ya kabhi nahi. Follow-up tab draft hota
hai jab waqt ho. Deal data forecast spreadsheet mein dobara type hoti hai. Pipeline weekly review meeting
mein defend hoti hai. Unwritten layer, top performers se: woh har call se pehle buyer ke authority signals
aur competitor presence check karte hain. Woh chupke se CRM data entry skip karte hain kyunke woh selling
time churati hai. Activity report banti hai aur kabhi parhi nahi jaati. Forecast override spreadsheet
chupke se asal system ban chuka hai. Archaeology is domain ki well-known bad habit bhi dhoondti hai:
seller ke optimism par stages advance hoti hain, aur activity volume buying evidence ki jagah le leta hai.
Dono sort mein Bin 2 mechanisms ki tarah jaate hain — inka honest purpose, evidence-based stage discipline,
invariant ban jata hai.

## Sales Sort

| Purana Element | Bin | Faisla Aur Wajah |
| --- | --- | --- |
| Har call CRM mein haath se log karna | 2 | Redesign. Purpose (complete record) invariant banta hai; mechanism automatic ban jata hai — Worker transcript attach karta hai aur facts extract karta hai. |
| Weekly pipeline review meeting | 2 | Redesign. Continuous deal-health monitoring exception alerts ke sath; sirf judgment deals ke liye chhoti meeting survive karti hai. |
| Deal data forecast spreadsheet mein dobara type karna | 3 | Delete. Forecast live deal state parhta hai. |
| Manager limit se upar discounts approve karta hai | 1 | Keep. Company ki policy-named commercial control. Worker margin analysis prepare karta hai; manager decide karta hai. |
| Written scope ke bina buyer ko koi commitment nahi | 1 | Keep. Yehi trust hai jo vertical becha jata hai. |
| Qualification checklist (budget, authority, need, timeline) | 2, purpose 1 mein | Qualification discipline invariant hai; manual checklist automated evidence-gathering ban jati hai, gaps flagged. |
| Ek din ke andar follow-up email | 2 | Redesign. Transcript se ek ghante ke andar draft, rep dekhta hai jab call abhi fresh hai. |

## Sales Invariants

Deal file ko chaar cheezein alag rakhni chahiye: customer ne kya kaha, seller ne kya infer kiya, research
kya suggest karti hai, aur kya abhi bhi unknown hai. **Assumption ko confirmed fact ki tarah likhna sales
ka invented-citation version hai.** Deal file ka har important field chhe evidence states mein se ek
rakhta hai: confirmed, indicated, inferred, unknown, contradicted, ya outdated — isse koi CRM field apni
evidence se zyada certain nahi lagta.

Deal file ka har material claim ek identified source record tak traceable hona chahiye. Koi price/discount
approved limit se upar named human approval ke bina move nahi hota. Koi commitment buyer tak human-approved
scope ke bina nahi pohanchta. Forecast category apne evidence rules satisfy kare — **hope ek stage nahi
hai.** Buyer-facing messages applicable AI-disclosure law follow karte hain (Worker hamesha disclose karta
hai ke woh AI hai). Unqualified deal unqualified marked rehta hai — missing evidence kabhi qualification
nahi maani jati.

## Sales Hierarchy, Decisions, Aur Permissions

Hierarchy shallow hai kyunke sales ke paas profession-specific regulator nahi hai:

1. Outreach aur privacy law (GDPR, CAN-SPAM, tumhare apne country ke equivalents)
2. Channel policies
3. Company ki binding commercial policy (pricing/discount authority)
4. Sales methodology — is vertical ke liye FISTA Sales Book, expert-authored corpus, jo kisi aur ke paas
   nahi
5. Playbooks, templates, graded examples — properly aur falsely qualified opportunities side-by-side,
   kyunke judgment contrast se sikhaya jata hai
6. Har customer ke rules of engagement, customer layer par
7. Historical win-loss examples

Permissions Appendix B ke contrast dikhati hain. Yeh Worker CRM, email, transcripts parh sakta hai. Kuch
bhi draft kar sakta hai. Aur **routine scheduling/follow-up messages khud bhej sakta hai** — low-risk hain,
correct ho sakte hain, disclosure invariant qaim rehta hai. Woh kabhi pricing nahi bhejta, kabhi negotiate
nahi karta, kabhi naya prospect sequence approval ke bina start nahi karta. **Autonomy kabhi domain ki
property nahi hoti — hamesha customer ka decision hoti hai.** Boundary invariants se khinchti hai, fear se
nahi.

## Ek Sales Exception, Ek Reflex

Exception: mid-conversation, buyer limit se zyada discount maangta hai. Worker chup nahi hota, aur maan
bhi nahi leta. Woh full-price par ek holding reply draft karta hai, aur escalate karta hai: *buyer ne
18% maanga hai; approved authority 12% hai; deal file full-price par budget evidence dikhati hai; ek
competitor doosri call mein mention hua tha; margin analysis attached; recommendation: price hold karo,
annual-payment structure offer karo; Thursday ki call se pehle decision chahiye.*

Deal-execution reflex, ek saans mein: har buyer interaction par, record attach karo, file update karo,
qualification evidence test karo, gaps flag karo, follow-up draft karo, routine ho to bhejo warna route
karo, deal health refresh karo, aur jo bhi price/scope/stalled-invariant chhue usay escalate karo.

**Evaluation set ka ek case family jo routine tests miss karte hain:** andar se pressure — seller Worker
se poochta hai stage bina evidence advance kare, urgency invent kare, objection chhupaye, ya deal
qualified mark kare taake forecast acha lage. In sab cases mein passing answer hai **refusal, evidence
stated ke sath**.

---
[⬅ 06 — Templates](06-templates.md) · [Agla: 08 — Appendix B: General Ledger SoR ➡](08-appendix-ledger-sor.md) · [⬆ Index](README.md)
