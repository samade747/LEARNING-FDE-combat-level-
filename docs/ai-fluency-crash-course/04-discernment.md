# 04 — Part 2: Discernment (Concept 5)

AI aksar confident sunta hai. Galat answer warning label ke sath nahi aata — polished, detailed,
certain lag sakta.

**Discernment** = judge karna ke AI ne tumhe kya diya quality mein kaisa hai. Description poochta
hai "kya maine job clearly explain ki?" Discernment poochta hai "kya AI ne actually job achhi ki?"

**Automation bias** = insaan ka automated answer ko bohot asaani se trust karna, khaas kar jab
confident/professional lage.

## Made-Up Answer Ke 4 Signs

- **Specifics jo bohot exact hain** — ek precise figure/date/name/citation jo kahin se nahi aaya.
  "99.97% on-time delivery" "reliable" se zyada suspicious hai.
- **Confidence jahan expert hesitate karta** — specialist jo "it depends" bolta, wahan flat "yes"
  aaye.
- **Long output mein contradiction** — Page 2 flat fee bolta, Page 6 per-user se yearly cost
  calculate karta.
- **Claimed action jo hui hi nahi** — "I sent the email," "I checked," "I ran the tests" — jab tak
  tool proof na dikhaye, ise sentence samjho, event nahi.

**Jab accuracy matter kare, verify karo.**

Discernment ke 3 parts, Description jaise hi teen chezon par:

1. **Product discernment** — result achha hai?
2. **Process discernment** — kaam karne ka yeh tareeqa pay off kar raha hai?
3. **Performance discernment** — AI apne aap act karte hue log achhe se serve ho rahe hain?

## 5.1 Product Discernment

Pucho: Factually correct? Har important requirement follow hui? Kuch missing? Internally
consistent? Expert credible samjhega? Apna naam lagaoge?

Yeh 6 sawal 3 references ke against check karte hain: tumne kya maanga, source material, field ke
standards. Answer 2 pass kar sakta, jo matter karta usme fail ho sakta.

**Yahan tumhari domain knowledge pay off karti hai** — accountant bad assumption, programmer bug,
teacher confusing explanation pakar leta. AI expert work tez karta hai, expertise ki zaroorat
khatam nahi karta.

Case bhi judge karo, result nahi sirf: agar AI Vendor A recommend karta hai kyunke ek feature
assume kiya jo exist nahi karta, recommendation trust mat karo jab tak support solid na ho.

Ask AI to show: assumptions, evidence, decision criteria, calculations, alternatives — par yeh
**review ke liye offered justification hai, model ki hidden reasoning ka record nahi.**

```text
Answer only from the three proposals I attached, not from anything you
know about these vendors. If a proposal does not state its exit terms,
say so instead of guessing. For every term you report, quote the
proposal's section heading and the sentence it came from.
```

## 5.2 Process Discernment

Kabhi answer fine hota hai, working relationship nahi. Session ko judge karo, last message ko
nahi: AI feedback se adapt kar raha ya drift kar raha? Mistake dohra raha jo 2 baar correct ki?
Agreeable ho gaya uselessness tak? Draft ko khud likhne se zyada edit kar rahe ho?

**Last sawal straight answer do:** 20 minute steering jo ghanta bachaye, win hai. 20 minute jo 15
bachaye — loss hai jo productive feel hone ki wajah se win samjha gaya.

Jab process kaam nahi kar raha, 3 moves escalate hoti hain: **performance description change karo
→ tool change karo → task wapas le lo.** Teeno fluency hain, sirf teesri defeat feel hoti hai.

## 5.3 Performance Discernment

Tabhi exist karta hai jab agency use ki ho. Pucho: AI ka independent behavior logon ke liye achhe
outcomes de raha? Alag sawal hai factual correctness se.

AI tutor har sawal accurately answer kar sakta aur phir bhi bad tutor ho, agar student hesitate
hote hi solution de deta aur koi nahi seekhta. Yeh **chat window ke andar se nahi dikhta** — kai
cases mein dikhta hai: users next kya karte hain, kya complain karte hain, kaunse cases hamesha
galat jaate hain. Koi hazaron conversations manually nahi parh sakta — isliye yeh infrastructure
ban jata hai jo inhe watch kare.

## Description + Discernment Loop

1. Describe karte ho kya chahiye
2. AI produce karta hai
3. Inspect karte ho
4. Kya change hona chahiye explain karte ho
5. AI try again karta hai

**Pehla response usually draft hota hai, finish line nahi.**

Feedback pattern: **Problem → Why it matters → Direction**

_Weak:_ "Wrong. Try again."

_Better:_ "The second section assumes enterprise customers. Our audience is solo founders, so the
advice is too expensive. Rewrite that section for a one-person business with a limited budget."

2 habits speed badhate hain: (1) named passes mein edit karo (clarity pass, tone pass, formatting
pass — har ek alag sawal), (2) jab stakes justify karein, 2-3 drafts maango, strongest se edit
karo.

Har review 3 tarah khatam hota hai: **work jaata hai / feedback ke sath wapas jata hai / tum task
wapas le lete ho.** Decide karo konsa ending hoga, next message type karne se pehle — "ek aur chhoti
change" loop se bachne ke liye.

> **Where this leads:** Discernment evaluation engineering ban jata hai — **eval suites**
> (repeatable tests jo AI output score karte hain), monitoring, sampling, release gates. Jo
> judgment khud nahi seekhi, wo automate nahi ho sakti. Aage: Trusting the Checker, Eval-Driven
> Development.
