# 07 — The Named Engines Compared, Reference Implementation, The Workforce Opportunity

## The Named Engines, Compared

Chaaron mutually-exclusive nahi. Ek serious Agent Factory shayad chaaron use kare — alag Workers ke
liye alag engines, jaisa Invariant 4 ijazat deta hai. Yeh competing products nahi — yeh alag theories
hain ke agent kahan khatam hota hai aur infrastructure kahan shuru hota hai.

| Dimension | OpenAI Agents SDK | Claude Managed Agents | Dapr Agents | Cursor SDK |
| --- | --- | --- | --- | --- |
| **Primary axis** | Model-native harness | Fully managed runtime | Durable distributed agents | Harness-first cloud agent platform |
| **Compute plane** | BYO sandbox; 7 partner integrations | Anthropic-hosted | Aapka Kubernetes cluster | Cursor Cloud VMs (ya local) |
| **Vendor lock-in** | High (harness OpenAI models ke liye tuned) | Total (harness, runtime, model sab) | None (Apache 2.0, CNCF) | High harness par; model-agnostic neeche |
| **Languages** | Python; TypeScript in progress | Koi bhi (HTTP/SDK) | Python; baaki TBD | TypeScript (`npm install @cursor/sdk`) |
| **Durability model** | Sandbox snapshot aur rehydrate | Server-side session persistence | Dapr Workflow checkpointing | Cloud VM persistence per task |
| **Multi-agent** | Handoffs, subagents | Research preview | Deterministic workflows + pub/sub | Parallel cloud agents, subagents, artifact handoff |

## Picking Your Engine

Invariant 4 kehta hai har Worker apna engine chunta hai. Practice mein, do axes choice drive karte hain:
failure kitna bura hai, aur infrastructure kaun chalata hai.

| Job Profile | Engine | Kyun |
| --- | --- | --- |
| **Fail nahi ho sakta** | Dapr Agents wrapping an SDK | Durable execution, auto-recovery, poori observability |
| **Fail nahi hona chahiye, operate nahi karna chahte** | Claude Managed Agents | Hosted aur operated aapke liye |
| **Fail nahi hona chahiye, portability chahiye** | OpenAI Agents SDK | Production-grade, self-hosted, vendor-flexible |
| **Kaam kar jaye to acha** | OpenClaw-native | Lightweight, deploy karne mein tez, routine tasks ke liye acha |
| **Engineering fleet, parallel cloud agents** | Cursor SDK | Parallel coding agents ke liye purpose-built harness, model-agnostic, Cursor ki apni engineering par proven |
| **Pehle se ek hai** | Koi bhi Paperclip-compatible runtime | Jo hai wahi plug karo |

*Harness aur compute par ek baat.* Har engine ke do planes hain. **Harness** control plane hai — agent
loop, model calls, tool routing, approvals, tracing, recovery. **Compute** execution plane hai — sandbox
jahan model-directed code files padhta hai, commands chalata hai, artifacts likhta hai. Kuch engines
dono fuse kar dete hain: Claude Managed Agents dono ko ek API ke peeche bundle karta hai. Kuch harness
ship karte hain aur aapko apna compute laane dete hain: OpenAI Agents SDK E2B, Cloudflare, Daytona,
Modal, Runloop, Vercel, aur Blaxel se integrate karta hai — ya koi bhi container jo aap ship karo. Kuch
compute plane ko Kubernetes maan lete hain: Dapr Agents. Split matter karta hai: credentials harness mein
rehte hain jabke untrusted, model-generated code sandbox mein rehta hai — aur compute plane ko agent
rewrite kiye bina swap kiya ja sakta hai.

Triggers ek orthogonal choice hain. Koi bhi engine Worker chalaye, Claude Code Routines aur Inngest usay
schedule, webhook, ya inbound API call se fire kar sakte hain — koi rewiring nahi chahiye.

Sandboxes bhi orthogonal hain. Koi bhi engine Worker chalaye, compute plane swap ho sakta hai — E2B,
Cloudflare, Daytona, Modal, apna Kubernetes — bina agent rewrite kiye.

Engines batate hain Workers kaise chalte hain. Woh jis ke against chalte hain — company ki authoritative
state — Invariant 5 ka subject hai.

## The Reference Implementation in 2026

Is section mein named products woh hain jo hum ship karte hain. Thesis inhein require nahi karti. Jab
behtar implementations aayenge, yeh subsection badalti hai. Upar wale invariants nahi badalte.

