# 03 — Gate 3: What Does "Finished" Look Like?

> **Rokti hai galti:** "Agent ne bara acha kaam kiya. Bas woh wahi kaam nahi tha jo mujhe chahiye tha —
> aur mujhe yeh pata tab chala jab kaam ho chuka tha."

Aap decide kar chuke ke yeh agent job hai (Gate 1) aur aap ise ek dafa solve karenge (Gate 2). Aakhri
gate, agent kholne se pehle: **finished** ka matlab likh do, teen chhoti lines mein.

1. **Kis se kaam kare (input).** Agent ko exactly kya dekhna chahiye — kaunsa folder, kaunsi files,
   kaunse messages. Specific raho. "Mere emails" bohat vague hai. "Support folder ke 400 messages,
   pichle 7 din ke" clear hai.
2. **Akhir mein kya chahiye (output).** Woh cheez jo finished hone par exist karni chahiye — ek
   spreadsheet, ek one-page summary, ek folder renamed files ka. **Shape** batao, sirf topic nahi.
3. **Woh check jo bataye ke done hai (done-check).** Ek cheez jise dekh kar pata chale kaam finished
   aur correct hai. Jaise: "har message exactly ek group mein hai, aur group counts jodkar 400 ban
   jaye." Jab yeh sach ho, aap done hain. Jab nahi, aap done nahi hain.

Bas itna hi — teen lines. Aap poori instructions nahi likh rahe, aur na hi agent ko batate ho *kaise*
karna hai. Aap sirf **target** decide kar rahe ho, taake jab agent usay hit kare, aapko pata chal jaye.

> **Yeh prompt likhne jaisa nahi hai:** Gate 3 sirf *target* decide karta hai — finished ka matlab kya
> hai. Asal instructions jo aap agent ko kaam karte waqt dete ho (kaise phrase karna, tables mangna,
> result check karna), agle course [Problem Solving with General Agents] mein sikhaya jata hai. Gate 3
> **target choose karna** hai. Agla course **usay hit karna** sikhata hai.

## Work Example — Ana

Wapis Ana ke paas, uske 400 customer messages ke sath. (Uske task ka Mode 2 future hai, lekin jab tak
worker nahi banta, woh har hafte ise ek dafa solve karti rehti hai — isiliye Gate 3 har run par
lagta hai.) Agent kholne se pehle woh teen lines likhti hai:

> **Works from:** Support folder ke 400 messages, pichle 7 din ke.
>
> **Chahiye akhir mein:** Ek spreadsheet, ek row per message — columns: sender, date, group (complaint/
> question/order/other), one-line summary. Plus ek one-page note jisme har group ka count aur top 3
> common complaints hon.
>
> **Done jab:** Har message exactly ek group mein hai, group counts jodkar 400 banti hain, aur note ke
> numbers spreadsheet se match karte hain.

Ab woh agent kholti hai. Jab result wapis ata hai, uske paas exact tareeqa hai check karne ka ke waqai
finished hai — aur done-check ("counts 400 tak jodna") kuch second mein confirm ho sakta hai. Yusuf, jo
"help me with these messages" leke gaya tha, uske paas yeh kuch nahi tha. Isiliye uska result kuch aisa
tha jise woh trust nahi kar sakta tha, aur check bhi nahi kar sakta tha.

## Sharpest Test: Done-Check

Apna most recent real task lo jo aap ne agent ko diya (ya jo dene wale ho). Teen lines likho: works
from, want at end, done when. Phir done-check ko gaur se dekho: **kya aap ise waqai check kar sakte
ho?** Kya aap, ya agent, ise ek minute se kam mein confirm kar sakte ho? Agar done-check vague hai
jaise "summary acha hai" — yeh abhi real check nahi hai. Isay sharp karo jab tak yeh testable na ban
jaye.

---
[⬅ Gate 2](02-gate-2-once-or-every-week.md) · [⬆ Index](README.md) · [Agla: Worked Example + Reference Card ➡](04-worked-example-reference-card.md)
