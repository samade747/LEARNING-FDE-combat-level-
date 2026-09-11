# Quiz — General Agents on the Web (Test Your Understanding)

**10-question self-contained assessment**, chapter ke 12 concepts (Remote Session se Open Path tak)
grounded — `00`–`03` files se seedha liya gaya, book se training-knowledge se nahi. Same 10 questions
[`05-test-your-understanding.md`](05-test-your-understanding.md) mein scenario version ke tor par bhi
hain.

---

### Q1. Laptop band, session ka kya hota hai?

**Q:** Aap Claude Cowork mein ek multi-step task chala rahe hain. Beech mein laptop ka lid band kar dete
hain. Kya hota hai?

- Task ruk jata hai, jab laptop khulega wahin se resume karna padega
- **Task chalta rehta hai — browser tab session ka window tha, runtime nahi. Vendor ke servers pe
  chalta rehta hai** ✅
- Task cancel ho jata hai, dobara shuru karna padega
- Sirf paid plans pe chalta rehta hai, free plan pe ruk jata hai

**Explanation:** "Tab ek window hai, runtime nahi." Remote session vendor ke servers pe chalti hai — aapka
browser sirf ek window hai jisse aap check karte ho, machine nahi jo kaam karti hai. Isi liye scheduled
task bhi ek band tab se fire hoti hai.
*(Source: `00-overview.md` — Concept 2)*

---

### Q2. Sessions ko naam kaise do?

**Q:** Aap har roz Cowork mein 3-4 sessions kholte hain. 3 mahine baad "Quick question" naam ki 40
sessions milti hain, kisi ka pata nahi konsi kya thi. Kya galat hua?

- Kuch nahi, yeh normal hai
- **Sessions ko work products ki tarah naam dena chahiye tha ("Acme renewal brief"), chats ki tarah
  nahi ("Quick question")** ✅
- Sessions auto-delete honi chahiye thi
- Har session mein sirf ek hi sawal poochna chahiye tha

**Explanation:** Account spine ki 3 chhoti aadatein: work-product naam do (khud ko 3 mahine baad dhoond
leti hai), ek session = ek workstream (mixing context bleed karta hai), aur dead cheezein prune karo
(lambi session poori history har turn le jati hai, cost badhta hai).
*(Source: `01-the-surface.md` — Concept 4)*

---

### Q3. Finance analyst ne memo bana kar platform link share kar diya

**Q:** Ek finance analyst ek variance memo web session mein banata hai aur platform ka share-link seedha
manager ko bhej deta hai — koi doosri jagah save nahi ki. 2 galtiyan batao.

- Koi galti nahi, link kaam kar raha hai
- **Custody galti: memo sirf Tier 2 (platform storage) mein hai, firm ke record ke bahar. Access galti:
  sharing story platform ki hai, firm ki nahi** ✅
- Sirf ek galti: memo bohat lamba tha
- Galti sirf yeh ke manager ne link click nahi kiya

**Explanation:** Tier 2 "aaj safe, kal hostage" hai — bachti hai, lekin sirf platform ki custody mein,
kisi aur ki login ke peeche. Fix Tier 3 hai: document management system mein save karo, wahan se share
karo — taake "March ka memo kahan hai?" ka jawab firm ke apne records ho, "somewhere in my Cowork
account" nahi.
*(Source: `01-the-surface.md` — Concept 5 Self-Check)*

---

### Q4. Mail connector ko "read" access diya — kya woh bhej bhi sakta hai?

**Q:** Aap ne Gmail connector ko sirf **read** access di hai (summarize karne ke liye). Kya Cowork agent
ab client ko email bhej sakta hai agar brief mein maanga jaye?

- Haan, connector connect hai to sab kuch kar sakta hai
- **Nahi — read scope send scope nahi hai. Write/send access ek alag, bara grant hai jo alag se dena
  padta hai** ✅
- Haan, lekin sirf ek email tak
- Nahi, connectors sirf reach dete hain, koi bhi action nahi karte

**Explanation:** Connectors permissions hain, suggestions nahi. Web pe connectors "double weight"
uthate hain — reach bhi hain, aur Tier 3 ka main automated exit door bhi — isliye read/write ka farq
zaroori hai. Bheji hui message wapas nahi hoti.
*(Source: `01-the-surface.md` — Concept 6)*

---

### Q5. Scheduled Monday brief 2 hafton se khamosh hai, koi error nahi

**Q:** Aapka scheduled Monday-morning brief 2 hafton se kuch produce nahi kar raha, koi error message
bhi nahi mila. Pehle kya check karoge?

- Seedha task delete karke naya banao
- **Pehle: kya gate aap tak pohanchta hi hai (koi session approval pe paused, jo phone tak kabhi nahi
  pohanchi)? Phir: kya task chali bhi ya nahi — metered/plan limits bina error ke pause kar sakte hain** ✅
- Internet connection check karo
- Kuch nahi karna, 2 hafte normal hai

**Explanation:** Human gate ab phone pe aata hai — ek dekhi na jane wali escalation ek delayed decision
ban jati hai jo kabhi "default se li gayi" lagti hai. Isi liye gate ko jaan-boojh kar ek dafa bajana
(Drill 3) is failure mode se bachne ka tareeqa hai.
*(Source: `01-the-surface.md` — Concept 7 Self-Check)*

---

### Q6. Plan-first line skip ki, meeting mein gaye, galat deliverable mili

