# 01 — The Surface: Sessions, Files, Connectors, Gate

## Concept 4: Account Spine

Purane Foundations workflow mein, ek standalone conversation aksar zero se shuru hoti thi — aap context
dobara paste karte, project dobara samjhate. Agent surface aapko **continuity ek feature ki tarah** deta
hai: sessions aur files aapke account mein save hoti hain. Kisi bhi device se kholo, wahi kaam, wahin
se.

Ye **account spine** hai — memory jo sessions/devices ke darmiyan bachi rehti hai, vendor ne banayi,
aapko kisi ko hire nahi karna parta.

> **Real gift hai, lekin keemat bhi hai:** Spine **vendor ki custody** aur **vendor ke format** mein
> rehti hai. Ye ek dependency hai: aapke plan pe, product ke zinda rehne pe, vendor ke rules pe.

**3 chhoti aadatein:**
- **Sessions ko work products ki tarah naam do, chats ki tarah nahi** — "Acme renewal brief" 3 mahine
  baad khud ko dhoond leta hai. "Quick question" kabhi nahi
- **Ek session, ek workstream** — client report aur holiday planning mix karna context bleed karta hai
- **Dead cheezein prune karo** — lambi session apni poori history har turn mein le jati hai, cost badhta hai

## Concept 5: 3 File Tiers — Is Course Ka Sab Se Zaroori Concept

Har file jo agent touch karta hai, 3 tiers mein se ek mein rehti hai:

**Tier 1: Task filesystem** — Remote session kaam karte waqt temporary scratch space use karti hai.
Kaam khatam hone pe cleanup ho jati hai. **Kal chahiye hone wali kisi bhi cheez ka ghar kabhi nahi.**

**Tier 2: Platform storage** — Files permanently aapke account mein save hoti hain vendor ke platform
pe. Task, tab, hafta — sab se bach jati hain. **Safe hai. Vendor ki custody mein bhi hai.**

**Tier 3: The Exit** — File platform se **nikal kar** aisi jagah jati hai jise **aap control** karte
ho. Connector save (Drive), email, direct download, local write, repo commit. **Sirf ye tier deliverable
ko aapke apne system of record mein daalta hai.**

> **Yaad rakhne wali line, poori course ki:**
> **"Finished work exits the platform. Everything else may stay."**

Risk ladder ki tarah parho: Tier 1 mein rehne wali cheez **already lost** hai (wipe bug nahi, tier ki
definition hai). Tier 2 mein rehne wali cheez **aaj safe, kal hostage** hai — safe kyunke bachti hai,
hostage kyunke **sirf wahin** bachti hai, kisi aur ki login ke peeche. Tier 3 mein rehne wali cheez
**aapki hai.**

**Worked example:** Ayesha invoicing karti hai. Draft numbers Tier 1 mein (scratch math, temp CSV) —
theek hai wahan marna. Invoice template Tier 2 mein (dobara use hogi). **Finished invoice PDF Tier 3
mein, do dafa** — firm ki Drive mein save, aur client ko email. Kyun do dafa? Kyunke koi din puchega
"March ka invoice kahan hai?" — aur jawab **firm ke records** hone chahiye, "somewhere in my Cowork
account" nahi.

**Har brief ke aakhir mein ye line add karo:**
```text
End by listing every file you created and where each one landed:
temporary working space, platform storage, or a system I control
(connector save, download, local write, or repo commit).
```

> **Simple:** Kaghaz 3 jagah reh sakta hai. Worker ke scratch pad pe: din ke aakhir mein phenk diya jata
> hai. Worker ki apni drawer mein: safe, lekin unki desk mein, aapki nahi. Aapki filing cabinet mein:
> aapki, jahan aapke rules chalte hain. **Rule simple hai: jo bhi khatam ho, filing cabinet mein jaye.**

### Self-Check
**Sawal:** Ek lawyer ek comparison memo web session mein banata hai aur platform link client ko share
kar deta hai. 2 galtiyan batao.
**Jawab:** Pehli, **custody:** memo sirf Tier 2 mein exist karta hai — vendor ka platform, firm ki matter
folder ke bahar, isliye firm ke apne record mein hole hai. Doosri, **access:** link ki sharing story
platform ki hai, firm ki nahi. **Fix Tier 3 hai:** document management system mein save karo, wahan se
share karo.

## Concept 6: Connectors Web Pe — Reach + Exit Door Ek Sath

Connector ki definition wahi hai (permission-scoped access, MCP). Jo badalta hai: **weight**. **Web pe,
connectors double weight uthate hain** — ye reach bhi hain, aur Tier 3 ka **main automated exit door**
bhi.

**2 zaroori baatein:**
- **Read scope send scope nahi hai** — mail connector ko read access dena summarize karne deta hai.
  Write/send access **alag, bara grant** hai. Bhaji hui message wapas nahi hoti
- **Untrusted content careful mode maangta hai** — koi aur banda jo text likhe usmein hidden instructions
  ho sakti hain (prompt injection). Jab task aisi content touch kare jo aap ne nahi likhi, ask-before-
  acting mode mein raho

> **Simple:** Connector ek chaabi hai jo aap worker ko dete ho. Web pe, wahi chaabi 2 cheezein kholti
> hai: wo rooms jahan worker information laane jata hai, aur wo mail slot jahan se aapke finished
> documents nikalte hain.

## Concept 7: The Gate In Your Pocket

**Human gate** wahi rehta hai — jo badalta hai wo hai **ye aapko kahan milta hai**. Desktop pe, aap
screen pe hote ho jab approval card ata hai — accident se ekathhe. Web pe, ye accident gayab hai — kaam
aapke lunch/meeting/neend ke dauran chalta hai. **Approval aapke phone pe ati hai.**

**Phone ka role:** phone **gate hai, workbench nahi.** Wahan se plan review karo, step approve karo,
redirect karo, ya task roko. Design work **bare screen** pe hota hai.

> **Ehtiyat:** *"Gate move nahi hui. Doorbell ko move hona pada."* Jab aap screen pe kaam karte thay,
> escalation khud ba khud aapki nazar ke saamne ati thi. Ab kaam wahan chalti hai jahan aapki nazar
> **nahi** hai. **Ek dekhi na jane wali escalation ek delayed decision hai** — jo kabhi default se li
> gayi decision ban jati hai.

**Aadat, non-negotiable:** **gate ko jaan-boojh kar ek dafa bajao.** Ek chhoti task design karo jo ek
approval mange, computer se poori tarah chale jao, confirm karo notification phone pe aai. **Ek alarm
jo aap ne kabhi nahi suna, ek afwah hai.**

### Self-Check
**Sawal:** Aapka scheduled Monday-morning brief 2 hafton se kuch bhi produce nahi kar raha, koi error
bhi nahi mila. Pehle kya check karo, phir kya?
**Jawab:** Pehle: kya gate aap tak pohanchta hi hai — kya koi session ek approval pe paused hai jo phone
tak kabhi nahi pohanchi? Doosra: kya task chali bhi ya nahi — metered usage/plan limits task ko pause
kar sakte hain bina error ke.

---
[⬅ Overview](00-overview.md) · [Agla: Working Unwatched ➡](02-working-unwatched.md)
