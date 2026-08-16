# Loop Engineering — Final Prep (Poora, Code-Ke-Sath, Book Se Verified)

*Source: The AI Agent Factory — "Loop Engineering: A Crash Course" (Panaversity), 15 Concepts*
*URL: https://agentfactory.panaversity.org/docs/loop-engineering-crash-course*
*Yeh file `Loop-Engineering-Summary.md` ki "aasan overview" ka deep, code-ke-sath companion hai — har code block seedha book se liya gaya hai (book hi is prep ka "system of record" hai). Interview/exam/self-study ke liye ready.*

---

## 0. Ek Sentence Mein Poora Course

> "A prompt says what to do. A loop says when to stop. Stop prompting your agent turn by turn. Design the loop that prompts it for you — a heartbeat, four working parts, and a spine that remembers — and stay the engineer who reads what it ships." — Book ki closing line

---

## 1. Foundation: Prompting Se Looping Tak

Pehle: aap turn-by-turn control karte the. Aap start karte, agent reply karta, aap padhte, aap decide karte, aap phir type karte. **Aap khud heartbeat, checker, aur memory the.**

**Loop shift karta hai:**

| Prompting (jo aap jante ho) | Looping (yeh course add karta hai) |
| --- | --- |
| Aap har turn start karte ho | Schedule/event har turn start karta hai |
| Aap output parh kar decide karte ho aage kya | Checker output check karta hai, loop decide karta hai aage kya |
| Aap typing rokte ho to loop bhi rukti hai | Aapke sote waqt bhi chalta rehta hai |
| Ek task, ek session, poori attention | Kai chote runs, mostly unattended, attention sirf gate par |

**2 cheezein jo loop kabhi nahi le sakta:**
1. **Intent** — itna clearly bataana ke result check ho sake
2. **Accountability** — jo ship ho uski zimmedari lena

**4 Nested Layers** (har ek pichli ko wrap karta hai, har ek ek alag failure rokti hai):

```
┌─────────────────────────────────────────────┐
│ 4. Loop Engineering — poora system: kis      │
│    cheez par kaam, kab start, kab "done"?    │
│  ┌─────────────────────────────────────────┐ │
│  │ 3. Harness Engineering — model ke around │ │
│  │    ka code: tools chalata, errors handle │ │
│  │   ┌───────────────────────────────────┐  │ │
│  │   │ 2. Context Engineering — model    │  │ │
│  │   │    ek turn mein kya dekhta hai    │  │ │
│  │   │  ┌─────────────────────────────┐  │  │ │
│  │   │  │ 1. Prompt Engineering — sirf │  │  │ │
│  │   │  │    woh alfaz jo aap likhte   │  │  │ │
│  │   │  └─────────────────────────────┘  │  │ │
│  │   └───────────────────────────────────┘  │ │
│  └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

**Har layer ek failure mode rokti hai:** No context → model guess karta hai. No harness → aap akele checker hain. No loop → schedule bhi aap hi hain. **Self-check:** "In layers mein se kaunsi mein abhi bhi hath se kaam kar raha hoon?"

### Chota Loop vs Bara Loop (Yeh Book Ki Sabse Confusing Cheez Hai)

**Chota loop (inner loop)** — har agent ke andar chand lines ka cycle:

```python
while True:
    reply = model(context)
    if not reply.tool_calls:
        break                     # model ne KHUD decide kiya "main done hoon"
    context += run_tools(reply.tool_calls)
```

`break` wali line dekho — **model apna khud judge hai**. Common failure: agent file change karta hai, "Done! All fixed." likhta hai, kabhi tests chalata hi nahi. Turn khatam, task nahi.

Isiliye **outside stops** chahiye (jo model ki apni opinion par depend nahi karte):
- **Checked condition** — real test se prove karo
- **Limit** — max tries
- **No-progress check** — kuch behtar nahi ho raha to ruko
- **Separate checker** — dusra process grade kare

**Bara loop (outer loop, yeh poora course)** — **manager** hai. Decide karta hai kaunsa kaam dena hai, kab start karna hai, kaise grade karna hai, kal ke liye kya yaad rakhna hai. Chote loop ka **ek poora run = ek "beat"**. Chota loop ka koi heartbeat/spine nahi hota — beat khatam hote hi sab bhool jata hai.

---

## 2. Loop Ke 6 Parts — Poora Anatomy

```
┌───────────────────────────────────────────────────────────────┐
│  1. HEARTBEAT         schedule/event jo beat start kare        │
│     (iske bina: ek run, loop nahi)                             │
├───────────────────────────────────────────────────────────────┤
│  2. WORKTREE           isolation, parallel agents collide na    │
│     karein (per-task checkout)                                 │
├───────────────────────────────────────────────────────────────┤
│  3. SKILL              project knowledge, ek baar likhi        │
│     (koi run zero se shuru nahi karta)                         │
├───────────────────────────────────────────────────────────────┤
│  4. SUBAGENTS           maker aur checker — ek likhta hai,     │
│     ek check karta hai                                         │
├───────────────────────────────────────────────────────────────┤
│  5. CONNECTOR (MCP)     asli tools mein act kare — PRs, tickets│
│     (act, sirf suggest nahi)                                   │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│  6. STATE / MEMORY — THE SPINE                                 │
│     Disk par file (CLAUDE.md/AGENTS.md + progress file), ya    │
│     board (Linear). Model bhool jata hai. Repo nahi bhoolta.   │
│     ★ NO SPINE, NO LOOP ★                                       │
└───────────────────────────────────────────────────────────────┘
                          ↓
              Beat ke end mein: HUMAN GATE
      Safe work → commit/PR   |   Risky/unsure → insaan tak
```

**Yeh code ke ilawa bhi kaam karta hai.** Yeh book khud markdown files ka ek repo hai — nightly link check, style sweep, stale-model-name flag — sab loops hain isi chapter se. Sirf **checker** badalta hai: code ke paas honest checkers (tests, linters) hain, prose ke paas nahi. Isliye writing loop mechanical checks (broken links) + rubric-with-a-bar reviewer use karta hai: *"Grade this draft against the rubric. Do not stop below 95."* — score ek soft judgment ko action-able stopping condition mein badal deta hai.

### Checker Ladder — 3 Qisam Ka "Done", Weakest Se Strongest

```
        STRONGEST                                    WEAKEST
