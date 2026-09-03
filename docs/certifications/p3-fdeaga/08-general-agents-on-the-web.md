# 08 — General Agents on the Web

*Source: `general-agents-web-crash-course` (Zia Tutor AI, corpus gen 62). Deep notes:
[`docs/general-agents-web/`](../../general-agents-web/README.md). **CCAO-F overlap:** yeh module
associate cert ki reading list mein bhi hai.*

---

## A. The Shift — Chat Box vs Agent Surface

- 6 courses tak sirf chat tab: **har turn tumse shuru hota tha**. Plain chat ki limit: **type karna
  band → conversation ruk jati hai.**
- **July 2026:** Anthropic (**Claude Cowork** on claude.ai) aur OpenAI (**ChatGPT Work** on
  chatgpt.com, GPT-5.6) ne agent surfaces browser mein la diye — chat box ke bagal mein, usi address
  par. Session company ke servers par chalti hai; tab band karo, plane mein baitho — **kaam chalta
  rehta hai**. Decision jo sirf tum le sakte ho → sawal tumhare phone par.

> **Test jo har marketing ko cut through karta hai:**
> **"Agar main type karna band kar doon, kya kaam ruk jayega?"** — Chat box: **haan**. Agent surface:
> **nahi**.

- **Deeper:** plain chat turn = **synchronous** (tum wait, jawab, wapas tumhara wait). Agent run =
  **delegated** (ek dafa shuru, outcome ki taraf badhta rehta hai, tumhare agle turn ki zaroorat
  nahi).

## B. Remote Session — Tab Ek Window Hai, Runtime Nahi

Agent 2 jagah reh sakta hai: **tumhari machine par** (desktop apps, terminals — app hi runtime, laptop
band = kaam ruka) ya **vendor ke servers par** (yeh course — **browser tab ek window hai, machine
nahi**).

**3 consequences:** tab band karo → kaam chalta rehta hai · phone se session kholo → **wahi session**
(copy nahi) · scheduled task band tab se bhi fire hoti hai.

**Ehtiyat:** remote session sirf wahi reach karti hai jo vendor ki machines reach karti hain
(connectors, task filesystem, platform files) — **tumhari local hard drive / desktop apps / logged-in
browser NAHI** (uske liye local bridge — agli courses).

## C. 2 Vendors, Ek Shape — Agent Surface Ke 6 Parts

| ChatGPT Work | Book | Matlab |
| --- | --- | --- |
| Scheduled Tasks | **Heartbeat** | kya bina tumhare kaam shuru karta hai (once, schedule, event, monitor) |
| Plugin Directory | **Connectors** | real services tak permission-scoped reach |
| Outcome-based execution | **Run-until-done loop** | outcome do, steps mein pohanchta hai |
| Cloud-synced sessions | **State spine** | devices/runs ke darmiyan yaad rehne wali memory |
| Approval prompts (mobile) | **Human gate** | risky decisions phone par insaan tak |
| Cloud execution environment | **Body** | jahan kaam asal mein hota hai — docs, sheets, decks |

> **Sabse zaroori idea:** naam badalte rahenge — **shape ek dafa seekho, har naya agent product
> 30-minute read ban jata hai, naya subject nahi.**

- **Farq kahan:** model (Claude vs GPT-5.6), plan structure, connector naam. **Deeper:** OpenAI ka
  coding agent (Codex) **usi app** mein; Anthropic ka Claude Code **poori tarah alag surface**.
- **Boundary sab par:** regulated data (PHI, privileged matter, financial records) **kisi bhi web
  surface** ke liye target user **nahi** jab tak compliance likhit mein na kahe — working files +
  platform storage **vendor ki custody mein hoti hain, by definition**.

## D. Account Spine

- **Continuity ek feature** — sessions + files account mein save; kisi bhi device se wahi kaam.
  Vendor ne banaya, kisi ko hire nahi karna.
- **Keemat:** spine **vendor ki custody + format** mein — dependency (plan, product ka zinda rehna,
  vendor ke rules).
