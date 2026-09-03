# 04 — Loop Engineering

*Source: `loop-engineering-crash-course` (Zia Tutor AI, corpus gen 62). Deep notes (16 files + 61-Q
test + 12 projects): [`docs/loop-engineering/`](../../loop-engineering/README.md) — exam se pehle
uska [`15-test-your-understanding.md`](../../loop-engineering/15-test-your-understanding.md) zaroor
chala lo.*

---

## A. Prompting vs Looping

| Prompting | Looping |
| --- | --- |
| Har turn **tum** start karte ho | **Schedule ya event** har turn start karta hai |
| Tum output parh kar decide karte ho | Ek **checker** output check karta hai, loop decide karta hai |
| Type karna band → kaam ruk jaata hai | Tum sote waqt bhi chalta hai |
| Ek task, ek session, poori tawajjo | Kai chhote runs, zyadatar unattended, tawajjo **sirf gate par** |

- Loop beech ke steps sambhalta hai. **Do sirey hamesha insaan ke:** **Intent** (itna saaf ke result
  check ho sake) aur **Accountability** (jo ship hota hai uski zimmedari).
- **Loop prompting se asaan nahi — MUSHKIL hai** (khud chalne wala loop khud galtiyan bhi kar sakta
  hai). Faida: ek achi loop bana lo, wahi kaam baar-baar khud karti hai.

## B. Chhota Loop vs Bara Loop

| | Chhota (inner) loop | Bara (outer) loop — **yeh course** |
| --- | --- | --- |
| Kya | model ko context bhejo → tool → result → repeat jab tak model khud na kahe "done" | "manager" — decide kaam konsa, kab start, kaise grade, kal ke liye kya yaad |
| Masla | **sirf model khud decide karta hai kaam mukammal — koi bahar se check nahi** | — |
| Rishta | chhote loop ka poora chakkar = bare loop ka sirf **ek "beat"** | — |

**4 layers (har ek tak ~1 saal):** Prompt eng → Context eng → Harness eng (chhota loop yahan) →
**Loop eng** (bara cycle). Har layer alag ghalti rokti hai — koi prompt "missing checker" ya
"schedule jo abhi bhi tum ho" theek nahi kar sakta.

## C. Loop Ke 6 Parts (Anatomy) — **5 working + 1 memory**

| # | Part | Job | Na ho to |
| --- | --- | --- | --- |
| 1 | **Heartbeat** | schedule/event jo loop start kare. Ek firing = **"beat"** | ek run hai, loop nahi |
| 2 | **Worktree** | isolation — 2 agents ek dusre ki file overwrite na karein | collision |
| 3 | **Skill** | project knowledge ek baar `SKILL.md` mein — har run zero se nahi | tokens waste, ghaltiyan |
| 4 | **Subagents (maker-checker)** | jo likhta hai woh **apna kaam khud approve nahi karta** — doosra agent grade karta hai (LLM-as-judge) | model khud ko aasani se pass kar deta hai |
| 5 | **Connector (MCP)** | loop **act** kare — PR khole, ticket update, Slack post | loop sirf **baat** kar sakta hai |
| 6 | **Spine (state/memory)** | disk par file (`progress.md`, `CLAUDE.md`/`AGENTS.md`) — kya hua, aage kya. **No spine, no loop** | loop apna **pehla step hamesha repeat** karega |

> **Exam classic:** "Loop har subah chalta hai lekin kal yaad nahi rakhta — kaunsa part missing?" →
> **Spine.** Model runs ke darmiyan sab bhool jaata hai.

## D. Heartbeats — 4 Kism

| Heartbeat | Analogy | Timer kahan | Session band hone par? | Laptop soye par? |
| --- | --- | --- | --- | --- |
| **In-session** | kitchen timer | tumhari open session | ❌ ruk jaata hai | ❌ |
| **Conditional (run-until-done)** | "jab tak taster na kahe ready" | ek checker decide karta hai | — | — |
| **Scheduled** | alarm clock | scheduler (cron / cloud) | ✅ | ✅ (cloud) |
| **Event-driven** | doorbell | event catcher (Routine/Channel) | ✅ | ✅ |

