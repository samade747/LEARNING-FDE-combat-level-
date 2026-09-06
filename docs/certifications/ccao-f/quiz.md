# Quiz — CCAO-F: Claude Certified Associate, Foundations (Test Your Understanding)

**10-question self-contained assessment**, grounded in `01-domain-blueprint.md` (7 domains) and
`03-how-to-prepare-and-sample-questions.md` (3 official sample questions). Same 10 questions also
live in [`05-test-your-understanding.md`](05-test-your-understanding.md) as the scenario version.

---

### Q1. CCAO-F ka sabse bara domain — prompt writing hai?

**Q:** Ek candidate sochta hai CCAO-F mukhya taur par "acche prompts likhna" test karta hai. Kya yeh
sahi hai?

- Haan, Domain 1 (Prompting) 21% ke sath sabse bara hai
- **Nahi — sabse bara domain (21%) hai "Output Evaluation and Validation": accuracy check karna,
  hallucinations spot karna, human-review kab chahiye decide karna** ✅
- Haan, prompting aur evaluation dono 21% hain, tied first
- CCAO-F mein koi ek domain dominant nahi, sab 14% hain

**Explanation:** Domain 1 (Prompting and Task Execution) sirf 14% hai. Domain 2 (Output Evaluation
and Validation) 21% ke sath sabse bara hai — yeh batata hai credential asal mein kya test karta hai:
prompt likhna nahi, balke **judgment** — jo Claude generate kare usay trust karne se pehle verify
karna.
*(Source: 01-domain-blueprint.md)*

---

### Q2. Sample Question 1 — regulation citation verify karna

**Q:** Claude ek naye regulation ka summary deta hai, ek specific subsection number cite karte hue,
high confidence ke sath. Compliance team ko bhejne se pehle sabse appropriate action?

- As-is bhej do, Claude confident tha
- **Cited subsection ko official regulation text ke against verify karo bhejne se pehle** ✅
- Claude se apni confidence rate karwao, high ho to bhej do
- Summary ko formal reword karo, phir bhej do

**Explanation:** Language models specific-looking details (citation numbers) fabricate kar sakte
hain — hallucination. Self-reported confidence reliable signal nahi hota. Compliance-bound claims ko
authoritative source ke against verify karna zaroori diligence hai.
*(Source: 03-how-to-prepare-and-sample-questions.md — Sample 1, Domain 2)*

---

### Q3. Sample Question 2 — model selection speed vs quality

**Q:** High-volume, short customer-reply drafts chahiye jahan speed aur cost deep-reasoning se zyada
matter karte hain. Sabse best choice?

- Har reply ke liye sabse capable, highest-cost model
- **Ek faster, lower-cost model jo straightforward, high-volume tasks ke liye suited ho** ✅
- Sab product features disable kar do cost kam karne ke liye
- Kisi doosre AI platform pe switch kar jao

**Explanation:** Model selection ko task requirements ke sath align karna hai — straightforward
high-volume kaam ke liye faster/cheaper model, aur sabse capable model complex reasoning ke liye
reserve. Hamesha top model use karna cost/latency budget waste karta hai.
*(Source: 03-how-to-prepare-and-sample-questions.md — Sample 2, Domain 3)*

---

### Q4. Sample Question 3 — sensitive data upload

**Q:** Ek project manager customer names + account numbers wala spreadsheet upload karna chahta hai
trend-analysis ke liye. Policy regulated personal data share karna restrict karti hai. Sabse
appropriate action?

- File as-is upload karo, analysis internal hai
- **Personal identifiers ko remove/anonymize karo upload se pehle, policy ke mutabiq** ✅
- File upload karo lekin Claude ko "retain mat karo" instruct karo
- Analysis poori tarah skip kar do

**Explanation:** Data-sensitivity safeguards ka matlab hai regulated identifiers ko redact/anonymize
karna use se pehle — analysis protected data expose kiye bina proceed ho sakta hai. As-is upload
policy violate karta hai; "retain mat karo" kehna technical control nahi hai.
*(Source: 03-how-to-prepare-and-sample-questions.md — Sample 3, Domain 6)*

---

### Q5. CCAO-F kis role ke liye best fit hai?

**Q:** Ek pre-sales engineer jo Claude adoption advise karta hai lekin khud integration code nahi
likhta, konsa credential uske liye best fit hai?

- CCDV-F (Developer)
- **CCAO-F (Associate) — advising/selling/leading Claude projects ke liye, implementation ke liye
  nahi** ✅
- CCAR-P (Architect Professional)
- Koi bhi credential fit nahi, ek naya banaya jayega

**Explanation:** CCAO-F un logon ke liye on-ramp hai jo Claude adoption influence karte hain bina
integration code likhe — consultants, pre-sales engineers, project managers, adoption leads. Yeh
capabilities/limitations/use-cases/adoption-patterns test karta hai, implementation nahi.
*(Source: parent 02-stage-two-anthropic.md — "CCAO-F")*

---

### Q6. CCAO-F Claude Partner Network tier eligibility mein count hota hai?

