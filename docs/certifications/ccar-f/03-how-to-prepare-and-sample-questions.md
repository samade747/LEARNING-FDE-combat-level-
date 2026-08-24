# 03 — How to Prepare + 4 Exercises + 12 Sample Questions (Full)

*Source: Official exam guide, section 7 (How to Prepare), section 8 (Preparation Exercises), section 9
(Sample Questions). Sab 12 sample questions PDF se seedha `Read` tool ke zariye nikale gaye — poore
options (A-D) + correct answer + explanation ke sath.*

## How to Prepare (Official Guide, Section 7)

- **Claude Agent SDK se ek agent banao:** poora agentic loop implement karo tool-calling, error
  handling, aur session management ke sath. Subagents spawn karna aur unke beech context pass karna
  practice karo.
- **Real project ke liye Claude Code configure karo:** CLAUDE.md configuration hierarchy set up karo,
  `.claude/rules/` mein path-specific rules banao, `context: fork`/`allowed-tools` frontmatter options ke
  sath custom skills build karo, aur kam se kam ek MCP server integrate karo.
- **MCP tools design + test karo:** tool descriptions likho jo similar tools clearly differentiate karein.
  Error categories + retryable flags ke sath structured error responses implement karo. Ambiguous
  requests ke sath tool-selection reliability test karo.
- **Structured data extraction pipeline banao:** `tool_use` JSON schemas ke sath use karo,
  validation-retry loops implement karo, optional/nullable fields ke sath schemas design karo, aur
  Message Batches API se batch processing practice karo.
- **Prompt engineering techniques practice karo:** ambiguous scenarios ke liye few-shot examples
  likho. False positives kam karne ke liye explicit review criteria define karo. Large code reviews ke
  liye multi-pass review architectures design karo.
- **Context management patterns study karo:** verbose tool outputs se structured facts extract karna
  practice karo, long sessions ke liye scratchpad files implement karna, aur context limits manage
  karne ke liye subagent delegation design karna.
- **Escalation aur human-in-the-loop patterns review karo:** samjho kab escalate karna hai (policy
  gaps, customer requests, progress na ho pana) vs autonomously resolve karna. Confidence-based
  routing ke sath human review workflows design karna practice karo.

## 4 Preparation Exercises (Full Detail)

### Exercise 1 — Multi-Tool Agent with Escalation Logic
**Objective:** Agentic loop design karna practice karna tool integration, structured error handling, aur
escalation patterns ke sath.

**Steps:**
1. 3-4 MCP tools define karo detailed descriptions ke sath jo har tool ka purpose, expected inputs, aur
   boundary conditions clearly differentiate karein. Kam se kam 2 similar-functionality tools include
   karo jinke liye careful description chahiye selection confusion avoid karne ke liye.
2. Ek agentic loop implement karo jo `stop_reason` check kare yeh decide karne ke liye ke tool
   execution continue karni hai ya final response present karni hai. Dono "tool_use" aur "end_turn"
   stop-reasons correctly handle karo.
3. Apne tools mein structured error responses add karo — `errorCategory`
   (transient/validation/permission), `isRetryable` boolean, human-readable descriptions include karo.
   Test karo ke agent har error type appropriately handle karta hai (transient errors retry, business
   errors user ko explain).
4. Ek programmatic hook implement karo jo tool calls intercept kar ke ek business rule enforce kare
   (jaise threshold-amount se upar operations block karna), trigger hone par escalation-workflow par
   redirect karte hue.
5. Multi-concern messages ke sath test karo (jaise multiple issues wale requests) aur verify karo ke
   agent request decompose karta hai, har concern handle karta hai, aur ek unified response synthesize
   karta hai.

**Domains reinforced:** Domain 1 (Agentic Architecture & Orchestration), Domain 2 (Tool Design & MCP
Integration), Domain 5 (Context Management & Reliability)

