# To-Do List

## Active

- [ ] **9 real content gaps found (2026-08-25 Zia Tutor audit)** — user se priority order confirm
  karni hai: Selling as a Vertical FDE, Glossary, The System of Context, Code You Never Write,
  Skills & Connectors, How to Think in the AI Era, aur 3 References & Companions chapters (Which AI
  Employees To Use in 2026?, Cheatsheets, Agentic Engineering Fundamentals). Plus 2 partial completions:
  Thesis (Seven Invariants section + quiz) aur Getting Paid as a Vertical FDE (11/25 sections).
- [ ] **PCAR-F push (deadline 2026-10-05):** `docs/certifications/07-practice-log.md` ke 6-week plan
  follow karo — Weeks 1-2 domain-weighted study, 3-4 ek chhoti app banao, 5 practice test, 6 PCAR-F
  sit karo. (2026-08-26 cross-check confirm kar chuka hai ke Week 1-2 ke sab required reads is repo
  mein already maujood hain — ab sirf revise + apply karna hai, naya fetch nahi.)
- [ ] **Track B "upcoming Claude sequence" periodically re-check karo** — 7 courses (The Loop by Hand,
  Structured Extraction Pipelines, Claude Agent SDK, Claude Code for Teams, Claude Code as a CI
  Worker, Claude Code Routines, Claude Managed Agents) abhi Zia Tutor corpus mein "not links yet" hain
  (`docs/certifications/certifications` page se confirm, 2026-08-26). Jab live hon, `read_agent_
  factory_lesson` se fetch karo — CCAR-F Domain 3 (20%) aur CCDV-F "Applications and Integration"
  (33.1%) seedha in par depend karte hain.
- [ ] Doorbell (Loop Eng Project 6): repo `samade747/my-doorbell` bana, workflow verify hui, secret
  set hai — lekin PR #1 run **fail** hui (`CLAUDE_CODE_OAUTH_TOKEN` khaali/invalid nikla). Fresh
  `claude setup-token` + `gh secret set` dobara chahiye, phir re-run confirm karna hai.
- [ ] User se confirm: baqi 30 chapters (Front Matter 12, The Ecosystem 9, Foundations-Everyone 6, References & Companions 3) note karni hain `docs/` mein?

## Done

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

- [ ] `Four-Layers-Summary_1.pdf` (duplicate PDF, repo root) — delete karna hai? (Pehle offer kiya tha, abhi tak koi jawab nahi)
- [ ] Baaki practice projects: 6 (Doorbell — GitHub repo/App install chahiye), 9-12 (claude.ai account chahiye)
- [ ] **Build the actual Vertical SoR (Track B FDE Practicum P1-P13, found 2026-08-26):** is repo ke
  paas KSoR/SoR *concept docs* hain (`docs/ksor/`, `docs/ecosystem-designing-the-vertical-sor/`) lekin
  koi real deployed project nahi — Track B syllabus Milestone 1 (Next.js+Fumadocs human site, 5+ governed
  docs, live) aur Milestone 2 (stateless MCP 2026-07-28 search/retrieve/cite surface, working) dono
  currently unmet hain. PCAR-F pass karne ke liye zaroori nahi, lekin CCAR-F/FDE-Internship ki taraf
  agla concrete kaam hai — user se priority/timing confirm karni hai.
