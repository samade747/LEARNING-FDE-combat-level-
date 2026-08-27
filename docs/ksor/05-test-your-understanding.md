# 05 — Test Your Understanding (Exam Assessment)

*Yeh chapter `panaversity/ksor` GitHub README + `KSoR-Complete-Guide (1).pdf` se bana hai (book ka
koi live `<Quiz>` component nahi — dekho [`docs/ecosystem-designing-the-vertical-sor/`](../ecosystem-designing-the-vertical-sor/README.md)
us book-lesson ke liye). Isliye yeh 12 questions is chapter (`00`-`04`) ke content se khud grounded
hain, harness-engineering ke quiz format follow karte hue: scenario, 4 options, ek sahi jawab ✅,
explanation, aur real-world analogy.*

---

### Q1. Spreadsheet aur accounting ledger mein farq ho to kaun jeetta hai?

**Q:** Ek company ka spreadsheet kehta hai revenue $1.2M hai, lekin accounting ledger $1.15M dikhata
hai. Traditional System of Record ka usool is farq ko kaise resolve karta hai?

- Dono ka average le lo
- **Ledger jeetta hai — wahi authoritative Traditional System of Record hai** ✅
- Jo zyada recent hai wo jeetta hai
- Kisi human manager se pooch lo

**Explanation:** Traditional Systems of Record (accounting ledger, CRM, HRIS) ka poora point yehi hai:
ek hi authoritative jagah jo batati hai "abhi operational state kya hai." Spreadsheet convenient ho
sakta hai lekin authoritative nahi — jab conflict ho, ledger ka jawab final hota hai, kyunke ledger
governed hai (review, controls, audit trail) aur spreadsheet nahi. Real-world: bank statement aapki
mental calculation se zyada authoritative hai, chahe aapki calculation "sahi feel" ho.
*(Section 1: KSoR Kyun Banaya Gaya)*

---

### Q2. Ek AI agent ko "$50,000 se zyada purchase ka approval threshold kya hai" jaisa sawal poochna hai

**Q:** Yeh sawal traditional SoR (jaise ERP) resolve nahi kar sakta, kyunke woh sirf operational state
(transactions, balances) record karta hai. Is gap ko kaun bharta hai, aur kaise?

- ERP ka permissions module — thresholds bhi ek tarah ka "state" hain
- **Knowledge System of Record — policies, rules, thresholds "hum kya jaante hain, kaise operate karna hai" ka jawab deta hai** ✅
- Ek doosra spreadsheet jo IT team maintain karti hai
- Model ki training knowledge — approval thresholds usually standard hote hain

**Explanation:** Traditional SoR ka bunyadi sawal hai "abhi kya sach hai" (state); KSoR ka bunyadi sawal
hai "hum kya jaante hain, kaise operate karna hai" (knowledge). Approval threshold ek policy hai, ek
transaction nahi — isliye ERP ka scope nahi. Model ki training knowledge guess hai, authoritative source
nahi. Real-world: ERP batata hai "abhi kitna paisa account mein hai," HR policy manual batata hai "kis
se approval leni hai" — dono alag documents, alag maqsad.
*(Section 2: Traditional SoR vs Knowledge SoR)*

---

### Q3. Ek naya RAG system har document ko vector database mein daal deta hai, similarity search karta hai

**Q:** Team dawa karti hai "yeh humara KSoR hai." Course ke mutabiq is dawe mein kya missing hai?

- Kuch nahi — RAG + vector database hi KSoR ki definition hai
- **Authority — ownership, provenance, versioning, review, conflict-resolution, abstention: sirf storage/retrieval kaafi nahi** ✅
- Sirf itna ke Markdown ki bajaye vector database use ho raha hai
- Search speed — RAG bohat slow hota hai KSoR ke muqable

**Explanation:** Ek knowledge base sirf information store/retrieve karta hai. KSoR **authority**
establish karta hai — malik kaun hai, source kahan se aayi, kaunsi version authoritative hai, review hui
ya nahi, conflict mein kya jeetega, aur agar jawab hi na ho to abstain karna. RAG/vector-search sirf ek
implementation detail ho sakta hai KSoR ke andar, lekin khud KSoR nahi. Real-world: Google Search bohat
files "retrieve" kar sakta hai, lekin koi bhi random webpage "authoritative company policy" nahi ban
jaati sirf isliye ke woh searchable hai.
*(Section 3: KSoR Sirf Knowledge Base Se Zyada Hai)*