- **3 aadatein:** sessions ko **work products ki tarah naam do** ("Acme renewal brief" NA "Quick
  question") · **ek session, ek workstream** · dead cheezein prune karo.

## E. 3 File Tiers — Course Ka Sabse Zaroori Concept

| Tier | Kya | Status |
| --- | --- | --- |
| **1. Task filesystem** | remote session ka temporary scratch space; kaam khatam → cleanup | **already lost** (tier ki definition, bug nahi) — kal chahiye kisi cheez ka ghar kabhi nahi |
| **2. Platform storage** | files permanently account mein, vendor ke platform par | **aaj safe, kal hostage** — safe kyunki bachti, hostage kyunki sirf wahin, kisi aur ki login ke peeche |
| **3. The Exit** | file platform se **nikal kar** jahan **tum control** karte ho — connector save (Drive), email, download, local write, repo commit | **tumhari hai** — sirf yeh tier deliverable ko tumhare system of record mein daalta hai |

> **Poori course ki line:** **"Finished work exits the platform. Everything else may stay."**

- Worked example (Ayesha invoicing): draft numbers → Tier 1; template → Tier 2; **finished invoice PDF
  → Tier 3, DO dafa** (firm ki Drive + client ko email) — kyunki koi din poochega "March ka invoice
  kahan?" aur jawab **firm ke records** hone chahiyen.
- Har brief ke aakhir mein: *"End by listing every file you created and where each one landed:
  temporary working space, platform storage, or a system I control."*

## F. Connectors on Web — Reach + Exit Door Ek Sath

- Definition wahi (permission-scoped, MCP). **Web par connectors DOUBLE weight uthate hain** — reach
  **aur** Tier 3 ka **main automated exit door**.
- **Read scope ≠ send scope** — read access = summarize; write/send = **alag, bara grant** (bheji hui
  message wapas nahi).
- **Untrusted content careful mode** — kisi aur ki likhi content mein hidden instructions (prompt
  injection) → jab task aisi content touch kare jo tumne nahi likhi, **ask-before-acting mode**.

## G. The Gate In Your Pocket

- Human gate wahi — jo badalta hai: **tumhe kahan milta hai**. Web par kaam lunch/meeting/neend mein
  chalta hai → **approval phone par**.
- **Phone = gate, workbench nahi** — plan review, step approve, redirect, task rok. Design work **bare
  screen** par.
- **"Gate move nahi hui. Doorbell ko move hona pada."** Ek dekhi na jane wali escalation = ek delayed
  decision → jo default se li gayi decision ban jati hai.
- **Non-negotiable aadat:** gate ko jaan-boojh kar ek dafa bajao (chhoti task jo ek approval mange,
  computer se poori tarah chale jao, confirm notification phone par aai). **Ek alarm jo tumne kabhi
  nahi suna, ek afwah hai.**

## H. Delegation Loop — Brief · Plan · Approve · Review (4 lamhे)

| Step | Kya |
| --- | --- |
| **1. Brief** | assignment aise describe karo jaise smart naye colleague ko jo tumhara context nahi jaanta — outcome, constraints, audience, wajah. ("Ye 3 files parho, har deadline flag karo, ek page ka brief: direct tone, deadlines pehle, koi intro nahi" — NA "ye PDF summarize karo") |
| **2. Plan** | *"Lay out your plan first, and pause for my approval before doing anything."* — **web par tum chale jaoge → plan usually tumhara AKELA intercept intent aur finished work ke darmiyan** |
| **3. Approve / redirect** | 4 checks (2 min): **Scope** (sirf named touch?) · **Order** (verify se pehle action?) · **Reach** (koi connector/send jo nahi manga?) · **Assumptions** (format/audience jo nahi bataya?). Galat → **ek sentence se redirect**, dobara shuru nahi |
| **4. Review** | 3 lines: "ask 1-2 clarifying questions" + "sources contradict → flag in deliverable, do not silently pick" + "list every file + where it landed" |

- **Anti-pattern:** surface ko "superpowers wale chat box" ki tarah treat karna — ek line ka prompt
  unattended multi-step ke liye. **Vague brief mein jitna khali, agent utna khud decide karta hai —
  akele.**
- **Plan sabse zaroori step** — theek karna 1 min, finished galat kaam theek karna poori shaam.

## I. Scheduled Tasks — 4 Jawab (order mein likhe)

1. **Kya karna hai?** standing brief — **gairhaziri survive kare, khali case samet** ("agar is hafte
   kuch naya nahi, ek line note produce karo" — chup hafte aur chup failure ka farq).
2. **Kya touch kar sakta hai?** files/platform storage, naam se.
3. **Kya reach kar sakta hai?** connectors listed — **permissions hain, suggestions nahi** (koi mail
   connector nahi → koi mail nahi, chahe brief kuch bhi kahe).
4. **Kab shuru hota hai?** cadence — *"Monday 8am"* = **around** Monday 8am (stagger, kabhi slip).

**3 rules pehli schedule se pehle:** jise trust nahi karte chhorne ke liye woh mat schedule karo
(pehle haath se, watched, kai baar) · metered math likh kar (runs/ghante ki budget, collision se
pehle count) · **complete hui run ≠ successful task** (success signal task ke apne output mein banao).

> **Boundary:** is se **reporting** schedule bana sakte ho (parhna, synthesize, brief, sahi tier).
> **Acting** schedule (bhejta, file karta, update karta, decide karta cadence par) abhi safely nahi —
> usay checker + machine-verifiable stopping condition + state file chahiye = **Loop Engineering**.

## J. Choosing — Jo Kaam Touch Kare Uske Hisaab Se

| Kaam ko chahiye | Surface | Course |
| --- | --- | --- |
| connector-and-document, cross-device continuity, koi install nahi | **Web** | yeh course |
| kaam jo machine band par bhi chale (repo work) | **Web** (cloud Routine) | Loop Engineering |
| local files, desktop apps, logged-in browser | **Desktop** | Cowork & OpenWork |
| code, repositories, command line | **Coding agents** | Agentic Coding |
| regulated data (PHI, privileged, financial) | **Koi nahi, abhi** — pehle compliance se likhit jawab | Cowork course |

- Regulated data: sawal *"ye surface careful hai?"* nahi — *"ye data is custody mein rehne ki ijazat
  hai?"* Sirf compliance, **likhit mein**.
- Mix ko mess se rokने wala rule: **jaano har deliverable kaunse tier mein utri.**

## K. Open Path — Koi Vendor Cloud Nahi

Dono tabs (Cowork web, ChatGPT Work) **closed products** hain. Open paths:
- **OpenWork remote/shared workspaces** — self-hosted worker (URL + access token) ya org ke shared
  cloud workers. Machine jo kaam karti hai woh tum dekh rahe nahi — **lekin infrastructure tum/org
  control karti hai**.
- **OpenCode apna scheduler** — repo-attached, cron ya GitHub Actions. Koi vendor cloud, koi plan
  tiers nahi.

> **Trade:** **Companies tumhe spine bech dete hain. Open path tumhe banana parta hai.** Vendor
> surface = furnished office (sab pehle din se kaam karta, unki building). Open path = khali kamra jo
> tum furnish karte ho — zyada mehnat, badle mein **custody** (tumhare control ki machines par data) +
> **choice** (kaunsa model tumhare prompts dekhta hai). **"Bina engineer ke, yehi asal decision hai,
> software nahi."**

## L. Ye Surface Kya NAHI Kar Sakti

- **Surface kaam behtar nahi banati** — remote session weak brief ko **unattended** bana deti hai,
  **behtar nahi**. Har quality lever tumhari taraf: brief, plan review (akela intercept), tier
  decision, gate test, walked-before-scheduled rule.
- **Surface hafton purani, metered, staged, vendor-shaped** — button names/product names sabse tezi
  se purana hone wala material. **Lasting layer:** stop-typing test · window-not-runtime architecture
  · 3 tiers ki 1-line discipline · 6-part reading lens · 4-step loop · schedule ke 4 jawab.

> **Ek discipline poore churn se bachati hai:** **kuch bhi zaroori sirf platform par nahi rehta** —
> Tier 3, hamesha, kisi bhi cheez ke liye jise khona bura lagega.
> **Closing:** chat box = jahan design karte ho; agent surface = jahan woh chalta hai. **Shape seekho.
> Address dobara badlega.**

---

## Ek-Line Revision (M8)

> Test: **"type karna band → kaam ruk jayega?"** chat=haan, agent surface=nahi · tab = window not
> runtime · 6 parts: heartbeat/connectors/run-until-done/state spine/human gate/body — **shape ek
> dafa** · **3 tiers: task fs (lost) / platform storage (safe but hostage) / the exit (yours)** —
> "**finished work exits the platform**" · connectors on web = reach + exit door; read ≠ send · gate
> ab phone par — "doorbell ko move hona pada", ek dafa test karo · delegation: brief→**plan (akela
> intercept)**→approve (scope/order/reach/assumptions)→review · schedule 4 jawab, gairhaziri survive ·
> reporting OK, **acting = Loop Engineering** · regulated data = koi surface nahi, compliance likhit ·
> open path = spine khud banao (custody + choice).

---

## MCQ Practice (jawab neeche)

1. Chat box aur agent surface ka test:
   a) Speed b) "Agar main type karna band kar doon, kya kaam ruk jayega?" (chat=haan, surface=nahi)
   c) Cost d) Model

