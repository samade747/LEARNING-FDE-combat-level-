# 01 — Part 1: Design the Work (Concepts 1-4)

## Concept 1 — Unit of Value Step Hai, Session Nahi

"Main AI use karta hoon" aur "hamari workflow AI use karti hai" alag cheezein hain. Pehli personal
habit hai — zehan mein rehti, mood se vary karti, leave par gayab ho jati. Doosri repeatable
process hai jo team chalati, jahan AI named steps karta har baar, same tareeqe se, koi bhi
keyboard par ho.

**Sirf doosri value mein grow karti. Sirf doosri ek tareeqe se galat rehti rehti hai.**

**Step** = ek named workflow piece, ek owner ke sath. Session ko baad mein judge karte ho (result
pasand aaya ya nahi). Step ke baare mein pehle se decide karte ho, aisi grounds par jo output
achha dikhe tab bhi change nahi hoti.

## Concept 2 — Requirements Extract Karo, Phir Attack Karo

Real work rarely clean brief se shuru hoti — 40-page document, half-formed emails, meeting mein
koi ne jo bola. Isay **requirements** mein badalna hai: specific, traceable, testable. AI yahan
strong hai, kisi bhi redesign ka right first use hai.

**Task definition** = business need jo 5 settled answers mein badli ho: kya produce hota, kiske
liye, kitni baar, kaunse data se, kaunse format mein. Har answer check kar sakte ho. Jo missing
ho, wo clarifying question hai jo kisi ko owe karte ho, blank nahi jo model fill kare.

"Better reporting chahiye" requirement nahi hai — koi nahi bana sakta, koi baad mein nahi bata
sakta kya met hua.

```text
From the attached RFP and the email thread, extract every distinct
requirement we are being asked to address. For each one give me a
short label, the exact section it comes from, whether our thread
already answers it, and whether it is ambiguous enough to need a
clarifying question. Return it as a table.
```

Summary nahi, structure maango — summary batati document kya kehta, structure rows deti jo doosre
log kaam kar sakein. **Source column** se woh insaan jo room mein nahi tha list check kar sakta.

Phir **attack** karo — jo requirement bid lose karati, plainly stated nahi hoti:

```text
Review the requirements you extracted. Which are ambiguous as written?
Which could two people on our team interpret differently? Which imply
a requirement the document states only indirectly?
```

Checking **output stage** se **requirements stage** mein move hoti, jahan bohot cheap hai. Unclear
requirement yahan catch hui to 1 clarifying question cost karti; work ban jane ke baad catch hui
to poora kaam cost karti.

> **Ambiguous requirement ambiguous nahi dikhti.** "Report month-end ke baad promptly deliver ho"
> requirement jaisi lagti — nahi hai. 2 din aur 2 hafte dono "prompt" hain kisi ke liye. **Test:**
> kya iske liye check likh sakte ho? Na likh sako to abhi decided nahi hai.

> **Yeh ek Project hai, one-off chat nahi.** Past winning proposals knowledge base mein; extraction
> format standing instructions mein; formatting procedure Skill mein. Yeh teeno sahi jagah rakho,
> next RFP 1 setup ki jagah 1 sentence cost karta.

## Concept 3 — Plan Numbers Jitna Hi Achha Hai

Planning work 2 cheezein mix karti jinhe AI bohot alag handle karta.

**Synthesis** = considerations gather karna, options mein shape karna. AI yeh achhe se karta —
kai factors ek saath hold karta bina thread khoye.

**Calculation alag hai** — isliye nahi ke models add nahi kar sakte (kar sakte hain), balke page
se pata nahi chalta kya actually kiya. Likha gaya figure aur calculated figure ek jaise dikhte.

**Rule consequence ke baare mein hai, ability ke baare mein nahi:**

> **Agar result matter karta, compute karo. Likho mat.**

Numbers **code execution** se produce karao, sentence mein likho mat. Code execution = assistant
code likhta aur chalata, phir jo compute hua report karta — 4th output format (inline text,
artifacts, structured data ke baad). Ek limit: run exact hai, par assistant ne code likha —
column galat pick kar sakta. **Kya compute hua check karo, sirf hua ya nahi nahi.**

```text
Using code execution on the attached ticket data, calculate quarterly
volume growth and average tickets resolved per analyst. Then, from
those figures, recommend the headcount needed to hold our current
resolution time next quarter, and show the assumptions.
```

Computation ko recommendation se separate karta, aur assumptions maangta — isse koi recommendation
se disagree kar sakta bina arithmetic dobara kiye.

**Diagnostic habit bhi hai:** numbers thodi galat aayein, usually cause prompt nahi hota — calculation
prose mein maangi gayi thi.

## Concept 4 — Kahan AI Insight Plan Change Karti Hai

Har planning step equally gain nahi karta — galat karna confidently useless plan banata.

Operations lead ne poora capacity plan 1 request mein maanga — ticket data analyze karo, growth
trend nikalo, next quarter headcount recommend karo. Well-structured answer mili, 3 analysts hire
karne ki recommendation. **Team hiring freeze mein thi**, 2 hafte pehle announce hui thi.

Data quality ka issue nahi tha — trend analysis fine thi, recommendation usi se follow hui. **Plan
useless thi kyunke ek step ko input chahiye thi jo machine reach nahi kar sakti thi: meeting mein
liya decision, dataset mein nahi.**

Synthesis steps information par chalte jo supply kar sakte ho, isliye achhe se handover hote.

**Judgment step** = jo information par chalta jo supply nahi kar sakte (ya nahi karna chahiye).
Risk appetite, hiring freeze, kya client ek aur delay accept karega. Yeh human rehte kyunke inputs
unavailable hain, judgment sacred hone ki wajah se nahi. Missing inputs wala model stop nahi karta —
gap ko "aisa decision usually kaisa dikhta" se fill karta, utni hi confidence se jitni real-computed
part ki thi.

**Window test:** kya is step ko chahiye sab kuch model ke saamne rakh sakte ho?

**Context** = model is kaam ke liye kya dekh sakta (prompt, files, conversation). **Context
window** = kitna context ek saath hold kar sakta — yeh limit hi wajah hai lambi session apni early
instructions kho deti (Concept 11 ki failure).

> **Kya is step ko chahiye sab window mein daal sakta hoon? Nahi to step mera hai.**

Jin steps ke inputs sab fit hote, unko bhi Part 2 ke 3 criteria survive karne hain.

**Research bhi synthesis step hai, window test chalao usi par:** model ka knowledge ek date tak
hai — uske baad sab window ke bahar hai, uske liye pucho to hiring-freeze jaisi failure milegi
(confident answer "aisa fact usually kaisa dikhta" se bana).

| Sawal Kiske Baare Mein | Answer Kahan Se Aani Chahiye | Kya Maango |
|---|---|---|
| Stable concept/method | Model ka apna knowledge theek hai | Explanation + reasoning |
| Current/priced/dated kuch bhi | External source jo khol sako | Answer **aur link** |

```text
For anything current, ask for a source you can open. Never a confident answer.
```
