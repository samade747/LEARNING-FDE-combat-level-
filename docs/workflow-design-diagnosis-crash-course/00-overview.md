# 00 — Overview: Workflow Design & Diagnosis

## Do Teams, Ek Hi Tool

2 teams ne same AI assistant same job (contract review) ke liye adopt ki. **Team 1** ne kaam
step-by-step map kiya: AI clauses extract karta, playbook se departures flag karta, **redline**
(changes dikhati marked-up version) draft karta. Lawyer har change approve karta. Review time ~50%
gira, quality hold hui.

**Team 2** ne AI ko poore process par point kiya. Drafting achhi thi, to low-risk clauses
unsupervised approve karne diya. Ek mahine mein ek approved clause ne obligation banayi jo kisi
ne catch nahi ki — team ne tool poori tarah hata diya.

**Same product, same process, same model — farq sirf yeh tha kaunse steps hand over kiye.**

Ab ek chhoti failure jo tumne khud face ki hogi: answer disappointing aaya, tumne ya tool ko
incapable maan liya, ya random words change karte rahe jab tak kuch chal gaya.

**Yeh same mistake hai 2 directions mein.** Team 2 ne achhi draft ko proof samjha ke step handover
ke liye safe hai. Tum ek bad output ko proof samajhte ke task impossible hai.

> **Output verdict nahi hai.**

Jo asal mein batata: kaunsa step tha, error kya cost karta, kaun jawabdeh hai, aur symptom **kab**
shuru hua.

## Course Ek Minute Mein — 6 Sawal

| Stage | Decide Karne Wala Sawal |
|---|---|
| **Design** | Actual requirements kya hain, kaunse numbers compute karna zaroori hai? |
| **Map** | Is step ke liye: undo ho sakta, error kya cost karta, kaun jawabdeh hai? |
| **Build** | Yeh abhi prompt-and-iterate loop mein fit hota, ya outgrow ho gaya? |
| **Diagnose** | Symptom pehli baar kab dikhi? |
| **Persist** | Yeh fix rule hai, reference hai, ya procedure hai? |
| **Communicate** | Yeh kya karta hai, aur human gate exactly kahan hai? |

## Pehle Yeh Parho

**AI Fluency** pehle parho — apne kaam par delegation sikhata. Yeh course wahi skill team-run
workflow par le jati, jahan galat split kisi doosre par girta.

Projects+standing instructions (ChatGPT & Claude Quick Reference), Skills (Skills & Connectors),
code execution (Code You Never Write) — pehle mil chuke hone chahiye, yeh course sab 3 use karta,
sikhata nahi.

**Yeh course jawab nahi deta:** kya AI is kaam/data ko touch bhi kar sakta hai — wo Governance,
Risk & Responsible Use hai (agla Foundations course). Yeh course assume karta jawab "haan" hai.

## 18 Sawal Jo Course Answer Karta

| # | Sawal | Objective |
|---|---|---|
| 1 | Habit team workflow banne par kya change hota? | D4.4 |
| 2 | Messy document se requirements kaise nikalein? | D4.1 |
| 3 | Number kab compute hona chahiye, likha nahi jana chahiye? | D4.2 |
| 4 | Kaunse steps ko sab kuch de sakte ho? | D4.2 |
| 5 | Step ka owner decide karne wale 3 criteria kya hain? | D4.4 |
| 6 | Alag workflows same pattern kyun produce karte? | D4.4 |
| 7 | Map galat hone ke 3 tareeqe kya hain? | D4.4 |
| 8 | Map ko true kaun rakhta jab workflow move kare? | additive |
| 9 | Build loop kaisa dikhta hai? | D4.3 |
| 10 | Prompt-and-iterate se kab outgrow hota? | D4.3 |
| 11 | Bad output ke 4 causes kaise alag karein? | D7.1 |
| 12 | Kis order mein check karna chahiye? | D7.1 |
| 13 | "Not quite right" ko instruction mein kaise badlein? | D7.2 |
| 14 | Fix kahan jaye ke lasting rahe? | D7.2 |
| 15 | Jo friction notice karna band kar diya usay kaise dhoondein? | D7.3 |
| 16 | Kya measure karein, kab rukein? | D7.3 |
| 17 | Bad output nikal jaye to kya karein? | additive |
| 18 | Bina overstate kiye kaise describe karein? | D4.5 |

(Objective column CCAO-F exam blueprint ko map karta — D4 = Workflow Integration/Solution
Design, D7 = Troubleshooting/Optimization.)

## Try It Before You Read

Apni koi real workflow (3+ steps, 1 decision) AI ko do: "redesign karo AI ke sath, har step ke
liye batao AI kare ya nahi." Jo step **undo nahi ho sakta** (payment, customer-facing message)
dhoondo — AI ne usay handover kiya ya vague raha? Agar haan, tumne dekha confident redesign sabse
important jagah galat hui. Flag kiya aur human rakha? Pucho **kyun** — reasonable answer milega
generic shape se, tumhari organization ke baare mein kuch nahi — usay pata nahi error kitna cost
karta, regulator care karta ya nahi, kaun sign-off karta.

## Source

https://agentfactory.panaversity.org/docs/workflow-design-diagnosis-crash-course — Zia Tutor AI
connector, 2 windows, fetched 2026-10-23.

## Agle Files

- **01** — Part 1: Design the Work (Concepts 1-4)
- **02** — Part 2: The Delegation Map (Concepts 5-8)
- **03** — Part 3: Build It, Watch It (Concepts 9-10)
- **04** — Part 4: When It Misbehaves (Concepts 11-12)
- **05** — Part 5: Make the Fix Stick (Concepts 13-16)
- **06** — Part 6: Operate It, Explain It (Concepts 17-18) + Recap
- **07** — One-Page Map Template + 5 Try-This-Now Prompts + Project Overview
- **08** — What This Leaves Out + Terms + Sources
- **09** — Test Your Understanding (12-Q quiz)
- **projects/** — "Map, Break, Fix, and Explain" full workflow project
