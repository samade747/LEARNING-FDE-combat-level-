# Loop Engineering — Aasan Summary (Roman Urdu + English)

*Source: The AI Agent Factory — "Loop Engineering: A Crash Course" (Panaversity) — 15 Concepts*
*URL: https://agentfactory.panaversity.org/docs/loop-engineering-crash-course*

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

**Yeh idea kahan se aya:** Boris Cherny (Claude Code ke banane wale) ne kaha "I don't prompt Claude anymore. I have loops running that prompt Claude... my job is to write loops." Peter Steinberger (OpenClaw ke banane wale) ne kaha "you should be designing loops that prompt your agents." Addy Osmani ne is pattern ko naam diya aur uske parts list kiye.

---

## 🧠 4 Layers — Prompt se Loop tak ka safar

Har layer pichli ko wrap karta hai, aur har layer ek alag qisam ki failure rokti hai:

1. **Prompt Engineering** — sirf woh alfaz jo aap likhte hain (galat prompt rokti hai)
2. **Context Engineering** — model ek turn mein kya kya dekhta hai (bina context, model guess karta hai)
3. **Harness Engineering** — code jo model ke around hota hai (tools chalata hai, errors handle karta hai) — bina harness, aap khud sirf checker hain
4. **Loop Engineering** (yeh course) — poora outer cycle: system kis cheez par kaam karta hai, kab start hota hai, kaise pata chalta hai "done" hai — bina loop, schedule bhi aap hi hain

**Useful self-check:** "In layers mein se kaunsi mein abhi bhi hath se kaam kar raha hoon?"

**Chota Loop vs Bara Loop:**

- **Chota loop (inner loop):** ek agent ka apna cycle — model ko context do, model tools mangta hai, tools chalao, result add karo, repeat — jab tak model khud "done" na keh de.

  ```python
  while True:
      reply = model(context)
      if not reply.tool_calls:
          break                     # model ne khud decide kiya ke kaam khatam hai
      context += run_tools(reply.tool_calls)
  ```

  **Problem:** `break` wali line dekho — model apne aap ko khud judge kar raha hota hai! Ek common failure: agent file change karta hai, confidently "Done! All fixed" likhta hai, lekin tests kabhi chalaye hi nahi. Isiliye "outside stops" chahiye: **checked condition** (real test se prove karo), **limit** (max tries), **no-progress check** (agar kuch behtar nahi ho raha to ruko), **separate checker** (dusra process jo grade kare).

- **Bara loop (outer loop):** yeh manager hai — decide karta hai kaunsa kaam dena hai, kab start karna hai, kaise grade karna hai, kal ke liye kya yaad rakhna hai. Chota loop ka ek pura run = ek **"beat"**. Chote loop ka koi heartbeat nahi hota aur koi spine nahi hoti — beat khatam, sab bhool jata hai. Bara loop hi usay start karta hai, grade karta hai, aur yaad rakhta hai.

---

## 🩺 Loop ke 6 Parts (Yaad rakhne wali cheez)

Har loop mein **5 working parts + 1 memory layer** hota hai:

| # | Part | Kaam |
| :---- | :---- | :---- |
| 1 | **Heartbeat** | Schedule ya event jo loop ko start karta hai (iske bina sirf ek run hoga, loop nahi) |
| 2 | **Worktree** | Isolation — do agents same file overwrite na karein |
| 3 | **Skill** | Project ki knowledge ek jagah likhi hui (`SKILL.md`), taake har run zero se start na ho |
| 4 | **Subagent (Maker-Checker)** | Ek agent kaam karta hai, dusra check karta hai |
| 5 | **Connector (MCP)** | Loop asli tools mein *act* kar sake (PR khole, ticket update kare) — sirf suggest na kare |
| 6 | **Spine (State/Memory)** | Disk par file jo yaad rakhti hai kya hua — **"No spine, no loop"** |

> Yaad rahe: model har run ke baad sab bhool jata hai. Repo (files) yaad rakhti hai.

**Yeh sirf code ke liye nahi hai.** Yeh book khud markdown files ka ek repo hai, aur isi ka har part loop se chalta hai. Sirf **checker** badalta hai: code ke paas honest checkers hain (tests, linters), prose ke paas nahi — isliye writing loop 2 kamzor checks use karta hai: mechanical checks (broken links, missing figures) aur rubric-with-a-bar wala reviewer agent ("Grade this against the rubric. Do not stop below 95").

