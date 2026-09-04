# 08 — Teaching Walkthrough (Roman Urdu, Domain-by-Domain)

*Yeh file un `05`/`06`/`07` se alag hai — woh test/cram-format hain, yeh **concept-teaching** format hai:
har domain ka plain Roman Urdu walkthrough (jaisa Zia Tutor AI padhata), phir scenario-based
brainstorming questions (MCQ nahi — open reasoning, taaki aap khud apni class ko sikha sakein).
Blueprint order mein chalta hai ([01-domain-blueprint.md](01-domain-blueprint.md) se grounded).
Answers khud likho, phir agla domain maango — is file mein reference-answers baad mein add hongi jab
aap apne jawab de dein.*

---

## Domain 1 — Prompting and Task Execution (14%)

CCAO-F ka pehla domain sabse chhota weight (14%) rakhta hai — is wajah se bhi ke yeh sabse "obvious"
skill hai: acha prompt likhna. Lekin exam yahan sirf yeh nahi dekhta ke aap fancy prompt likh sakte ho
— yeh dekhta hai ke aap **task ko sahi tarah decompose aur adapt** kar sakte ho.

Teen core ideas:

1. **Effective prompting** — ek achha business prompt teen cheezein deta hai jo Claude khud guess
   nahi kar sakta: **audience** (kaun parhega), **format** (kis shape mein chahiye), aur **goal** (kis
   decision ko feed karega). "Write something about our product" fail isliye hota hai kyunki teenon
   missing hain — lambi prompt ya persona add karne se bhi fix nahi hota jab tak yeh teen cheezein na
   aayein.

2. **Task decomposition** — jab ek request mein multiple parts hon (jaise quarterly review: budget +
   status + staffing + risks), to ek hi mega-prompt shallow output deta hai. Sahi approach: har part
   ko apna focused prompt do, phir combine karo. Yeh wahi principle hai jo harness-engineering mein
   "sub-tasks" ke roop mein aata hai — same logic, business-writing context mein.

3. **Adapting strategy by task type** — yeh sabse zyada test hota hai. **Divergent tasks**
   (brainstorming) mein loose constraints, zyada options chahiye. **Convergent tasks** (drafting,
   analysis) mein tight structure, format, tone chahiye. Ek associate jo dono ko same tarah prompt
   karta hai — woh galat hai, chahe prompt "acha" hi kyun na ho.

**Iteration** bhi isi domain ka hissa hai: pehla draft kabhi perfect nahi hota. Sahi move specific
feedback dena hai ("zyada casual karo, request ko pehle paragraph mein lao"), poora naya prompt likhna
ya manually rewrite karna nahi.

### Scenario Brainstorming — Domain 1

1. Ek HR associate Claude se poochta hai: "policy document ka summary do." Output generic aur kaam
   ka nahi. **Aap iss associate ko kya 3 sawal poochne ko kahoge taaki woh apna prompt improve kare?**

2. Ek marketing lead ek hi din mein Claude se do kaam leta hai: (a) 20 naye taglines brainstorm
   karna, (b) final launch email draft karna. **Dono ke liye prompting strategy mein kya farq hoga —
   specifically kaunsi cheez "loose" rakhoge aur kaunsi "tight"?**

3. Ek associate complain karta hai ke "Claude ka pehla draft hamesha ghalat hota hai, mujhe har baar
   poora naya prompt likhna padta hai." **Yeh unka misconception kahan hai, aur aap unhe iteration ka
   sahi tareeka kaise sikhaoge — ek concrete example ke sath?**

*(Aapke jawab: abhi pending — likh kar bhejo, phir yahan reference answers add hongi.)*

---

## Domain 2 — Output Evaluation and Validation (21%) — 🔲 Agla

## Domain 3 — Product and Model Selection (12%) — 🔲

## Domain 4 — Workflow Integration and Solution Design (16%) — 🔲

## Domain 5 — Configuration and Knowledge Management (12%) — 🔲

## Domain 6 — Governance, Risk, and Responsible Use (15%) — 🔲

## Domain 7 — Troubleshooting and Optimization (10%) — 🔲

---
[⬅ CCAO-F Index](README.md) · [01 — Domain Blueprint](01-domain-blueprint.md)