---

### Q4. Company ki website ek cheez kehti hai, aur agent ka MCP corpus doosri

**Q:** Ek customer complain karta hai ke chatbot ne refund policy kuch aur bataya, jabke website kuch
aur dikhati hai. KSoR ke "Ek Source, Do Surfaces" principle ke mutabiq yeh kaise hona hi nahi chahiye
tha?

- Website aur agent corpus alag-alag maintain honi chahiyen, sync manually honi chahiye
- **Dono ek hi governed source ke projections hain ("Same Truth") — agent corpus website ki chhupi copy nahi** ✅
- Chatbot ko hamesha website se zyada trust milna chahiye kyunke woh live hai
- Yeh normal hai — dono systems thoda alag reh sakte hain

**Explanation:** KSoR ka core usool: Human Surface (website) aur Agent Surface (MCP) dono ek hi governed
source ke do projections hain, alag-alag maintain wali copies nahi. Agar dono alag drift karein to
"Same Truth" toot jaati hai — yehi bug is scenario mein customer ne dekha. Fix maintenance mein nahi,
architecture mein hai: ek hi source, do views. Real-world: ek company ka printed brochure aur website
dono ek hi central pricing database se generate hone chahiye, do alag teams ke hath se type nahi.
*(Section 4: Ek Source, Do Surfaces)*

---

### Q5. Agent ko pata nahi ke kisi khaas cost ko capitalize karna sahi hai ya nahi, KSoR mein clear policy nahi hai

**Q:** Accounting KSoR misaal mein, is situation mein agent ko kya karna chahiye per "Abstention Is a
Feature" principle?

- Sabse conservative guess le le (hamesha expense treat kare)
- Sabse aggressive guess le le (hamesha capitalize kare)
- Apni training knowledge se general accounting rule use kar le
- **Bata de ke policy is situation ko cover nahi karti — khud se naya policy invent na kare** ✅

**Explanation:** Principle 5 explicit hai: "Agar KSoR mein jawab nahi hai, to sahi jawab hai 'yeh maloom
nahi' — guess karna nahi." Accounting misaal mein bhi yehi likha hai: "Agar policy is situation ko cover
nahi karti, to system khud se policy banayega nahi." Guessing (chahe conservative ho ya aggressive)
authority ko replace kar deta hai model ke confidence se — yehi galti KSoR rokta hai. Real-world: ek
doctor jo apne pass koi test result na hone par bhi confidently diagnosis de de, uske bajaye "aur tests
chahiye" kehna zyada safe hai.
*(Section 5: 7 Core Principles — Abstention Is a Feature)*

---

### Q6. Do documents ek hi policy par contradict karte hain — ek 2024 ka hai, ek 2026 ka

**Q:** Agent ko "Citation Before Confidence" aur "Provenance Matters" principles follow karte hue is
conflict ko kaise handle karna chahiye?

- Jo document zyada detail mein likha hai usay follow kare
- **Dono ki version/date trace kare, aur clarify kare kaunsi authoritative hai (ya escalate kare agar pata na chale) — apni training se guess na kare** ✅
- Confidently newer document follow kare bina kisi ko batae
- Dono ko ignore kar ke apni general knowledge use kare

**Explanation:** Provenance Matters ka matlab hai jawab ka chain (kaunsi document, kaunsi version, kab
bani) hamesha maloom honi chahiye. Citation Before Confidence ka matlab hai model ka confident lehja
proof nahi — jawab trace hona chahiye. Sirf "newer wins" assume karna khud ek guess hai jab tak
governance rule explicitly na kahe ke naya document purane ko supersede karta hai. Sahi jawab: provenance
dikhana, aur agar authoritative version clear na ho to escalate/abstain karna. Real-world: do alag saal
ki tax guidance milein to accountant dono ki effective date check karta hai, sirf "jo zyada recent lage"
use nahi karta.
*(Section 5: 7 Core Principles — Provenance Matters, Citation Before Confidence)*