### 🪜 Checker Ladder — 3 Qisam Ka "Done"

| # | Checker | Kya Hai | Strength |
| :--- | :--- | :--- | :--- |
| 1 | **Passing test** (code) | Test runner/linter decide karta hai, command apne aap ko convince nahi kar sakti | **Proof** |
| 2 | **Mechanical checks** (prose) | Broken links, missing figures, banned words, heading levels | **Partial proof** |
| 3 | **Rubric with a bar** | Reviewer agent grade karta hai, "do not stop below 95" — score ek claim hai, proof nahi | **Claim, proof nahi** |

**Jitna kamzor checker, utna zyada kaam human gate se guzarta hai.** Yeh failure nahi hai — yeh method bata raha hai aapki judgment kahan rehti hai.

---

## ❤️ Part 2 — 4 Heartbeats (Loop kaise start hota hai)

**Ek idea jo sab 4 ke neeche hai:** loop ek single action nahi hai — *"yeh karo, wait karo, phir karo"* hai, isliye kuch to jaaga rehna chahiye beats ke darmiyan agli beat fire karne ke liye. Sawal sirf yeh hai: **woh cheez kahan rehti hai?**

| Heartbeat | Timer Kahan Rehta Hai | Beats Ke Darmiyan Kya Jaaga Rehta Hai |
| --- | --- | --- |
| In-session `/loop` | Session ke andar | Aapka open session (machine, open terminal) |
| Scheduled task/Routine | Bahar, scheduler mein | Scheduler, jo har tick par fresh run launch karta hai |

Chaar tarah ke heartbeat hain — "aap pakde huye ho" se "khud chalta hai" tak:

1. **In-session loop** (`/loop`) — kitchen timer jaisa. Sirf tab tak chalta hai jab tak aapka session/terminal khula hai. Session band = loop band.

   - *Example:* ISS (Space Station) ki location har minute check karna. `/loop show me the location of the ISS every minute` — sirf itna type karo. Terminal band karo, watching mar jati hai — yehi is heartbeat ki definition hai.
   - **3 rungs of "kitna jaaga rehna hai":** In-session `/loop` (terminal band = khatam) → Background session `--bg` (terminal band ke baad bhi chalta hai, lekin machine so jaye to nahi) → Scheduled/Routine (laptop band ho tab bhi chalta hai, cloud par).

2. **Conditional loop / Run-until-done** (`/goal`) — "khana taste karke bataye ke ready hai ya nahi." Timer se nahi, ek **checked condition** se rukta hai. **Fixed-timer loop ko nahi pata kaam khatam hua ya nahi. Conditional loop isliye rukta hai kyunki kaam khatam ho gaya.**

   - Zaroori: agent khud apna kaam approve nahi karta — ek **alag checker** (chota model, Haiku default) decide karta hai "done" hai ya nahi. Checker commands chala nahi sakta, sirf transcript parh sakta hai — isliye worker ko tests khud chalane aur output dikhana zaroori hai.
   - Har loop ko 3 stops chahiye: **success condition**, **limit** (max tries), **no-progress check**.
   - **Ralph loop** — sabse simple well-known run-until-done loop online. Wahi prompt baar-baar chalata hai, ek state file parhta/update karta hai. Sirf 2 stops rakhta hai (success + time cap) — koi stuck-check, skill, ya alag checker nahi. Yeh bareness hi lesson sikhati hai: vague condition wala Ralph loop bhatakta rehta hai jab tak time khatam na ho.
   - **Doom loop** — lambi run apna context junk se bhar leti hai (purana tool output, dead ends), messy context se galat decision, galat decision se aur mess. Defense: har kuch der baad **compact** karo (summary se replace), bare outputs **files mein** rakho (context mein sirf pointer), messy subtasks **subagent** ko do. Context ko **budget** ki tarah treat karo, bucket nahi.

3. **Scheduled (Routine)** — alarm clock jaisa. Laptop band ho tab bhi chalta hai (Anthropic ke servers par). Jaise: "har weekday 9am, overnight CI failures dekho."

   - **Daily cap hai:** launch-time numbers — Pro 5/din, Max 15/din, Team/Enterprise 25/din. Ek-baar wale (one-off) schedules cap mein count nahi hote.
   - **Sirf `claude/` branches par push kar sakta hai** (default) — `main` tak seedha nahi jata, yeh safety hai.

