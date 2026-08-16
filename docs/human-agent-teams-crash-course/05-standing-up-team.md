# 05 — Part 6-7: Apni Team Khadi Karo + Ceiling

## Operating Manual: Ek Folder, 8 Files

```text
human-agent-team/
  01-working-agreement.md      few clear boundaries · public/private
  02-roster.md                 har member · owner · tools · autonomy (L0-L4)
  03-role-cards/                ek card per agent
  04-north-star.md              goal · kaun unprompted act kare
  05-verification-rubric.md     pass/fail checks
  06-doer-verifier.md           kaun kisay check kare
  07-weekly-report.md           shipped · lessons/missteps · autonomy changes
  08-attention-budget.md        review vs batched · cap
```

**Order dependency order hai:**
1. **Working agreement** (context sab se pehle)
2. **Roster + role cards**
3. **North star**
4. **Verification rubric + doer-verifier**
5. **Weekly report + attention budget**

Har file ka apna chota checklist hai. File tab tak "done" nahi jab tak checklist sab "yes" na ho.

**Anthropic ke 5 questions — team ready hai jab sab "yes" ho:**
1. Kya information/access agents aur insano dono ko public aur broadly searchable hai?
2. Kya aap team ka roster likh sakte ho, humans aur agents, aur bata sakte ho har member kya own karta hai?
3. Kya har human aur agent ke paas sahi tools hain?
4. Kya key work products verify karne ke liye rubrics/tests hain?
5. Kya team ka ek clear north star hai jise sab reference kar sakein?

## Worked Example: Finance Close Team

**North star:** *har number jo building se bahar jaye, sahi aur apne source tak traceable ho.*

| Member | Human/Agent | Owns | Autonomy |
| --- | --- | --- | --- |
| Controller | Human | Sign-off jo bahar jaye | **human-only** |
| Puller | Agent | Source systems se figures | L2 (verified) |
| Reconciler | Agent | Figures match karna, variances flag | L3 routine ties; L1 new accounts |
| Checker | Agent | Reconciliation rubric ke against grade | doer-verifier only |

**Escalation trigger (Reconciler):** Controller ko escalate karo jab: variance account balance ka 1%
ya $10,000 se zyada ho (jo bhi chota ho), **ya** kisi figure ka system of record mein koi source na ho.

**Verification rubric (Checker):** (1) har balance apne source se threshold ke andar tie kare, (2) har
variance ka reason code ho, (3) har source document link ho, (4) har exception escalation queue mein ho.

Yeh escalation line poori operating model ki miniature hai: Reconciler routine ties khud chalata hai
(L3), Checker verify karta hai insan dekhne se pehle (doer-verifier), unsourced/material numbers ruk
kar insan tak pahunchte hain, aur Controller wahi role rakhta hai jo bahar number ship karta hai.

## Capstone

Apni organization mein ek real goal chuno aur poora artifact set banao: working agreement, roster, role
cards, north star, verification rubric, doer-verifier, weekly report, attention budget.

## Part 7 — Ceiling, Yeh Kahan Barhta Hai

Operating model khud team ko scale nahi karta. **Agle 4 courses machinery hain jo isi par chalti hai:**

- **Workforce with Paperclip** — roster ko automate karta hai: lead agent budgets/approvals ke under
  workers hire/run karta hai
- **Self-Expanding Workforce** — team ko kaam ke sath grow karta hai
- **Identic AI** — attention budget ko automate karta hai: signed identity jo routine approvals clear
  kare
- **Payment-Enabled Agents** — worker ko transact karne deta hai

> **In practices mein kuch naya nahi hai, insano ke liye.** Clear north star, defined roles, khule mein
> kaam, shared quality bar — yeh healthy team habits dahaiyon se maloom hain. Agents inhe introduce
> nahi karte. **Yeh skip karna fatal bana dete hain** — kyunki agent ek buri practice ko utni hi tezi se
> scale karega jitni achi ko.

---
[⬅ Trust, Kamaya Hua](04-trust-earned.md) · [⬆ Index](README.md)
