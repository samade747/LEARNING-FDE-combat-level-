# 03 — Part 2: Description (Concept 4)

Shuru ki colleague ki kahani yaad karo — uski outline galat thi kyunke tumne important info chhod
di. AI ke sath yeh problem aur zyada hai: **sirf available info se kaam karta hai** — agar kuch
important chhod do, wo guess karega, aur reasonable guess bhi galat ho sakta.

**Description** = AI ko wo information aur guidance dena jo kaam achhe se karne ke liye chahiye.
Yeh "good prompt likhna" se bohot bara hai — full size par yeh **context engineering** ban jata
hai (saari info design karna jo AI ko chahiye, sirf ek message ki wording nahi).

Teen hisse:

1. **Product description** — kya chahiye
2. **Process description** — kaam kaise approach kiya jaye
3. **Performance description** — AI kaise behave kare (tumhare sath, aur apne aap)

**Memory aid: What → How → How to work with me**

## 4.1 Product Description

Sawal: "mujhe wapas kya chahiye?" Include karo: output type, audience, format, length, tone,
important topics, chhodne wali cheezein.

_Vague:_ "Summarize this report."

_Clearer:_ "Summarize this quarterly financial report for senior executives who have ten minutes
to read. Focus on revenue trends, major risks, and recommended actions. Short bullets, one page.
Highlight significant changes from last quarter. Avoid unnecessary accounting jargon."

**Completeness clever wording se zyada matter karta hai.**

## 4.2 Process Description

Sawal: "AI kaam kaise kare?" Steps, order, method, imitate karne wale examples, finish se pehle
checks specify karo.

_Example:_ "Review this code for correctness first, security second, style last. Naming issues par
time waste na karo jab tak code actually work na kar raha ho confirm na ho."

Process description sabse zyada matter karta hai jab kaam ke multiple stages hain. 3 vendor
proposals ka example: sab paste kar ke ek saath recommendation maangne se tum sirf ending check kar
sakte ho. Isliye **order se split karo**, har step check karo send karne se pehle:

1. Har proposal se same facts ek table mein extract karo (price, length, exit terms, support
   hours). **Check:** source se 3-4 cells confirm karo.
2. Criteria par vendors compare karo, sirf table se. **Check:** kya har difference table mein hai?
3. Score karo, apni weighting se. **Check:** kya scores tumhare criteria follow karte hain?
4. Recommendation draft karo. **Check:** sirf wo claim ho jo steps 1-3 support karte hain.

Extraction pehle aata hai kyunke sab kuch usi par depend karta hai — galat price comparison,
scoring, draft tak carry hoti hai aur fine lagti hai.

## 4.3 Performance Description

Sawal: "yeh AI kaise behave kare, kiske liye?" Concise/detailed, supportive/challenging,
exploratory/decisive, questions-first/assumptions, flag-uncertainty/best-answer.

_Example:_ "Challenge my assumptions when they are weak. Flag uncertainty. Do not agree with me
just to be polite. If my argument is stronger, explain why. If yours is stronger, hold your
position."

Yeh version audience-of-one serve karta hai. Framework-size matlab: performance description define
karta hai AI apne aap kaise behave kare, un logon ke liye jo aksar tum nahi ho aur kabhi instruction
nahi dekhenge. Chat mein bad performance description 10 minute irritate karta hai; deployed agent
mein, **yeh product hai.**

> Prompt engineering poochta hai "yeh message kaise phrase karoon?" Context engineering poochta hai
> "AI ko succeed karne ke liye kya available hona chahiye?" (documents, examples, memory, history,
> policies, tools, records, definitions, instructions). Achha-likha prompt agent ko bacha nahi
> sakta jiske pass galat data, missing rules, poor examples, ya tools na hon.

> **Where this leads:** **System prompt** = standing instruction jo AI har conversation ki shuruat
> mein parhta hai — performance description permanent banata hai. `SKILL.md` process description
> reusable banata hai. System of Record domain knowledge/rules/governance rakhta hai. Aage: System
> of Context, System of Record.
