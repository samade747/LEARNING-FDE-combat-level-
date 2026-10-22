# 02 — Part 2: Delegation (Concept 3)

**Sabse common beginner mistake** first prompt se pehle hoti hai: log typing shuru kar dete hain
bina decide kiye ke kya chahiye, good result kaisa dikhta hai, kaunse parts AI kare, aur kaunse
decisions kabhi hath se na jaayein. Yeh hai **Delegation**.

**Delegation** = decide karna ke kaam insaan aur AI mein kaise divide ho. Sirf AI ko kaam dena
nahi — **workflow design karna hai.**

Teen parts:

1. **Problem awareness** — goal aur kaam samajhna
2. **Platform awareness** — kaunsa AI system/tool fit karta hai, samajhna
3. **Task delegation** — decide karna kaun kaunsa part kare

## 3.1 Problem Awareness

AI se kuch bhi maangne se pehle khud se pucho:

- Goal kya hai?
- Yeh kiske liye hai?
- Success kaisa dikhta hai?
- Kya ghalat ho sakta hai?
- Human judgment kahan essential hai?

**Example:** "Build me an invoice-chasing agent" bolna kaafi nahi. Hard questions abhi bhi
unanswered: kaunse customers contact ho, kitne din late invoice, kaunsa tone, kis amount se upar
human approval, dispute hone par kya ho, accounting system mein kya padhe, sirf draft ya send bhi
kar sakta — **yeh business questions hain, prompting questions nahi.** AI tumhari business policy
decide nahi kar sakta jab tak tum deliberately authority na do — aur kai cases mein dena bhi nahi
chahiye.

## 3.2 Platform Awareness

Koi AI system har job mein equally achha nahi: hard multi-step problem ke liye reasoning model,
current info ke liye search-enabled assistant, software work ke liye coding agent, multi-step kaam
ke liye agent-capable system. Model names yaad rakhna zaroori nahi (market tezi se badalta hai) —
habit zaroori hai: **"is right tool for this job hai?"** poochna. Alag systems try karo, notes
rakho.

## 3.3 Task Delegation

Problem + platform samajhne ke baad kaam split karo:

| Task | Best Owner | Why |
|---|---|---|
| Audience/learning goals decide karna | Human | Purpose + judgment chahiye |
| Possible structures suggest karna | AI + human | AI breadth deta, human choose karta |
| Agreed outline se sections draft karna | AI | First drafts mein tez |
| Factual claims verify karna | Human | Accountability author ke pass rehti |
| Lived experience/local examples | Human | AI ka experience nahi hota |
| Grammar/consistency | AI | Mechanical review ke liye fit |
| Final course approve karna | Human | Tumhara naam/reputation attached |

Sawal "Can AI do this?" nahi — **"Kaunse parts AI kare, kaunse main karoon, aur kyun?"**

> **Where this leads in Agent Factory:** Delegation specification ban jata hai — goal, constraints,
> risks, definition of done. Task delegation Digital FTE ki boundary ban jati hai (AI kya kare,
> human kya rakhe, kya escalate ho). Aage: Spec-Driven Development, The FDE AF Model.