**3 rungs (kitna "awake"):** in-session `/loop` (terminal band → mar jaata hai) → background session
`--bg` (terminal band OK, machine on chahiye) → **Scheduled/Routine** (cloud, sab chalta hai).

### Conditional loop ke 3 zaroori stops

| Stop | Kya | Na ho to |
| --- | --- | --- |
| **Success condition** | loop ko kaise pata kaam khatam — aisi likho jo **command se prove** ho ("tests pass, lint clean", NA "code achha hai") | "done" define hi nahi |
| **Limit** | max tries / minutes / spend | impossible goal poora token budget kha jaata hai |
| **No-progress check** | same mistake baar-baar → ruk jao | poori limit ek hi ghalti dohrane mein |

- **Ralph loop** = simplest famous run-until-done — same prompt baar-baar, ek state file
  parhta/update. Sirf 2 stops (success + time cap), na stuck-check na separate checker → vague
  condition wala Ralph loop time cap tak bhatakta hai.
- **`/goal` (Claude Code):** har turn ke baad chhota alag model (default Haiku) transcript parh kar
  poochta "done?". Checker **khud commands nahi chala sakta** — sirf dikhta output. Isliye
  condition **command-provable** ho, aur `show me both` jaisa **visible evidence** maango.

### Routine ke 4 blanks

**Prompt** (kya + rules + "done") · **Repos** (kin repos) · **Connectors** (Slack/email...) ·
**Trigger** (schedule / API / GitHub event).

- **Daily cap** (launch: 5 Pro / 15 Max / 25 Team-Enterprise per din) — Routine cap par **chup-chaap
  ruk** sakti hai; arithmetic pehle karo.
- Default: **sirf `claude/` branches par push** — `main` par seedha nahi (safety, hurdle nahi).

## E. Body — Loop Har Beat Par Kya Karta Hai

- **Worktree (isolation)** — Claude Code `--worktree` flag / subagent `isolation: worktree`; OpenCode
  git worktrees.
- **Skill (knowledge)** — jo bhi har run dobara explain karte, skill mein. Loop prompt ek line rakho:
  *"run the daily-triage skill"*.
- **Connector — loop mein 3 zaroori baatein** (loop tools khud chunta hai, koi dekh nahi raha):
  1. **Kam, focused tools > bohot overlapping tools** — agar human engineer confidently na keh sake
     konsa tool fit hai, agent bhi nahi keh sakta.
  2. **Writes idempotent hon** — retry par wahi write dobara → duplicate record. "update-or-create" >
     blind "create".
  3. **Error messages agla step batayen** — error hi agle beat ka input hai. *"Permission denied:
     request the repo scope"* khud fix ho jaata hai; *"Error 403"* ek beat waste.
- **Maker-checker (subagents)** — maker apna kaam approve nahi kar sakta. Checker ko apna **model** do
  (sasta, read-only), instructions: "PASS ya FAIL with reasons". Zyada tokens = trustworthy checker
  ki keemat; throwaway read-only chores ke liye skip OK.
- **Codify the body — dynamic workflows:** Claude Code poori orchestration ko ek **re-runnable
  script** likhne deta hai (turn-by-turn improvise ke bajaye).

## F. Spine — Runs Ke Darmiyan Memory

- **2 spine layers (trap):**
  | Layer | File | Kya |
  | --- | --- | --- |
  | Rules file | `CLAUDE.md` / `AGENTS.md` | project ki standing aadatein — har run shuru mein parhi jaati |
  | Checkpoint file | `progress.md` | kya ho chuka, aage kya — har beat start par parho, end par update karo |
