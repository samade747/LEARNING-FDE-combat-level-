# 01 — Part 1: The Deal (Concepts 1-3)

## Concept 1 — Code Ab Coding Se Gated Nahi Hai

Bookkeeper ki whole career mein deal same tha: ya programming seekho, ya hand se karo. 2 files
reconcile karna matlab ek shaam hunting, ya developer se **script** (chhota program, file ki tarah
saved, dobara run ho sake) maango — phir 2 hafte wait karo kuch almost-fit cheez ke liye.

**Naya deal: AI developer hai, tum client ho, developer seconds mein kaam karta hai, free mein,
aur revisions se kabhi tired nahi hota.**

AI code likh sakta tha 2022 mein bhi — badly. 3 cheezein saath grow hui:

- **AI _working_ code likhta hai** small, well-described problems ke liye — pehli ya doosri try
  mein usually succeed
- **AI khud code _run_ karta hai** — **sandbox** (temporary computer AI company ki taraf se) mein,
  ya tumhari permission se tumhare machine par
- **AI khud code _repair_ karta hai** — error message AI ko wapas jata hai, AI fix karta hai

> **2023 mein try kiya tha? Ek cheez unlearn karo:** pehle AI code ka block haath mein de deta tha
> aur chala jata — agar language installed na ho, conversation wahan khatam. **Yeh era khatam
> hai.** Aaj AI code likhta _aur run karta_ same reply mein.

Unit of work change hoti hai: "Can I write this?" nahi — **"Can I describe this?"** Description
pehle se tumhari skill hai — colleagues, contractors, tailors ko tum har hafte describe karte ho.

**6 professions se:**

| Kaun | Describe kiya problem | Code ne kya kiya |
|---|---|---|
| Bookkeeper | 2 sheets match karni, mismatches dhoondo | 1,400 rows reconcile, 23 mismatches flag |
| Doctor | Appointments ka saal, worst no-show slots | Monday 9am 3x worse |
| Marketer | 4 exports, alag columns, ek table | Formats merge, table+chart |
| Teacher | 200 students, weighted finals, comments | Teeno kiye, comments ne shaam bachayi |
| Student | 300 files ka naam date se rename karo | 300 under 1 minute rename |
| Network engineer | Devices mein login, health report | Daily chalta hai, desk pe aane se pehle |

6 professions, zero lines of code read.

## Concept 2 — Code Actually Kya Hai (60-Second Version)

**Code exact instructions ki list hai jo computer perfectly follow karta hai, kisi bhi speed/
number of times par.** English mein likha procedure hai; programming language mein likha code hai.

2 naam dekhoge:

- **Python** — files/spreadsheets/data/reports ke liye normal choice, AI isse best jaanta hai
- **JavaScript/TypeScript** — click-able cheez ke liye (web tool, game, calculator)

**Tum kabhi language choose nahi karte** — technical judgment hai jo tum hand over kar rahe ho.
Number/file/report chahiye = Python. Click-able cheez = JavaScript. **Choice output follow karta
hai.**

```python
totals = {}
for row in rows:
    totals[row.category] = totals.get(row.category, 0) + row.amount
```

Eyes slide off ho jaye, fine hai. "Har row ke liye, amount us category ke total mein add karo" —
yeh level reading chahiye, aur zyada nahi. Tum **allowed** ho code dekhne ke liye, **required**
nahi ho. Scrolling code mechanic ke open engine bay jaisi hai — proof ke real kaam ho raha hai,
test nahi jo tumhe pass karna hai.

**Property yaad rakho: Code dono directions mein exact hai.** Last cent tak compute karta hai bina
arithmetic error ke; exactly wo bhi karta hai jo bola gaya, including ghalat cheez, perfectly, at
scale. Galat samajh par bana script 300 files ko galat tarah se bhi utni hi tezi se rename karta
jitna sahi tarah se karta. **Power aur danger same property se aate hain.**

**Kitchen analogy:** Recipe = insaan ke liye code. "20 minute simmer karo" attentive cook ko diya
to dinner bane; obedient robot ko "20 hours" ghalti se bola gaya to charcoal bane, flawlessly.
Robot fail nahi hua — **brief** (plain-English job description) fail hui. AI clear brief bhi
misread kar sakta hai, isliye result hamesha check karo.

## Concept 3 — Dividing Line: Kaunse Problems Code Problems Hain

**Yeh sawal prompt se pehle decide karo: AI ki mind ke liye sawal, ya AI ke hath ke liye kaam?**

**Answer problem** — AI apni reasoning se reply kar sakta (draft/advise/summarize/explain).
**Code problem** — AI ko tumhare real data par code likhni/chalani zaroori hai. Zyada log sirf
pehle use karte hain, phir sochte hain summary mein galat totals kyun aaye — **AI ne answer diya
jahan compute karna chahiye tha, data skim kiya, process nahi kiya.**

4 signals, koi bhi **ek** kaafi hai: **VPRF — Volume, Precision, Repetition, Files**

| Signal | Test | Examples |
|---|---|---|
| Volume | Hand se karne se zyada items | 300 files rename, 5,000 rows total |
| Precision | Galat digit ka consequence | Invoices, payroll, grades, money |
| Repetition | Yeh task phir se aayega | Month-end reports, daily checks |
| Files | Problem files mein rehta hai, sentences mein nahi | Spreadsheets, logs, image folders |

Koi signal fire na ho → answer problem, AI Prompting skills use karo. Ek bhi fire ho → code
problem.

**Trap:** jo answer problem lagte hain par Precision fire karte hain. "Roughly mera sales trend
kaisa tha is saal?" conversational lagta hai, par decision number par depend karta hai — yeh
**code problem hai, phrasing casual ho tab bhi.**

**School example:** administrator ne AI se "fee spreadsheet dekho, kaun behind hai" pucha —
confidently 8 names di, real number **11** thi. AI ne skim se answer diya — skim partial payment ko
"paid" padh leta hai.

**Language curiosity (never choose it):** number/file/report → Python; click-able cheez →
JavaScript/TypeScript.
