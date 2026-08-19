# Loop Engineering — Summary

Prompting se looping tak: ek chhota system banana jo khud shuru hota hai, kaam dhoondta hai, karta hai,
check karwata hai, memory update karta hai, aur sirf zaroori decisions ke liye insaan ko bulata hai. 12
practice projects + Routines appendix is repo mein `projects/` folder mein alag se implement/tested hain
(unki apni `SUMMARY.md` files hain, is file mein sirf top-level chapter concepts cover hote hain).

## 00 — Overview: Loop Engineering Kya Hai

- Prompting vs Looping table: aap start karte ho vs schedule/event start karta hai; aap parh kar decide
  karte ho vs checker+loop decide karta hai; type rukne pe kaam rukta hai vs aap sote waqt bhi chalta hai.
- 2 cheezein hamesha insaan ki: **intent** (saaf batana ke aapko kya chahiye) aur **accountability**
  (ship hue ki zimmedari).
- Inner loop (model↔tool, khud "done" decide karta hai) vs outer loop (yeh course — manager, kaam/schedule/
  grading/memory decide karta hai). **4 layers** waqt ke sath ubhre: prompt → context → harness →
  **loop engineering**.
- **Loop ke 6 parts:** heartbeat, worktree, skill, subagents (maker-checker), connector (MCP), spine
  (state/memory — **no spine, no loop**).
- Code-only nahi — kisi bhi repo (prose bhi) pe chalta hai, sirf checker badalta hai. Claude Code (built-in:
  `/loop`, `/goal`, `/schedule`, Routines) vs OpenCode (khud scheduler lagana, zyada control) — shape same.

## 01 — Heartbeats: Loop Kab Start Hota Hai

- **4 heartbeat kisam:** in-session (kitchen timer), conditional/run-until-done (taster), scheduled
  (alarm clock), event-driven (doorbell).
- **Concept 4 — In-session:** `/loop 5m <prompt>`; OpenCode `while true + sleep`. 3 rungs: bottom (session
  khuli), middle (`--bg`), top (scheduled/cloud). Real project: ISS Loop.
- **Concept 5 — Conditional:** `/goal <condition>` — chhota alag checker-model "done hain?" poochta hai.
  3 zaroori stops: success condition, limit, no-progress check. Ralph loop = simplest run-until-done
  (sirf success+time-cap). Doom Loop se bachao: compact, files mein bara output, subagent ko messy chores.
- **Concept 6 — Unattended schedules:** Claude Code Routines (4 blanks: prompt/repos/connectors/trigger).
  Daily cap (5 Pro/15 Max/25 Team), sirf `claude/` branches par push (default). OpenCode: apna cron/Actions.
  Real project: Sky Watch.
- **Concept 7 — Event-driven:** GitHub PR/release, Channels, API triggers. Asal sawal: "kaam kis ke
  computer pe chal raha hai" — laptop band, phir bhi chalta hai. Real project: The Doorbell.
- Konsa heartbeat chuno: command prove kar sakti → conditional; repeat hota → schedule/event; ek dafa →
  koi loop nahi.

## 02 — Body: Loop Har Run Mein Kya Karta Hai

- **Concept 8 — Worktrees:** parallel agents ek dusre ki files overwrite na karein. `--worktree` flag,
  `isolation: worktree` subagent field. OpenCode: `git worktree add`.
- **Concept 9 — Skills:** har run fresh session hai (koi memory), `SKILL.md` mein knowledge ek dafa likho.
  Prompt chhota rakho: "run the daily-triage skill."
- **Concept 10 — Connectors (MCP):** loop ko real tools tak reach (PR khol sakta hai, sirf suggest nahi).
  3 rules: kam/focused tools > overlapping tools; writes retry-safe hon (update-or-create); error messages
  agla step batayein.
- **Concept 11 — Maker-Checker/Subagents:** jo banata hai wo khud approve nahi karta (LLM-as-judge).
  `.claude/agents/` ya OpenCode subagents (`general`/`explore`/`scout`), checker ko sasta read-only model
  do. Extra tokens lagte hain — sirf wahan use karo jahan doosri opinion matter kare.
