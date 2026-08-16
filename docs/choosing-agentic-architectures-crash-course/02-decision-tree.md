# 02 — Part 2: The Five-Question Decision Tree (Concepts 4-8 + Bridges 8.5, 8.6)

| # | Sawal | Kya Test Karta Hai | Kahan Route Karta Hai |
| --- | --- | --- | --- |
| **Q1** | Solution path pehle se define ho sakta hai? | Process runtime se pehle specify ho sakta hai? | Yes → Q2; No → Q3 |
| **Q2** | Workflow fixed aur stable hai runs ke across? | Same steps har baar apply hote hain? | Yes → **Sequential Workflow**; No → adaptive patterns dekho |
| **Q3** | Task structure execution se pehle articulable hai? | Major stages/dependencies clear hain? | Yes → **Planning + ReAct**; No → **Single Agent + ReAct + Tools** |
| **Q4** | Quality speed se zyada matter karti hai, checkable criteria ke sath? | Extra critique/refinement passes latency/cost worth hain? | Yes → **Reflection layer** add karo; No → skip |
| **Q5** | Specialization, context, ya scale bottleneck hai? | Ek agent expertise/context/parallel capacity ki kami rakhta hai? | Yes → **Multi-Agent Specialist System**; No → single agent rakho |

*Q1-Q3 core pattern decide karte hain. Q4-Q5 additive layers hain — kisi bhi core par apply ho sakte
hain, lekin sirf tab jab unke assumptions hold karein.*

## Concept 4 — Q1: Kya Solution Path Pehle Se Define Ho Sakta Hai?

Yeh sabse important sawal hai — decide karta hai kya aapko agentic system chahiye bhi ya nahi.

**"Solution path" ka matlab:** agar aap mujhe input batao, kya main aapko exact sequence of steps
bata sakta hoon jo output produce kare? Invoice intake: email receive → fields extract → database
validate → store → notify. 5 steps, har baar wahi 5 steps. **Yeh known solution path hai.**

Contrast: customer poochta hai "November 12 ko mujhe double charge kyun hua?" — path depend karta hai
kya milta hai. Transaction history dekho aur mil jaye. 2 charges alag merchants se hon to "fraud tha?"
pivot karo. Same merchant, alag timestamps ho to "retry tha?" pivot karo. **Yeh unknown solution path
hai — path emerge karta hai investigation se.**

**3 tests, order mein:**
1. **Kya aap input dekhne se pehle steps ka flowchart likh sakte ho?** Agar flowchart mein "ab agent
   decide karta hai" boxes chahiye, path unknown hai
2. **Kya steps kai runs mein unchanged repeat hote hain?**
3. **Jab input badle, kya steps badalte hain?**

**Sabse common galti:** path ko known **believe** karna kyunki task description structured lagti hai.
"Refund requests process karo" known lagta hai, lekin real refund requests mein dispute investigation,
policy lookup, escalation, multiple charges disambiguation sab shamil hote hain — actual path adaptive
hai.

**Mirror error:** path ko unknown believe karna kyunki description open-ended lagti hai. "Aaj raat city
mein achha restaurant dhoondo" adaptive lagta hai, lekin agar implementation "parse → filter query →
top 5 return" hai, path known hai.

**Heuristic:** *"Agar mujhe yeh Python function ki tarah likhna pare bina LLM calls ke, kya mujhe pata
hoga kaise structure karoon?"* Haan to path probably known hai; nahi to unknown.

## Concept 5 — Q2: Kya Workflow Fixed Aur Stable Hai Runs Ke Across?

Q1 ka jawab "haan, path known hai" tha. Q2 doosra check hai: kya **fixed aur stable** hai expected
inputs ke across? **"Known" aur "stable" same nahi hain.**

Distinction: path **principle mein known** ho sakta hai lekin **practice mein vary** kare. "Research
assistant" agent — kabhi quick answer chahiye (ek fact lookup), kabhi multi-source synthesis, kabhi
document analysis. Har case ka path likha ja sakta hai, lekin path input type ke sath vary karta hai —
**known-but-variable, known-and-stable nahi.**

**Test:** representative sample of real inputs dekho. Step sequence same rehta hai?
- Har input same steps se guzre → workflow stable hai → **Sequential Workflow** banao
- Alag inputs alag step sequences maangte hain → variable hai → (a) explicit branching wala workflow,
  ya (b) agentic pattern jo path ko adapt kare

**Sabse common galti:** "known on average" ko "known and stable" treat karna. 80% case fixed workflow
hai, 20% deviation maangta hai. Engineers 80% ke liye workflow banate hain aur 20% ke liye ad-hoc
patches add karte hain — eventually patches original workflow par haavi ho jate hain.

**Route:** fixed/stable → **Sequential Workflow**, yahan ruko. Known-but-variable → variants kam ho
to branched workflow, zyada/evolving ho to Q3 par agentic pattern ki taraf jao.

## Concept 6 — Q3: Kya Task Structure Execution Se Pehle Articulable Hai?

