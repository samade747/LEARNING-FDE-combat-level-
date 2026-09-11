# 4. The First Reporting Schedule

**Type:** No-code, browser practice (runs across a week). **Difficulty:** Medium · **Time:** 30 min
setup, phir 1 hafta wait. **Concept:**
[9 — Scheduled Tasks](../../02-working-unwatched.md#concept-9-scheduled-tasks--bina-kisi-device-online-ke)

**Boundary jo yaad rakhna hai:** yeh drill sirf **reporting** schedule banati hai (parhna, synthesize
karna, brief banana) — **acting** schedule (bhejna, file karna, decide karna) abhi nahi, uske liye Loop
Engineering course chahiye (checker + stopping condition + state file).

## Setup

Koi installation nahi. Chahiye: Claude Cowork ya ChatGPT Work, ek connector (jaise Google Drive/Gmail
read-only) ya ek file source jo hafte mein badalti ho.

## Steps

Scheduled task banane se pehle, **4 jawab likh kar taiyar karo** (order mein):

1. **Kya karna hai?** Standing brief likho — aur ek zaroori line add karo empty case ke liye:
   *"Agar is hafte kuch naya nahi hai, ek line note produce karo"* (chup hafta aur chup failure mein
   farq yehi line karti hai).
2. **Kya touch kar sakta hai?** Files/platform storage, naam se list karo.
3. **Kya reach kar sakta hai?** Connectors, listed — sirf wohi jo brief ke liye zaroori hain.
4. **Kab shuru hota hai?** Cadence chuno (jaise "Monday 8am") — yaad rakho iska matlab **around** Monday
   8am hai, exact nahi.

Phir:

5. **Metered math likh kar karo** pehle: kitne runs/hafta yeh use karegi, plan ki limit kitni hai —
   collision se pehle confirm karo.
6. Task ko pehle **haath se, watched, kam se kam ek dafa chalao** — kabhi wo cheez schedule mat karo jise
   abhi trust nahi karte chhor kar jane ke liye.
7. Schedule set karo, phir **1 hafta wait karo** bina check kiye (sirf notification/inbox check karna
   allowed hai, session manually re-run mat karo).

## Done Jab (Self-Check)

- [ ] Task **2 dafa fire ho chuki hai** — koi device online kiye bagair
- [ ] Har result mein ek **success signal** hai (na ke sirf "run complete ho gaya") — jaise task ne khud
      confirm kiya ke usay kya mila ya "kuch naya nahi tha"
- [ ] Bata sakta hoon farq: **"complete hui run"** vs **"successful task"** — scheduler ka kaam "chali"
      tak khatam hota hai, "sahi thi" uska business nahi
- [ ] Bata sakta hoon yeh **reporting** schedule kyun hai, **acting** schedule kyun nahi (1-word farq:
      "acts" — is task ne bahar duniya pe kuch nahi kiya, sirf parha aur likha)

---
[⬅ Practice Projects Index](../../04-practice-projects.md) · [Chapter Index](../../README.md)