┌──────────────────┐  ┌────────────────────┐  ┌──────────────────┐
│ 1. Passing test   │  │ 2. Mechanical      │  │ 3. Rubric with   │
│    (code)         │  │    checks (prose)  │  │    a bar          │
│                    │  │                    │  │                  │
│ Test runner/linter │  │ Broken links,      │  │ Reviewer agent   │
│ decide karta hai.  │  │ missing figures,   │  │ grade karta hai. │
│ Command khud ko    │  │ banned words,      │  │ "Do not stop     │
│ convince nahi kar  │  │ heading levels.    │  │ below 95."       │
│ sakti.             │  │                    │  │                  │
│                    │  │ = "partial proof"  │  │ Score ek OPINION │
│ = "PROOF"          │  │                    │  │ hai, proof nahi. │
│                    │  │                    │  │                  │
│                    │  │                    │  │ = "CLAIM, not    │
│                    │  │                    │  │   proof"         │
└──────────────────┘  └────────────────────┘  └──────────────────┘
        │                       │                       │
        ▼                       ▼                       ▼
  narrow gate            wider gate            widest gate:
  (spot-checks)          (judge content)        ek insaan parhta hai
```

**Jitna kamzor checker, utna zyada kaam human gate se guzarta hai.** Yeh failure nahi — method aapko bata rahi hai judgment kahan rehna chahiye.

---

## 3. Part 2 — Heartbeats: Poori Detail

Ek idea sab 4 ke neeche: loop ek single action nahi, **"do this, wait, do it again"** hai — kuch to jaaga rehna chahiye beats ke darmiyan. Sawal: **woh kahan rehta hai?**

| Heartbeat | Timer Kahan | Beats Ke Darmiyan Kya Jaaga |
| --- | --- | --- |
| In-session `/loop` | Session ke andar | Aapka open session |
| Scheduled/Routine | Bahar, scheduler mein | Scheduler (jo har tick par fresh run banata hai) |

### Concept 4 — In-Session Loops

Kitchen timer jaisa. `/loop`:

```text
/loop 5m check if the deployment finished and tell me what happened
```

Cancel karna:
```text
show my running loops
cancel the deploy-check loop
```

**Real project — ISS watch:**
```bash
git clone https://github.com/panaversity/agentfactory-labs.git
cd agentfactory-labs/crash-course/loop-eng/iss-loop
claude
```
```text
/loop show me the location of the ISS every minute
```
Terminal band karo → watching mar jati hai. **Yehi in-session loop ki definition hai.**

**OpenCode equivalent** (koi `/loop` command nahi, shell se banao):
```bash
while true; do
  opencode run "check if the deployment finished; if it did, say DONE"
  sleep 300   # 5 minutes
done
```
MCP/config start-up cost bachane ke liye:
```bash
opencode serve --port 4096 &
opencode run --attach http://localhost:4096 "check the deploy status"
```

**3 rungs — kitna jaaga rehta hai:**

| Rung | Option | Terminal band ho to bhi chalta hai? | Laptop so jaye to bhi chalta hai? |
| --- | --- | --- | --- |
| Bottom | In-session `/loop` | Nahi | Nahi |
| Middle | Background session (`claude --bg`) carrying `/loop` | Haan | Nahi |
| Top | Scheduled task/Routine | Haan | Haan (cloud) |

### Concept 5 — Conditional Loop (Run-Until-Done)

Fixed-timer loop ko nahi pata kaam khatam hua ya nahi. **Conditional loop isliye rukta hai kyunki kaam khatam ho gaya** — ek alag command/checker decide karta hai.

```text
/goal All tests in test/auth pass and `npm run lint` is clean.
```
Ek alag smaller model (Haiku default) transcript parhta hai aur poochta hai "kya hum done hain?" — commands khud nahi chala sakta, sirf transcript parh sakta hai.

**OpenCode equivalent:**
```bash
for i in $(seq 1 8); do          # cap — kabhi infinite loop mat karo
  opencode run "Make the tests in test/auth pass and fix any lint errors."
  if npm test -- test/auth && npm run lint; then
    echo "Condition met on try $i"; break
  fi
done
```

**Har loop ko 3 stops chahiye:**

| Stop | Kya Hai | Na Ho To Kya Hota Hai |
| --- | --- | --- |
| Success condition | "Done" kaise pata chalta hai | Kuch define nahi karta "done" ka matlab |
| Limit | Max tries/minutes/spend | Impossible goal poora token budget kha jata hai |
| No-progress check | Same action same arguments repeat ho raha? | Poori limit ek hi galti repeat karne mein jati hai |

**Ralph loop:** sabse simple well-known run-until-done loop online — wahi prompt baar-baar, ek state file parhta/update karta hai. Sirf 2 stops (success + time cap), koi stuck-check/skill/alag checker nahi. Vague condition wala Ralph loop time khatam hone tak bhatakta hai.

**Doom loop:** lambi run apna context junk se bhar leti hai → messy context → galat decision → aur mess. Defense: **compact** karo (summary se replace), bare outputs **files** mein rakho, messy subtasks **subagent** ko do. Context = budget, bucket nahi.

### Concept 6 — Unattended Schedules

**Routine ke 4 parts:**
1. **Prompt** — self-contained standing instruction
2. **Repos** — kaunse repos touch kar sakta hai
3. **Connectors** — kya reach kar sakta hai (Slack, email)
4. **Trigger** — schedule, API call, ya GitHub event

**Cron (laptop on, no Anthropic cloud):**
```bash
0 9 * * 1-5 cd /path/to/repo && claude -p "check the CI dashboard and summarize any failures" >> ~/claude-cron.log 2>&1
```

**OpenCode — GitHub Actions (koi machine on nahi chahiye):**
```yaml
name: Scheduled OpenCode Task
on:
  schedule:
    - cron: "0 9 * * 1-5"   # weekdays 9am UTC
