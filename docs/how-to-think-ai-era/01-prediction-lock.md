# 01 — Discipline 1: The Prediction Lock

**Prediction Lock** = tumhari apni written position, AI ke answer se pehle committed. Yehi poora
goal hai — 4 lines sirf method hain.

Lock ke bina: AI se important sawal poochte, confident answer aata, "sounds right" soch kar chal
dete. 2 din baad koi pucche "kyun decide kiya?" — pata chalta wo AI ka answer tha, tumhara nahi.

## 4 Lines (3 Minute Ka Fix)

**Line 1 — Yeh decision asal mein kiske baare mein hai?** Surface label nahi — real question.
("Debate ya coding" nahi, "friends follow karoon ya apna pick karoon" hai.)

**Line 2 — WOH EK fact jo sabse zyada help karegi?** Vague nahi ("kaunsa better hai") — specific,
checkable ("kya bootcamp Python sikhata, jo school already 9th grade mein sikhata hai?").

**Line 3 — AI se pehle tumhara decision kya hai?** Position lo — "it depends" nahi. Debate ya
coding, aur kyun. _(Maya: debate — 2 hafte friends ke sath, kuch naya seekhna, ek hafte ka repeat
se behtar.)_

**Line 4 — Kitne confident ho, aur kaunsa specific AI answer flip karega?** Percentage (60%,
75%) — exact number matter nahi karta, commitment karta hai. Phir exact AI answer likho jo
mind change karega. _(Maya: 70% sure. Bootcamp Rust/embedded sikhaye to coding wins.)_

## Kyun 4 Lines, 1 Nahi?

Har line ek failure catch karti jo doosri nahi kar sakti:

- **Line 1 skip karo**, galat sawal ka jawab milta (surface label hamesha real question chhupata)
- **Line 2 skip karo**, prompt collapse hota — "kaunsa better" AI ko decision maker bana deta
- **Line 3 skip karo**, AI ke answer ko compare karne ke liye kuch nahi bachta
- **Line 4 skip karo**, hope hai, commitment nahi — kabhi pata nahi chalega commit kiya ya AI ke
  pehle hint par drop kar dete

## Lock Kaam Kiya Ya Nahi — Ek Test

**Kya tum loud bol sakte ho tumhara position AI kholne se pehle kya tha, aur kya flip karta?**
Haan — lock kaam kiya. "Well, AI ne X bola to X se chal diya" — nahi kiya. **Line count matter
nahi karta.**

## Prompt Mein Kya Jaye

**Sirf Lines 1+2 prompt mein jaate hain.** Line 3 (decision) aur Line 4 (reversal) AI se chhipao —
AI ko pata chale tumne kya commit kiya, wo agree karega, comparison kho jati.

```text
I'm trying to decide [1-2 sentence situation].
My question is: [Line 2 question].
Just answer that one question. Don't make the decision for me.
```

**Answer aane ke baad compare karo Line 4 se:**

- AI ka answer Line 4 nahi hai → decision stays, jo reason likha tha usi par
- AI ka answer exactly Line 4 hai → decision change hoti, jo pehle se set tha usi reason se
- Beechon beech hai → Line 3 ki reasoning weaken hoti? Haan to change karo aur likho kyun

**AI hedge kare** ("it depends") → _"Just give me the specific information. Don't qualify it."_
Phir bhi fail ho → Line 2 bohot broad hai, specific banao.

**Lock revise karna:** AI ka answer dekhne se **pehle** Line 4 revise karna theek hai (naya kuch
notice kiya). Dekhne ke **baad**, sirf us answer ko flip na maanne ke liye revise karna — lock
defeat karta. Test: kya tum AI ka answer dekhe bina yeh naya Line 4 likhte? Haan → revise karo.
Nahi → purana Line 4 stands.

## Bigger Decision: Bank Manager Example

Branch close karne ka decision. Line 1: real question — kya kaafi customers abhi bhi walk-in karte
branches khule rakhne justify karne ke liye? Line 2: kitna % customers app-only hain? Line 3: close
karo — maine socha most customers app-only ho gaye. Line 4: 60% sure — agar 50% se kam app-only
hon, open rakho.

Data anonymize kiya (names/account numbers hatae), AI se % pucha — **45% aaya**, jo 50% se kam
tha, **Line 4 flipped**. Close karna sahi call nahi raha. **Gap** (expected most, mila sirf 45%)
bani uski report ki opening line, aur ek middle-path (reduced hours) surface hui jo lock ke bina
kabhi nahi hoti.

## Research Ke Peeche (3 Decades, 1 Habit)

- **Premortem (Gary Klein, 2007):** project shuru hone se pehle team imagine karti project fail
  ho gaya, sab reasons likhti. "Prospective hindsight" future outcomes ki correct reasons
  identify karne ki ability 30% barha deta.
- **Forecasting calibration (Tetlock, 2011-2015):** superforecasters predictions confidence % ke
  sath **pehle** likhte, baad mein outcome se compare karte. Written prediction ke bina pata
  nahi chalta guess kitna close tha.
- **Anchoring (Tversky & Kahneman, 1974):** confident answer jo tumhari apni jagah le le, reference
  point ban jata — tum pata nahi laga sakte bina uske kya sochte. AI ke answers default confident
  hain — lock anchor banne se rokta, apna pehle rakh ke.

**Teeno saath:** decision+flip-condition pehle likho, confidence record karo calibration check
karne ke liye, dono AI ka answer parhne se pehle karo.