**Q:** Aap multi-source task brief karte ho, "plan pehle dikhao" wali line skip karte ho, meeting mein
chale jate ho. Wapas ane pe ek galat-source-reading pe bani deliverable milti hai. Ek line se kya isay
rok sakti thi?

- Task ko chhota karna chahiye tha
- **`Lay out your plan first, and pause for my approval before doing anything.` — yeh yahan good
  practice nahi, safety net hai, kyunke desktop jaisa beech-mein-pakadna yahan possible nahi** ✅
- Doosri AI se dobara karwana chahiye tha
- Kuch nahi kar sakta tha, yeh normal risk hai

**Explanation:** Desktop agent pe screen pe aankhein hoti hain, beech mein pakad lete. Web pe aankhein
kabhi screen pe nahi hoti — unwatched kaam karna hi is surface ka point hai. Sirf ek intercept bacha hai:
run se **pehle** plan-approval.
*(Source: `02-working-unwatched.md` — Concept 8 Self-Check)*

---

### Q7. Donor summary vs reminder emails — konsi schedule ho sakti hai abhi?

**Q:** Ayesha 2 cheezein schedule karna chahti hai: (a) Monday summary unpaid invoices ka, Drive se
parhna. (b) Friday automatic reminder emails late clients ko. Konsi abhi fit hoti hai, konsi wait kare?

- Dono abhi ho sakti hain
- **(a) Monday summary fit hoti hai — reporting schedule. (b) Friday reminders wait karein — yeh
  bahar duniya pe unattended **act** karti hai; galat run real clients ko email karti hai** ✅
- Dono ko wait karna chahiye
- Sirf (b) fit hoti hai, (a) nahi

**Explanation:** 1-word farq: **acting** (vs reporting). Acting schedule ko checker, machine-verifiable
stopping condition, aur state file chahiye — Loop Engineering course sikhati hai. Yeh course sirf
reporting schedules ke liye safe hai.
*(Source: `02-working-unwatched.md` — Concept 9 Self-Check)*

---

### Q8. 3 tasks — web, desktop, ya "koi nahi abhi"?

**Q:** 3 tasks route karo: (a) Slack/Notion se weekly summary, travel ke dauran bhi chalni chahiye.
(b) laptop pe 200 local files clean karna. (c) privileged client documents se memo.

- Teenon web pe ho sakti hain
- **(a) Web — sirf connectors touch karta hai. (b) Desktop — local filesystem chahiye, remote session
  khud reach nahi karti. (c) Koi nahi, abhi — compliance se likhit jawab pehle chahiye** ✅
- Teenon desktop pe honi chahiye
- (c) bhi web pe ho sakti hai agar connector encrypted ho

**Explanation:** Rule chhota hai: jo kaam touch kare uske hisaab se chuno. Regulated data ka sawal
"surface careful hai?" nahi, "data is custody mein rehne ki ijazat hai?" hai — sirf compliance team,
likhit mein, yeh jawab de sakti hai.
*(Source: `03-choosing-open-path.md` — Concept 10 Self-Check)*

---

### Q9. NGO donor records — policy third-party platforms mana karti hai

**Q:** Ek NGO weekly donor-report automation chahti hai. Policy donor records ko third-party consumer
platforms pe rakhne se mana karti hai, koi engineer bhi nahi. Kaunsa path force hota hai, kya khota hai?

- Web surface, kyunke sabse aasan hai
- **Open path force hoti hai (OpenWork/OpenCode) — donor records vendor ke Tier 1/2 mein nahi ja
  sakte. Khoti hain: free spine, sync, phone gate, managed scheduler — ab kisi ko banani/chalani hai** ✅
- Desktop agent, kyunke woh cloud use nahi karta
- Koi automation nahi ho sakti, policy sab kuch block karti hai

**Explanation:** "Companies aapko spine bech dete hain. Open path aapko banana parta hai." Trade:
custody (control ki machines pe data) + choice (kaunsa model prompts dekhta hai) — badle mein setup,
chalana, fix karna khud/organization ki zimmedari.
*(Source: `03-choosing-open-path.md` — Concept 11 Self-Check)*

---

### Q10. Naya vendor "Flows" launch hota hai — kaise samjhoge bina docs parhe?

**Q:** Agle quarter ek 3rd vendor "Flows" launch karta hai: triggers, integrations, autopilot mode,
workspace memory. Yeh 4 naam book ke kis part se map hote hain?

- Yeh naye concepts hain, book unhe cover nahi karti
- **Triggers = Heartbeat. Integrations = Connectors. Autopilot mode = Run-until-done loop (sawal:
  stopping condition kya, kaun check karta hai?). Workspace memory = State spine** ✅
- Sab ek hi cheez hain, "AI features"
- Sirf "workspace memory" book se map hoti hai, baaki 3 naye hain

**Explanation:** "Naye products aate rahenge, naam badalte rahenge. Shape ek dafa seekho, aur har naya
agent product 30-minute read ban jata hai, naya subject nahi." Surface hafton purani, metered, vendor-
shaped hai — lasting layer yeh 6 parts + stop-typing test + 3 tiers hain, product naam nahi.
*(Source: `00-overview.md` — Concept 3 Self-Check; `03-choosing-open-path.md` — Concept 12)*

---
[⬅ Chapter Index](README.md) · [Scenario version (same content) ➡](05-test-your-understanding.md)
