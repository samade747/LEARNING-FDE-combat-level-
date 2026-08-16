# 01 — Gate 1: Does This Need an Agent At All?

> **Rokti hai galti:** "Maine 20 minute lagaye agent se woh kaam karwane mein jo spreadsheet ek step
> mein karti hai — ya maine poora agent khol diya sirf ek sawal ka jawab lene ke liye jo chatbot 5
> second mein deta hai."

Gate 1 ke do chote checks hain, order mein.

## Check 1a — Kya isko AI chahiye, ya regular tool jo pehle se paas hai?

Agents **fuzzy** kaam mein acche hain: jahan judgment chahiye, mukhtalif tarah ki files mix hoti hain,
aur koi normal app us kaam ke liye banaya hi nahi gaya. Woh **best choice nahi** hain us kaam ke liye
jo koi regular tool pehle se perfectly karta hai.

**Simple test:** Agar aap task ko ek exact step mein describe kar sakte hain jo har baar same ho, to
regular tool zyada tez aur reliable hoga:

- "Numbers ka column add karo." → Yeh **spreadsheet** hai. AI nahi.
- "Contacts mein 'Khan' naam wale sab dhundo." → Yeh contacts app ka **search box** hai. AI nahi.
- "Document mein har '2024' ko '2025' se badlo." → Yeh **find-and-replace** hai.

Jaise hi kaam ko *judgment* chahiye ("messages ko topic se sort karo" — yahan decide karna hai "topic"
ka matlab kya hai), ya *mukhtalif tarah ki files* mix hoti hain jinko koi single app khol nahi sakta
(photos **aur** PDFs **aur** screenshots), ya bas **koi app hai hi nahi** jo yeh karti ho — to aap
Check 1a paar kar chuke. Yeh AI job hai.

## Check 1b — Kya isko agent chahiye, ya sirf chatbot?

Yeh woh check hai jo log sabse zyada skip karte hain. Yaad rahe: **chatbot jawab deta hai, agent kaam
karta hai.**

Poochho: *kya iske liye tool ko meri asli cheezon ko chhoona parega?*

- "Debit aur credit mein farq batao." → Sirf **jawab** chahiye. Kuch bhi aapka nahi chhuta. Yeh
  **chatbot** job hai.
- "Mere 400 customer messages mein se guzro aur har ek ko group mein dalo." → Tool ko aapki **asli
  files par act** karna hoga. Yeh **agent** job hai.

Poora farq hai **jawab vs action.** Agar sirf kuch jaanna hai, ya draft/ideas chahiye — woh jawab wala
kaam hai, chatbot. Agar tool ko files kholni hain, badalni hain, kuch chalana hai, ya doosri app use
karni hai — woh action wala kaam hai, agent.

### Rozmarra Ki Example

Cooking sochein. "Anda kitni der ubaalu?" — yeh **jawab** hai, aap poochte ho, number milta hai, khatam.
Chatbot. Lekin "fridge mein dekho kya hai, aur 3 dinner ka shopping list banao" — yahan kai cheezein
*actually karni* parti hain. Yeh agent ka kaam hai. Aur "grocery receipt ke prices jodo" — yeh dono
mein se koi nahi, yeh sirf calculator hai.

## Work Example — Mei

Mei ek chhoti company ka office chalati hai. Ek subah 4 kaam aate hain, woh har ek ko Gate 1 se
guzarti hai:

- *"Yeh expense list ka total kya hai?"* → Spreadsheet add kar deti hai. **AI bhi nahi. 1a pe ruk gaya.**
- *"Purchase order kya hota hai, samjhao."* → Sirf jawab chahiye; kuch bhi uska nahi chhuta.
  **Chatbot. 1b pe ruk gaya.**
- *"Bills ke folder mein dekho, kaunse mein signature missing hai."* → Judgment chahiye (har ek parhna)
  aur uski files par act karta hai. **Agent. Gate 1 paar.**
- *"Bank ki payment list ko apni list se compare karo, bolo kya match nahi hota."* → Do alag files,
  judgment, uske data par act. **Agent. Gate 1 paar.**

Mei ke 4 mein se 2 "AI tasks" agent tasks the hi nahi. Yeh normal aur acha hai. Gate 1 kaam ko agent
ki *taraf* nahi dhakelta — yeh us kaam ko rokta hai jo wahan belong hi nahi karta.

---
[⬅ Overview](00-overview.md) · [⬆ Index](README.md) · [Agla: Gate 2 ➡](02-gate-2-once-or-every-week.md)
