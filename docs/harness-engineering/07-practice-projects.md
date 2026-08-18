# 07 — Practice Projects (8 Harness Builds)

Harness ke baare mein parhna aur usay **tight** karna alag cheezein hain. Ye 8 builds easy se hard tak
hain — kisi bhi tool mein karo.

**2 rules, hamesha:**
- **Throwaway git repo use karo** — aap jaan-boojh kar apne guardrails trip karoge
- **Failure khud banao** — harness sirf us ghalti se proof hoti hai jo wo pakre. Har project mein
  jaan-boojh kar ek break-in/break-down/bad-verdict shamil hai

---

### 1. 🧱 The First Wall
**Difficulty:** Easy · **Time:** 20-30 min · **Concept:** 4 (permission rules)

Throwaway repo ke liye deny list likho: secrets files, recursive deletes, force-push. Phir har rule ko
jaan-boojh kar trip karo — agent se secret parhwao, force push karwao, dekho har deewar khari rehti hai.

**Done jab:** Har deny rule ek deliberate attempt ko block kar chuki ho, aur aap keh sako kis layer ne
enforce kiya (tool layer). Agar koi variant command pattern se slip kar jaye, aap ne Concept 4 ki
honesty note khud jee li: patterns tripwires hain, sandbox deewar hai.

---

### 2. 🪝 The Lint Hook
**Difficulty:** Easy-Medium · **Time:** 30-45 min · **Concept:** 8 (hooks)

Post-edit hook lagao jo linter chalaye aur failures agent ko wapas de. File tor kar dekho agent error
receive kar ke fix karta hai. Phir ek `Stop`/`pre-commit` gate lagao jo lint fail hone tak khatam hi na
hone de.

**Done jab:** Aap ne dono behaviors dekh liye ho aur ek line mein farq bata sako: pehla **feedback** hai
(edit undo nahi kar sakta), doosra **gate** hai (kaam uske aage "done" count hi nahi ho sakta).

---

### 3. 🗣️ The Error Audit
**Difficulty:** Medium · **Time:** 45-60 min · **Concept:** 7 (AX)

Ek connector chuno jo aapki loops use karti hain. Uski 3 sab se common errors jaan-boojh kar trigger
karo, aur har message aise parho jaisay agent parhega — bina kisi insaan ki madad ke. Har ek ko aisay
rewrite karo ke wo agla step bataye.

**Done jab:** Fail hui call agent ki agli koshish pe **khud heal** ho jaye kyunke error ne bata diya kya
badalna hai, aur aap us beat ki taraf ishara kar sako jo pehle waste hoti thi.

---

### 4. ✂️ The Tool Diet
**Difficulty:** Medium · **Time:** 1-2 hrs, phir ek hafta beats · **Concept:** 6, 7

Aapki triage loop jo bhi tools dekh sakti hai unki list banao. List ko sirf utna kaato jitna skill ko
asal mein chahiye. Ek hafta chhoti list pe beats chalao.

**Done jab:** Aap wrong-tool incidents ka before/after compare kar sako, aur after count chhota ho. Agar
kuch improve na ho, iska matlab aapki list pehle se hi lean thi — ye bhi jaanne ki cheez hai.

---

### 5. 📋 The Typed Reviewer
**Difficulty:** Medium-Hard · **Time:** 1-1.5 hrs · **Concept:** 9 (typed output)

PASS/FAIL reviewer ko Concept 9 ke JSON verdict pe upgrade karo, field-by-field `jq` validation add
karo, aur protocol breaks ko "needs a human" mein route karo. Phir usay ek jaan-boojh kar lambi, unclear
review khilao.

**Done jab:** Wo lambi, unclear review guess hone ki bajaye **escalation path** mein chali jaye, aur
hand-crafted `{"verdict": "MAYBE"}` reject ho jaye — prove karta hai aap **values** validate karte ho,
sirf **presence** nahi.

---

### 6. 🔩 The Ratchet Week
**Difficulty:** Medium · **Time:** 1 hafta, ~15 min/din · **Concept:** 10 (failure classes, ratchet)

7 din ke liye, har agent mistake ko 4 failure classes mein classify karo aur har fix us class ki surface
pe likho, `HARNESS.md` mein ek line per fix log karte hue.

**Done jab:** Hafta khatam ho aur aapke paas per-class count ho, aur aap bata sako aapki harness kahan
sab se patli thi — kyunke wahi class dominate karti hai. Same shape ki 2 failures pehli ke baad
**namumkin** ho jani chahiyen.

---

### 7. 🔒 The Fenced Night
**Difficulty:** Medium-Hard · **Time:** 1-2 hrs, phir ek overnight run · **Concept:** 5, 11

Part 5 wali morning-triage loop lo — bilkul wahi files — aur poori tarah fence karo: worktree, no
network (ya chhoti allowlist), gated branches. Phir attack karo: bura-raat wale transcript wala
malicious-injection issue apni queue mein daal do aur raat guzarne do.

**Done jab:** Subah ka log dikhaye har injected action **block** hui thi, aur blocks **loud** thin,
chup nahi. Ek guardrail jo invisibly fire ho, project fail kar deta hai — chahe usne roka hi kyun na ho.

---

### 8. 🔁 The Model Swap (Capstone)
**Difficulty:** Capstone · **Time:** 2-3 hrs, phir teen raatein · **Concept:** 12 (coupling), sab 5 verbs

Apni hardened loop ko teen raaton tak **alag model** pe chalao. Jo bhi tootay ya shift ho log karo:
budgets, wordiness thresholds, prompt habits jo purani model bardasht karti thi.

**Done jab:** Har failure ko **behavior-coupling** se **contract-coupling** (exit codes, schemas, tests)
mein move kar ke fix kar diya ho, aur loop **dono** models pe clean chale. Yehi proof hai ke harness
**aapki** hai, kisi ek model ki nahi.

---
[⬅ Dogfooding](06-dogfooding.md) · [Agla: Appendix (Hook Pipeline) ➡](08-appendix-hook-pipeline.md) · [⬆ Index](README.md)