2. Remote session mein "tab" kya hai?
   a) Runtime b) Window hai, machine nahi — kaam vendor ke servers par c) Sandbox d) Spine

3. Remote session kya reach NAHI kar sakti?
   a) Connectors b) Task filesystem c) Tumhari local hard drive / logged-in browser d) Platform files

4. Agent surface ke 6 parts mein "run-until-done loop" ChatGPT Work mein kya kehlata hai?
   a) Scheduled Tasks b) Plugin Directory c) Outcome-based execution d) Cloud-synced sessions

5. 3 file tiers mein "already lost" kaunsa hai?
   a) Tier 1 (task filesystem) — tier ki definition, bug nahi b) Tier 2 c) Tier 3 d) Koi nahi

6. Poori course ki line:
   a) Sab kuch platform par rakho b) "Finished work exits the platform. Everything else may stay."
   c) Kuch save mat karo d) Sirf Tier 1 use karo

7. Tier 2 (platform storage) ki honest characterization:
   a) Tumhari hai b) Aaj safe, kal hostage — sirf wahin bachti, kisi aur ki login ke peeche
   c) Already lost d) System of record

8. Web par connector ka "double weight":
   a) 2x cost b) Reach AUR Tier 3 ka main automated exit door c) 2 permissions d) 2 servers

