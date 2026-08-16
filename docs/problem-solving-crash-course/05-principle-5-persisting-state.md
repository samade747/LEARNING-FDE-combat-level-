# 05 — Principle 5: Persisting State in Files

> **Failure mode:** "Agent kal kya decide hua tha bhool kyun jata hai?"

Conversation band karo, AI sab bhool jata hai. Dobara kholo, koi memory nahi ke kya discuss hua tha, kya
decisions the, kya rules the. Har baar zero se explain karna parta hai.

**Fix:** Zaroori info ko **file mein save karo.** Files hamesha rehti hain; conversations gayab ho jati
hain.

Sabse important file hai **rules file**: Claude Code/Cowork mein `CLAUDE.md`, OpenCode/OpenWork mein
`AGENTS.md`. Yeh short text file hai jo AI **har session ke shuru mein khud parhta hai.**

## Rules File Kaisi Dikhti Hai

`/init` command chalao (aapke folder ko scan kar ke pehla draft banata hai). Sirf naam farq hai
`CLAUDE.md` vs `AGENTS.md`. (OpenCode `CLAUDE.md` ko bhi fallback ki tarah parh leta hai.)

**Kitni lambi honi chahiye:**
- Pehla draft: 250 words se kam
- Kuch hafton baad: 60 lines se kam — har line isliye ho ke bina uske kuch ghalat hua tha
- Agar 500 words se zyada hai, aap isay documentation ki tarah use kar rahe ho — details alag files
  mein le jao

> **Sabse common mistake: yeh file zyada lambi bana dena.** AI isay **har message** par parhta hai.
> Bari file AI ko slow karti hai, chahe zyada tar content relevant na ho. **Isay table of contents
> samjho, encyclopedia nahi.**

**Shape jo sab tools mein chalti hai:**

```text
# Project: [name]

## What this is
[Two lines: domain, audience]

## Where things live
- folder-a/: [what's in it]

## Critical rules
- [The one mistake people keep making]
- [A non-obvious convention]
- [A thing that's expensive to undo]

## On-demand references
- @docs/conventions.md
```

## Ek Doosra Persistence Pattern: Plan Files

Multi-session tasks ke liye, plan `docs/plans/feature-name.md` mein save karo. Ek message mein resume
karo: *"plans/q4-launch.md parho aur step 4 se continue karo."*

> **Hierarchy:** Conversation = volatile. Project folder ki files = durable. Referenced files = on-demand.

## Jab Files Kaafi Na Hon: Database

Agar har naya sawal code rewrite maange (jaise expense totals se "food spending by month" poochna), to
approach files se aage nikal chuki hai. Fix: data database mein daalo (Neon par free, 60 second mein).
Ab har naya sawal ek query hai.

## Hands-On Practice

Course "Pack 6 — Hiring loop persistence" deta hai: 5 resumes. **Run A** (koi rules file nahi): AI sab
resumes evaluate karta hai, Carlos ko uski MBA/titles ki wajah se ADVANCE deta hai. **Phir** ek
`CLAUDE.md` banwate hain jisme credential-verification rule hai. **Run B** (identical prompt, rules file
maujood): AI khud rule follow karta hai — pata chalta hai Carlos ki MBA 2018 ki hai lekin uska school
2019 tak exist hi nahi karta tha. Carlos ab HOLD hota hai.

**Key insight:** Run B prompt mein credentials ka zikr nahi tha. Rule isliye chala kyunki file mein tha
jo AI khud parhta hai. **Jo file mein hai, AI follow karta hai. Jo nahi hai, AI bhool jata hai.**

## Apne Kaam Par Apply Karo

1. Woh folder chuno jahan aap baar baar wapas ate ho aur wahi cheezein repeat karte ho.
2. AI se khud pehla draft likhwao (khud memory se mat likho):
   ```text
   Read this folder. Draft a CLAUDE.md (or AGENTS.md) under 250 words:
   what this project is, where things are stored, 3-5 rules I would
   normally have to explain manually, and 3 rules that would cause real
   problems if you got them wrong.
   ```
3. Generic lines hatao ("be professional" jaisi). Sirf **is folder ke liye specific** rules rakho.
4. Test karo: same kaam dobara karo bina rules repeat kiye. Jo bhi repeat karna pare, woh missing line
   hai — add karo.

---
[⬅ Principle 4](04-principle-4-decomposition.md) · [⬆ Index](README.md) · [Agla: Principle 6 ➡](06-principle-6-constraints-safety.md)
