# 00 — Overview

## Yeh Kiske Liye Hai

Har us bande ke liye jo AI tool use karta hai jo aapki taraf se **action le sake**: files parhe, likhe,
commands chalaye, services se connect ho. Yeh chatbots nahi hain jo sirf jawab dete hain — yeh **AI
assistants hain jo asal mein kaam karte hain.**

4 tools jo is tarah kaam karte hain:

|             | Coding/Engineering ke liye | Non-coding kaam ke liye |
| --- | --- | --- |
| **Anthropic** | Claude Code (terminal, IDE, web) | Claude Cowork (desktop app) |
| **Open-source** | OpenCode (terminal, koi bhi AI model) | OpenWork (desktop app, koi bhi AI model) |

**7 principles in sab 4 tools mein same tarah kaam karte hain.** Examples alag alag fields (research,
writing, coding, business) se hain, lekin principles identical hote hain.

## Mode 1 vs Mode 2 (Reminder)

1. **Mode 1: Problem solving.** Tool kholo, task solve karo, result ship karo. **Yeh course Mode 1
   sikhata hai.**
2. **Mode 2: AI Workers banana.** Permanent AI assistants jo khud chalte hain, aapke bina. Yeh alag
   course mein hai.

> **Safety pehle:** Yeh AI tools aapki files parh, edit, delete kar sakte hain. Commands chala sakte
> hain. AI ko kuch bhi dene se pehle samjho woh kya touch kar sakta hai — approval maango har action
> se pehle, sab kuch ek sath access mat do.

## The Essentials in Five Bullets (60% Value)

1. **Action over talk.** General agent ki value **karne** mein hai — commands chalana, files parhna,
   services call karna. Har prompt ko treat karo jaise usse ek action ya artifact nikalna chahiye, sirf
   ek paragraph explanation nahi.
2. **Code (aur structured artifacts) over prose.** Jab precision matter kare, schema, table, code
   block, ya checklist mango — paragraph nahi. Format constrain karne se output quality bohat barh
   jati hai.
3. **Verify, don't trust.** Har meaningful output ko verification step chahiye: code ke liye tests,
   memo ke liye rubric, high-stakes deliverable ke liye cross-model review. "Looks right" hi failure
   mode hai.
4. **Small steps, atomic checkpoints.** Kaam ko reversible units mein todo. Har unit ke baad commit/
   snapshot/save karo. Agent ko kabhi bhi ek ghante ka kaam bina ek bhi checkpoint ke mat karne do.
5. **Files are memory.** Conversation volatile hai; filesystem durable hai. Jo bhi sessions ke across
   yaad rakhna hai (decisions, plans, conventions, glossaries) — file mein likho, chat history mein
   nahi.

Baqi do principles (**Constraints** aur **Observability**) yeh nahi ke nayi skills hain — yeh pehle
paanch ko **operationalize** karte hain: agent ko lane ke andar rakhte hain, aur batate hain woh lane
mein raha ya nahi.

## Kyun Yeh Principles "Purane" Lagte Hain — The Lindy Effect

Computing ke sabse important tools sabse purane bhi hain: terminal, files, Git, SQL. Yeh dahaiyon se
hain aur ab bhi kaam karte hain. Iska naam hai **Lindy Effect** — jo cheez lambe waqt se useful rahi ho,
woh aage bhi useful rahegi.

**AI ke liye yeh kyun matter karta hai?** AI tools apna alag tareeqa invent nahi karte — woh wahi
dahaiyon purane tools use karte hain: terminal mein commands chalate hain, files mein result save karte
hain, Git se changes track karte hain, SQL se data dhoondte hain. AI insaani zaban mein sochta hai,
lekin **act** inhi proven tools se karta hai.

Teen cheezein samajhne wali:

1. **Yeh purane tools AI ke sath aur zyada important ban jate hain.** Terminal AI ko task chalane deta
   hai. Git changes track/undo karne deta hai. Files AI ko kaam save karne ki jagah deti hain.
2. **Aapka role badalta hai, lekin aap ab bhi zaroori ho.** AI code likh sakta hai, tests chala sakta
   hai, files edit kar sakta hai. Lekin usko **aap** chahiye problem clearly define karne ke liye aur
   result correct hai ya nahi check karne ke liye.
3. **AI tools best kaam karte hain jab woh apna kaam track, undo, aur check kar sakte hain.**

**AI in tools ko replace nahi karta. Inhe aur zyada valuable banata hai.**

## 7 Principles — Ek Nazar Mein

| # | Principle | Rokti Hai Kaunsi Galti |
| --- | --- | --- |
| 1 | **Bash is the Key** | "Agent sirf baat karta hai, karta kuch nahi" |
| 2 | **Code as Universal Interface** | "Prose request baar baar galat samjha jata hai" |
| 3 | **Verification as Core Step** | "Output theek lagta hai lekin production mein toot jata hai" |
| 4 | **Small, Reversible Decomposition** | "Ek bare change ne poori dopeher barbaad kar di" |
| 5 | **Persisting State in Files** | "Agent bhool jata hai kal kya decide hua tha" |
| 6 | **Constraints and Safety** | "Agent ne aisi files chhui jo authorize nahi thi" |
| 7 | **Observability** | "Pata hi nahi agent ne asal mein kya kiya" |

Yeh **importance ke order mein nahi** hain — **building dependency** ke order mein hain. Har ek upar
wali par khara hota hai.

> **Principle 1 aur 2 alag hain:** P1 (Action) — AI kaam ke baare mein *baat karta hai* lekin karta
> nahi. P2 (Structure) — AI kaam karta hai lekin result messy format mein deta hai. Dono chahiye: P1
> se AI kaam karta hai, P2 se result useful hota hai.

> **Thesis, ek line mein:** Principles **session** ko govern karte hain; tools sirf usi session ke
> **interfaces** hain. Principles se sochna seekho, to skill kisi bhi tool mein transfer ho jati hai.

---
[⬆ Index](README.md) · [Agla: Principle 1 ➡](01-principle-1-bash.md)
