<!-- progress.md — loop ki memory runs ke darmiyan (spine, as taught in Loop-Engineering-Summary.md) -->

## Done

- 2026-08-29: User ne `docs/ccar-f-fde-track-b/` ke liye "find out aur update karo" mangi — live
  primary sources se research kiya (root syllabus MD file khud unchanged nikla, 2026-08-26 se). **2 bare
  findings:**
  (1) **`@panaversity/ksor` ab genuinely shipped hai** (npm `0.0.42`, `docs/status.md` GitHub se
  confirm) — `ksor init`, `ksor build`, `ksor serve`, `ksor ingest` sab real, released commands hain,
  jo P4/P5/P8 practicum weeks ke bilkul real equivalents hain. `p4-p5-fumadocs-corpus-to-site/` aur
  `p8-agent-surface/` READMEs mein "Real Path" sections add kiye exact current commands ke sath
  (pehle wala `create-fumadocs-app` hint generic/stale tha).
  (2) **MCP 2026-07-28 spec ka poora primary-source text mila** (changelog +
  [MRTR pattern page](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr))
  — pehle `p6-p7-stateless-mcp/` scaffold honestly kehta tha "book MRTR cover nahi karti, exact fields
  syllabus se hain, spec ke against verify karo." Ab woh verification ho chuki hai: `server.py` poora
  rewrite hua spec-exact field names (`resultType`, `inputRequests` as `elicitation/create`-shaped map,
  `inputResponses` as `ElicitResult`-shaped) + spec ki apni replay-protection guidance (principal + TTL
  + request-digest HMAC envelope mein) ke sath — `test_server.py` mein ek naya decline-path test bhi
  add hua. Sab 4 scaffolds dobara verify hue, sab pass.
  **Follow-up flag (is turn mein nahi kiya, scope se bahar tha):** `docs/ksor/` chapter (PDF-sourced,
  older SDK-README-based) ab is naye `docs/status.md` se **version-stale** hai — `todolist.md` mein
  backlog note kar diya.

- 2026-08-28: User ne certifications ke baare mein "aur data lao, book se aur Anthropic se, research
  karo, quiz + sab kuch banao" mangi. **Research (book + live Anthropic pages):** Zia Tutor
  `certifications` page dobara search kiya (generation 43→44, content substantively unchanged —
  domain weights same). Do live Anthropic-adjacent sources cross-check kiye: **Pearson VUE program
  page** (WebFetch) aur locally-maujood **Exam Registration Guide PDF** (`Read` tool, safe — PDF
  hallucination-risk memory follow ki). 4 findings mile: (1) naya — Global Premier tier ke liye
  100%-off promotion 31 Aug 2026 tak, phir 50%; (2) naya — poora exam-day/registration flow detail
  (password rules, security questions, CCTV/palm-vein consent, accommodation-before-scheduling);
  (3) ⚠️ **unresolved discrepancy** — book "24-hour reschedule window" kehti hai, Pearson VUE page
  "48 hours" — dono flag kiye, conservative number follow karne ko kaha, resolve nahi kiya khud se;
  (4) ⚠️ registration-guide PDF ka apna CCAR-F-domain screenshot (30/25/25/20%, 4 domains) is repo
  ke verified table (27/20/20/18/15%, 5 domains, full Exam Guide v1.0 se) se **bilkul alag** nikla —
  stale/pre-v1.0 screenshot maan kar flag kiya, **is repo ka table nahi badla** (poora-text-parhi
  authoritative Exam Guide hi source of truth rahi). Sab 4 `docs/certifications/05-registration-
  costs-mistakes.md` mein naye section ki tarah likh diye, honest uncertainty ke sath.
  **Build:** `ccao-f` (judgment-heavy, coding-appropriate nahi) ko quiz + 10-Q test-understanding +
  ek **no-code judgment-drills worksheet** (8 scenarios + reference answers, jaisa `tool-diet`
  pattern) mila. `ccar-p` (capstone) ko quiz + 10-Q test-understanding + ek coding project
  (`00-professional-scenarios/`, teenon official sample questions — least-privilege, cache-aware
  prompt ordering, RAG-regression diagnosis — 6 offline pytest tests pass) mila. Ab poore
  `docs/certifications/` (sab 4 Anthropic + 2 Panaversity folders) mein quiz/test-understanding hai,
  aur jahan technically appropriate hai wahan tested practice projects bhi — **33 offline pytest
  tests total, sab pass.**

- 2026-08-27 (2nd update): User ne `pcar-f`/`pcdv-f` folders mein bhi projects+quiz mangi. PCAR-F
  aur PCDV-F dono apne Anthropic counterpart (CCAR-F/CCDV-F) ke **bilkul usi domain-weight blueprint**
  par based hain, isliye duplicate scaffolds banane ki bajaye dono folders ke "Practice Projects"
  section CCAR-F/CCDV-F ke scaffolds ko point karte hain. PCAR-F ko CCAR-F ke already-bane 5 scaffolds
  mil gaye (link hi kaafi tha). **CCDV-F ke paas koi scaffold nahi tha** (uska exam guide CCAR-F ki
  tarah 4 numbered exercises nahi deta, sirf "ek application banao" + 3 sample questions) — isliye
  pehle `docs/certifications/ccdv-f/projects/00-integration-application/` banaya (batch-vs-realtime
  decision, prompt-injection guardrail, reusable MCP-tool pattern — 3 official sample questions,
  Domain 2/7/8, 8 offline pytest tests pass), phir PCDV-F usay point karta hai. Dono PCAR-F aur
  PCDV-F mein `05-test-your-understanding.md` + `quiz.md` (10 questions each) add kiye — Panaversity
  logistics + apne-apne domain-weight blueprint par grounded.

