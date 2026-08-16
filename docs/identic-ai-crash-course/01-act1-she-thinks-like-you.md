# 01 — Act 1: Apni Identic AI Banao

## Claudia Ko Online Lao

Yeh poora Act 1 hai: Claudia ko aapke twin ki tarah online lao, kisi company se wired nahi. OpenClaw
ka raw kaam (install, chat app pair karna) aap [on-ramp](/docs/openclaw-with-general-agents) mein kar
chuke ho; yahan coding agent sirf woh **verify** karta hai, phir ek ready-made Claudia aapke workspace
mein place karta hai aur prove karta hai ke woh aapko janti hai.

Starter mein ek **complete Claudia** ship hoti hai: pre-authored workspace jisme uska persona, chief-of-
staff role, aur aap kaise decide karte ho iska seed pehle se baked hai. Coding agent usay scratch se
nahi likhta ya personality improvise nahi karta — jo workspace already hai usay backup karta hai
(kuch bhi lost nahi hota), Claudia swap karta hai, aur OpenClaw reload karta hai.

**Coding agent ko paste karo:**
```text
Bring my Identic AI online. First verify OpenClaw is already installed and that the chat app I
paired in the on-ramp can reach me... Then place the ready-made Claudia from the starter into my
OpenClaw workspace: back up any workspace I already have... Run her on a capable model. Do not wire
her to any company yet.

When she's ready, have her message me on my chat app answering "what do you know about how I
approve refunds?" from her seeded knowledge of me.
```

**Done jab:** Claudia aapke chat app par kuch aisa reply kare jo uske seed se aya ho (real numbers aur
patterns aapke refund handling ke), generic "I can help you manage approvals" nahi. Agar generic lage,
seed load nahi hui — recovery move paste karo.

> **Carry-forward:** Claudia ab aapko janti hai, aur kisi se wired nahi. Scenario 1 usay ek single
> decision par reason karte dekhta hai, koi company tasveer mein nahi. Act 2 mein company khadi hogi.

---

## Scenario 1 — Woh Pehle Se Aapki Tarah Sochti Hai (~12 min)

Aap ne Claudia isliye banayi kyunki workforce jo approvals throw karti hai woh badhta hi rehta hai:

| Workforce | Approvals/week Aap Tak | Kaisa Lagta Hai |
| --- | --- | --- |
| 4 Workers | ~dozen | phone par chand taps meetings ke darmiyan |
| 40 Workers | ~100 | 3-4 ghante roz threads parhna |
| 400 Workers | 1000+ | impossible; aap khud bottleneck ban gaye |

Hiring loop kabhi nahi tootta. Jo tootta hai woh **aap** ho. Isliye Claudia ko kisi real company se
chune se pehle, sabse pehla check yeh hai: **kya woh waqai aapki tarah decide karti hai?** Yeh test
kuch bhi wire kiye bina ho sakta hai — bas usay chat mein ek decision dikhao.

> **Poore course ka core idea:** Policy fixed criteria apply karti hai: "is amount ke neeche, approve."
> Aapka twin aapki **judgment** apply karta hai, jo waqt ke sath aapke asal decisions se seekhi hai.
> Isi liye woh routine ko aapki tarah handle kar sakti hai — woh case pakar sakti hai jo har rule fit
> karta hai lekin phir bhi aapki nazar deserve karta hai, jabke ek rigid rule nahi pakregi.

**Coding agent ko paste karo:**
```text
Have Claudia weigh one sample decision for me, just in chat, with nothing else wired up. Tell her:
a long-tenure customer with no prior refunds is asking for a refund well inside what I normally
wave through. Ask her, on my chat app, what she would do and why. She isn't connected to any
company, so she's only reasoning out loud, not acting on anything.
```

**Done jab:** Claudia message kare ek clear recommendation ke sath ("I would approve this; it matches
how you handle long-tenure customers with no prior refunds"), aur kahin kuch nahi hua kyunki woh
kisi se wired nahi. Woh soch rahi hai, kar nahi rahi. Acting Act 2 mein ati hai.

<details>
<summary>Claudia kis cheez se decide karti hai (3 layers)</summary>

1. **Standing instructions** — aapne plain language mein jo rules diye ("always surface envelope-
   extension hires to me"). Sabse reliable layer.
2. **Per-decision feedback** — jab woh galat kare aur aap correct karo, reasoning ke sath, taake
   similar-but-not-identical cases par apply kar sake.
3. **Derived patterns** — jo woh khud dekh kar infer karti hai ("aap long-tenure customers par fast
   approve karte ho"). Routine volume ke liye sabse useful, lekin sabse kam certain.

**Reasoning authority se pehle aati hai, jaan-boojh kar.** Abhi woh sirf un decisions par reason karti
hai jo aap dikhao, kuch wire kiye bina — taake aap uska judgment dekh sako trust karne se pehle. Act 2
mein bhi jab woh company se connect hoti hai, woh dry-run se shuru karti hai: real queue parhti hai
aur log karti hai woh kya karti, kuch post nahi karti, jab tak aap enough dekh kar trust na kar lo.
</details>

<details>
<summary>Sab auto-approve kyun nahi, ya human approvers kyun nahi?</summary>

- **Auto-approve zyada aggressively:** limits itni badhao ke queue khud clear ho jaye. Yeh governance
  ko convenience ke liye trade karta hai — bina kisi conscious decision ke naya authority mil jata hai.
- **Approval pool mein humans add karo:** human chief of staff hire karo. Yeh wohi management hierarchy
  wapis banata hai jo AI-native company ne flatten karni thi, aur har human ki apni attention ceiling
  hoti hai — 3 log 3x kaam cap karte hain, infinity nahi.

Delegate hi teesra option hai, aur sirf yehi scale karta hai: woh aapki judgment routine par apply
karti hai, taake workforce bina bottleneck rebuild kiye aur bina governance chorhe grow ho sake.
</details>

> **Act 1 khatam:** Ab aapke paas aapki Identic AI hai — ek twin jo aapki tarah reason karti hai aur
> kisi se wired nahi. Act 2 usay job deta hai.

---
[⬅ Setup](00-two-agents-and-setup.md) · [⬆ Index](README.md) · [Agla: Signed Bounded Mandate ➡](02-signed-bounded-mandate.md)
