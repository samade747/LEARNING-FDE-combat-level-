# 03 — Do Content Classes: Authority Vs Orientation

## Ek Rule Jis Par Yeh SoR Chalti Hai

**One source, two readers.** Agents cite karte hain. Insaan ise kitab ki tarah parhte hain. Ek reader ke
liye design karo, doosre mein fail ho jaoge. Sirf circulars/thresholds ka corpus Worker ke liye theek hai
lekin junior professional ke liye unreadable. Sirf textbook chapters ka corpus reader ke liye friendly
hai lekin Worker ke liye useless noise. Jawab reader choose karna nahi — ek governed home mein **do content
classes** rakhna hai, aur unhe alag treat karna hai.

### Class One — Authority (Citable)

Teen tests mein se **kam se kam ek** pass karna zaroori hai:
1. **Citation test** — kya Worker isay kabhi reviewer ko cite karega?
2. **Change test** — kya yeh agle saal ya agli jurisdiction mein alag ho sakta hai? (tax rates, standards)
3. **Dispute test** — kya do professionals (ya khud model) disagree kar sakte hain, isliye authority ko
   settle karna zaroori hai? (classification judgments)

Authority content ko poora treatment milta hai: register row, rights basis, owner, version, hierarchy
mein jagah. **Yehi Worker cite karta hai.** Ek aur label: authority ki **kind** — law, professional
standard, signed contract, internal policy, expert methodology, judgment guidance, graded example — sab
citable ho sakte hain, lekin equally strong nahi. Worker kabhi graded example ko law jaisa cite nahi
karta.

### Class Two — Orientation (Explaining)

Teenon tests fail karti hai, phir bhi belong karti hai — doosre reader ki zaroorat hai. Iska apna test:
**kya ek professional reader iske bina lost ho jayega?** Teen treatment rules: (1) **short** rakho — sirf
authority samajhne layak, poora course nahi; (2) **context ki tarah mark karo** — Worker isay kabhi
conclusion ke basis ki tarah cite nahi karta, parhna allowed hai, citing nahi; (3) **halka governance** —
stable content jo badal nahi sakta, sabse sasti governance.

**Kaise mark karo?** Book khud "In plain words" tip/info boxes use karta hai — reader ke liye friendly
signal ("yahan se shuru karo"), aur ingestion pipeline ke liye machine-readable boundary (ek simple rule
har admonition block ko citable authority se exclude karta hai). Lekin formatting poora control nahi hai
— writer galti kar sakta hai, real threshold tip box ke andar ja sakta hai. Isliye 3 validation rules bhi
chalti hain: binding rule/number sirf orientation ke andar nahi reh sakta; har authority block ko apna
stable ID + source chahiye; build fail hoti hai jab page yeh rules break kare.

## Ek Page, Do Baar Parha

**Accounting: "Journal Entries" page.** Part 1 (orientation, top): "journal entry ek business event
record karti hai, dono sides equal honi chahiye — double-entry bookkeeping." Part 2 (authority, middle):
"$500,000 se upar har entry controller approval chahti hai (Firm Policy 4.2)..." Part 3 (checker):
automated test jo reject kare agar debits = credits na ho.

**Junior accountant** Part 1 pehle parhti hai (uske bina Part 2 wall of rules hai). **Worker** Part 2 use
karta hai, "Firm Policy 4.2" cite karta hai jab entry route karta hai — Part 1 background ki tarah parh
sakta hai, lekin **kabhi cite nahi karta**.

**Sales: "Deal Stages" page** — same 3-part pattern (orientation: "stage sirf feeling nahi, claim hai jo
evidence maangti hai"; authority: FISTA Playbook citations; checker: evidence-field block).

**Galat banaya jaye to dono directions mein fail hoti hai:** Part 1 delete karo → page authority-only ban
jata hai, naya rep policy numbers ke sath akela reh jata hai, dusre colleague se poochta hai. Part 1 ko
poore chapter mein expand kar do, kuch mark na karo → retrieval Worker ko chapter deti hai rule ki jagah,
Worker ek din likhta hai "deal advance hui, jaisa hamari guide kehti hai momentum matter karta hai" —
reviewer sahi tareeqe se reject karta hai, guide ki opinion evidence nahi hoti.

## Teen Bars, Ek Page

Simple language ek taraf beh ti hai: jo text ek beginner parh sakta hai, expert usay faster parhta hai,
aur **agent usay zyada reliably parse karta hai** (simple sentences kam ambiguities le kar chalti hain).
Lekin simple bars mein sirf pehla hai:

1. **Simple** — beginner ke liye readable
2. **Exact** — yeh Worker ka bar hai. "Big entries need extra approval" samajh mein aata hai, useless
   hai. "Entries above $500,000 (Firm Policy 4.2, version 2026-03)" — yeh sentence abhi bhi simple hai,
   lekin exact bhi hai. Simple words aur exact content opposite nahi hain.
3. **Structured** — koi human reader ko iski zaroorat nahi, stable IDs, version metadata, authority-or-
   orientation marking, retrieval-shaped sections — reader ke liye invisible, Worker ke liye essential.

**"Beginner" ka matlab:** **day-one junior professional** — jo yeh profession chun chuka hai lekin is firm
aur inke rules mein naya hai. True beginner ke liye likho (jo journal entry hi nahi jaanta) to curriculum
wapas corpus mein khich aayega — woh reader **twin** ka hai.

## Whole Design Target, Ek Instruction Mein

**System of Record ko best handbook ki tarah likho jo apne day-one junior ko doge. Phir machine layer add
karo jo agents ko cite/check/build karne de.** Junior target khud dono classes produce karta hai: woh nayi
hai, isliye good handbook state karne se pehle explain karti hai (= orientation); woh din-1 se real files
par kaam karti hai, isliye handbook rates + citations ke sath rules deti hai (= authority). Commercial
reason bhi hai: is SoR ka pehla stranger reader zyada tar buyer hoga.

**Kuch content bahar hi rehta hai:** pure vocabulary jo reader ke paas already hai, folklore jo na
authority hai na explanation, poore lessons jo full course duplicate karte hain. Costs: retrieval noise,
review burden, aur **paraphrased authority** (agar corpus standard ko apne shabdon mein re-explain kare
aur kuch mark na kare, paraphrase citable ban jata hai — aur agar drift ho jaye, tumhari stamp ke sath
drift hoti hai).

---
[⬅ 02 — Three-Bin Sort](02-three-bin-sort-and-hierarchy.md) · [Agla: 04 — Decisions, Rules, Exceptions ➡](04-decisions-rules-exceptions-reflexes.md) · [⬆ Index](README.md)
