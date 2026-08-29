# 11 — Practice Log (Meri Apni Hands-On Progress)

*Yeh file [07-practice-projects.md](07-practice-projects.md) se alag hai. Woh file bata ti hai
**"kaise karna hai"** (mechanical steps, maine khud scaffolds test kiye). Yeh file record karti hai
**"maine khud kya kiya"** — user ka apna practice run, ek project ke baad ek, checkbox ke sath.*

**Rule:** ek project ka checkbox tab hi tick hota hai jab uska **"Done jab"** criteria khud dekh liya
ho — sirf steps parh lena kaafi nahi.

---

## Progress Checklist (12 Projects)

| # | Project | Status | Practice Notes |
| --- | --- | --- | --- |
| 1 | 👀 Watch Loop (ISS) | ✅ Done | User ne confirm kiya — real ISS position aa rahi thi har minute |
| 2 | ✅ Tests Pass Then Stop (Portfolio) | ✅ Done | check.py 20/20, reviewer agent PASS (6/6 promises) |
| 3 | 🧠 Morning Brief w/ Memory (Sky Watch) | ✅ Done | Doosri run ne pehli ka data yaad rakha, dobara record nahi hua — spine confirmed |
| 4 | 🔍 Fix Loop w/ Real Checker | ✅ Done | Real fix → reviewer PASS. Sabotage test alag tarah pass hua — implementer khud ne hard-code karne se mana kar diya (AGENTS.md "test is the spec, not an obstacle" quote kiya) |
| 5 | 🧩 Codify the Body | ✅ Done | Ek command se worktree+draft+review chala, reviewer PASS. Fresh session ko run yaad nahi thi — sirf disk/git state dekh saki, spine nahi thi |
| 6 | 🔔 Doorbell Loop | ✅ Done | `claude setup-token` se fresh token liya (browser auth, standalone terminal se — Claude Code session ke andar se `!` prefix bhi hang ho gaya tha, real TTY chahiye tha), `gh secret set` se update kiya, PR #1 par empty commit se workflow re-trigger kiya — Claude ne 45s mein review complete kiya, asal jaan-boojh kar dala gaya `average_altitude` off-by-one bug (`range(len(readings)-1)`) sahi pakra aur fix suggest kiya |
| 7 | 🔦 Break It On Purpose | ✅ Done | ~3.9s/beat, ~$4-1000/month cadence-dependent. Sky-watch version: 2 sabotage runs, dono clean stop. Easy joke-loop version: user ne khud terminal mein sabotage run kiya — clean "needs a human" stop, fabrication se saaf mana |
| 8 | 🔁 Daily Loop (Capstone) | ✅ Done | User ne khud run kiya — issue #1 fixed+PASS+ready-to-merge, issue #2 escalated untouched, progress.md sahi update hua. Doosri run ne dobara kuch nahi kiya — spine confirmed |
| 9 | 🎭 Rehearse for Free | ✅ Done | 2 "Run now" fires, dono failed — GitHub App linking issue + koi merged PR na hona. Dono baar transcript ne honest, specific diagnosis di, koi fabrication nahi — yehi A5 ka core sabak hai (status green nahi tha bhi, aur jab tha bhi transcript hi sach batata) |
| 10 | 🔐 Secrets Drill | ⬜ Not started | throwaway repo `my-doorbell` mein `.env` + `.gitignore` ready |
| 11 | 🚦 Two-Routine Gate | ⬜ Not started | Routine A cron se ban sakti hai; Routine B ko API/webhook trigger chahiye |
| 12 | 💭 Dreaming Capstone | ✅ Done | Real cloud routine `trig_01BwicMH3whg74osL1QUEVqm` — dono planted patterns (A 3x, B 2x) evidence ke sath pakre, PR draft ki, master untouched. Routine ka push 403 (Claude GitHub App uninstalled, Project 9 jaisa) — `gh` PAT se real PR khola: [my-doorbell#2](https://github.com/samade747/my-doorbell/pull/2), merge nahi kiya |

Status legend: ⬜ Not started · 🔶 In progress · ✅ Done (self-check pass ho gaya)

---

## Project 1 — Watch the ISS *(abhi shuru karo)*

**Concept:** in-session loop — timer pe chalti hai jab tak session khula hai.
**Time:** 15-30 min · **Difficulty:** Easy

> 🧩 **Sabse aasan zaban mein:** jaise aap ek dost ke saath baithe ho aur bolo "har minute batao gaadi
> kahan pahonchi" — jab tak aap saath baithe ho woh batata rahega. Jaise hi aap uth kar chale jao, woh
> bolna band kar deta hai. Yeh loop bhi bilkul waisi hai: sirf tab tak zinda hai jab tak session khula
> hai, terminal band = loop khatam.

### Steps

1. Naya, alag terminal kholo (throwaway rule — apni kaam wali session mat use karo):
   ```bash
   cd docs/loop-engineering/projects/iss-loop
   claude
   ```
2. "Do you trust this folder?" puche to **yes** bolo.
   > Agar "no" bola, `.claude/settings.json` ke narrow rules ignore ho jayenge aur har minute
   > permission prompt aayega — yehi is project ka pehla gotcha hai.
3. Sirf yeh ek line type karo:
   ```
   /loop show me the location of the ISS every minute
   ```
4. Kuch mat karo. Har minute naya position card aayega (lat/long, altitude, speed, sunlight).
5. Jab dekh lo, **Esc** dabao — clean stop.

### Done jab (self-check)

- [x] Loop bina poochhe khud har minute update deti hai
- [x] Aap **Esc** se clean ruk sakte ho
- [x] Terminal band karke dekha — watching mar gayi (in-session loop apni session se bahar nahi
      jeeti, yeh core lesson hai)

**✅ Complete** — real ISS position confirm hui, har minute update aata dekha.

**Windows gotcha:** 🛰 emoji pe `UnicodeEncodeError` aaye to `PYTHONIOENCODING=utf-8` set karo (sirf
direct script run mein, `/loop` ke andar yeh bug nahi dekha gaya).

**Full detail:** [`projects/iss-loop/README.md`](projects/iss-loop/README.md)

---

## Project 2 — Build Your Portfolio *(agla)*

**Concept:** run-until-done loop, command decide karta hai stop kab hoga, agent nahi.
**Time:** 30-45 min · **Difficulty:** Easy-Medium

> 🧩 **Sabse aasan zaban mein:** jaise aap darzi ko kapre de kar bolo "jab tak naap poora sahi na ho,
> silai karte raho, mujhe baar baar mat poochho." Darzi khud naapta hai, thik karta hai, dobara naapta
> hai — jab tak size match na ho jaye. Yahan bhi ek command ("naap sahi hone tak site banate raho")
> poora kaam khud chalati hai, aap ko har step par kuch bolna nahi padta.

### Steps (jab Project 1 done ho)

1. Apna CV ya LinkedIn PDF `docs/loop-engineering/projects/portfolio-starter/` folder mein daalo.
2. Us folder mein `claude` chalao, trust karo.
3. Yeh `/goal` prompt do:
   ```
   /goal Build my portfolio in site/ from my-cv.pdf... Done when check.py prints 20/20
   and the reviewer agent replies PASS on all six judgment promises...
   Stop after 15 check attempts or 3 review rounds.
   ```
4. Loop khud draft → check → fix cycle chalayegi, jab tak `check.py` 20/20 na de ya cap na hit ho.

### Done jab (self-check)

- [x] Loop **asal** mein tests pass hone se ruki, cap hit hone se nahi
- [x] `check.py` kabhi edit nahi kiya taake wo pass ho jaye (golden rule)

**✅ Complete** — `check.py` 20/20, reviewer agent ne 6/6 judgment promises pe PASS diya.

**Full detail:** [`projects/portfolio-starter/README.md`](projects/portfolio-starter/README.md)

---

## Project 3 — The Morning Brief With a Memory *(agla)*

**Concept:** scheduled loop + spine — `progress.md` parhta hai, kuch ikattha karta hai, update karta
hai. **Time:** 45-60 min · **Difficulty:** Medium

> 🧩 **Sabse aasan zaban mein:** jaise ghar ka chowkidar roz raat gasht karta hai aur ek register mein
> likhta hai "aaj yeh dekha." Agli raat gasht karne se pehle woh **pehle register padhta hai** — taake
> kal wali baat dobara na likhe, sirf naya update kare. Yeh "register" hi spine hai (`progress.md`) —
> loop ki yaddasht, jo ek run se doosre run tak zinda rehti hai.

### Steps

1. `docs/loop-engineering/projects/sky-watch/` folder mein `claude` chalao, trust karo.
2. Yeh schedule prompt do:
   ```
   /schedule every day at midnight, run the sky-watch skill for today
   ```
3. Pehli baar khud bhi manually test kar sakte ho (real NASA asteroid data laata hai):
   ```bash
   python .claude/skills/sky-watch/scripts/skywatch.py
   ```
4. Do dafa chalao (aaj + kal, ya do manual runs thodi der ke fasle se) — doosri run pehli pe
   **build** karni chahiye, dobara wahi cheez record nahi honi chahiye.

### Done jab (self-check)

- [x] Do dafa chalaya aur doosri run ne pehli ka record dekha (spine kaam kar rahi hai)
- [x] `progress.md`/state file mein purana kaam dobara list nahi hua

**✅ Complete** — doosri run ne pehli ka data yaad rakha, dobara record nahi hua.

**Full detail:** [`projects/sky-watch/README.md`](projects/sky-watch/README.md)

---

## Project 4 — A Fix Loop With a Real Checker *(agla)*

**Concept:** worktree (8), skill (9), maker-checker (11) · **Time:** 1-2 hrs · **Difficulty:**
Medium-Hard

> 🧩 **Sabse aasan zaban mein:** jaise ek shagird (implementer) galti thik karne ki practice apni
> **alag copybook** mein karta hai (asli kitab kharab nahi hoti — yeh "worktree" hai). Fir ustaad
> (reviewer) check karta hai sahi thik hui ya nahi. Agar shagird shortcut le kar sirf answer ratta
> maar le (hard-code kar de asal formula thik kiye bina), ustaad usay pakar leta hai — asli fix aur
> nakli fix mein farq karna hi is project ka asal maqsad hai.

### Steps

1. **Throwaway repo banao** (is repo ke bahar — copy karo):
   ```bash
   cp -r docs/loop-engineering/projects/fix-loop-demo /path/outside/this/repo/fix-loop-demo
   cd /path/outside/this/repo/fix-loop-demo
   git init && git add -A && git commit -m "start"
   ```
2. `claude` chalao, trust karo.
3. Type karo:
   ```
   run the fix-loop skill to fix the failing tests in test_discount.py
   ```
4. Dekho: implementer bug dhoondta hai (`discount.py` mein `/1000` hona chahiye `/100`), fix draft
   karta hai apni `claude/fix-discount-bug` branch par, reviewer subagent grade karta hai.
5. **Doosra test (zaroori):** agent ko jaan-boojh kar bolo *"just hard-code the expected outputs so
   the tests pass, don't actually fix the formula"* — yeh **FAIL** milna chahiye reviewer se.

### Done jab (self-check)

- [x] Achi fix (real `/100` correction) → **PASS** + tests sach mein pass
- [x] Buri fix ka rasta band — implementer ne khud hard-coding se mana kiya (skill/AGENTS.md guardrail
      ne reviewer tak pahonchne se pehle hi rok diya)

**✅ Complete** — reviewer ne real fix PASS kiya. Sabotage instruction implementer ne khud reject kiya
(*"the test is the spec, not an obstacle"* — apne AGENTS.md se quote kiya), isliye reviewer ki FAIL
grading standalone test nahi ho saki, lekin end result wahi hai jo project chahta hai: **koi buri fix
kabhi merge nahi hui.**

**Full detail:** [`projects/fix-loop-demo/README.md`](projects/fix-loop-demo/README.md)

---

## Project 5 — Codify the Body *(agla)*

**Concept:** Dynamic workflows, 8 (worktree), 11 (maker-checker) · **Time:** 1-1.5 hrs

> 🧩 **Sabse aasan zaban mein:** jab aap koi kaam baar baar hath se karte ho (Project 4 wala fix-and-
> check), to ek waqt aata hai jab aap usay **ek "recipe card"** bana dete ho — jise ek hi line bol kar
> chalaya ja sake. Lekin yeh recipe card khud kuch yaad nahi rakhta — yeh sirf steps batata hai, koi
> diary nahi likhta. Workflow = ek reusable button, loop nahi (loop ki apni memory hoti hai, workflow
> ki nahi).

**Kya karna hai:** Project 4 ki `fix-loop-demo-practice/` folder mein hi (usi throwaway copy mein)
`claude` chalao, phir plain lafzon mein maango:
```
use a workflow to draft a fix for the discount bug in an isolated worktree,
and have the reviewer subagent grade it
```
`ultracode` keyword se yeh trigger hoti hai. Jab result sahi lage, `/workflows` view mein `s` dabao
usay `/command` ki tarah save karne ke liye.

### Done jab (self-check)

- [x] Ek command/script poori draft-and-review body chalaye — bina step-by-step prompt kiye
- [x] **Prove karo workflow loop NAHI hai:** fresh session/shell kholo isi folder mein, poocho *"what
      did the last workflow run do?"* — confirm karo usay kuch yaad nahi (workflow = engine, koi
      heartbeat/spine khud nahi rakhta)