jobs:
  opencode:
    runs-on: ubuntu-latest
    permissions: { contents: write, pull-requests: write, issues: write }
    steps:
      - uses: actions/checkout@v6
        with: { persist-credentials: false }
      - uses: anomalyco/opencode/github@latest
        env: { ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }} }
        with:
          model: anthropic/claude-sonnet-5
          prompt: |
            Review the codebase for TODO comments and summarize them.
            If any are worth acting on, open an issue to track them.
```

**Daily cap (launch-time numbers):** Pro 5/din, Max 15/din, Team/Enterprise 25/din. One-off runs cap mein count nahi hote. **Default: sirf `claude/` branches par push** — `main` tak seedha nahi, yeh safety hai.

### Concept 7 — Event-Driven

| Event Kahan Se Ata Hai | Use Karo | Kaam Kahan Chalta Hai | Laptop Band? |
| --- | --- | --- | --- |
| GitHub (PR, release) | Routine, GitHub trigger | Fresh cloud session, per event | Chalta hai |
| GitHub, bina Routine ke | Claude Code GitHub Action (CI) | Fresh CI runner, per event | Chalta hai |
| Chat message (Telegram/Discord) | Channel | Already-running session | Nahi, machine chahiye |
| Kuch bhi jo web request bhej sake | Routine, API trigger | Fresh cloud session, per call | Chalta hai |

**Asal rule:** sawal "yeh Routine hai?" nahi — **"kaam kis ke computer par chalta hai?"** Aapki machine band hote hi mar jati hai. Anthropic/GitHub ke servers kabhi aapke the hi nahi — isliye unhe token chahiye, aapka laptop pehle se janta tha aap kaun hain.

**OpenCode — PR review Action:**
```yaml
name: opencode-review
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]
jobs:
  review:
    runs-on: ubuntu-latest
    permissions: { contents: read, pull-requests: read }
    steps:
      - uses: actions/checkout@v6
        with: { persist-credentials: false }
      - uses: anomalyco/opencode/github@latest
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          model: anthropic/claude-sonnet-5
          use_github_token: true
          prompt: |
            Review this pull request for bugs, quality issues, and security risks.
```

**Heartbeat chunne ka decision tree:**
```
Task khatam hoti hai, command prove kar sakti hai?  → CONDITIONAL loop
Task repeat hoti hai?                                → SCHEDULE ya EVENT
Task ek hi baar hoti hai?                            → KOI LOOP NAHI (normal session)
```

---

## 4. Part 3 — The Body: Poori Detail

### Concept 8 — Isolation (Worktrees)

```bash
git worktree add ../wt-feature-a feature-a
git worktree add ../wt-feature-b feature-b
( cd ../wt-feature-a && opencode run "implement feature A" ) &
( cd ../wt-feature-b && opencode run "implement feature B" ) &
wait
```
Claude Code: `--worktree` flag, ya subagent par `isolation: worktree`.

### Concept 9 — Skills

`SKILL.md` mein project knowledge — **anything you'd re-explain every run** yahan jata hai. Loop prompt ek line ban jata hai: *"run the daily-triage skill"* — chota prompt, easy-to-update logic, kam token cost per beat.

### Concept 10 — Connectors (MCP)

**3 rules kyunki yeh loop mein hai:**
1. **Kam, focused tools** — model har beat par bina dekhe tool chunta hai; 100 overlapping tools mein bhatak jata hai. Anthropic ka rule: agar human engineer certain nahi keh sakta kaunsa tool fit karta hai, agent bhi nahi.
2. **Writes safe-to-repeat honi chahiyein** — retry ek "create customer" dubara chalaye to duplicate + double billing. Update-or-create prefer karo, blind creates nahi.
3. **Error messages clear hon** — error message hi agle beat ka input hai. "Permission denied: request repo scope" khud fix ho jata hai. "Error 403" ek beat waste karta hai.

### Concept 11 — Maker-Checker (Subagents)

**Sab se important choice: jo agent kaam banata hai, wahi khud approve nahi karta.**

**Claude Code** subagent (`.claude/agents/reviewer.md`):
```markdown
---
name: reviewer
description: Reviews a diff against the spec and the test results. Replies PASS or FAIL with reasons. Makes no changes.
tools: Read, Bash
model: claude-haiku-4-5-20251001
---

You are a strict, read-only code reviewer. You never edit files.

1. Run the tests and the linter. Read the output yourself. Do not trust a claim
   that they pass.
2. Check the change against the project conventions in `CLAUDE.md` and the
   relevant spec.
3. Look for bugs, missing edge cases, security risks, and any change to public
   behaviour.

Then reply with exactly one of:
- `PASS` — followed by one line saying what you verified.
- `FAIL` — followed by the specific reasons, one per line.
```

**OpenCode** subagent (`.opencode/agents/reviewer.md`):
```markdown
---
mode: subagent
model: anthropic/claude-haiku-4-5-20251001
description: Reviews a diff against the spec and tests. Replies PASS or FAIL with reasons. Read-only.
permission:
  edit: deny
  bash:
    "*": deny
    "npm test*": allow
    "npm run lint*": allow
    "git diff*": allow
---

You are a strict, read-only code reviewer. You never edit files.
1. Run the tests and the linter. Read the output yourself.
2. Check the change against project conventions in `AGENTS.md` and the spec.
3. Look for bugs, missing edge cases, security risks, behaviour changes.