### Exercise 2 — Configure Claude Code for a Team Development Workflow
**Objective:** CLAUDE.md hierarchies, custom slash commands, path-specific rules, aur MCP server
integration configure karna practice karna ek multi-developer project ke liye.

**Steps:**
1. Ek project-level CLAUDE.md banao universal coding standards + testing conventions ke sath. Verify
   karo ke project-level par rakhe instructions poori team mein consistently apply hote hain.
2. `.claude/rules/` files banao YAML frontmatter glob patterns ke sath different code areas ke liye
   (jaise `paths: ["src/api/**/*"]` API conventions ke liye, `paths: ["**/*.test.*"]` testing conventions ke
   liye). Test karo ke rules sirf matching files edit karte waqt load hote hain.
3. `.claude/skills/` mein ek project-scoped skill banao `context: fork` aur `allowed-tools` restrictions ke
   sath. Verify karo ke skill isolation mein chalti hai main conversation context pollute kiye bina.
4. `.mcp.json` mein ek MCP server configure karo env-var expansion ke sath credentials ke liye. Ek
   personal experimental MCP server `~/.claude.json` mein add karo aur verify karo dono simultaneously
   available hain.
5. Plan mode vs direct execution test karo varying-complexity tasks par — ek single-file bug fix, ek
   multi-file library migration, aur multiple valid implementation approaches wala ek naya feature.
   Observe karo plan mode kab value provide karta hai.

**Domains reinforced:** Domain 3 (Claude Code Configuration & Workflows), Domain 2 (Tool Design &
MCP Integration)

### Exercise 3 — Build a Structured Data Extraction Pipeline
**Objective:** JSON schemas design karna, structured output ke liye `tool_use` use karna,
validation-retry loops implement karna, aur batch-processing strategies design karna practice karna.

**Steps:**
1. Ek extraction tool define karo ek JSON schema ke sath jisme required + optional fields hon, ek
   "other" + detail-string pattern wala enum, aur nullable fields un info ke liye jo source documents
   mein exist nahi kar sakti. Documents process karo jahan kuch fields absent hon aur verify karo ke
   model values fabricate karne ki bajaye null return karta hai.
2. Ek validation-retry loop implement karo: jab Pydantic/JSON-schema validation fail ho, ek follow-up
   request bhejo jisme document, failed extraction, aur specific validation error include ho. Track karo
   kaunse errors retry se resolvable hain (format mismatches) vs kaunse nahi (source mein info hi
   absent hai).
3. Few-shot examples add karo jo varied-format documents se extraction demonstrate karein (jaise
   inline citations vs bibliographies, narrative descriptions vs structured tables) aur verify karo
   structural-variety handling improve hui.
4. Ek batch-processing strategy design karo: Message Batches API se 100 documents ka ek batch
   submit karo, failures `custom_id` se handle karo, failed documents ko modifications ke sath resubmit
   karo (jaise oversized documents chunk karna), aur SLA constraints ke relative total processing time
   calculate karo.
5. Ek human-review routing strategy implement karo: model se field-level confidence scores output
   karwao, low-confidence extractions ko human review route karo, aur document-type/field ke hisaab se
   accuracy analyze karo consistent performance verify karne ke liye.

**Domains reinforced:** Domain 4 (Prompt Engineering & Structured Output), Domain 5 (Context
Management & Reliability)

### Exercise 4 — Design and Debug a Multi-Agent Research Pipeline
**Objective:** Subagents orchestrate karna, context passing manage karna, error propagation implement
karna, aur provenance-tracking ke sath synthesis handle karna practice karna.

**Steps:**
1. Ek coordinator agent banao jo kam se kam 2 subagents ko delegate kare (jaise web search aur
   document analysis). Ensure karo ke coordinator ke `allowedTools` mein "Task" include ho aur har
   subagent apni research findings directly apne prompt mein receive kare, automatic context
   inheritance pe relying kiye bina.
2. Parallel subagent execution implement karo coordinator se ek single response mein multiple `Task`
   tool calls emit karwa ke. Sequential execution ke against latency improvement measure karo.
