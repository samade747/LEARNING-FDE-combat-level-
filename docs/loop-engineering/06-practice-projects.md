# 06 — Practice Projects (8 Hands-On)

Padhna aur banana ek jaisa nahi. Ye 8 projects easy se hard tak hain. Kisi bhi tool (Claude Code ya
OpenCode) mein karo — shape same hai.

**2 rules, hamesha:**
- **Throwaway git repo use karo** — loop khud files edit karti hai, apna kaam wala repo mat do
- **Limit pehle set karo** — max tries/minutes/spend, khud chalne se pehle

---

### 1. 👀 A Watch Loop
**Difficulty:** Easy · **Time:** 15-30 min · **Concept:** 4 (in-session)

Ek lamba task shuru karo (jaise script jo sota rahe phir file likhe). In-session loop banao jo har
minute check kare kaam khatam hua ya nahi, aur khatam hone pe batae.

**Done jab:** Loop notice kare kaam khatam hua, ek dafa bataye, aur aap saaf tarah rok sako — aur aap ne
kabhi terminal ghoor kar nahi baitha.

**Real project:** ISS Loop — real space station ki location har minute. `/loop show me the location of
the ISS every minute` — terminal band karo, watching mar jati hai (yehi concept hai).

---

### 2. ✅ Make the Tests Pass, Then Stop
**Difficulty:** Easy-Medium · **Time:** 30-45 min · **Concept:** 5 (conditional), 11 (maker-checker)

Repo mein 2-3 chhoti failing tests dalo. Loop banao jo chalta rahe jab tak tests pass na hon — lekin
**command** (test runner) decide kare, agent nahi. 6 tries pe cap karo.

**Done jab:** Loop ruke kyunke tests **asal mein** pass ho gayin, cap hit hone se nahi. Agar baar baar
cap hit ho raha hai, aapka stop condition ya prompt theek nahi — yehi lesson hai.

---

### 3. 🧠 The Morning Brief With a Memory
**Difficulty:** Medium · **Time:** 45-60 min · **Concept:** 6 (schedule), 12 (spine)

Scheduled loop banao jo `progress.md` parhe, repo se kuch simple ikattha kare (open TODOs, ya last din
ke commits), short summary likhe, aur `progress.md` update kare.

**Done jab:** Do dafa chalao aur doosri run pehli pe **build** kare — matlab jo pehle record ho chuka
usay dobara na kare. Ye prove karta hai spine kaam kar rahi hai.

**Real project:** Sky Watch — har subah asteroid feed check karta hai. `/schedule every day at
midnight, run the sky-watch skill for today` — laptop band karo, subah forecast wahan hoga.

---

### 4. 🔍 A Fix Loop With a Real Checker
**Difficulty:** Medium-Hard · **Time:** 1-2 hrs · **Concept:** 8 (worktree), 9 (skill), 11 (maker-checker)

Part 5 wali loop ka chhota version. Chhoti skill likho, reviewer agent banao jo PASS/FAIL de. Ek real
bug lo, implementer apni checkout mein fix draft kare, reviewer grade kare. Sirf PASS pe PR khule.

**Done jab:** 2 cheezein sach hon — ek achhi fix **PASS + PR** paye, **aur** aap jo jaan-boojh kar buri
fix plant karo wo **FAIL + reasons** paye. Agar reviewer buri fix bhi pass kar de, checker bohat naram
hai — usay tight karo.

**Real project:** Portfolio Project — CV/LinkedIn PDF se poori website banwao, `/goal` ko finish line do:
```text
/goal Build my portfolio in site/ from my-cv.pdf... Done when check.py prints 20/20
and the reviewer agent replies PASS on all six judgment promises...
Stop after 15 check attempts or 3 review rounds.
```
**Golden rule:** Kabhi `check.py` ko edit mat karo taake wo pass ho jaye — yehi sab se pehli cheez hai
jo ek "green" ke liye optimize karti loop try karegi.

---

### 5. 🧩 Codify the Body
**Difficulty:** Medium-Hard · **Time:** 1-1.5 hrs · **Concept:** Dynamic workflows, 8, 11

Project 4 ki fix loop ko codify karo. Claude Code mein plain lafzon mein describe karo: *"use a workflow
to draft fixes for these three issues in parallel worktrees, and have a reviewer grade each one"*.

**Done jab:** Ek command/script poori draft-and-review body chalaye, **aur** aap ne prove kiya ho ke
fresh session mein workflow ko pichli run ka kuch yaad nahi (isay loop banane ke liye kya chahiye —
heartbeat + progress file — bata sako).

---

### 6. 🔔 The Doorbell Loop
**Difficulty:** Medium · **Time:** 45-60 min · **Concept:** 7 (event-driven), 10 (connectors)

Apni throwaway repo ko apni PRs review karwao. OpenCode: `opencode github install`. Claude Code:
GitHub pull-request trigger wali Routine banao. Ek planted bug wala PR kholo (off-by-one, ya deleted
null check) aur wait karo.

**Done jab:** PR ko wo review mile jo aap ne kabhi manga hi nahi, aur review planted bug ko flag kare.
Projects 1-3 ke saath, ab char'on heartbeats complete: in-session, conditional, scheduled, event-driven.

**Real project:** The Doorbell — laptop band karo, koi aur PR khole, review phir bhi aata hai (kyunke ye
kabhi aapki machine pe chal hi nahi raha tha).

---

### 7. 🔦 Break It On Purpose
**Difficulty:** Medium · **Time:** 45-60 min · **Concept:** Observability, 13 (cost), 14

Project 3 ki loop lo. Pehle ek beat measure karo (kitne tokens, monthly cost nikaalo). Phir sabotage
karo — prompt ko wo file dikhao jo exist hi nahi karti, ya aisi condition do jo kabhi poori na ho
(limit set karke). Fail hone do, phir sirf **spine se** diagnose karo.

**Done jab:** Sirf spine/log se pata chal jaye kya fail hua aur kab, loop ne clear "needs a human" note
chora ho (khamoshi se fail nahi hua), aur aap apni loop ki monthly cost jaante ho.

---

### 8. 🔁 Your Own Daily Loop (Capstone)
**Difficulty:** Capstone · **Time:** 2-4 hrs · **Concept:** All 6 parts

Ek real, boring, repeating chore chuno jis pe aap kaam karte ho — dependency audit, docs-freshness
check, changelog draft, lint sweep. Poori loop banao: heartbeat, worktree, skill, maker-checker,
connector, spine. Budget guards lagao. Chalne do.

**Done jab:** Ek hafta unattended chali ho aur aap jo ship hua usay **trust karte ho kyunke aap ne parha
hai**, na ke kyunke parhna chhor diya. Ye Concept 15 se poocho: kya aapki samajh loop ke changes ke
saath chalti rahi? Agar nahi, to loop slow kar do.

---
[⬅ Human Control](05-human-control.md) · [⬆ Index](README.md)