Reply with exactly one of:
- PASS — followed by one line saying what you verified.
- FAIL — followed by the specific reasons, one per line.
```

Subagent zyada tokens kharch karta hai — wahan use karo jahan real matter kare (kuch bhi jo aapki gair-mojoodgi mein commit hoga).

### Interlude — Dynamic Workflows (Body Ko Ek Re-Runnable Unit Banana)

Body (kaam dhoondo, worktree mein draft karo, alag agent se grade karwao) ko **script** ki tarah likha ja sakta hai:

```text
use a workflow to draft fixes for these three issues in parallel worktrees,
and have a reviewer grade each one
```
`ultracode` keyword se start hoti hai, ~16 agents ek waqt, 1000/run cap. `/workflows` view mein `s` dabao usay `/command` save karne ke liye.

> **Sabse asaan galti:** Workflow **loop nahi hai**. Ek baar chalta hai, khatam hone par sab bhool jata hai. **Workflow = engine. Trigger (Routine/cron/`/loop`) = key jo engine start karti hai. `progress.md` = agli trip tak information carry karta hai.**

### Interlude — Verification Skills (Checker Ko Codify Karna)

**Test:** jo bhi cheez aap **har baar hath se correct karte ho**, likh do.

```markdown
# .claude/skills/verify-log-hygiene/SKILL.md  (ya .opencode/skills/…)
---
name: verify-log-hygiene
description: Check that error logs include the request ID and never
  include the request body. Use when the diff touches error handling
  or logging.
allowed-tools: [Read, Edit, Grep]
---

Read the error-handling paths in the current diff.

For each log call on an error path, confirm it includes the request ID
and does not pass the request body, headers, or any user-supplied
payload.

Report each violation with file:line, then fix it: add the request ID
where it's missing and strip the payload from the log call.
```

**4 possible ghar, har ek ek alag heartbeat:**

| # | Ghar | Kya | Kis Ke Liye |
| --- | --- | --- | --- |
| 1 | Standalone | Aap khud invoke karo | Checks jo har change par apply nahi hote — pre-commit security scan |
| 2 | Embedded | Producing skill ke end mein ek line add: *"After creating the component, run eslint..."* | Aap khud skills jo edit kar sakte ho |
| 3 | Chained | Ek skill dusri ko end mein call kare (`/code-review` → `/simplify` → `/verify` → `/design`) | Skills jo aap edit nahi kar sakte (wrapper skill likho) |
| 4 | Har PR par | Doorbell event heartbeat, check as prompt | Team-wide gate — personal se team infrastructure ban jata hai |

**Graduation rule:** home 4 se shuru mat karo. Signal: aap khud usay har change ke baad chalate paate ho → embed/chain karo. PR-wide gate se pehle wait karo jab tak chain stable ho.

---

## 5. Part 4 — The Spine: Poori Detail

**Model har run ke baad sab kuch bhool jata hai.** Do files:

- **Rules file** (`CLAUDE.md`/`AGENTS.md`) — steady habits, har run par padhi jati hai (short rakho, har beat par cost hoti hai)
- **Progress file** (`progress.md`) — kya try hua, kya pass hua, kya khula hai

```markdown
<!-- progress.md — the loop's memory between runs -->

## Done

- 2026-06-22: fixed flaky test in test/auth (retry on token refresh)

## In progress

- Dependency audit: 3 of 7 advisories patched; lodash bump blocked by an API change

## Open / needs a human

- CVE-2026-xxxx in image lib — the fix changes the output format, escalating to a maintainer
```

**Habit:** har run **start mein padhta hai, end mein update karta hai.**

**Intern ki diary:** front mein sabak (mistakes se seekha), roz padho. Back mein kal kya kiya kahan chhoda, roz likho. Front = rules file, back = progress file. Bina diary ke intern aur loop roz wahi galtiyan repeat karte hain.

**Industry bhi isi par pahunchi (Anthropic, ek saal ki koshish ke baad):**
1. `CLAUDE.md` (bloats)
2. In-session memory tools (too opinionated)
3. Skills (growth solve hui — short description, on-demand full body)
4. **Current best practice:** memory ko **plain file system** ki tarah model karo — markdown files, `grep`/shell se search, koi special memory API nahi.

### Dreaming — Loop Jo Loop Ko Improve Karta Hai

Rules-file mein lesson likhna = **hill-climbing loop** (output = system mein improvements, kaam nahi). **Dreaming** = out-of-band, managed version:

```
Weekly heartbeat
  → memory store + recent run transcripts collect karo
  → orchestrator subagents ko baant deta hai
  → repeat hone wale patterns dhoondo
  → memory store mein changes propose karo, evidence ke sath (kaunsi runs, kitni baar)
  → HUMAN accept/reject karta hai har change se pehle
```

School analogy: students (working agents) kaam karte hain, head teacher (dreaming pass) sab marked papers dekhta hai, poori class ek hi sawal fail kar rahi hai — curriculum fix karta hai, koi student class time waste nahi karta.

**2 tareeqe galat ja sakti hai:**
- **Memory poisoning** — ek run ke input mein plant ki gayi instruction memory mein likhi jati hai, har baad ka run steer karti hai. Defense: evidence hamesha cite ho, human gate hamesha rahe.
- **Brevity bias + context collapse** — rewrite general point rakhta hai, specifics kho deta hai; har rewrite lossy copy hoti hai. Defense: **chote diffs, kabhi poore rewrites nahi.** Memory file mein kabhi relative date mat likho.

**Khud banane ka recipe (dreaming loop capstone):**
1. Heartbeat: weekly, daily nahi (batch chahiye patterns ke liye)
2. Input: apne loops ko transcripts likhne do
3. Body: orchestrator + analyst subagents
4. Maker-checker, do baar: analysts propose, orchestrator sirf enough-evidence patterns rakhta hai, phir loop **kabhi rules file/skill seedha edit nahi karta** — `claude/` branch par draft karta hai, PR khol deta hai jispar evidence hota hai
5. Human gate: aap merge karte ho, ya close
6. Apni spine: `dreaming-state.md` — last-reviewed batch ki date

---

## 6. Part 5 — Poora Real Loop, Code Ke Sath (Book Se Exact)

### Minimum Safe Loop Checklist (7 Cheezein)

```
[ ] 1. Success condition   — kaam kaise pata done hai (Concept 5)
[ ] 2. Limit                — max tries/minutes/spend (Concept 13)
[ ] 3. Isolated worktree    — parallel work collide na ho (Concept 8)
[ ] 4. Read-only checker    — grade karta hai, edit nahi (Concept 11)
[ ] 5. State file           — spine, runs ke darmiyan yaad rakhti hai (Concept 12)
[ ] 6. Human gate           — risky/failed kaam insaan tak, kabhi seedha main nahi (Part 5)
[ ] 7. Log/notification     — overnight failure visible ho, chup na ho (Part 6)
```

### Loop Ka Shape (Dono Tools Mein Same)

```
1. Heartbeat:      har weekday 9am
2. Skill:           `daily-triage` skill steps rakhti hai, prompt ek line rehta hai
3. Spine:            progress.md start mein padho, end mein update karo
4. Worktree:         har fix apne checkout mein draft hota hai
5. Maker-checker:    implementer draft karta hai, alag reviewer PASS/FAIL kehta hai
6. Connector:        PASS par PR khol do. FAIL/risky par "needs a human" mein likho, ruko
```

### Step 1 — Shared Skill (Dono Tools Mein Same File)

Save karo: `.claude/skills/daily-triage/SKILL.md` (Claude Code) ya `.opencode/skills/daily-triage/SKILL.md` (OpenCode).

```markdown
---
name: daily-triage
description: >-
  Runs the morning maintenance pass. Reads the progress file, gathers overnight
  CI failures, open issues, and new audit advisories, drafts safe fixes (each
  one checked by a separate reviewer agent), opens pull requests for what passes,
  and writes anything risky to the progress file for a human. Use this for the
  scheduled morning maintenance loop.
