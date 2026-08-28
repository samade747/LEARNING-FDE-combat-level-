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
[⬅ CCAO-F Index](README.md) · [Scenario version (same content) ➡](05-test-your-understanding.md)
