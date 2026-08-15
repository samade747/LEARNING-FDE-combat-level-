# 02 — Working Unwatched: Delegation Loop + Scheduled Tasks

## Concept 8: Delegation Loop — Brief, Plan, Approve, Review

Foundations mein sab kuch conversation thi. **Delegation alag hai:** aap ek outcome describe karte ho,
agent multi-step kaam karta hai, aap result dekhte ho. Result ki quality **4 lamhon** se decide hoti hai
— sirf ek prompt nahi.

**Step 1: Brief.** Assignment aise describe karo jaise ek smart, motivated naye colleague ko brief karte
ho jo aapka context nahi jaanta: outcome, constraints, audience, aur wajah.

- *Query:* "Ye PDF summarize karo."
- *Assignment:* "Ye 3 files parho. Har deadline aur open commitment flag karo. Manager ke liye ek
  page ka brief banao: direct tone, deadlines pehle, koi intro paragraph nahi."

**Step 2: Plan.** Har non-trivial brief ke aakhir mein:
```text
Lay out your plan first, and pause for my approval before doing anything.
```
> **Zaroori:** Desktop agent pe aap run dekh sakte ho aur beech mein rok sakte ho. **Yahan aap chale
> jaoge.** Isliye **plan usually aapka akela intercept hai intent aur finished work ke darmiyan.**

**Step 3: Approve ya redirect.** Plan parhne se pehle 4 cheezein check karo (2 minute):
- **Scope** — sirf jo naam liya wahi touch ho raha hai?
- **Order** — koi action verify hone se pehle to nahi ho raha?
- **Reach** — koi connector/send jo aap ne nahi manga?
- **Assumptions** — format/audience/rules ke baare mein kya assume kiya ja raha hai jo aap ne nahi bataya?

Agar kuch galat hai, dobara shuru mat karo — **ek sentence se redirect karo**: *"Step 2 mein, existing
template ke headings use karo, naye invent mat karo."*

**Step 4: Review.** Har brief ke aakhir mein ye 3 lines:
```text
Before you start: ask me 1-2 clarifying questions.
If any sources contradict each other on a material point, flag the
contradiction in the deliverable. Do not silently pick one.
When done: list every file you created and where each one landed.
```

> **Simple:** 4 steps, hamesha. Poori tarah batao kya chahiye. Kaam shuru hone se pehle plan dekhne ki
> maango. Plan parho, galat ho to ek sentence se theek karo. Phir result ko apni request ke against
> parho. **Plan sab se zaroori step hai — theek karna 1 minute, finished galat kaam theek karna poori
> shaam.**

**Anti-pattern:** Sab se common failure — is surface ko superpowers wale chat box ki tarah treat karna:
ek line ka prompt unattended multi-step kaam ke liye fire karna. **Vague brief mein jitni cheezein khali
hain, agent utni khud decide karta hai — akele.**

### Self-Check
**Sawal:** Aap ek multi-source task brief karte ho, plan-first line skip karte ho, meeting mein chale
jate ho. Wapas ate ho ek galat-source-reading pe bani deliverable milti hai. Desktop agent pe shayad
beech mein pakar lete. Ye safety net yahan kyun nahi thi, aur ek line se kya replace hoti hai?
**Jawab:** Safety net aapki screen pe aankhein thin — yahan aankhein kabhi screen pe nahi hone wali
thin, kyunke unwatched kaam karna hi is surface ka point hai. Sirf ek intercept bacha: run se **pehle**
— *"Lay out your plan first, and pause for my approval."* Yahan ye good practice nahi, **safety net**
hai.

## Concept 9: Scheduled Tasks — Bina Kisi Device Online Ke

**Scheduled task** ek assignment hai jo aap ek dafa describe karte ho, cadence ke sath, jo phir vendor
ke servers pe apne clock pe chalti hai — laptop band, phone jeb mein.

**Har scheduled task 4 jawab hai, order mein likhe:**

1. **Kya karna hai?** Standing brief. **Ek zaroori addition:** koi wahan clarify karne nahi hoga, isliye
   brief aapki gairhaziri survive kare, khaali case samet. *"Agar is hafte kuch naya nahi hai, ek line
   note produce karo"* — yehi chup hafte aur chup failure ka farq hai
2. **Kya touch kar sakta hai?** Files/platform storage, naam se
3. **Kya reach kar sakta hai?** Connectors, listed. Connectors permissions hain, suggestions nahi — koi
   mail connector nahi to koi mail nahi bhej sakta, chahe brief kuch bhi kahe
4. **Kab shuru hota hai?** Cadence. **Honest fact:** *"Monday 8am"* ka matlab hai **around** Monday 8am
   — schedulers stagger karte hain, kabhi slip bhi

**3 rules pehli schedule se pehle:**
- **Kabhi wo mat schedule karo jise aap already trust nahi karte chhor kar jane ke liye** — task ko haath
  se, watched, kai baar chalao pehle
- **Metered math likh kar karo** — har din/plan ke runs/ghante ki budget hoti hai. Apni scheduled tasks
  ko limit ke against count karo **collision se pehle**
- **Complete hui run, successful task nahi hai** — scheduler ka kaam "chali" tak khatam hota hai. Kya
  kaam **sahi** tha, ye scheduler ka business nahi. **Success signal task ke apne output mein banao**

**Boundary, honestly:** Is concept se aap **reporting** schedule bana sakte ho — sources parhna,
synthesize karna, brief banana, sahi tier mein rakhna. Jo aap abhi safely nahi bana sakte: **acting**
schedule — jo bhejta, file karta, update karta, decide karta hai cadence pe. Isay checker, machine-
verifiable stopping condition, state file chahiye — **Loop Engineering course sikhati hai.**

### Self-Check
**Sawal:** Ayesha 2 cheezein schedule karna chahti hai: Monday summary unpaid invoices ka (Drive se
parhna), aur Friday automatic reminder emails late clients ko. Konsi yahan fit hoti hai, konsi wait
kare, aur 1-word farq kya hai?
**Jawab:** Monday summary yahan fit hoti hai — reporting schedule hai. Friday reminders wait karein —
ye baahar duniya pe **act** karti hai unattended, cadence pe, galat run real clients ko email karti hai.
**1-word farq: acting** (vs reporting).

---
[⬅ The Surface](01-the-surface.md) · [Agla: Choosing + Open Path ➡](03-choosing-open-path.md)