---

### Q7. Ek naya team member poochta hai: "Yeh Accounting KSoR hai, ya Agent Factory KSoR, ya Design System KSoR — teeno mein farq kya hai?"

**Q:** Course ke "KSoR Se Kya Bana Sakte Hain" section ke mutabiq, yeh teeno kis classification mein
aate hain?

- Teeno alag products hain, koi common architecture nahi
- **Teeno Organizational/Domain/Product-Method KSoR ki teen categories hain — same underlying pattern, alag content scope** ✅
- Sirf Accounting KSoR asal KSoR hai, baaki misnomers hain
- Yeh purane naam hain, ab sab "Vertical KSoR" kehlate hain

**Explanation:** Course teen types define karta hai: Organizational KSoR (jaise Agent Factory KSoR,
Engineering KSoR), Domain KSoR (jaise Accounting, Healthcare, Legal — inhi mein se ek "Vertical KSoR"
hai), aur Product/Method KSoR (jaise Design System, API Standards). Teeno ek hi underlying pattern use
karte hain (governed source, do surfaces, 7 principles) — sirf content ka scope alag hota hai
(organization-wide vs domain-specific vs product-specific). Real-world: ek company ke paas HR handbook,
engineering runbook, aur product design-guide teeno alag documents hain lekin sab "governed internal
knowledge" ke underlying pattern follow karte hain.
*(Section 6: KSoR Se Kya Bana Sakte Hain)*

---

### Q8. Ek developer poochta hai "`npx @panaversity/ksor init` chala kar dekhta hoon, working KSoR mil jayega?"

**Q:** Course ke Quick Start section ke mutabiq abhi is command ka kya hoga?

- Poora working KSoR scaffold ban jayega, ready to deploy
- **"Status notice" print hoga aur exit code 2 dega — commands abhi sirf design hain, implement nahi hue (package `0.0.0` par hai)** ✅
- Error dega kyunke package publish hi nahi hua
- Interactive setup wizard khulega jo questions poochega

**Explanation:** Course explicitly warn karta hai: neeche diye commands (`init`, `dev`, `build`, `serve`)
abhi **design** hain, implement nahi — package `0.0.0` version par hai, sirf naam reserve karne ke liye.
Chalane par status notice print hoga, exit code 2. Yeh AGENTS.md/CLAUDE.md ke "test before claiming
done" pattern ki reminder bhi hai — agar tum khud SDK use karne ki koshish karo, doc se pehle verify
karo woh implement hui hai ya sirf designed hai. Real-world: ek npm package jiska README poora hai lekin
`package.json` mein `"version": "0.0.0"` likha ho — naam reserve hua hai, code nahi.
*(Section 7: Quick Start Aur CLI)*

---

### Q9. Ek reviewer poochta hai "yeh jawab agent ne kahan se liya?" — kaunsa mechanism jawab deta hai?

**Q:** Course ke "Build Provenance" section ke mutabiq, konsa specific artifact yeh chain trace karta
hai?

- Agent ke chat logs, jo har session save hote hain
- **`build.lock.json` — included documents, unke hashes, source commit, KSoR version record karti hai, chain: Answer → Passage → Document → Build → Commit → Source** ✅
- Git blame, kyunke sab kuch Markdown mein hai
- Model provider ka apna internal logging system

**Explanation:** "Knowledge As Code" section specific karta hai: `build.lock.json` file included
documents, unke hashes, source commit, aur KSoR version record karti hai. Isse ek poori traceable chain
banti hai: AI Answer → Retrieved Passage → Knowledge Document → KSoR Build → Git Commit → Reviewed
Source. Yeh chain hi "jab koi poochay agent ne yeh kyun kaha" ka discoverable jawab deti hai — chat logs
ya git blame akele itni specific chain nahi dete. Real-world: software supply-chain security mein
`package-lock.json` bhi isi tarah exact dependency versions/hashes pin karta hai reproducibility ke liye.
*(Section 9: Knowledge As Code + Build Provenance)*

---

### Q10. Ek team KSoR ko "bas ek RAG system hai" keh kar dismiss karti hai

