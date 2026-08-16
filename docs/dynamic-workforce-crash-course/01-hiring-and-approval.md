# 01 — Scenarios 2-3: Hire Likhna Aur Approval

## Scenario 2 — Hire Ko Likh Do (~10 min)

Koi bhi join karne se pehle, agent hire ko concrete cheez ki tarah likhta hai — job rec jaisi. **3
decisions:**

- **Role** — naam, title, kisay report kare
- **Capabilities** — plain description yeh Worker kis liye hai
- **Engine** — kaunsi runtime power deti hai
- **Budget** — chota monthly cap, probation ke liye
- **Receipt** — source issue jo hire justify karta hai

> **Zaroori note:** Capabilities text **description hai, fence nahi.** Worker ko batati hai kis liye
> hai — usay kuch karne se **nahi** rokti.

## Aap Resume Par Nahi, Work Sample Par Hire Karte Ho

Description ek claim hai. Standing Worker ko claim par commit nahi karte — pehle sasti tarike se prove
karte ho. **Probation** — chota trial, chota budget, minimal authority. Kuch plain cheezon par score
karo: sahi jawab, **apni lane mein raha**, sahi tone, cost kya hui.

> **Kabhi compromise mat karo: apni lane mein rehna.** Support Worker jo chupke se refund issue kare,
> billing badle, account edit kare — yeh galat jawab dene se bhi zyada bura fail hua hai. **Ghalat
> jawab quality problem hai; lane se bahar act karna governance problem hai.**

**Draft karo:**
```text
Draft the Reader Support Specialist hire... a plain capabilities
description, a deliberately small probation budget, and the source
issue it traces back to. Then write the probation plan: three or four
real issues it must handle, with "stays in its lane" as the one I will
not compromise.
```

**Done jab:** Aap poori hire packet pakre huye ho, drafted role + probation plan, keyless local engine
par, aur ek sentence mein bata sako probation ko kya prove karna hai.

## Scenario 3 — Approve Karo, Minimal Power Ke Sath (~12 min)

## Hiring Wahi Gate Reuse Karti Hai

Naya approval step seekhne ki zaroorat nahi. Hire file karna usay wahi board-approval inbox mein daal
deta hai jo CEO aur strategy ke liye use ki thi.

## Alfaz Fence Nahi Hain. Grants Hain.

**Yahi is scenario ka poora point hai.** Lagta hai capabilities text control karti hai Worker kya kar
sakta hai — carefully worded description usay lane mein rakhegi. **Nahi rakhti.** Asli fence Paperclip
ki **server-enforced** layer hai: explicit **permissions** jo Worker ko milti hain, har ek **scoped**
(kya chhu sakta hai), plus per-issue rule jo review se guzar sakti hai.

**2 layers, building ki tarah:**
- **Coarse gate** — company switch jo decide karti hai naya hire approval maange ya nahi (master door
  policy)
- **Fine grant** — permissions/scopes jo yeh Worker hold karta hai (individual keycards)

**Capabilities text batati hai Worker kis liye hai. Grants batate hain woh kya kar sakta hai.**

> **Class of hires bina click ke through karwana aapki discipline hai, feature nahi.** Paperclip ka
> koi built-in rule nahi hai jo class of hires auto-approve kare. Woh khud banana parta hai — agent
> written policy ke against har proposed hire check kare, sirf fitting wale file kare, sab log kare.
> **Rule:** pre-approval discipline sirf usay pre-filter kar sakti hai jo aap khud approve karte —
> kabhi zyada authority nahi de sakti.

**Draft karo:**
```text
File the Reader Support Specialist hire... Then show me two things
side by side: the one company switch that decides whether hires need
my approval, and the exact permissions this new Worker would hold once
I approve it onto probation.
```

**Done jab:** Hire aapke approval inbox mein evidence ke sath pada ho, aur aap gate (switch) aur grant
(permissions) dono point kar sako, aur samjha sako capabilities description kyun Worker ko lane mein
nahi rakhti.

---
[⬅ Gap Spot Karna](00-spotting-gaps.md) · [⬆ Index](README.md) · [Agla: Probation Aur Lifecycle ➡](02-probation-and-lifecycle.md)
