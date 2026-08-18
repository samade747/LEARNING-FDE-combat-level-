# 09 — Routine Drills (9-11) + Dreaming Capstone (12)

Yeh 3 drills jaan-boojh kar appendix ki sabse important failure cases ko ek throwaway repo mein
reproduce karte hain — taake aap unhe cheap, controlled tareeqe se experience karo. Drill 9 sirf
one-off runs use karta hai (daily cap mein count nahi hota). 10 aur 11 milakar ~5 runs lete hain (Pro
cap ka ek din). **2 rules yahan bhi:** throwaway repo, limit pehle set karo.

Project 12 doosra capstone hai — Project 3 ya 8 par build karta hai (isay run karne ke liye pehle un
mein se ek chahiye).

---

### 9. 🧪 Rehearse a Routine For Free
**Difficulty:** Easy · **Time:** 20-30 min · **Uses:** A1, A3 (one-off schedules), A5 (reading runs)

**Kya banana hai:** Ek throwaway repo mein ek Routine banao jiska prompt ek chota, checkable kaam kare
(jaise kal ke commits ko `claude/summary` branch par summarize karna). Isay repeating schedule par mat
dalo. **One-off run** se fire karo aur poora **transcript** parho, status column nahi. Phir prompt ko
badal do taake task **fail** ho (jaise ek aisi file parhna jo exist hi nahi karti), aur ek baar aur fire
karo.

**Kaise karein (step-by-step):**
1. `claude.ai/code/routines` par jao, **New routine → Remote**
2. Prompt: *"Summarize yesterday's merged pull requests and push a short summary to a new branch
   claude/summary."*
3. Repo select karo, koi extra connector mat do
4. Trigger: **one-off**, `/schedule tomorrow at 9am, ...` ya web UI mein **Run now**
5. Run khatam hone par **transcript** parho — na ke sirf green status
6. Ab prompt ko todo: *"Read the file nonexistent-report.txt and summarize it."*
7. Fire karo dobara, transcript parho — dekho model kaise fail hone par react karta hai

**Done jab:** 2 green runs dekh chuke ho — ek jiska transcript success dikhaye, ek jiska failure. Aap
ek sentence mein bata sako ke status column dono mein farq kyun nahi kar sakta.

---

### 10. 🔑 The Secrets Drill
**Difficulty:** Easy-Medium · **Time:** 30-45 min · **Uses:** A4 (secrets), A2 (environment)

**Kya banana hai:** Ek prompt likho jisay ek secret chahiye (dummy token chalega — drill iske baare mein
hai ke value **kahan rehti hai**, kya unlock karti hai woh matter nahi karta). Pehli run: token
gitignored `.env` file mein daalo, Routine fire karo, dekho fail hoti hai. Doosri run: token
environment-variables panel mein move karo.

**Kaise karein (step-by-step):**
1. Repo mein `.env` file banao (gitignored): `MY_API_TOKEN=dummy-123`
2. Prompt: *"Read MY_API_TOKEN and confirm it starts with 'dummy'."*
3. Routine fire karo (one-off) — transcript parho, dekho Claude token dhoond nahi pata (kyunki
   `.env` gitignored hai, cloud clone tak kabhi nahi pahunchta)
4. Ab Routine ki **Environment → Variables** panel mein `MY_API_TOKEN=dummy-123` add karo
5. Prompt mein ek line add karo: *"credentials are available as environment variables; do not look
   for a `.env` file."*
6. Dobara fire karo

**Done jab:** Doosri run token environment se successfully parhti hai, aur aap mechanical wajah bata
sakte ho pehli run kyun fail hui: gitignored files GitHub tak kabhi nahi jatin, isliye fresh cloud
clone mein woh kabhi hoti hi nahi.

---

### 11. 🚪 Build the Two-Routine Gate
**Difficulty:** Medium-Hard · **Time:** 1-2 hrs · **Uses:** A3 (API trigger), A4 (the gate), A6 (checklist)

**Kya banana hai:** Routine A (one-off schedule par) kuch reviewable draft kare — ek `claude/` branch,
ya connector se ek chota summary post. Routine B ka **API trigger** ho aur woh ek chota follow-up action
kare. B ka bearer token dikhte hi store karo (ek baar hi dikhta hai). A ka draft khud review karo. Phir
usay B ko `curl` call se fire karke approve karo.

