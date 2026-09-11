# 2. The Three-Tier Audit

**Type:** No-code, browser practice. **Difficulty:** Easy · **Time:** 30 min · **Concept:**
[5 — 3 File Tiers](../../01-the-surface.md#concept-5-3-file-tiers--is-course-ka-sab-se-zaroori-concept),
[8 — Delegation Loop](../../02-working-unwatched.md#concept-8-delegation-loop--brief-plan-approve-review)

Is course ka sab se zaroori concept khud tarikha maangta hai, doc parhna kaafi nahi: **"Finished work
exits the platform. Everything else may stay."** Yeh drill aapko apne khud ke kaam mein 3 tiers dikhwati
hai — Tier 1 (task filesystem, khud khatam), Tier 2 (platform storage, vendor ki custody), Tier 3 (exit —
aapka apna system of record).

## Setup

Koi installation nahi. Claude Cowork ya ChatGPT Work ka access.

## Steps

1. Ek **real task chuno** jo ek deliverable banaye (ek report, ek plan, ek draft — kaam jo aap waise bhi
   karte).
2. Apni brief **poori Concept 8 shape** mein likho — 4 hisse:
   - **Outcome + audience + constraints** (Step 1: Brief)
   - `Lay out your plan first, and pause for my approval before doing anything.` (Step 2: Plan)
   - Plan ko 4 cheezon se check karo before approving: **scope, order, reach, assumptions**
   - Closing lines (Step 4: Review):
     ```text
     Before you start: ask me 1-2 clarifying questions.
     If any sources contradict each other on a material point, flag the
     contradiction in the deliverable. Do not silently pick one.
     End by listing every file you created and where each one landed:
     temporary working space, platform storage, or a system I control
     (connector save, download, local write, or repo commit).
     ```
3. Task chalao poori tarah — brief, plan-approve, run, review.
4. Jab khatam ho, agent ki closing file-list padho. **Har file ko khud bhi tier assign karo** — agent
   ke jawab se independently (yehi asal audit hai).

## Done Jab (Self-Check)

- [ ] Har file ka tier bata sakta hoon — Tier 1 (scratch, khud khatam), Tier 2 (platform, safe lekin
      vendor ki custody), ya Tier 3 (mera apna control — Drive/email/download/repo)
- [ ] Deliverable khud **Tier 3 mein exist karta hai** — sirf platform pe nahi. Agar nahi, wahi galti
      hai jo drill pakadne ke liye bani hai
- [ ] Bata sakta hoon Tier 2 kyun "aaj safe, kal hostage" hai — safe kyunke bachti hai, hostage kyunke
      sirf wahin bachti hai, kisi aur ki login ke peeche

---
[⬅ Practice Projects Index](../../04-practice-projects.md) · [Chapter Index](../../README.md)
