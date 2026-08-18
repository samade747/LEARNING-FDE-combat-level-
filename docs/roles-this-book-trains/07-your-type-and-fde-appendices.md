# 07 — The Second Axis: Your Type — Plus the FDE Résumé and Interview

## Your Type, Not Just Your Seat

Naqsha upar batata hai kaam **kahan** baitha hai. Yeh nahi batata **kaunsi seat aapko fit karti
hai**. June 2026 mein, Boris Cherny (Claude Code ke creator) ne apni team dekh kar poocha ke roles
kya ban jaate hain jab engineering, product, design, aur data science "ek naye tarah ke role mein
ghul jaate hain." Uska jawab paanch archetypes the, koi bhi job function nahi:

- **The Prototyper** — bilkul nayi ideas churn karta hai, zyadatar kabhi ship nahi hotin.
- **The Builder** — prototype ko production-grade product ya infrastructure mein tezi se badalta hai.
- **The Sweeper** — system simplify karta hai, UI clean karta hai, unships karta hai, optimize karta hai.
- **The Grower** — built product ko product-market fit ki taraf iterate karta hai.
- **The Maintainer** — ek mature system ka malik hai aur usay secure, reliable, tez rakhta hai.

Cherny ki do observations yahan kaam karti hain. Pehli: archetypes titles se bandhi nahi — Anthropic
mein, kuch designers Prototypers hain, kuch Builders, kuch Sweepers, aur wahi spread engineers, PMs,
aur data scientists mein bhi hai. Doosri: zyadatar log do archetypes mein failte hain, kabhi teen,
aur team ko kaunsa mix chahiye woh product ke phase ke sath badalta hai.

Is naqshe ke khilaf, rhymes loud hain lekin one-to-one nahi: Outcome Architect ek Prototyper ki seat
hai. Digital FTE Builder ek Builder ki. Evals Engineer ek Sweeper ki. Cloud AI Engineer aur
Supervisor ek Maintainer ki. Aur "spanning" hi pod of one ka andar se manzar hai: Workers tasks
absorb karte hain, jabke insan ke do-teen archetypes decide karte hain kaunsi seats woh genuinely
le sakta hai. **Roles batati hain kaam kahan hai. Aapke archetypes batate hain kaunsi seat lena
hai.**

## Appendix A — The FDE Résumé: Six Signals

Recruiters ek FDE profile ko software engineer ki tarah nahi parhte. Chhe signals hain, aur profile
jo inhein chhupaye, technical bar test hone se pehle hi reject ho jata hai. Pehle teen poochte hain
**kya aapne asal mein deliver kiya**: shipped production systems (real deployments, backlog
features nahi), quantifiable impact (numbers mein, "feature X banaya" nahi), aur direct customer
exposure. Doosre teen poochte hain **kaise aap deliver karte hain**: messy-data work, ownership
under ambiguity, aur AI/LLM depth (RAG, agents, evals).

Teen rewrites in signals se nikalte hain. **Pehla:** har bullet ko activity se outcome mein badlo —
"ETL pipeline banaya" ban jata hai "ek pipeline ship ki jisne client ka month-end close 5 din se 2
din kar diya." **Doosra:** "I" likho, "we" nahi — screeners "we" ko "was carried" ki tarah parhte
hain. **Teesra:** competitive-programming awards kaato — data-structure puzzles ka prize galat
interview ki taqleeb dikhata hai. Iski jagah ek **portfolio** leta hai: ek deployed Worker, ek
shipped plugin, ek live connector app — har ek ke sath ek-line outcome.

Ek item baqi se alag hai, aur vendor-neutral candidate isay lead karna chahiye: **ek governed slice
of a profession**, dono readers ke liye published. Deployed Worker sabit karta hai aap bana sakte
ho. Governed slice sabit karta hai aap kuch **own** karte ho jo kisi employer ne nahi diya.

## Appendix B — The FDE Interview: The Loop and the Trap

Loop paanch se aath stages chalta hai, teen se chhe hafton mein: recruiter screen, hiring-manager
screen, practical coding round, system-design round, **decomposition case study**, client
simulation, aur behavioral round.

**Decomposition round hi filter hai.** Aapko ek vague, real enterprise problem diya jata hai — jaise
"ek bara city emergency response time kam karna chahta hai; unke paas call data, traffic data, aur
ambulance GPS hai; aapke paas 60 minute hain." Sabse aam rejection: **seedha jawab dena.** Jo
candidate "main XGBoost se predictive model banaunga" se shuru karta hai, woh pehle hi fail ho chuka
hai — usne solve kar diya, scope kiye bina. Jo score karta hai woh sequence hai: asal goal clarify
karo, stakeholders aur success metric naam lo, data map karo aur uska owner poochho, subproblems ko
risk ke hisaab se decompose karo, aur sabse patla end-to-end skeleton propose karo — assumptions
zubaan se bolte huay, failure modes bina poochhe bataate huay. Yeh **spec-driven development hai,
verbally perform ki gayi.**

**Client simulation doosra filter hai.** Ek interviewer customer ka role play karta hai — kabhi
frustrated, kabhi non-technical — aur aap bad news deliver karte ho, ek governance-compromising
request par pushback karte ho, ya explain karte ho ke system 100% accuracy promise nahi kar sakta —
bina jargon ke, bina jhoothe waade ke. Paanch red flags: pehle solve karna clarify kiye bina, cost
aur constraints ignore karna, thin deployment stories, regulated domains mein zero compliance
vocabulary, aur zero customer instinct.

Ek naya format bhi phail raha hai: **the live build.** Ek documented loop teen ghante ka tha: 30
minute vague use case ko requirements mein badalna cross-examination ke tehat, 90 minute working
solution banana ek AI coding assistant ke sath (har suggestion validate karte huay), aur 60 minute
result present karna role-played stakeholder ko pure business language mein. **Koi LeetCode nahi.**

## Appendix C — Preparing for the FDE with This Book

| Interview Round | Yeh Kya Test Karta Hai | Book Mein Kahan Train Hota Hai |
| --- | --- | --- |
| Decomposition case study | Scoping before solving | Spec-Driven Development, How to Think in the AI Era |
| Practical coding | Real engineering, agent ke sath, verified | Python in the AI Era, Code You Never Write |
| AI-specific depth | RAG, agents, evals | Give Your AI Searchable Context, Build AI Agents, Eval-Driven Development |
| System design | Enterprise deployment constraints ke tehat | Thesis Invariants, Choosing Agentic Architectures |
| Client simulation | Trust, pushback, business language | Human-Agent Teams, Strategist track |
| The live build | Agent ko observation ke tehat direct karna | Claude Code and OpenCode |
| Portfolio | Shipped, demonstrable outcomes | Har capstone: deployed Worker, plugin, governed slice |

Table ko neeche se upar parho: interview ke sabse mushkil rounds — decomposition, live build, eval
sawal — curriculum ke upar bolted extras nahi. **Yeh khud curriculum hai, examined.** Jo candidate
ne asal mein spec discipline ke tehat ek Worker manufacture kiya ho, woh decomposition round mein
rehearsed hone ki tarah jata hai — kyunke intent likhna jispar Worker ko hold kiya ja sake, aur ek
vague enterprise problem ko zubaan se scope karna, yeh dono ek hi skill hai, do alag volumes par.

---
[⬅ Supporting Roles](06-supporting-roles-and-where-book-stops.md) · [⬆ Index](README.md)
