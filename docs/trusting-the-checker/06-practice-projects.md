# 06 — Practice Projects (8 Eval Builds)

Easy se hard tak 8 builds. Wahi 2 rules hamesha: **throwaway repo**, aur **failure khud plant karo**.
Suite sirf us miss se proof hoti hai jo wo pakre.

---

### 1. 📁 The First Five Cases
**Difficulty:** Easy · **Time:** 30-45 min · **Concept:** 4-5

Apni `HARNESS.md` (ya harness course ki stories) se 5 entries lo aur har ek ko case file ki tarah likho:
input, expected behavior, unacceptable patterns, `origin` line.

**Done jab:** Folder commit ho chuka ho aur har hard case ek real event point kare. Koi runner abhi nahi
— **cases hi asset hain.**

---

### 2. 🐚 The Runner
**Difficulty:** Easy-Medium · **Time:** 45-60 min · **Concept:** 5

Apne tool ke liye `evals/run.sh` likho: har case pe 3 runs, jq grading, printed rate. Project 1 ke folder
pe chalao.

**Done jab:** Ye ek rate print kare, aur jab aap jaan-boojh kar ek case ki fixture tor do, rate gir jaye.
**Jo runner fail nahi ho sakta wo runner nahi hai.**

---

### 3. 📏 The Anchored Rubric
**Difficulty:** Medium · **Time:** 45-60 min · **Concept:** 6

Apne reviewer ki rubric lo aur har score ko pichli runs se pasted real example se anchor karo. Har
impression question ko fact question se replace karo.

**Done jab:** Koi ajnabi aapki rubric se 3 items grade kar sake aur wahin pohanche jahan aap pohanchte.
Literally test karo — kisi ko de do.

---

### 4. ⚖️ Grade Your Grader
**Difficulty:** Medium · **Time:** 1-2 hrs · **Concept:** 7

4-step protocol chalao: 20 graded items sample karo, blind grade karo, compare karo, agreement rate
calculate karo.

**Done jab:** Aapke paas ek written calibration score ho aur worst disagreement se ek rubric fix. Agar
agreement perfect thi, sample bohat easy tha.

---

### 5. 🚧 The Gate
**Difficulty:** Medium · **Time:** 1-2 hrs · **Concept:** 8

`baseline.json` commit karo, eval job CI mein add karo harness-file changes pe, branch protection mein
require karo. Phir ek PR kholo jo jaan-boojh kar reviewer prompt bigare.

**Done jab:** Wo PR eval job se block ho jaye, aur ek harmless PR pass ho jaye. **Dono half matter
karte hain.**

---

### 6. 🌙 The Night Watch
**Difficulty:** Medium · **Time:** 1 hr, phir ek hafta raatein · **Concept:** 9

Poori suite ko nightly schedule pe daalo (Routine/scheduled Action), loud alert ke sath kisi bhi baseline
se neeche girne pe.

**Done jab:** Ek hafte ki raatein chal chuki hon, chup ka matlab baseline ho, aur aap ne alarm ek dafa
test kiya ho temporary rubric bug plant kar ke.

---

### 7. 🕵️ The Injection Category
**Difficulty:** Medium-Hard · **Time:** 1-2 hrs · **Concept:** 6, 10, harness course

3 injection cases likho (diff comment mein chhupi instructions, issue body, tool output fixture),
category bar ko 100% set karo, chalao.

**Done jab:** Aapko apne reviewer ka real number pata ho adversarial input pe, aur agar ek miss hui,
fix rubric mein gaya aur re-run green aya.

---

### 8. 🔒 The Sealed Hold-Outs (Capstone)
**Difficulty:** Capstone · **Time:** 1-2 hrs, phir hafton ka sabr · **Concept:** 11

5 hold-out cases likho, seal karo (ek alag folder jo daily workflow kabhi na khole), weekly schedule
karo, ek mahine ke liye dono rates side-by-side record karo.

**Done jab:** Aapke paas ek mahine ki tuned-vs-hold-out history ho aur aap numbers ke sath bata sako kya
Goodhart's law aapki suite pe shuru ho chuka hai. **Badhta gap sab se pehli honest warning hai jo aapko
kabhi milegi.**

---
[⬅ Staying Honest](05-staying-honest.md) · [⬆ Index](README.md)
