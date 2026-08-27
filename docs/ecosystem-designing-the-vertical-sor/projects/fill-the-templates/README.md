# Practice Project — Fill The Templates

**Chapter:** [Designing the Vertical System of Record from First Principles](../../README.md)
**Type:** Worksheet-style (no code) — jaisa harness-engineering ka `tool-diet`/`ratchet-week`
**Time:** 2-4 ghante (ek sitting mein, ya kai sessions mein)
**Difficulty:** Medium

## Yeh Project Kya Hai

Chapter ke [7 templates](../../06-templates.md) sirf parhne ke liye nahi hain — yeh woh **working
documents** hain jo tum apni asal System of Record banate waqt fill karte ho. Is project mein tum apna
koi bhi profession/vertical choose karoge (apna khud ka, ya ek jo tum jaante ho — teaching, freelancing,
accounting, recruitment, kuch bhi), aur uske ek outcome par poora method chalaoge: outcome likhna se
lekar evaluation set tak.

Iska koi code nahi hai. Yeh ek structured exercise hai — bilkul waisa jaise Ayesha ne apni khala ki
checklist par kiya ([05 — Failure Modes + Ayesha](../../05-failure-modes-and-ayesha.md) dekho). Ayesha ka
worked example is folder mein `reference-solution-ayesha.md` ki tarah diya gaya hai — apna kaam usse
compare karo, copy nahi.

## Setup

Koi setup nahi chahiye. Bas:

1. [`worksheet.md`](worksheet.md) ko copy karo (apni khud ki file mein, ya isi repo mein edit karo agar
   tum sirf practice kar rahe ho).
2. Ek profession/vertical choose karo jo tum kam se kam thoda jaante ho — ideally kisi aisi cheez ka jo
   tumne khud kabhi ki ho ya kisi ko karte dekha ho (teaching, tutoring, freelance proposals, customer
   support, event planning — kuch bhi chalega, sirf **ek real workflow** hona chahiye jise tum yaad kar
   sako).
3. Worksheet ko top se neeche fill karo. Order matter karta hai — outcome pehle, sort baad mein, reflex
   sabse aakhir mein (chapter ka apna order hai: [01](../../01-outcome-and-archaeology.md) →
   [02](../../02-three-bin-sort-and-hierarchy.md) → [04](../../04-decisions-rules-exceptions-reflexes.md)).

## Steps

1. **Outcome Contract (Template 1).** Apna outcome likho — weak outcome se shuru mat karo ("processes
   automate karo"), strong outcome likho ("X decide karo, evidence Y ke sath, Z tak ready").
2. **Sort Record (Template 2).** Apne chune hue workflow ke 8-10 elements list karo (steps, checks,
   approvals, reports). Har ek ko Bin 1/2/3 mein sort karo, reason ke sath.
3. **Invariants List (Template 3).** Sirf Bin 1 se — 3-6 invariants likho, chhoti list rakho.
4. **Source Register (Template 4).** 3-5 sources list karo jo tumhare outcome ko govern karte (law,
   policy, tumhari apni expertise/rules-of-thumb).
5. **Decision Map (Template 5).** 4-6 decisions list karo jo outcome ke liye chahiye — departments nahi,
   decisions.
6. **Exception Entry (Template 6).** Kam se kam 2 exception shapes likho, normal path finish karne se
   pehle.
7. **Coverage Register (Template 7).** Ek row — apna outcome, "probe" state mein (kyunke abhi real
   evaluation set nahi hai).
8. **Ek Reflex Derive Karo.** Worksheet ke aakhri section mein, apne outcome + invariants ke around ek
   chhota reflex likho (5-8 steps, expert ki apni voice mein — jaisa Ayesha ne kiya).
9. **Evaluation Set.** Kam se kam 3 **non-happy-path** cases likho (missing evidence, conflicting
   evidence, ya forbidden-action request jaisi cases) — sirf clean case nahi.

## Done Jab (Self-Check)

- [ ] Apna vertical/outcome choose kar liya, aur outcome contract likh diya (weak outcome nahi, strong)
- [ ] Source register mein kam se kam 3 sources hain, har ek ka apna authority-class/scope
- [ ] Purane workflow ka three-bin sort kiya — kam se kam 8 elements, har ek apni reason ke sath
- [ ] Kam se kam ek reflex derive kiya, expert ki apni voice mein (na ke "purani SOP ko markdown mein
      convert" — failure mode 2 se bacho)
- [ ] Ek exception list bana, kam se kam 2 shapes ke sath (detection + Worker may/must-not + escalation)
- [ ] Evaluation set mein 3+ non-happy-path cases hain (sirf clean case nahi — [failure mode 6](../../05-failure-modes-and-ayesha.md#the-failure-modes)
      "happy-path demo" se bacho)
- [ ] `reference-solution-ayesha.md` se apna kaam compare kiya — kya tumhare invariants sach mein
      invariants hain (violation = invalid/unlawful/untrustworthy), ya woh sirf guidance hain?

---
[⬅ Chapter Index](../../README.md)
