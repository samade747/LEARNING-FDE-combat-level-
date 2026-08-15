# 07 — Practice Projects (8 Graph Builds)

Graph ke baare mein parhna aur usay bharna alag cheezein hain. 8 builds, easy se hard tak, kisi bhi tool
mein.

**2 rules, hamesha:**
- **Throwaway repo + real documents use karo** — invented data ki bajaye apni real READMEs/notes/logs
- **Pehla claim likhne se pehle schema likho** — 5 minute mein likha `graph/SCHEMA.md` baad mein
  reconstruct karne se behtar hai

---

### 1. ✏️ Draw Your System
**Difficulty:** Easy · **Time:** 10-15 min · **Concept:** 2, 3, 11

Kagaz ya Mermaid pe, aaj jo har loop, checker, human gate, anchor, memory file aap chalate ho — sab
typed nodes + labeled directed edges ki tarah draw karo. Konse nodes loops hain aur konse nahi, mark
karo. Phir 2 cheezein circle karo: koi finding jo sirf transcript mein exist karti hai, aur koi
optimizing loop jiska koi watcher na ho.

**Done jab:** Aap ek circled item har type ka point kar sako aur bata sako iski cost kya hai.

---

### 2. 🧾 Spine to Claims
**Difficulty:** Easy · **Time:** 30-45 min · **Concept:** 1, 8, Part 6

Apni real `progress.md` (ya kisi loop ka log) lo, uske aakhri 10 durable findings ko Part 6 ke schema ke
under `claims.json` records mein convert karo. Har invariant field bharo, `produced_by` aur real
`source` samet.

**Done jab:** Sab 10 mein se har ek ya to kuch cite kare jo baad wala agent khol sake, ya explicitly
`"source": {"kind": "inference"}` mark ho. **Inference wale count karo.** Yehi count wo cheezein hain jo
aap facts samajh rahe thay sirf model ki fluency ki wajah se.

---

### 3. 🔍 First Extraction
**Difficulty:** Medium · **Time:** 45-60 min · **Concept:** 6

Concept 6 ka prompt 3 related documents pe headlessly chalao. Har reply `jq` se validate karo. Phir count
karo kitni distinct entities 2+ surface forms ke under ayin.

**Done jab:** Sab 3 documents schema-valid JSON return karein, aur aap 1 entity naam sako jo 2+ naamon
ke under ayi ho. Agar count zero ho, documents bohat similar hain — alag logon ke likhe 3 documents use
karo.

---

### 4. 🌿 The DAG Speaks
**Difficulty:** Medium · **Time:** 30-45 min · **Concept:** 4, 5

Real history wali repo mein, AgentHub ke 3 sawal plain Git se answer karo: commit X ke upar kya try hua,
konse tips unexplored frontier hain, konsi path current state tak pohanchi. Phir 3 commands ek
`GRAPH.md` mein likho taake future agents bhi puch sakein.

**Done jab:** 3 commands kaam karte hon aur aap bata sako DAG **kya nahi bata sakti**: konse experiments
try hue aur phenk diye gaye.

---

### 5. 🔗 Resolution Drill
**Difficulty:** Medium · **Time:** 45-60 min · **Concept:** 7

Project 3 se 20 surface forms lo, type se group karo, descriptions ke sath, ek stronger model se
canonical clusters mango rationale + confidence ke sath, har alias rakhte hue. Phir trap plant karo: 2
genuinely alag entities jo naam share karti hain add karo, dobara chalao.

**Done jab:** Real duplicates merge hon, 2 same-named ajnabi alag rahein, aur har canonical entity apne
surface forms list kare. Agar ajnabi merge ho jayein, resolution prompt fix mat karo pehle — descriptions
ko richer banao.

---

### 6. ⚖️ The Grounded Reviewer
**Difficulty:** Hard · **Time:** 1-2 hrs, phir 5 beats · **Concept:** 10, Part 6

Part 6 ka reviewer apni ek chalti loop mein wire karo. Verdicts mein `grounded_in` resolvable claim ids
ke sath honi chahiye, bina supporting claim wali factual statement REVISE force kare `missing` ke sath,
aur `inference` source wali claim akeli kisi cheez ko ground na kar sake. 5 real beats chalao.

**Done jab:** Kam se kam ek beat REVISE ke sath wapas aye ek named missing edge ke sath, aur maker ki
agli koshish ne ya evidence produce ki ya claim withdraw ki.

---

### 7. 📏 A Gold Set for Extraction
**Difficulty:** Hard · **Time:** 2-3 hrs · **Concept:** 6, 7

5 documents mein entities aur relations hand-label karo. Phir Project 3 ke prompt ko apne labels ke
against score karo: precision, recall, schema-valid rate. Prompt ki ek line badlo, dobara score karo,
number ke basis pe keep ya revert karo.

**Done jab:** Aap ne prompt pe ratchet kam se kam 3 dafa chalayi ho, reverted attempts samet record ke
sath. **Aap ne graph autoresearch bana diya** — same loop, alag artifact.

---

### 8. 🏗️ Two Loops, One Graph (Capstone)
**Difficulty:** Capstone · **Time:** Ek weekend, phir ek hafta beats · **Concept:** Sab kuch

2 loops, ek graph pe. Triage loop real tool-output sources ke sath claims likhti hai. Changelog loop
unhe 2-hop context builder se parhti hai, file dump se nahi. Dono reviewers apne verdicts ground karte
hain. Pre-commit hook schema + append-only rule guard karta hai. Triage loop ke throughput number ko ek
counter-metric milta hai jo review loop watch karti hai.

**Done jab:** Changelog loop sahi tarah ek fix report kare jo usne kabhi **witness nahi kiya**, kyunke
graph ne carry kiya, **aur** aap us line se claim, run, aur captured tool output tak wapas walk kar sako
jo kisi model ne nahi likha. Jab ye walk succeed ho jaye, aap ne **anchors ke sath shared memory** bana
li hai.

---
[⬅ Staying Grounded](06-staying-grounded.md) · [⬆ Index](README.md)