- Galtiyan **spine ke andar jama hoti hain** — aaj ki galat line kal ka galat starting point.
- **Kai loops ek memory share karein — 4 guardrails:** versioning (rollback) · conflict checks
  (write se pehle file badli to nahi) · permissions by level (org-wide rules read-only) · portability
  (plain open format).

## G. Human Control — Course Ka Sabse Ahm Part

### 3 feedback cycles — tumhari loop sirf ek hai

| Loop | Waqt | Kaun | Kya |
| --- | --- | --- | --- |
| **Coding loop** | minutes | agent akela | likhta, test, fix — jab tak spec match |
| **Feedback loop** | hours | **tum** | try karte ho, decide kya change, spec update |
| **Outside loop** | days | duniya | real log use karte hain, unka react aage batata hai |

**Andrew Ng — context advantage:** agent teeno khud kyun nahi chala sakta? Kyunki **tum** woh jaante
ho jo agent nahi — kaun use karega, unhe kya chahiye, "achha" kaisa lagta hai.

### In / On / Out of the loop

| Term | Matlab | Kahan |
| --- | --- | --- |
| **Human in the loop** | har action se pehle insaan approve | prompting turn-by-turn, plan mode, merge gate |
| **Human on the loop** | system khud chale, insaan dekhta rahe + rok sake | Routine `claude/` branches par push, tum subah review |
| **Human out of the loop** | koi na dekhe, koi intervene na kar sake | **kabhi acceptable nahi — failure mode** |

- Prompting = **in** the loop · Loop engineering = **on** the loop · achi loop **mix** hoti hai
  (safe fixes "on", risky/FAIL wapas "in").
- **"Out of the loop" jaan-boojh kar nahi banta — DRIFT se banta hai:** diffs parhna band, green
  checkmarks par trust, weekly review skip → "on" chup-chaap "out" ban jaati hai.

### Token cost — asal limit

- Ek beat (maker + checker) ~40,000 in + ~6,000 out ≈ **$0.20/beat**. 5 beats/din × 20 din ≈ **$20/mo**.
- Wahi loop **har 5 min** din-raat ≈ **$1,800/mo** — **same kaam, sirf frequency**.
- Fixes: har loop cap · model ko kaam se match (strong plan/check, sasta kaam — **sabse bara
  saving**) · loop prompt + rules file chhoti · **kam frequency** (~12x sasta).
- **Achi spine cost bhi kam karti hai** — pehli try ka lesson yaad → kam retries.

### Concept 15 — apne project ko samajhna band mat karo

- Do log ek jaisi loop bana sakte hain, opposite result: ek jo woh **deeply samajhta hai** use tez
  chalata hai; doosra **samajhne se bachne** ke liye. Loop farq nahi bata sakta, **tum bata sakte ho**.
- **AI gravity** (Eric So, MIT Sloan) — AI ko zyada sochne dene ki musalsal pull; loop is pull ko
  mazboot karta hai (sote waqt bhi chalta hai).

### Observability — loop fail ho to

- Output wahan bhejo jahan tum dekh sako (log file, Slack/Discord) — na woh terminal jo band kiya.
- Har run par ek line, **fail hone par bhi**, timestamp ke sath — chup-chaap fail sabse bura.
- Runs replayable rakho.
- Limit par **loudly fail** — clear "needs a human" note, sirf ruk na jaye.
- **Overnight se pehle prove karo:** hourly + watched → nightly + unattended. Report-only → gated
  fixes → unattended action.

## H. Do Rastay

- **Claude Code:** parts product ke andar — `/loop`, `/goal`, `/schedule`, Routines, `--worktree`,
  `.claude/agents`, Channels, hooks. Cloud Routines laptop band par bhi, lekin daily run limit.
- **OpenCode:** "worker" milta hai (`opencode run`), scheduler/trigger khud (cron, launchd, Task
  Scheduler, GitHub Actions). Zyada setup, zyada control, koi vendor cloud nahi.
- **Shape same, commands alag** — shape hi transferable skill hai.

---

## Ek-Line Revision (M4)

