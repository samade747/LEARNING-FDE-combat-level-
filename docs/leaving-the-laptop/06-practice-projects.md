# 06 — Practice Projects (8 Moves)

8 moves, easy se hard tak. Wahi 2 rules: **throwaway repo**, aur **failure khud plant karo**. Ghar sirf
us buri raat se proof hota hai jo wo survive kare.

---

### 1. 📁 The Headless Wrapper
**Difficulty:** Easy · **Time:** 30-45 min · **Concept:** 3

Apni loop ki beat ko ek script mein wrap karo: headless invocation, exit code check, failure kisi aisi
jagah loud ho jo aap asal mein dekhte ho.

**Done jab:** Network cable nikal kar chalane se **alarm** aye, chup nahi. Chup ka matlab success hona
chahiye — is course ki har cheez isi pe khari hai.

---

### 2. ⏰ The First Scheduled Beat
**Difficulty:** Easy-Medium · **Time:** 1-2 hrs · **Concept:** 4

Wrapper ko ghar 2 mein schedule pe daalo (Routine, ya Actions `schedule:` trigger), config repo se
source ho.

**Done jab:** Ek beat laptop band ke sath chal chuki ho, aur aap bata sako result kahan gaya. Kit ki
pehli 3 rows bhi kisi na kisi form mein exist karein: idempotency, missed-run detection, concurrency
lock.

---

### 3. 🧳 The Suitcase Audit
**Difficulty:** Medium · **Time:** 45-60 min · **Concept:** 7

Apna config, cases, aur fixtures walk karo. Har wo item list karo jo discipline layer ke andar chhupi
mechanics hai: absolute paths, machine names, prose mein baked flags.

**Done jab:** List committed ho aur top 3 fix ho chuke hon. Kam se kam ek milne ki umeed rakho — Part 4
ki story invented nahi thi.

---

### 4. 📏 The Arrival Protocol
**Difficulty:** Medium · **Time:** 1-2 hrs · **Concept:** 8

Naye ghar mein poora golden set chalao. Misses ko category se sort karo. Naya baseline runtime label ke
sath record karo.

**Done jab:** `baseline.json` mein `runtime:` field ho aur har miss ka written verdict ho: noise, suite
bug, ya real — real ones ka fix shipped ho.

---

### 5. 🌙 Probation
**Difficulty:** Medium · **Time:** 1 hr, phir 2 hafte raatein · **Concept:** 4, 8

Kam se kam ek poora operating cycle aur 10 scheduled beats naye ghar mein, roz naye baseline ke against
check, purana ghar available. Beech mein ek failure plant karo.

**Done jab:** 10 beats green hon, planted alarm aap tak pohanch chuka ho, aur purani schedule delete ho
chuki ho. Log ke top pe likho *"initial operational evidence"* — kyunke yehi 10 beats hain.

---

### 6. 🗺️ The Four Questions, In Writing
**Difficulty:** Medium · **Time:** 45-60 min · **Concept:** 9, 10

Har loop jo aap asal mein chalate ho, uske liye Q1-Q4 ek committed markdown file mein answer karo, har
ek ka ant ek ghar aur speed limit pe karo.

**Done jab:** Koi is file ko akela parh kar bata sake har loop kahan rehti hai aur kyun. Aur kam se kam
ek loop ka jawab aapko itna surprise kare ke aap usay move kar do.

---

### 7. 🏢 One Session in Home 3
**Difficulty:** Medium-Hard · **Time:** 2-3 hrs · **Concept:** 5, 6
*(Claude Code track. OpenCode readers: Project 2 ke runner ko harden karo — credentials rotated, updates
scheduled, uptime checked.)*

Live docs se ek managed agent, ek environment, ek session banao jo golden set se ek graded case chalaye.
Event log end-to-end parho. Active-runtime meter pehle aur baad mein note karo.

**Done jab:** Aap apni run se bata sako: log ne kya dikhaya, kya nahi dikha saka, session ki keemat kya
thi. 3 sentences, Project 6 file ke sath committed.

---

### 8. 🔥 The Vanishing-Home Drill (Capstone)
**Difficulty:** Capstone · **Time:** 2 hrs, phir ek quarter ka sabr · **Concept:** 11

Sirf repo se (koi vendor console, koi purani machine nahi), apni loop ke ghar ki ek fresh copy configure
karo aur baseline tak le jao. Time karo. Drill ko quarterly schedule karo.

**Done jab:** Fresh ghar poori suite pass kare, aur written time-cost aapka **measured lock-in** ho. Agar
drill fail ho, aap ne leak dhoond li jab wo abhi ek item chhoti thi — yehi poora point hai.

---
[⬅ Staying Honest](05-staying-honest.md) · [⬆ Index](README.md)