3. Subagents ke liye structured output design karo jo content ko metadata se separate kare: har finding
   mein claim, evidence excerpt, source URL/doc name, aur publication date include ho. Verify karo ke
   synthesis subagent findings combine karte waqt source attribution preserve karta hai.
4. Error propagation implement karo: ek subagent timeout simulate karo aur verify karo ke coordinator
   structured error context receive karta hai (failure type, attempted query, partial results). Test karo
   ke coordinator partial results ke sath proceed kar sakta hai aur final output ko coverage-gaps ke sath
   annotate karta hai.
5. Conflicting source data ke sath test karo (jaise 2 credible sources different statistics ke sath) aur
   verify karo ke synthesis output dono values source-attribution ke sath preserve karta hai (arbitrarily
   ek select karne ki bajaye), aur report ko well-established vs contested findings distinguish karne ke
   liye structure karta hai.

**Domains reinforced:** Domain 1 (Agentic Architecture & Orchestration), Domain 2 (Tool Design & MCP
Integration), Domain 5 (Context Management & Reliability)

---

## 12 Sample Questions (Full — Official Guide, Section 9)

Yeh questions practice test se liye gaye hain, explanations ke sath — format aur difficulty level
illustrate karte hain.

### Scenario: Customer Support Resolution Agent (Q1-Q3)

**Q1.** Production data batata hai ke 12% cases mein aapka agent `get_customer` poori tarah skip kar
deta hai aur `lookup_order` ko sirf customer ke stated naam se call karta hai, kabhi-kabhi
misidentified accounts aur galat refunds tak le jata hai. Kaunsa change is reliability issue ko sab se
effectively address karega?

A. Ek programmatic prerequisite add karo jo `lookup_order` aur `process_refund` calls ko block kare jab
tak `get_customer` ek verified customer ID return na kare.
B. System prompt enhance karo yeh state karne ke liye ke `get_customer` se verification mandatory hai
kisi bhi order operation se pehle.
C. Few-shot examples add karo jo dikhayein agent hamesha `get_customer` pehle call kare, chahe
customer khud order details volunteer kare.
D. Ek routing classifier implement karo jo har request analyze kare aur sirf uss request-type ke liye
appropriate tools ka subset enable kare.

**Sahi jawab: A.** Jab critical business logic ke liye specific tool sequence zaroori ho (jaise refunds
process karne se pehle customer identity verify karna), programmatic enforcement deterministic
guarantees deta hai jo prompt-based approaches nahi de sakte. B aur C probabilistic LLM compliance pe
rely karte hain, jo financial consequences hone par insufficient hai. D tool-ordering ki bajaye
tool-availability address karta hai, jo actual problem nahi hai.

**Q2.** Production logs dikhate hain ke agent frequently `get_customer` call karta hai jab users orders
ke baare mein poochte hain (jaise "check my order #12345"), `lookup_order` ki bajaye. Dono tools ke
descriptions minimal hain ("Retrieves customer information" / "Retrieves order details") aur similar
identifier formats accept karte hain. Tool-selection reliability improve karne ka sab se effective pehla
step kya hai?

A. System prompt mein few-shot examples add karo jo correct tool-selection patterns demonstrate
karein, 5-8 examples ke sath jo order-related queries ko `lookup_order` par route karein.
B. Har tool ki description expand karo — input formats, example queries, edge cases, aur boundaries
include karo jo similar tools ke against use-kab-karna explain karein.
C. Ek routing layer implement karo jo har turn se pehle user input parse kare aur detected
keywords/identifier patterns ke basis par appropriate tool pre-select kare.
D. Dono tools ko ek single `lookup_entity` tool mein consolidate karo jo koi bhi identifier accept kare
aur internally decide kare kaunsa backend query karna hai.

