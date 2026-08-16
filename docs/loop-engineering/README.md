# Loop Engineering — Notes (Roman Urdu + English)

Ye notes **"Loop Engineering: A Crash Course"** chapter ka easy explainer hain, jo Panaversity ke
**The AI Agent Factory** book se liya gaya hai (Zia Tutor AI connector ke zariye).

Source: https://agentfactory.panaversity.org/docs/loop-engineering-crash-course

## Index

1. [00 — Overview: Loop Engineering kya hai](00-overview.md)
2. [01 — Heartbeats: Loop kab start hota hai](01-heartbeats.md)
3. [02 — Body: Loop har run mein kya karta hai](02-body.md)
4. [03 — Spine: Runs ke darmiyan memory](03-spine.md)
5. [04 — Ek Complete Loop (Morning Triage Example)](04-complete-loop-example.md)
6. [05 — Human Control: Insaan loop mein kahan khara hai](05-human-control.md)
7. [06 — Practice Projects (Projects 1-8)](06-practice-projects.md)
8. [07 — Routines Appendix: Field Guide (A1-A6)](07-routines-appendix.md)
9. [08 — Routine Drills (9-11) + Dreaming Capstone (12)](08-routine-drills-and-dreaming.md)

## Runnable Projects

- [`projects/iss-loop/`](projects/iss-loop/README.md) — **Project 1 (Watch Loop)** ka real, ready-to-run
  code. Official Panaversity `agentfactory-labs` repo se yahan copy kiya gaya hai. Isi folder mein
  `claude` chalao aur `/loop show me the location of the ISS every minute` type karo.

## Ek line mein poori cheez

> Pehle aap agent ko **prompt** karte thay, turn by turn. Ab aap ek **loop** design karte hain —
> ek system jo khud start hota hai, kaam dhoondta hai, karta hai, check karwata hai, yaad rakhta hai,
> aur sirf zaroori (risky) decisions ke liye aapko bulata hai. Aapki value **prompt** se **loop design**
> mein shift ho gayi hai — lekin do cheezein hamesha aapki rahengi: **intent** (kya chahiye) aur
> **accountability** (zimmedari).
