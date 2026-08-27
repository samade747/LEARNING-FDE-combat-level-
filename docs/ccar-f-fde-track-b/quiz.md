# Quiz — CCAR-F FDE Track B Accelerated (Self-Authored, 12 Questions)

Root syllabus file + [[ecosystem-designing-the-vertical-sor]] se grounded. Format harness-engineering
quiz jaisa: scenario, sahi jawab, explanation, real-world analogy.

---

### Q1. Ek bug fix chhota, isolated, well-understood hai

**Q:** Ek team ek single-file, well-understood bug fix ke liye plan mode chalu karti hai "safety ke
liye." Decision framework (Week 6) ke hisab se yeh sahi hai?

- Haan, plan mode hamesha safer hai
- **Nahi — plan mode fixed/predictable, multi-file, ya multiple-valid-approach kaam ke liye hai; isolated well-understood change direct execution se chalti hai** ✅
- Sirf tab sahi hai jab codebase bara ho
- Plan mode sirf Claude Agent SDK mein exist karta hai, Claude Code mein nahi

**Explanation:** Framework clear hai: direct execution chhote, well-understood, isolated changes ke
liye; plan mode architectural/multi-file/uncertain/multiple-valid-approach kaam ke liye. Har cheez par
plan mode lagana overhead add karta hai bina value ke. Real-world: ek chhoti si repair ke liye poora
blueprint banwana waqt zaya karta hai.
*(Week 6 — Claude Code architecture)*

---

### Q2. Refund control sirf prompt mein likha hai

**Q:** Project 2 (governed customer-support agent) mein "$500 se zyada refund manager approval maange"
sirf system prompt mein likha hai, code mein nahi. Architecture Decision Framework kya kahegi?

- Theek hai, clear prompt kaafi hai
- **Yeh required behaviour hai — deterministic control chahiye (code/hook/permission gate), prompt guidance nahi** ✅
- Escalation criteria hai, sirf documentation chahiye
- Ismein koi farq nahi padta jab tak model reliable ho

**Explanation:** "Required behaviour → deterministic control" framework ka pehla row hai. Ek business
invariant jo violate nahi honi chahiye, prompt wording par depend nahi kar sakti — model confused ho
sakta hai, context rot ho sakta hai. Yehi wajah hai Project 2 explicitly "programmatic refund controls"
maangta hai, sirf prompt instruction nahi. Real-world: bank ka approval-above-limit rule software mein
hard-coded hota hai, teller ke "yaad rakhne" par depend nahi karta.
*(Week 5 — Claude Agent SDK III, trust and hooks)*

---

### Q3. Subagent ko poori parent conversation "chahiye"

**Q:** Ek developer assume karta hai delegated subagent ko parent conversation ka poora context
automatically milta hai. Week 4 ka context rule kya kehta hai?

- Sahi assumption hai, subagents hamesha full context inherit karte hain
- **Subagents parent context automatically inherit nahi karte — jo context chahiye woh explicitly pass karna padta hai** ✅
- Sirf `Task` tool automatic inheritance deta hai, baaki nahi
- Context sirf `CLAUDE.md` se automatically flow karta hai

**Explanation:** Multi-agent architecture ka core rule: coordinator jo bhi subagent ko chahiye woh
explicitly pass karta hai, kuch bhi automatic nahi. Isay bhoolna woh classic "creative industries"
narrow-decomposition failure paida karta hai jo Week 4 lab reproduce karti hai. Real-world: ek naya
contractor site par aata hai — usay poori company history nahi pata hoti, sirf woh brief milti hai jo
diya jaye.
*(Week 4 — multi-agent architecture)*

---

### Q4. Message Batch ke andar multi-turn tool loop

**Q:** Ek engineer Message Batches ka use ek multi-turn tool-calling loop ko ek hi batch request ke
andar chalane ke liye karna chahta hai. Week 10 kya kehti hai?

- Yeh standard use-case hai, Batches isi ke liye bane
- **Message Batches multi-turn tool loop support nahi karti ek request ke andar — plus koi latency SLA nahi, 24h tak le sakti hai** ✅
- Sirf `tool_choice: auto` ke sath support karti hai
- Batches sirf structured extraction ke liye hain, tool calls ke liye nahi

**Explanation:** Batches ek cost trade-off hain (50% reduction) but shape mismatch — ek single request,
no multi-turn loop andar, no latency guarantee. Suitable workload: bulk independent extraction/
classification jobs, real-time ya conversational multi-step kaam nahi. Real-world: bulk mail cheap hai
lekin ek back-and-forth conversation ke liye nahi bana.
*(Week 10 — validation, human review, batch)*

---

### Q5. "0.95 reliable enough" jaisa architect-level sawal

**Q:** Track B ka Architecture Decision Framework "Expensive mistakes → explicit human-review/approval
boundary" kehta hai. Ek $50 refund aur ek $50,000 contract-signing action, dono automatic hon to yeh
rule kaise differ karegi?

