# 02 — Question 2: The Data — Kya Yeh Information Jaa Sakti Hai?

Project manager ke pass customer names+account numbers ki spreadsheet hai, AI se spending trends
dhoondne chahti customer base mein. Company policy regulated personal data restrict karti. As-is
upload karo, identifiers pehle strip karo, "retain na karo" instruction ke sath upload karo, ya
analysis skip karo? Decide karo pehle.

**Reasonable AI task bhi aisi data par chal sakta jo wo tool/route ke liye nahi jana chahiye.**

Order use karo: **Data classify karo → task ko identifying details chahiye kya pucho → route
confirm karo → control choose karo.** Privacy feature se shuru mat karo, backward mat karo.

## 2.1 — 3 Practical Tiers

**Data tier** = label jo batata information kitni carefully handle honi chahiye.

- **Green: generally permitted.** Public material, aggregated figures, broad-use-approved internal
  material. **Anonymized** data bhi (badli hui, apni organization ke standard se kisi ko identify
  nahi karti).
- **Yellow: check first ya control add karo.** Internal-only documents, personal contact details,
  customer/employee identifiers, confidential drafts, unannounced deal/product info, ya jiska use
  route par depend karta.
- **Red: unapproved route se mat use karo.** Credentials, secrets, highly regulated/specially
  protected data, privileged material (legally disclosure-protected, jaisa client-lawyer
  communication), third-party confidential info, licensed material jo copy karne se mana karti.

> **Unsure ho 2 tiers ke beech?** Zyada sensitive wala use karo jab tak authorized koi policy
> padh ke kahe. Ek tier zyada careful 2-minute confirmation cost karti; galat direction poora
> program cost kar sakta.

## 2.2 — Sabse Useful Data Sawal

Sensitive task impossible maanne se pehle: **Kya task ko identifiers chahiye hain, ya sirf
pattern?**

Yeh key branching sawal hai, course isay **discriminator** bolta — decide karta tum kaunse branch
par ho. Spending trends ko customer names shayad nahi chahiye. Ek account reconcile karne ke liye
identifier zaroori ho sakta.

Sirf pattern chahiye to move **redaction** hai — jo fields task ko nahi chahiye unhe data model
tak pahunchne se pehle hatana. "Customer 17" naam replace karna pehla move hai, verdict nahi. Ek
aur sawal: koi abhi bhi list rakhta jo Customer 17 ko real person se map karti? Haan to data
**pseudonymized** hai (labels trace back ho sakte) — tier same rehti.

## 2.3 — Redaction Useful Hai, Magic Nahi

2 common failures:

1. **Partial redaction** — obvious identifier hataya, par enough clues chhode jo person identify
   karein (rare job title, exact date, region, age — combination).
2. **Redaction jo task break karti** — jo info task ko chahiye wo hata di. Result safe dikhta,
   useless hota.

**Pseudonymized data ko anonymous ki tarah treat mat karo.** Mapping list gayi ho aur task sirf
pattern chahta ho, analysis ab protected fields touch nahi karti — restriction apply nahi hoti.
**Yeh ordinary case hai.** Apni organization ka standard hi tier drop karne deta hai, relabeling
nahi.

## 2.4 — Route Tool Ke Naam Jitna Hi Matter Karta Hai

**Entry point** = route jisse material AI system tak pahunchta: chat, project/workspace, incognito
conversation, file upload, **connector**, **API**, ya desktop agent. Connector = approved link jo
AI ko ek app tak pahunchata; uski **scopes** = exact list jo karne deti ho (read files, kabhi
email na bhejo). Approved hona harmless nahi matlab — scopes check karo on karne se pehle. API =
direct software-to-software link, chat window nahi.

Routes retention/access/logging/admin properties mein alag hote, aur contract terms+training-use
mein bhi.

**Useful sawal "yeh AI product approved hai?" nahi hai — "kya yeh route is data aur is purpose
ke liye approved hai?"** hai. **Purpose** = data pehli baar collect karne ka reason. Sensitive/
regulated data ke liye approval admin/policy-owner/security/compliance/contract se aati, keyboard
par guess se nahi.

**Gym example:** members ke phone numbers class reminders ke liye hain. Same numbers supplements
sell karne ke liye use karna **alag purpose** hai. Objection phone numbers ke baare mein nahi —
jo promise collect karte waqt kiya gaya usske baare mein hai.

## 2.5 — Privacy Controls Narrower Sawal Answer Karte

Temporary conversations, memory controls, retention settings, sandboxed execution, encryption,
projects, managed workspaces — har ek specific risk kam karta. **Koi bhi earlier authorization
sawal answer nahi karta.**

| Control | Kya Help Karti | Kya Decide Nahi Karti |
|---|---|---|
| Temporary/incognito conversation | History/memory persistence | Data entry allowed thi ya nahi |
| Memory controls | Cross-session reuse | Upload allowed tha ya nahi |
| Code-execution sandbox | Kahan code chale limit karti | Data us environment ke liye authorized thi ya nahi |
| Project/workspace | Shared knowledge+files saath | Har file/data type approved hai ya nahi |
| Admin controls | Roles, retention, exports, audit | Har workflow/data-type ke liye blanket approval |

> **Sandbox aur authorization alag hain.** Sandbox execution boundary hai, approval boundary
> nahi. Data phir bhi system mein daakhil hui, outputs phir bhi nikal sakte. Alag se pucho: data
> jaane ke liye allowed hai, aur results/actions jaane ke liye allowed hain?

## 2.6 — Claude Routes: 5 Distinctions (Checked Sept 2026)

- **Memory retention nahi hai** — off switch plan par depend karta. Team plans mein org-level
  memory controls nahi; Enterprise mein Owners off kar sakte sab ke liye.
- **Incognito zero-retention nahi hai** — history/memory mein nahi dikhta, par 30-day default
  retention documented hai (Enterprise par custom longer bhi). Projects se bahar hi available.
- **Training use plan par depend karti** — Free/Pro/Max mein privacy settings decide karti; allow
  karne se retention 5 saal tak extend hoti. Team/Enterprise/API default training-use nahi karte.
  Incognito kisi plan par training mein use nahi hota.
- **Sandbox data authorization nahi hai** — execution isolation reach kam karta, sensitive file
  allowed thi yeh prove nahi karta.
- **Interface mein private = organizational records se absent nahi** — Team/Enterprise data-export
  mechanisms dete, Enterprise compliance+audit mechanisms bhi.

## Worked Examples

- Confidential-material-free meeting notes → usually **Green**
- Anonymized survey responses (identifiers really gone) → **Green**; decisions-par-rehne-wale
  totals code execution sandbox mein compute karo
- Credentials/API secrets → **Red**, approved secret-handling mechanism use karo
- Patient/financial/privileged records → **Red** jab tak specific route+use-case approved na ho
- Spreadsheet example (opening): spending trends ko pattern chahiye, logon ko nahi — identifiers
  strip karo, confirm koi mapping file ke sath travel nahi karti, analysis chalao. As-is upload
  policy todti; analysis skip karna kisi ko protect nahi karta; "retain mat karo" instruction wish
  hai, control nahi.

## Now Do It — Record Ka Block 2

Kya data enters, uski tier; task ko identifiers chahiye ya nahi, kaunse fields hata sakte;
approved route sensitive fields reh jayein to, aur purpose yeh use cover karta ya nahi.

> Redaction practice ke liye **synthetic data** (made-up, real jaisi) use karo — partly-redacted
> real sensitive document unapproved chat mein mat daalo yeh pucchne ke liye kaafi redacted hai
> ya nahi.