- **Interlude — Dynamic workflows:** poori orchestration ko ek re-runnable script (Claude Code). Warning:
  workflow **beat ka body hai, loop nahi** — na heartbeat, na spine. Loop = heartbeat + workflow + progress
  file combo.
- **Interlude — Verification skills:** "verification loop" — checker ko codify karo. Jo bhi haath se
  correct karte ho har dafa, wahi likhne layak. **4 Homes:** standalone (aap invoke), embedded (skill ke
  end mein), chained (`/code-review` → `/simplify` → `/verify`), har-PR-pe (team infra). Graduation rule:
  Home 4 se shuru mat karo.

## 03 — Spine: Runs Ke Darmiyan Memory

- Sab se zaroori fact: model runs ke darmiyan **sab bhool jata hai**. Fix: state ko model ke bahar, disk
  pe. **2 layers:** rules file (`CLAUDE.md`/`AGENTS.md`, chhoti rakho) aur progress file (`progress.md`,
  yehi asal spine hai — start mein parho, end mein update karo).
- Intern-diary analogy: diary front = rules file (permanent lessons), diary back = progress file
  (checkpoints). Diary nahi hoti to intern/loop wahi correction baar baar seekhta hai.
- Real project: Paper Watch — `progress.md` delete karo aur test karo, sab papers phir "naya" — no spine,
  no loop, ek command mein prove.
- Industry bhi isi design pe aayi: Anthropic ka memory research bhi "plain file system, grep se search"
  tak pahuncha.
- **Hill-climbing/Dreaming:** loop jo rules file mein lesson likh de = system improvement. Dreaming
  (Anthropic managed): memory+transcripts collect → subagents analyze → repeat pattern dhoondein →
  changes propose evidence ke sath → **insaan accept/reject**. Yeh wo loop hai jo **kabhi bina human gate
  ke nahi chalni chahiye.** 2 khatare: memory poisoning (defense: evidence+human gate), brevity
  bias/context collapse (defense: chhote diffs, poore rewrite nahi).

## 04 — Ek Complete Loop (Morning Triage Example)

- **Minimum Safe Loop Checklist (7 cheezein):** success condition, limit, isolated branch/worktree,
  read-only checker, state file, human gate, log/notification.
- Morning maintenance loop shape: heartbeat (9am weekday) → skill (`daily-triage`) → spine (progress.md)
  → worktree per fix → maker-checker (implementer + reviewer PASS/FAIL) → connector (PASS→PR, FAIL/risky→
  needs-a-human note).
- Full `daily-triage` SKILL.md aur `reviewer.md` (dono Claude Code + OpenCode) code diya gaya hai —
  memory-first, max 5 candidates, isolated checkout, PASS+low-risk→PR, never direct-to-main.
  Heartbeat wiring dono tools ke liye (Routine text / GitHub Actions yaml).
- Real-morning trace example: 2 CI failures → 2 PASS → 2 PRs; 1 advisory → FAIL (public behavior change)
  → escalated. Owner ne kuch type nahi kiya.

## 05 — Human Control: Insaan Loop Mein Kahan Khara Hai

- **3 nested feedback cycles** (typing-game example): coding loop (minutes, agent akela), feedback loop
  (hours, aap), outside loop (days, duniya/real users). Andrew Ng's sawal: agent teeno khud kyun nahi
  chala sakta — kyunki aap **context advantage** rakhte ho.
- **Concept 13 — Token cost:** cap har loop, model kaam se match karo (biggest saving), prompts/rules
  chhote rakho, kam frequency pe chalao. Numbers: 1 beat ≈ $0.20; 5 beats/din × 20 din ≈ $20/month; har
  5-min din-raat ≈ $1,800/month. Achi spine cost bhi kam karti hai (kam retries).
- **Concept 14 — Kaam check karna ab bhi aapka hai:** "done" = claim, proof nahi. Kai-loops-ek-sath: 3
  new problems (failure math — 5×95%≈0.77 clean; loop-kya-kar-sakta-limit-karo, sirf review nahi; counting
  question = workforce management). 4 shared-memory guardrails: versioning, conflict checks, permissions
  by level, portability.