- **Delegate** — [OpenClaw](https://github.com/openclaw/openclaw)
- **Management layer** — [Paperclip](https://github.com/paperclipai/paperclip) (poori workforce
  lifecycle — hire, assign, govern, observe, retire — callable APIs ki tarah expose karta hai)
- **Engines** — Dapr Agents, Claude Managed Agents, OpenAI Agents SDK, Cursor SDK, OpenClaw-native.
  Engines increasingly durability native taur par absorb kar rahe hain — Dapr Agents workflow
  checkpointing se, Claude Managed Agents server-side sessions se, OpenAI Agents SDK stateful workflows
  se, Cursor SDK cloud-VM persistence per task se. Thesis isay engine-internal evolution maanti hai,
  alag invariant nahi.
- **Skills** — Agent Skills format (agentskills.io), SKILL.md + optional scripts/references/assets ke
  sath, progressive disclosure se load hote hain.
- **Nervous system** — Inngest workforce ke event substrate ki tarah: external triggers (schedules,
  webhooks, inbound API calls), internal events (Worker-to-Worker handoff), durable execution (step
  memoization, retry, replay), aur flow control (concurrency, throttling, batching) — sab ek operational
  envelope ke tehat. Claude Code Routines coding-agent automation ke liye specialist trigger ki tarah —
  jab code-related events hon to Claude Code fire karta hai. Dono saath rehte hain: Inngest workforce ko
  front karta hai, Routines coding agent ko.

Hiring Claude Managed Agents par chalti hai: wahi technology jo ek engine option ki tarah serve karti
hai, meta-layer ki tarah bhi serve karti hai, kyunke runtime mein agents/environments create karne ki
uski ability hi workforce expansion ko ek callable capability banati hai.

**Industry corroboration.** Feb 2026 mein, Cursor ke CEO ne company ke IDE-se-factory pivot ko is thesis
ki architecture jaise strikingly close terms mein describe kiya — fleets of agents teammates ki tarah
kaam karte hue, insan problems define kar ke artifacts review karte hue, parallel cloud agents
line-by-line guidance replace karte hue. May 2026 mein, The New Stack ne isi pattern ko Anthropic, OpenAI,
Google, Microsoft, aur Cursor ke across ek industry-wide consensus ki tarah document kiya: model
commodity ban raha hai, harness product ban raha hai. Google Cloud ke Chief Evangelist ne khule aam
maana ke company ko ab farq nahi parta developers kaunsa coding tool istemal karte hain. Dono pieces
evidence hain ke is thesis ke naam liye seams — principal, delegate, management layer, engine, system of
record, aur nervous system ke darmiyan — ab production mein scale par carve ho rahe hain.

**First-party genealogy.** Mid-2026 mein, Anthropic ne Claude Code ki origins ki ek oral history publish
ki, jo is thesis ke invariant vs implementation wale central distinction ka ek controlled experiment
jaisi parhti hai. Form factor model se pehle try hui thi: ek internal terminal agent "clide" launch se
kaafi pehle substantially yehi shape rakhta tha, aur team isay "ahead of its time but too unreliable to
matter" batati hai. Jab models capability threshold cross kar gaye, wahi shape kamyab ho gayi — researcher
Dawn Drain ke lafzon mein, "once you cross the model capability threshold, the form factor kind of
reveals itself." Team ke andar, yeh hindsight se pehle doctrine tha: Ben Mann, jinhon ne Labs team lead
ki jisne product incubate kiya, batate hain ke woh jaan-boojh kar aisi cheezein banate the jo 20-30%
waqt kaam karein taake agla model unhein 80% kaam karne laayak bana de — us model ke liye design karna
jo aa raha hai, jo maujood hai uske liye nahi. Yehi is thesis ki reference-implementation philosophy hai,
product practice ki tarah bayan ki gayi: invariant ke liye build karo, aur realization ko catch up karne
do. Retrospective genealogy bhi confirm karta hai jo invariants assume karte hain: agentic pattern jo
yeh describe karte hain — ek model shell ke sath, ek harness, durable execution — Anthropic ki
reinforcement-learning aur safety research ke andar 2021-22 jitni jaldi carve ho raha tha, aur team note
karti hai ke 2026 ke infrastructure problems (secure code execution, environment management, harness
design) pehle se 2022 ke problems the. Architecture us product se pehle ki hai jisne isay famous banaya.

## The Workforce Opportunity

AI jobs ko tasks mein **unbundle** karega. Kuch tasks poori tarah automate ho jayenge. Lekin unbundling
naye combinations bhi banata hai — nayi roles, naye businesses, naye markets jo tab exist nahi karte the
jab kaam rigid job titles mein locked tha.

Future workforce ko **dynamic skill portfolios** banane hongi, fixed career paths par bharosa karne ke
bajaye. Jo professionals AI ke sath sochna seekhte hain, roz AI tools use kar ke build karte hain, aur AI
ko ek digital teammate ki tarah collaborate karte hain — woh sirf transition survive nahi karenge, usmein
**thrive** karenge.

SaaS era ne developers, designers, aur product managers ke liye lakhon jobs banayin. Agent Factory era
inse zyada banayega — agent designers, outcome architects, verification specialists, aur domain experts
jo machines ko sikhate hain ke unke field mein "correct" ka matlab kya hai. **Yeh history ke sabse bare
workforce training opportunities mein se ek bhi hai:** 2030 tak, duniya bhar mein har 100 mein se 59
workers ko naye technologies aur kaam ke tareeqon ke liye reskilling/upskilling chahiye hogi.

Wahi factory har business function mein specialist Workers produce karta hai. GTM (Go-To-Market — sales,
marketing, aur revenue motion jo prospects ko paying customers banata hai) mein, ek Worker fleet lead
enrichment, outreach sequencing, CRM hygiene, pipeline analysis, proposal generation, aur demo
customization handle karta hai — jo kaam SaaS era mein human "GTM Engineers" haath se karte the, ab
Workers ki tarah manufacture hota hai aur ek human GTM lead supervise karta hai. Yehi pattern **Finance**
(close, AR/AP, FP&A), **Support** (triage, resolution, escalation), **Engineering** (review, refactor,
deploy), **HR** (sourcing, screening, onboarding), aur **Legal** (review, redline, intake) mein repeat
hota hai. Har Worker Paperclip ke through hire hota hai, relevant function mein ek insan se supervise
hota hai, aur us function ke system of record ke against chalta hai — GTM ke liye CRM, Finance ke liye
general ledger, Support ke liye ticketing system, Engineering ke liye code repository. Invariants
verticals ke across nahi badalte. Sirf role definitions aur systems of record badalte hain.

**Opportunity chhota nahi ho raha. Yeh bara ho raha hai, aur jo adapt karte hain unhein reward karta
hai.**

Jan 2026 tak, US data center construction $42 billion annualized tak pahonch chuka tha, jabke office
construction apne peak se 35% gir chuka tha. Lines cross ho chuki hain: America ab digital workers ke
liye workplaces banane par insaano ke liye banane se zyada kharch karta hai.

Data centers copper aur electricity ko industrial scale par khatam kar rahe hain: ek hyperscale AI
facility ko 50,000 tons tak copper chahiye — ek conventional data center se dus guna zyada. Sirf Meta,
Google, Amazon, aur Microsoft milkar 2026 ke liye $600 billion se zyada AI infrastructure spending
project karte hain.

Agent era ki factories hypothetical nahi. Woh construction mein hain.

Yeh sirf ek American story nahi. UNCTAD ki *World Investment Report 2026* ke mutabiq, strategic sectors
(data centers aur baaqi AI infrastructure, semiconductors, critical minerals, energy-transition
technology) ne 2025 mein 44% global greenfield FDI project value capture ki, jo 2020 mein 16% thi — aur
inmein se sabse bara sector, data centers, akele 21 cents (44 mein se) le gaye. Renewable-energy
greenfield values 28% gir gayin, international infrastructure investment 10% gir gayi.

Yeh reallocation balance sheets par bhi dikhta hai. 15 saal tak hyperscalers capitalism ki sabse pure
cash machines thin — asset-light platforms jo $250 billion saalana free cash flow generate karti thin.
AI buildout ne isay invert kar diya hai: Amazon, Google, Meta, Microsoft, aur Oracle ki combined free
cash flow pehli baar negative hone ka forecast hai, jabke chipmakers (Nvidia, Micron, Broadcom, Applied
Materials) $400 billion se aage nikal rahe hain. Cash gayab nahi ho raha — supply chain mein neeche move
ho raha hai. Aur pehli baar, buyers build karne ke liye udhar le rahe hain: BofA 2026 mein hyperscaler
debt issuance $175 billion tak pahonchne ka forecast karta hai — pichle 5 saal ki annual average se 6
guna zyada.

Is scale ka ek precedent problem hai. Har pichli capital surge itni steep boom-bust mein khatam hui —
Railway Mania, Canal Mania, Roaring Twenties, Dot-Com. In sabse compare karein to, AI ki investment curve
tez aur jaldi zyada barh rahi hai. Honest sawal yeh nahi ke yeh ek boom hai — sawal yeh hai ke kya yeh
record par sabse bari bubble bhi hai.

Lekin ek bursting investment bubble aur ek failed technology same event nahi. Railway Mania ne investors
barbaad kiye; Britain ne railways rakhi. Dot-Com crash ne trillions market value mita di; jis internet
par yeh bana tha usne agle do dashak reshape kiye. Capital cycle aur underlying capability ki durability
independent variables hain — aur yeh book doosre par bet hai, pehle par nahi. Kya AI infrastructure
spending 2027 mein correct hoti hai, yeh valuations ka sawal hai. Kya agentic systems Digital FTEs mein
manufacture ho kar AI-Native Companies mein compose ho sakte hain, yeh architecture ka sawal hai. Saat
invariants bubble ke zinda rehne par depend nahi karte. Factories dono soorat mein banti hain.

**Winners seats sold se nahi measure honge. Woh guaranteed outcomes se measure honge.**

### Where This Points

Agla kya aata hai, yeh naam lene se pehle, yeh yaad rakhna zaroori hai ke thesis abhi kahan khadi hai.
Mid-2026 tak, single-digit-headcount firms billion-dollar annualized revenue report kar rahi thin
AI-operated workforces ke against — ek company category jo teen saal pehle kisi bhi meaningful form mein
exist nahi karti thi. Individual cases apne merits par succeed/fail karenge, aur kuch regulatory
scrutiny survive nahi karengi. Category karegi. Thesis ne firm ki shape predict ki thi; firm aa chuki
hai.

Thesis defend karti hai jo Agent Factory aaj aur immediate future mein banata hai: software AI Workers,
jo AI-Native Companies mein compose hote hain, human-mediated commerce ke edges par transact karte hue.
Yehi scope hai jo yeh document earn karta hai. Lekin architecture scope se aage extend karta hai, aur
band karne se pehle teen trajectories naam lene laayak hain:

**Physical AI Workers.** Wohi factory architecture jo software AI Workers banati hai, embodied Workers
tak extend karti hai. Warehouse work karta ek robot, autonomous courier ki tarah operate karti ek
vehicle, factory floor par ek machine — har ek usi authority envelope ke tehat ek AI Worker hai, usi
management layer se hired, aisi runtime engine par chalta hai jo API calls ke bajaye actuators drive
karta hai. Invariants nahi badalte. Compute layer ek body add karti hai.

**Fully autonomous economic agents.** Is thesis ki opening isi trajectory ka naam leti hai; yeh section
usay earn karta hai. Jaise AI Workers durable identity, payment rails, reputation, aur contractual
capacity paate hain, woh apni company ke operate kiye tools nahi rehte — apne haq mein economic actors
ban jate hain — doosri companies ke AI Workers se services khareedte hain, jinko zaroorat hai unhein
capacity bechte hain, capital accumulate karte hain, aur har transaction ke liye insan ke bina agreements
mein enter karte hain.

**Cross-company workforce mobility.** Aaj, ek AI Worker ek company banati aur deploy karti hai. Jaise
manufacturing layer mature hoti hai, AI Workers portable ban jate hain — ek company mein hire, doosri
mein transfer, shayad kai companies mein simultaneously kaam karte hue. Paperclip ki hiring API
intra-company se cross-company tak generalize hoti hai. Alag companies ke authority envelopes ek hi AI
Worker par overlap karte hain, contract se governed. AI Workers ke liye labor market ek real market ban
jata hai — rates, reputations, specializations, aur turnover ke sath.

Yeh teen trajectories — embodiment, autonomy, aur mobility — architecture ki extensions hain, departures
nahi.

> **Invariants hold karte hain. Realizations evolve karte hain. Thesis khadi rehti hai.**

---
[⬅ 06 — Seven Invariants Part 2](06-seven-invariants-part2.md) · [Agla: 08 — Test Your Understanding ➡](08-test-your-understanding.md) · [⬆ Index](README.md)
