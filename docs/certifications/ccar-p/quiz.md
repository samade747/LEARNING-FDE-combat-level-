# Quiz — CCAR-P: Claude Certified Architect, Professional (Test Your Understanding)

**10-question self-contained assessment**, grounded in `01-domain-blueprint.md` (7 domains) and
`03-how-to-prepare-and-sample-questions.md` (3 official sample questions). Same 10 questions also
live in [`05-test-your-understanding.md`](05-test-your-understanding.md) as the scenario version.

---

### Q1. CCAR-P ka sabse bara domain kaunsa hai?

**Q:** CCAR-P ke 7 domains mein sabse zyada weight kis par hai?

- Solution Design & Architecture (17%)
- **Integration (19%) — RAG pipeline design, observability at scale, protocol selection (MCP vs
  API/CLI vs agent-to-agent) sameet, CCAR-F ke "Tool Design & MCP" se wider scope** ✅
- Evaluation, Testing & Optimization (16%)
- Governance, Safety & Risk Management (14%)

**Explanation:** Integration 19% ke sath sabse bara domain hai — CCAR-F ke 18%-weight "Tool Design &
MCP Integration" ka professional-level, wider-scope version.
*(Source: 01-domain-blueprint.md)*

---

### Q2. CCAR-F mein bilkul na hone wale 2 domains kaunse hain?

**Q:** CCAR-P mein kaunse 2 domains hain jo CCAR-F mein bilkul cover nahi hote, aur inka combined
weight kya hai?

- Solution Design + Integration, 36%
- **Governance/Safety/Risk Management (14%) + Stakeholder Communication/Lifecycle Management (14%)
  = 28% — CCAR-F mein stakeholder-facing ya regulatory-compliance skills bilkul test nahi hote** ✅
- Models/Prompting + Dev Productivity, 20%
- Koi naya domain nahi, sab CCAR-F se overlap karta hai

**Explanation:** CCAR-F sirf "hooks ke through guardrails" tak scope tha — CCAR-P explicit regulatory
compliance (GDPR/HIPAA/FedRAMP) aur poori stakeholder-lifecycle (discovery se iteration tak) add
karta hai.
*(Source: 01-domain-blueprint.md — "CCAR-F Se Farq")*

---

### Q3. Sample Question 1 — least privilege

**Q:** Ek support agent read tickets, draft replies, refunds issue, aur accounts delete kar sakta
hai. Support staff ko sirf pehle 2 chahiye. Least-privilege ke hisaab se sabse risk-reducing change?

- Refund/delete tools mein logging add karo audit ke liye
- **Refund aur delete tools ko agent ke configuration se poori tarah remove karo** ✅
- Sab tools rakho lekin confirmation prompt add karo
- Bara model use karo jo instructions zyada reliably follow kare

**Explanation:** Least privilege ka matlab hai capabilities remove karna, sirf monitor/guard karna
nahi — attack surface eliminate karo. Logging/confirmation detective controls hain, removal nahi.
Model size authorization scope se unrelated hai.
*(Source: 03-how-to-prepare-and-sample-questions.md — Sample 1, Domain 3)*

---

### Q4. Sample Question 2 — prompt caching

**Q:** Har request pe wahi 8,000-token system prompt + policy bhejta hai, phir chhota varying user
message. Latency aur cost dono concern hain. Sabse directly-addressing optimization?

- Policy document ko 1,000 tokens tak truncate karo
- Task-fit se qatai matlab na rakhte hue sabse chhota model pe switch karo
- **Static content ko pehle rakho aur prompt caching enable karo** ✅
- Policy document ko few-shot example block mein move karo

**Explanation:** Stable content ko pehle order karke prompt caching enable karna repeated prefixes
reuse hone deta hai — time-to-first-token aur cost dono kam. Truncation zaroori policy kho deta hai;
downsizing quality risk karta hai; few-shot relocate karna cacheable prefix nahi banata.
*(Source: 03-how-to-prepare-and-sample-questions.md — Sample 2, Domain 2)*

---

### Q5. Sample Question 3 — RAG regression

**Q:** Document refresh ke baad RAG system confident-lekin-galat answers dena shuru karta hai,
latency + model version unchanged. Sabse pehle investigate karne ki jagah?

- Model weights silently change ho gaye
- **Retrieval/indexing step irrelevant ya stale chunks return kar raha hai** ✅
- Temperature setting bohat kam hai
- Context window shrink ho gaya

**Explanation:** Document-refresh trigger + unchanged model/latency retrieval ko point karta hai
(broken re-index, mismatched embeddings) — baaqi options specifically document-refresh se trigger
nahi hote.
*(Source: 03-how-to-prepare-and-sample-questions.md — Sample 3, Domain 4)*