Q1 "path unknown hai" — agentic reasoning chahiye. Q3 poochta hai: kya work ka **high-level structure**
pehle se articulate ho sakta hai, chahe specific steps na hon?

**"Structure" yahan:** steps nahi (woh unknown hain), balke **stages** aur unki dependencies. Market
research agent: sources/competitors/analyses pata nahi (Q1=no), lekin structure articulate ho sakta
hai: gather → analyze → synthesize → report. 4 stages, clear order. **Articulable structure.**

Contrast: customer-support agent "mujhe ek issue hai" handle karta hai — investigation jo complete
hone tak chalti hai, ek lookup ho sakta hai ya paanch. **Structure articulable nahi.**

**Test:** kaam ko phase diagram ki tarah draw karne ki koshish karo, koi specific input dekhne se
pehle. Major phases label kar sakte ho?
- Haan (gather → analyze → synthesize; design → implement → test) → **Planning + ReAct Execution**
- Nahi (investigation, iteration, open-ended exploration) → **Single Agent + ReAct + Tools**

**Sabse common galti:** structure invent karna jahan koi nahi hai — engineers feel karte hain plan
hamesha possible hona chahiye, force kar dete hain. Planner plan generate karta hai; execution turant
diverge ho jati hai. **Ulta error:** pure ReAct use karna jahan genuinely phases the.

**Heuristic:** planning tab madad karti hai jab work ki **shape** predictable ho lekin **content**
nahi. ReAct akela sahi hai jab **shape** bhi discover karni pare.

> **Q2 vs Q3 confusion:** Q2 poochta hai kya **steps khud** fixed hain runs ke across. Q3 poochta hai
> kya **major stages** articulable hain, chahe step-level kaam vary kare. Conflation jo bite karta hai:
> engineers task mein structure dekhte hain ("clearly stages hain: research, analyze, write") aur Q2
> ko YES answer kar dete hain. Lekin "structure exist karta hai" Q3 ka sawal hai, Q2 ka nahi. Agar agent
> ko har stage ke andar decisions leni parti hain, Q2 = NO hai aur aap Q3 par hone chahiye.

## Concept 7 — Q4: Kya Quality Speed Se Zyada Matter Karti Hai, Checkable Criteria Ke Sath?

Q4 pehla **additive layer** sawal hai. Core pattern (Q1-Q3) already chun liya. Q4 poochta hai kya
**reflection** upar layer karni hai.

**2 conditions, dono hold karni chahiye:**
1. **Quality speed se zyada matter karti hai.** Reflection kam az kam ek extra LLM call add karti hai
   (critique), usually 2 (critique + refinement). Interactive use cases (real-time support) ke liye
   yeh cost prohibitive hai. Batch use cases (reports, code) ke liye acceptable hai
2. **Evaluation criteria explicit aur checkable hain.** Vague criteria vague critiques produce karte
   hain. "Yeh acha hai confirm karo" criterion nahi hai. "SQL parse hoti hai, sirf listed tables hit
   karti hai" hai

**Test:** *response 3-5x lambi le to users okay hain, meaningful quality improvement ke sath?* Aur:
*"good output" ka matlab 5-10 specific bullets mein likh sakte ho, jo doosra LLM check kar sake?* Dono
YES ho to reflection value add karti hai.

**Sabse common galti:** critic aur generator same model/prompt style use karna — same blind spots
share karte hain, isliye rubber-stamp karte hain. Effective reflection: (a) critic ke liye alag model,
(b) critic ko fundamentally different perspective ("strict reviewer" vs generator ka "helpful" framing),
(c) explicit checking tools (SQL run karo, JSON parse karo).

**Route:** dono conditions hold karein to reflection ko core pattern ke upar **layer** karo — replace
nahi karta. Ek condition fail ho to skip karo; genuinely quality assurance chahiye lekin criteria
checkable nahi to **human review** sahi fix hai, LLM reflection nahi.

## Concept 8 — Q5: Kya Specialization, Context, Ya Scale Bottleneck Hai?

Dusra additive layer sawal, sabse consequential — multi-agent systems banane mein sabse mehnga hain
aur hatane mein bhi.

**3 alag claims jo aksar confuse hoti hain:**
1. **Specialization claim** — task ko distinct expertise chahiye jo ek agent ek prompt mein achi
   tarah na rakh sake
2. **Context claim** — task ko itna context chahiye jo ek agent effectively use na kar sake
3. **Scale claim** — kaam parallel chal sakta hai, multi-agent system single sequential agent se
   fast execute kar sakta hai

**Specialization claim sabse zyada bina evidence believe hoti hai.** Engineers "feature banao" jaisa
task dekh kar roles mein decompose karte hain (architect, coder, tester, reviewer) kyunki intuitive
lagta hai — intuition utna hi galat jitna sahi hota hai.

**Quantitative triggers (judgment ko measurement se replace karo):**

