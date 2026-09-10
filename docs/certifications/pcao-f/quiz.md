# Quiz — PCAO-F: Panaversity Certified Associate, Foundations (Test Your Understanding)

**10-question self-contained assessment**, PCAO-F-specific: Panaversity logistics (attempts, cost,
sequence, rollout) + the CCAO-F blueprint PCAO-F is aligned to (domain weights, "one level up"
framing). Grounded in this folder's `README.md`, the parent chapter's `01-stage-one-panaversity.md`,
aur book page [`/docs/certifications/pcao-f`](https://agentfactory.panaversity.org/docs/certifications/pcao-f)
(Zia Tutor corpus gen 70, re-read 2026-09-11). Domain-level judgment drills yahan **nahi** hain — woh
[`../ccao-f/`](../ccao-f/README.md) folder mein rehte hain (single source of truth). Same 10 questions
[`05-test-your-understanding.md`](05-test-your-understanding.md) mein scenario version ke tor par bhi
hain.

---

### Q1. Panaversity student, PCAO-F 1st attempt — cost?

**Q:** Ek Panaversity student apna pehla PCAO-F attempt de raha hai. Kitna kharch hoga?

- $99, jaisa CCAO-F ka list price
- **Free — Panaversity students ko har exam ke 2 free attempts milte hain; retake aur external
  proctoring fees abhi announce nahi hui** ✅
- Proctoring fee (announced, fixed)
- Free sirf agar PCAR-F bhi ek sath diya jaye

**Explanation:** PCAO-F Panaversity ka apna independently-proctored exam hai, CCAO-F ($99 list,
Anthropic/Pearson VUE) se alag. Panaversity students ko har exam ke pehle 2 attempts free milte hain;
3rd+ retake aur non-student external proctoring ki fee "not announced yet" hai. Do-attempt policy
jaan-boojh kar hai — real second chance, lekin unlimited trial-and-error nahi.
*(Source: README.md — Quick Facts; book page /docs/certifications/pcao-f — "Same Blueprint, One Level Up" table)*

---

### Q2. PCAO-F pehle kyun, PCAR-F baad mein?

**Q:** Kyun PCAO-F ko FDE path mein **pehla** exam rakha gaya hai, PCAR-F se pehle?

- Alphabetical order
- **Judgment foundation hai — agentic system design karne se pehle effective prompting, output
  evaluation, hallucination detection, results validation, governance aana chahiye; PCAR-F ki
  architecture usi judgment par banti hai** ✅
- PCAO-F harder hai isliye warm-up chahiye
- PCAO-F sasta hai isliye pehle diya jata hai

**Explanation:** Book ki progression explicit hai: **"Use AI well → evaluate it correctly → govern it
responsibly → design the system."** PCAO-F pehle do sawal poochta hai (kya aap AI responsibly use +
evaluate kar sakte ho?), PCAR-F teesra (kya aap wo system design kar sakte ho jisme AI chalega?).
Judgment pehle, architecture baad mein.
*(Source: parent 01-stage-one-panaversity.md — "Associate Pehle, Phir Architect"; book page — "After You Pass")*

---

### Q3. PCAO-F ka domain-weight table kahan se aata hai?

**Q:** PCAO-F ke 7 domains aur unke weights kis authority se liye gaye hain?

- Panaversity ka apna independent blueprint, CCAO-F se alag
- **Anthropic ke published CCAO-F blueprint se — usi ke published weights par — phir PCAO-F uske
  aage bhi jata hai (vendor-neutral)** ✅
- CCAR-F ka blueprint
- Har sitting apne weights randomize karti hai

**Explanation:** "PCAO-F takes the same blueprint one level up" — har CCAO-F objective usi published
weight par examine hota hai, phir courses ke sath aage: Claude aur ChatGPT side by side, product
surface se upar. Isi liye poora objective-level detail seedha [`../ccao-f/01-domain-blueprint.md`](../ccao-f/01-domain-blueprint.md)
mein hai, yahan duplicate nahi.
*(Source: book page — "Same Blueprint, One Level Up"; README.md — Domain Weights)*