4. **Event-driven** — doorbell jaisa. Kuch nahi hota jab tak koi PR khole ya message aaye — phir turant react karta hai.

   - **3 routes (Claude Code mein):** GitHub event → Routine (GitHub trigger); Chat message → Channel (session already running honi chahiye); Kuch aur (alert, deploy, form) → Routine ka API trigger.
   - **Asal sawal:** "yeh Routine hai?" nahi — **"kaam kis ke computer par chal raha hai?"** Aapki machine band hote hi mar jati hai. Anthropic ke servers ya GitHub ke runners nahi, kyunki woh kabhi aapke the hi nahi.

**Choose karne ka rule:** Task khatam hota hai aur command prove kar sakta hai → **conditional**. Task repeat hota hai → **schedule/event**. Task sirf ek dafa hota hai → **koi loop nahi chahiye**, normal session use karo! (Zyada tar kaam abhi bhi isi row mein hai.)

---

## 🏋️ Part 3 — Loop Kya Karta Hai (The Body)

Yeh 4 cheezein har "beat" mein hoti hain:

- **Isolation (Worktrees):** Parallel agents ek dusre ke kaam ko overwrite na karein — har ek ko apna folder/branch milta hai (`git worktree add`, ya Claude Code mein `--worktree` flag).
- **Knowledge (Skills):** Project ki habits ek `SKILL.md` mein likhi hoti hain, taake har run se dobara explain na karna pare. Loop prompt ko chota rakhti hai — schedule ka prompt sirf ek line ("run the daily-triage skill").
- **Action (Connectors/MCP):** Loop sirf baat nahi karta — real kaam karta hai (PR khole, Slack post kare). **3 rules kyunki yeh loop mein hai:** (1) Kam, focused tools rakho — 100 overlapping tools mein model bhatak jata hai, unattended har beat par ek galat tool pick permanent nuksan karta hai. (2) Writes safe-to-repeat honi chahiyein — retry ek "create customer" dubara chalaye to duplicate customer + double billing. (3) Error messages clear hon — "Permission denied: request repo scope" khud fix ho jata hai, "Error 403" ek beat waste karta hai.
- **Maker-Checker (Subagents):** Sab se important choice! **Jo agent kaam banata hai, wahi khud grade nahi karta.** Ek dusra agent (alag model bhi ho sakta hai) check karta hai — isko **LLM-as-judge** bhi kehte hain. Subagent tokens zyada kharch karta hai — isay wahan use karo jahan real matter kare (jo kaam aapki gair-mojoodgi mein commit hoga), throwaway/read-only chores par skip karo.

### Interlude: Dynamic Workflows (Body Ko Codify Karna)

Claude Code ab poori "beat ki body" (kaam dhoondo, har fix apne checkout mein draft karo, alag agent se grade karwao) ko ek **re-runnable script** ki tarah likh sakta hai — **dynamic workflow**. Aap plain words mein maango ("use a workflow to…"), start karo `ultracode` keyword se, Claude script likhta hai jo kaam kai subagents ko de deta hai (~16 ek waqt mein, 1000 per run cap), background mein chalta hai jabke aapka session free rehta hai. Save karke `/command` bana sakte ho.

> **Sabse asaan galti:** workflow **loop nahi hai**. Ek baar chalta hai, khatam hone par sab bhool jata hai — koi heartbeat, koi spine nahi. **Workflow = engine. Routine/`cron`/`/loop` = key jo engine start karta hai. `progress.md` = agli trip tak information carry karta hai.**

### Interlude: Verification Skills (Checker Ko Codify Karna)

Anthropic ka apna word: **verification loop** — agent apna kaam check karta hai aur fix karne ki koshish karta hai, baar-baar, jab tak check pass na ho jaye (yehi Attempt → Check → Fix → Repeat cycle hai jo Boris Cherny "single most important tip" kehte hain).

**Kaunse checks likhne layak hain:** jo bhi cheez aap **har baar hath se correct karte ho** jab agent kaam khatam kare — likh do. *"Reject any migration that drops a column without a backfill step"* jaisa fixed rule bhi qualify karta hai, chahe woh judgment call na ho — koi general-purpose linter isay kabhi include nahi karega kyunki yeh sirf aapka hai.

