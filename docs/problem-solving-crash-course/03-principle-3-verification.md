# 03 — Principle 3: Verification as a Core Step

> **Failure mode:** "Output theek dikhta hai lekin production mein toot kyun jata hai?"

Finished-lagta output verified output nahi hota. Models aisa output dete hain jo **plausible** hai —
yeh **correct** hone jaisi baat nahi. Woh confidently list mein cheezein galat count kar denge, aisa
paragraph cite kar denge jo exist hi nahi karta, aisa code likh denge jo compile ho jaye lekin teesre
edge case par chupke se fail ho jaye. **Verification workflow ka ek step hona chahiye, afterthought
nahi.**

## Key Rule

**Jo agent ne output banaya, wahi uska sabse ghatiya verifier hai.** Usme wahi blind spots hain jinhone
original galti ki. Verification ko **independent path** chahiye — aapki apni nazar, ek alag model, ek
test, ek type-checker, ya database constraint.

## Examples

- **Legal:** "Case X ke mutabiq, company liable hai" — lekin Case X aisa kehta hi nahi. Verification se
  ("har reference ke liye exact sentence dhoondo jo support kare") galat references pakdi jati hain.
- **Insurance:** Summary kehti hai "policy 250,000 tak cover karti hai" — lekin asli limit water damage
  ke liye 100,000 hai. Verification asli limit doond leti hai.
- **Research:** "Koi serious side effects nahi" — lekin data mein 2 hain. Verification ("har claim ko
  exact rows se match karo") error pakar leti hai.

**Prompt pattern (high-stakes deliverable ke liye):**

```text
Before saving the final version, verification pass:
  - List every factual claim in the draft
  - For each one, identify the source location and quote the supporting text
  - Flag any claim you cannot ground
Refuse to save until every flag is resolved.
```

## "Wrong Number" Problem

Manager ne Q-sales region-wise poocha. AI ne kaha "West: 4.2 million." Finance team ne same data se
3.8 million nikala. AI se poocha kyun, AI ne **teesra** number diya: 4.5 million. **"Is this correct?"
poochna real verification nahi hai** — AI usi ghalti ke saath khud ko "haan sahi hai" bolega. Jisne
galti ki, usi se check mat karwao apna kaam.

**Fix:** Code/formula khud parho (likhna nahi, parhna kaafi hai). "Kya sahi data dekh raha hai? Kuch
filter to nahi kar raha jo include hona chahiye?" Phir khud chalao aur trusted source se compare karo.

**Delete/change karne wale kaam ke liye:** Hamesha pehle test run karo — kitne items affect honge check
karo, tabhi aage badho jab number expected ke match kare.

## Hands-On Practice

Course "Pack 5 — Verification" deta hai: ek polished-lagta memo jismein 5 hidden mistakes hain, plus
asli data spreadsheets. Prompt: har claim ko source se match karo, `VERIFICATION.md` banao teen
categories mein: Confirmed / Mismatch / No source found. AI pehli koshish mein kam az kam 3/5 galtiyan
pakar leta hai.

**Sabak:** Verification se pehle sab 5 claims equally correct **lagte** the. AI confidently likhta hai
chahe sahi ho ya ghalat. Verification step yehi cheez pakarta hai.

## Apne Kaam Par Apply Karo

Is hafte ka sabse important AI output chuno (numbers wala document, references wala report). Prompt:

```text
Verify every factual claim in <your-file>. For each claim, quote the
exact row or sentence from <your-sources> that supports it. Flag any
claim you cannot find proof for. Save to <your-file>-verification.md.
```

**Zaroori:** AI sources ko **alag** se parhe, sirf apna hi output dobara na parhe. Agar AI "sab consistent
hai" bina quote diye kahe, yeh real verification nahi — sharp karo.

---
[⬅ Principle 2](02-principle-2-code-interface.md) · [⬆ Index](README.md) · [Agla: Principle 4 ➡](04-principle-4-decomposition.md)