| Bottleneck Claim | Quantitative Trigger |
| --- | --- |
| Specialization | Single-agent traces mein tool-routing errors specific domain mein concentrated (~1/3 affected category runs) |
| Context overflow | Holdout accuracy materially degrade ho context barhne se (~10 points drop 15K→45K tokens) |
| Scale (parallelizable) | 5+ independent sub-tasks per run AND single-agent latency user budget se >2x zyada |
| Scale (throughput) | Run volume single-agent rate-limit ceiling se 10x zyada |

**Evidence hierarchy, strongest se weakest:** production trace data (best) → holdout-set measurements
(strong) → domain analysis with written specs (acceptable) → "feels like specialists" (insufficient —
yahin pattern-overshoot rehta hai).

**Self-check:** *"Sabse chota single-agent design kya hai jo hum pehle ship kar sakte, aur kaunsi
specific failure hume baad mein multi-agent force karegi?"* **Multi-agent rarely galat endpoint hai;
almost hamesha galat starting point hai.**

## Bridge 8.5 — OpenAI Agents SDK Primitives: Har Pattern Kya Use Karta Hai

**5 primitives jo pattern selection ke liye matter karte hain:**

| Primitive | Kya Hai | Kaunse Patterns Use Karte Hain |
| --- | --- | --- |
| `Agent` | Core class: instructions, tools, output_type, handoffs | Sab 5 patterns |
| `Runner.run(agent, input)` | Agent loop chalata hai, hand-rolled loop nahi chahiye | Single agent + ReAct, Planning + ReAct, Multi-agent |
| `@function_tool` | Python function ko tool banata hai | ReAct, Planning + ReAct, Multi-agent, Sequential (LLM-step ke liye) |
| `handoff(target_agent)` | Ek agent doosre ko conversation handover karta hai, context preserve | Multi-agent (primary), Planning (planner-to-executor) |
| `output_guardrail`/`input_guardrail` | Validation/critique pass primitive | Reflection (primary) |

`Agent.as_tool()` bhi important hai — Agent ko callable tool banata hai jo doosra Agent invoke kar
sake. `as_tool()` matlab **coordinator control mein rehta hai**; `handoff()` matlab **specialist
conversation le leta hai**. Yeh distinction architecturally important hai, primitive naam incidental.

Maya ka Tier-1 Support agent `Agent` + `@function_tool` + `Runner.run()` use karta hai — yeh **single
agent + ReAct + tools** pattern hai, exactly Concept 10 wala.

## Bridge 8.6 — Operational Envelope (Inngest) Per Pattern

> Yeh concept pattern choice ke **operational consequences** ke baare mein hai, Inngest sikhane ke
> baare mein nahi. Argument kisi bhi durable-execution platform (Temporal, Restate, Dapr) tak
> generalize hota hai.

Bridge 8.5 ne patterns ko **engine** primitives (SDK) se map kiya. Bridge 8.6 unhe **operational
envelope** primitives se map karta hai — runtime machinery jo agent loop ko failures survive karwati
hai, many concurrent users tak scale karti hai. **SDK loop chalata hai; envelope usay production-grade
banata hai.**

| Primitive | Kya Hai | Kaunse Patterns Sabse Zyada |
| --- | --- | --- |
| `@inngest_client.create_function` | Durable-execution runtime mein function register karta hai | Sab 5 |
| `TriggerEvent`, `TriggerCron` | Trigger surfaces | Sab 5 |
| `ctx.step.run(name, fn)` | Durable checkpoint, memoized retry | Sequential (direct map), Planning (per-stage), Reflection |
| `ctx.step.wait_for_event(...)` | Durable suspend, HITL primitive | HITL, multi-agent handoffs, human-critic reflection |
| `concurrency`, `throttle`, `priority` | Per-function flow control | Multi-agent (critical), high-volume single-agent |
| Fan-out triggers | 1 event → N subscriber functions | Multi-agent (parallel), Planning (parallel stages) |
| Replay + dead-letter | Fix ship karo, replay click karo | Sab patterns, elaborate pattern jitni zyada matter karta hai |

**2 production failure modes jo architecture-diagram level par visible nahi hoti:**
1. **Crash mid-flight** — 6-step planning+ReAct run jo step 4 par crash ho (durable execution ke bina)
   pehle 3 steps ke liye dubara pay karta hai. GPT-5-class pricing par, crashed run ~$0.10-$2.00 waste
   kar sakti hai; 1000 runs/din par $30-$600/month sirf crashes se
2. **Coordination at scale** — 5 specialists, 10 tenants, bursts 100 events/minute rate limits khatam
   kar denge bina per-specialist concurrency caps ke

**3 layers side-by-side:** operational envelope (Inngest) engine (SDK) ko wrap karta hai, dono cloud
deployment ke andar chalte hain. World triggers upar fire karti hai (customer emails, webhooks, cron,
fan-out events, human approvals); trigger 3 layers se neeche flow karte hain.

---
[⬅ Pattern Selection Problem](01-pattern-selection-problem.md) · [⬆ Index](README.md) · [Agla: 5 Patterns In Depth ➡](03-five-patterns.md)