**Sahi jawab: B.** Tool descriptions LLMs ka primary tool-selection mechanism hain. Jab descriptions
minimal hon, models similar tools differentiate karne ke liye context nahi rakhte. B is root cause ko
directly address karta hai low-effort, high-leverage fix ke sath. Few-shot examples (A) token overhead
add karte hain underlying issue fix kiye bina. Routing layer (C) over-engineered hai aur LLM ki natural
language understanding bypass karta hai. Tools consolidate karna (D) valid architectural choice hai
lekin "first step" se zyada effort chahiye jab immediate problem inadequate descriptions hai.

**Q3.** Aapka agent 55% first-contact resolution achieve karta hai, 80% target se kaafi kam. Logs
dikhate hain ke yeh straightforward cases escalate karta hai (photo-evidence ke sath standard damage
replacements) jabke complex situations autonomously handle karne ki koshish karta hai jinhe policy
exceptions chahiye. Escalation calibration improve karne ka sab se effective tareeqa kya hai?

A. System prompt mein explicit escalation criteria few-shot examples ke sath add karo jo dikhayein kab
escalate karna hai vs autonomously resolve karna hai.
B. Agent se har response se pehle ek confidence score (1-10) self-report karwao aur requests ko humans
ke paas automatically route karo jab confidence threshold se neeche gire.
C. Historical tickets par trained ek separate classifier model deploy karo yeh predict karne ke liye ke
kaunse requests ko escalation chahiye main agent processing shuru karne se pehle.
D. Sentiment analysis implement karo customer frustration levels detect karne ke liye aur automatically
escalate karo jab negative sentiment threshold se zyada ho.

**Sahi jawab: A.** Explicit escalation criteria few-shot examples ke sath add karna root cause ko
directly address karta hai: unclear decision boundaries. Yeh infrastructure add karne se pehle
proportionate first response hai. B fail hota hai kyunki LLM self-reported confidence poorly calibrated
hota hai — agent already hard cases par incorrectly confident hai. C over-engineered hai, labeled data
+ ML infrastructure chahiye jab prompt optimization try hi nahi hui. D ek bilkul alag problem solve
karta hai; sentiment case-complexity se correlate nahi karta, jo actual issue hai.

### Scenario: Code Generation with Claude Code (Q4-Q6)

**Q4.** Aap ek custom `/review` slash command banana chahte ho jo aapki team ka standard code-review
checklist chalaye. Yeh command har developer ko available honi chahiye jab wo repository clone/pull
karein. Yeh command file kahan banani chahiye?

A. Project repository mein `.claude/commands/` directory mein
B. Har developer ke home directory mein `~/.claude/commands/` mein
C. Project root ki CLAUDE.md file mein
D. Ek `.claude/config.json` file mein commands array ke sath

**Sahi jawab: A.** Project-scoped custom slash commands `.claude/commands/` directory mein store hone
chahiye repository ke andar. Yeh commands version-controlled hote hain aur automatically sab
developers ko available hote hain clone/pull par. B (`~/.claude/commands/`) personal commands ke liye
hai jo version control se share nahi hote. C (CLAUDE.md) project instructions/context ke liye hai,
command definitions ke liye nahi. D ek configuration mechanism describe karta hai jo Claude Code mein
exist hi nahi karta.

**Q5.** Aapko assign hua hai team ki monolithic application ko microservices mein restructure karna.
Isme dozens files ke across changes honge aur service-boundaries + module-dependencies ke baare mein
decisions chahiye honge. Kaunsa approach lena chahiye?

A. Plan mode mein enter karo codebase explore karne ke liye, dependencies samajhne ke liye, aur
changes se pehle ek implementation approach design karne ke liye.
B. Direct execution se shuru karo aur incrementally changes karo, implementation ko natural service
boundaries reveal karne do.
C. Direct execution use karo comprehensive upfront instructions ke sath jo detail mein bataye har
service kaise structure hona chahiye.
D. Direct execution mode mein shuru karo aur sirf plan mode par switch karo agar implementation ke
dauran unexpected complexity encounter ho.

