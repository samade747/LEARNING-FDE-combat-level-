# 07 — Principle 7: Observability

> **Failure mode:** "Mujhe pata hi nahi agent ne asal mein kya kiya?"

Aap sirf woh direct kar sakte ho jo dekh sakte ho. Agent ka har meaningful action aap ko qareeb real-time
mein dikhna chahiye. Jab kuch ghalat ho, log dekh kar exactly samajh ana chahiye kya hua. Observability
hi ek drifted session debug karne ka, autonomy ladder chadhne ke liye track record banane ka, aur output
ko trust karne ka tareeqa hai.

## Discipline

**Har novel task par kam az kam ek dafa execution view dekho.** "Agent ne kuch unexpected kiya" ka sabse
bara source yeh hai ke user ne dekha hi nahi.

## Examples

- **Fleet-routing:** Logistics coordinator batch chala kar stand-up mein chala jata hai. Beech mein ek
  customer ke address-notes field mein prompt-injection thi — agent ne 47 driver ko galat pings bhej
  diye. Pehle 10 deliveries dekhna hota, farq delivery 4-5 par hi dikh jata.
- **Lawyer:** Per-step approval cards parhte hue, response #4 par ek galat-tagged privileged document
  pakri gayi — ship hone se pehle.
- **Controller:** Walk-away rung par ek task chalaya. Wapis aake execution view scan karne ki habit se
  pata chala agent ne `payroll-confidential.xlsx` bhi khola tha — ek stale folder reference `AGENTS.md`
  mein.
- **Silent agent (Ali ka competitor-tracker):** Dashboard "running" dikhata raha lekin 3 din se koi data
  nahi aaya — firewall ne database port block kar diya tha. **Agent chal raha tha lekin kuch nahi kar
  raha tha.** 10-second check pakar leta.
- **Cascading failure:** Teen agents ek sath fail — asli wajah disk 100% full thi. **LNPS triage**
  (Logs → Network → Process → System) System se shuru kiya jata to ek hi root cause turant pakri jati.

## 5 Symptoms — Session Off the Rails Ja Rahi Hai

1. Agent baar baar purani baaton ka reference deta hai jo current task se related nahi
2. Responses lambe aur vague hote jate hain, zyada hedging
3. Kayi turns pehle stated constraint se contradict karta hai
4. Baar baar apologize karta hai bina progress ke
5. Aisi files/folders/connectors touch karne ki baat karta hai jo mention hi nahi hui

Jab yeh dikhein: **type karna band karo.** Naya prompt se fix karne ki koshish mat karo — usse aur
tangled context add hota hai. `/clear` chalao (CC/OC) ya nayi session kholo (Cowork/OW), sirf woh 1-2
zaroori facts paste karo, wahin se continue karo. **Reset almost hamesha rescue se tez hai.**

## Hands-On Practice

Wahi "Pack 1" folder teesri baar. Prompt mein AI ko har step narrate karne ko kaho: "kya khola, kya
dekha, kya conclude kiya." Execution view mein chote steps ki sequence bharti hai. **Principle moment:**
ek surprise likh lo — koi file jo expect nahi ki thi, koi extra tool call, koi inference jo prompt mein
nahi thi. **Yehi ek observation hi asli principle hai.**

## Apne Kaam Par Apply Karo

1. Woh task chuno jo aap already walk-away par chala rahe ho.
2. Aaj poori run baithe dekho — 3 columns mein note karo: step, expected tha ya nahi, koi surprise.
3. Har surprise ke liye decide karo: task badalna hai, constraints tighten karni hain, ya apni
   expectations calibrate karni hain.
4. **Habit banao:** kisi bhi naye task ko walk-away promote karne se pehle ek watch-once karo.

**Kyun matter karta hai:** Principles 1-6 kaam sahi karne ke baare mein hain. Principle 7 hai **pata
karna kya aap ne sahi kiya**, real-time ke qareeb — ghalti ki cost barhne se pehle. Iske bina, baqi
chhe principles sirf claims hain jo verify nahi ho sakte.

---
[⬅ Principle 6](06-principle-6-constraints-safety.md) · [⬆ Index](README.md) · [Agla: Four-Phase Workflow ➡](08-four-phase-workflow.md)
