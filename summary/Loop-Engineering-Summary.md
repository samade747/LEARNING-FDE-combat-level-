# Loop Engineering — Aasan Summary (Roman Urdu + English)
*Source: The AI Agent Factory — "Loop Engineering: A Crash Course" (Panaversity)*

---

## 🎯 Bunyadi Idea (The Big Shift)

Pehle aap coding agent ko **turn-by-turn** chalate the: aap prompt likhte, agent kaam karta, aap check karte, phir agli instruction dete. Aap khud "heartbeat" the — matlab aap hi system ko baar baar start karte the.

**Loop Engineering** iska ulta hai. Ab aap ek chota **system** banate hain jo *khud* chalta hai:
- Subah khud start hota hai
- Dekhta hai raat mein kya hua
- Faisla karta hai kya karna hai
- Kaam agent ko deta hai
- Result check karta hai
- Sirf zaroori faislay (jo risky hain) aap tak late hain

Aapki value khatam nahi hoti — bas **shift** ho jati hai do cheezon mein:
1. **Intent** — aap clearly bata dein ke aapko kya chahiye (itna clear ke result check ho sake)
2. **Accountability** — jo bhi ship ho, uski zimmedari aap lete hain

> Loop beech ka kaam karta hai. Do ends (intent + accountability) hamesha aapke paas rehte hain.

---

## 🧠 4 Layers — Prompt se Loop tak ka safar

Har layer pichli ko wrap karta hai:

1. **Prompt Engineering** — sirf woh alfaz jo aap likhte hain
2. **Context Engineering** — model ek turn mein kya kya dekhta hai
3. **Harness Engineering** — code jo model ke around hota hai (tools chalata hai, errors handle karta hai)
4. **Loop Engineering** (yeh course) — poora outer cycle: system kis cheez par kaam karta hai, kab start hota hai, kaise pata chalta hai "done" hai

**Chota Loop vs Bara Loop:**
- **Chota loop (inner loop):** ek agent ka apna cycle — model ko context do, model tools mangta hai, tools chalao, result add karo, repeat — jab tak model khud "done" na keh de. **Problem:** model apne aap ko khud judge kar raha hota hai! Isiliye "outside stops" chahiye (test, limit, checker).
- **Bara loop (outer loop):** yeh manager hai — decide karta hai kaunsa kaam dena hai, kab start karna hai, kaise grade karna hai, kal ke liye kya yaad rakhna hai. Chota loop ka ek pura run = ek **"beat"**.

---

## 🩺 Loop ke 6 Parts (Yaad rakhne wali cheez)

Har loop mein **5 working parts + 1 memory layer** hota hai:

| # | Part | Kaam |
|---|------|------|
| 1 | **Heartbeat** | Schedule ya event jo loop ko start karta hai (isके bina sirf ek run hoga, loop nahi) |
| 2 | **Worktree** | Isolation — do agents same file overwrite na karein |
| 3 | **Skill** | Project ki knowledge ek jagah likhi hui (`SKILL.md`), taake har run zero se start na ho |
| 4 | **Subagent (Maker-Checker)** | Ek agent kaam karta hai, dusra check karta hai |
| 5 | **Connector (MCP)** | Loop asli tools mein *act* kar sake (PR khole, ticket update kare) — sirf suggest na kare |
| 6 | **Spine (State/Memory)** | Disk par file jo yaad rakhti hai kya hua — **"No spine, no loop"** |

> Yaad rahe: model har run ke baad sab bhool jata hai. Repo (files) yaad rakhti hai.

---

## ❤️ Part 2 — 4 Heartbeats (Loop kaise start hota hai)

Chaar tarah ke heartbeat hain — "aap pakde huye ho" se "khud chalta hai" tak:

1. **In-session loop** (`/loop`) — kitchen timer jaisa. Sirf tab tak chalta hai jab tak aapka session/terminal khula hai. Session band = loop band.
   - *Example:* ISS (Space Station) ki location har minute check karna.