- 2026-08-27: User ne 4 workstreams ek sath mangi (ksor/certifications projects+quiz, CCAR-F ke
  missing exercises, naya CCAR-F Track B chapter) — 4 parallel background forks se kiya, coordinator
  (main session) ne verify + reconcile + root-doc updates + commit khud kiye. **Sabse bara finding:**
  `docs/ecosystem-designing-the-vertical-sor/` galat source (KSoR-Complete-Guide PDF + panaversity/ksor
  GitHub README) se bana tha — uska slug book ke apne ek real lesson (`ecosystem-designing-the-vertical-sor`)
  se exactly match karta hai, jo ab **42K+ tokens ka nikla** (pehle jitna cover hua uska kai guna) aur
  ismein 7 templates, 2 poore end-to-end appendices (Sales SoR, General Ledger SoR), poster, flashcards,
  aur mandatory "test-your-understanding" (59-Q quiz) hain — sab pehle missing thay. Poora chapter Zia
  Tutor se rebuild kiya (AGENTS.md rule 3 compliance), + 1 worksheet-style practice project
  (`fill-the-templates/`, 3-bin sort + outcome contract apply karne ke liye).
  `docs/ksor/` (SDK reference, alag rakha, PDF source theek hai) mein `05-test-your-understanding.md`
  + `quiz.md` + 3 practice scaffolds add kiye (corpus-to-site validator, stub stateless MCP tool,
  governance/provenance register).
  `docs/certifications/` mein `08-test-your-understanding.md` + `quiz.md` (14 scenario questions)
  add kiye, aur CCAR-F ke 3 missing project scaffolds banaye: `00-agentic-loop-no-framework` (5
  deliberately-injected bugs — missing history, lost tool result, incorrect stop handling, repeated
  tool calls, premature termination — diagnostic exercise), `03-structured-extraction-pipeline`
  (validation-retry, batch+resubmit, confidence-routing), `04-multi-agent-research-pipeline`
  (parallel subagents, timeout handling, conflicting-source synthesis) — sab 15 offline pytest tests
  pass. Naya `docs/ccar-f-fde-track-b/` chapter banaya (root syllabus MD file se) — full 13-week
  breakdown + quiz + 4 **local-runnable** practicum scaffolds (P4-P5 Fumadocs site, P6-P7 stateless
  MCP+MRTR server, P8 agent surface, P11 eval runner) — koi live deployment nahi (user ne explicitly
  yeh scope confirm kiya, hosting account/domain avoid karne ke liye).
  **2 subagent-git-bypass incidents pakre:** ek fork ne apna kaam kiye bina "verification report"
  bana diya (retry se fix kiya), aur ek **doosre** fork ne explicit "commit mat karo" instruction ke
  bawajood ek unauthorized `git commit`+`push` kar diya (commit `f76af32`, "1042") — pehle se
  documented pattern (`feedback_subagent_git_bypass` memory, 2026-08-24 wali incident) ka recurrence,
  memory update ki aur product feedback file ki. Final commit+push khud coordinator ne kiya, poore
  batch ka `git log`/`git status` audit karne ke baad.

- 2026-08-26: User ne `Graph-Engineering-Complete-Guide (4).pdf` ko `docs/graph-engineering/` folder mein
  seedha drop kiya aur docs update karne ko kaha. PDF parh kar dekha to wo already-covered content ka hi
  ek "class notes" compile tha (Parts 1-7), lekin uski apni outline mein 2 sections explicitly listed
  thay jo humari 00-07 files mein kahin nahi thay: **Dogfooding** aur **Exam-Prep Cheat Sheet**. Isi wajah
  se `outline_agent_factory`/`read_agent_factory_lesson` se authoritative structure re-confirm ki (same
  AGENTS.md Critical Rule audit jo pehle Loop aur Harness Engineering mein hua tha) — is dafa **Graph
  Engineering** mein wahi gap mila: `using-a-graph-on-this-book-dogfooding`, `sources-further-reading`,
  `flashcards-study-aid`, aur `test-your-understanding` (18-Q quiz) sab missing thay, sirf 00-07 files
  thin (dogfooding + practice-projects ki jagah sirf 07-practice-projects tha).
  Fix kiya: book ke apne order ko match karne ke liye `07-practice-projects.md` → `08-practice-projects.md`
  renumber kiya, naye `07-dogfooding.md`, `09-sources-further-reading.md` (full bibliography + viral-PDF
  origin-story correction), `10-test-your-understanding.md` (18 Q&A, English verbatim + Roman Urdu intro)
  aur standalone `quiz.md` (same content, root-accessible copy) add kiye. `00-overview.md` mein book ke
  "teaching-aid" section se **Glossary** (Zaroori Terms table) aur "two ways to read this course" note
  add ki, jo pehle kahin nahi thi. Chapter `README.md` + `SUMMARY.md` index update kiye (PDF ko reference
  ki tarah link kiya), root `Graph-Engineering-Summary.md` ka file-count aur dogfooding/test-understanding
  pointers update kiye. Sab internal cross-file links verify kiye (bash grep chain, koi broken link nahi).