> 6 parts: heartbeat · worktree · skill · subagents (maker≠checker) · connector (act) · **spine (no
> spine no loop)** · 4 heartbeats: in-session / conditional / scheduled / event · 3 stops: success
> (command-provable) + limit + no-progress · human **on** the loop (in=approve each, out=failure
> mode, drift → out) · cost = frequency; strong-plan/cheap-execute + low frequency + good spine ·
> intent + accountability hamesha insaan ke.

---

## MCQ Practice (jawab neeche)

1. Loop ke 6 parts mein woh kaunsa jo beginners skip karte hain?
   a) Heartbeat b) Worktree c) Spine (state/memory) d) Connector

2. "No spine, no loop" ka matlab:
   a) Loop slow ho jaata b) Bina memory ke loop apna pehla step hamesha repeat karega c) Loop crash
   d) Cost barh jaata

3. Loop har subah chalta hai par kal ka kaam yaad nahi — kaunsa part missing?
   a) Skill b) Spine c) Checker d) Connector

4. Maker-checker rule:
   a) Ek hi agent sab kare b) Jo agent kaam banata hai woh apna kaam khud approve nahi kar sakta —
   doosra grade kare c) Human har baar check kare d) Tests kaafi hain

5. `/goal` ka checker kya kar sakta hai?
   a) Commands chala sakta hai b) Sirf dikhta output/transcript parh sakta hai — isliye condition
   command-provable ho c) Files edit kar sakta hai d) PR khol sakta hai

6. Conditional loop ke 3 stops:
   a) Start, middle, end b) Success condition + limit + no-progress check c) Heartbeat, spine,
   checker d) Prompt, repo, trigger

7. "Ralph loop" mein kya missing hota hai (baaki run-until-done ke muqable)?
   a) Success condition b) Time cap c) Stuck-check aur separate checker d) State file

8. In-session `/loop` ka timer kahan rehta hai?
   a) Cloud b) Tumhari open session ke andar — session band, loop khatam c) Scheduler d) GitHub

9. Routine default kis branch par push karti hai?
   a) main b) `claude/` branches c) koi bhi d) ek naya repo

10. "Human on the loop" ka matlab:
    a) Har action approve karo b) System khud chale, insaan dekhta rahe aur rok sake c) Koi na dekhe
    d) Sirf gate par type karo

11. "Human out of the loop" kaise banta hai?
    a) Design decision se b) Drift se — diffs parhna band, green checkmarks par trust, review skip
    c) Vendor default se d) Kabhi nahi banta

12. Loop mein connector writes kaisi honi chahiye?
    a) Blind "create" b) Idempotent — "update-or-create" (retry par duplicate na bane) c) Read-only
    d) Batched

13. Loop mein error message kaisa hona chahiye?
    a) Chhota b) Agla step bataye ("request the repo scope") — warna ek beat waste c) Error code
    d) Stack trace

14. Loop ki asal cost sabse zyada kis se badalti hai?
    a) Model size b) Frequency (har 5 min vs 5/din = ~100x) c) Prompt length d) Repo size

15. 3 feedback cycles mein "tumhari" loop kaunsi hai?
    a) Coding loop (minutes) b) Feedback loop (hours — try, decide, spec update) c) Outside loop
    (days) d) Teenon

16. Andrew Ng ka "context advantage":
    a) Bara context window b) Tum woh jaante ho jo agent nahi — kaun use karega, kya chahiye, "achha"
    kaisa c) AI ka training data d) Cloud compute

### Jawab Key

1‑c · 2‑b · 3‑b · 4‑b · 5‑b · 6‑b · 7‑c · 8‑b · 9‑b · 10‑b · 11‑b · 12‑b · 13‑b · 14‑b · 15‑b · 16‑b

---
[⬅ 03 — Local AI and Agentic Coding](03-local-ai-and-agentic-coding.md) · [Agla: 05 — Harness Engineering ➡](05-harness-engineering.md)