2. **Conditional loop / Run-until-done** (`/goal`) — "khana taste karke bataye ke ready hai ya nahi." Timer se nahi, ek **checked condition** se rukta hai. Jaise: "jab tak tests pass na ho jayein."
   - Zaroori: agent khud apna kaam approve nahi karta — ek **alag checker** (chota model) decide karta hai "done" hai ya nahi.
   - Har loop ko 3 stops chahiye: **success condition**, **limit** (max tries), **no-progress check**.

3. **Scheduled (Routine)** — alarm clock jaisa. Laptop band ho tab bhi chalta hai (Anthropic ke servers par). Jaise: "har weekday 9am, overnight CI failures dekho."

4. **Event-driven** — doorbell jaisa. Kuch nahi hota jab tak koi PR khole ya message aaye — phir turant react karta hai.

**Choose karne ka rule:** Task khatam hota hai aur command prove kar sakta hai → **conditional**. Task repeat hota hai → **schedule/event**. Task sirf ek dafa hota hai → **koi loop nahi chahiye**, normal session use karo!

---

## 🏋️ Part 3 — Loop Kya Karta Hai (The Body)

Yeh 4 cheezein har "beat" mein hoti hain:

- **Isolation (Worktrees):** Parallel agents ek dusre ke kaam ko overwrite na karein — har ek ko apna folder/branch milta hai.
- **Knowledge (Skills):** Project ki habits ek `SKILL.md` mein likhi hoti hain, taake har run se dobara explain na karna pare.
- **Action (Connectors/MCP):** Loop sirf baat nahi karta — real kaam karta hai (PR khole, Slack post kare). **Rule:** Kam tools rakho (jo zaroori nahi unhe hatao), writes safe-to-repeat hon, error messages clear hon.
- **Maker-Checker (Subagents):** Sab se important choice! **Jo agent kaam banata hai, wahi khud grade nahi karta.** Ek dusra agent (alag model bhi ho sakta hai) check karta hai — isko **LLM-as-judge** bhi kehte hain.

**Verification Skills:** Jo cheez aap baar baar manually check karte hain, usko ek skill mein likh dein. Yeh check 4 jagah "reh" sakta hai:
1. **Standalone** — aap khud invoke karo
2. **Embedded** — us skill ke end mein add ho jo kaam banati hai
3. **Chained** — ek skill dusri ko call kare
4. **Har PR par** — team-wide gate ban jata hai

---

## 🦴 Part 4 — Spine (Memory Between Runs)

**Sab se zaroori concept jo beginners skip karte hain!**

Model har run ke baad **sab kuch bhool jata hai**. Agar har beat zero se start ho, to loop nahi — bas wahi pehla step baar baar chalta hai.

Do files rakho:
- **Rules file** (`CLAUDE.md` / `AGENTS.md`) — hamesha ki habits, har run start mein padhi jati hai (short rakhna, kyunki har run par cost hoti hai)
- **Progress file** (`progress.md`) — jo hua uska record: kya done hua, kya baaki hai. Har run **shuru mein padhta hai, end mein update karta hai**.

**Intern ki diary wali example:** Naye intern ko diary do. Front mein — sabak jo mila (mistakes se seekha), roz padho. Back mein — kal kya kiya, kahan chhoda, roz likho. Bina diary ke intern (aur loop) roz wahi galtiyan repeat karega.

---

## 🔁 Part 5 — Ek Poora Loop (Real Example)

**Morning-triage loop:** Har weekday 9am — overnight CI failures dekhta hai, safe fixes draft karta hai, ek reviewer check karta hai, PASS pe PR khol deta hai, risky cheez insaan ke liye chhod deta hai.

**Minimum Safe Loop Checklist (7 cheezein):**
1. Success condition
2. Limit (max tries/time/spend)
3. Isolated branch/worktree
4. Read-only checker
5. State file (spine)
6. Human gate (risky kaam insaan tak jata hai)
7. Log/notification (silent failure na ho)

**Result:** Aap subah uthte hain — 2 PRs review ke liye, 1 flagged decision. Aapne kuch type nahi kiya!

---

## 👨‍💻 Part 6 — Insaani Control Kaise Rakhein (Sabse Important Part!)

