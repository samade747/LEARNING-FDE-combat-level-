# 01 — Domain Blueprint (Full Task Statements)

*Source: Official exam guide, section 4 (Exam Content Outline) + section 6 (Detailed Objectives by
Domain). Yeh sabse bara file hai is folder mein — pura blueprint jis pe exam items likhe jate hain.*

**Correction note (2026-08-24):** Is repo ke pehle wale single-file README mein Domain 2/3/4 ka
numbering PDF se mismatch tha (Claude Code Config ko "Domain 2" aur Tool Design ko "Domain 4" likha
gaya tha). Official guide ka apna order neeche hai — **Domain 2 = Tool Design & MCP Integration (18%),
Domain 3 = Claude Code Configuration (20%), Domain 4 = Prompt Engineering (20%)**. Weights aur
content khud sab sahi thay, sirf numbering corrected hui hai.

## Domain Weight Table

| Domain | Content Domain | Weight |
| --- | --- | --- |
| 1 | Agentic Architecture & Orchestration | **27%** |
| 2 | Tool Design & MCP Integration | 18% |
| 3 | Claude Code Configuration & Workflows | 20% |
| 4 | Prompt Engineering & Structured Output | 20% |
| 5 | Context Management & Reliability | 15% |
| | **Total** | **100%** |

**Study priority:** Domain 1 (27%) akela sab se bara hai → Domain 3+4 (20%+20%=40%) → Domain 2
(18%) → Domain 5 (15%). Weights job-task-analysis se aayi hain — competent performance ke liye har
domain ki relative importance batati hain.

---

## Domain 1 — Agentic Architecture & Orchestration (27%)

### Task Statement 1.1 — Agentic loops design/implement karna autonomous task execution ke liye
- **Knowledge:** agentic loop lifecycle (request → `stop_reason` check "tool_use" vs "end_turn" →
  tool execute → result agli iteration mein); tool results conversation history mein append hote hain
  taaki model agla action reason kar sake; model-driven decision-making vs pre-configured decision
  trees ka farq
- **Skills:** loop control-flow implement karna jo `stop_reason` "tool_use" par continue aur "end_turn"
  par terminate ho; tool results ko iterations ke beech context mein add karna; anti-patterns avoid
  karna — natural-language signals parse karke termination decide karna, arbitrary iteration caps ko
  primary stopping mechanism banana, ya assistant text content ko completion indicator maan lena

### Task Statement 1.2 — Multi-agent systems orchestrate karna coordinator-subagent patterns se
- **Knowledge:** hub-and-spoke architecture jahan coordinator sab inter-subagent communication,
  error handling, aur routing manage karta hai; subagents **isolated context** ke sath operate karte
  hain — coordinator ki conversation history automatically inherit nahi karte; coordinator ka role
  decomposition, delegation, result aggregation, aur query complexity ke hisaab se subagent-selection
  mein; overly narrow decomposition ka risk (broad topics incomplete cover hote hain)
- **Skills:** coordinator design karna jo query requirements analyze kar ke dynamically subagents
  select kare (fixed pipeline nahi); research scope subagents mein partition karna duplication kam
  karne ke liye; iterative refinement loops implement karna (coordinator synthesis output ke gaps
  evaluate kare, targeted re-delegation kare, coverage sufficient hone tak re-invoke kare); sab
  subagent communication coordinator se route karna observability + consistent error handling ke liye

### Task Statement 1.3 — Subagent invocation, context passing, spawning configure karna
- **Knowledge:** `Task` tool subagents spawn karne ka mechanism hai — coordinator ke `allowedTools`
  mein "Task" hona zaroori hai; subagent context **explicitly** prompt mein dena padta hai — parent
  context ya memory automatically inherit nahi hoti invocations ke beech; `AgentDefinition`
  configuration (descriptions, system prompts, tool restrictions har subagent type ke liye); fork-based
  session management divergent approaches explore karne ke liye ek shared baseline se
- **Skills:** prior agents ki complete findings directly subagent ke prompt mein include karna (jaise
  synthesis subagent ko web-search + doc-analysis outputs dena); structured data formats use karna
  content ko metadata (source URLs, doc names, page numbers) se separate rakhne ke liye attribution
  preserve karne ke liye; parallel subagents spawn karna ek hi coordinator response mein multiple
  `Task` calls emit kar ke (separate turns mein nahi); coordinator prompts design karna jo research
  goals/quality criteria specify karein, step-by-step procedures nahi — subagent adaptability ke liye

