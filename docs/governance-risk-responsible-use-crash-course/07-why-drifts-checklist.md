# 07 — Kyun Governance Drift Hoti + Daily Checklist + Record Finish Karna

## Kyun Governance Drift Hoti

High-stakes decisions usually attention paati, sab jaante important hain. **Routine decisions
zyada dangerous hain** — har ek itni chhoti feel hoti ke count karna bhool jate.

Insaan thodi easier tool use karta. Human review glance ban jati. Connector permission rakhti
rehti project change hone ke baad. Sensitive field ek dataset mein dikhne lagti jahan pehle nahi
thi. **Koi ek moment program-level failure nahi lagta — risk wo distance hai jo intended process
aur actual process ke beech build hoti.**

**Diligence gap** = distance jo policy require karti aur log actually karte uske beech. Naam AI
Fluency Framework ki Diligence se aata (AI kaise use hui+output se kya hua uski responsibility
lena). Team scale par matlab: **log actually kya karte audit karo, policy follow ho rahi assume
mat karo.**

## 8.1 — Usage Audit Chalao

Lightweight team audit yeh answer kare:

- Kaunse AI workflows actually use mein hain?
- Kaunsa data actually unse guzar raha?
- Kya defined human gates really chali?
- Kaunse naye tools/Skills/connectors/permissions add hue?
- Model/feature/route/data/audience mein kya change hua?

**Example:** Team lead ek mahine ki AI use review karta, 3 gaps milte: marketer ne unreleased
product spec unapproved entry point par upload ki; ek Skill bina source-check enable hui; client
report ne 2 baar review gate skip ki deadline pressure mein. **Kuch malicious nahi tha — sab
drift tha.** Fixes habit-level hain: approved entry points ka reminder, Project setup mein
Skill-vetting step built-in, review gate non-negotiable treat karna.

Small quarterly sample reasonable start hai, rollout ke waqt ya gaps milne ke baad zyada frequent.

## 8.2 — Process Audit Karo, Person Nahi

Governance audit hidden performance review ban jaye to log auditors ko sirf cleanest work
dikhate. Organization behavior samajhna miss kar deti. **Purpose: system gaps dhoondna** —
confusing rules, unnecessary friction, weak gates, stale permissions, bina-review-badhi practices.

## 8.3 — Friction Rule

Approved path 10 steps leta, unapproved path 1 step leta to deadline-pressure-wale log 1-step
route dhoond lenge. **Shadow AI** = work data jo unapproved tools/accounts se guzarta jo
organization dekh nahi sakti.

Yeh policy-violation ko excuse nahi karta — **usability ko control system ka hissa treat karna
hai.** "Friction hatao, tooling nahi" — slow approved path fix karo, tools mat hatao.

Repeated workarounds milein to pucho: _"Approved tareeqa unsafe tareeqe se harder kyun hai?"_ —
usay fix karna ek aur reminder email se zyada risk kam karta.

## 8.4 — Jab Koi AI Policy Na Ho

Organization ke pass AI policy nahi hai to khud ek invent mat karo aur official kar ke present mat
karo. **Interim proposal likho** sahi owner endorse kare. 1-page start:

- approved AI products + specific routes
- data types jinhe use se pehle confirmation chahiye (short list)
- external/consequential outputs ke liye human-gate rule
- naye Skills/connectors/high-authority tools ke liye review rule
- 1 named role/channel sawal+incidents ke liye

Regulated environments mein yeh guide legal/compliance/security/privacy/contractual approval ka
substitute nahi hai.

## 8.5 — Workflow Change Hone Par Dobara Check Karo

Calendar reminders help karte, **change stronger trigger hai.** Governance Record dobara check
karo jab yeh change hon: model/model family; AI product feature/retention behavior; connector/
Skill/plugin/permission/action; data type/sensitivity; outside content ka source; affected
audience/population; error ka consequence; law/policy/contract/vendor terms.

"Pichle saal approved hui" review skip karne ka reason nahi hai agar jo approve hua wo ab same
cheez nahi hai.

---

## Recap: One-Minute Checklist

Meaningful work se pehle chalao:

| Question | Quick Check | Middle Answer Ko Chahiye | Jo Trap Catch Karti |
|---|---|---|---|
| Case | AI yeh task responsibly kar sakta? | Defined human gate: kaun/kya/kab | "Insaan review karega" bina loop defined |
| Data | Yeh info is route se jaa sakti? | Control, kam data, ya confirmed approved route | Privacy mode ko permission maanna, ya pattern-se-hone-wala kaam chhodna |
| Capability | Yeh tool/authority enable honi chahiye? | Specific security/admin review sawal | Extension sirf jo description bolti wohi kar sakti maanna |
| People | Yeh logon ko affect karti ya disclosure chahiye? | Fairness check, disclosure, ya escalation | Sirf jo AI ne select kiya review karna, jo excluded kiya nahi |

**Sab 4 ke neeche ek trap hai:** sawal ko plain yes/no mein force karna — recklessness aur
abandonment dono produce karta.

Phir ek final sawal: **"Last baar jab decide kiya yeh theek hai, usske baad kya change hua?"**
Kuch na badla to continue karo. Important badla to relevant block dobara check karo.

## Record Finish Karna

4 Now-do-it blocks kiye to Blocks 1-4 ready hain. 2 steps bachte:

**Step 5 — Evidence:** success measure, failure threshold, monitoring owner+cadence, residual
risk.

**Step 6 — Record share karo:** jo workflow/policy/risk owns karta usko bhejo: _"Yeh hai jaise
main workflow chalane ka propose karta hoon. Approval/data-route/reviewer/control ke baare mein
koi assumption correct karo."_ Goal har harmless task ke liye signatures nahi — **hidden
assumptions ko visible decisions banana incidents banne se pehle.**

```text
GOVERNANCE RECORD
Workflow:                        Owner:                    Date:

THE CASE
  Classification:      appropriate / appropriate with review / inappropriate
  Deciding factor:
  Gate: who               what they verify              when

THE DATA
  Tier:                green / yellow / red
  Does the task need the identifiers?     yes / no
  Fields removed:
  Approved route:

THE CAPABILITY
  Tools, Skills, connectors enabled:
  Source:                                  Reach:
  Outside content it reads:
  Actions it must not take without review:

THE PEOPLE
  Who is affected:
  Fairness check (including exclusions):
  Disclosure decision:                     Required by / judgment
  Open question or escalation:

THE EVIDENCE
  Success measure:
  Failure threshold:
  Monitored by:                            How often:
  Residual risk:

RE-CHECK IF: model, feature, data, audience, permission, policy,
vendor term, or business consequence changes.
```