- **In/On/Out of the loop table:** in-the-loop (prompting), **on**-the-loop (loop engineering — system
  chalta hai, attention gate pe), out-of-the-loop (**kabhi acceptable nahi** — failure mode). "Out of the
  loop" drift se banta hai, jaan-boojh kar nahi.
- **Concept 15:** loop farak nahi bata sakta samajhne-ke-liye-use vs samajhne-se-bachne-ke-liye-use — sirf
  aap bata sakte ho. AI gravity force (Eric So, MIT Sloan). Observability: dekh-sakte-jagah output, har
  run pe ek line (fail par bhi), replayable runs, limit-pe-loudly-fail, overnight se pehle prove karo
  (hourly+watched → nightly+unattended).

## 06 — Dogfooding: Yeh Kitaab Khud Apne Loops Kaise Use Karti Hai

- Kitaab 2 production loops se khud chalti hai (kagaz se real): **Loop 1 (Feedback Loop)** — 2 Routines
  (triage + weekly fix-drafting), spine = live database (kabhi note dobara na kaam ho), zyada tar feedback
  khud-ba-khud close, chhote-safe fixes ke liye khud PR draft, human gate sirf zaroori cheezon tak
  (blocked reader, contribution, content error) + har fix ship se pehle approve.
- **Loop 2 (What's New Loop)** — GitHub Actions, worker **OpenCode** (doosra tool), state = chhoti file
  (last-change-yaad), koi human gate nahi (koi approve nahi karta live jaane se pehle).
- Dono loops jahan disagree karti hain sabse useful baat hai: deciding factor **galat move ki cost** hai —
  mehnga/undo-mushkil → in-the-loop (human gate), chota/reversible → on-the-loop. Koi loop akela nahi
  chorha jata — transcripts parhe jate hain (green run ≠ correct run).

## 07 — Practice Projects (Projects 1-8 of 12)

8 easy→hard projects, 2 rules (throwaway repo, limit pehle set karo): (1) Watch Loop [in-session] — ISS
Loop, repo mein ready; (2) Tests Pass Then Stop [conditional+maker-checker] — Portfolio Starter, `/goal`,
golden rule: check.py kabhi edit mat karo; (3) Morning Brief With Memory [schedule+spine] — Sky Watch,
NASA data; (4) Fix Loop With Real Checker [worktree+skill+maker-checker] — Fix Loop Demo, planted bug
`/1000` vs `/100`; (5) Codify the Body [dynamic workflows] — CODIFY-AND-SABOTAGE.md; (6) Doorbell Loop
[event-driven+connectors] — apna GitHub repo+App chahiye; (7) Break It On Purpose [observability+cost] —
Sky Watch sabotage; (8) Your Own Daily Loop (Capstone, sab 6 parts) — Daily Triage Demo, real bug + jaan-
boojh-kar-risky-issue jo reviewer hamesha reject karta hai.

## 08 — Routines Appendix: Field Guide (A1-A6)

- Routine = saved Claude Code config (prompt+repos+environment+connectors), Anthropic servers par chalti
  hai. Quick-reference table 9 common defaults/risks/fixes (Local vs Remote, all-connectors-default,
  `.env` gitignored, fresh-clone-har-run, 1-hour schedule floor, API token ek baar dikhta hai, GitHub
  events hourly-capped-dropped, `matches regex` poora field test karti, no mid-run approval, green≠success).
- **A1:** Local = Desktop task (apni machine); Remote = cloud routine. **A2:** Creation form fields —
  Prompt (self-contained), Repositories (default `claude/*` branches), Environment (Trusted allowlist
  default), Connectors (default sab included+writes — sabse zaroori cheez trim karna).
- **A3 — Teen Triggers:** Schedule (1-hour floor), API (`/fire` + bearer token, no dedup — sender-side
  dedup zaroori), GitHub events (hourly caps, overflow **dropped** not queued, regex poora-field-match).
- **A4 — Secrets/State/Identity:** env-variables panel mein (`.env` kabhi nahi), har run fresh clone
  (state repo mein push karo), Routines aapki identity carry karti hain, no mid-run approval → two-routine
  gate (draft → human review → API-fired executor).
- **A5:** Green status = no infra error, **not** task success — har baar transcript parho.
- **A6:** 8-item checklist save karne se pehle.

## 09 — Routine Drills (9-11) + Dreaming Capstone (12)

3 drills throwaway repo mein appendix ki failure cases reproduce karte hain: (9) Rehearse a Routine For
Free — one-off run, transcript parhna, phir fail-karwa ke dekhna; (10) The Secrets Drill — `.env` (fail)
vs environment-variables panel (success), mechanical wajah samajhna; (11) Build the Two-Routine Gate —
Routine A draft karti hai, human review, Routine B API-fire se approve/execute. Project (12) Build a
Dreaming Loop (Capstone 2) — existing loop (Project 3/8) ke upar weekly Routine jo repeated
failure/correction patterns dhoondti hai, evidence-cited PR draft karti hai (kabhi direct commit nahi),
ek deletion bhi propose karti hai — kabhi khud approve mat karo, evidence-less improvement no-improvement
se bura hai.

## 10 — Commands Cheat Sheet

Single-page reference: sab Claude Code commands (`/loop`, `/goal`, `/schedule` variants, `--worktree`,
`isolation: worktree`, subagent/skill file locations) + OpenCode equivalent shell patterns (while-loop,
for-loop-with-condition, cron, git worktree) + Routine API curl + Decision table (kaunsa command kab) +
minimum checklist recap.

## 11 — Practice Log

User ka apna hands-on progress record (README/practice-projects se alag — "kya kiya" vs "kaise karna
hai"). 12-project checklist table jisme 7/12 done note hue is dauran (1-5, 7, 8 complete; 6 aur 9-11
claude.ai account/GitHub App pending) — rule: checkbox sirf tab tick hota hai jab "Done jab" criteria
khud verify ho, sirf steps parhna kaafi nahi.

## 12 — Key Words Glossary

15-term plain-English glossary (Agent, Prompt, Loop, Beat, Heartbeat, Trigger/fire, Unattended, Stopping
condition, Maker-checker, Worktree, Skill, Connector/MCP, State/memory, Spine, Human gate, Routine).
Origin note: Boris Cherny (Claude Code) — "I don't prompt Claude anymore... my job is to write loops";
Peter Steinberger (OpenClaw) — "design loops that prompt your agents"; Addy Osmani named the pattern.
Parts naye nahi, ab affordable/reliable ho gaye — isliye naam useful bana.

## 13 — Where to Go Next

Book ke apne pointers: multi-loop coordination → Graph Engineering; non-coding loops → Cowork & OpenWork;
API-native scheduling+dreaming → Claude Managed Agents (platform primitive versions); managed checker →
Code Review + Rubrics in Managed Agents → Trusting the Checker course; retry tuning →
`CLAUDE_CODE_MAX_RETRIES`/`RETRY_WATCHDOG`; starter kits → community `loop-engineering` repo +
`awesome-loop-engineering`; stopping condition ka source → Spec-Driven Development.

## 14 — Sources & Further Reading

Primary sources list: Addy Osmani (origin essay), Avi Chawla, Data Science Dojo, Rakesh Gohel, Sydney
Runkle/LangChain, Lamis/Anthropic (memory+dreaming talk), Letta (Sleep-time Compute), Stanford/SambaNova/
Berkeley (ACE — brevity bias/context collapse), OWASP Agentic Top 10 (memory poisoning), Simon Willison,
TrueFoundry, The New Stack, Cherny/Steinberger quotes, Andrew Ng (3 loops), Karpathy (success criteria).
Plus official docs (Claude Code Routines/Channels/Scheduled Tasks/Memory, OpenCode CLI/Agents/GitHub,
model-ID docs). Closing line: "Prompt batata hai kya karna hai. Loop batata hai kab rukna hai."

## 15 — Test Your Understanding

Live-page flashcards widget = interactive-only, no static text (noted, not fabricated). Followed by a
**61-question scenario-based assessment** (verbatim from book, kept in English for precision) covering
every concept 1-15 plus dogfooding, dreaming, and the verification-skills interlude — each question has
a correct answer, explanation, and a real-world analogy (e.g., Q1: accountability given away when diffs
stop being read; Q2: spine missing when a loop repeats day-one work forever).
