# 05 — Test Your Understanding (Scenario-Based)

CCAR-P-specific assessment — 7-domain blueprint + the 3 official sample questions. Same content as
[`quiz.md`](quiz.md), standalone self-test version.

---

### Q1. CCAR-P ka sabse bara domain kaunsa hai?

**Q:** CCAR-P ke 7 domains mein sabse zyada weight kis par hai?

- Solution Design & Architecture (17%)
- **Integration (19%) — RAG pipeline design, observability at scale, protocol selection sameet** ✅
- Evaluation, Testing & Optimization (16%)
- Governance, Safety & Risk Management (14%)

**Explanation:** Integration 19% ke sath sabse bara domain hai — CCAR-F ke 18%-weight domain ka
professional-level, wider-scope version.
*(Source: 01-domain-blueprint.md)*

---

### Q2. CCAR-F mein bilkul na hone wale 2 domains kaunse hain?

**Q:** CCAR-P mein kaunse 2 domains hain jo CCAR-F mein bilkul cover nahi hote?

- Solution Design + Integration, 36%
- **Governance/Safety/Risk Management (14%) + Stakeholder Communication/Lifecycle Management (14%)
  = 28%** ✅
- Models/Prompting + Dev Productivity, 20%
- Koi naya domain nahi

**Explanation:** CCAR-P explicit regulatory compliance (GDPR/HIPAA/FedRAMP) aur poori stakeholder-
lifecycle add karta hai jo CCAR-F mein nahi hai.
*(Source: 01-domain-blueprint.md — "CCAR-F Se Farq")*

---

### Q3. Sample Question 1 — least privilege

**Q:** Ek support agent read/draft/refund/delete kar sakta hai. Support staff ko sirf pehle 2 chahiye.
Sabse risk-reducing change?

- Refund/delete tools mein logging add karo
- **Refund aur delete tools ko config se poori tarah remove karo** ✅
- Confirmation prompt add karo
- Bara model use karo

**Explanation:** Least privilege ka matlab capabilities remove karna hai, sirf monitor karna nahi.
*(Source: 03-how-to-prepare-and-sample-questions.md — Sample 1, Domain 3)*

---

### Q4. Sample Question 2 — prompt caching

**Q:** Har request pe wahi 8,000-token system prompt + policy, phir chhota varying message. Latency
aur cost dono concern. Sabse directly-addressing optimization?

- Policy document truncate karo
- Sabse chhota model pe switch karo
- **Static content pehle rakho aur prompt caching enable karo** ✅
- Policy ko few-shot block mein move karo

**Explanation:** Stable content ko pehle order karke caching enable karna repeated prefixes reuse
hone deta hai.
*(Source: 03-how-to-prepare-and-sample-questions.md — Sample 2, Domain 2)*

---

### Q5. Sample Question 3 — RAG regression

**Q:** Document refresh ke baad RAG confident-galat answers deta hai, latency + model unchanged.
Sabse pehle investigate karne ki jagah?

- Model weights silently change ho gaye
- **Retrieval/indexing stale ya irrelevant chunks return kar raha hai** ✅
- Temperature bohat kam hai
- Context window shrink ho gaya

**Explanation:** Document-refresh + unchanged model/latency retrieval ko point karta hai.
*(Source: 03-how-to-prepare-and-sample-questions.md — Sample 3, Domain 4)*

---

### Q6. CCAR-P kaun le, CCAR-F pass karne ke baad?

**Q:** Ek architect CCAR-F pass kar chuka hai aur senior ownership role mein hai. Kya CCAR-P relevant
hai?

- Nahi, CCAR-F kaafi hai
- **Haan — CCAR-P professional capstone hai, ownership discovery se lifecycle-iteration tak** ✅
- Nahi, sirf managers ke liye
- Haan, lekin content 100% overlap hai

**Explanation:** CCAR-P CCAR-F ka content extend karta hai, plus stakeholder-comm/lifecycle/
governance jo CCAR-F mein nahi.
*(Source: parent 02-stage-two-anthropic.md)*

---

### Q7. Domain 7 (Dev Productivity) itna halka (7%) kyun hai?

**Q:** Study priority is bare-ke-hisaab-se rank karte waqt Dev Productivity kahan aata hai?

- Sabse pehle
- **Sabse aakhir — explicitly "sab se halka" hai** ✅
- Skip kar sakte ho
- Equal weight sab domains ko

**Explanation:** Study priority: Integration → Solution Design → Evaluation → Governance+Stakeholder
→ Models/Prompting → Dev Productivity (sab se halka).
*(Source: 01-domain-blueprint.md — "Study priority")*

---

### Q8. CCAR-P Claude Partner Network tier eligibility mein count hota hai?

**Q:** CCAR-P certified staff Partner Network tier standing mein count hote hain?

- Nahi, sirf CCAR-F aur CCDV-F
- **Haan — teen technical credentials mein se ek hai, CCAO-F ke ulat** ✅
- Nahi, koi bhi nahi
- Haan, lekin sirf senior architects ke liye

**Explanation:** CCAR-P teen technical credentials mein se ek hai jo partner-tier count karte hain.
*(Source: parent 02-stage-two-anthropic.md)*

---

### Q9. CCAR-P ke practice projects kahan hain?

**Q:** CCAR-P ke 3 sample questions practice karne ke liye konsa scaffold hai?

- Koi scaffold nahi
- **`docs/certifications/ccar-p/projects/00-professional-scenarios/` — 6 offline pytest tests** ✅
- Sirf CCAR-F ke scaffolds
- Har candidate khud design kare

**Explanation:** CCAR-P ka scaffold CCAR-F ke 5 scaffolds ke sath complement karta hai.
*(Source: projects/README.md)*

---

### Q10. CCAR-P ka pass score aur validity CCAR-F se alag hai?

**Q:** CCAR-P ka passing score aur validity CCAR-F se different hai?

- Haan, 800/1000
- **Nahi — dono 720/1000, 12 months; sirf price ($175 vs $125) aur question count (63 vs 60) alag** ✅
- Haan, 24 months
- Koi renewal nahi

**Explanation:** Sab 4 exams shared mechanics use karte hain — sirf price/question-count exam-specific
hain.
*(Source: parent 02-stage-two-anthropic.md — "Exam Mechanics")*

---
[⬅ CCAR-P Index](README.md) · [Quiz (same content) ➡](quiz.md)
