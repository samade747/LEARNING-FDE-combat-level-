# Spec-Driven Development — Summary

Chapter #6, "thinking discipline hai, coding skill nahi." Core: "Agree on the what before you generate
the how." Data point: Anthropic ke ~400K sessions mein log planning ka 70% khud karte, agent execution
ka 80%; success ka sabse bara predictor coding skill nahi, **domain expertise** thi.

## 00 — The Shift

- **Concept 1 — Vibe coding vs SDD:** Farq hai aap sochte kab ho. Vibe coding = banate waqt sochna (cost
  baad mein ek saath aati); SDD = pehle sochna, likhna, phir build mostly mechanical. Rule of thumb:
  result phenkne se bura lagega to spec likho.
- **Concept 2 — Spec product hai, code build output:** Purana: spec→build→phenko; SDD ulta: spec durable,
  code usse regenerate hota. "Build output" ≠ black box — Valentina Servile (Thoughtworks) finding: tangled
  codebase mein agent zyada galat assumptions banata hai. Achi spec 3 sawal answer karti (why/what/what-
  NOT-to-build), HOW missing hai (spec behavior, plan implementation). Test: "kya koi competent banda ye
  line satisfy karte hue galat cheez bana sakta hai?" — haan to line vague hai.
- **Concept 3 — SDD ke 3 levels:** Spec-First (default, zyada tar features), Spec-Anchored (mahino
  maintain), Spec-as-Source (mature/high-discipline teams — claim sabse bara, evidence sabse kam,
  production mein agent-written systems tez decay hoti). Course: Spec-First se shuru, Spec-Anchored ki
  taraf badho.

## 01 — The Method (Constitution + 4 Phases)

- **Concept 4 — Constitution:** persistent rules for sab features (`CLAUDE.md`/`AGENTS.md`/claude.ai
  Project instructions) — persistent **context** hai, enforced law nahi (tests/hooks/CI se back karo).
  Example template diya gaya (Principles/Constraints/Definition of done). Zyada sakht constitution zeher
  deti hai — "stakes se match karo." Test: "ise hatane se AI galti karega?"
- **Concept 5 — Phase 1 Research:** AI se territory map karwao. Power move: parallel research via
  subagents (4 areas — usual approach, trade-offs, existing-project fit, failure modes).
- **Concept 6 — Phase 2 Specify:** 6 sections — Goal, User scenarios, Functional requirements, Edge
  cases & rules, Out of scope (kabhi skip mat karo), Acceptance criteria. "Tighten by hand" example
  (password reset: vague → precise with expiry/no-enumeration).
- **Concept 7 — Phase 3 Clarify (AI se poochwao):** Sabse zyada value, sabse zyada skip — AI se **aapko**
  interview karwao, ambiguities/edge-cases/assumptions par. Sabse sasti galti-fix jagah. Skip-karne-ka
  cost example: profile photo upload — 3 bugs jo 3 sentences hote (size limit, uniqueness, fallback).
- **Concept 8 — Phase 4 Build:** Process = change size ke barabar (1-sentence → poocho; kuch files →
  pehle plan; multi-file → poora loop). 2 constants: code se pehle approach review, result spec ke
  against check. Agent khud task breakdown karta hai. Strong model se plan, cheap model se implement.
  2nd check: design pass — agent khud ka bura judge hai (passing build ke liye optimize karta).

## 02 — Three Ways: claude.ai, Claude Code, OpenCode

- **Concept 9 — claude.ai:** Projects (persistent workspace) + Artifacts (editable docs). Setup: Project
  banao, constitution custom instructions mein, docs Project knowledge mein. 4 phases 4 artifacts banate
  (findings/spec.md/interview-fold/plan.md→tasks.md→code). ChatGPT/Gemini same discipline (Projects+
  Canvas / Gem+Canvas). Ehtiyat: sensitive data web assistant mein paste mat karo.
- **Concept 10 — Claude Code:** Constitution = `CLAUDE.md` file (Claude har session parhta). Plan mode
  (`Shift+Tab`) = Specify/Clarify gate, enforced (code nahi likh sakta jab tak approve). Subagents
  parallel research. Agent apni task list khud maintain, aap review/commit har step. Sab 4 artifacts
  plain files, version control, PR review.