**Ek complete verification skill:**
```markdown
# .claude/skills/verify-log-hygiene/SKILL.md
---
name: verify-log-hygiene
description: Check that error logs include the request ID and never
  include the request body. Use when the diff touches error handling.
allowed-tools: [Read, Edit, Grep]
---
Read the error-handling paths in the current diff.
For each log call on an error path, confirm it includes the request ID
and does not pass the request body, headers, or any user-supplied payload.
Report each violation with file:line, then fix it.
```

**Check ke 4 possible ghar, har ghar ek alag heartbeat hai:**

1. **Standalone** — aap khud invoke karo (aap abhi bhi heartbeat hain)
2. **Embedded** — us skill ke end mein add ho jo kaam banati hai (ek line: *"After creating the component, run eslint on it..."*)
3. **Chained** — ek skill dusri ko call kare (`/code-review` → `/simplify` → `/verify` → `/design`) — habit ("main hamesha baad mein check karta hoon") ek contract ban jata hai (skill hamesha check chalati hai)
4. **Har PR par** — Doorbell event heartbeat se, team-wide gate ban jata hai — check "personal infrastructure" se "team infrastructure" ban jati hai

**Graduation rule:** home 4 se shuru mat karo. Signal ke check "ready" hai: aap khud usay har change ke baad chalate paate ho. Tab embed/chain karo. PR-wide gate se pehle wait karo jab tak chain stable na ho — kyunki ek baar team ke PRs guard karne lage, har change us check mein team ko dikhta hai.

---

## 🦴 Part 4 — Spine (Memory Between Runs)

**Sab se zaroori concept jo beginners skip karte hain!**

Model har run ke baad **sab kuch bhool jata hai**. Agar har beat zero se start ho, to loop nahi — bas wahi pehla step baar baar chalta hai.

Do files rakho:

- **Rules file** (`CLAUDE.md` / `AGENTS.md`) — hamesha ki habits, har run start mein padhi jati hai (short rakhna, kyunki har run par cost hoti hai)
- **Progress file** (`progress.md`) — jo hua uska record: kya done hua, kya baaki hai. Har run **shuru mein padhta hai, end mein update karta hai**.

```markdown
<!-- progress.md — loop ki memory runs ke darmiyan -->

## Done
- 2026-06-22: fixed flaky test in test/auth (retry on token refresh)

## In progress
- Dependency audit: 3 of 7 advisories patched; lodash bump blocked by an API change

## Open / needs a human
- CVE-2026-xxxx in image lib — the fix changes the output format, escalating to a maintainer
```

**Intern ki diary wali example:** Naye intern ko diary do. Front mein — sabak jo mila (mistakes se seekha), roz padho. Back mein — kal kya kiya, kahan chhoda, roz likho. Bina diary ke intern (aur loop) roz wahi galtiyan repeat karega.

**Industry bhi isi par pahunchi:** Anthropic ne ek saal alag rastay try kiye — pehle sirf `CLAUDE.md`, phir in-session memory tools, phir Skills. **Aakhri jawab sabse simple nikla: memory ko plain file system ki tarah model karo** — markdown files folders mein, `grep`/shell se search karo, koi special memory API nahi. Yehi spine hai, exactly jaisa yeh course sikhata hai.

### 🌙 Dreaming — Loop Jo Loop Ko Improve Karta Hai

Rules file mein lesson likhna ek naam rakhta hai: **hill-climbing loop** — iska output kaam nahi, **system mein improvements** hai. **Dreaming** iski managed/out-of-band version hai (Anthropic Applied AI team):

1. Memory store + recent run transcripts collect karo (weekly heartbeat, daily nahi — patterns cross-session dekhne ke liye batch chahiye)
2. Orchestrator transcripts ko subagents mein baant deta hai
3. Patterns dhoondo jo repeat hote hain (same failing tool call, same missing knowledge)
4. Memory store mein **changes propose** karo, evidence ke sath (kaunse runs, kitni baar)
5. **Human accept/reject karta hai** har change ko lagne se pehle