### 3 Feedback Loops (Ek Dusre Ke Andar)
1. **Coding loop** (minutes) — agent likhta hai, test karta hai, fix karta hai
2. **Feedback loop** (hours) — aap try karte hain, decide karte hain kya change karna hai
3. **Outside loop** (days) — real users use karte hain

Agent teenon khud nahi chala sakta — kyunki **aapko woh cheezein pata hain jo agent ko nahi** (Andrew Ng isko "context advantage" kehte hain). Machine fast loop chalata hai; aap decide karte hain **kya banana hai** aur **kaun zimmedar hai**.

### Token Cost — Asli Limit
- Har loop ko **cap karo** (max tries/time/spend)
- Sahi model choose karo (mushkil kaam ke liye strong, aasan ke liye cheap)
- Loop ko kam frequency par chalao — har 5 min ki jagah har ghante, cost mein bohat farq aata hai!
- *Example:* Har 5 minute chalne wala loop, har ghante chalne wale se 100+ guna mehnga ho sakta hai — kaam wahi hai!

### Human In / On / Out of the Loop
| Term | Matlab |
|------|--------|
| **Human IN the loop** | Har action se pehle insaan approve karta hai — slow, zyada control |
| **Human ON the loop** | System khud chalta hai, insaan dekhta hai aur rok sakta hai — fast |
| **Human OUT of the loop** | Koi dekh hi nahi raha — **yeh kabhi acceptable nahi** |

**Rule:** Jahan galat move mehngi aur wapis lena mushkil ho, wahan insaan rakho. Baqi jagah loop chalne do.

### Concept 15: Apne Project Ki Samajh Mat Khona!
Do log same loop bana sakte hain — ek use kar ke aur tez ho jata hai (kyunki gehri samajh rakhta hai), dusra use kar ke samajhna hi chhod deta hai. **Loop yeh farq nahi bata sakta — sirf aap bata sakte hain.**

> "AI Gravity" — yeh force hamesha khinchta hai ke AI se zyada se zyada kaam karwao. Loop se yeh pull aur strong ho jata hai kyunki woh so'te waqt bhi chalta hai.

---

## 🐕 Dogfooding — Yeh Book Khud Apne Loops Use Karti Hai

1. **Feedback loop** — readers ke comments automatically sort karta hai, sirf zaroori cheezein insaan tak jati hain
2. **What's New loop** — book mein daily changes ka summary khud likhta hai, koi human approval nahi (kyunki galti sasti hai, revert kar sakte hain)

**Rule jo yahan se seekha:** Jahan galti mehngi ho, wahan human gate rakho. Baqi jagah chhod do.

---

## 📌 Sabse Zaroori Baat (Yaad Rakhne Wali)

> **Do layers hain is course mein — ek yaad rakhni hai, doosri sirf lookup karni hai:**
> - **Lasting layer (yaad rakho):** Loop ki shape (heartbeat, 5 working parts, spine), maker-checker split, aur intent+accountability ka concept.
> - **Mechanical layer (lookup karo):** Commands, flags, model names — yeh har hafte change hote hain, docs check karte rehna.

---

## 📝 Quick Glossary

| Term | Aasan Matlab |
|------|--------------|
| Agent | AI system jo tools use kar sakta hai, sirf jawab nahi deta |
| Loop | System jo kaam start karta hai, check karta hai, yaad rakhta hai, repeat karta hai |
| Beat | Loop ka ek pura run |
| Heartbeat | Woh schedule/event jo beat start karta hai |
| Stopping condition | Testable rule jo bataye kaam done hai |
| Maker-checker | Ek banata hai, dusra check karta hai |
| Worktree | Alag working folder/branch |
| Spine | Saved state jo ek beat se dusre beat tak memory le jati hai |
| Human gate | Woh point jahan insaan approve karta hai risky kaam se pehle |
| Routine | Claude Code ka cloud automation |

---

*Yeh summary poore chapter (6 Parts + Dogfooding + 8 Practice Projects + Routines Appendix) ka overview hai. Agar kisi ek part ko deeply teach karna ho students ko, bata dena — us par alag se detail nikaal doonga.*