- **Concept 11 — OpenCode:** Same shape, `AGENTS.md` constitution, Plan mode (`Tab`), git-backed `/undo`.
  Naya: model choice — strong reasoning model spec/plan ke liye, cheap model (`deepseek-v4-flash`)
  agreed task list build ke liye.

## 03 — Complete Worked Example: Weekly Digest

- Feature: har user ko har Monday notes summary email — kai files touch karta (poori loop deserve karta,
  Concept 8 right-sizing rule se). 2 dafa chalaya: claude.ai (thinking visible) phir Claude Code (real
  repo files).
- **claude.ai run:** Research phase se **time-zone question** nikalta hai jo socha nahi tha. Clarify se
  3 unstated decisions: local Monday not UTC, zero-notes-week = no email, unsubscribed users skip.
- **Claude Code run:** subagents per-area research, `specs/weekly-digest/research.md`; Plan mode enforce
  karta; task-by-task build, commit-per-step, `git log` task-list jaisa parhta.
- **Asal farq:** spec kahan reh gayi — claude.ai Artifact vs Claude Code `specs/` (version-controlled).
- Trimmed artifact shapes diye gaye: `spec.md` (FR-1 se FR-5, har ek testable), `plan.md` (approach —
  existing mailer reuse), `tasks.md` (5 tasks, har ek apna FR cite karta, aakhri task verification).

## 04 — Judgment (Kab Use Karein, Kab Nahi)

- **Concept 13 — Kab SDD, kab overkill:** Table — SDD chuno (multi-file, maintained hoga, galat hona
  mehnga, fuzzy requirements, multiple stakeholders) vs skip/vibe (one-off script, aaj hi phenk denge,
  undo-cheap, task clear, exploring/learning). "Button blue karo" ko poori process se guzaarna absurd.
  Beginners method ko theek bura lagne pe chhod dete hain, kamai hone se pehle.
- Doosra faida — unstuck karna: Anthropic data mein sabse kam-experienced users **give up** karte
  (doosron se kai guna zyada rate). Pehle-se-agreed spec = steering wheel.
- **Spec ko zinda rakho:** sirf tab source of truth jab sach rahe. Drift example: subject-line seedha
  code mein badla, spec purani reh gayi, naya teammate spec parh kar chalte kaam ko "fix" kar deta hai —
  fix: change spec.md mein jaye, code ke sath usi commit mein hamesha (Spec-First → Spec-Anchored).
- **Specs ki limit — Valentina Servile ke 3 counter-points** (maximalist "spec is the only language"
  view ke khilaf): natural language ambiguous ban jata (compiler-less programming), agents non-
  deterministic (judgment spec file mein nahi rehta), agent-written code decay hoti hai. SDD in teenon
  se bachta hai table ke sath (acceptance criteria = executable checks; plan+result dono review; design
  pass fixed point; "spec zinda rakho" hi Waterfall se farq).
- Reframe: code ke ab 2 readers hain — insan (judge) aur agent (agla badlaav). Discipline "spec instead
  of code" nahi — "what pe agree karo, how generate karo, phir dekho kya nikla."

## 05 — Practice (6 Projects)

- 4 artifacts har project ke liye: constitution, spec.md, plan.md, tasks.md, + working result. Success
  test: "kya ajnabi sirf spec se sahi cheez bana sakta hai, sawal poochhe bagair?"
- **Warm-up** (claude.ai, ~30min): sabse chhoti real cheez, interview mehsoos karo, decisions count karo.
- **Project 1** (claude.ai, ~1hr): "Tag and filter" feature, edge cases pin karo.
- **Project 2** (Claude Code/OpenCode, ~2hrs): repo mein move, task-per-commit, `git log` clean dikhna
  chahiye.
- **Project 3** (sabse mushkil, ~1hr): spec ko zinda rakho — naya requirement, pehle spec edit, phir
  Clarify dobara, phir implement. Diff match test.
- **Project 4** (~2hrs): existing open-source code mein kaam — Phase 1 sabse zaroori, "fits the existing
  system" spec section.
- **Project 5** (claude.ai, ~45min): bina code ke SDD — repeatable process (report/pipeline/routine),
  build phase se process+prompts nikalte hain, source code nahi.
- **Project 6 — Stranger Test, Capstone** (~1.5hrs): spec kisi fresh session/peer ko do zero sawal ke
  sath — jahan bhi galat bane, spec ki galti hai unki nahi, spec fix karo code nahi.