Yeh school ki tarah hai: students (working agents) kaam karte hain, head teacher (dreaming pass) sab marked papers parhta hai, dekhta hai poori class ek hi sawal fail kar rahi hai, curriculum fix karta hai.

> **2 tareeqe dreaming galat ja sakti hai:**
> - **Attack launder kar sakti hai** — "memory poisoning": ek run ke input mein plant ki gayi instruction memory mein likhi jati hai aur baad ke har run ko steer karti hai. Defense: har proposal evidence cite kare, human gate hamesha rahe.
> - **Jo maintain karti hai usay erode kar sakti hai** — **brevity bias** (specific point general point mein simplify ho jata hai) aur **context collapse** (har rewrite lossy copy hoti hai). Defense: **chote diffs, kabhi poore rewrites nahi**. Memory file mein kabhi relative date mat likho ("kal" 6 hafte baad meaningless hai) — absolute dates likho.

**Claude Code ka `Auto Dream`** (research preview) yehi karta hai apne notes ke liye — duplicates merge, purani facts delete jo naye kaam ne prove ki galat thin. Sirf memory files likh sakta hai, kabhi code nahi. **`CLAUDE.md` sirf aapka hai** — jo rule kabhi touch na ho, wahan likho.

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

> **Poora runnable code example (SKILL.md, reviewer.md, Routine/GitHub Actions wiring, real morning run) is file ke [Loop-Engineering-Final-Prep.md](./Loop-Engineering-Final-Prep.md) mein hai — direct book se liya gaya.**

---

## 👨‍💻 Part 6 — Insaani Control Kaise Rakhein (Sabse Important Part!)

### 3 Feedback Loops (Ek Dusre Ke Andar)

1. **Coding loop** (minutes) — agent likhta hai, test karta hai, fix karta hai
2. **Feedback loop** (hours) — aap try karte hain, decide karte hain kya change karna hai — **spec** aur **evals** yahan kaam karte hain
3. **Outside loop** (days) — real users use karte hain

Agent teenon khud nahi chala sakta — kyunki **aapko woh cheezein pata hain jo agent ko nahi** (Andrew Ng isko **"context advantage"** kehte hain: kaun use karega, unhe asal mein kya chahiye, "acha" kaisa feel karta hai). Jab tak aap kuch aisa jante ho jo agent nahi janta, aap loop mein rehte ho usay batane ke liye. Machine fast loop chalata hai; aap decide karte hain **kya banana hai** aur **kaun zimmedar hai**.

### Token Cost — Asli Limit

- Har loop ko **cap karo** (max tries/time/spend)
- Sahi model choose karo (mushkil kaam ke liye strong, aasan ke liye cheap) — Claude Code mein `/effort` ya `CLAUDE_CODE_EFFORT_LEVEL` se **effort level** ko bhi beat se match karo
- Loop ko kam frequency par chalao — har 5 min ki jagah har ghante, cost mein bohat farq aata hai!
- Loop prompt + rules file **chota** rakho — har beat par pay karte ho

**Real numbers (example):** ek beat (maker + checker) ~40,000 tokens parhe, ~6,000 likhe. Sonnet ki standard price ($3/million input, $15/million output) par yeh **~$0.20 per beat** hai. 5 beats/din, 20-din month = **~$20/month**. **Wahi loop har 5 minute chale (din-raat)** to 100+ guna zyada beats — **month mein $1,000+ ho sakta hai**, chahe har beat wahi kaam kare. **Frequency, command ka naam nahi, isay drive karti hai.**

**OpenCode mein model bhi ek cost lever hai:** sasta model beat ki cost kam kar sakta hai, lekin kamzor maker zyada failed attempts de sakta hai jo savings kha jate hain. Pattern: **cheap maker, trustworthy checker.**

> **Ek achi spine bhi cost lever hai:** achi memory wala agent doosri baar kaam achi tarah karta hai (pehli attempt ka lesson pehle se disk par hai) — behtar first attempts = kam retries = kam tokens.

### Human In / On / Out of the Loop (Industry Ke Naam)

| Term | Matlab | Yahan Kahan Bana |
| :---- | :---- | :---- |
| **Human IN the loop** | Har action se pehle insaan approve karta hai — slow, zyada control | Turn-by-turn prompting, plan mode, merge par human gate |
| **Human ON the loop** | System khud chalta hai, insaan dekhta hai aur rok sakta hai — fast | Routine `claude/` branches par push kare, aap subah review karo |
| **Human OUT of the loop** | Koi dekh hi nahi raha — **yeh kabhi acceptable nahi** | Nowhere, jaan-boojh kar — yeh third option nahi, failure mode hai |

