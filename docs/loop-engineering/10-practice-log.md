# 10 — Practice Log (Meri Apni Hands-On Progress)

*Yeh file [06-practice-projects.md](06-practice-projects.md) se alag hai. Woh file bata ti hai
**"kaise karna hai"** (mechanical steps, maine khud scaffolds test kiye). Yeh file record karti hai
**"maine khud kya kiya"** — user ka apna practice run, ek project ke baad ek, checkbox ke sath.*

**Rule:** ek project ka checkbox tab hi tick hota hai jab uska **"Done jab"** criteria khud dekh liya
ho — sirf steps parh lena kaafi nahi.

---

## Progress Checklist (12 Projects)

| # | Project | Status | Practice Notes |
| --- | --- | --- | --- |
| 1 | 👀 Watch Loop (ISS) | ✅ Done | User ne confirm kiya — real ISS position aa rahi thi har minute |
| 2 | ✅ Tests Pass Then Stop (Portfolio) | 🔶 In progress | apna CV/LinkedIn PDF chahiye — abhi shuru |
| 3 | 🧠 Morning Brief w/ Memory (Sky Watch) | ⬜ Not started | — |
| 4 | 🔍 Fix Loop w/ Real Checker | ⬜ Not started | — |
| 5 | 🧩 Codify the Body | ⬜ Not started | Project 4 par build hota hai |
| 6 | 🔔 Doorbell Loop | ⬜ Not started | apna GitHub repo + App install chahiye |
| 7 | 🔦 Break It On Purpose | ⬜ Not started | Project 3 par build hota hai |
| 8 | 🔁 Daily Loop (Capstone) | ⬜ Not started | — |
| 9 | 🎭 Rehearse for Free | ⬜ Not started | claude.ai account chahiye |
| 10 | 🔐 Secrets Drill | ⬜ Not started | claude.ai account chahiye |
| 11 | 🚦 Two-Routine Gate | ⬜ Not started | claude.ai account chahiye |
| 12 | 💭 Dreaming Capstone | ⬜ Not started | claude.ai account chahiye |

Status legend: ⬜ Not started · 🔶 In progress · ✅ Done (self-check pass ho gaya)

---

## Project 1 — Watch the ISS *(abhi shuru karo)*

**Concept:** in-session loop — timer pe chalti hai jab tak session khula hai.
**Time:** 15-30 min · **Difficulty:** Easy

### Steps

1. Naya, alag terminal kholo (throwaway rule — apni kaam wali session mat use karo):
   ```bash
   cd docs/loop-engineering/projects/iss-loop
   claude
   ```
2. "Do you trust this folder?" puche to **yes** bolo.
   > Agar "no" bola, `.claude/settings.json` ke narrow rules ignore ho jayenge aur har minute
   > permission prompt aayega — yehi is project ka pehla gotcha hai.
3. Sirf yeh ek line type karo:
   ```
   /loop show me the location of the ISS every minute
   ```
4. Kuch mat karo. Har minute naya position card aayega (lat/long, altitude, speed, sunlight).
5. Jab dekh lo, **Esc** dabao — clean stop.

### Done jab (self-check)

- [x] Loop bina poochhe khud har minute update deti hai
- [x] Aap **Esc** se clean ruk sakte ho
- [x] Terminal band karke dekha — watching mar gayi (in-session loop apni session se bahar nahi
      jeeti, yeh core lesson hai)

**✅ Complete** — real ISS position confirm hui, har minute update aata dekha.

**Windows gotcha:** 🛰 emoji pe `UnicodeEncodeError` aaye to `PYTHONIOENCODING=utf-8` set karo (sirf
direct script run mein, `/loop` ke andar yeh bug nahi dekha gaya).

**Full detail:** [`projects/iss-loop/README.md`](projects/iss-loop/README.md)

---

## Project 2 — Build Your Portfolio *(agla)*

**Concept:** run-until-done loop, command decide karta hai stop kab hoga, agent nahi.
**Time:** 30-45 min · **Difficulty:** Easy-Medium

### Steps (jab Project 1 done ho)

1. Apna CV ya LinkedIn PDF `docs/loop-engineering/projects/portfolio-starter/` folder mein daalo.
2. Us folder mein `claude` chalao, trust karo.
3. Yeh `/goal` prompt do:
   ```
   /goal Build my portfolio in site/ from my-cv.pdf... Done when check.py prints 20/20
   and the reviewer agent replies PASS on all six judgment promises...
   Stop after 15 check attempts or 3 review rounds.
   ```
4. Loop khud draft → check → fix cycle chalayegi, jab tak `check.py` 20/20 na de ya cap na hit ho.

### Done jab (self-check)

- [ ] Loop **asal** mein tests pass hone se ruki, cap hit hone se nahi
- [ ] `check.py` kabhi edit nahi kiya taake wo pass ho jaye (golden rule)

**Full detail:** [`projects/portfolio-starter/README.md`](projects/portfolio-starter/README.md)

---

## Baaki Projects (3-12)

In par abhi mat jao — Project 1 aur 2 pehle. Jab wahan pahonch jao, is file mein wahi structure
(Steps → Done jab → checkbox tick) add karte jayenge, aur `06-practice-projects.md` se full detail
link karte rahenge:

- Project 3 — [`sky-watch/README.md`](projects/sky-watch/README.md)
- Project 4 — [`fix-loop-demo/README.md`](projects/fix-loop-demo/README.md)
- Project 5, 7 — [`CODIFY-AND-SABOTAGE.md`](projects/CODIFY-AND-SABOTAGE.md)
- Project 6 — [`doorbell/README.md`](projects/doorbell/README.md)
- Project 8 — [`daily-triage-demo/README.md`](projects/daily-triage-demo/README.md)
- Projects 9-12 — [`08-routine-drills-and-dreaming.md`](08-routine-drills-and-dreaming.md)

---
[⬅ Commands Cheat Sheet](09-commands-cheat-sheet.md) · [⬆ Index](README.md)