- Dono same treatment paate hain, dollar amount irrelevant hai
- **Blast radius differ karti hai: $50 refund shayad allow-bucket mein ja sakta hai, $50,000 action ko explicit human approval boundary chahiye — mistake ki cost decide karti hai, frequency nahi** ✅
- Sirf regulatory domains mein approval chahiye
- Approval boundary sirf refunds ke liye hai, contracts ke liye nahi

**Explanation:** Yeh [[harness-engineering]] ke "blast radius, not frequency" principle ka wahi
architecture-level version hai (Concept 4). Chhoti reversible actions autonomy pa sakti hain; bari
ya irreversible actions ko named-human approval chahiye — dollar amount ek proxy hai blast radius ke
liye. Real-world: ek bank teller $50 withdrawal khud approve kar sakta hai, $50,000 wire transfer ke
liye manager sign-off chahiye.
*(Week 5 + Architecture Decision Framework)*

---

### Q6. Stateless MCP server "session" maintain karta hai

**Q:** P6 (Stateless MCP I) mein ek student apne MCP server mein ek in-memory session object banata hai
jo requests ke beech state yaad rakhta hai "performance ke liye." Yeh stateless core ke against hai?

- Nahi, sessions optional optimization hain
- **Haan — stateless core ka poora point yeh hai ke har call independent request/response ho, koi protocol-level session nahi, taake server ko load-balancer ke peeche multiple copies mein chalaya ja sake** ✅
- Sirf tab problem hai jab server crash ho
- Sessions sirf `server/discover` mein allowed nahi hain

**Explanation:** Book (`context-layer-crash-course`) confirm karti hai: stateless HTTP default hai
kyunki koi ek client ek specific server instance se pinned nahi hota — koi bhi copy koi bhi request
answer kar sakti hai. In-memory session state yeh guarantee tor deti hai (agar request kisi doosri
copy par jaye, state gayab). Per-request metadata use karo, server-side session nahi. Real-world: ek
call-center jahan koi bhi agent koi bhi call utha sake, agent apni memory par depend nahi karta.
*(P6 — Stateless MCP I; book-confirmed)*

---

### Q7. `requestState` ko client apni marzi se modify kar deta hai

**Q:** P7 (MRTR) implement karte waqt, server `requestState` ko trust kar leta hai bina validate kiye,
kyunki "yeh humne khud generate kiya tha." Syllabus kya kehti hai?

- Theek hai, apna hi generate kiya field trust karna safe hai
- **`requestState` ko untrusted treat karo aur handler ko re-entrant banao — client-supplied kuch bhi tamper ho sakta hai** ✅
- `requestState` sirf debugging ke liye hai, production mein use nahi hota
- Yeh rule sirf stateless core par lagu hota hai, MRTR par nahi

**Explanation:** Syllabus explicit hai: `requestState` opaque hai server ki taraf se generate, lekin
client ke through round-trip karta hai — jab wapas aaye, tab bhi untrusted input hai, kyunki koi bhi
client-controlled channel tamper-able hai. Handler ko re-entrant hona chahiye taake ek replayed ya
modified `requestState` crash ya security hole na bane. Real-world: ek signed cookie ko bhi server
dobara verify karta hai, sirf isliye trust nahi karta ke usne khud issue kiya tha.
*(P7 — Stateless MCP II, MRTR)*

---

### Q8. Ek "thin" Vertical SoR ko "incomplete" samjha jaraha hai

**Q:** Ek student kehta hai unka Vertical SoR "thin" hai isliye "abhi unfinished/draft hai." Design
method ([[ecosystem-designing-the-vertical-sor]]) kya correction degi?

- Sahi hai, thin ka matlab draft hai
- **Thin sirf breadth (kitne outcomes) measure karta hai, depth nahi — ek thin slice bhi poori tarah complete honi chahiye (missing-evidence case, wrong jurisdiction, forbidden request sab handle karti ho), warna woh "unfinished" hai, "thin" nahi** ✅
- Thin ka matlab hai koi governance abhi tak nahi lagi
- Sirf capstone (P13) tak thin rehna theek hai

**Explanation:** Method explicit distinction karta hai: thin/thick sirf outcome-count hai (ek vs kai).
Ek outcome jo sirf clean cases handle kare, missing-evidence/wrong-jurisdiction/forbidden-request
handle na kare, woh "thin" nahi hai — woh unfinished hai, chahe governance kitni bhi lagi ho. Milestone
3 (P11) ka 3-class evaluation set isi ko test karta hai. Real-world: ek restaurant jo ek hi dish
perfect banata hai (thin menu) — lekin us dish ko allergies, substitutions, aur complaints ke sath bhi
handle karna aata hai (complete), sirf ek clean order nahi.
*(P3-P13, design method cross-reference)*

---

### Q9. Bin 1 element "habit jaisa" lag raha hai

**Q:** Workflow archaeology karte waqt ek student ek "hamesha do log approve karte hain" rule ko Bin 3
(old technology) mein daal deta hai kyunki "do log ki zaroorat nahi, ek Worker sab dekh sakta hai."
Design method kya warning degi?