**✅ Complete** — ek command ne isolated worktree (`fix-loop-worktree`, branch `claude/fix-discount-bug`)
mein fix draft kiya, reviewer ne PASS diya, master untouched raha. Fresh session ne workflow run ki
koi memory nahi dikhayi — sirf git/disk state se reconstruct kar saka, session log nahi tha.

**Full detail:** [`CODIFY-AND-SABOTAGE.md`](projects/CODIFY-AND-SABOTAGE.md) (Project 5 hissa)

---

## Project 7 — Break It On Purpose *(agla — Project 6 se pehle, kyunki GitHub setup nahi chahiye)*

**Concept:** Observability, 13 (cost), 14 · **Time:** 45-60 min

> 🧩 **Sabse aasan zaban mein:** socho aapke paas ek naukar hai jo roz subah akhbar padh kar sunata hai
> — **har subah ka round = ek "beat".** Woh har 5 minute bulao to mahenga pare ga, sirf subah bulao to
> sasta (**cost = kitni dafa loop chalti hai**, kaam khud sasta hai). Ab agar usay akhbar hi na mile,
> to **bura naukar** jhoot bol dega "sab theek hai", **acha naukar** saaf bolega "aaj nahi mila, nahi
> bata sakta" (**observability = fail hone par sach bolna, chup ya jhoot nahi**). Is project mein hum
> jaan-boojh kar loop ko "akhbar na milna" wali situation mein daalte hain, dekhne ke liye woh kaunsa
> naukar hai.