### Task Statement 1.4 — Multi-step workflows implement karna enforcement + handoff patterns ke sath
- **Knowledge:** programmatic enforcement (hooks, prerequisite gates) vs prompt-based guidance ka
  farq; deterministic compliance kab zaroori hai (jaise financial operations se pehle identity
  verification) — prompt instructions ka non-zero failure rate hota hai; structured handoff protocols
  mid-process escalation ke liye (customer details, root cause, recommended actions sameet)
- **Skills:** programmatic prerequisites implement karna jo downstream tool calls ko block karein jab
  tak prerequisite steps complete na hon (jaise `process_refund` ko `get_customer` ke verified ID tak
  block karna); multi-concern requests ko distinct items mein decompose karna, phir parallel
  investigate kar ke unified resolution synthesize karna; structured handoff summaries compile karna
  (customer ID, root cause, refund amount, recommended action) jab human agents ko escalate ho jinke
  paas transcript access nahi

### Task Statement 1.5 — Agent SDK hooks apply karna tool-call interception aur data normalization ke liye
- **Knowledge:** hook patterns (jaise `PostToolUse`) jo tool results ko model process karne se pehle
  transform karte hain; hook patterns jo outgoing tool calls intercept kar ke compliance rules enforce
  karte hain (jaise threshold se upar refunds block karna); hooks ka deterministic-guarantee use vs
  prompt-instructions ka probabilistic-compliance use
- **Skills:** `PostToolUse` hooks implement karna heterogeneous data formats (Unix timestamps, ISO
  8601, numeric status codes) different MCP tools se normalize karne ke liye; tool-call-interception
  hooks implement karna jo policy-violating actions block karein (jaise $500+ refunds) aur alternative
  workflow (human escalation) par redirect karein; hooks ko prompt-based enforcement se zyada
  choose karna jab business rules ko guaranteed compliance chahiye ho

### Task Statement 1.6 — Task decomposition strategies design karna complex workflows ke liye
- **Knowledge:** fixed sequential pipelines (prompt chaining) vs dynamic adaptive decomposition kab
  use karni hai intermediate findings ke hisaab se; prompt-chaining patterns jo reviews ko sequential
  steps mein break karte hain (per-file analysis, phir cross-file integration pass); adaptive
  investigation plans ki value jo har step par discovered cheezon se subtasks generate karte hain
