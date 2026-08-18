# 05 — Human Control: Insaan Loop Mein Kahan Khara Hai

> Ye course ka **sab se important part** hai. Loop kaam ka tareeqa badalta hai — aapko kaam se **bahar
> nahi karta**.

## 3 Feedback Cycles — Aapki Loop Sirf Ek Hai

Ek example: aap agent se bacchay ke liye ek typing game banwate ho.

| Loop | Waqt | Kaun chalata hai | Kya karta hai |
| --- | --- | --- | --- |
| **Coding loop** | Minutes | Agent akela | Likhta hai, test karta hai, fix karta hai, jab tak spec match na ho |
| **Feedback loop** | Hours | Aap | Try karte ho, decide karte ho kya change karna hai, spec update karte ho |
| **Outside loop** | Days | Duniya | Real log use karte hain, unka react karna batata hai aage kya karna hai |

Ye loops ek dusre ke **andar** baithe hain — bahar nahi. Kai coding loops ek feedback loop ke andar
chalte hain; kai feedback loops ek outside-loop round ke andar.

**Andrew Ng ka sawal:** Agent teeno loops khud kyun nahi chala sakta? Kyunke **aap** wo cheezein jaante
ho jo agent nahi jaanta — kaun use karega, unhe asal mein kya chahiye, "achha" kaisa lagta hai. Isay Ng
**context advantage** kehte hain.

**Poore course ka nichod:** Machine fast loop chalati hai. Aap wo do cheezein hold karte ho jo agent
kabhi hold nahi kar sakta: **kya banana hai**, aur **kis ki zimmedari hai**.

---

## Concept 13: Token Cost — Asal Limit

Loop baar baar chalta hai, kai dafa subagents bhi start karta hai — cost andaze se zyada tezi se barhti
hai.

**Fixes:**
- **Har loop cap karo** — max tries, minutes, ya spend.
- **Model ko kaam se match karo** — strong model plan/check ke liye, sasta model kaam ke liye. Sab se
  bara saving.
- **Loop prompt aur rules file chhoti rakho** — har beat pe cost hoti hai.
- **Kam frequency pe chalao** — har ghante, har 5 minute nahi (~12 guna sasta).

**Numbers ka andaza:** Ek beat (maker + checker) ~40,000 input + ~6,000 output tokens = ~**$0.20/beat**.
5 beats/din × 20 din = ~**$20/mahina**.

Wahi loop **har 5 minute** chale (din-raat) = 100+ guna zyada beats = **$1,000+/mahina** ho sakta hai —
same kaam ke liye, sirf **frequency** ki wajah se.

| Cadence | Beats/mahina | Cost/mahina |
| --- | --- | --- |
| 5 beats/din (weekday) | ~100 | ~$20 |
| Har ghante, din-raat | ~720 | ~$150 |
| Har 5 minute, din-raat | ~8,600 | ~$1,800 |

> **Zaroori tip:** Achi spine (memory) sirf correctness ke liye nahi — **cost bhi kam karti hai**. Jab
> agent ko pehli try ka lesson yaad hota hai, kam retries lagti hain.

---

## Concept 14: Kaam Check Karna Ab Bhi Aapka Kaam Hai

Maker-checker split se loop ka "done" **kuch matlab rakhta** hai — lekin "done" phir bhi ek **claim**
hai, **proof nahi**. Aapka kaam khatam nahi hua, sirf **move** hua hai. Aap har step type nahi karte,
lekin aap hi confirm karte ho ke loop ne asal mein kaam karne wala code ship kiya.

**Jab kai loops ek saath chalein — 3 nayi problems:**

1. **Failure ka math:** 5 steps, har ek 95% reliable = sirf 3 mein se ~3 runs cleanly khatam hoti hain.
   Aur galtiyan **spine ke andar** jama hoti hain — aaj ki galat line kal ka galat starting point hai.
2. **Loop jo kar sakta hai wo limit karo, sirf review nahi** — Reviewer sirf diff dekhta hai, lekin ye
   prove nahi karta ke loop ne aur kuch nahi kiya (config value badalna, flag flip karna). Fix: **narrow
   loop** — har part ko "standing permission" samjho, sirf utna hi do jitna zaroori hai.
3. **Counting question:** Jab 5 log aapki loop copy karein, sawal uthega — kitni loops chal rahi hain,
   har ek kya touch kar sakti hai, kis ki identity se act karti hai, kisne approve ki. Ye ab **loop
   engineering nahi, workforce management** hai.

**Jab kai loops ek memory share karein — 4 guardrails** (production practice se):
- **Versioning** — har change record ho, rollback ho sake
- **Conflict checks** — write se pehle check ke file change to nahi hui
- **Permissions by level** — organization-wide rules read-only hon, review ke bagair change na ho
- **Portability** — memory plain, open format mein rakho

---

## In / On / Out of the Loop — Industry Ki Zaban

| Term | Matlab | Kahan banaya |
| --- | --- | --- |
| **Human in the loop** | Har action se pehle insaan approve kare | Prompting turn-by-turn, plan mode, human gate pe merge |
| **Human on the loop** | System khud chale, insaan dekhta rahe aur rok sake | Routine `claude/` branches pe push karti hai, aap subah review karte ho |
| **Human out of the loop** | Koi na dekhe, koi intervene na kar sake | **Kabhi bhi acceptable nahi — ye failure mode hai** |

- **Prompting** = in the loop (aap heartbeat, checker, memory sab ho)
- **Loop engineering** = **on** the loop (system chalta hai, aapka attention gate pe)
- Achi loop **mix** hoti hai: safe fixes ke liye "on", risky/FAIL ke liye wapas "in" (jaise `claude/`
  branch rule)

> **"Out of the loop" jaan-boojh kar nahi banta — drift se banta hai.** Diffs parhna band karo, green
> checkmarks pe trust karo, weekly review skip karo — aur "on the loop" chup chaap "out of the loop" ban
> jata hai, koi design change ke bagair.

---

## Concept 15: Apne Project Ko Samajhna Band Mat Karo

Loop jitna smooth chalega, utna gap barhta hai us cheez ke darmiyan jo project mein hai aur jo aap
**samajhte** ho. Ye gap khamoshi se barhta hai.

**Do log ek jaisi loop bana sakte hain, opposite result ke saath:**
- Ek isay us kaam pe tez chalne ke liye use karta hai jo wo deeply samajhta hai
- Doosra isay us kaam ko **samajhne se bachne** ke liye use karta hai

Loop farak nahi bata sakta. **Aap bata sakte ho.**

Ye force ka naam hai: **AI gravity** (Eric So, MIT Sloan) — AI ko zyada se zyada sochne dene ki musalsal
"pull". Loop is pull ko mazboot banata hai kyunke wo aap ke sote waqt bhi chalta hai.

## Loop Fail Ho To (Observability)

- **Output wahan bhejo jahan aap dekh sakte ho** — log file, Slack/Discord, na ke wo terminal jo aap
  band kar chuke ho
- **Har run pe ek line likho, fail hone pe bhi** — timestamp ke saath, chup chaap fail hona sab se bura hai
- **Runs replayable rakho** (`opencode run --format json`, Routine web UI history)
- **Limit pe loudly fail ho** — clear "needs a human" note chhore, sirf ruk na jaye
- **Overnight se pehle prove karo** — hourly + watched, phir nightly + unattended. Report-only se shuru
  karo, phir gated fixes, phir unattended action

---
[⬅ Complete Loop Example](04-complete-loop-example.md) · [Agla: Dogfooding ➡](06-dogfooding.md)
