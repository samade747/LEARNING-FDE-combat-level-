# 05 — Test Your Understanding (Scenario-Based)

PCAO-F-specific assessment — Panaversity logistics (attempts, cost, sequence, rollout) + the CCAO-F
blueprint PCAO-F is aligned to ("same blueprint, one level up"). Same content as [`quiz.md`](quiz.md),
standalone self-test version. Domain-level judgment drills [`../ccao-f/`](../ccao-f/README.md) folder
mein hain, yahan nahi.

---

### Q1. Panaversity student, PCAO-F 1st attempt — cost?

**Q:** Ek Panaversity student apna pehla PCAO-F attempt de raha hai. Kitna kharch hoga?

- $99, jaisa CCAO-F ka list price
- **Free — Panaversity students ko har exam ke 2 free attempts milte hain; retake aur external
  proctoring fees abhi announce nahi hui** ✅
- Proctoring fee (announced, fixed)
- Free sirf agar PCAR-F bhi ek sath diya jaye

**Explanation:** PCAO-F Panaversity ka apna independently-proctored exam hai, CCAO-F ($99 list,
Anthropic/Pearson VUE) se alag. Students ko pehle 2 attempts free; 3rd+ retake aur non-student
proctoring fee "not announced yet".
*(Source: README.md — Quick Facts; book page /docs/certifications/pcao-f)*

---

### Q2. PCAO-F pehle kyun, PCAR-F baad mein?

**Q:** Kyun PCAO-F ko FDE path mein **pehla** exam rakha gaya hai?

- Alphabetical order
- **Judgment foundation hai — prompting, output evaluation, hallucination detection, results
  validation, governance PCAR-F ki architecture se pehle aani chahiye** ✅
- PCAO-F harder hai isliye warm-up chahiye
- PCAO-F sasta hai isliye pehle

**Explanation:** Book ki progression: **"Use AI well → evaluate it correctly → govern it responsibly
→ design the system."** Judgment pehle, architecture baad mein.
*(Source: parent 01-stage-one-panaversity.md — "Associate Pehle, Phir Architect")*

---

### Q3. PCAO-F ka domain-weight table kahan se aata hai?

**Q:** PCAO-F ke 7 domains aur weights kis authority se?

- Panaversity ka apna independent blueprint
- **Anthropic ke published CCAO-F blueprint se — usi ke published weights par — phir aage
  (vendor-neutral)** ✅
- CCAR-F ka blueprint
- Har sitting apne weights randomize karti hai

**Explanation:** "Same blueprint one level up" — har CCAO-F objective usi weight par, phir Claude aur
ChatGPT side by side. Objective-level detail [`../ccao-f/01-domain-blueprint.md`](../ccao-f/01-domain-blueprint.md).
*(Source: book page — "Same Blueprint, One Level Up")*

---

### Q4. Sabse bara domain kaunsa hai — aur "Prompting" kahan aata hai?

**Q:** Blueprint ka sab se bara-weight domain?

- Prompting and Task Execution
- **Output Evaluation and Validation (21%) — sab se bara; Prompting sirf 14%. Domain 2 + 4 + 6 =
  52% of exam** ✅
- Governance, Risk, and Responsible Use (25%)
- Troubleshooting and Optimization

**Explanation:** Sab se bhaari domain wo hai jo aap answer ke sath karte ho — check, hallucination
pakadna, "yeh human sign karega?". Prompt likhna nahi.
*(Source: book page — "What It Tests")*

---

### Q5. PCAO-F mein per-domain minimum score hota hai?

**Q:** Total scaled score 780 (pass), lekin Governance mein sirf 55% correct. Fail?

- Haan — har domain mein alag se 720-equivalent chahiye
- **Nahi — sirf total scaled score vs 720; koi per-domain minimum nahi** ✅
- Haan, agar koi domain 60% se neeche
- Score report domain breakdown deta hi nahi

**Explanation:** Section percentages pass/fail decide nahi karte. Phir bhi strong total jo ek patli
area chhupa raha ho — wohi risky profile hai agle question draw pe.
*(Source: book page — "What It Tests" → ":::note There is no per-domain minimum")*