**Q:** Ek organisation apni Partner Network tier badhana chahti hai. Kya CCAO-F certified staff is
count mein shamil hote hain?

- Haan, sab 4 credentials equally count hote hain
- **Nahi — CCAO-F tier eligibility mein count nahi hota; sirf 3 technical credentials (Developer,
  Architect Foundations, Architect Professional) count hote hain** ✅
- Haan, lekin sirf agar 10+ log pass karein
- Nahi, koi bhi credential count nahi hota

**Explanation:** CCAO-F advisory/selling role ke liye hai, integration-building ke liye nahi — isliye
partner-tier standing (jo deployed customers + technical practitioner counts pe based hai) mein
count nahi hota.
*(Source: parent 02-stage-two-anthropic.md)*

---

### Q7. PCAO-F (Panaversity ka equivalent) kab available hoga?

**Q:** Kya PCAO-F (CCAO-F ka Panaversity-aligned free version) abhi available hai?

- Haan, PCAR-F/PCDV-F ki tarah available hai
- **Nahi — PCAO-F "Planned" status mein hai, abhi available nahi (sirf PCAR-F aur PCDV-F available
  hain)** ✅
- Haan, lekin sirf waitlist ke zariye
- PCAO-F kabhi nahi banega, sirf CCAO-F rahega

**Explanation:** Panaversity ke 4 exams mein se sirf 2 (PCAR-F, PCDV-F) launch pe available thay.
PCAO-F aur PCAR-P "Planned" hain — is repo ka current FDE-path focus bhi isi wajah se PCAR-F/PCDV-F
→ CCAR-F/CCDV-F pair par hai, CCAO-F par nahi.
*(Source: parent 01-stage-one-panaversity.md — "Panaversity Ka Poora Framework")*

---

### Q8. "Judgment" is credential ka core kya hai — exact quote?

**Q:** Domain weights dekh kar, CCAO-F asal mein kis cheez ki testing hai?

- Fastest prompt-writer kaun hai
- **Judgment — output evaluate karna, problems spot karna, result pass karne se pehle validate
  karna** ✅
- Sabse zyada Claude features yaad rakhna
- Coding speed

**Explanation:** Domain 2 (21%) + Domain 4 (16%) + Domain 6 (15%) milke exam ka 52% hain — sab
"judgment" domains hain (evaluate, integrate-responsibly, govern), na ke "generate" domains. Yeh
credential ka core signal hai.
*(Source: 01-domain-blueprint.md — top note)*

---

### Q9. Ek associate ko workflow-integration decision (Domain 4) lena hai — kaunsa skill test hota hai?

**Q:** Domain 4 (Workflow Integration and Solution Design, 16%) mein "Claude ki value aur limitations
stakeholders ko communicate karna" bhi shamil hai. Yeh kis tarah ka skill hai?

- Purely technical/coding skill
- **Communication + judgment skill — samajhna Claude kahan fit baithta hai aur kahan nahi, aur woh
  non-technical stakeholders ko explain karna** ✅
- Sirf sales pitch skill, technical accuracy irrelevant
- Sirf CCAR-P mein test hota hai, CCAO-F mein nahi

**Explanation:** Domain 4 "Claude apply karna" aur "existing workflows mein integrate karna" dono
cover karta hai, saath hi limitations ko honestly communicate karna — yeh advisory role ka core hai:
na sirf "kya ho sakta hai" balke "kahan nahi karna chahiye" bhi.
*(Source: 01-domain-blueprint.md — Domain 4)*

---

### Q10. CCAO-F ke practice ke liye is repo mein konsa scaffold hai?

**Q:** CCAO-F judgment-heavy hai, coding-heavy nahi. Is repo mein kaunsa practice format istemal hua
hai?

- Ek pytest-based coding project, jaisa CCDV-F
- **Ek no-code judgment worksheet (`projects/00-judgment-drills/`) — real outputs evaluate karne ki
  practice, code likhne ki nahi** ✅
- Koi practice scaffold nahi hai
- Sirf CCAR-F ke scaffolds reuse hote hain

**Explanation:** CCAO-F ki skill (output evaluation, escalation judgment, governance) code se test
nahi hoti — isliye is repo ka scaffold ek structured worksheet hai jahan candidate real-jaisi Claude
outputs ko evaluate karta hai aur apna reasoning likhta hai, coding scaffold ki bajaye.
*(Source: README.md — Practice, is quiz ke sath add hua)*

---

### Q11. Domain 5 — Project knowledge source stale ho jaye to?

**Q:** Ek team ka Claude Project mein internal policy document knowledge source ke tor par upload hai.
Kuch hafton baad woh document naye version mein update hota hai, lekin Project mein purana hi upload
raha. Sabse appropriate action?

- Kuch nahi karna — Claude khud internet se latest version check kar lega
- **Project ki knowledge source ko manually update karna — purana document naye version se
  replace/remove karna** ✅
- System instructions mein likh dena "hamesha latest policy follow karo"
- Naya Project bana lena har baar jab koi document update ho