**Sahi jawab: A.** Plan mode complex tasks ke liye designed hai jinme large-scale changes, multiple
valid approaches, aur architectural decisions shamil hon — bilkul jaisa monolith-to-microservices
restructuring chahta hai. Yeh safe codebase exploration aur design enable karta hai changes commit
karne se pehle. B mein dependencies late discover hone par costly rework ka risk hai. C assume karta
hai ke aap already sahi structure jaante ho code explore kiye bina. D ignore karta hai ke complexity
already requirements mein stated hai, koi baad mein emerge hone wali cheez nahi.

**Q6.** Aapke codebase mein alag-alag areas ke different coding conventions hain: React components
functional style hooks ke sath, API handlers async/await specific error-handling ke sath, database
models repository pattern follow karte hain. Test files poore codebase mein spread hain unke code ke
saath (jaise `Button.test.tsx` `Button.tsx` ke paas), aur aap chahte ho sab tests location se independent
same conventions follow karein. Claude ko automatically correct conventions apply karwane ka sab se
maintainable tareeqa kya hai?

A. `.claude/rules/` mein rule files banao YAML frontmatter ke sath jo glob patterns specify karein file
paths ke basis par conventions conditionally apply karne ke liye
B. Sab conventions root CLAUDE.md file mein consolidate karo har area ke headers ke andar, Claude par
rely karte hue ke kaunsa section apply hota hai infer kare
C. `.claude/skills/` mein har code-type ke liye skills banao jinke `SKILL.md` files relevant conventions
include karein
D. Har subdirectory mein alag CLAUDE.md file rakho us area ki specific conventions ke sath

**Sahi jawab: A.** `.claude/rules/` glob patterns (jaise `**/*.test.tsx`) ke sath conventions ko file paths
ke basis automatically apply karne deta hai directory location se independent — test files ke poore
codebase mein spread hone ke liye essential. B inference pe rely karta hai explicit matching ki bajaye,
isliye unreliable hai. C manual skill invocation chahta hai ya Claude ke choose karne pe depend karta
hai, jo "automatic" application ki deterministic zaroorat se contradict karta hai. D kai directories mein
spread files handle nahi kar sakta kyunki CLAUDE.md files directory-bound hoti hain.

### Scenario: Multi-Agent Research System (Q7-Q9)

**Q7.** Topic "impact of AI on creative industries" par system chalane ke baad, aap observe karte ho ke
har subagent successfully complete hota hai: web-search agent relevant articles dhoondta hai,
document-analysis agent papers correctly summarize karta hai, aur synthesis agent coherent output
produce karta hai. Lekin final reports sirf visual arts cover karte hain — music, writing, aur film
production poori tarah miss ho jate hain. Coordinator ke logs check karne par, aap dekhte ho isne topic
ko 3 subtasks mein decompose kiya: "AI in digital art creation," "AI in graphic design," aur "AI in
photography." Sab se likely root cause kya hai?

A. Synthesis agent ke paas doosre agents se receive hui findings mein coverage-gaps identify karne ke
liye instructions ki kami hai.
B. Coordinator agent ki task decomposition bohat narrow hai, jiski wajah se subagent assignments topic
ke sab relevant domains cover nahi karte.
C. Web-search agent ki queries kaafi comprehensive nahi hain aur inhe more creative-industry sectors
cover karne ke liye expand karna chahiye.
D. Document-analysis agent overly-restrictive relevance criteria ki wajah se non-visual creative
industries se related sources filter kar raha hai.

**Sahi jawab: B.** Coordinator ke logs directly root cause reveal karte hain: usne "creative industries"
ko sirf visual-arts subtasks (digital art, graphic design, photography) mein decompose kiya, music,
writing, aur film poori tarah omit kar diye. Subagents ne apne assigned tasks correctly execute kiye —
problem yeh hai ke unhe kya assign hua tha. A, C, aur D incorrectly downstream agents ko blame karte
hain jo apne assigned scope ke andar correctly kaam kar rahe hain.