**3 baatein is table se:**
1. Concept 1 ka mindset shift ab naam rakhta hai: prompting = human **IN**, loop engineering aapko **ON** the loop move karti hai.
2. **Achi loop ek ya doosri nahi hoti — mix hoti hai, har action ke liye set.** Morning-triage loop safe fixes ke liye on-the-loop, risky cheez ke liye wapis in-the-loop. Checker ladder mix decide karti hai: **passing test autonomy kamata hai, rubric score nahi.**
3. **"Out of the loop" wahi hai jahan AI Gravity khinchti hai.** Koi jaan-boojh kar out-of-the-loop design nahi karta — drift se hota hai. Diffs parhna band karo, green checkmarks trust karo, weekly read skip karo — aur on-the-loop chupke se out-of-the-loop ban jata hai.

**Rule:** Jahan galat move mehngi aur wapis lena mushkil ho, wahan insaan rakho. Baqi jagah loop chalne do.

### Concept 15: Apne Project Ki Samajh Mat Khona!

Do log same loop bana sakte hain — ek use kar ke aur tez ho jata hai (kyunki gehri samajh rakhta hai), dusra use kar ke samajhna hi chhod deta hai. **Loop yeh farq nahi bata sakta — sirf aap bata sakte hain.**

> "AI Gravity" (MIT Sloan ke Eric So) — yeh force hamesha khinchta hai ke AI se zyada se zyada kaam karwao. Loop se yeh pull aur strong ho jata hai kyunki woh so'te waqt bhi chalta hai. Chorho isay, aur **Intent** "sirf chalta rakho" tak simplify ho jati hai, **Accountability** green checkmarks trust karne tak.

### Observability — Jab Unattended Loop Fail Ho

- **Output wahan bhejo jahan aap dekhoge:** log file, Slack/Discord (Channels), band terminal nahi
- **Har run par ek line likho, fail hone par bhi** — silent failure sab se bura hai
- **Runs replayable rakho** — `opencode run --format json`, `opencode export`, Routine ka run history
- **Limit par loudly fail ho** — "needs a human" note chorho, chup mat ruko
- **Overnight se pehle prove karo:** cadence (hourly-watched pehle, phir nightly-unattended) aur capability (report-only pehle, phir fixes-behind-gate, phir unattended action) dono axes par grow karo

### After Loops: Graph Engineering

Ek thread jaan-boojh kar khula chorha gaya: jab aap **ek se zyada** loops chalate ho, unhe **wiring** chahiye — kaun kisay feed karta hai, kaun kisay check karta hai, shared memory kahan rehti hai. Yeh **Graph Engineering** course cover karta hai (Harness Engineering ke baad). Yaad rakho: **"a graph is loops, composed."** Loops hatao, graph khaali box hai.

---

## 🐕 Dogfooding — Yeh Book Khud Apne Loops Use Karti Hai

**2 loops jo poori book chalate hain, roz, production mein:**

1. **Feedback loop** — readers ke comments automatically sort karta hai. Heartbeat: 2 cloud Routines (triage + weekly fix-drafting). Spine: live database + GitHub issues. Sirf zaroori cheezein (blocked reader, genuine content error) insaan tak jati hain — baqi (ratings, thank-yous, duplicates) khud close hoti hain. Pehli runs mein hazaron notes ka backlog saaf hua.
2. **What's New loop** — book mein daily changes ka summary khud likhta hai. Heartbeat: daily GitHub Actions (OpenCode se, poori book ka **doosra** tool). Spine: chota state file. **Koi human approval nahi.**

**Rule jo yahan se seekha:** Feedback loop ship se pehle rukta hai; What's New kisi ke liye nahi rukta. Farq **wrong-move ki cost** hai — ek bad edit mehnga hai wapis lena, ek changelog line ek `revert` door hai. **Jahan galti mehngi ho, wahan human gate rakho. Baqi jagah chhod do.**

---

## 🚀 8 Practice Projects + 3 Routine Drills + 1 Capstone