- **Skills:** workflow ke hisaab se decomposition pattern select karna — predictable multi-aspect
  reviews ke liye prompt chaining, open-ended investigation ke liye dynamic decomposition; large
  code reviews ko per-file local passes + separate cross-file integration pass mein split karna
  attention dilution avoid karne ke liye; open-ended tasks decompose karna (jaise "legacy codebase
  mein comprehensive tests add karo") pehle structure map kar ke, high-impact areas identify kar ke,
  phir ek adapting prioritized plan banake

### Task Statement 1.7 — Session state, resumption, aur forking manage karna
- **Knowledge:** named session resumption (`--resume <session-name>`) specific prior conversation
  continue karne ke liye; `fork_session` independent branches banane ke liye ek shared analysis
  baseline se divergent approaches explore karne ke liye; resumed sessions ko file changes ke baare
  mein inform karne ki ahmiyat code modifications ke baad; stale tool results ke sath resume karne se
  behtar hai structured summary ke sath naya session start karna
- **Skills:** `--resume` session names ke sath use karna named investigation sessions continue karne
  ke liye across work sessions; `fork_session` use karna parallel exploration branches banane ke liye
  (jaise 2 testing strategies compare karna ek shared codebase-analysis se); session resumption
  (jab prior context mostly valid ho) vs fresh start with injected summaries (jab prior tool results
  stale hon) mein choose karna; resumed session ko specific file changes ke baare mein inform karna
  targeted re-analysis ke liye, poori re-exploration ki bajaye

---

## Domain 2 — Tool Design & MCP Integration (18%)

### Task Statement 2.1 — Effective tool interfaces design karna clear descriptions + boundaries ke sath
- **Knowledge:** tool descriptions LLM ka primary tool-selection mechanism hain — minimal
  descriptions similar tools ke beech unreliable selection deti hain; input formats, example queries,
  edge cases, boundary explanations descriptions mein include karne ki ahmiyat; ambiguous/overlapping
  descriptions misrouting cause karte hain (jaise `analyze_content` vs `analyze_document` near-identical
  descriptions ke sath); system-prompt wording ka tool-selection par impact — keyword-sensitive
  instructions unintended tool associations bana sakti hain
- **Skills:** tool descriptions likhna jo har tool ka purpose, expected inputs/outputs, aur kab-use-karna
  clearly differentiate karein; tools rename/update karna functional overlap khatam karne ke liye;
  generic tools ko purpose-specific tools mein split karna defined input/output contracts ke sath;
  system prompts review karna keyword-sensitive instructions ke liye jo well-written descriptions ko
  override kar sakti hain

### Task Statement 2.2 — Structured error responses implement karna MCP tools ke liye
- **Knowledge:** MCP `isError` flag pattern tool failures communicate karne ke liye; transient errors
  (timeouts) vs validation errors (invalid input) vs business errors (policy violations) vs permission
  errors ka farq; uniform generic error responses ("Operation failed") agent ko appropriate recovery
  decisions lene se rokte hain; retryable vs non-retryable errors ka farq, structured metadata wasted
  retries prevent karta hai
- **Skills:** structured error metadata return karna — `errorCategory` (transient/validation/permission),
  `isRetryable` boolean, human-readable description; `retriable: false` flags + customer-friendly
  explanations business-rule violations ke liye; subagents mein local error recovery implement karna
  transient failures ke liye, sirf unresolvable errors coordinator ko propagate karna partial results ke
  sath; access failures (retry-decision-needed) ko valid empty results (successful-no-match) se
  distinguish karna

### Task Statement 2.3 — Tools appropriately distribute karna agents ke across + tool_choice configure karna
- **Knowledge:** ek agent ko zyada tools dena (jaise 18 instead of 4-5) tool-selection reliability
  degrade karta hai decision-complexity badhane se; specialization se bahar ke tools agent misuse
  karte hain (jaise synthesis agent web-search attempt kare); scoped tool access — agent ko sirf uske
  role ke tools dena, limited cross-role tools high-frequency needs ke liye; `tool_choice` options:
  "auto", "any", forced selection (`{"type": "tool", "name": "..."}`)
- **Skills:** har subagent ka tool-set uske role tak restrict karna cross-specialization misuse rokne ke
  liye; generic tools ko constrained alternatives se replace karna (jaise `fetch_url` ko `load_document`
  se replace karna jo document URLs validate kare); scoped cross-role tools provide karna high-frequency
  needs ke liye (jaise synthesis agent ke liye `verify_fact` tool) complex cases coordinator se route
  karte hue; forced `tool_choice` use karna specific tool pehle call ho yeh ensure karne ke liye; `"any"`
  set karna guarantee karne ke liye ke model tool call kare, conversational text nahi

### Task Statement 2.4 — MCP servers integrate karna Claude Code + agent workflows mein
- **Knowledge:** MCP server scoping — project-level (`.mcp.json`) shared team tooling ke liye vs
  user-level (`~/.claude.json`) personal/experimental servers ke liye; `.mcp.json` mein environment
  variable expansion (jaise `${GITHUB_TOKEN}`) credential management ke liye bina secrets commit kiye;
  sab configured MCP servers ke tools connection-time par discover hote hain aur simultaneously
  available hote hain; MCP resources content catalogs expose karne ka mechanism hain (issue summaries,
  doc hierarchies, DB schemas) exploratory tool calls kam karne ke liye
- **Skills:** shared MCP servers project-scoped `.mcp.json` mein configure karna env-var expansion ke
  sath auth tokens ke liye; personal/experimental MCP servers user-scoped `~/.claude.json` mein
  configure karna; MCP tool descriptions enhance karna capabilities/outputs detail mein explain karne
  ke liye — agent ko built-in tools (jaise Grep) prefer karne se rokna jab MCP tool zyada capable ho;
  standard integrations (jaise Jira) ke liye existing community MCP servers choose karna custom
  implementations se zyada; content catalogs ko MCP resources ki tarah expose karna exploratory tool
  calls ki zaroorat khatam karne ke liye

### Task Statement 2.5 — Built-in tools (Read, Write, Edit, Bash, Grep, Glob) select + apply karna
- **Knowledge:** Grep content search ke liye (function names, error messages, imports patterns file
  contents mein dhoondna); Glob file-path pattern matching ke liye (naam/extension patterns se files
  dhoondna); Read/Write full-file operations ke liye; Edit targeted modifications ke liye unique text
  matching se; jab Edit non-unique text matches ki wajah se fail ho, Read+Write fallback use karna
- **Skills:** Grep select karna codebase content search ke liye (function ke sab callers dhoondna, error
  messages locate karna); Glob select karna naming-pattern files dhoondne ke liye (jaise `**/*.test.tsx`);
  Read use karna full file load karne ke liye phir Write jab Edit unique anchor text na dhoondh paye;
  codebase understanding incrementally build karna — pehle Grep se entry points, phir Read se imports
  follow karna, sab files upfront read karne ki bajaye; wrapper modules ke across function-usage trace
  karna pehle exported names identify kar ke, phir har naam codebase mein search kar ke

---

## Domain 3 — Claude Code Configuration & Workflows (20%)

### Task Statement 3.1 — CLAUDE.md files configure karna hierarchy, scoping, modular organization ke sath
- **Knowledge:** CLAUDE.md hierarchy — user-level (`~/.claude/CLAUDE.md`), project-level
  (`.claude/CLAUDE.md` ya root `CLAUDE.md`), directory-level (subdirectory CLAUDE.md files);
  user-level settings sirf usi user ke liye apply hote hain — `~/.claude/CLAUDE.md` version control ke
  zariye teammates ke sath share nahi hota; `@import` syntax modular CLAUDE.md ke liye (har package
  ke liye relevant standards files import karna); `.claude/rules/` directory topic-specific rule files ke
  liye ek monolithic CLAUDE.md ke alternative ke tarah
- **Skills:** configuration-hierarchy issues diagnose karna (jaise naya team member instructions
  receive nahi kar raha kyunki wo user-level mein hain, project-level mein nahi); `@import` use karna
  har package ke CLAUDE.md mein selectively relevant standards include karne ke liye; bare CLAUDE.md
  files ko `.claude/rules/` mein focused topic-specific files mein split karna (jaise `testing.md`,
  `api-conventions.md`); `/memory` command use karna verify karne ke liye kaunse memory files load
  hue hain, sessions ke across inconsistent behavior diagnose karne ke liye

### Task Statement 3.2 — Custom slash commands aur skills create/configure karna
- **Knowledge:** project-scoped commands `.claude/commands/` mein (version control ke zariye shared)
  vs user-scoped `~/.claude/commands/` mein (personal); skills `.claude/skills/` mein `SKILL.md` files
  ke sath jo frontmatter support karti hain — `context: fork`, `allowed-tools`, `argument-hint`;
  `context: fork` option skills ko isolated sub-agent context mein run karta hai, skill outputs ko main
  conversation pollute karne se rokta hai; personal skill customization — `~/.claude/skills/` mein
  different names ke sath personal variants banana taaki teammates affect na hon
- **Skills:** project-scoped slash commands `.claude/commands/` mein banana team-wide availability ke
  liye version control se; `context: fork` use karna verbose-output ya exploratory-context skills ko main
  session se isolate karne ke liye; `allowed-tools` configure karna skill frontmatter mein tool access
  restrict karne ke liye (jaise destructive actions rokne ke liye sirf file-write permissions); `argument-hint`
  frontmatter use karna developers ko required parameters prompt karne ke liye; skills (on-demand,
  task-specific) vs CLAUDE.md (always-loaded, universal) mein choose karna

### Task Statement 3.3 — Path-specific rules apply karna conditional convention loading ke liye
- **Knowledge:** `.claude/rules/` files YAML frontmatter `paths:` fields ke sath glob patterns rakhte
  hain conditional rule activation ke liye; path-scoped rules sirf tab load hote hain jab matching files
  edit ho rahi hon, irrelevant context/token usage kam karte hue; glob-pattern rules ka advantage
  directory-level CLAUDE.md files se un conventions ke liye jo multiple directories mein spread hain
  (jaise test files poore codebase mein)
- **Skills:** `.claude/rules/` files banana YAML frontmatter path-scoping ke sath (jaise
  `paths: ["terraform/**/*"]`) taaki rules sirf matching files edit karte waqt load hon; glob patterns use
  karna path-specific rules mein conventions ko file-type ke hisaab se apply karne ke liye directory
  location se independent (jaise `**/*.test.tsx` sab test files ke liye); path-specific rules ko
  subdirectory CLAUDE.md files se zyada choose karna jab conventions poore codebase mein spread
  files pe apply honi chahiye

### Task Statement 3.4 — Plan mode vs direct execution kab use karna hai determine karna
- **Knowledge:** plan mode complex tasks ke liye designed hai — large-scale changes, multiple valid
  approaches, architectural decisions, multi-file modifications; direct execution simple well-scoped
  changes ke liye appropriate hai (jaise ek function mein single validation check add karna); plan mode
  safe codebase exploration aur design enable karta hai changes commit karne se pehle, costly rework
  prevent karte hue; `Explore` subagent verbose discovery output isolate karne aur summaries return
  karne ke liye main conversation context preserve karne ke liye
- **Skills:** plan mode select karna architectural-implication tasks ke liye (jaise microservice
  restructuring, 45+ files affecting library migrations, different infra-requirement integration
  approaches choose karna); direct execution select karna well-understood clear-scope changes ke liye
  (jaise clear stack-trace wala single-file bug fix); `Explore` subagent use karna verbose discovery
  phases ke liye context-window exhaustion prevent karne ke liye multi-phase tasks mein; plan mode
  (investigation ke liye) ko direct execution (implementation ke liye) ke sath combine karna

### Task Statement 3.5 — Iterative refinement techniques apply karna progressive improvement ke liye
- **Knowledge:** concrete input/output examples sab se effective way hain expected transformations
  communicate karne ka jab prose descriptions inconsistently interpret ho rahi hon; test-driven
  iteration — pehle test suites likhna, phir test failures share kar ke progressive improvement guide
  karna; interview pattern — Claude se questions poochwana jo developer ne anticipate na kiye hon
  implementation se pehle; ek single message mein sab issues dena (interacting problems) vs
  sequentially fix karna (independent problems) kab appropriate hai
- **Skills:** 2-3 concrete input/output examples dena transformation requirements clarify karne ke liye
  jab natural-language descriptions inconsistent results dein; test suites likhna expected behavior,
  edge cases, performance requirements cover karte hue implementation se pehle, phir test failures
  share kar ke iterate karna; interview pattern use karna design considerations surface karne ke liye
  (jaise cache-invalidation strategies) implement karne se pehle unfamiliar domains mein; multiple
  interacting issues ek detailed message mein address karna jab fixes interact karte hon, vs sequential
  iteration independent issues ke liye

### Task Statement 3.6 — Claude Code CI/CD pipelines mein integrate karna
- **Knowledge:** `-p` (ya `--print`) flag Claude Code ko non-interactive mode mein automated pipelines
  mein chalane ke liye; `--output-format json` aur `--json-schema` CLI flags CI contexts mein structured
  output enforce karne ke liye; CLAUDE.md project context (testing standards, fixture conventions,
  review criteria) CI-invoked Claude Code ko dene ka mechanism; session context isolation — wahi
  Claude session jo code generate karta hai apne changes review karne mein independent-review-instance
  se kam effective hota hai
- **Skills:** Claude Code CI mein `-p` flag ke sath chalana interactive-input hangs prevent karne ke liye;
  `--output-format json` + `--json-schema` use karna machine-parseable structured findings produce
  karne ke liye automated inline-PR-comments posting ke liye; new commits ke baad reviews re-run karte
  waqt prior review findings context mein include karna, Claude ko sirf naye/still-unaddressed issues
  report karne ka instruct karna duplicate comments avoid karne ke liye; existing test files context
  mein dena taaki test generation duplicate scenarios suggest na kare jo already test suite mein
  covered hain; testing standards, valuable test criteria, aur available fixtures CLAUDE.md mein
  document karna test-generation quality improve karne ke liye

---

## Domain 4 — Prompt Engineering & Structured Output (20%)

### Task Statement 4.1 — Explicit criteria ke sath prompts design karna precision improve/false-positives kam karne ke liye
- **Knowledge:** explicit criteria ki ahmiyat vague instructions se zyada (jaise "flag comments only
  when claimed behavior contradicts actual code behavior" vs "check that comments are accurate");
  general instructions ("be conservative", "only report high-confidence findings") specific categorical
  criteria se compare karke precision improve nahi karti; false-positive rates ka developer trust par
  impact — high-false-positive categories accurate categories mein bhi confidence undermine karte hain
- **Skills:** specific review criteria likhna jo define karein kaunse issues report karne hain (bugs,
  security) vs skip karne hain (minor style), confidence-based filtering ki bajaye; high-false-positive
  categories temporarily disable karna developer trust restore karne ke liye jab tak prompts improve na
  hon; explicit severity criteria define karna concrete code examples ke sath har severity level ke liye
  consistent classification ke liye

### Task Statement 4.2 — Few-shot prompting apply karna output consistency/quality improve karne ke liye
- **Knowledge:** few-shot examples sab se effective technique hain consistently-formatted actionable
  output ke liye jab detailed instructions akele inconsistent results dein; few-shot examples ka role
  ambiguous-case handling demonstrate karne mein (jaise ambiguous requests ke liye tool selection);
  few-shot examples model ko novel patterns pe judgment generalize karne dete hain, sirf
  pre-specified cases match karne ki bajaye; extraction tasks mein hallucination kam karne mein
  few-shot ki effectiveness (jaise informal measurements, varied document structures handle karna)
- **Skills:** 2-4 targeted few-shot examples banana ambiguous scenarios ke liye jo reasoning dikhayein
  ke ek action kyun choose hua plausible alternatives ke against; few-shot examples include karna jo
  specific desired output format (location, issue, severity, fix) demonstrate karein consistency ke
  liye; acceptable code patterns ko genuine issues se distinguish karne wale few-shot examples dena
  false positives kam karte hue generalization enable karna; varied document structures ke correct
  handling ke liye few-shot examples use karna (inline citations vs bibliographies)

### Task Statement 4.3 — Structured output enforce karna tool use + JSON schemas se
- **Knowledge:** `tool_use` JSON schemas ke sath guaranteed schema-compliant structured output ka sab
  se reliable approach hai, JSON syntax errors eliminate karte hue; `tool_choice`: "auto" (model text
  bhi return kar sakta hai) vs "any" (tool call zaroori, lekin koi bhi) vs forced selection (specific
  named tool zaroori) ka farq; strict JSON schemas syntax errors eliminate karte hain lekin semantic
  errors nahi (jaise line items jo total tak sum nahi hote); schema design considerations — required vs
  optional fields, enum fields "other" + detail-string patterns extensible categories ke liye
- **Skills:** extraction tools JSON schemas input parameters ki tarah define karna aur `tool_use`
  response se structured data extract karna; `tool_choice: "any"` set karna structured output guarantee
  karne ke liye jab multiple extraction schemas exist karte hon aur doc type unknown ho; specific tool
  force karna (`{"type": "tool", "name": "extract_metadata"}`) ensure karne ke liye ke ek particular
  extraction enrichment se pehle chale; schema fields ko optional (nullable) design karna jab source
  documents info na rakhte hon, model ko required-fields satisfy karne ke liye values fabricate karne
  se rokte hue; "unclear" jaise enum values aur "other" + detail fields extensible categorization ke liye

### Task Statement 4.4 — Validation, retry, aur feedback loops implement karna extraction quality ke liye
- **Knowledge:** retry-with-error-feedback — specific validation errors prompt mein append karna retry
  par model ko correction ki taraf guide karne ke liye; retry ki limits — retries ineffective hote hain jab
  required info source document mein simply absent ho (format/structural errors ke against); feedback
  loop design — `detected_pattern` field track karna kaunse code constructs findings trigger karte hain
  dismissal-pattern analysis ke liye; semantic validation errors (values sum nahi hote) vs schema syntax
  errors (tool use se eliminate) ka farq
- **Skills:** follow-up requests implement karna jo original document, failed extraction, aur specific
  validation errors include karein model self-correction ke liye; identify karna kab retries ineffective
  honge (info sirf ek external doc mein hai jo provide nahi hui) vs kab succeed karenge (format
  mismatches); `detected_pattern` fields add karna structured findings mein false-positive-pattern
  analysis enable karne ke liye jab developers findings dismiss karte hain; self-correction validation
  flows design karna — "calculated_total" ko "stated_total" ke sath extract kar ke discrepancies flag
  karna, "conflict_detected" booleans add karna inconsistent source data ke liye

### Task Statement 4.5 — Efficient batch processing strategies design karna
- **Knowledge:** Message Batches API — 50% cost savings, 24-hour tak processing window, koi
  guaranteed latency SLA nahi; batch processing non-blocking latency-tolerant workloads ke liye
  appropriate hai (overnight reports, weekly audits) aur blocking workflows ke liye inappropriate
  (pre-merge checks); batch API multi-turn tool calling support nahi karta ek single request ke andar;
  `custom_id` fields batch request/response pairs correlate karne ke liye
- **Skills:** API approach ko workflow latency requirements se match karna — synchronous API blocking
  pre-merge checks ke liye, batch API overnight/weekly analysis ke liye; batch submission frequency
  calculate karna SLA constraints ke hisaab se (jaise 30-hour SLA guarantee karne ke liye 4-hour
  windows 24-hour batch processing ke sath); batch failures handle karna — sirf failed documents
  (`custom_id` se identify) resubmit karna appropriate modifications (jaise chunking) ke sath; prompt
  refinement ek sample set par karna large-volume batch-processing se pehle first-pass success rate
  maximize karne ke liye

### Task Statement 4.6 — Multi-instance aur multi-pass review architectures design karna
- **Knowledge:** self-review limitations — model generation se reasoning context retain karta hai, isi
  session mein apne decisions question karne ka chance kam ho jata hai; independent review instances
  (prior reasoning context ke bina) subtle issues catch karne mein self-review-instructions ya extended
  thinking se zyada effective hain; multi-pass review — large reviews ko per-file local-analysis passes
  + cross-file integration passes mein split karna attention dilution aur contradictory findings avoid
  karne ke liye
- **Skills:** ek doosra independent Claude instance use karna generated code review karne ke liye
  generator ke reasoning context ke bina; large multi-file reviews ko focused per-file passes (local
  issues) + separate integration passes (cross-file data-flow analysis) mein split karna; verification
  passes chalana jahan model confidence self-report kare har finding ke sath calibrated review routing
  enable karne ke liye

---

## Domain 5 — Context Management & Reliability (15%)

### Task Statement 5.1 — Conversation context manage karna critical information preserve karne ke liye long interactions mein
- **Knowledge:** progressive summarization risks — numerical values, percentages, dates, customer-stated
  expectations vague summaries mein condense ho jate hain; "lost in the middle" effect — models
  reliably beginning/end ki info process karte hain lekin middle-section findings omit kar sakte hain;
  tool results context mein accumulate hote hain aur unki relevance se disproportionately tokens
  consume karte hain (jaise order-lookup mein 40+ fields jab sirf 5 relevant hon); complete conversation
  history subsequent API requests mein pass karne ki ahmiyat conversational coherence ke liye
- **Skills:** transactional facts (amounts, dates, order numbers, statuses) ek persistent "case facts"
  block mein extract karna jo har prompt mein include ho, summarized history ke bahar; structured
  issue data (order IDs, amounts, statuses) ek separate context layer mein persist karna multi-issue
  sessions ke liye; verbose tool outputs ko sirf relevant fields tak trim karna context accumulate hone
  se pehle; key-findings summaries aggregated inputs ke start mein rakhna aur detailed results explicit
  section headers ke sath organize karna position effects mitigate karne ke liye

### Task Statement 5.2 — Effective escalation + ambiguity-resolution patterns design karna
- **Knowledge:** appropriate escalation triggers — customer human ki request kare, policy
  exceptions/gaps (sirf complex cases nahi), meaningful progress na kar pana; explicit customer demand
  par turant escalate karna vs straightforward issue par resolve offer karna ka farq; sentiment-based
  escalation aur self-reported confidence scores actual case-complexity ke unreliable proxies hain;
  multiple customer matches clarification maangte hain (additional identifiers request karna) heuristic
  selection ki bajaye
- **Skills:** explicit escalation criteria few-shot examples ke sath system prompt mein add karna kab
  escalate vs autonomously resolve karna hai demonstrate karne ke liye; explicit customer requests
  human agent ke liye turant honor karna bina pehle investigation attempt kiye; frustration
  acknowledge karte hue resolution offer karna jab issue agent ki capability mein ho, escalate sirf tab
  jab customer preference reiterate kare; policy ambiguous/silent hone par escalate karna specific
  customer request pe; agent ko instruct karna additional identifiers maangne ke liye jab tool results
  multiple matches dein, heuristic selection ki bajaye

### Task Statement 5.3 — Error-propagation strategies implement karna multi-agent systems ke across
- **Knowledge:** structured error context (failure type, attempted query, partial results, alternative
  approaches) coordinator ko intelligent recovery decisions lene deta hai; access failures (timeouts,
  retry-decision-needed) vs valid empty results (successful queries no matches ke sath) ka farq; generic
  error statuses ("search unavailable") coordinator se valuable context chupate hain; errors silently
  suppress karna (empty results ko success maan lena) ya single-failure par poora workflow terminate
  karna dono anti-patterns hain
- **Skills:** structured error context return karna (failure type, kya attempt hua, partial results,
  potential alternatives) coordinator recovery enable karne ke liye; access failures ko valid empty
  results se distinguish karna error reporting mein taaki coordinator appropriate decisions le sake;
  subagents mein local recovery implement karna transient failures ke liye, sirf unresolvable errors
  propagate karna (jo attempt hua + partial results ke sath); synthesis output ko coverage annotations
  ke sath structure karna — kaunsi findings well-supported hain vs kaunse topic-areas mein gaps hain

### Task Statement 5.4 — Context effectively manage karna large-codebase exploration mein
- **Knowledge:** extended sessions mein context degradation — model inconsistent answers dena shuru
  karta hai, "typical patterns" reference karta hai specific classes ki bajaye jo pehle discover hui thin;
  scratchpad files ka role key findings persist karne mein context boundaries ke across; subagent
  delegation verbose exploration output isolate karne ke liye jabke main agent high-level understanding
  coordinate karta hai; crash-recovery ke liye structured state persistence — har agent state ek known
  location par export karta hai, coordinator resume par manifest load karta hai
- **Skills:** subagents spawn karna specific questions investigate karne ke liye (jaise "find all test
  files") jabke main agent high-level coordination preserve karta hai; agents ko scratchpad files
  maintain karwana key findings record karne ke liye, subsequent questions ke liye unhe reference
  karna context degradation counteract karne ke liye; ek exploration phase se key findings summarize
  karna next-phase subagents spawn karne se pehle; crash recovery design karna structured agent
  state exports (manifests) se jo coordinator resume par load kare; `/compact` use karna context usage
  reduce karne ke liye extended exploration sessions mein

### Task Statement 5.5 — Human review workflows aur confidence calibration design karna
- **Knowledge:** aggregate accuracy metrics (jaise 97% overall) specific document types/fields par poor
  performance mask kar sakti hain; stratified random sampling high-confidence extractions mein error
  rates measure karne aur novel error patterns detect karne ke liye; field-level confidence scores
  labeled validation sets se calibrated review-attention routing ke liye; document-type/field ke hisaab
  se accuracy validate karne ki ahmiyat high-confidence extractions automate karne se pehle
- **Skills:** stratified random sampling implement karna high-confidence extractions ka ongoing
  error-rate measurement aur novel-pattern-detection ke liye; document-type/field ke hisaab se accuracy
  analyze karna consistent performance verify karne ke liye human review kam karne se pehle; models ko
  field-level confidence scores output karwana, phir review thresholds calibrate karna labeled
  validation sets se; low-model-confidence ya ambiguous/contradictory source documents wali
  extractions ko human review route karna, limited reviewer capacity prioritize karte hue

### Task Statement 5.6 — Information provenance preserve karna + uncertainty handle karna multi-source synthesis mein
- **Knowledge:** source attribution summarization steps mein lost ho jaati hai jab findings claim-source
  mappings preserve kiye bina compress hoti hain; structured claim-source mappings ki ahmiyat jo
  synthesis agent ko preserve/merge karna chahiye findings combine karte waqt; conflicting statistics
  credible sources se handle karna — conflicts ko source attribution ke sath annotate karna, arbitrarily
  ek value select karne ki bajaye; temporal data — publication/collection dates structured outputs mein
  require karna taaki temporal differences contradictions maan li na jayein
- **Skills:** subagents se structured claim-source mappings (source URLs, doc names, relevant excerpts)
  output karwana jo downstream agents synthesis ke through preserve karein; reports ko explicit
  sections ke sath structure karna jo well-established findings ko contested findings se distinguish
  karein, original source characterizations preserve karte hue; document analysis conflicting values
  ke sath explicitly annotate kar ke complete karna, coordinator ko reconcile-decision dena synthesis
  se pehle; subagents se publication/data-collection dates require karna correct temporal
  interpretation ke liye; synthesis outputs mein content types appropriately render karna — financial
  data tables ki tarah, news prose ki tarah, technical findings structured lists ki tarah

---
[⬅ 00 — Quick Facts](00-quick-facts-and-audience.md) · Next → [02 — Scope, Scoring & Exam Format](02-scope-scoring-and-exam-format.md)