**Q8.** Web-search subagent ek complex topic research karte waqt timeout ho jata hai. Aapko design
karna hai ke yeh failure information coordinator agent tak kaise flow kare. Kaunsa error-propagation
approach intelligent recovery sab se accha enable karta hai?

A. Coordinator ko structured error context return karo jisme failure type, attempted query, koi bhi
partial results, aur potential alternative approaches include hon.
B. Subagent ke andar exponential-backoff ke sath automatic retry logic implement karo, generic "search
unavailable" status sirf tab return karo jab sab retries exhaust ho jayein.
C. Timeout ko subagent ke andar catch karo aur ek empty result set successful mark kar ke return karo.
D. Timeout exception ko directly ek top-level handler tak propagate karo jo poora research workflow
terminate kar de.

**Sahi jawab: A.** Structured error context coordinator ko wo information deta hai jo usay intelligent
recovery decisions lene ke liye chahiye — retry modified query se karna hai, alternative approach try
karna hai, ya partial results ke sath proceed karna hai. B ka generic status coordinator se valuable
context chupa deta hai, informed decisions rokte hue. C failure ko success mark kar ke error suppress
karta hai, jo recovery rok deta hai aur incomplete research outputs ka risk banata hai. D poora workflow
unnecessarily terminate kar deta hai jab recovery strategies succeed ho sakti thin.

**Q9.** Testing ke dauran, aap observe karte ho ke synthesis agent ko frequently specific claims verify
karne ki zaroorat parti hai findings combine karte waqt. Currently, jab verification chahiye hoti hai,
synthesis agent control coordinator ko wapas deta hai, jo web-search agent invoke karta hai, phir
results ke sath synthesis re-invoke karta hai. Yeh per-task 2-3 round trips add karta hai aur latency 40%
badha deta hai. Aapka evaluation dikhata hai ke 85% verifications simple fact-checks hain (dates,
names, statistics) jabke 15% ko deeper investigation chahiye. Overhead kam karne aur reliability
maintain karne ka sab se effective approach kya hai?

A. Synthesis agent ko simple lookups ke liye ek scoped `verify_fact` tool do, jabke complex
verifications coordinator ke through web-search agent ko delegate hoti rahein.
B. Synthesis agent se sab verification needs accumulate karwao aur unhe apne pass ke end mein
coordinator ko batch ki tarah return karwao, jo phir unhe web-search agent ko ek saath bhej de.
C. Synthesis agent ko sab web-search tools tak access do taaki wo koi bhi verification need directly
handle kar sake coordinator ke through round-trips ke bina.
D. Web-search agent se initial research ke dauran har source ke around proactively extra context cache
karwao, anticipate karte hue synthesis agent ko kya verify karna pare ga.

**Sahi jawab: A.** A least-privilege ka principle apply karta hai synthesis agent ko sirf 85% common
case (simple fact verification) ke liye zaroori cheez dete hue, jabke complex cases ke liye existing
coordination pattern preserve karte hue. B ka batching approach blocking dependencies banata hai
kyunki synthesis steps earlier-verified facts par depend kar sakte hain. C synthesis agent ko
over-provision karta hai, separation-of-concerns violate karte hue. D speculative caching pe rely karta
hai jo reliably predict nahi kar sakta synthesis agent ko kya verify karna parega.

### Scenario: Claude Code for Continuous Integration (Q10-Q12)

**Q10.** Aapka pipeline script `claude "Analyze this pull request for security issues"` chalata hai lekin
job indefinitely hang ho jaati hai. Logs indicate karte hain ke Claude Code interactive input ka wait kar
raha hai. Automated pipeline mein Claude Code chalane ka sahi approach kya hai?

A. `-p` flag add karo: `claude -p "Analyze this pull request for security issues"`
B. Command chalane se pehle environment variable `CLAUDE_HEADLESS=true` set karo
C. stdin ko `/dev/null` se redirect karo: `claude "Analyze this pull request for security issues" < /dev/null`
D. `--batch` flag add karo: `claude --batch "Analyze this pull request for security issues"`