**Explanation:** Project ka knowledge source ek static upload hai (jab tak live connector jaise
Google Drive na ho) — Claude khud background mein "latest version" dhoond ke apne aap update nahi
karta. System instructions mein "latest follow karo" likhna sirf ek instruction hai, technical
guarantee nahi: Claude ke paas physically latest document hi na ho to woh follow nahi kar sakta.
Domain 5 ka core skill yahi hai — configurations/knowledge sources ko **maintain/update karna**,
sirf configure karke chhod na dena.
*(Source: 01-domain-blueprint.md — Domain 5)*

---

### Q12. Domain 1 — vague result ko fix karna: flattery vs specification

**Q:** Ek marketing associate types "write something about our new product" aur generic result se
disappointed hai. Sabse effective revision kaunsi hai?

- "Write something better about our new product."
- **"Write a 150-word LinkedIn post announcing our scheduling app to small-business owners;
  friendly, professional tone; end with a waitlist call to action."** ✅
- "Write about our product" repeated three times in a row
- "You are the world's greatest copywriter, with decades of award-winning experience. Write
  something about our product that really captures how great it is."

**Explanation:** Elaborate persona/flattery prompts ("world's greatest copywriter") impressive
lagte hain lekin koi real specification nahi dete — na length, na audience, na tone, na CTA.
Effective prompting (Domain 1) ka matlab concrete task decomposition hai: length + audience + tone
+ call-to-action specify karna, jaisa dusra option karta hai. Sirf "better" likhna ya same vague ask
repeat karna underlying ambiguity door nahi karta.
*(Source: user-provided practice question, Domain 1)*

---

### Q13. Domain 1 — shallow/uneven coverage ko task decomposition se fix karna

**Q:** Ek operations lead ko quarterly review chahiye jo budget variance, project status, staffing,
aur next-quarter risks cover kare. Ek single prompt poori document mangta hai lekin shallow, uneven
coverage deta hai. Kaunsi technique isay fix karti hai?

- Poori document dobara mangna, lekin word count double kar dena
- Claude ko kehna "weak sections par zyada try karo"
- Sirf bullet points mein switch kar dena, taake gaps kam nazar aayein
- **Decompose karna: har section ko apna alag request banana, har ek review karna, phir ek combined,
  consistent draft mangna** ✅

**Explanation:** Complex, multi-part request (4 alag topics) ko ek hi mega-prompt mein daalna
shallow/uneven coverage deta hai — model ka focus sab sections mein barabar bant jata hai. Sahi
technique **task decomposition** hai: har section alag request, phir combine. Word count double
karna, "try harder" kehna, ya bullet points mein chhupana — teeno symptom ko mask karte hain,
underlying complexity fix nahi karte.
*(Source: user-provided practice question, Domain 1)*

---

### Q14. Domain 1 — draft weak ho to specific feedback se iterate karna

**Q:** Claude ka pehla draft (client email) bohot formal hai aur key request final paragraph mein
dab gayi hai. Iterate karne ka sabse effective tareeqa kya hai?

- **Specific feedback dena: "Make it warmer and more conversational, and move the request to
  reschedule into the opening two sentences"** ✅
- Wahi identical prompt dobara bhej dena, "natural variation" pe umeed rakh kar
- Bilkul nayi conversation shuru karna aur original prompt dobara type karna
- Draft ko as-is accept karna aur sab kuch khud manually edit karna

**Explanation:** Prompts iterate karna (Domain 1) ka matlab hai concrete, specific feedback dena —
"tone warm karo" + "request ko opening mein lao". Same prompt dobara bhejna random luck pe depend
karta hai; nayi conversation shuru karna wahi generic starting point deta hai; sab kuch manually
khud edit karna Claude ki iteration capability waste karta hai jabke ek chhoti feedback line kaafi
thi.
*(Source: user-provided practice question, Domain 1)*

---

### Q15. Domain 1 — prompting strategy ko task-type ke hisaab se adapt karna

**Q:** Ek project manager Claude se do alag kaam karwana chahta hai: internal program ke naam
brainstorm karna, aur program ka formal charter draft karna. Prompting strategy in dono mein kaise
alag honi chahiye?

- Dono tasks ke liye identical prompt use karna, kyunki prompting principles universal hote hain
- Brainstorm mein exact formatting rules aur strict limits dena; charter mein maximum creativity
  aur complete structural freedom dena
- **Brainstorm ke liye: bohot saare varied options mangna, judgment defer karna; charter ke liye:
  structure, required sections, tone, aur constraints dena** ✅
- Brainstorming avoid karna, kyunki models original ideas generate nahi kar sakte

**Explanation:** Domain 1 ka ek core objective hai prompting strategy ko task-type ke hisaab se
adapt karna. Brainstorming **divergent** task hai — maqsad hai varied options, judgment baad mein;
strict rules creativity kaat dete hain. Charter drafting **convergent/formal** task hai — structure
+ tone + constraints dene se hi usable, consistent document banta hai; "complete freedom" yahan
uncontrolled result deta hai. Doosra option (B ka reverse) dono tasks ko ulta treat karta hai.
*(Source: user-provided practice question, Domain 1)*

---
[⬅ CCAO-F Index](README.md) · [Scenario version (same content) ➡](05-test-your-understanding.md)
