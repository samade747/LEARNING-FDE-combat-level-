# 05 — Part 5: Safely Use Karna (Woh Hissa Jo Zyadatar Tutorials Rush Karte)

Same principle jo What AI Actually Is mein tha: **model ke andar kuch bhi check nahi karta ke
action safe/correct hai — tum yeh check ho.**

**Skill ek instructions ka set hai jise AI ko follow karne deta hai, Connector tumhari real data
ka darwaza hai. Stranger ki skill ko contract ki tarah treat karo jis par sign karne wale ho,
Connector ko ek chaabi ki tarah jo tum handover karne wale ho.**

## 2 Real Risks

1. **Malicious skills.** Skill text file hai (shayad kuch programs bhi), isliye bad actor ek
   banaa sakta jiski hidden instructions AI ko data leak karne ya suspicious server contact karne
   par majboor karein. 2 named dangers: **prompt injection** (hidden instructions jo AI ko
   unintended actions mein push karein), **data exfiltration** (skill tumhari info secretly bahar
   bhejti). Isliye "social media se free skill download ki" — yeh sentence tumhe rukna chahiye.

2. **Over-broad connector access.** Connector sirf wahi reach kar sakta jo tum reach kar sakte,
   par write access carelessly diya to AI tumhari taraf se change kar sakta — usually dramatic
   nahi, ek galat edit, galat jagah record, ya delete file jiska easy undo na ho.

   Access connector ki reach ka aadha hissa hai — doosra aadha actions ki list hai jo wo karne ke
   liye bani, aur **yeh tumhara set nahi hai.** Drive connector naya file save kar sakta par
   existing document in-place edit nahi kar sakta. Weekly habit build karne se pehle pucho:
   _"What can you actually do in my Drive through this connector, and what can't you do?"_ Limit
   bug nahi hai — **tool ki shape hai.**

## Safe-Use Checklist

- **Trusted sources se skills install karo.** Built-in + official directory safe default hain.
  Forum se zip file nahi.
- **Enable karne se pehle skill parho.** `SKILL.md`+bundled files khud khol lo, ya pucho AI se:
  _"Read this skill and tell me exactly what it instructs you to do. Flag anything that contacts
  external servers, handles credentials, or could leak my data."_
- **Naya connector read-only se shuru karo.** "Search and summarize" "send"/"delete" se pehle.
  Write access sirf tool ke achhe behave karne ke baad.
- **Sabse chhote folder/app par scope karo.** Ek-folder job ke liye whole-drive access mat do.
- **Scope Connector idea hai, Skill idea nahi.** Connector ke scopes narrow kar sakte; **Skill ka
  koi dial nahi hai** — jo access chat ke pass already hai, usi se chalti hai, sirf task ko jo
  chahiye usse nahi. Isliye Skills ke liye control = pehle parhna, Connectors ke liye = read-only
  se start karna.
- **Edits allow karne se pehle recovery check karo.** Connector version-history/undo kaise
  handle karta confirm karo. Kuch write actions recovery path skip karte, backups rakho.
- **Team par shared skills organization ki directory se route karo** (owner ne review ki), zip
  files pass karne se nahi.

Isse scared hone ki zaroorat nahi — built-in tools safe hain, everyday workflow low-risk hai.
Point yeh hai: jaise "built-in use karo" se "community skills + write access" ki taraf move karo,
**tumhari caution match karne ke liye uthni chahiye.**
