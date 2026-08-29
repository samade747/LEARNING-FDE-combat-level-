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
7. [06 — Dogfooding: Yeh Kitaab Khud Apne Loops Kaise Use Karti Hai](06-dogfooding.md)
8. [07 — Practice Projects (Projects 1-8)](07-practice-projects.md)
9. [08 — Routines Appendix: Field Guide (A1-A6)](08-routines-appendix.md)
10. [09 — Routine Drills (9-11) + Dreaming Capstone (12)](09-routine-drills-and-dreaming.md)
11. [10 — Commands Cheat Sheet (sab commands ek jagah)](10-commands-cheat-sheet.md)
12. [11 — Practice Log (meri apni hands-on progress, project-by-project)](11-practice-log.md)
13. [12 — Key Words Glossary (plain-English terms)](12-key-words-glossary.md)
14. [13 — Where to Go Next (book ke apne pointers)](13-where-to-go-next.md)
15. [14 — Sources & Further Reading](14-sources-further-reading.md)
16. [15 — Test Your Understanding (61-question exam assessment)](15-test-your-understanding.md)

## Runnable Projects — Poore 12, Har Ek Ki Real Jagah

| Project | Concept | Summary | README (run steps) | Status |
| --- | --- | --- | --- | --- |
| 1 — Watch Loop | 4 (in-session) | [`iss-loop/SUMMARY.md`](projects/iss-loop/SUMMARY.md) | [`iss-loop/README.md`](projects/iss-loop/README.md) | ✅ Official kit, live tested — real ISS position |
| 2 — Build Your Portfolio | 5 (run-until-done) | [`portfolio-starter/SUMMARY.md`](projects/portfolio-starter/SUMMARY.md) | [`portfolio-starter/README.md`](projects/portfolio-starter/README.md) | ✅ Official kit, `check.py` tested (aapka CV chahiye poora chalane ke liye) |
| 3 — Sky Watch | 6 (schedule) | [`sky-watch/SUMMARY.md`](projects/sky-watch/SUMMARY.md) | [`sky-watch/README.md`](projects/sky-watch/README.md) | ✅ Official kit, live tested — real NASA data |
| 4 — Fix Loop With a Real Checker | 8, 9, 11 | [`fix-loop-demo/SUMMARY.md`](projects/fix-loop-demo/SUMMARY.md) | [`fix-loop-demo/README.md`](projects/fix-loop-demo/README.md) | ✅ DIY scaffold banaya, khud test kiya — planted bug 2/3 tests fail karta hai |
| 5 — Codify the Body | Dynamic workflows | [`CODIFY-AND-SABOTAGE.md`](projects/CODIFY-AND-SABOTAGE.md) | (isi file mein) | 📋 Instructions (Project 4 par build hota hai, naya code nahi chahiye) |
| 6 — The Doorbell | 7 (event-driven) | [`doorbell/SUMMARY.md`](projects/doorbell/SUMMARY.md) | [`doorbell/README.md`](projects/doorbell/README.md) | ✅ Official kit, copied (aapka GitHub repo + App install chahiye) |
| 7 — Break It On Purpose | Observability, 13, 14 | [`CODIFY-AND-SABOTAGE.md`](projects/CODIFY-AND-SABOTAGE.md) | (isi file mein) | ✅ Sky-watch version live tested — 2 sabotage runs, dono clean fail |
| 7 (easy version) — Joke Loop | Observability, 13, 14 | [`joke-loop/README.md`](projects/joke-loop/README.md) | [`joke-loop/README.md`](projects/joke-loop/README.md) | ✅ DIY, simpler stand-in — koi API key nahi, ~60-line script |
| 8 — Your Own Daily Loop (Capstone) | Sab 6 parts | [`daily-triage-demo/SUMMARY.md`](projects/daily-triage-demo/SUMMARY.md) | [`daily-triage-demo/README.md`](projects/daily-triage-demo/README.md) | ✅ DIY scaffold banaya, khud test kiya — bug + risky-issue dono confirm |
| Bonus — Paper Watch | 12 (spine) | [`paper-watch/SUMMARY.md`](projects/paper-watch/SUMMARY.md) | [`paper-watch/README.md`](projects/paper-watch/README.md) | ✅ Official kit, live tested — spine confirmed |
| 9 — Rehearse a Routine For Free | Appendix A1/A3/A5 | [`09-routine-drills-and-dreaming.md`](09-routine-drills-and-dreaming.md) | (isi file mein) | ✅ Done — 2 one-off runs, dono honest failure diagnosis |
| 10-11 — Routine Drills | Appendix A2/A4 | [`09-routine-drills-and-dreaming.md`](09-routine-drills-and-dreaming.md) | (isi file mein) | 🖐️ Setup ready — env-vars panel / webhook trigger claude.ai UI se |
| 12 — Dreaming Capstone | Concept 12 (spine + dreaming) | [`dreaming-loop/README.md`](projects/dreaming-loop/README.md) | [`dreaming-loop/RUN-LOG.md`](projects/dreaming-loop/RUN-LOG.md) | ✅ Done — real cloud routine, planted patterns pakre, PR [my-doorbell#2](https://github.com/samade747/my-doorbell/pull/2) |

**Dogfooding note:** yeh kitaab khud 2 production loops se chalti hai (feedback loop + What's New loop)
— dekho [`06-dogfooding.md`](06-dogfooding.md). Book ka apna live proof ke loop parts kaam karte hain.

**Har project folder mein 2 files:** `SUMMARY.md` (kya sikhata hai, kyun zaroori hai, kaise kaam karta
hai — chota, conceptual) aur `README.md` (isay actually chalane ke exact steps — mechanical).

**Legend:** ✅ = maine khud banaya/copy kiya aur test kiya (real output verify hua). 📋 = instructions
ready, kisi existing project par build hoti hai. 🖐️ = cloud/account-gated feature, sirf aap khud kar
sakte ho — poori step-by-step guide di hui hai.

## Ek line mein poori cheez

> Pehle aap agent ko **prompt** karte thay, turn by turn. Ab aap ek **loop** design karte hain —
> ek system jo khud start hota hai, kaam dhoondta hai, karta hai, check karwata hai, yaad rakhta hai,
> aur sirf zaroori (risky) decisions ke liye aapko bulata hai. Aapki value **prompt** se **loop design**
> mein shift ho gayi hai — lekin do cheezein hamesha aapki rahengi: **intent** (kya chahiye) aur
> **accountability** (zimmedari).
