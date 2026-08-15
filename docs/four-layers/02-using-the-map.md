# 02 — Map Use Karna

## Concept 9: Konsi Layer Toti Hai?

Har layer apne alag, pehchan ne layak tareeqe se toti hai — isliye **symptom surface batata hai.**

| Kya Dikhta Hai | Pehle Kahan Dekho | Kya Badlo |
| --- | --- | --- |
| Output shape/tone galat, lekin task samjha | **Prompt** | Sab se kamzor ingredient |
| Jawab confident, fluent, factually galat | **Context** | Curator: kya aya, kaunse order mein, kya drop hua |
| Success report karta hai jo demonstrate nahi hua | **Harness** | Tools, error handling, beat kya prove kare |
| Galat jawab bina check ke insaan/system tak jate hain | **Loop** | Checker, kisne criteria choose kiye |
| Kabhi rukta nahi, jaldi rukta hai, ya guess karta hai | **Loop** | Stops aur gate |

**2 honest notes:**
- **Ye search order hai, verdict nahi.** Failures layers cross karti rehti hain. Har row "yahan pehle
  dekho" hai, "yahan blame hai" nahi
- **Ye table jo aadat todti hai:** Team $50 kharch karti hai repeat kar ke, response system prompt
  rewrite karna hota hai. Prompt theek thi. **No-progress check nahi thi.** Lekin prompt wo layer hai
  jo 10 second mein edit hoti hai. **Layer ko zor se naam do, kuch touch karne se pehle. 5 second lagte
  hain, aur ek fix vs 6 fixes ka farq hai.**

## Concept 10: Kaunsi Layers Aap Asal Mein Own Karte Ho?

Har project pe sab 4 nahi banate. Zyada tar waqt 3 **rent** karte ho.

| Layer | Mode 1: General Agent Se Problem Solve Karna | Mode 2: Worker Manufacture Karna |
| --- | --- | --- |
| **Prompt** | Zyada tar aapki | Aapki, ek dafa likhi, reuse hoti |
| **Context** | Partly aapki: kya attach karo, kab clear karo | Aapki. Curator aap likhte ho |
| **Harness** | Rented, partly configurable | Aapki |
| **Loop** | Zyada tar rented | Aapki. Har stop kuch hai jo aap ne likha |

**Mode 1** mein, "no-progress check add karo" ek instruction nahi hai jo aap le sako — koi file nahi
hai. Aapka kaam **rented behavior jaanna** hai: harness window kahan compact karti hai? Kya wo chup
chaap retry karti hai? Room khatam ho to task ke beech mein kya hota hai?

> **Ehtiyat:** *"Mera tool ye sab karta hai"* — tool ye **apne** kaam ke liye karta hai. Wo worker jo
> aap banane wale ho, uske liye koi tool nahi karta. Claude Code apni beats cap karta hai. Aapki likhi
> loop ko cap nahi karta. **Yehi gap hai jahan demo production incident ban jata hai.**

**4 minute mein pata karo:** Apna beats-used tool lo, likho guess: (1) window bharne pe harness kya
hataati hai, batati hai? (2) tool call fail ho to retry karti hai, kitni dafa, dikhti hai? (3) run limit
pe pohanche to already kiya kaam ka kya hota hai?

## Concept 11: Graphs Kahan Fit Hote Hain

Graph engineering bohat discuss hoti hai, lekin **graph 5th layer nahi hai.**

4 layers **ek execution path** describe karte hain: ek message, ek window, ek beat, ek run. **Graph
ek topology describe karta hai:** aage kya chalega, edge pe kya move hota hai, kaun kisay check karta
hai.

> **4 layers describe karte hain ek node ke andar kya hota hai. Graph describe karta hai nodes ke
> darmiyan kya hota hai.**

Node **agent hona zaroori nahi** — function, rule, tool call, human gate, measurement, ek beat, poori
loop ho sakta hai.

**3 uses is book ke:** **Execution graph** (aage kya chale), **memory graph** (entities/findings preserve
karta), **governance graph** (kaun feed/check/approve/constrain karta hai).

**Ek real graph, 6 nodes, ek agent:**
- **Pull** — function payments/invoices parhta hai, koi model nahi
- **Route** — fixed rule Rs.500,000 se upar invoices flag karti hai
- **Match** — **poora agent**, 4 layers use kar ke matches propose karta hai
- **Gate** — Ayesha low-confidence/high-value cases decide karti hai
- **Prove** — function matched total ko statement total se compare karta hai
- **Post** — accepted matches likhta hai, unresolved review ko bhejta hai

**Sirf Match agent hai.** Baaki nodes deterministic code, rule, insaan, measurement hain. **Prove node**
wo check rakhta hai jo Concept 6 mein missing thi — Match ke bahar, Match ise skip nahi kar sakta.

> **Token cost zyada tar Match ke andar hai.** *"Humne graph banaya"* isliye keemat ke baare mein kam
> batata hai — agentic nodes count karo, unki frequency measure karo.

## Concept 12: Jab Framework Aapse Larta Hai

Ek map jise aap kabhi challenge nahi karte, wo map nahi rehta, ritual ban jata hai.

**Kuch failures genuinely 2-layer hain.** Context ki dropping policy sirf isliye problem karti hai
kyunke loop runs ko itna lamba jane deti hai ke window bhar jaye. Konsi layer toti? Dono, honestly.

**Kuch diagnoses ek layer point karte hain, fix doosri layer pe hoti hai.** Jab agent aisi success
report kare jo demonstrate nahi hui, **diagnosis layer 3** hai (beat apne baare mein kya jaan sakti
hai). **Fix usually layer 4** hai (bahar se chuna hua success criterion). **Framework ne apna kaam
theek kiya jab usne aapko symptom ki jagah se kahin aur bheja.**

**Kuch failures in 4 mein se koi nahi hain.** Kabhi model **task genuinely nahi kar sakta** — koi bhi
containers ka arrangement capability nahi banati jo hai hi nahi. Sab 4 clear kar chuke ho aur kaam abhi
bhi bura hai, to honest agla move: behtar model, chhota task, alag approach.

**Har project ko 4 nahi chahiye.** Ek dafa chalne wala task loop nahi maangta.

---
[⬅ 4 Layers](01-four-layers.md) · [Agla: Practice ➡](03-practice.md)