---

# Daily triage

You are the morning maintenance loop. Work through these steps in order.
Do not skip the progress file. It is your only memory between runs.

## 1. Read your memory first

- Open `progress.md`. Read the "In progress" and "Open / needs a human" sections.
- Do not redo anything already listed under "Done".

## 2. Find the work

Gather candidates in this order, and stop once you have at most 5:

1. CI runs that failed since the last entry in `progress.md`.
2. Open issues labelled `bug` or `maintenance`.
3. New advisories from `npm audit` (or this project's audit command).

## 3. Work each candidate

- Create an isolated checkout: a git worktree, or a fresh branch named
  `claude/<short-slug>`.
- Draft the smallest fix that solves the one problem. Do not bundle changes.
- Send the diff to the reviewer agent. Wait for its verdict before going on.

## 4. Decide from the verdict

- PASS, and the change is low risk (no public API change, no data migration,
  no file deletion): open a pull request. Title it `fix: <one short line>` and
  link the issue.
- FAIL, or the change touches anything risky: do NOT open a pull request. Add a
  short entry to the "Open / needs a human" section of `progress.md`. Say what
  you tried and why you stopped.

## 5. Update your memory last

- Move finished items to "Done" with today's date.
- Save `progress.md`. This is the file tomorrow's run will read.

## Rules

- Never open more than 5 pull requests in one run.
- Never change `main` directly. Only `claude/*` branches.
- When in doubt, escalate. A flagged item a human checks is always safer than a
  wrong fix shipped while no one was watching.
```

### Step 2 — Reviewer (The Checker)

**Claude Code** (`.claude/agents/reviewer.md`):
```markdown
---
name: reviewer
description: Reviews a diff against the spec and the test results. Replies PASS or FAIL with reasons. Makes no changes.
tools: Read, Bash
model: claude-haiku-4-5-20251001
---

You are a strict, read-only code reviewer. You never edit files.

1. Run the tests and the linter. Read the output yourself. Do not trust a claim
   that they pass.
2. Check the change against the project conventions in `CLAUDE.md` and the
   relevant spec.
3. Look for bugs, missing edge cases, security risks, and any change to public
   behaviour.

Then reply with exactly one of:

- `PASS` — followed by one line saying what you verified.
- `FAIL` — followed by the specific reasons, one per line.

A change that only "looks fine" is not a PASS. The tests must actually pass, and
the change must do only what was asked.
```

**OpenCode** (`.opencode/agents/reviewer.md`):
```markdown
---
mode: subagent
model: anthropic/claude-haiku-4-5-20251001
description: Reviews a diff against the spec and tests. Replies PASS or FAIL with reasons. Read-only.
permission:
  edit: deny
  bash:
    "*": deny
    "npm test*": allow
    "npm run lint*": allow
    "git diff*": allow
---

You are a strict, read-only code reviewer. You never edit files.

1. Run the tests and the linter. Read the output yourself. Do not trust a claim
   that they pass.
2. Check the change against the project conventions in `AGENTS.md` and the
   relevant spec.
3. Look for bugs, missing edge cases, security risks, and any change to public
   behaviour.

Reply with exactly one of:

- PASS — followed by one line saying what you verified.
- FAIL — followed by the specific reasons, one per line.

A change that only "looks fine" is not a PASS. The tests must actually pass, and
the change must do only what was asked.
```

### Step 3 — Heartbeat Wire Karna

**Claude Code — Routine** (`claude.ai/code/routines`, weekday-9am schedule):
```text
Run the daily-triage skill.
Start by reading progress.md; finish by updating it.
For each fix: draft it in an isolated worktree, have the reviewer subagent grade it,
open a PR only on PASS, and append anything risky to the "needs a human" section.
```
`isolation: worktree` parallel fixes ko alag rakhti hai. GitHub connector PRs kholta hai. Cloud Routine hone ki wajah se 9am par chalti hai chahe laptop khula ho ya nahi. Weekday-9am = 5 runs/week — Pro cap (5/day) mein aaram se fit.

**OpenCode — GitHub Actions workflow:**
```yaml
name: morning-maintenance
on:
  schedule:
    - cron: "0 9 * * 1-5"
jobs:
  triage:
    runs-on: ubuntu-latest
    permissions: { contents: write, pull-requests: write, issues: write }
    steps:
      - uses: actions/checkout@v6
        with: { persist-credentials: false }
      - uses: anomalyco/opencode/github@latest
        env: { ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }} }
        with:
          model: anthropic/claude-sonnet-5   # confirm with `opencode models`
          prompt: |
            Run the daily-triage skill.
            Read progress.md first; update it last.
            For each candidate fix: draft it on a new branch, then invoke the
            @reviewer subagent to grade it. Open a PR only when the reviewer
            replies PASS. Append anything risky to the "needs a human" section
            of progress.md and leave it for the maintainer.