---

### Q4. Sabse bara domain kaunsa hai — aur "Prompting" kahan aata hai?

**Q:** PCAO-F / CCAO-F blueprint ka sab se bara-weight domain kaunsa hai?

- Prompting and Task Execution (sab se bara, kyunke prompt likhna core skill hai)
- **Output Evaluation and Validation (21%) — sab se bara; Prompting sirf 14% hai. Domain 2 + 4 + 6
  (Evaluation + Workflow Integration + Governance) = exam ka 52%** ✅
- Governance, Risk, and Responsible Use (25%)
- Troubleshooting and Optimization

**Explanation:** Credential ki thesis ek number mein: sab se bhaari domain wo hai jo aap **answer ke
sath karte ho** — check karna, hallucination pakadna, decide karna ke yeh case human sign karega ya
nahi. Prompt likhna nahi. Domain-weighted study ka matlab: Evaluation ko sab se zyada time, Prompting
ko usse kam.
*(Source: book page — "What It Tests"; README.md — Domain Weights)*

---

### Q5. PCAO-F mein per-domain minimum score hota hai?

**Q:** Ek candidate ka total scaled score 780 hai (pass), lekin Governance domain mein sirf 55%
correct. Kya woh fail ho jayega?

- Haan — har domain mein alag se 720-equivalent chahiye
- **Nahi — result sirf total scaled score vs cut score 720 hai; koi per-domain minimum nahi. Ek
  weak domain akela fail nahi kar sakta** ✅
- Haan, agar koi domain 60% se neeche ho
- Score report domain breakdown deta hi nahi

**Explanation:** Score report domain-wise percent-correct dikhata hai, lekin guide explicit hai ke woh
section percentages pass/fail decide **nahi** karte. Phir bhi: strong total jo ek patli area chhupa
raha ho — wohi profile hai jiski fikar karni chahiye, kyunke agle question draw pe wohi domain
zyada aa sakta hai.
*(Source: book page — "What It Tests" → ":::note There is no per-domain minimum")*

---

### Q6. PCAO-F pass karne se employer-verifiable credential milta hai?

**Q:** Ek recruiter kisi candidate ka PCAO-F pass Anthropic ke official registry mein verify karna
chahta hai. Kya woh kar sakta hai?

- Haan — PCAO-F aur CCAO-F ek hi registry mein hain
- **Nahi — CCAO-F wo credential hai jo employer Anthropic ke sath verify karta hai. PCAO-F ek
  readiness gate + FDE Internship qualification hai, registry entry nahi** ✅
- Haan, lekin sirf 90 din tak
- PCAO-F verify hota hai, CCAO-F nahi

**Explanation:** "One honest limit": PCAO-F ek readiness credential aur access gate hai — wo cheez
nahi jo employer Anthropic ke apne registry mein dekhta hai. Gate isliye hai ke Anthropic attempt fee
+ waqt dono kharch karta hai (fail ke baad wait: **14, 30, 90 din**), aur ek sasti same-blueprint
readiness-check un failures se bacha sakti hai.
*(Source: book page — "After You Pass" → "One honest limit"; "Same Blueprint, One Level Up" — gate rationale)*

---

### Q7. External candidate, kabhi enrolled nahi — PCAO-F de sakta hai?

**Q:** Ek consultant jo kabhi Panaversity course mein enrolled nahi raha, PCAO-F sit karna chahta
hai. Kaise?

- Nahi — sirf enrolled students eligible hain
- **Haan — enrolled nahi ho to ek attempt buy karo aur one-on-one proctoring ke sath sit karo;
  enrolled ho to attempt free hai aur teacher ke sath arrange karte ho** ✅
