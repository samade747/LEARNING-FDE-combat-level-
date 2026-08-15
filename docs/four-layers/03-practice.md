# 03 — Practice: Layer Ka Naam Do

**8 failures.** Har ek ke liye, pehle kaunsi layer dekhoge aur kya ek change karoge, likh lo jawab
dekhne se pehle.

---

**1.** Competitor summary table format mein manga (5 columns), 3 excellent paragraphs mile. Content
accurate hai.
> **Jawab: Prompt.** Model ne task samjha, kaam sahi kiya. Sirf shape galat hai. Fix: table ka example
> do, lambi explanation nahi. **Is layer ka sab se saaf signature: sahi kaam, galat container.**

**2.** Agent confidently kehta hai pricing tier 5,000 requests pe cap hai. Aapki pricing page 50,000
kehti hai. Agent ne page parha tha.
> **Jawab: Context.** Confident + fluent + galat ek document ke baare mein jo window mein thi — almost
> ek signature. Kuch compress/truncate/replace hua. Curator test chalao.

**3.** Overnight run report karti hai *"all tests passing, changes committed."* Subah test suite kabhi
chali hi nahi, build red hai.
> **Jawab: Diagnosis harness ke liye, fix loop ke liye.** Concept 6 exactly. Hook do jo suite chalaye
> aur bina chalaye beat khatam na hone de — **lekin** ye sirf prove karta hai suite chali, run ne khud
> decide kiya suite hi sahi bar thi. Trustworthy version: **outside stop** — pehle se chuna success
> condition.

**4.** Run poora budget ek dopahar mein kharch kar deti hai. Log dikhata hai wahi 3 approaches baar
baar, thora alag lafzon mein.
> **Jawab: Loop.** No-progress check nahi, aur shayad spending limit bhi nahi. Yehi is course ka opening
> story hai. Prompt attractive jagah hai dekhne ki, aur wahan bhi poori dopahar waste hogi.

**5.** Invoice-matching agent 300 invoices process karta hai, 300 matched report karta hai. Hand-check
mein pata chalta hai kuch jagah 2 payments equally plausible thin, agent ne chup chaap ek chun liya.
> **Jawab: Loop, specifically missing gate.** Kuch bhi malfunction nahi hua. Agent ek genuinely
> ambiguous decision se mila, sirf 2 options thay: guess ya fail. Usne guess ki, aur guess bilkul 290
> sahi jawabon jaisi lagti hai.

**6.** Subagent ko 40 support tickets parhne bheja. Clean 3-paragraph summary mila. 2 claims galat
nikalti hain.
> **Jawab: Harness.** Subagent tool call se ata hai lekin poori nested stack chalata hai, isliye summary
> **poore confidence** ke sath ata hai chahe usne kitna bhi galat parha ho. Fix: quotes, ticket IDs,
> receipts jo aap check kar sako, sirf conclusions nahi.

**7.** Lambi session 20 turns tak achi chalti hai. Phir agent ek decision se contradict karna shuru kar
deta hai jispe aap dono agree hue thay, jaise kabhi hua hi na ho.
> **Jawab: Context.** Window bhar gayi aur kuch nikal gaya. Dropping policy harness ne set ki, aap ne
> nahi. Fix: decision ko conversation se bahar durable banao — rules file, spec, ya dobara attach hoti
> note mein.

**8.** Sab 4 layers clear ki hain ek hard research task pe — precise prompt, sahi window, verified
harness, loop sahi tarah rukti/check karti hai. Output abhi bhi mediocre hai.
> **Jawab: In mein se koi nahi.** Yehi Concept 12 ke liye hai. Layers batate hain kahan toot sakta hai.
> Capability nahi banate. Honest agle moves: stronger model, chhota/sharper task, alag approach.

## Apni Khud Ki Failure Pe Try Karo

Pichli dafa jab agent ne kuch galat/mehnga banaya, ye sawal order mein answer karo:
1. **Kaunsa unit of work galat hua?** Ek model call, window, ek beat, ya poori run?
2. **Baad mein maine kya badla?** Kya wahi layer thi?
3. **Kya usay pakar leta?** Mechanism, layer, aur kisne criterion chuna, naam do.

**Example:** Legal ops team agent se poochti hai har supplier contract dhoondo jo auto-renew hota hai.
Report: 40 contracts review hue, 3 renewals. 2 mahine baad, 3 aur contracts renew hote hain — unhon ne
*"evergreen term"* lafz use kiya tha.

**Team ne kya badla?** Prompt mein aur phrases add kiye. **Ye layer 1 badla jab failure layer 4 pe
thi.**

**Kya pakarta?** Legal lead ka pehle-se-chuna success condition: har contract mein quoted renewal clause
+ page number wapas ana chahiye, ya **"no renewal clause found"** insaan ko jaye. Command check kar
sakti hai 40 contracts ne 40 complete results diye bina blanks ke.

> **Asal skill sahi layer turant naam karna nahi hai. Tempting answer ko test karna hai, aur sab se
> aasan-to-edit layer pe rukne se inkar karna hai.**

---

## Poori Section Ka Nichod

> **"A good prompt fails inside bad context. Good context fails inside a bare harness. A good harness
> sits idle without a loop. So when something breaks, name the layer before you reach for a fix."**

**Ye is poore chapter ka wahi ek sentence hai jo yaad rakhne layak hai.** Demo mein kaam karne wala
agent production mein isi liye fail karta hai — demo ko sirf inner layers chahiye thin. Outer kabhi bani
hi nahi. Model problem nahi thi. **Uske ird gird ki layers missing thin.**

---
[⬅ Using the Map](02-using-the-map.md) · [⬆ Index](README.md)