- Sahi hai, Worker fatigue-proof hai isliye dual-approval waste hai
- **Jab doubt ho, element Bin 1 mein rehta hai jab tak governing source + expert confirm na karein ke redesign safe hai — separation-of-duties jaisa control regulator ka requirement ho sakta hai, habit nahi (Chesterton's Fence)** ✅
- Dual-approval hamesha Bin 2 hoti hai
- Sort decision record karne ki zaroorat nahi jab tak final version na ho

**Explanation:** Method ka apna failure-mode #7 "first-principles theater" isi galti ko naam deta hai —
Bin 1 ko habit samajh kar delete karna, phir compliance meeting mein pata chalna woh law thi. Separation
of duties aksar regulator ka naam-diya requirement hoti hai (control ka *purpose* Bin 1, sirf
*mechanism* Bin 2 ho sakta hai). Har sort decision apni reason ke sath record honi chahiye. Real-world:
Chesterton's Fence — jab tak pata na ho fence kyun lagi thi, usay hatao mat.
*(P3 — Design the Vertical SoR, three-bin sort)*

---

### Q10. Escalation message sirf "unable to continue" kehta hai

**Q:** Week 5 ka escalation-quality bar Project 2 ke support agent par apply karo: agent likhta hai
"I cannot process this request." Yeh acceptable escalation hai?

- Haan, honest hai ke agent stuck hai
- **Nahi — useful escalation kya-already-verify-hua batata hai, ek specific open requirement naam deta hai, aur ek ready-to-make decision deta hai; "unable to continue" insaan ko poora case zero se dobara dekhne par majboor karta hai** ✅
- Sirf tab acceptable hai jab refund $500 se kam ho
- Escalation ka format sirf CCAR-F exam mein matter karta hai, production mein nahi

**Explanation:** [[ecosystem-designing-the-vertical-sor]] ka escalation-bar principle Track B ke Week-5
"structured human handoffs" ke sath directly overlap karta hai: ek useful escalation kehta hai *"refund
approve nahi kar sakta kyunki proof of purchase missing hai; customer ID aur order dono verified hain;
sirf proof of purchase chahiye; supervisor approval maangi ja rahi hai."* Ek bare "cannot continue" sab
kaam wapas insaan par daal deta hai. Real-world: ek nurse jo doctor ko bulati hai "patient ki BP high
hai, dawa X di ja chuki hai, dosage confirm chahiye" — na ke sirf "kuch theek nahi hai."
*(Week 5 + design method cross-reference)*

---

### Q11. Milestone 2 ka "working agent surface" kya prove karta hai

**Q:** Ek student P8 complete karta hai — MCP tools chalte hain, koi crash nahi. Kya yeh Milestone 2 pass
kar deta hai?

- Haan, chalna hi kaafi hai
- **Nahi — Milestone 2 ka evidence hai "stateless MCP search/retrieve/cite interface" jo knowledge boundary bhi enforce kare (jo corpus mein nahi hai uspar abstain kare) — sirf tools chalna kaafi nahi, boundary enforcement zaroori hissa hai** ✅
- Milestone 2 sirf P9 (KSoR adoption) ke baad claim ho sakta hai
- Milestone 2 ka koi evidence-criteria nahi, sirf demo dikhana kaafi hai

**Explanation:** Milestones table explicit "evidence" column deti hai — Milestone 2 = "stateless MCP
search/retrieve/cite interface," aur P8 ka apna task line "enforce the knowledge boundary in
application logic" kehta hai. Ek Worker jo corpus se bahar ki cheez confidently answer kar de, boundary
fail kar chuka hai chahe tool call successfully chal jaye. Real-world: ek reference librarian jo har
sawal ka jawab de deta hai, chahe kitab shelf par ho ya na ho, "helpful" nahi hai — galat hai.
*(P8 + Milestones table)*

---

### Q12. Assessment weight — Mock Two vs Trade-off Notebook

**Q:** Ek student sochta hai "trade-off notebook chhota kaam hai, Mock Two hi asli grade hai." Assessment
table (70/30 split) is soch ko kaise correct karti hai?

- Trade-off notebook 21% hai, Mock Two 7% — student sahi hai
- **Mock Two 21% hai (highest single component), lekin trade-off notebook 7% + scenario practice 7% dono milkar hafta-hafta wahi reasoning practice karte hain jo Mock Two test karti hai — chhota individually, lekin cumulative aur foundational** ✅
- Sirf Mock One aur Mock Two grade matter karti hain, baaki sab pass/fail hai
- Practicum ka 30% architect grade se pehle complete hona zaroori hai

**Explanation:** Architect subtotal: scenario practice 7%, Projects 1-4 28%, Mock One 7%, Mock Two 21%,
trade-off notebook 7% = 70%. Mock Two akela sabse bara single item hai, lekin notebook + scenario
practice mil kar poori quarter mein wahi "trade-off kya tha, kya choose kiya, alternatives kamzor kyun"
reasoning drill karte hain jo scenario-based exam items test karte hain — cumulative practice, ek-baar
ka test nahi. Real-world: roz ka practice-drill chhota lagta hai, lekin final match uske bina nahi
jeeta jata.
*(Assessment table, Week 12-13)*

---
[⬅ Test Your Understanding](05-test-your-understanding.md) · [⬆ Index](README.md)