---

### Q6. PCAO-F pass karne se employer-verifiable credential milta hai?

**Q:** Recruiter PCAO-F pass Anthropic registry mein verify karna chahta hai. Ho sakta hai?

- Haan — PCAO-F aur CCAO-F ek hi registry mein
- **Nahi — CCAO-F wo credential hai jo employer Anthropic ke sath verify karta hai; PCAO-F readiness
  gate + FDE Internship qualification hai** ✅
- Haan, lekin sirf 90 din tak
- PCAO-F verify hota hai, CCAO-F nahi

**Explanation:** "One honest limit": PCAO-F access gate hai, registry entry nahi. Gate isliye — Anthropic
fail ke baad wait **14 / 30 / 90 din**, aur ek sasti same-blueprint check un failures se bacha sakti hai.
*(Source: book page — "After You Pass" → "One honest limit")*

---

### Q7. External candidate, kabhi enrolled nahi — PCAO-F de sakta hai?

**Q:** Consultant jo kabhi enrolled nahi raha, PCAO-F kaise sit karega?

- Nahi — sirf enrolled students eligible
- **Haan — enrolled nahi: attempt buy karo + one-on-one proctoring; enrolled: free, teacher ke sath
  arrange** ✅
- Haan, lekin pehle CCAO-F dena zaroori
- Haan, lekin sirf Pakistan ke candidates

**Explanation:** Enrollment sirf **free attempts** ka criterion hai, exam access ka nahi.
*(Source: book page — "Schedule Your Exam")*

---

### Q8. PCAO-F pass hone ke baad seedha Anthropic se CCAO-F register?

**Q:** PCAO-F pass — ab seedha CCAO-F register kar sakta hai?

- Haan, PCAO-F pass hi kaafi hai
- **Nahi — Anthropic ko eligible organisational account chahiye (koi individual sign-up nahi). PCAO-F
  + PCAR-F dono → FDE Internship → Panaversity registration mein assist karta hai** ✅
- Haan, lekin sirf $99 fee ke sath
- Nahi — pehle PCDV-F bhi zaroori

**Explanation:** Internship mechanically matter karti hai: Anthropic ke paas individual sign-up nahi.
Qualification stage complete → internship → registration assist. Anthropic pair optional.
*(Source: book page — "After You Pass"; parent 01-stage-one-panaversity.md — sequence diagram)*

---

### Q9. "One level up" ka matlab — Governance domain ka example

**Q:** CCAO-F ke Governance domain ko PCAO-F kaise "ek level upar" le jata hai?

- Same question, sirf Roman Urdu mein
- **Ek vendor ki acceptable-use policy yaad karne ki jagah — regulated client mein jo governance
  obligation aap carry karte ho, wo. Product surface se upar** ✅
- Governance domain PCAO-F mein hai hi nahi
- Sirf Anthropic ke connectors ki permissions

**Explanation:** Har domain pe yehi: model names → "class of decision"; ek product ka Projects panel →
instruction + knowledge layer in general; vendor AUP → regulated-client obligation. Upar professional
layer: client ko pehle batao system kya **nahi** karega.
*(Source: book page — "What It Tests" (Panaversity sitting extensions))*

---

### Q10. Sample exam kab, aur kya woh attempt consume karta hai?

**Q:** PCAO-F ka Panaversity sample kab, aur real attempt kharch karta hai?

- Sample exam hai hi nahi
- **Sample 10 September 2026 se free; proctored PCAO-F 18 September 2026 se live. Sample attempt
  consume nahi karta — pehle wohi do** ✅
- Sample dena 1 free attempt kharch karta hai
- Sample sirf 18 September ke baad khulta hai

**Explanation:** Pehle free sample (10 Sep), phir proctored (18 Sep se). Alag caveat: CCAO-F guide ke
apne sample questions live item bank se nahi aate — sirf shape dikhate hain, content nahi.
*(Source: book page — "Sit a Sample First", "The Anthropic Twin" → footnotes)*

---
[⬅ PCAO-F Index](README.md) · [Quiz (same content) ➡](quiz.md)
