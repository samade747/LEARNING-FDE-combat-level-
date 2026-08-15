# 05 — Staying Honest: Goodhart's Law Aur Limits

## Concept 11: Goodhart's Law — Jab Measure Target Ban Jaye

Discipline ka ek dushman bacha hai, aur ye discipline **khud** hai. **Goodhart's law: jab ek measure
target ban jata hai, wo achha measure hona band kar deta hai.** Jis lamhe *"suite ko 33/36 se upar
rakho"* goal ban jaye, sab kuch **unhi 36 verdicts** ke liye optimize hone lagta hai: prompts cases ke
liye tune ho jate hain, rules fixtures ki shape le lete hain, number chadhta hai jab ke behavior jo ye
represent karta tha chup chaap measure hona band ho jata hai. **Suite abhi bhi pass hoti hai. Bas ab
uska matlab kuch nahi.**

**3 defenses, sab sasti:**

- **Hold-outs** — chand cases jo loop ke authors kabhi tune nahi karte — likhi, sealed, sirf weekly
  schedule pe chalti hain. Tuned set aur hold-outs ke darmiyan gap khulna Goodhart's law khud ko dikha
  raha hai — **aap test seekh rahe ho, material nahi**.
- **Production se refresh karo** — naye real failures naye cases banti rehti hain, ratchet pipeline
  kabhi nahi rukta. **Retirement zyada sakht hai jitna lagta hai** — case sirf tab retire karo jab wo
  behavior jo test karti hai exist na kare, ya requirement badal jaye. **High-severity ones (false
  greens, injections) permanently rehti hain.**
- **Agent ko kabhi answer key na dikhne do** — cases aur fixtures loop ki working context se bahar rehte
  hain — na rules file mein, na kisi skill mein jo maker load kare.

> **Safety note:** Attack fixtures **live ammunition** hain. Injection cases mein real attack text hoti
> hai — ek normal session jo `evals/fixtures/` mein bhatak jaye, aapke apne test data se steer ho sakti
> hai. Answer key ko chupane wala rule fixtures pe bhi lagao.

## Concept 12: Evals Kya Prove Nahi Kar Sakte

Trilogy jahan hamesha khatam hoti hai wahin khatam karte hain: **honest boundary** ke sath. Eval suite
aapki confidence un situations pe bound karti hai jo **usmein hain**. Ye un situations ke baare mein
kuch nahi bol sakti jo **usmein nahi hain**: genuinely novel input, aisi failure jo folder mein kisi
jaisi nahi, wo din jab duniya set ke refresh hone se tezi se badal jaye.

> **Calibrated 35/36 known territory ke baare mein ek strong statement hai aur unknown territory ke
> baare mein total khamoshi.** Isi liye 3 courses mein se kisi ne human gate nahi hataya, aur is course
> ne bhi nahi. **Evals wo kam karte hain jo gate tak pohanchta hai aur wo sharpen karte hain jo gate
> dekhta hai. Wo us insaan ki jagah nahi lete jo gate pe khara hai.**

**Bridge aage — Mode 2 ke liye.** Jab aap Mode 2 mein *building* agents shuru karo (custom tools,
knowledge layers, fleets of Digital FTEs), yehi ideas **Eval-Driven Development** course mein scale
hoti hain: aapki 3 depths uska nine-layer pyramid ban jati hain, aapka case folder DeepEval mein golden
datasets ban jata hai, aapka transcript-reading judge trace grading ban jata hai, aapki scheduled
Routine Phoenix (production watching) ban jati hai. **Har concept transfer hota hai. Sirf tooling badhti
hai.**

**Managed option:** **Rubrics in Claude Managed Agents** (beta) rubric-with-a-bar ko built-in platform
feature ki tarah offers karta hai. Ek alag grader agent har outcome ko aapki rubric ke against check
karta hai. **Ye shape jo aap ne haath se banayi, product ki tarah offered hai — lekin managed judge bhi
phir bhi ek model hai.** Usay bhi Concept 7 calibration chahiye trust karne se pehle, aur insaan ko phir
bhi uska bar choose karna hai.

## Closing Thought (Trilogy)

> **Loop ne aapke agent ko waqt diya. Harness ne usay limits diye. Evals usay ek zyada rare cheez dete
> hain: ek track record.** Aur track record, honestly measured, wo akela cheez hai jo kabhi kisi ka
> trust kama saki hai — logon ke liye ya agents ke liye.

### Self-Check
**Sawal:** 2 mahine baad, tuned set 36/36 pe chal raha hai lekin hold-outs 90% se 70% pe gir chuke hain.
Kuch bhi maliciously nahi badla. Kya hua, aur 2 moves kya hain?
**Jawab:** Goodhart's law, apni innocent form mein — hafton ki prompt/rule adjustments har ek unhi 36
verdicts ke against validate hui, isliye system dheere dheere test seekh gaya jab uska general behavior
drift kar gaya. **2 moves:** kai hold-outs ko tuned set mein promote karo (ab wo reality ko behtar
represent karte hain memorized cases se), aur sab se stale **low-severity** cases retire/rewrite karo,
recent production failures se refresh kar ke. High-severity ones rehti hain (Concept 11 ke mutabiq).
Phir re-baseline karo, aur naye hold-outs ka batch seal karo.

---
[⬅ Complete Eval Suite](04-complete-eval-suite.md) · [Agla: Practice Projects ➡](06-practice-projects.md)
