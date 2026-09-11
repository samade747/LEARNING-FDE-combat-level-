# 05 — Test Your Understanding (Scenario-Based)

Chapter ke 12 concepts (Remote Session se Open Path tak) grounded assessment. Same content as
[`quiz.md`](quiz.md), standalone self-test version.

---

### Q1. Laptop band, session ka kya hota hai?

**Q:** Aap Claude Cowork mein ek multi-step task chala rahe hain. Beech mein laptop ka lid band kar dete
hain. Kya hota hai?

- Task ruk jata hai, jab laptop khulega wahin se resume karna padega
- **Task chalta rehta hai — browser tab session ka window tha, runtime nahi. Vendor ke servers pe
  chalta rehta hai** ✅
- Task cancel ho jata hai, dobara shuru karna padega
- Sirf paid plans pe chalta rehta hai

**Explanation:** "Tab ek window hai, runtime nahi." Remote session vendor ke servers pe chalti hai.
*(Source: `00-overview.md` — Concept 2)*

---

### Q2. Sessions ko naam kaise do?

**Q:** Aap har roz 3-4 sessions kholte hain. 3 mahine baad "Quick question" naam ki 40 sessions milti
hain, pata nahi konsi kya thi. Kya galat hua?

- Kuch nahi, normal hai
- **Sessions ko work products ki tarah naam do ("Acme renewal brief"), chats ki tarah nahi** ✅
- Sessions auto-delete honi chahiye
- Har session mein sirf ek sawal poochna chahiye tha

**Explanation:** 3 chhoti aadatein: work-product naam, ek session = ek workstream, dead cheezein prune.
*(Source: `01-the-surface.md` — Concept 4)*

---

### Q3. Finance analyst ne memo bana kar platform link share kar diya

**Q:** Ek analyst variance memo web session mein banata hai, platform share-link seedha manager ko bhej
deta hai — kahin aur save nahi ki. 2 galtiyan batao.

- Koi galti nahi
- **Custody: memo sirf Tier 2 mein, firm ke record ke bahar. Access: sharing story platform ki hai,
  firm ki nahi** ✅
- Sirf yeh ke memo lamba tha
- Manager ne link click nahi kiya

**Explanation:** Tier 2 "aaj safe, kal hostage." Fix Tier 3: document management system mein save karo.
*(Source: `01-the-surface.md` — Concept 5 Self-Check)*

---

### Q4. Mail connector ko "read" access diya — kya woh bhej bhi sakta hai?

**Q:** Gmail connector ko sirf **read** access di hai. Kya agent client ko email bhej sakta hai agar
brief maange?

- Haan, connect hai to sab kuch kar sakta hai
- **Nahi — read scope send scope nahi hai. Write/send alag, bara grant hai** ✅
- Haan, sirf ek email tak
- Nahi, connectors koi action nahi karte

**Explanation:** Connectors permissions hain, suggestions nahi. Bheji hui message wapas nahi hoti.
*(Source: `01-the-surface.md` — Concept 6)*

---

### Q5. Scheduled Monday brief 2 hafton se khamosh, koi error nahi

**Q:** Scheduled brief 2 hafton se kuch produce nahi kar raha, koi error nahi mila. Pehle kya check
karoge?

- Task delete karke naya banao
- **Pehle: gate pohanchta hi hai (approval phone tak gayi ya nahi)? Phir: task chali bhi ya nahi —
  metered/plan limits bina error pause kar sakte hain** ✅
- Internet connection check karo
- Kuch nahi karna

**Explanation:** Ek dekhi na jane wali escalation ek delayed decision ban jati hai — gate on-purpose test
karo (Drill 3).
*(Source: `01-the-surface.md` — Concept 7 Self-Check)*

---

### Q6. Plan-first line skip ki, galat deliverable mili

**Q:** Multi-source task brief kiya, "plan pehle dikhao" skip kiya, meeting mein gaye. Galat-source-
reading pe bani deliverable mili. Ek line se kya rok sakti thi?

- Task chhota karna chahiye tha
- **`Lay out your plan first, and pause for my approval` — yahan good practice nahi, safety net hai** ✅
- Doosri AI se dobara karwana chahiye tha
- Kuch nahi kar sakta tha

**Explanation:** Web pe aankhein kabhi screen pe nahi hoti — sirf ek intercept bacha: run se pehle
plan-approval.
*(Source: `02-working-unwatched.md` — Concept 8 Self-Check)*

---

### Q7. Donor summary vs reminder emails — konsi schedule ho sakti hai abhi?

**Q:** (a) Monday summary unpaid invoices, Drive se parhna. (b) Friday automatic reminder emails late
clients ko. Konsi abhi fit, konsi wait kare?

- Dono abhi ho sakti hain
- **(a) fit hoti hai — reporting. (b) wait kare — bahar duniya pe unattended **act** karti hai** ✅
- Dono ko wait karna chahiye
- Sirf (b) fit hoti hai

**Explanation:** 1-word farq: acting (vs reporting) — Loop Engineering course acting schedules sikhati
hai (checker + stopping condition).
*(Source: `02-working-unwatched.md` — Concept 9 Self-Check)*

---

### Q8. 3 tasks — web, desktop, ya "koi nahi abhi"?

**Q:** (a) Slack/Notion weekly summary, travel ke dauran. (b) laptop pe 200 local files. (c) privileged
client documents se memo.

- Teenon web pe ho sakti hain
- **(a) Web — sirf connectors. (b) Desktop — local filesystem chahiye. (c) Koi nahi, abhi — compliance
  se likhit jawab pehle** ✅
- Teenon desktop pe honi chahiye
- (c) bhi web pe ho sakti hai agar encrypted ho

**Explanation:** Regulated data ka sawal "surface careful hai?" nahi, "data is custody mein rehne ki
ijazat hai?" hai.
*(Source: `03-choosing-open-path.md` — Concept 10 Self-Check)*

---

### Q9. NGO donor records — policy third-party platforms mana karti hai

**Q:** NGO weekly donor-report automation chahti hai. Policy donor records ko third-party platforms pe
rakhne se mana karti hai, koi engineer nahi. Kaunsa path force hota hai, kya khota hai?

- Web surface, aasan hai isliye
- **Open path force hoti hai — free spine, sync, phone gate, managed scheduler khoti hain, ab khud
  banani hai** ✅
- Desktop agent
- Koi automation nahi ho sakti

**Explanation:** Trade: custody + choice, badle mein setup/chalana/fix khud ki zimmedari.
*(Source: `03-choosing-open-path.md` — Concept 11 Self-Check)*

---

### Q10. Naya vendor "Flows" launch hota hai — kaise samjhoge bina docs parhe?

**Q:** 3rd vendor "Flows": triggers, integrations, autopilot mode, workspace memory. Kis part se map
hote hain?

- Naye concepts hain, book cover nahi karti
- **Triggers=Heartbeat, Integrations=Connectors, Autopilot=Run-until-done loop, Workspace memory=
  State spine** ✅
- Sab ek hi cheez, "AI features"
- Sirf "workspace memory" map hoti hai

**Explanation:** Shape ek dafa seekho, har naya agent product 30-minute read ban jata hai, naya subject
nahi.
*(Source: `00-overview.md` — Concept 3 Self-Check)*

---
[⬅ Chapter Index](README.md) · [Quiz (same content) ➡](quiz.md)
