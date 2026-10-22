# 05 — Part 5: Fix Ko Stick Banana (Concepts 13-16)

## Concept 13 — Reaction Ko Instruction Mein Badlo

Har disappointing output setup ke baare mein kuch batati hai, par zyadatar lost ho jata kyunke
fix hand se ban jati.

**Reaction** output kaisi feel hoti batata ("too generic," "not quite right," "missed the point").
**Instruction** batata kya change karna, taki next output alag ho.

**Ek sawal jump karati:** _kya present hona chahiye tha isay sahi hone ke liye, aur setup ka
kaunsa part usay control karta?_

| Reaction | Instruction | Kaunsa Lever |
|---|---|---|
| "Too generic" | Audience aur 1 action naam do jo chahiye | Prompt |
| "Wrong tone" | Tone constraint add karo har draft par | Instruction |
| "Point miss kiya" | Wo ek sawal state karo jo output answer kare, shuru mein | Prompt |
| "Purana data use kar rahi" | Knowledge base mein source document replace karo | Knowledge |

**Lever naam nahi kar sakte to critique abhi bhi reaction hai**, aur next attempt revision jaisi
dikhne wali guess hogi.

## Concept 14 — Rule, Reference, Ya Procedure

Fix dhoondna aasan hissa hai. Expensive failure: dhoond ke **kho dena**.

Monday ki session mein mila fix usi conversation mein chhoda to agle Monday phir dhoondna hoga,
aur jo koi tumhari jagah le wo bhi phir dhoondega. Har baar pehli baar jitna cost karega.

**Test chhota hai:** _yeh correction phir chahiye hogi, mujhe ya kisi doosre ko?_ Haan to
configuration mein jati. **Promotion** = fix ko chat se nikal kar configuration mein daalna, taki
lasting rahe.

Ek sawal decide karta kahan jati: fix **rule, reference, ya procedure** hai?

- **Rule** hamesha applicable limit hai → **standing instructions** mein jati (behavior change
  karti). "Target segment hamesha first line mein state karo."
- **Reference** wo material hai jo kaam ko parhna hai → **knowledge base** mein jati (kya pata hai
  change karti). Brand voice guide, current product list.
- **Procedure** steps ki sequence hai → **Skills** mein jati (kaam kaise hota change karti).
  "Weekly report is exact format mein, is order mein generate karo."

Fix ko galat ghar mein daalna hi wajah hai kuch improvements stick nahi karti. Procedure jo
1-line instruction mein paste ki jati, steps kho deti. Reference material standing instruction
mein stuffed, har prompt bloat karti, chahiye ya nahi.

**2 log, ek habit door:**

Marketer ne notice kiya har campaign brief target segment miss karti, call-to-action bury karti.
Hand-se fix karna band kiya, 2 standing instructions briefs Project mein likh diye. Har draft uske
baad correct aati, har kisi ke liye jo Project kholta.

Analyst ne pehle mahine mein seekha figures ko canceled orders exclude karni hain, har mahine chat
mein reminder type karta rehta. Kaam karta har mahine. Phir 2 hafte chhutti par gaya, colleague ne
report chalayi, canceled orders report mein reh gaye.

**Fix pehle se exist karti thi. Failure yeh thi ke kahin chhodi jahan sirf ek insaan dhoond sakta
tha.**

> **Memory jawab nahi hai yahan.** Assistant tumhari preferences pick kar sakta, par: per-user hai
> (sirf tumhara), best-effort hai (pattern pick kar sakta, ya nahi). Configuration shared ghar hai
> jo khol/parh/handover kar sakte ho.

## Concept 15 — Friction Dhoondo Optimize Karne Se Pehle

**Friction** = chhoti repeated cost jo notice karna band ho gayi. 2-minute reformat kisi ko
bother nahi karta — 50 baar saal mein karte.

| Signal | Kaisa Dikhta | Fix |
|---|---|---|
| **Repetition** | Same cheez paste/type karte har run | Saved context ya standing instruction |
| **Correction** | Same flaw har output mein fix karte | Configuration change jo flaw hatae |
| **Variance** | Alag log same task kar ke alag results dete | Shared Skill/knowledge base |

**Variance wohi hai jo teams miss karti** — koi individual isay feel nahi karta, inconsistency
sirf logon ke beech exist karti, sirf reviewer par dikhti.

Friction dikh nahi rahi to workflow ek baar chalao har manual step likhne ke job ke sath — wo
list backlog hai.

2 moves friction hatate: **Consolidate** (steps saath chalana, teen prompts ki jagah jinme tum
beech mein background re-explain karte) aur **Promote** (repeated pattern configuration mein
move karna, Concept 14 se). **Consolidation pehle, promotion baad mein** — jo step merge hone wala
hai usay promote karna fazool kaam hai.

**Worked audit:** weekly reporting workflow ~45 min/analyst leti, outputs alag. Audit 3 frictions
dhoondti: har analyst same background re-paste karta, output hand se reformat karta, alag issues
catch karta. Concept 14 test se sort: background reference hai → knowledge base; format procedure
hai → Skill; checking step rule hai → standing instruction. **Result: ~25 min/analyst, consistent
format, 1 kam revision round.**

## Concept 16 — Jo Actually Matter Karta Usay Measure Karo

Improvement jo measure nahi kar sakte, justify karna hard hai, rakhna harder.

**Before measure karo.** Audit "45 se 25" claim karti sirf kyunke kisi ne workflow **change karne
se pehle** time ki. **Baseline** = wo measurement. Bina usi "improvement jo believe karte, state
nahi kar sakte" ho jata — koi improvement jitna same jab manager puche.

1 cycle cost karta: workflow ek baar unchanged chalao, 3 numbers record karo (kitna time laga,
kitne revision rounds, kitne manual steps). **Baad mein baseline rebuild nahi kar sakte** — purani
tareeqe ka estimate tumhe flatter karega.

Time-saved sabse aasan metric hai, aksar sahi nahi:

| Workflow Agar Hai | Optimize Kiske Liye | Kyun |
|---|---|---|
| Internal draft | Time | Speed point hai, chhoti galtiyan cheap hain |
| Customer-facing report | Consistency | Varying formats trust tez erode karte delay se |
| Compliance/finance output | Accuracy | Ek galat figure hour bachane se zyada cost karti |
| Multiple log ka kaam | Variance | Cost logon ke beech rehta, ek insaan ke andar nahi |

Metric naam dena yeh bhi batata **kab rukna hai** — metric achhi ho jaye, aur tuning apni khud ki
friction ban jati.

**Parallel run** = purana+naya workflow saath chalana — 2-3 rounds real duplicated effort cost
karta, par evidence khareedta naya tareeqa better hai, working fallback agar nahi, aur jinka kaam
change hua unki agreement. **Yeh last cheez sabse matter karti** — parallel run "hum tumhara job
change kar rahe" ko "humne dono chalaye, yeh hua" mein badalta.

**Cost ka jawab de sako.** Redesign budget review survive karta cost-vs-saving par. Cost = tool ko
jo pay karte + human time jo abhi bhi hai (jo gates rakhe). Saving = baseline × kitni baar chalti
× kitne log chalate. "20 min/week across 3 analysts ~50 hours/year" manager act kar sakta aise
sentence par. Phir risk naam do jo gates survive karta — business case jo ek hide karti, believed
hona band ho jati.