```
`reviewer` agent (cheap, read-only model) checker hai. Naye branches = worktree isolation CI mein. OpenCode GitHub app PRs kholta hai. Apni machine par chahiye to same prompt `cron` line se `opencode run` chalati hai — sirf heartbeat badalta hai.

### Step 4 — Ek Real Morning Kaisi Dikhti Hai

```text
[09:00] daily-triage fires
  → reads progress.md: 1 item still "in progress" (lodash bump), nothing new flagged
  → finds: 2 CI failures overnight, 1 new npm-audit advisory
  → CI failure #1 (flaky auth test):
        drafts fix on branch claude/fix-auth-retry
        reviewer → PASS (tests green; retries on token refresh; no API change)
        → opens PR #142, links the issue
  → CI failure #2 (type error in report.ts):
        drafts fix on branch claude/fix-report-types
        reviewer → PASS → opens PR #143
  → advisory (image library):
        the safe fix changes the output format
        reviewer → FAIL (public behaviour change)
        → writes it to "Open / needs a human" in progress.md, opens no PR
  → updates progress.md, exits
[you, 09:30] two PRs to review, one flagged item to decide on. You typed nothing.
```

**Kya rok raha tha galat fix ko merge hone se aap sote waqt?** Teen cheezein: reviewer ko PASS wapis dena zaroori tha (maker-checker), sirf low-risk changes PR khol sakti hain, aur human gate risky/failed kaam ko "needs a human" note mein bhejta hai, `main` mein nahi. Har run bhi capped aur logged hai.

**Dono tools mein sirf ek asal farq tha: heartbeat aur run kahan hua.** Beech ka sab kuch (skill, spine, worktree, maker-checker, connector) same design tha.

---

## 7. Part 6 — Human Control (Sabse Important Part)

### 3 Feedback Loops, Ek Dusre Ke Andar

```
┌──────────────────────────────────────────────────────┐
│  OUTSIDE LOOP (days) — real users use karte hain      │
│  ┌──────────────────────────────────────────────────┐│
│  │  FEEDBACK LOOP (hours) — aap try karte ho, decide ││
│  │  karte ho kya badalna hai (spec + evals yahan)    ││
│  │  ┌────────────────────────────────────────────┐  ││
│  │  │  CODING LOOP (minutes) — agent likhta hai,  │  ││
│  │  │  test karta hai, fix karta hai — jo aapne    │  ││
│  │  │  Part 5 mein banaya                          │  ││
│  │  └────────────────────────────────────────────┘  ││
│  └──────────────────────────────────────────────────┘│
└──────────────────────────────────────────────────────┘
```

Agent teenon khud nahi chala sakta — **Andrew Ng ka "context advantage":** aap kuch jante ho jo agent nahi janta (kaun use karega, unhe asal mein kya chahiye, "acha" kaisa lagta hai). Jab tak aap kuch aisa jante ho jo agent nahi, aap loop mein rehte ho usay batane ke liye. Machine fast loop chalati hai; aap **kya banana hai** aur **kaun zimmedar hai** decide karte ho.

### Concept 13 — Token Cost

- Har loop **cap** karo
- Model job se match karo (plan/check ke liye strong, kaam ke liye cheap) — Claude Code mein `/effort` beat ko bhi match karo
- Loop prompt + rules file **chota** rakho
- Kam frequency par chalao (hourly ~12x sasta hai 5-minute se)

**Real numbers:** 1 beat (maker+checker) ~40,000 tokens read, ~6,000 write. Sonnet ($3/M input, $15/M output) par **~$0.20/beat**. 5 beats/din × 20 din = **~$20/month**. Wahi loop har 5 min chale (24/7) = 100+ guna zyada beats = **$1,000+/month**, same kaam ke liye. **Frequency drive karti hai, command ka naam nahi.**

**OpenCode mein model bhi lever hai:** sasta maker + trustworthy checker pattern. Kamzor maker zyada failed attempts de sakta hai jo savings kha jati hain.

> **Achi spine bhi cost lever hai:** memory-rich agent doosri baar behtar karta hai (pehli attempt ka lesson pehle se disk par) — kam retries, kam tokens.

### Concept 14 — Checking The Work Is Still Your Job

Loop chalne se aapka job khatam nahi hota — **move** hota hai. Aap ab har step type nahi karte, lekin aap wohi ho jo confirm karta hai ke loop ne asal mein kaam karne wala code ship kiya.

**Jab kai loops chalte hain (organization-level):**
- **Failure math:** 5 steps ek line mein, har ek 95% reliable — sirf ~3 mein se 4 runs clean khatam hoti hain. Galtiyan **spine ke andar** accumulate hoti hain — aaj ki galat line kal ka galat starting point hai
- **Loop kya kar sakta hai limit karo, sirf kya review karte ho nahi** — har part ek **standing permission** hai (schedule = permission so'te waqt act karne ki, connector = real system tak standing access)
- **Counting question:** kitne loops team chalati hai? Har ek kya touch kar sakta hai? Kis ki identity se act karta hai? — yeh workforce management hai, loop engineering nahi

**Shared memory (kai loops, ek store):** 4 guardrails — **versioning** (git-tracked spine free mein deta hai), **conflict checks before writing**, **permissions by level** (scratch space free, org-wide rules read-only + review), **portability** (open format).

### In / On / Out of the Loop (Industry Ke Naam)

| Term | Matlab | Yahan Kahan Bana |
| --- | --- | --- |
| **Human IN the loop** | Har action se pehle approve — slow, zyada control | Turn-by-turn prompting, plan mode, human gate merge par |
| **Human ON the loop** | System khud chalta, insaan dekh/rok sakta hai — fast | Routine `claude/` push, subah review |
| **Human OUT of the loop** | Koi dekh nahi raha | **Kabhi acceptable nahi** — third option nahi, **failure mode hai** |

**3 baatein:** (1) Prompting = IN, loop engineering aapko **ON** move karti hai. (2) Achi loop **mix** hoti hai, per-action set — safe fixes on-the-loop, risky in-the-loop. Checker ladder mix decide karti hai: **passing test autonomy kamata hai, rubric score nahi.** (3) **"Out of the loop" wahin hai jahan AI Gravity khinchti hai** — drift se hota hai, design se nahi.

### Concept 15 — Understanding Gap

> "Two people can build the exact same loop and get opposite results. One uses it to move faster on work they understand deeply. The other uses it to avoid understanding the work at all. **Build the loop. But build it like someone who plans to stay the engineer, not just the person who presses go.**"

**AI Gravity** (MIT Sloan, Eric So) — force jo hamesha zyada AI se kaam karwane khinchti hai. Loop se strong ho jata hai kyunki so'te waqt bhi chalta hai. Chorho isay: **Intent** "keep it working" tak simplify, **Accountability** green checkmarks trust karne tak.

### Observability — Jab Unattended Loop Fail Ho

```
[ ] Output wahan bhejo jahan dekhoge (log/Slack/Discord Channel, band terminal nahi)
[ ] Har run par ek line likho, FAIL par bhi — silent failure sab se bura
[ ] Runs replayable rakho (opencode export, Routine run history)
[ ] Limit par LOUDLY fail ho, "needs a human" note chorho
[ ] Overnight se pehle prove karo:
      Cadence:    hourly-watched → phir nightly-unattended
      Capability: report-only → fixes-behind-gate → phir unattended action
