# 06 — 7 Templates + Definition Of Done

Method ko jo bhi chahiye, ek jagah. Saat working templates, usi order mein jis order mein page unhe use
karta hai, aur definition of done. Har ek ko apni System of Record mein copy karo aur wahin fill karo.
**Har filled template khud governed content hai** — usay owner, review, aur version milta hai.

## Template 1: The Outcome Contract

Har professional outcome ke liye ek. Kisi bhi workflow study se pehle likha jata hai.

| Field | Tumhari Entry |
| --- | --- |
| Outcome (woh completed result jo exist karna chahiye) | |
| Trigger (woh event jo kaam shuru karta hai) | |
| Inputs (jo information chahiye ho sakti hai) | |
| Evidence (result ko kya support kare) | |
| Acceptance criteria (reviewer kaise decide kare ke complete hai) | |
| Main number (kya improve hona chahiye) | |
| Guardrails (kya worse nahi hona chahiye) | |
| Forbidden actions (Worker kabhi kya na kare) | |
| Final authority (named human jo decision ka accountable hai) | |
| Record (completion ke baad kya retain hona chahiye) | |

## Template 2: The Sort Record

Purane workflow ke har element ke liye ek row. Yeh record System of Record mein **permanently** rehta
hai — isi se tum design defend karte ho.

| Old element | Yeh kyun exist karta hai? | Bin | Faisla | Reason, source ke sath agar Bin 1 | Kisne sort kiya | Date |
| --- | --- | --- | --- | --- | --- | --- |
| | | 1 / 2 / 3 | keep / redesign / delete | | | |

Sort karte waqt teen reminders. Ek control ka purpose Bin 1 hai; uska mechanism zyada tar Bin 2 hai. Jab
shak ho, element Bin 1 mein rehta hai jab tak governing sources aur expert confirm na karein ke uska
purpose safely redesign/remove ho sakta hai. Aur Bin 3 deletions ko carefully record karo — yeh woh
productivity gain hai jo contract of success measure karega, isliye yeh tumhara sales evidence bhi hai.

## Template 3: The Invariants List

Bin 1, rules ki tarah likha hua. List chhoti rakho — rule jo sirf useful hai woh guidance hai; rule
jiski violation result ko invalid/unlawful/untrustworthy bana de woh invariant hai. Sort section ke
paanch sawal se inhe dhoondo.

| # | Invariant | Source (law, standard, ya trust requirement) | Enforced by (words / tool permission / approval gate / policy check) |
| --- | --- | --- | --- |
| | | | |

## Template 4: The Source Register

Har corpus source ke liye ek row. **Relevance kaafi nahi hai — source applicable bhi hona chahiye.**
Class column mein authority ki kind bhi record karo: law, standard, contract, internal policy, expert
methodology, guidance, ya example.

| Source name | Publisher | Authority class + scope | Jurisdiction | Version | Effective period | Rights basis | Owner | Stable ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | public domain / open license / commercial license / direct permission / replacement plan | | |

## Template 5: The Decision Map

Outcome ke liye jitne decisions chahiye, ek row har ek ke liye. Decisions departments se zyada der zinda
rehte hain.

| Decision | Evidence required | Governing source (register row) | Rule ya judgment? | Permission (kaun/kya decide kar sakta hai) | Escalation condition | Record retained |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Template 6: The Exception Entry

Har exception shape ke liye ek — normal path finish hone se pehle define ki jaati hai.

| Field | Tumhari Entry |
| --- | --- |
| Exception (kya galat hua hai) | |
| Detection (Worker ko kaise pata chalta hai) | |
| Worker kya kar sakta hai | |
| Worker kya kabhi na kare | |
| Escalates to (named role) | |
| Escalation mein kya hona chahiye (taake insaan ko ready-to-make decision mile) | |
| Wait karte hue, Worker kya kare | |
| Resolution record mein kaise enter hoti hai | |

## Template 7: The Coverage Register

Har professional outcome ke liye, har jurisdiction mein, ek row. Isi se tum "profession ka kitna hissa
cover karte ho?" ka jawab **fact** se dete ho, feeling se nahi. Ek outcome is register mein sirf tab
enter hota hai jab woh neeche wali definition of done pass kar chuka ho — **partial credit nahi hota**,
kyunke half-covered outcome unfinished hai, thin nahi.

| Outcome | Jurisdiction | State | Definition of done: date passed | Expert approval | Next re-check |
| --- | --- | --- | --- | --- | --- |
| | | probe / covered | | | |

State column par do notes. **Probe** sasti evidence hai jo tumne domain score karte waqt gather ki —
koi owner nahi, versions nahi, evaluation set nahi, aur yeh System of Record ka hissa nahi hai, isliye
kabhi coverage count nahi hota. **Covered** ka matlab hai outcome definition of done pass kar chuka.
Covered rows count karo aur jawab mil jata hai: ek thin hai, kai thick hai, aur naya jurisdiction add
karna rows ka naya set kholta hai jo phir ek se shuru hota hai.

## Definition Of Done

Pehla thin slice agle stage ke liye ready hai jab har box check ho. **Domain expert aakhri box khud
check karta hai.**

- [ ] Ek professional outcome precisely define hua hai (Template 1 complete).
- [ ] Purana workflow real cases se study hua — ek failure aur ek escalation samet.
- [ ] Purane workflow ke har element ka sort record hai (Template 2 complete).
- [ ] Invariants likhe, sourced, aur approved hain (Template 3 complete).
- [ ] Har corpus source ka register row hai, rights basis ke sath (Template 4 complete).
- [ ] Har corpus entry ki class hai: authority (citation/change/dispute test pass karti hai, citable
      hai) ya orientation (context ki tarah marked, short, agents kabhi cite nahi karte). Poore lessons
      curriculum ke paas rehte hain.
- [ ] Decisions mapped hain, rules/judgment/permissions alag hain (Template 5 complete).
- [ ] Har exception shape ka entry hai, normal path finish hone se pehle likha gaya (Template 6
      complete).
- [ ] Ek complete reflex outcome aur Bin 1 invariants ke around bana hai, expert ki voice mein authored,
      approved.
- [ ] High-risk rules tool permissions, approval gates, ya policy checks se enforce hoti hain, sirf
      words se nahi.
- [ ] Evaluation set routine, incomplete, conflicting, wrong-jurisdiction, escalation, aur
      forbidden-action cases cover karta hai.
- [ ] Har change ka impact record hai: kya badla, kyun, kisne approve kiya, konse maps/reflexes/
      evaluations affected hue.
- [ ] Insaan aur agents ek hi governed source se parhte hain.
- [ ] Customer-private knowledge shared vertical se bahar hai.
- [ ] Outcome coverage register mein enter hua (Template 7).
- [ ] Domain expert ne complete slice approve kiya hai.

**Yeh list do baar parho, kyunke yeh do lists hain.** Yeh ek outcome ka definition of done hai. Yeh
tumhara **"ready to sell" ka definition** bhi hai, kyunke aakhri unchecked box hi wajah hai ke tum abhi
buyer ki meeting mein nahi ho. Is par kuch bhi first customer ke baad tak deferred nahi ho sakta:
governance, exception cases, aur expert ki approval — yehi hai jo slice ko dikhane laayak banate hain.

---
[⬅ 05 — Failure Modes + Ayesha](05-failure-modes-and-ayesha.md) · [Agla: 07 — Appendix A: Sales SoR ➡](07-appendix-sales-sor.md) · [⬆ Index](README.md)
