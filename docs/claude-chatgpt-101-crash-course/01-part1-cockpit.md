# 01 — Part 1: The Cockpit (Concepts 1–3)

## Concept 1: Two Cockpits, One Discipline

Claude aur ChatGPT ko side-by-side kholo — surprisingly similar lagte hain. Dono dete hain:

- previous chats ki list
- message box
- model ya reasoning control
- files/tools ka menu
- projects ya workspaces
- memory aur instructions
- search aur research features

Yeh similarity **matter karti hai**. Tumhe do completely alag ways of working seekhne ki zaroorat nahi
— ek discipline seekhni hai, phir dekhna hai har product ne controls kahan rakhe hain.

**Jo skills transfer hoti hain:**

- task clearly describe karna
- useful context dena
- decide karna kya delegate karna hai
- answer check karna
- jaanna kab stronger model chahiye
- sensitive information protect karna

Products naam, layout, aur strengths mein differ karte hain — yeh differences time ke sath badalti
rehti hain. **Underlying work nahi badalta.**

Cockpit comparison ka ek honest moment: pilots do aircraft ko interchangeable nahi samajhte. Woh flying
ek baar seekhte hain, phir thora time lagate hain ek particular aircraft ke switches kahan hain yeh
dekhne mein. Flying transferable part hai. **Switch layout** wo part hai jo tum look up karte ho —
aur update ke baad dobara look up karte ho.

Dono products har task pe identical perform nahi karte — jo ek task pe excellent hai, doosre task pe
weaker ho sakta hai. Important work ke liye, acha habit hai: **same task dono mein chalao aur compare
karo.** Yeh hai **platform awareness** — kisi ek interface ka loyal banne ke bajaye, har tool ki
strength jaanna.

Dono companies ab chat se zyada offer karti hain: desktop apps, coding tools, browser agents — woh baad
mein book mein aate hain. Abhi **chat window ke andar** raho.

### Sab Se Zaroori Beginner Habit

Assistant se baat karo jaise ek capable colleague se karte ho. Koi serious request bhejne se pehle teen
cheezein cover karo:

1. **Set the stage.** Tum kaun ho, kya achieve karna chahte ho?
2. **Define the task.** Assistant ko exactly kya karna chahiye?
3. **Set the rules.** Kaunsa tone, format, constraints, ya examples follow karne hain?

Interface ek achi description ka replacement nahi hai — woh description ko rehne ki jagah deta hai.

**Yaad rakho:** pattern seekho, button placement nahi.

---

## Concept 2: Models and Thinking Modes

Dono assistants tumhe choose karne dete hain ke task pe kitni capability spend karni hai. Beginners
model **naamon** se shuru karte hain — yeh wrong jagah hai, kyunke naam fast badalte hain.

Iske bajaye **three-level pattern** seekho:

| Level | Best For | Trade-off |
| --- | --- | --- |
| Fast default | Roz ke sawaal, drafting, summaries, routine kaam | Fast aur cheap, hard problems pe kam depth |
| Thinking/reasoning | Multi-step reasoning, analysis, math, tricky code | Slower, zyada careful |
| Heavy flagship | Sab se hard analysis, lamba demanding kaam | Slowest aur sab se expensive, sab se capable |

Claude aur ChatGPT in controls ko alag expose karte hain, aur yeh naam hi tum actually milte ho — model
picker mein, vendor ke update notes mein, colleague ke message mein jo kehta hai "run it on Opus."

**Claude ke model names:** Haiku (sab se fast/cheap), Sonnet (everyday choice), Opus (heavy flagship).
Haiku aur Sonnet dono "fast" level pe, Opus "flagship" level pe. **Thinking Claude pe ek separate
switch hai**, model naam nahi.

**ChatGPT ke labels** Instant (everyday) se Pro (hardest tasks) tak chalte hain, beech mein thinking
levels.

Yeh jaanna ke konsa naam konsay level pe hai — iska matlab hai "run it on Opus" heavy flagship maang
raha hai aur "turn on thinking" switch maang raha hai. Anthropic ke apne certification exams Claude ke
naam bhi poochte hain.

Naam jaano, lekin apna mental model unke upar mat banao. **Trade-off** pe banao: **fast, phir zyada
reasoning, phir maximum capability.**

### Do Simple Rules

**Rule 1: Fast se shuru karo.** Normal fast mode zyada tar everyday work ke liye. Short rewrite, summary,
ya simple explanation ke liye heavy reasoning ka wait mat karo.

**Rule 2: Hard task pe escalate karo.** Thinking mode ya stronger model use karo jab:

- several steps ki logic ho
- careful comparison ho
- mathematics ho
- difficult debugging ho
- code jo correct hona zaroori ho
- complex analysis ho

Kabhi "AI fail ho gaya" ka matlab asal mein hota hai **"maine wrong level of capability use ki."**

> **Rule jo har model release survive karti hai:** model task se choose karo, habit se nahi — fast
> everyday ke liye, thinking hard reasoning ke liye, flagship genuinely difficult ke liye. Jab naam
> badlenge, pattern phir bhi kaam karega.

**Yaad rakho:** pehle reasoning ka level choose karo, current model names doosra number pe seekho.

---

## Concept 3: Context You Attach

Language model sirf us information se kaam kar sakta hai jo uske saamne hai. Isi liye **attachments**
matter karti hain.

Dono assistants yeh upload karne dete hain: PDFs, Word documents, spreadsheets, CSV files, images,
screenshots, code files.

File attach karne pe tum us conversation ko **zyada context** de rahe ho. Compare karo:

> Summarize this contract.

vs

> Summarize this contract. _(contract attached ke sath)_

Words almost identical hain. Doosra useful hai kyunke assistant **actually contract dekh sakta hai**.
Yehi screenshots ke liye bhi sach hai — dashboard, error, chart, ya interface mein help chahiye to
**dikhana** usually **yaad se describe karne se behtar** hai.

Dono products **live web search** kar sakte hain — jab model ka built-in knowledge kaafi nahi hota,
search current information conversation mein laata hai. Aur dono current conversation track karte hain,
isliye pehle kaha gaya baad ke answers ko shape karta hai.

**Lekin yeh tracking ki ek limit hai**, aur lambi piece of work pe tum us limit tak pahonch jaoge. Maan
lo tumne poora din quarterly board report draft karne mein guzara ek hi chat mein — teen signs batate
hain ke chat stale ho gayi hai:

- morning wali koi rule bhool jaye (jaise "no bullet points"), aur bullets wapis aa jayein
- apni pehle di hui figure se contradict kare
- answers generic advice mein drift kar jayein jo kisi bhi report ke baare mein ho sakti hai

Jab ek bhi sign dekho, na push karte raho, na chat chhoro — pehle **state summary** maango, ek short
record jahan kaam khara hai:

```text
Summarize what we have decided so far, what is still open, and every
rule I gave you. Keep it short enough to paste into a new chat.
```

Parho, galat cheez correct karo, files dobara attach karke fresh chat mein paste karo, aur aage chalo.
Agar har hafte yehi summary paste karte paye jao, **yeh project ka signal hai** (Concept 4).

### Habit Jo Build Karni Hai

Koi important sawaal poochne se pehle khud se poocho: **ek capable human colleague ko yeh sawaal achhe
se answer karne se pehle kya dekhna chahiye?** Phir assistant ko woh material do.

**Yaad rakho:** behtar context usually cleverer prompt se zyada answer improve karta hai.

---
[⬅ Overview](00-overview.md) · [Agla: Projects aur Memory ➡](02-part2-projects-memory.md) · [⬆ Index](README.md)
