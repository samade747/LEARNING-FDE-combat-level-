# Human-Agent Teams: The Operating Model for Your Workforce — Summary

Ek unit (trustworthy Digital FTE) se **team** tak jaane ka operating model — insaan ke sath kai Digital FTEs ka team chalana, worker banana nahi. Build-along course nahi hai — yahan **operating documents** likhte ho (roster, role cards, north star, rubric), jaise manager likhta hai, sivaye iske ke agent draft karta hai aap decide karte ho.

**Output — 8-file artifact set:** Team roster, Role card (per agent), Working agreement, North-star doc, Verification rubric, Doer-verifier setup, Weekly report, Attention budget.

## 00 — Ek Worker Se Team Tak (Concepts 1-3)

- 20-saal purani "pod" unit (1 lead + 6-10 engineers, Amazon two-pizza team) coding agents ne tod di — building slow part nahi rahi, bottleneck ulat gaya: "kya hamare paas banane ke haath hain?" se "kya hamare paas validate karne ki judgment hai?"
- **Concept 1 — Single-player khatam:** shift multiplayer ki taraf — multiplayer agent apni memory/credentials rakhta hai, jahan kaam hota hai wahin rehta hai (channels/docs), private session mein nahi. Claude Tag example: Anthropic ka internal team 65% code isi se banata hai.
- **Concept 2 — Worker ko 3 cheezein:** Persistent memory, apni identity, broad searchable access.
- **Concept 3 — Scarce resource human judgment hai:** poori model isay protect karti hai. Failure mode bina model ke: log side-by-side apne AIs chalate hain, kaam duplicate, context private windows mein tootta hai. **4 Practices:** khule mein kaam karo, ek roster/saaf roles, ek north star, trust kamaya hua.

## 01 — Khule Mein Kaam Karna (Concepts 4-5)

- **Concept 4 — Agar likha nahi, exist nahi karta:** agent samajh sirf searchable material se banata hai (channels/code/docs) — private/DM/hallway invisible hain. Payoff: agent dead kaam propose nahi karega, patterns reuse karega; log seekhte hain agent kaise achhe se use hota hai dekh kar.
- **Concept 5 — Boundaries workspace par, document par nahi:** kam, clear security boundaries (workspace-level walls) — andar context azaad flow karta hai. Sensitive kaam ke liye narrow exception lane (DM/private apps). Draft prompt diya gaya hai.

## 02 — Ek Roster, Saaf Roles (Concepts 6-7)

- **Concept 6 — Roster:** har member (human+agent) aur kya own karta hai — Roles Taxonomy + Digital FTE taxonomy ka team-specific version.
- **Concept 7 — Role Card + Skill File:** kya own karta hai, kya **nahi** karta (utna hi zaroori), tools/access (least privilege), kaam kaise check hota hai, escalation trigger. Role ko skill file ki tarah likho → **portable** ban jata hai (roles copy-hone-wali skills ban jate hain, org-chart boxes nahi). Human-only roles explicit rakho (consequential calls). Note: worker ko doosra agent chahiye ho to "Workforce with Paperclip" course automate karti hai.

## 03 — North Star (Concepts 8-9)

- **Concept 8 — Proactive-banane-wala goal:** north star = ambitious wide-reaching goal, ek sentence, insaan set karta hai, business mission mein grounded. Share karne ke baad batao **kaun bina-poochhe act kar sakta hai**. Anthropic example: onboarding-error-message rewrite jo poochha nahi gaya, north star ne on-mission bataya.
- **Concept 9 — Proactivity ek grant hai:** naam se hoti hai, assume nahi. Claude Tag "ambient" mode = explicit revocable per-channel grant.

## 04 — Trust, Kamaya Hua (Concepts 10-12)

- **Concept 10 — Trust Ladder (L0-L4):** L0 (sirf draft) → L1 (act, har output review) → L2 (act, verifier check) → L3 (limits ke andar, escalations batch) → L4 (task type khud chalata, weekly report review). Autonomy **worker-on-a-job** ko milti hai, poore worker ko nahi. **Caution — AI gravity:** insaan ki check-karne-ki-ability permanent nahi, ladder dono taraf move honi chahiye — har hafte kuch clean passes khud dobara verify karo.
- **Concept 11 — Kaam checkable banao:** rubric = team-level Eval-Driven Development. Doer-verifier setup — sasti insurance.
- **Concept 12 — Insaani attention ko paisa ki tarah kharch karo:** questions batch karo, key context repeat karo, item-count limit karo. Weekly "lessons and missteps" report.

## 05 — Apni Team Khadi Karo + Ceiling (Parts 6-7)

- **8-file operating manual** (dependency order): working-agreement → roster+role-cards → north-star → verification-rubric+doer-verifier → weekly-report+attention-budget.
- **Anthropic 5 readiness questions:** public/searchable info? roster likh sakte ho? sahi tools hain? rubrics/tests hain? clear north star hai?
- **Worked example — Finance Close Team:** Controller (human-only, sign-off), Puller (agent, L2), Reconciler (agent, L3 routine/L1 new), Checker (agent, doer-verifier-only). Escalation trigger: variance &gt;1%/$10K ya no-source. Verification rubric: 4 pass/fail checks.
- **Part 7 — Ceiling:** operating model khud team scale nahi karta — agle 4 courses machinery hain: Workforce with Paperclip (roster automate), Self-Expanding Workforce (team grow), Identic AI (attention budget automate), Payment-Enabled Agents (transact). Practices insano ke liye purani hain — agents unhe skip karna **fatal** bana dete hain (buri practice bhi utni hi tezi se scale hoti hai jitni achi).