---

### Q6. CCAR-P kaun le, CCAR-F pass karne ke baad?

**Q:** Ek architect CCAR-F pass kar chuka hai aur ab senior, end-to-end solution ownership role mein
hai. Kya CCAR-P uske liye relevant hai?

- Nahi, CCAR-F kaafi hai har role ke liye
- **Haan — CCAR-P professional capstone hai, senior architects ke liye jo solution ka ownership
  discovery se lifecycle-iteration tak rakhte hain, stakeholder communication sameet** ✅
- Nahi, CCAR-P sirf managers ke liye hai, architects ke liye nahi
- Haan, lekin CCAR-F ka koi prerequisite nahi hai (technically), lekin content overlap 100% hai

**Explanation:** CCAR-P CCAR-F ke content ko extend karta hai — "everything in CCAR-F mapping still
applies," plus stakeholder-comm/lifecycle/governance jo CCAR-F mein nahi hai. Ownership ka scope
CCAR-F se bara hai.
*(Source: parent 02-stage-two-anthropic.md — "CCAO-F / CCAR-P" section)*

---

### Q7. Domain 7 (Dev Productivity) itna halka (7%) kyun hai?

**Q:** CCAR-P ka sabse chhota domain "Developer Productivity & Operational Enablement" (7%) hai. Study
priority is bare-ke-hisaab-se rank karte waqt yeh kahan aata hai?

- Sabse pehle, kyunke practical hai
- **Sabse aakhir mein — study priority table isay explicitly "sab se halka" bataata hai, baaqi 6
  domains (Integration se leke Models/Prompting tak) pehle aate hain** ✅
- Skip kar sakte ho, exam mein nahi aata
- Equal weight, sab domains ko barabar time do

**Explanation:** Study priority: Integration (19%) → Solution Design (17%) → Evaluation (16%) →
Governance+Stakeholder-Comm (28% combined) → Models/Prompting (13%) → Dev Productivity (7%, sab se
halka).
*(Source: 01-domain-blueprint.md — "Study priority")*

---

### Q8. CCAR-P Claude Partner Network tier eligibility mein count hota hai?

**Q:** CCAR-P certified staff Partner Network tier standing mein count hote hain?

- Nahi, sirf CCAR-F aur CCDV-F count hote hain
- **Haan — teen technical credentials (Developer Foundations, Architect Foundations, Architect
  Professional) tier standing mein count hote hain, CCAO-F ke ulat** ✅
- Nahi, koi bhi credential count nahi hota
- Haan, lekin sirf senior architects ke liye jo 5+ saal experience rakhte hain

**Explanation:** CCAR-P teen technical credentials mein se ek hai jo partner-tier count karte hain —
CCAO-F (advisory role) alag hai, count nahi hota.
*(Source: parent 02-stage-two-anthropic.md)*

---

### Q9. CCAR-P ke practice projects kahan hain?

**Q:** CCAR-P ke 3 sample questions practice karne ke liye is repo mein konsa scaffold hai?

- Koi scaffold nahi, sirf notes hain
- **`docs/certifications/ccar-p/projects/00-professional-scenarios/` — teenon sample questions
  (least-privilege, cache-aware ordering, RAG diagnosis) directly implement karta hai, 6 offline
  pytest tests** ✅
- Sirf CCAR-F ke scaffolds, CCAR-P ke apne koi nahi
- Har candidate ko khud se design karna padta hai

**Explanation:** CCAR-P ka apna scaffold CCAR-F ke 5 scaffolds ke sath complement karta hai (CCAR-F
foundation practice + CCAR-P professional-scenario practice), duplicate nahi.
*(Source: projects/README.md, is quiz ke sath add hua)*

---

### Q10. CCAR-P ka pass score aur validity CCAR-F se alag hai?

**Q:** CCAR-P ka passing score aur credential validity CCAR-F se different hai?

- Haan, CCAR-P ka pass score 800/1000 hai (zyada strict)
- **Nahi — dono ka pass score 720/1000 hai, validity 12 months hai; sirf price ($175 vs $125) aur
  question count (63 vs 60) alag hain** ✅
- Haan, CCAR-P ki validity 24 months hai (senior role hone ki wajah se)
- Dono exams mein koi renewal nahi hota, life-time valid hai

**Explanation:** Sab 4 Anthropic exams shared mechanics use karte hain: proctored, 120 minutes, 100-
1000 scale, 720 cut score, 12-month validity. Sirf price aur question count exam-specific hain.
*(Source: parent 02-stage-two-anthropic.md — "Exam Mechanics — Sab Exams Shared Hain")*

---
[⬅ CCAR-P Index](README.md) · [Scenario version (same content) ➡](05-test-your-understanding.md)
