# To-Do List

## Active

- [ ] **CCAR-F FDE Track B course chal raha hai (shuru 2026-08-29)** — working dir
  `Claude Certified Architect Foundations(CCA-F)/`, spine = `TRACK-B-WORKLOG.md`, guide = `HOW-TO-RUN.md`.
  **Done:** Week 1 + Week 2 (architect), P1 + P2-scored (practicum). `stop_reason/plan.md` deliverable
  bhi complete (`lib/sdk_parser/stop_reason.py`). **Next architect:** Week 3 (Claude Agent SDK I —
  tools, permissions, MCP, structured tool errors). **BLOCKED — needs user:** P2/P3 ke liye vertical
  confirm karo (recommendation: #1 PK freelancer/software-house tax & FBR) + personal-access check
  (1 practitioner + 3 real source docs).

- [ ] **11 net-new chapters baaqi (2026-08-26 corrected count)** — Thesis aur Getting Paid dono partial
  chapters ab poore ho chuke (neeche Done mein). Baaqi: Selling as a Vertical FDE, Glossary, The System
  of Context, Claude and ChatGPT 101, AI Fluency, Code You Never Write, Skills & Connectors, How to
  Think in the AI Era, aur 3 References & Companions chapters (Which AI Employees To Use in 2026?,
  Cheatsheets, Agentic Engineering Fundamentals). User ne "yes update it" keh kar in par kaam karne ki
  ijazat de di hai (koi specific priority order nahi di) — book-order mein continue karo.
- [ ] **PCAO-F → PCAR-F push (deadline 2026-10-05):** ⚠️ **2026-09-02 gen 61 timing constraint** —
  PCAO-F proctored **18 Sep se live** (sample 10 Sep); PCAR-F sample+proctored **date-less
  ("coming soon")**. Deadline at-risk — `07-practice-log.md` risk-analysis table (A: both in time /
  B: PCAR-F slips → re-scope to PCAO-F / C: nothing bookable → prep-only). Stance: prep deadline-ready
  (dono blueprints, samples 75%+), sitting seat-dependent. Checklist: Week 1 CCAO-F blueprint, Week 2
  CCAR-F blueprint + 6 scenarios, Weeks 3-4 build, Week 5 PCAO-F sample + CCAR-F Practice Exam, Week 6
  sit PCAO-F (18 Sep) then PCAR-F (when seat opens).
- [x] **CCAR-P 63-question count discrepancy — RESOLVED (2026-09-02, gen 61):** book: "Every price
  and every count above comes from Anthropic's published exam guides." 63 + full 7-domain blueprint
  wapas official. Repo ka 2026-08-24 PDF-read sahi tha. `02`/`03`/`pcar-p/` updated.
- [ ] **Book course-catalog re-audit (new, 2026-09-02):** gen 47→61 mein book ka poora course
  structure expand hua (Foundations 10, General Agents 15, Mode 2 3, etc.) aur bahut se existing
  slugs pe `-crash-course` suffix laga. Ex-"7-course upcoming sequence" ab study guides mein live
  links. Certifications scope se bahar — poora `outline_agent_factory` walk + `docs/` disk cross-check
  karke root `README.md` status table + Track B references sync karni hain.
- [ ] **Track B syllabus route line stale:** `docs/ccar-f-fde-track-b/04-certification-path-and-sources.md`
  flagged — user-provided syllabus (26 Aug) ka `PCAR-F → PCDV-F → ...` route ab book se match nahi
  karta (ab PCAO-F → PCAR-F; Anthropic optional). Baaki Track B chapter theek hai.
- [ ] User se confirm: baqi 30 chapters (Front Matter 12, The Ecosystem 9, Foundations-Everyone 6, References & Companions 3) note karni hain `docs/` mein?

## Done

- [x] **Doorbell (Loop Eng Project 6) — complete (2026-08-29):** fresh `claude setup-token` (standalone
  terminal, browser auth — Claude Code session ke andar se 2x hang hua tha, real TTY chahiye tha),
  `gh secret set CLAUDE_CODE_OAUTH_TOKEN` update kiya, PR #1 par empty commit se re-trigger kiya —
  Claude ne 45s mein `average_altitude`'s jaan-boojh kar dala gaya off-by-one bug sahi pakra. Loop
  Engineering ab **8/12 projects Done** (9-12 claude.ai account maangte hain, blocked).
- [x] **Thesis** aur **Getting Paid as a Vertical FDE** dono partial chapters poore kiye — Thesis mein
  01-08 (Paradigm Shift, Industrialized Stack, 10-80-10, Two-Layer Model, Two Modes, Seven Invariants
  x2, Named Engines, 48-Q quiz), Getting Paid mein 04-06 (Earning While Walking, Failure Modes, Ayesha's
  Walk, Honest Label, Sources, 28-Q quiz). Dono commits alag push kiye. Foundations-Everyone count
  correction (6→8 lessons) bhi root README mein sync ki.
- [x] User ne `Graph-Engineering-Complete-Guide (4).pdf` `docs/graph-engineering/` mein drop kiya — re-audit
  se pata chala **Dogfooding, Sources & Further Reading, Test Your Understanding (18-Q)** sections
  chapter se missing thay (sirf Parts 1-7 thin). `07-dogfooding.md`, `09-sources-further-reading.md`,
  `10-test-your-understanding.md` + `quiz.md` add kiye, `07→08-practice-projects.md` renumber kiya,
  `00-overview.md` mein Glossary section add ki. README/SUMMARY/root `Graph-Engineering-Summary.md`
  sync kiye. Same AGENTS.md Critical Rule gap jo pehle Loop/Harness Engineering mein tha.
- [x] `docs/ksor/` (naya, alag folder) banaya — user ne clarifying question ke jawab mein "Naya alag
  folder banao" confirm kiya (`docs/ecosystem-designing-the-vertical-sor/` untouched raha). 7 files:
  README + 00-04 numbered + SUMMARY.md, standalone framing ke sath, dono folders cross-linked. Root
  `README.md` update kiya naye folder ko point karne ke liye.
- [x] Full Zia Tutor audit (`outline_agent_factory` + disk cross-check) — root `README.md` status
  table stale-ness resolved (was 36/65, actually 54/65 fully done + 2 partial). 9 real gaps + 2
  partials identified and tabled (see Active).
- [x] User-provided root PDFs (`Graph-Engineering-Complete-Guide (1).pdf`,
  `KSoR-Complete-Guide (1).pdf`) check + process kiye. `Graph-Engineering-Summary.md` (root) naya banaya
  — Loop Engineering pattern match karta hai, `docs/graph-engineering/` (already ✅) ka root companion.
  Ecosystem chapter 7 "Designing the Vertical System of Record from First Principles"
  (`docs/ecosystem-designing-the-vertical-sor/`, pehle khaali) `panaversity/ksor` SDK README se poora
  banaya — README + 5 numbered files + SUMMARY.md. Root `README.md` status table dono jagah update.
- [x] 4 Anthropic cert folders (`ccar-f/`, `ccdv-f/`, `ccao-f/`, `ccar-p/`) deep-research kiye — official
  exam-guide PDFs `Read` tool se seedha parhe (WebFetch hallucinate kar raha tha 2 exams ke liye).
  Har folder mein ab MQC profile, task-statement/sub-skill breakdown, exam scenarios, sample
  questions, prep exercises, policies, doc-control history hai.
- [x] `docs/certifications/` ko per-certification folders mein restructure kiya — 8 subfolders
  (pcar-f, pcdv-f, pcao-f, pcar-p, ccar-f, ccdv-f, ccao-f, ccar-p), har ek apni quick facts + domain
  table + prep resources ke sath. Top-level files ab shared pathway/logistics + index hain.
- [x] `docs/certifications/` chapter banaya (README + 8 numbered files) — PCAR-F/CCAR-F pathway, exam
  domain-weight tables, free 6-week study plan, registration/costs/mistakes, sample tests, aur user
  ke apne 2026-10-05 PCAR-F-deadline goal ke liye practice log. Root `README.md` update kiya (row ✅,
  progress bar, total count). Rasta mein root README status-table staleness discover ki (upar Active
  mein tracked).

- [x] Har chapter folder (`docs/[slug]/`) mein `SUMMARY.md` add ki — poore 55 content-wale folders cover
  hue, Roman Urdu + English mein, sab key points sub-headings ke sath. `docs/thesis/` aur
  `docs/how-to-get-paid/` mein pehle-se-maloom incomplete-chapter gaps (missing files) summary ke top par
  note kiye.
- [x] Zia Tutor AI MCP se Harness Engineering re-audit kiya, missing "dogfooding" + "Appendix: Hook Pipeline" sections mili aur add ki (`docs/harness-engineering/06-dogfooding.md`, `08-appendix-hook-pipeline.md`), chapter index update kiya. Root README structure verified — koi change nahi chahiye thi.
- [x] User ne "sources/flashcards/test-your-understanding skip kiya" faisla reject kiya — sahi tha. Dono chapters mein `sources-further-reading` + `test-your-understanding` (Harness: 18 Q&A, Loop: 61 Q&A) add kiye, `flashcards-study-aid` widget-only note ke sath documented (koi static content nahi). Loop Engineering mein ek aur poora-missed section mila: `dogfooding` (2 real production loops) + `key-words-glossary` + `where-to-go-next` — sab add kiye, poori chapter renumber hui (06→15) taake book ka order match kare.
- [x] Mode 2 (Manufacturing) — 18/18 chapters, sab `docs/` mein, committed + pushed
- [x] `Loop-Engineering-Summary.md` ko book ke poore 15-concept content se enhance kiya
- [x] `Loop-Engineering-Final-Prep.md` likhna (root) — sab 15 concepts + real code example (SKILL.md, reviewer.md, Routine, GitHub Actions) + Routines Appendix A1-A6 + System of Record connection
- [x] Root `README.md` rewrite — FDE framing (book ke apne "Roles This Book Trains" chapter se) + `outline_agent_factory` se verified poori book structure ka status table (35/65 chapters covered)
- [x] Project 1 (Watch Loop / ISS Loop) `docs/loop-engineering/projects/iss-loop/` mein permanently add kiya, live tested (skill kaam kar rahi hai), Windows encoding footgun note kiya
- [x] Har project folder (7) mein `SUMMARY.md` add ki — conceptual explainer, README.md se alag
- [x] Projects 4, 8 (DIY scaffolds, koi official kit nahi) khud banaye aur live test kiye (`fix-loop-demo/`, `daily-triage-demo/`) + Projects 5, 7 ke liye instructions (`CODIFY-AND-SABOTAGE.md`) — poore 12/12 Loop Engineering projects ab documented + jahan possible tha live tested
- [x] Projects 2, 3, 6 + bonus paper-watch — official starter kits copied to `docs/loop-engineering/projects/`, live tested (sky-watch/paper-watch real API data; check.py verified), Portfolio real-project callout ki galat placement fix ki
- [x] Root `AGENTS.md` + `CLAUDE.md` (rules file) banaye — "chapter complete = poora content, appendices sameet" lesson permanent kiya, fetch/push/spine discipline codify ki
- [x] `docs/loop-engineering/` mein baqi 4 projects (9-12) add kiye: `07-routines-appendix.md` (A1-A6) + `08-routine-drills-and-dreaming.md` (step-by-step "kaise karein" ke sath) — ab poore 12 projects documented hain

- [x] User ne khud Project 7 (Break It On Purpose) aur Project 8 (Daily Loop Capstone) hands-on kiye —
  `docs/loop-engineering/11-practice-log.md` mein track. Naya `joke-loop/` easy-stand-in project bhi
  Project 7 ke liye banaya. Ab 7/12 practice projects done.
- [x] Bonus "Proposal Loop" project banaya aur live run kiya — fictional personas, ek real mailbox
  (Gmail MCP se), do OODA-state-machine paths (Hard Rejection + Joyful Acceptance) real threaded
  emails se, dono terminal state tak pahonche. `docs/loop-engineering/projects/proposal-loop/`.
- [x] Harness Engineering ke liye bhi `11-practice-log.md` banaya (Loop Eng pattern) — 8 projects +
  appendix ke 3 drills, sab checklist ke sath.
- [x] Harness Engineering `projects/` folder banaya — 8 real runnable scaffolds (first-wall,
  lint-hook, error-audit, tool-diet, typed-reviewer, ratchet-week, fenced-night, model-swap) +
  hook-pipeline-drills. Scripts (`lint_check.py`, `validate.sh`, `trace_log.py`, `block_curl.py`)
  khud chala kar verify kiye commit se pehle.
- [x] Root `AGENTS.md` mein 2 naye standing rules add kiye: (5) practice projects ko real runnable
  scaffold do `projects/` mein (test-before-commit sameet), (6) har chapter "Test Your
  Understanding"/quiz section ke bina "complete" nahi.

## Backlog / Open Questions

- [ ] **`docs/ksor/` chapter version-stale (found 2026-08-29):** built from `KSoR-Complete-Guide` PDF
  + an older GitHub README state. Live `docs/status.md` in `panaversity/ksor` now shows real, shipped
  CLI verbs (`ksor init/build/serve/ingest/migrate/schema/grant/takedown/calibrate/gc`, npm
  `0.0.42`) that go well beyond what the chapter documents. Needs a research-and-update pass like
  `docs/ccar-f-fde-track-b/` just got, whenever KSoR content is next touched.

- [ ] `Four-Layers-Summary_1.pdf` (duplicate PDF, repo root) — delete karna hai? (Pehle offer kiya tha, abhi tak koi jawab nahi)
- [ ] **Harness Engineering practice — 6/8 + appendix done (2026-09-01).** P1 First Wall, P2 Lint
  Hook, P3 Error Audit, P4 Tool Diet (worksheet), P5 Typed Reviewer, P7 Fenced Night (1 beat),
  Appendix hook drills — sab `claude -p` se throwaway repos mein. **Baaki:** P6 Ratchet Week (real
  7-day run — ledger session-data se seeded), P8 Model Swap (needs hardened loop + 3 nights on alt
  model). Details: `docs/harness-engineering/11-practice-log.md`.
- [ ] **Loop Engineering — 10.5/12 projects.** 6/9/12 ✅. **Project 10 (Secrets Drill): Run 1 ✅**
  (cloud routine — gitignored `.env` cloud tak nahi pahuncha, `check_token.py` FAIL). **Run 2 baaqi:**
  user claude.ai routine ke Environment→Variables panel mein `MY_API_TOKEN=dummy-abc123` add kare →
  Run now (API se env-vars set nahi ho sakte). **Project 11 (Two-Routine Gate): BLOCKED** — dono
  routines ko GitHub push chahiye. **Recurring blocker → USER ACTION:** Claude GitHub App install karo
  → https://github.com/apps/claude/installations/select_target . Uske baad: Project 11 (~10 min) +
  Project 12 dreaming routine (`trig_01BwicMH3whg74osL1QUEVqm`, abhi disabled) re-enable + clean
  re-run. Sab 3 cloud routines abhi disabled (weekly push-fail avoid karne ko).
- [ ] **Dreaming Loop PR review pending (user):** [my-doorbell#2](https://github.com/samade747/my-doorbell/pull/2)
  — Project 12 ka rule: dreaming loop apne rules khud approve nahi karti. User evidence dekh kar
  merge/close kare.
- [x] **Local-runnable Track B FDE Practicum scaffolds (2026-08-27):** `docs/ccar-f-fde-track-b/`
  chapter + `projects/` mein 4 scaffolds — Fumadocs corpus-to-site (P4-P5), stateless MCP + MRTR
  server (P6-P7), agent surface with knowledge-boundary (P8), 3-class eval runner (P11) — sab local
  hi chalte hain (koi live deploy nahi, user ne yehi scope confirm kiya tha). **Abhi bhi baaki:**
  actual **live/public deployment** (real Next.js+Fumadocs hosting, real MCP server URL) — jab
  CCAR-F/FDE-Internship ki taraf aage badhna ho, user se hosting/domain decision leni hogi.