```

---

## 8. Routines Appendix — Poora Field Guide (A1-A6)

### Quick-Reference Table

| Default/Behavior | Risk | Fix |
| --- | --- | --- |
| "Local" option New-routine dialog | Desktop task ko Routine samajh baithna | Remote = cloud routine, Local = Desktop task (A1) |
| Sab connectors included, writes allowed | Unattended agent har linked tool mein act kar sakta hai | Zaroorat se zyada har connector hatao (A2) |
| `.env` gitignored, cloud clone tak nahi pahunchta | Routine credentials na paye, fail ya improvise kare | Secrets env-variables panel mein, prompt mein bhi bata do (A4) |
| Fresh clone, fresh environment, har run | Loop apna pehla step forever repeat kare | Committed context/progress file, ya external board (A4) |
| Schedule floor 1 hour | Design 15-minute fires assume kare | API trigger + apna scheduler higher frequency ke liye (A3) |
| API bearer token ek baar dikhta hai, endpoint dedupe nahi karta | Lost token, webhook retries se duplicate runs | Turant store karo, prompt safe-to-repeat likho (A3) |
| GitHub events hourly capped, overflow **dropped** | Event-heavy loop chupke se kaam miss kare | Nightly reconciliation sweep, schedule trigger par (A3) |
| `matches regex` poora field test karti hai | `hotfix` "urgent hotfix for auth" match nahi karega | `.*hotfix.*`, ya `contains` use karo (A3) |
| Runs **aapki** identity carry karte hain, koi mid-run approval nahi | External actions ship hote hain aapke naam se, unreviewed | Two-routine gate: draft, phir human approve, phir API-fired executor (A4) |
| Green status = koi infra error nahi | Failed tasks successful lagti hain | Har baar run transcript parho (A5) |

### A1. Local Session ≠ Cloud Routine

Desktop app **New routine** button: **Remote** = cloud routine (yeh appendix). **Local** = [Desktop scheduled task](https://code.claude.com/docs/en/desktop-scheduled-tasks) — apni machine par, real files (unsaved changes bhi), sirf machine on hone tak. Local files chahiye → Desktop task. Laptop-closed guarantee/connectors/API/GitHub triggers chahiye → cloud routine.

### A2. Creation Form, Field By Field

- **Prompt** — self-contained honi zaroori hai. Koi permission prompt nahi, koi puchne wala nahi mid-run. Skill ko point karo, routine ka text chota rakho.
- **Repositories** — har run fresh clone hoti hai, default branch se. Default: sirf `claude/*` branches par push. **Allow unrestricted branch pushes** toggle isay hata deta hai — sirf jaan-boojh kar, ek repo par, jaisa key handover.
- **Environment** — network access, env variables, setup script (cached). **Default** = **Trusted** allowlist (registries, cloud APIs). Kuch aur chahiye → **Custom**, sirf woh domain allow karo.
- **Connectors** — **default: sab connected connectors included, writes allowed, bina puche.** Yeh sabse zaroori cheez hai har baar badalne ki — jo routine ko zaroorat nahi hai woh hatao.

### A3. Teen Triggers

**Schedule** — presets hourly/daily/weekdays/weekly. **1 hour floor.** Higher frequency chahiye → API trigger + apna scheduler. One-off runs cap mein count nahi karte.

**API** — `/fire` endpoint + bearer token (ek baar dikhta hai, turant store karo):
```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/<routine-id>/fire \
  -H "Authorization: Bearer <routine-token>" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```
> **Warning:** `/fire` endpoint mein koi built-in deduplication nahi hai, webhooks default se retry karte hain. Deduplicate/rate-limit sender par karo, aur prompt ko safe-to-repeat likho.

**GitHub events** — pull request + release events. `matches regex` **poora field** test karta hai (`hotfix` matlab exactly `hotfix`, `.*hotfix.*` likho). **Per-routine/account hourly caps, overflow dropped** (queued nahi) — event-heavy design ko nightly reconciliation sweep chahiye.

### A4. Secrets, State, Identity

- **Secrets env-variables panel mein, `.env` mein kabhi nahi** — `.env` gitignored hai, cloud clone tak kabhi nahi pahunchta
- **Har run zero se shuru hota hai** — fresh clone, fresh environment. Jo bhi yaad rakhna hai machine se pehle nikalna zaroori hai: repo mein push, external system mein write, board ka API
- **Routines aap ki tarah act karti hain** — commits/PRs/Slack posts sab aapki identity carry karte hain
- **Koi mid-run approval nahi** — gate **routines ke darmiyan** banao: Routine A draft karti hai, **human** review karta hai, approval Routine B ko API trigger se fire karta hai jo action leta hai

### A5. Runs Parhna

**"Green status matlab session bina infrastructure error ke khatam hui. Yeh iska proof nahi ke task succeed hua."** Blocked network requests, missing connector tools, task failures sab transcript mein hain, status column mein nahi. **Har baar transcript parho.**

### A6. Routine Checklist (Save Karne Se Pehle)

```
[ ] Repositories: sirf sahi repo, unrestricted pushes OFF
[ ] Prompt: self-contained, success condition + limit shamil
[ ] Connectors: jo zaroorat nahi unhe hatao
[ ] Environment: secrets variables panel mein, network access narrow
[ ] Trigger: jaan-boojh kar chuna, no accidental high-frequency
[ ] State: committed progress/context file ya external board
[ ] Human gate: draft PRs/branches/messages, no direct merge/deploy/payment
[ ] Test run: one-off/Run now se fire karo, TRANSCRIPT parho, status color nahi
```

---

## 9. System of Record — Loop Engineering Se Connection

Yeh section user ke explicit sawal ka jawab hai: loop engineering ka "system of record" concept se kya connection hai.

### 9.1 — Loop Ki Apni Spine, Ek Chota System of Record

Book khud kehti hai: **"the repo remembers what the model cannot."** `progress.md` aur `CLAUDE.md`/`AGENTS.md` ek loop ke liye **authoritative source of truth** hain — model ke context window (jo har run ke baad khatam ho jata hai) ke bahar rehte hain. Yeh exactly wahi shape hai jo ek "system of record" ki hoti hai: ek jagah jahan "kya sach hai" likha hota hai, aur woh jagah kisi bhi ek session/agent se zyada lambi umar rakhti hai.

```
System of Record ki 3 properties (generic definition):     Loop Ki Spine Mein:
─────────────────────────────────────────────────────      ────────────────────────
1. Authoritative — yehi asal jawab hai                  →  progress.md "Done"/"Open" sections
2. Durable — session khatam hone se zyada zinda rehta   →  disk par file, git-tracked
3. Queryable/readable by multiple actors                →  har naya run/agent isay padh sakta hai
```

### 9.2 — Connectors (MCP) Se Real Systems of Record Tak

Loop khud sirf ek **local** system of record (repo files) rakhta hai, lekin uske **Connectors (Concept 10)** usay **real, external systems of record** tak reach dete hain: GitHub issues, Linear board, Slack channel, database. Jab morning-triage loop ek PR kholta hai ya Linear ticket update karta hai, woh apni chhoti spine se **company-wide** system of record mein likh raha hota hai.

Yeh seedha AI Agent Factory book ke Mode 2 (Manufacturing) courses ke **"System of Record"** invariant se jorta hai (Course 4 — Connector-Native Apps / Digital FTE):

| Loop Engineering Course Mein | Manufacturing Track Mein (System of Record Invariant) |
| --- | --- |
| `progress.md` / `CLAUDE.md` — loop ki apni memory | Agent ka context window — chota, disposable |
| Connector (MCP) se GitHub/Linear/Slack mein likhna | MCP se authoritative data store mein likhna/parhna |
| "No spine, no loop" | "Authoritative data agent ke context ke bahar rehni chahiye" |
| Har naya beat repo se state parhta hai | Har naya agent run system of record se state parhta hai |
| Git = versioning, rollback free mein | Database/board = audit trail, history free mein |

**Ek line mein farq:** loop engineering ka spine **ek loop ke andar** ka system of record hai (usi repo mein, us loop ke liye). Manufacturing track ka "system of record" concept **poori company** ke liye hai (MCP se reach hone wala authoritative store, jise kai Workers/agents share karte hain). **Dono ka core idea same hai: authoritative truth model ke context se bahar rakho, taake har naya run/agent usay reliably padh sake.**

### 9.3 — Dreaming Bhi Isi Pattern Ka Extension Hai

Dreaming loop (Concept 12 ka improvement pass) is idea ko ek level upar le jata hai: **memory store khud ek system of record ban jata hai** jise kai loops share karte hain. Isi liye book **production guardrails** maangti hai jo kisi bhi real system of record ko chahiye hote hain: **versioning** (git), **conflict checks before writing**, **permissions by level** (org-wide rules read-only, sirf review se badalte hain), **portability** (open format). Yeh exact wahi discipline hai jo ek company database ko production-grade banati hai — loop engineering usay chote scale par phir se discover karti hai.

---

## 10. Full Glossary (15 Concepts Ke Sath Mapped)

| Concept # | Naam | Ek-Line Takeaway |
| --- | --- | --- |
| 1 | From prompting to looping | Aap sirf 2 cheezon ke zimmedar rehte ho: intent + accountability |
| 2 | What a loop is made of | 5 working parts + 1 spine; chota loop vs bara loop |
| 3 | Two ways to build a loop | Claude Code built-in tools deta hai; OpenCode raw parts deta hai — shape same hai |
| 4 | In-session loops | `/loop` — session khule tak chalta hai |
| 5 | Run-until-done | `/goal` — separate checker decide karta hai "done" |
| 6 | Unattended schedules | Routine/cron — laptop band ho tab bhi chalta hai |
| 7 | Event-driven | Doorbell — GitHub/Channel/API trigger, question hai "kis ke computer par" |
| 8 | Isolation | Worktrees — parallel agents collide na karein |
| 9 | Knowledge | Skills — project knowledge ek baar likhi jati hai |
| 10 | Action | Connectors/MCP — loop act karta hai, sirf suggest nahi |
| 11 | Maker-checker | Subagents — jo banata hai, khud grade nahi karta |
| 12 | State that survives | Spine — `progress.md`/`CLAUDE.md`, "no spine, no loop" |
| 13 | Token cost | Cap, model match, frequency kam, prompts chote |
| 14 | Checking the work | Aapka job move hua, khatam nahi hua |
| 15 | Don't lose understanding | AI Gravity — loop banao lekin engineer rehte hue |

---

*Yeh file `Loop-Engineering-Summary.md` ka poora, code-ke-sath companion hai. Har code block book se seedha liya gaya hai (book = is document ka system of record). Agar koi ek Concept ko aur deep dive chahiye ho, bata dena.*