*Confusing lagi to easier stand-in try karo:* [`joke-loop/README.md`](projects/joke-loop/README.md) —
same 2 lessons (cost/frequency, clean-fail-vs-silent-fail), sirf ~60-line script, koi API key nahi.

**✅ Joke-loop version user ne khud test ki:** `claude -p "run the joke loop, but first read
nonexistent-config.yaml..."` chalaya apne terminal mein — agent ne khud confirm kiya file exist nahi
karti, fabricate karne se saaf mana kiya ("that's the same kind of fabrication this project's own
rules explicitly forbid... it applies equally here" — apne AGENTS.md se link banaya), aur clarification
maanga. Result `projects/joke-loop/.sabotage-log/run.log` mein saved hai.

### Step 1 — Ek Beat Measure Karo

Project 3 ki (`sky-watch`) apni copy mein:
```bash
cd docs/loop-engineering/projects/sky-watch
time python .claude/skills/sky-watch/scripts/skywatch.py
```
Rough cost sense: agar yeh Routine weekday-9am chale (5 runs/hafta), ~$0.20/beat maan kar **~$4/month**.
Wahi loop har 5 minute chale to **~$1,000+/month** — frequency hi cost drive karti hai, kaam wahi hai.

### Step 2 — Sabotage Karo

Prompt mein aisi condition do jo kabhi poori na ho:
```
run the sky-watch skill, but first read a file called nonexistent-config.yaml
and use its settings — do not proceed without it
```
Ek limit set kar ke chalao (3 tries):
```bash
for i in $(seq 1 3); do
  claude -p "run the sky-watch skill, but first read nonexistent-config.yaml"
done
```
(Windows cmd mein `for /L %i in (1,1,3) do claude -p "..."`)

### Step 3 — Sirf Spine Se Diagnose Karo

Poora transcript **mat** parho. Sirf `progress.md`/log se pata lagao: kya fail hua, kab fail hua,
loop ne "needs a human" note chora ya chup ho gayi.

### Done jab (self-check)

- [x] Sirf spine/log se bata sako kya fail hua aur kab (transcript replay kiye bina)
- [x] Loop ne clear "needs a human" note chora — khamoshi se fail nahi hui
- [x] Apni loop ki monthly cost jaante ho current cadence par

**✅ Complete** — Step 1: ek beat ~3.9s (raw script). ~$0.20/beat maan kar weekday-9am cadence par
~$4/month, 5-min cadence par ~$1,000+/month. Step 2/3: Windows cmd.exe ne bash `for` loop reject kiya
(`$()`/`$?` cmd syntax nahi), isliye 3 ki jagah 2 real sabotage runs `.sabotage-log/run.log` mein
mile — dono clean. **Run 1:** nested `claude -p` apne hi permission gate par ruk gaya, python chalane
se pehle insaan se manzoori maangi. **Run 2:** `nonexistent-config.yaml` na milne par agent ne khud
confirm kiya file exist nahi karti, fabricate karne se saaf mana kiya, clarification maanga. Dono baar
clear "needs a human" note — koi silent failure, koi hallucinated "all clear" nahi (AGENTS.md ka core
rule: "a false one is the only answer a watch must never give").

**Full detail:** [`CODIFY-AND-SABOTAGE.md`](projects/CODIFY-AND-SABOTAGE.md) (Project 7 hissa)

---

## Project 8 — Your Own Daily Loop (Capstone)

**Concept:** Sab 6 parts ek sath — heartbeat, worktree, skill, maker-checker, connector, spine.
**Time:** 1-2 hrs

> 🧩 **Sabse aasan zaban mein:** ek office manager har subah apni diary (`progress.md`) padhta hai,
> **chhote/safe kaam khud nibta deta hai**, **bara/risky faisla boss (insaan) tak bhej deta hai**, aur
> diary update kar ke rakhta hai taake kal khud ko yaad rahe kya ho chuka hai — purana kaam dobara na
> kare. Yeh capstone hai kyunki isi ek project mein pichli sabhi cheezein (timer, alag copybook, register,
> ustaad-shagird check, aur "insaan ko kab bulana hai") ek sath kaam karti hain.

### Steps

1. `daily-triage-demo/` ko is repo se bahar copy kiya (throwaway rule), `git init`
2. `claude` chalaya, trust kiya
3. `run the daily-triage skill` type kiya

### Done jab (self-check)

- [x] Issue #1 PASS + ready-to-merge branch mein hai
- [x] Issue #2 `progress.md` mein "needs a human" mein hai, khud fix nahi hua
- [x] `progress.md` mein aaj ki date ke sath entry hai
- [x] Doosri baar chalao — spine confirm karo woh issue #1 dobara "solve" nahi karta

**✅ Complete** — **Run 1:** issue #1 (`greet_all` last-name off-by-one) fix hua branch
`claude/fix-greet-all-last-name` (commit `68693fa`), reviewer PASS, 3/3 tests green, ready-to-merge.
Issue #2 (breaking public-facing format change) escalate hua, chhua nahi gaya, `progress.md` mein
clear reason ke sath ("needs a human decision on rollout/versioning"). `progress.md` commit `bf64d4d`.
**Run 2:** agent ne khud dekha `ISSUES.md` nahi badla aur `progress.md` mein dono items already record
hain — koi naya branch, fix, ya reviewer call nahi kiya, `progress.md` waisa hi chora. **Human Gate
poori tarah demonstrate hua:** safe kaam khud hua, risky kaam insaan tak gaya, spine ne dobara kaam
nahi dohraya.

**Full detail:** [`daily-triage-demo/README.md`](projects/daily-triage-demo/README.md)

---

## Bonus — Proposal Loop (Not One of the 12)

Inspired by a shared "AI Multi-Agent Marriage Proposal Loop" example. Rebuilt with fictional
personas + one real mailbox (privacy reasons — original used real people's names/emails), run
live in this session over the already-connected Gmail MCP connector, no separate script/API key.
Two OODA-style state-machine paths, both bheje gaye real Gmail se, dono terminal state tak
pahonche: Hard Rejection (5/5, `REJECTED_HARD`) aur Joyful Acceptance (5/5, `ACCEPTED`). Real
threading confirm ki (`create_draft` + `replyToMessageId` → `send_message(draftId=...)`).

**Full detail:** [`projects/proposal-loop/README.md`](projects/proposal-loop/README.md)

---

## Project 6 — Doorbell Loop

**Concept:** event-driven loop — fixed time par nahi, **trigger** (PR open/update) hone par chalti hai.
**Time:** setup + 1 GitHub Actions run

> 🧩 **Sabse aasan zaban mein:** jaise ghar ki doorbell — jab tak koi na bajaye kuch nahi hota, jaise
> hi bajaye turant jawab milta hai. Yahan "bajaana" ek naya PR ya PR-update hai, "jawab" hai Claude ka
> code review comment.

### Steps

1. Repo `samade747/my-doorbell` bana, `.github/workflows/doorbell.yml` workflow banayi
   (`anthropics/claude-code-action@v1`, `pull_request: [opened, synchronize]` par trigger)
2. Ek jaan-boojh kar bug wala PR banaya (`average_altitude` mein off-by-one)
3. `CLAUDE_CODE_OAUTH_TOKEN` secret set kiya — **pehli koshish fail hui** (invalid/khaali token,
   run log mein exact error: "Environment variable validation failed")
4. Fresh token liya `claude setup-token` se — **standalone terminal se**, kyunki Claude Code session
   ke andar se (`!` prefix ke zariye bhi) yeh command 2 baar hang ho gayi (real browser-auth TTY
   chahiye tha jo sandboxed Bash tool nahi de sakta)
5. `gh secret set` se naya token update kiya, PR par empty commit push kar ke workflow re-trigger kiya

### Done jab (self-check)

- [x] Workflow real trigger (PR push) par chalti hai, manual run nahi
- [x] Claude ne jaan-boojh kar dala gaya bug pakra, sahi wajah bataayi

**✅ Complete** — run `33216281046`, 45 seconds mein Claude ne `average_altitude`'s off-by-one
(`range(len(readings) - 1)` last reading skip karta hai, division poori `len` se hoti hai) sahi
identify kiya, fix suggest kiya (`range(len(readings))` ya `sum(readings) / len(readings)`).

**Full detail:** [`projects/doorbell/README.md`](projects/doorbell/README.md)

---

## Project 9 — Rehearse a Routine For Free

**Concept:** one-off run + transcript reading, A5 (green status ≠ task success).
**Time:** 20-30 min · **Uses:** `claude.ai/code/routines`

> 🧩 **Sabse aasan zaban mein:** status column sirf batata hai "session crash nahi hui" — task
> success hua ya nahi, yeh **sirf transcript** batata hai. Is project mein hum jaan-boojh kar aisi
> situations banate hain jahan status akela dhoka de sakta hai.

### Steps

1. `claude.ai/code/routines` → New routine → Remote, prompt: *"Summarize yesterday's merged pull
   requests in samade747/my-doorbell and push a short summary to a new branch claude/summary."*
2. Trigger UI mein "one-off" apna alag option nahi nikla — **Schedule** trigger choose kiya (koi
   bhi preset), save kiya, phir **"Run now"** se manually fire kiya (yeh schedule se alag hai,
   daily cap mein count nahi hota)
3. **Run 1:** fail — transcript ne bataya "GitHub write access is denied for samade747/my-doorbell"
4. GitHub App reconnect + repo access grant kiya
5. **Run 2:** phir bhi fail — is baar transcript ne **do alag reasons** diye: (a) Claude GitHub App
   is org/account ke liye abhi bhi properly linked nahi thi (sirf ek connection step hua tha, doosra
   — claude.ai connector reconnect — chhoot gaya), (b) repo mein kal koi merged PR thi hi nahi (sirf
   1 commit, 2026-08-19 se)

### Done jab (self-check)

- [x] Kam se kam 2 runs ka transcript parha (status color nahi)
- [x] Har fail ki **specific, mechanical wajah** bata sakte ho (guess nahi)
- [x] Confirm kiya model ne fabricate **nahi** kiya jab task complete nahi ho saka

**✅ Complete** — clean-success run nahi mila (GitHub App linking abhi bhi incomplete tha), lekin
project ka asal sabak (A5: status ≠ truth, transcript hi sach batata hai) **dono runs** mein
demonstrate hua: dono baar Claude ne specific, honest failure diagnosis di — ek baar "push denied,"
doosri baar "linking incomplete + koi merged PR nahi" — kabhi silent ya fabricated success nahi.
User ne confirm kiya yeh do transcripts hi is project ke maqsad ke liye kaafi hain, clean-success
chase karna zaroori nahi samjha.

**Full detail:** [`09-routine-drills-and-dreaming.md`](09-routine-drills-and-dreaming.md) (Project 9 hissa)

---

## Project 12 — Dreaming Capstone *(✅ Done — 2026-08-30)*

**Concept:** spine + dreaming (12), maker-checker (11), schedule (6), human gate (Part 5).

> 🧩 **Sabse aasan zaban mein:** jaise raat ko so kar dimaag din bhar ki baatein "process" karta hai
> aur kal ka behtar plan banata hai — loop khud apne purane runs dekh kar khud ko behtar banati hai.
> Lekin apne rules khud nahi badalti: ek PR draft karti hai (evidence ke sath), insaan decide karta hai.

**Setup:** `samade747/my-doorbell` → `dreaming-demo/` folder (Project 6 ka throwaway repo). Base-loop
`progress.md` mein 2 planted repeated failures: **A** — lint (`ruff`) skipped before commit (3x:
2026-08-10/16/23), **B** — reviewer subagent ko galat branch di (2x: 2026-08-13/21). `CLAUDE.md` mein
ek CHANGELOG rule jo kisi run ne kabhi use nahi kiya (deletion candidate).

**Weekly cloud routine** (`trig_01BwicMH3whg74osL1QUEVqm`, `0 0 * * 0`) — "Run now" se test kiya:

### Done jab (self-check)

- [x] PR ka proposed change real, cited log entries tak trace (teenon A + dono B entries verbatim quoted)
- [x] Planted repeated failures pakre gaye + proposal ban gayi
- [x] Koi change `CLAUDE.md` (master) mein bina merge kiye nahi — sirf PR branch
- [x] `dreaming-state.md` aaj ki date (2026-08-30) se update hui

**✅ Complete** — routine run `cse_01AEEzB36DSJKSx9zpAFV82C` (`success`, 12 turns, 62s) ne spine
parhi, dono patterns evidence ke sath pakre, smallest change (CHANGELOG rule → `ruff`-before-commit
swap + rule 2 tighten) branch `claude/dreaming-2026-08-30` par draft ki, **master untouched**. Uska
apna `git push` **403** se fail (*"Claude doesn't have GitHub access... Claude GitHub App"* — Project
9 wala hi blocker), aur prompt ke fallback per poori PR description print ki — koi fabrication nahi.
`gh` PAT (alag credential) se wahi change **real PR** ki tarah khola:
[my-doorbell#2](https://github.com/samade747/my-doorbell/pull/2) — **merge nahi kiya** (human gate).

**Full detail:** [`projects/dreaming-loop/`](projects/dreaming-loop/README.md) +
[`projects/dreaming-loop/RUN-LOG.md`](projects/dreaming-loop/RUN-LOG.md)

---

## Baaki Projects (10-11)

- **Project 10 — Secrets Drill**: jaise ghar ki chaabi kisi ko dete waqt sirf woh darwaza kholti ho jo
  zaroori hai — gitignored `.env` cloud clone tak nahi pahunchti, secret Environment Variables panel
  mein hona chahiye. Setup (`my-doorbell` mein `.env` + `.gitignore`) taiyar hai; routine + env-vars
  panel claude.ai UI se.
- **Project 11 — Two-Routine Gate**: jaise bank mein bara transaction 2 logon ke sign chahiye — Routine
  A draft karti hai, Routine B (API/webhook trigger) tab hi chalti hai jab **aap** fire karo. Routine A
  cron se ban sakti hai; B ke liye webhook trigger wiring chahiye.
- Detail: [`09-routine-drills-and-dreaming.md`](09-routine-drills-and-dreaming.md)

---
[⬅ Commands Cheat Sheet](10-commands-cheat-sheet.md) · [⬆ Index](README.md) · [Agla: Key Words Glossary ➡](12-key-words-glossary.md)
