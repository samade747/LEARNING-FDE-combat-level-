# 03 — Part 3: What Turned a Text-Predictor Into Something That Acts (Ideas 8-9)

Do ideas jo "yeh text predict karta hai" aur is poori book ke agents ke darmiyan gap band karte hain.
Yeh bridge hai *yeh kya hai* se *yeh duniya mein kya karta hai* tak.

## Idea 8 — Tools Isko Act Karne Dete Hain, Sirf Describe Nahi

Ab tak jo describe hua wo ek machine hai jo text produce karti hai. Ek pure text-predictor aapko
training se yaad mausam bata sakta hai, lekin aaj ka mausam **check** nahi kar sakta, real numbers par
calculation nahi chala sakta, aapki file nahi parh sakta, email nahi bhej sakta. Saalon tak yehi
ceiling thi.

Ceiling uthi **tools** ke saath. Tool ek defined action hai jo model call kar sakta hai (web search,
code run, file read, email draft), context window mein describe kiya gaya baaqi sab cheezon ke saath
(Idea 5). Mechanism almost embarrassingly simple hai result dekh kar. Kabhi kabhi model predict karta
hai ke sahi continuation plain prose nahi, balke "search tool ko yeh query ke saath use karo" hai. Jab
aisa hota hai, product woh action **real mein** chalata hai, result wapis context window mein daal
deta hai, aur model wahan se continue karta hai. Prediction, action, result-wapis-context-mein,
dobara predict. Yehi loop hai farq ek chatbot ke darmiyan jo duniya describe karta hai, aur ek
assistant ke darmiyan jo duniya par act karta hai.

Isi wajah se ek hi underlying machine kabhi chat window ban sakti hai, aur tools wire hone par, agla
din aapka folder reorganize karne wala agent. Baqi Foundations courses, hood ke neeche, isi predictor
par wire kiye gaye specific tools ke courses hain:

- **Code execution** — *Code You Never Write* ke peeche ka tool: model program predict karta hai, tool
  chalata hai, real result wapis aata hai.
- **Connectors** — tools jo aapki real apps (Drive, Gmail, Slack, tracker, database) se wire hote hain,
  agent ko safe, permission-scoped access dete hain — *Skills & Connectors* ka subject. Connectors ek
  shared open standard bolte hain, **MCP** (Model Context Protocol). Rishta ek line mein: **MCP standard
  plug shape hai; connector ek specific appliance hai jo usi plug ke liye bana hai.** Kyunke plug
  standard hai, ek agent thousands of alag services se connect ho sakta hai bina har ek ke liye custom
  wiring ke. Aur jo cheez **nahi** badalti: connector jo bhi fetch kare, wo har tool result ki tarah
  text ban kar context desk par aata hai (Idea 5), jise model continue karta hai (Idea 1). Naya plug,
  same machine.
- **Web search** — woh tool jo stale model (Idea 2) ko rescue karta hai — *AI Prompting in 2026* mein
  cover hota hai.

> **"Agent" ki mechanical definition:** Yeh book "agent" un AI ko kehti hai jo aapki taraf se multi-step
> kaam karta hai. Ab aap dekh sakte ho hood ke neeche yeh matlab kya hai: agent hai wahi next-token
> predictor, jise tools diye gaye hain, jo predict-act-observe loop baar baar chalata hai ek goal ki
> taraf: ek action predict karna, uska result apne context mein dekhna, aur wahan se agla action
> predict karna. Koi nayi tarah ka mind involved nahi hai. Ek familiar predictor hai, kuch tools hain,
> aur ek loop hai. Yehi poori foundation hai jis par baaqi book banati hai.

## Idea 9 — "Thinking" Bas Answer Se Pehle Aur Zyada Prediction Hai

Naye models answer dene se pehle "think" ya "reason" kar sakte hain, aur *AI Prompting in 2026*
(Concept 5) aapko batati hai ke mushkil tasks ke liye "think hard" invoke karo. Yeh asal mein kya hai
jaan lena aapko isko zaroorat se zyada mystify karne se rokta hai.

Ek **reasoning** model, final answer dene se pehle, pehle intermediate working ka ek lamba stretch
predict karta hai (steps lay out karna, approaches try karna, khud ko check karna) aur **tab** final
answer predict karta hai, ab woh poori working uski apni context window mein baithi hui build karne
ke liye (Idea 5). Yeh phir bhi pure next-token prediction hai. Trick yeh hai ke **answer predict karna
aasan aur zyada accurate ho jata hai jab achi reasoning chain pehle se desk par predict karne ke liye
maujood ho.** Pehle work through karna genuinely help karta hai — usi wajah se jaise ek insaan ko paper
par sochna help karta hai commit karne se pehle.

Yeh isi liye hai ke "think step by step" kabhi ek useful phrase type karne ke liye hoti thi, aur ab
often built-in hai: aap manually model se reasoning desk par pehle rakhne ko kehte the; ab model khud
hard problems ke liye yeh karta hai. Yeh cost aur wait bhi explain karta hai. Reasoning matlab bohat
saare extra tokens (Idea 4) generate karna jo aap kabhi nahi dekhte, aur woh tokens time aur money lete
hain. Isi liye prompting course kehti hai thinking mode genuinely hard sawalon ke liye save karo, quick
lookups ke liye skip karo.

Yeh, **however**, machine ko Idea 3 wali second faculty nahi deta. Reasoning model apna kaam usi
prediction process se check karta hai jo ghalat ho sakta hai — is liye yeh apni **kayi** mistakes pakar
leta hai, phir bhi kuch miss karta hai, aur ek reasoning chain ke andar full confidence ke saath
hallucinate kar sakta hai jo rigorous lagti hai. Zyada thinking gap ko narrow karta hai. Isko band
nahi karta. Aap phir bhi final check ho.

---

> **Yeh course jaan-boojh kar chhorta hai:** *No math, no code* ka promise rakhne ke liye kuch real
> topics side mein rakhe gaye. Teen worth naming: **training compute aur cost** (enormous, isi liye
> sirf chand organizations models banati hain), **safety aur alignment** (apna bara field), aur
> **weights ki deeper mechanics** (jisme yeh course chhora hua math chahiye). Yeh teeno upar wale 9
> ideas ko nahi badalte — yeh unke neeche aur saath baithe hain.

---
[⬅ Part 2 — Why It Behaves This Way](02-why-it-behaves-this-way.md) · [⬆ Index](README.md) · [Agla: Recap + Practice Prompts ➡](04-recap-and-practice-prompts.md)