**Q:** Course ke "KSoR vs RAG" section ke mutabiq, is dawe mein sabse bara galti kya hai?

- Koi galti nahi, KSoR asal mein RAG hi hai different naam se
- **RAG ka sawal hai "context mein kya dalein," KSoR ka sawal hai "kaunsi knowledge itni authoritative hai ke insaan/agents is se operate karein" — retrieval to KSoR ka ek chhota hissa hai** ✅
- RAG hamesha behtar hota hai KSoR se, kyunke zyada flexible hai
- KSoR RAG use nahi kar sakta, dono mutually exclusive hain

**Explanation:** Course clearly farq karta hai: RAG ek retrieval technique hai ("relevant info context
mein kaise dalein"). KSoR ek bara sawal poochta hai ("kaunsi knowledge authoritative hai ke organization
insaan aur AI agents ko is se operate karne ki ijazat de"). RAG, KSoR ka hissa ho sakta hai (implementation
detail), lekin KSoR sirf ek RAG wrapper nahi — Governance, Authority, Provenance, Versioning, Review,
Scope, dono surfaces shamil hain, jinmein retrieval ek chhota hissa hai. Real-world: GPS navigation
(retrieval: "yahan se wahan tak rasta") aur traffic-law authority (jo bataye kaunsa rasta legal hai) do
alag cheezein hain, chahe dono ek app mein mil jayein.
*(Section 10: Agent Surface — MCP, Retrieval Asal Product Nahi Hai)*

---

### Q11. Ek policy update hoti hai, lekin koi bhi nahi jaanta kis ne approve kiya ya kab effective hui

**Q:** Course ka Governance Model (Source → Draft → Review → Approved → Authoritative) is masle ko kaise
rokta hai?

- Yeh masla KSoR se bahar hai — koi bhi documentation system isay solve nahi kar sakta
- **Har change ek defined pipeline se guzarti hai; regulated/high-risk knowledge ke liye named owners, approval, effective dates, review periods, audit history explicitly track hoti hain** ✅
- Sirf latest git commit dekh lo, wahi sach hai
- Governance sirf documentation hai, koi enforcement nahi

**Explanation:** Governance Model section explicit pipeline deti hai: Source → Draft → Review → Approved
→ Authoritative KSoR (phir Human/Agent Surface, aur eventually Superseded/Retired). High-risk knowledge
ke liye extra controls: named knowledge owners, approval requirements, effective dates, mandatory review
periods, change records, audit history. Course yeh bhi clarify karta hai: "KSoR architecture deta hai,
governance policy khud organization ki zimmedari rehti hai" — tool structure deta hai, discipline
organization ko laani hoti hai. Real-world: ek company ka document-control system versions track karta
hai, lekin "kaun approve karega" ka policy khud company banati hai.
*(Section 11: Governance Model)*

---

### Q12. Ek agent poocha jata hai "agle saal ki approval policy kya hogi?"

**Q:** "Knowledge Boundaries — Teen Misaalein" table ke mutabiq, yeh sawal kis category mein aata hai,
aur agent ka sahi response kya hai?

- In scope — KSoR mein already answer maujood hai
- Requires reasoning — operational SoR se data jorna padega
- **Outside the KSoR — agar approved nahi hai to guess nahi karna, seedha mana kar dena** ✅
- Yeh invalid sawal hai, agent ko ignore karna chahiye

**Explanation:** Table teen categories deti hai: (1) In scope — policy directly maujood hai, jawab +
source milta hai; (2) Requires reasoning — governed rule ko doosre SoR ke operational facts se jorna
padta hai; (3) Outside the KSoR — future/unapproved cheez, jahan sahi jawab hai "yeh approved nahi hai,"
guess nahi. "Agle saal ki policy" abhi approved nahi hai (future hai), isliye seedha category 3 —
Abstention principle (Q5) yahan bhi apply hota hai. Real-world: ek lawyer "agla saal kaunsa naya tax law
aayega" ka confident jawab nahi deta — sirf "abhi yeh law hai" bata sakta hai.
*(Section 11: Knowledge Boundaries — Teen Misaalein)*

---
[⬅ 04 — Applications, Design Goals, Status](04-applications-design-goals-and-status.md) · [⬆ Index](README.md)