- Haan, lekin pehle CCAO-F dena zaroori hai
- Haan, lekin sirf Pakistan ke candidates

**Explanation:** Do routes hain ek seat tak: matching Panaversity course mein enrolled → free, teacher
ke sath arrange; enrolled nahi → attempt khareedo, independent one-on-one proctoring. Enrollment sirf
**free attempts** ka criterion hai, exam access ka nahi.
*(Source: book page — "Schedule Your Exam")*

---

### Q8. PCAO-F pass hone ke baad seedha Anthropic se CCAO-F register kar sakte ho?

**Q:** Candidate ne PCAO-F pass kar liya. Ab woh seedha Anthropic Partner Academy se CCAO-F register
kar sakta hai?

- Haan, PCAO-F pass hi kaafi hai
- **Nahi — Anthropic registration ke liye eligible organisational account chahiye (individual
  sign-up route hai hi nahi). PCAO-F + PCAR-F dono pass → FDE Internship Program → Panaversity
  qualifying participants ki registration mein assist karta hai** ✅
- Haan, lekin sirf $99 fee ke sath
- Nahi — pehle PCDV-F bhi dena zaroori hai

**Explanation:** Internship mechanically bhi matter karti hai: Anthropic ke paas abhi koi individual
sign-up nahi, sirf organisational account. Panaversity qualification stage (PCAO-F → PCAR-F) complete
karne se FDE Internship unlock hoti hai, aur wahan se Anthropic registration mein assist milta hai.
Anthropic pair baithna phir bhi **optional** hai.
*(Source: book page — "After You Pass"; parent 01-stage-one-panaversity.md — sequence diagram)*

---

### Q9. "One level up" ka matlab — Governance domain ka example do

**Q:** CCAO-F ke Governance domain ko PCAO-F kaise "ek level upar" le jata hai?

- Same question, sirf Roman Urdu mein
- **Ek vendor ki acceptable-use / usage policy yaad karne ki jagah — regulated client mein jo
  governance obligation aap carry karte ho, wo. Product surface se upar, vendor framing ke baghair** ✅
- Governance domain PCAO-F mein hai hi nahi
- Sirf Anthropic ke connectors ki permissions

**Explanation:** Yehi pattern har domain pe: product-and-model-selection → 3 model names ki jagah
"class of decision" (speed ka cost, long context ka cost, session restart vs stretch);
configuration/knowledge → ek product ka Projects panel ki jagah instruction + knowledge layer in
general; governance → ek vendor ki AUP ki jagah regulated-client obligation. Upar professional layer:
client ko batana ke system kya **nahi** karega, is se pehle ke woh khud pata karein.
*(Source: book page — "What It Tests" (Panaversity sitting extensions); README.md — "Same Blueprint, One Level Up")*

---

### Q10. Sample exam kab, aur kya woh attempt consume karta hai?

**Q:** PCAO-F ka Panaversity sample exam kab available hua, aur usay dena real attempt kharch karta
hai?

- Sample exam hai hi nahi — pehla real attempt hi practice hai
- **Sample 10 September 2026 se free available; proctored PCAO-F 18 September 2026 se live. Sample
  attempt consume nahi karta — pehle wohi do** ✅
- Sample dena 1 free attempt kharch karta hai
- Sample sirf 18 September ke baad khulta hai

**Explanation:** Sequence: **pehle free sample (10 Sep), phir proctored exam (18 Sep se)** — real
attempt kharch karne se pehle weak areas discover karo. Alag caveat: CCAO-F guide ke apne sample
questions **live item bank se nahi** aate — sirf question ki shape dikhate hain, content nahi; unhe
leaked items ki tarah mat parho.
*(Source: book page — "Sit a Sample First", "Schedule Your Exam", "The Anthropic Twin" → footnotes; README.md — Rollout Dates)*

---
[⬅ PCAO-F Index](README.md) · [Scenario version (same content) ➡](05-test-your-understanding.md)