9. Mail connector ko read access dena kya deta hai?
   a) Send bhi b) Sirf summarize — write/send alag, bara grant hai c) Nothing d) Full access

10. Web par human gate kahan pohanchta hai?
    a) Screen par b) Phone par (kaam lunch/meeting/neend mein chalta hai) c) Email d) Terminal

11. "Gate move nahi hui. ___ ko move hona pada."
    a) Model b) Doorbell — dekhi na jane wali escalation = delayed decision c) Spine d) Body

12. Delegation loop mein sabse zaroori step (web par):
    a) Brief b) Plan — web par tum chale jaoge, plan tumhara akela intercept c) Approve d) Review

13. Plan approve karte waqt 4 checks:
    a) Speed, cost, model, tool b) Scope, order, reach, assumptions c) Start, middle, end, done
    d) Corpus, map, reflexes

14. Scheduled task ka brief kya survive karna chahiye?
    a) Model change b) Tumhari gairhaziri — khali case samet ("kuch naya nahi → ek line note")
    c) Network outage d) Plan upgrade

15. Scheduled task se abhi safely kya bana sakte ho?
    a) Acting schedule (bhejta, file karta) b) Reporting schedule (parhna, synthesize, brief) —
    acting = Loop Engineering c) Dono d) Kuch nahi

16. Regulated data (PHI, privileged) web surface par:
    a) Careful mode mein OK b) Koi web surface target user nahi jab tak compliance likhit mein na kahe
    — custody ka sawal hai c) Tier 3 mein OK d) Encrypt karke OK

17. Open path ka core trade:
    a) Speed vs cost b) Companies spine bech dete hain; open path tumhe banana parta hai — badle mein
    custody + choice c) Model quality d) UI

18. "Surface kaam behtar nahi banati" ka matlab:
    a) Surface bekaar hai b) Remote session weak brief ko unattended bana deti hai, behtar nahi — har
    quality lever tumhari taraf c) Chat box behtar hai d) Model matter nahi karta

### Jawab Key

1‑b · 2‑b · 3‑c · 4‑c · 5‑a · 6‑b · 7‑b · 8‑b · 9‑b · 10‑b · 11‑b · 12‑b · 13‑b · 14‑b · 15‑b · 16‑b
· 17‑b · 18‑b

---
[⬅ 07 — Leaving the Laptop](07-leaving-the-laptop.md) · [Agla: Full Mock Quiz ➡](quiz.md)