| # | Project | Difficulty | Kya Sikhata Hai |
| --- | --- | --- | --- |
| 1 | Watch loop (in-session) | Easy | Concept 4 |
| 2 | Tests pass karo, phir ruko | Easy-Medium | Concept 5, 11 |
| 3 | Morning brief with memory | Medium | Concept 6, 12 (spine) |
| 4 | Fix loop with real checker | Medium-Hard | Concept 8, 9, 11 |
| 5 | Codify the body (workflow) | Medium-Hard | Dynamic workflows interlude |
| 6 | Doorbell loop | Medium | Concept 7, 10 |
| 7 | Break it on purpose | Medium | Observability, cost |
| 8 | **Capstone:** apni real daily loop | Capstone | Sab 6 parts, 1 hafta unattended |
| 9 | Routine free mein rehearse karo | Easy | Appendix A1, A3, A5 |
| 10 | Secrets drill | Easy-Medium | Appendix A4 |
| 11 | Two-routine gate banao | Medium-Hard | Appendix A3, A4, A6 |
| 12 | **Capstone:** dreaming loop banao | Capstone | Concept 12 (dreaming), 11, 6 |

---

## 📌 Sabse Zaroori Baat (Yaad Rakhne Wali)

> **Do layers hain is course mein — ek yaad rakhni hai, doosri sirf lookup karni hai:**

> - **Lasting layer (yaad rakho):** Loop ki shape (heartbeat, 5 working parts, spine), maker-checker split, checker ladder, aur intent+accountability ka concept.
> - **Mechanical layer (lookup karo):** Commands, flags, model names, daily caps — yeh har hafte change hote hain, docs check karte rehna.

---

## 📝 Quick Glossary

| Term | Aasan Matlab |
| :---- | :---- |
| Agent | AI system jo tools use kar sakta hai, sirf jawab nahi deta |
| Loop | System jo kaam start karta hai, check karta hai, yaad rakhta hai, repeat karta hai |
| Beat | Loop ka ek pura run |
| Heartbeat | Woh schedule/event jo beat start karta hai |
| Unattended | Bina kisi ke dekhe chalna |
| Stopping condition | Testable rule jo bataye kaam done hai |
| Maker-checker | Ek banata hai, dusra check karta hai (LLM-as-judge) |
| Worktree | Alag working folder/branch |
| Skill | Saved project instructions, dobara use hoti hain |
| Connector/MCP | Outside system (GitHub, Slack, database) se connection |
| Spine | Saved state jo ek beat se dusre beat tak memory le jati hai |
| Human gate | Woh point jahan insaan approve karta hai risky kaam se pehle |
| Routine | Claude Code ka cloud automation |
| Doom loop | Messy context → galat decision → aur mess |
| Dreaming | Out-of-band loop jo memory store improve karti hai, evidence + human gate ke sath |
| AI Gravity | Force jo AI se zyada se zyada kaam karwane khinchti hai |
| Context advantage | Andrew Ng ka term — aap kuch jante ho jo agent nahi janta |
| Checker ladder | Proof (test) → partial proof (mechanical check) → claim (rubric score) |

---

## 🔗 System of Record Ka Connection

Loop engineering ka **spine** (`progress.md` + `CLAUDE.md`) khud loop ke liye ek chota **system of record** hai — yeh authoritative jagah hai jahan "kya hua" likha jata hai, model ke bharose se bahar. Jab loop apne **Connectors (MCP)** se real systems of record (GitHub issues, Linear board, Slack) mein likhta hai, yeh Agent Factory book ke Digital FTE/Connector-Native Apps courses wale "system of record" invariant se seedha jorta hai: authoritative data agent ke context window ke bahar, ek clean interface (MCP) se reach hota hai. **Poora detail [Loop-Engineering-Final-Prep.md](./Loop-Engineering-Final-Prep.md) mein hai.**

---

*Yeh summary poore course (4 Layers, Checker Ladder, 6 Parts, Dynamic Workflows, Verification Skills, Spine, Dreaming, Part 5 Real Loop, Part 6 Human Control, Dogfooding, 12 Practice Projects, Routines Appendix, Graph Engineering) ka overview hai. Har concept ka poora, code-ke-sath breakdown [Loop-Engineering-Final-Prep.md](./Loop-Engineering-Final-Prep.md) mein hai.*