**Sahi jawab: A.** `-p` (ya `--print`) flag Claude Code ko non-interactive mode mein chalane ka documented
tareeqa hai. Yeh prompt process karta hai, result stdout par output karta hai, aur bina user input wait
kiye exit ho jata hai — bilkul jo CI/CD pipelines chahte hain. Baaqi options non-existent features
(`CLAUDE_HEADLESS` env variable, `--batch` flag) reference karte hain ya Unix workarounds use karte
hain jo Claude Code ki command syntax ko properly address nahi karte.

**Q11.** Aapki team automated-analysis ke liye API costs kam karna chahti hai. Currently, real-time
Claude calls 2 workflows power karte hain: (1) ek blocking pre-merge check jo developers merge karne
se pehle complete hona zaroori hai, aur (2) ek technical-debt report jo overnight generate hoti hai
agli subah review ke liye. Aapke manager ne propose kiya hai dono ko Message Batches API par switch
karna 50% cost-savings ke liye. Yeh proposal kaise evaluate karni chahiye?

A. Batch processing sirf technical-debt reports ke liye use karo; pre-merge checks ke liye real-time
calls rakho.
B. Dono workflows ko batch processing par switch karo status polling ke sath completion check karne ke
liye.
C. Dono workflows ke liye real-time calls rakho batch result-ordering issues avoid karne ke liye.
D. Dono ko batch processing par switch karo ek timeout fallback ke sath real-time par jane ke liye agar
batches zyada waqt lein.

**Sahi jawab: A.** Message Batches API 50% cost savings offer karta hai lekin processing times 24-hour
tak ja sakti hain koi guaranteed latency SLA ke bina. Yeh blocking pre-merge checks ke liye unsuitable
banata hai jahan developers results ka wait karte hain, lekin overnight batch jobs (jaise technical-debt
reports) ke liye ideal hai. B galat hai kyunki "often faster" completion pe rely karna blocking workflows
ke liye acceptable nahi hai. C ek misconception reflect karta hai — batch results `custom_id` fields se
correlate kiye ja sakte hain. D unnecessary complexity add karta hai jab simpler solution har API ko
uske appropriate use-case se match karna hai.

**Q12.** Ek pull request stock-tracking module ke 14 files modify karta hai. Aapka single-pass review jo
sab files ek saath analyze karta hai inconsistent results deta hai: kuch files ke liye detailed feedback
lekin doosron ke liye superficial comments, obvious bugs miss ho jate hain, aur contradictory feedback
milta hai — ek file mein ek pattern ko problematic flag karna jabke same PR ki doosri file mein identical
code approve karna. Review kaise restructure karni chahiye?

A. Focused passes mein split karo: har file individually local issues ke liye analyze karo, phir ek
separate integration-focused pass cross-file data-flow examine karne ke liye chalao.
B. Developers se require karo ke automated review chalne se pehle large PRs ko 3-4 files ke chhote
submissions mein split karein.
C. Ek higher-tier model par switch karo bare context window ke sath taaki sab 14 files ek pass mein
adequate attention paayein.
D. Poori PR par 3 independent review passes chalao aur sirf wahi issues flag karo jo kam se kam 2 mein
se 3 runs mein appear hon.

**Sahi jawab: A.** Reviews ko focused passes mein split karna directly root cause address karta hai:
attention dilution jab bohat files ek saath process ho rahi hon. File-by-file analysis consistent depth
ensure karta hai, jabke separate integration pass cross-file issues catch karta hai. B burden developers
par shift karta hai system improve kiye bina. C misunderstand karta hai ke larger context windows
attention-quality issues solve nahi karte. D actually real bugs ki detection suppress kar dega consensus
require karke un issues par jo sirf intermittently catch ho sakte hain.

---
[⬅ 02 — Scope, Scoring & Exam Format](02-scope-scoring-and-exam-format.md) · Next → [04 — Policies, Resources & Doc Control](04-policies-resources-and-doc-control.md)