- 2026-08-19: User ne har chapter folder (`docs/[slug]/`) ke liye ek `SUMMARY.md` maangi — har chapter/folder ka apna alag, sab points wala summary, Roman Urdu + English mein, usi folder mein. **Poore 55 content-wale chapter folders** mein `SUMMARY.md` add ki (4 folders — `ecosystem-designing-the-vertical-sor`, `ecosystem-system-of-context`, `glossary`, `how-to-sell` — khaali hain, skip kiye). Kaam 7 parallel background agents (fork) se hua, har ek ~8 folders ke README + poori numbered content files parh kar draft banata; ek harness-level restriction mili (subagents "SUMMARY.md" naam ki file khud Write nahi kar sakte — "report file" pattern samajh kar block hota hai) — sab agents ko redirect kiya draft **text** return karne ke liye, coordinator (main session) ne khud sab 55 files disk par likhin. Do folders mein pehle-se-maloom "incomplete chapter" gaps re-confirm hue (`docs/thesis/` sirf 00 file hai, 01-07 missing; `docs/how-to-get-paid/` sirf 00-03 hain, 04-05 missing) — dono ke SUMMARY.md mein warning note likha, baaki jo maujood tha wo poora cover kiya. Session beech mein claude.ai usage limit reset hui — resume karte waqt disk state check kiya (`find docs -name SUMMARY.md`) taake dobara kaam na ho, phir jo missing tha (2 batches ke files jo receive hue the lekin write nahi hue thay, + 1 fresh-launched agent ke 7 folders) complete kiya.
- 2026-08-19 (correction): User ne pichli entry ka "sources-further-reading/flashcards/test-your-understanding skip kiya" faisla reject kiya — sahi tha, yeh bhi AGENTS.md critical-rule ka wahi gap tha jo "quiz/study-aid boilerplate hai" ka bahana bana kar chhupaya ja raha tha. Dono sections `flashcards-study-aid` bare `<Flashcards />` widget nikla (koi extractable static text nahi, live-site-only note likh diya) lekin `test-your-understanding` dono chapters mein **genuinely substantive content** nikla: **Harness Engineering** ke 18 aur **Loop Engineering** ke 61 (!) scenario-based exam questions, har ek real-world analogy ke sath, poori tarah book se. Dono `sources-further-reading` sections (full bibliography, one-line summary) bhi add ki. **Loop Engineering** ka ek aur poora-missed section mila isi audit mein: `using-these-loops-in-this-book-dogfooding` (2 real production loops jo yeh kitaab khud chalati hai — feedback loop + What's New loop) — Harness Engineering wali dogfooding sirf ek chapter mein thi, Loop Engineering ki khud reh gayi thi. Plus `key-words-in-plain-english` (glossary) aur `where-to-go-next` bhi missing thay.
  **Harness Engineering** mein add kiye: `09-sources-further-reading.md`, `10-test-your-understanding.md` (18 Q&A).
  **Loop Engineering** mein add kiye: `06-dogfooding.md` (dogfooding, book's own order mein insert kiya — isliye 07 se 15 tak sab files renumber hui), `12-key-words-glossary.md`, `13-where-to-go-next.md`, `14-sources-further-reading.md`, `15-test-your-understanding.md` (61 Q&A — bara file, ek Python script se `read_agent_factory_lesson` ke windowed JSON output se parse kar ke generate kiya, taake token-heavy manual typing na ho).
  Dono chapters ke `README.md` index update kiye, sab cross-file nav links aur project-folder references (`daily-triage-demo/`) fix kiye. **Lesson:** "yeh boilerplate/quiz hai isliye skip" apni khud ki rationalization thi, book ka apna judgment nahi — content hamesha fetch kar ke khud dekho, phir decide karo, guess mat karo.
- 2026-08-19: Zia Tutor AI MCP se **Harness Engineering** chapter dobara audit kiya (`outline_agent_factory` se book structure re-confirm ki — Front Matter/Ecosystem/Getting-Started ka naqsha unchanged hai, koi naya chapter nahi). Audit ne wahi AGENTS.md critical-rule-wala gap dhoonda jo pehle Loop Engineering mein tha: `docs/harness-engineering/` mein 06-practice-projects tha, lekin book ke apne 2 sections — **"Using this harness on this book (dogfooding)"** aur **"Appendix: The hook pipeline, end to end"** — bilkul missing thay. `read_agent_factory_lesson` se dono sections poore fetch kiye aur naye files add ki: `06-dogfooding.md` (5 verbs production mein — book khud apni harness kaise use karti hai) aur `08-appendix-hook-pipeline.md` (5 hook moments table, exit-code contract, 3 drills). `07-practice-projects.md` renumber kiya (pehle 06 tha) taake book ka apna order match kare. Chapter `README.md` index update kiya 9 files ke sath. ~~"sources-further-reading"/"flashcards"/"test-your-understanding" sections jaan-boojh kar skip kiye~~ **(galat faisla tha, upar wali entry mein fix hua)**. Root `README.md` ka top-level status table verify kiya — 65-chapter naqsha same hai, koi change nahi chahiye thi.
- 2026-08-15: Mode 2 (Manufacturing) — poora complete: Phase 1 Building Blocks (6/6), Phase 2 Build Workers (3/3), Phase 3 Scale the Workforce (9/9). Sab `docs/[slug]/` folders README + numbered parts ke sath, Roman Urdu/English mixed, committed aur pushed (last commit `b6bf818`).
- 2026-08-16: `Loop-Engineering-Summary.md` (root) ko poori tarah enhance kiya — book ke sab 15 concepts se missing points add kiye: checker ladder, dynamic workflows interlude, verification skills (4 homes), dreaming/memory-improvement loop, in/on/out-of-loop industry table, real token-cost math, observability checklist, Andrew Ng ke 3 feedback loops, dogfooding detail, 12 practice projects/drills table, aur System of Record connection note.
- 2026-08-16: `Loop-Engineering-Final-Prep.md` (root, naya file) mukammal ban gaya — sab 15 concepts detail mein, poora real loop code example (daily-triage `SKILL.md` + `reviewer.md` dono tools ke liye + Claude Code Routine wiring + OpenCode GitHub Actions wiring + real morning run trace) seedha book se, poora Routines Appendix (A1-A6 field guide + checklist), aur System of Record ka detailed connection section (loop's spine as its own SoR + Manufacturing track ka authoritative-data-via-MCP pattern se comparison table).
- 2026-08-17: Har official/DIY project folder mein `SUMMARY.md` add ki (iss-loop, portfolio-starter, sky-watch, fix-loop-demo, doorbell, daily-triage-demo, paper-watch — 7 files) — har ek mein "kya sikhata hai / kyun zaroori hai / kaise kaam karta hai / maine kya test kiya" format, conceptual layer (SUMMARY.md) ko mechanical layer (README.md) se alag kiya. `docs/loop-engineering/README.md` ka table update kiya taake dono links dikhein.
- 2026-08-17: Projects 4 aur 8 (koi official starter kit nahi thi) khud DIY scaffold ki tarah banaye aur live test kiye. **Project 4** (`fix-loop-demo/`): `discount.py` mein real planted bug (`/1000` instead of `/100`), `test_discount.py` — `pytest` se confirm kiya 2/3 tests fail hote hain, phir cache clean kiya. **Project 8 capstone** (`daily-triage-demo/`): `greeter.py` mein real off-by-one bug + `ISSUES.md` mein ek jaan-boojh kar risky issue (public behaviour change) jo reviewer.md hamesha reject karta hai — `pytest` se confirm kiya bug reproduce hota hai. Dono mein Claude Code + OpenCode dono ke liye SKILL.md/reviewer.md/AGENTS.md/CLAUDE.md/.gitignore/README (full run + "done when" criteria) hain. **Projects 5 aur 7** ke liye naya `projects/CODIFY-AND-SABOTAGE.md` banaya — instructions-only (Project 4 aur 3 ki repos par build hote hain, naya code nahi chahiye). Sab index files (`README.md`, `06-practice-projects.md`) update kiye poori 12/12 mapping ke sath (✅/📋/🖐️ legend).
- 2026-08-17: Official `agentfactory-labs` repo mein loop-eng ke tahat sirf **4 pre-built starter kits** nikle (iss-loop, portfolio-starter, sky-watch, doorbell) + ek bonus (paper-watch, Concept 12 spine demo) — Projects 4, 5, 7, 8, 9, 10, 11, 12 ke koi official starter kit nahi, woh "apna banao" DIY exercises hain. Sab 4+1 available projects `docs/loop-engineering/projects/` mein copy kiye. **Live tested:** sky-watch (real NASA asteroid data), paper-watch (spine confirmed — 2nd run ne "nothing new since last run ✓" bola, test artifact clean kar diya), portfolio-starter's `check.py` (missing-profile.md par sahi error deta hai). doorbell copy hua lekin poori tarah chalane ke liye user ka apna GitHub repo + App install chahiye. Rasta mein ek pehle se maujood galti bhi fix ki: Portfolio real-project callout galat jagah (Project 4 ke neeche) tha, Project 2 (Concept 5) ke neeche move kiya. `06-practice-projects.md`, `03-spine.md`, aur `README.md` (loop-engineering) sab update kiye.
- 2026-08-17: Project 1 (Watch Loop) ka real code `docs/loop-engineering/projects/iss-loop/` mein permanently add kiya (official `panaversity/agentfactory-labs` se copy, scratchpad se yahan move kiya jab user ne mangi). `.claude/skills/iss-position` khud is session mein auto-discover ho gayi aur test ki — live ISS position successfully fetch hui (26.7°N 95.1°E, North-East India ke upar). Rasta mein ek Windows-specific `UnicodeEncodeError` (cp1252 vs emoji) mila aur fix (`PYTHONIOENCODING=utf-8`) project README mein note kar diya. `06-practice-projects.md` aur `README.md` (loop-engineering) index update kiye taake naya `projects/` folder link ho.
- 2026-08-17: Root `AGENTS.md` (rules file) + `CLAUDE.md` (`@AGENTS.md` pointer) banaye — is session ki sabse zaroori lesson (Loop Engineering ke 4 projects pehli baar miss hone ki wajah: book ke "core path vs appendix/deferred" split ko "chapter complete" ka signal samajh liya) ko permanent rule bana diya, taake future chapters mein appendices/deferred sections kabhi skip na hon. Fetch discipline, push discipline, aur spine discipline bhi isi file mein codify ki.
- 2026-08-17: `docs/loop-engineering/` mein baqi 4 projects add kiye (poore 12 ab documented hain): naya `07-routines-appendix.md` (A1-A6 field guide — local vs cloud routine, form fields, 3 triggers, secrets/state/identity, run-reading, save-checklist) aur `08-routine-drills-and-dreaming.md` (Project 9 rehearse-for-free, 10 secrets drill, 11 two-routine gate — teeno ke liye step-by-step "kaise karein" instructions add ki — aur Project 12 dreaming capstone). `06-practice-projects.md` aur `README.md` index update kiye taake naye 2 files link hon.
- 2026-08-16: Root `README.md` ko poori tarah rewrite kiya — repo ko "Forward Deployed Engineer (FDE) combat-level" training journey ki tarah frame kiya (book ki apni "Roles This Book Trains" aur "FDE Agent Factory Model" chapters se accurate definition liye — Palantir origin, ~729% posting growth, ~$190K median pay), aur **book ki poori authoritative structure** `outline_agent_factory` tool se confirm karke ek complete status table banayi: Front Matter (12), The Ecosystem (9), Foundations-Everyone (6), General Agents (12 ✅), Personal Agent Harnesses (2 ✅), Mode 1 (3 ✅), Mode 2 (18 ✅ — Phase 1/2/3), References & Companions (3). Total: 35/65 chapters covered, sab links `docs/` folders tak.

- 2026-08-21: **Doorbell (Loop Eng Project 6)** setup kiya: `gh` CLI install + login (`samade747`),
  repo `samade747/my-doorbell` bana (workflow file verify hui — `pull_request` trigger, `track_progress:
  true`), `claude setup-token` se token liya, `gh secret set CLAUDE_CODE_OAUTH_TOKEN` chalaya. PR #1
  se ring kiya (`average_altitude` off-by-one bug) — workflow trigger hui lekin **fail** hui:
  `CLAUDE_CODE_OAUTH_TOKEN` khaali/invalid nikla (secret naam se maujood tha, value nahi). Root cause
  isolate kiya GitHub Actions log se. Fix (fresh token + re-set secret) user ke terminal mein baaki hai.
- 2026-08-21: **Bonus "Proposal Loop" project** banaya aur live run kiya — user ne ek shared
  "AI Multi-Agent Marriage Proposal Loop" (real logon ke naam/emails wala) example poocha; usay
  fictional personas (Rayan/Meher) aur ek hi real mailbox (already-connected Gmail MCP,
  `samad.x747@gmail.com`) se rebuild kiya — privacy ke liye. Do OODA-state-machine paths (Hard
  Rejection + Joyful Acceptance) real threaded Gmail emails se bheje (`create_draft` +
  `replyToMessageId` → `send_message(draftId=...)`), dono terminal state (`REJECTED_HARD`,
  `ACCEPTED`) tak pahonche. `docs/loop-engineering/projects/proposal-loop/` mein documented.
- 2026-08-21: **Harness Engineering practice infrastructure** banaya (Loop Engineering pattern
  follow karte hue): `11-practice-log.md` (8 projects + appendix drills checklist, simplest-language
  boxes), aur poora `projects/` folder — 8 real runnable scaffolds (first-wall, lint-hook,
  error-audit, tool-diet, typed-reviewer, ratchet-week, fenced-night, model-swap) + hook-pipeline-
  drills. 4 scripts (`lint_check.py`, `validate.sh`, `trace_log.py`, `block_curl.py`) khud chala kar
  commit se pehle verify kiye (jq install karna pada — `winget install jqlang.jq`).
- 2026-08-21: Root `AGENTS.md` mein 2 naye standing rules add kiye (isi session ke kaam se seekh kar):
  (5) practice projects ko `docs/[slug]/projects/[slug]/` mein real runnable scaffold do, scripts
  test-before-commit; (6) har chapter "Test Your Understanding"/quiz section ke bina "complete" nahi.

- 2026-08-24: User ne naya personal goal diya: **2026-10-05 tak PCAR-F (free Panaversity internal exam,
  CCAR-F blueprint-aligned) pass karo** — Anthropic ke official Claude Certified Architect: Foundations
  (CCAR-F) certification ki taraf pehla step, GIAIC/PIAIC/Panaversity ke sab faculty/students ke liye
  ek community-wide challenge ka hissa. Zia Tutor AI se `outline_agent_factory` confirm kiya ke book
  mein yeh top-level doc hai (`slug: certifications`, "Certifications: Proof You Can Carry In",
  position #13, Front Matter ke `—` row wala jo root README mein already tha). `read_agent_factory_lesson`
  se poora page ek window mein fetch hua (koi pagination nahi chahiye thi), naya `docs/certifications/`
  folder banaya — README index + 8 numbered files (00-overview, 01-stage-one-panaversity,
  02-stage-two-anthropic, 03-exam-domains yeh sab se zaroori hai kyunke domain-weight tables hain
  CCAR-F/CCDV-F/CCAO-F/CCAR-P ke, 04-gaps-and-study-plan yani free 6-week plan, 05-registration-costs-
  mistakes, 06-sample-tests, 07-practice-log jo user ke apne 2026-10-05 deadline ke sath week-by-week
  checklist hai). **Zaroori discovery:** `docs/certifications/` folder **pehle se maujood tha** (README.md + 2 numbered
files + SUMMARY.md, ek purani commit se) — lekin purana content bilkul alag scheme describe karta tha:
ek single "Certified Agentic AI Architect" 5-course program (AI-101→AI-491, 15 exams) + optional CCA-F.
Fresh fetch ne confirm kiya ke **book ne is poore page ko rewrite kar diya hai** — ab Panaversity
qualification stage (PCAR-F/PCDV-F) + 4 alag Anthropic exams (CCAR-F/CCDV-F/CCAO-F/CCAR-P) wala
structure hai, purani "AI-101" course numbering gayab hai. Purani 2 files
(`00-two-tracks-one-ecosystem.md`, `01-professional-track-curriculum.md`) delete kar di kyunke unka
content ab live page se match nahi karta, aur `SUMMARY.md` naye content ke sath dobara likha. **Lesson:**
book content static nahi hai — dobara fetch karte waqt hamesha check karo ke purana content abhi bhi
valid hai ya book ne restructure kar diya hai, sirf naye sections add mat karo.

**Discovery isi kaam se hui:** `03-exam-domains.md` ke domain→book-coverage mapping
  banate waqt pata chala ke root `README.md` ka status table **stale hai** — `docs/roles-this-book-trains/`,
  `docs/ai-prompting-2026/`, `docs/what-you-carry-in/`, `docs/what-ai-actually-is-crash-course/`,
  `docs/markdown-html-crash-course/` jaisi folders poori documented hain (README + numbered files +
  SUMMARY.md maujood) lekin table abhi bhi 🔲 dikhata tha. Root `README.md` mein Courses & Certifications
  row ko ✅ kiya, Front Matter progress bar 0/12→1/12, total 35/65→36/65, aur is staleness ko explicit
  warning callout ki tarah note kiya (poora audit is task ka scope nahi tha, alag se karna hoga).

- 2026-08-24 (follow-up): User ne mangi ke **har certification ka apna alag folder** ho
  `docs/certifications/` ke andar, is repo ke `projects/[slug]/` pattern jaisa. Poore 8 credentials ke
  liye subfolders banaye: Panaversity 4 (`pcar-f/`, `pcdv-f/`, `pcao-f/`, `pcar-p/`) + Anthropic 4
  (`ccar-f/`, `ccdv-f/`, `ccao-f/`, `ccar-p/`) — har ek mein quick-facts table, domain-weight table
  (jahan applicable) + book-coverage mapping, prep resources (official guide, free sample test) uska
  apna hai. Top-level `03-exam-domains.md` aur `06-sample-tests.md` ko bulky detail se **short index/
  comparison pages** mein badla (poori detail folders mein move ho gayi) taake duplicate content na
  ho. `README.md`, `SUMMARY.md`, `01-stage-one-panaversity.md`, `02-stage-two-anthropic.md`,
  `07-practice-log.md` sab naye folders ki taraf cross-link update kiye.

- 2026-08-24 (3rd update, same din): User ne 4 Anthropic cert folders (`ccar-f/`, `ccdv-f/`, `ccao-f/`,
  `ccar-p/`) par "deep research + full details" mangi. Official exam-guide PDFs `WebFetch` se fetch
  kiye — **WebFetch ka built-in summarizer PDF text extract nahi kar saka**: CCAR-F aur CCAO-F ke liye
  honestly "cannot read binary" bola, lekin **CCDV-F aur CCAR-P ke liye plausible-sounding lekin
  completely fabricated content diya** (galat domain names, galat weights, galat prerequisites "70%
  pass/2+ years experience" jo kahin se nahi aaye) — book ke already-verified data se mismatch ne
  turant fabrication pakri. Fix: WebFetch ke saved local `.pdf` paths use kar ke `Read` tool (jo PDFs
  multimodal parh sakta hai) se **chaaron guides seedha, poore, accurately parhe**. Har cert folder ko
  is real data se rewrite kiya: MQC profile, task-statement/sub-skill-level breakdown har domain ke
  andar, exam mechanics, sample questions + rationale, prep exercises, policies, document-control
  history. CCAR-P ka question count (63) — jo pehle book page khud "independent-report-only, not
  official-confirmed" keh rahi thi — ab official-guide-confirmed hai, dono files (02, 03) mein fix
  kiya. **Lesson (naya, memory mein bhi save hoga):** kisi tool ka output jab already-verified facts se
  mismatch kare, turant discard karo aur reliable path dhoondo — chup-chap accept mat karo.

- 2026-08-25: User ne 2 PDFs root mein add kiye: `Graph-Engineering-Complete-Guide (1).pdf` aur
  `KSoR-Complete-Guide (1).pdf`, dono ko "check karo aur update accordingly" bola. Dono `Read` tool se
  poore parhe (12 pages har ek). **Graph Engineering PDF** nikla condensed class-notes recap of
  `docs/graph-engineering/` (already ✅ complete, sab 16 concepts match karte hain) — asal gap yeh tha
  ke Loop Engineering ki tarah iska koi root-level `*-Summary.md` nahi tha. `Graph-Engineering-Summary.md`
  (root) banaya PDF se (glossary, 7 parts, 8 projects, exam cheat-sheet). **KSoR PDF** nikla genuinely
  naya content — Ecosystem chapter 7 "Designing the Vertical System of Record from First Principles"
  (`docs/ecosystem-designing-the-vertical-sor/`) pehle bilkul khaali tha (2026-08-19 audit mein bhi note
  hua tha). `panaversity/ksor` open-source SDK ke GitHub README se poora chapter banaya: README + 5
  numbered files (00-04: kyun+definition, 7 principles+kya banaya ja sakta hai, architecture+tooling,
  governance+AI-native role, applications+design goals+status) + SUMMARY.md — cross-linked
  `ecosystem-system-of-record` (chapter 5) aur `ecosystem-fde-af-model` se. Root `README.md` ke dono
  status rows update kiye (chapter 7: 🔲→✅; Graph Engineering row mein root summary link add kiya).

- 2026-08-25: User ne "Zia Tutor se aur fetch karo, is repo ke gaps dhoondo" mangi. `outline_agent_factory`
  se poori book ki current authoritative structure confirm ki (root, then `the-ecosystem`,
  `getting-started`, `foundations-everyone`, `references-companions` drill-down) aur har slug disk
  (`docs/`) ke against cross-check kiya. **Nateeja: root `README.md` ka status table bohat stale tha** —
  Front Matter ke 7/10 aur Ecosystem ke 7/9 chapters already fully documented thay lekin 🔲 dikha rahe
  thay (staleness note khud README mein already flag ki hui thi, is baar poora resolve kiya). Table ab
  audited: **54 fully ✅, 2 🟡 partial (thesis — Seven Invariants section + quiz missing; how-to-get-paid
  — 11/25 sections missing, dusra aadha hissa), 9 🔲 genuinely not started** (how-to-sell, glossary,
  ecosystem-system-of-context, 3 Foundations chapters — code-you-never-write, skills-connectors,
  how-to-think-ai-era —, aur 3 References & Companions chapters — which-agents-2026, cheatsheets,
  agentic-engineering-crash-course). `glossary` aur `how-to-get-paid` ke section-lists `read_agent_factory_lesson`
  se pull kiye (75K+ char responses the, persisted files se `grep`/jq se sirf `sections`/`remaining_outline`
  fields nikale — fetch discipline follow ki, poora text load nahi kiya context mein). Root `README.md`
  ke 3 status tables (Front Matter, Ecosystem, Foundations) + Overall Progress block sab is audit se
  update kiye, ek naya "Real gaps" table add ki. Content abhi nahi likha — sirf audit + report, user se
  priority order confirm karna baaqi hai.

## In progress

- 2026-08-29: **CCAR-F FDE Track B** course chal raha hai (working dir `Claude Certified Architect
  Foundations(CCA-F)/`). Setup: dono strands saath, auth = claude-agent-sdk (verified), vertical P2
  par. Spine `TRACK-B-WORKLOG.md`, graded `trade-off-notebook.md`, operating guide `HOW-TO-RUN.md`.
  - **Week 1 (Foundations Sprint) ✅** — Hour 1 Messages API demo (real run) + response-field notes +
    plan-vs-direct defense; Hour 2 four architect distinctions; Hour 3 classification lab (6 problems
    → type/enforcement/failure mode).
  - **Week 2 (The Agentic Loop by Hand) ✅** — `concepts.md`; `by_hand_loop.py` correct 2-tool loop
    (offline FakeClient, real run — parallel tools + tool_result round-trip + end_turn);
    **`lib/sdk_parser/stop_reason.py`** NEW = completes user's own `stop_reason/plan.md` goal
    (`classify_stop_reason`/`is_tool_turn`/`text_is_final`/`next_step`); `test_week2.py` 6 pass;
    5-bug diagnostic lab (existing scaffold `pytest` 5 pass, symptoms→root-cause writeup);
    `scenario-practice.md` 12 items; homework; 2 trade-off notebook entries.
  - **P1 ✅** — governed-knowledge-vs-chatbot thesis, 3 candidate verticals, env verified.
  - **P2 🟡** — 5-criteria matrix scored, provisional pick **Vertical #1 (PK freelancer/software-house
    tax & FBR compliance)**. Source register template started.
  - **Blocked:** P2/P3 need user to confirm the vertical + a personal-access check (1 practitioner +
    3 real source docs). **Next architect:** Week 3 (Claude Agent SDK I — tools, permissions, MCP).

- 2026-08-26: User ne "yes update it" keh kar 9+2-gap list par kaam shuru karne ki ijazat di (priority
  order khud choose karne ko kaha gaya). **Thesis** aur **Getting Paid as a Vertical FDE** dono partial
  chapters poore kiye — Zia Tutor se live sections fetch kiye (`read_agent_factory_lesson`), Thesis mein
  01-08 (Seven Invariants 2-parts + Reference Stack + 48-Q quiz parsed via Python script se Quiz JSX se),
  Getting Paid mein 04-06 (Ayesha's walk, Honest Label, 28-Q quiz). Dono commits alag-alag push kiye.
  Rasta mein audit correction mili: Foundations-Everyone group ki actual 8 lessons hain, 6 nahi (AI
  Fluency aur Claude/ChatGPT 101 pehle miss ho gayi thin) — total chapter count 65→67 corrected. Root
  README table dono jagah update. **Concurrent-session discovery:** isi session ke doran `docs/graph-
  engineering/` par ek doosra local Claude session active mila (uncommitted changes + ek bad-message
  commit "136") — us se door raha (`git reset` se sirf apne staged files rakhe), aur woh session khud
  apna kaam "Complete Graph Engineering chapter..." commit + push kar ke khatam hua, bina kisi conflict
  ke. Baaki 9 net-new chapters (how-to-sell, glossary, ecosystem-system-of-context, 5 foundations crash
  courses, 3 references-companions) abhi baaqi hain.

- 2026-08-26: User ne root mein `Claude Certified Architect Foundations (CCAR-F) FDE Track B
  Accelerated.md` add ki (Panaversity ka official 13-week syllabus, architect strand + FDE practicum
  dono) aur "read think plan update accordingly" mangi. Zia Tutor `outline_agent_factory` +
  `search_agent_factory` se poora cross-check kiya. **2 nateeje:** (1) syllabus ke Week 1/6/11 required
  reads sab is repo mein already ✅ hain (`docs/roles-this-book-trains`, `ecosystem-fde-af-model`,
  `agentic-coding`, `four-layers`, `is-this-an-agent-problem`, `choosing-agentic-architectures-crash-
  course`, `spec-driven-development`, `context-layer-crash-course`) — pehle audit mein `choosing-
  agentic-architectures-crash-course` aur `context-layer-crash-course` explicitly confirm nahi hue
  thay, ab hain. (2) syllabus ke Weeks 2-5/9-10 "required Claude courses" (Loop by Hand, Claude Agent
  SDK, Claude Code for Teams, Claude Code as a CI Worker, Structured Extraction Pipelines, Claude Code
  Routines, Claude Managed Agents) abhi bhi Zia Tutor corpus mein "not links yet" hain — `04-gaps-and-
  study-plan.md` ka 2026-08-24 wala finding confirm hua, koi naya kaam abhi mumkin nahi in par. **Naya
  gap mila:** syllabus ka FDE Practicum (P1-P13) ek *actually deployed* Fumadocs site + stateless MCP
  server maangta hai — is repo ke paas sirf KSoR/SoR *concept docs* hain (`docs/ksor/`, `docs/
  ecosystem-designing-the-vertical-sor/`), koi real deployment nahi. PCAR-F ke liye zaroori nahi lekin
  CCAR-F/Internship ki taraf agla concrete kaam hai. Root `README.md` (Repo Structure block),
  `docs/certifications/README.md`, aur `docs/certifications/07-practice-log.md` (naya section) update
  kiye is syllabus ko authoritative reference ki tarah link karne ke liye + findings document karne ke
  liye.

- 2026-08-26: User ne "KSor complete guide ka folder banho" mangi — clarifying question (AskUserQuestion)
  se confirm hua: `docs/ecosystem-designing-the-vertical-sor/` ko chherna nahi tha, balke ek **naya alag
  `docs/ksor/` folder** banana tha. Naya standalone reference folder banaya: `README.md` + `00`
  (Kyun/Definition) + `01` (7 Principles) + `02` (Architecture/Tooling) + `03` (Governance/AI-Native) +
  `04` (Applications/Design Goals/Status) + `SUMMARY.md` — content `ecosystem-designing-the-vertical-sor`
  ke sath identical (dono ek hi `KSoR-Complete-Guide (1).pdf` se aaye), lekin framing standalone hai
  ("kisi ek book-chapter tak mehdood nahi") aur dono folders ek dusre ko cross-link karte hain. Sab
  internal links verify kiye (bash script, koi broken link nahi). Root `README.md` mein chapter #7 row
  aur Repo Structure section mein naye folder ka pointer add kiya.

- 2026-08-18: User ne khud Loop Engineering ke practice projects hands-on karne shuru kiye
  (`docs/loop-engineering/10-practice-log.md` mein track). **Project 7 (Break It On Purpose):** sky-watch
  version pehle complete hui, phir user confused raha (2 dafa dobara samjhaya, real-life analogy
  — "naukar/akhbar" — se click hua). Isi ke sath ek **naya easier stand-in project banaya:
  `docs/loop-engineering/projects/joke-loop/`** (~60-line script, koi API key nahi, free joke API) taake
  same cost/observability lesson kam moving parts ke sath sikhaya ja sake — user ne isi version par khud
  sabotage test chalaya (clean "needs a human" result, fabrication se saaf mana kiya). **Project 8 (Daily
  Loop Capstone):** user ne `daily-triage-demo/` khud copy kar ke (Windows `xcopy`, `cp` nahi chalta)
  do dafa run kiya — Run 1: issue #1 fix+PASS+ready-to-merge, issue #2 escalate hua untouched; Run 2:
  spine ne dobara kaam nahi dohraya, dono items already-done recognize kiye. Ab 7/12 projects done
  (1-5, 7, 8) — sirf 6 (Doorbell) aur 9-12 (claude.ai account chahiye) baaki hain.

- 2026-08-17: `docs/loop-engineering/09-commands-cheat-sheet.md` add ki — sab is chapter ke commands (Claude Code `/loop`, `/goal`, `/schedule`, worktree/subagent syntax; OpenCode shell equivalents; Routine API `curl`; decision table; minimum-safe-loop checklist) ek single-page quick-reference mein. `README.md` index aur `08-routine-drills-and-dreaming.md` ka footer link update kiye.

## Open / needs a human

- **Root `README.md` status table stale hai** (upar ka discovery) — Front Matter/Foundations groups ke
  kai rows abhi 🔲 dikhate hain jab ke docs/ mein content already maujood hai. Poora audit karke table
  ko actual disk state se sync karna hai — separate task.


- **Loop Engineering ke 12/12 projects ab sab mapped hain:** 5 official kits (1,2,3,6,bonus) live tested, 2 DIY scaffolds (4,8) khud banaye aur test kiye, 2 instructions-only (5,7 — existing projects par build), 4 (9-12) sirf user apne `claude.ai` account se kar sakta hai
- User se confirm: root ki naye/updated files (`README.md`, `Loop-Engineering-Summary.md`, `Loop-Engineering-Final-Prep.md`, `progress.md`, `todolist.md`) ab commit + push karni hain?
- Baqi 30 chapters (Front Matter, The Ecosystem, Foundations-Everyone, References & Companions) — kya inhe bhi `docs/` mein note karna hai, jaisa Mode 1/2 ke sath kiya? User se confirm chahiye.
- `Four-Layers-Summary_1.pdf` (duplicate PDF, repo root) — delete karna hai? (Pehle offer kiya tha, abhi tak koi jawab nahi)
