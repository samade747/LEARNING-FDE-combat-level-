# 08 — Glossary + Limits + Where This Leads + Appendix

## Plain-English Glossary

- **Delegation criteria** — 4 screens jo decide karte AI kaam kare ya nahi: reversibility,
  consequence of error, human judgment/empathy, accountability
- **Three answers** — fully appropriate, appropriate with review, inappropriate
- **Defined gate** — review jo naam karti kaun reviews, kya verify karta, kab
- **Deciding factor** — screen jo actually classification carry karti
- **Accountability** — kaun outcome ke liye jawabdeh rehta — tool par move nahi hoti
- **Diligence gap** — policy require karti aur log actually karte uske beech ki distance
- **Data tier** — label kitni carefully info handle honi chahiye (green/yellow/red)
- **Entry point** — route jisse data AI system mein jaati (chat/project/connector/API/upload)
- **API** — direct software-to-software link, chat window ke bina
- **Purpose** — data pehli baar collect karne ka reason — naya use usi reason ya fresh permission
  se covered hona chahiye
- **Redaction** — fields hatana jo task ko nahi chahiye, data pahunchne se pehle
- **Pseudonymized** — identifiers labels se replaced, par reconnect karne ka tareeqa exist karta
- **Anonymized** — organization/law ke standard se ab person identify nahi karti
- **Scopes** — exact list jo connector ko karne dete — grant+narrow kar sakte; Skills ke pass
  nahi hoti
- **The five checks** — source, reach, fit, outside content, actions
- **Prompt injection** — misleading instructions content ke andar jo AI parhti, usay steer karne
  ke liye
- **Least privilege** — insaan/service/agent ko sirf jo access task ko chahiye wo dena
- **Shadow AI** — work data jo unapproved tools/accounts se guzarta, organization dekh nahi sakti
- **Residual risk** — kya galat ho sakta planned controls design ke mutabiq kaam karne ke baad bhi
- **Governance Record** — 1-page summary (Case/Data/Capability/People/evidence/owner/re-check
  triggers) ek workflow ke liye

## Yeh Course Kya Replace Nahi Karta

- Applicable law/sector regulation
- Organization ki privacy/security/acceptable-use/records/HR/legal/procurement/risk policies
- Client contracts, confidentiality terms, professional obligations
- Formal security assessment
- High-impact systems ka structured model evaluation
- Legal advice (data personal/anonymous/privileged/regulated hai ya nahi)

Yeh practitioners ko batata **kaunsa sawal face kar rahe**, aur sahi owner tak useful reasoning ke
sath pahunchna. Organization ka formal AI management system NIST AI RMF ya ISO/IEC 42001 par bana
ho sakta — yeh 4 questions uska practitioner-slice hain, substitute nahi.

Underlying judgment sharp rakhne ke liye: **How to Think in the AI Era**. Extensions
install+scope karne ke checklist ke liye: **Skills & Connectors**.

## Yeh Book Mein Kahan Le Jata

- **The Case** → autonomy design + human-agent operating model (Human-Agent Teams)
- **The Data** → custody/context/minimization/approved routes (General Agents on the Web, Cowork)
- **The Capability** → tool boundaries/scoped credentials/confirmations/typed actions/audit logs
  (Designing Agent Experiences, Mode 2)
- **The People** → evaluation/disclosure/fairness checks/monitoring/recourse (System of Record ka
  governance layer)
- **Governance Record** → design review/testing/launch criteria/monitoring ka compact input

> AI Fluency na parhi ho to yeh course ke sath parho — AI Fluency achhi delegation sikhati, yeh
> course us delegation ko organization ke andar **defensible aur repeatable** banata.

---

## Appendix A.1 — Managers Ke Liye: Evidence, Residual Risk, Review Quality

Managers/governance-leads/risk-owners jo design baad mein defend karte, unke liye:

**Har important control mein evidence add karo.** "Manager review karta" sirf statement belief
hai jab tak tum dekh na sako review hoti hai aur intended problem catch karti hai. Residual risk
confession nahi hai design fail hone ka — har real control kuch boundary se bahar chhod deta,
usay naam dena hi sahi owner ko decide karne deta acceptable hai ya nahi.

**Review quality review volume se zyada matter karti.** Insaan ne "approve" click kiya isse
workflow safe nahi ban jata. Achhi review ko chahiye: source material, kaafi time, specific risk
dhoondne ko, reject karne ki authority, outcome hard-to-reverse hone se pehle position. Reviewers
sab approve kar dete to pucho control zaroori hai, galat jagah hai, ya perform karna impossible
hai.

**Edge cases sample karo.** Random samples useful hain, high-risk systems ko wahan bhi sample
karna chahiye jahan failure zyada likely/expensive ho: unusual inputs, minority categories,
escalations, low-confidence outputs, exclusions, threshold-ke-qareeb cases.

## Appendix A.2 — Agent Builders Ke Liye: 4 Questions Architecture Ki Tarah

Framework shape change karta jab AI software ke zariye act karta, insaan copy-paste ka wait karne
ke jagah.

- **Case → autonomy level.** Sawal "agent yeh kar sakta" nahi — "task ne kya autonomy earn ki"
  hai. Draft only. Confirmation ke liye action propose karo. Narrow reversible boundary ke andar
  act karo. Akele act karo sirf jahan reliability/monitoring/rollback justify kare.
- **Data → custody aur minimization.** Design karo agent kya parh sakta, data kahan store hoti,
  prompts+logs mein kya jata, kitni der rakhi jati, kaunse sensitive fields agent se pehle exclude
  hote. Users par rely mat karo redact-karna-yaad-rakhne ke liye jo architecture hata sakta hai.
- **Capability → scoped authority.** Narrow credentials, read-only jahan kaafi ho, explicit tool
  allow-lists, consequential actions ke liye confirmation, audit trails, agents ke liye separate
  identities (shared human credentials nahi).
- **People → evaluation aur recourse.** Relevant groups ke across fairness testing, exclusions+
  false-negatives ki review, required jagah meaningful disclosure, consequential outcomes appeal/
  reverse karne ka tareeqa, deployment ke baad monitoring.

> Practitioner framework aur architecture same story bolni chahiye. Governance Record bole
> "human approves before send" par API token confirmation ke bina send kar sakta — architecture
> ne policy already overrule kar di hai.

## Sources

Screening approach AI Fluency Framework (Rick Dakan + Joseph Feller) par based hai, khaas kar
Delegation+Diligence ideas. 3-answer structure, deciding-factor test, route-first data reasoning,
Governance Record — is book ke adaptations hain. Claude examples 2026-09-02 ko Anthropic
documentation ke against re-checked. Anonymized/regulated data ka treatment deliberately
principle-based hai, kyunke jurisdictions+sectors alag legal tests use karte.

(Checked: Zia Tutor AI connector, 2026-10-23.)