**Kaise karein (step-by-step):**
1. **Routine A** banao (one-off): prompt = *"Draft a short release note for this week's merged PRs on
   a new claude/release-note branch. Do not open a PR."*
2. **Routine B** banao: trigger = **API**, prompt = *"Open a pull request from the claude/release-note
   branch with the content already on it."* — token generate karte hi copy/store karo
3. Routine A fire karo, branch ka content khud review karo
4. Sahi lage to Routine B ko A3 wala `curl` command se fire karo (`{"text": "approved by <aapka naam>"}`
   bhej sakte ho context ke liye)
5. B ka transcript parho — confirm PR khuli

**Done jab:** 3 cheezein sach hon — B sirf isliye chali kyunki **aap** ne fire kiya, B ke transcript mein
action asal mein hua dikhta hai, aur dono Routines par A6 checklist run kar chuke ho (connectors pruned,
unrestricted pushes off, state file chuna hua).

---

### 12. 🌙 Build a Dreaming Loop (Capstone 2)
**Difficulty:** Capstone · **Time:** 2-3 hrs · **Uses:** Concept 12 (spine + dreaming), 11 (maker-checker), 6 (schedule), Part 5 (human gate)

**Kya banana hai:** Aapko ek loop chahiye jo pehle se ek hafte se chal rahi ho aur `progress.md` mein
dated entries chorh chuki ho (Project 3 ya Project 8 dono kaam ayenge). Ab uske **upar** ek doosri loop
banao. Weekly schedule par, apni `dreaming-state.md` mein likhi last date ke baad ke sab log entries
parhe, koi bhi failure/correction dhoonde jo **ek se zyada baar** dikhi ho, aur us pattern ko rokne wala
sabse chota rules-file/skill change **PR ki tarah** draft kare (`claude/` branch par, kabhi direct
commit nahi). PR description mein evidence hona zaroori: kaunse runs, kitni baar, kyun yeh line usay
rokegi. Ek **deletion** bhi propose kare: koi rule jo recent runs ko chahiye nahi tha.

**Kaise karein (step-by-step):**
1. Confirm karo `progress.md` mein kam az kam 5-7 dated entries hain (Project 3/8 se)
2. `dreaming-state.md` banao: `last_reviewed_date: 2026-08-01` jaisi ek line
3. Ek weekly Routine/cron banao, prompt:
   ```text
   Read progress.md entries dated after the date in dreaming-state.md.
   Find any failure or correction pattern that appears more than once.
   For each pattern found, draft the smallest CLAUDE.md or skill change that
   would prevent it, on a new claude/dreaming-<date> branch. Open a PR whose
   description cites: which runs showed the pattern, how often, and why this
   line stops it. Also propose one deletion: a rule no recent run needed.
   Never edit CLAUDE.md or a skill directly — only through this PR.
   Finish by updating dreaming-state.md with today's date.
   ```
4. **Test evidence-forcing:** hath se `progress.md` mein ek repeated failure plant karo (jaise "agent
   forgot to run lint" 3 alag dates par)
5. Loop chalao, PR check karo — kya usne plant kiya hua pattern pakra, evidence cite kiya?
6. **Kabhi khud approve mat karo** — yeh sabse high-leverage write hai poore system mein (har future run
   isay padhega). Sirf tab merge karo jab evidence genuinely convincing ho

**Done jab:** 3 cheezein sach hon — PR ka proposed change real, cited log entries tak trace hota hai
(guess nahi), jaan-boojh kar plant ki gayi repeated failure pakri gayi aur proposal ban gayi, aur koi
change aapke rules file mein bina merge kiye nahi hua. Agar loop bina evidence ke changes propose kare,
prompt tighten karo — evidence-less improvement loop no-improvement-loop se bura hai, kyunki uske
guesses har future run ko steer karte hain.

---
[⬅ Routines Appendix](08-routines-appendix.md) · [⬆ Index](README.md) · [Agla: Commands Cheat Sheet ➡](10-commands-cheat-sheet.md)
