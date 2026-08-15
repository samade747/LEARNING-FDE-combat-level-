# 00 — Overview: Aakhri Dependency

## Aapka System Mukammal Hai, Aur Trapped Hai

3 courses mein aap ne kya banaya, count karo: ek loop jo aapke baithne se pehle morning queue triage kar
deti hai. Ek harness jo khatarnak galtiyan namumkin banati hai. Ek eval suite jo reviewer ko ek defended
number deti hai. Roughly: **ek junior colleague, written job description, supervisor, aur performance
record ke sath.**

Ab count karo ye kis pe depend karta hai. Aapka laptop khula hona. Aapki session logged in hona. Aapki
machine 9am pe awake, power pe, network pe hona. **Koi ek miss karo, aur beat chup chaap nahi chalti** —
queue barhti hai, escalations jama hoti hain, aur Monday ka aap Friday ke band lid ki keemat chukata hai.

Trilogy ne aapko single points of failure hataana sikhaya, ek ek kar ke: maker-checker split ne single
unreviewed opinion hataya, harness ne single unguarded action hataya, evals ne single unchecked checker
hataya. **Ek baaki hai, aur wo aap ho** — aapka judgment nahi (jo human gate sahi tarah rakhta hai), balke
aapka **hardware**. **System us machine se zyada reliable hai jis pe wo chalta hai. Yehi signal hai ke
ye apne ghar se bahar nikal chuka hai.**

> **Simple:** Aap ne ek achha worker train kiya aur phir usay sirf apne living room mein kaam karne pe
> majboor kar diya, sirf tab jab aap ghar pe ho. **Worker theek hai. Arrangement problem hai.**

## Concept 2: Ek Sawal Jo Har Option Sort Karta Hai

Jaise hi aap naya ghar dhoondte ho, options aur vocabulary shor macha deti hain: cloud sessions, hosted
agents, managed runtimes, SDKs. **Ek sawal se sab kuch cut through karo, jiske 2 halves hain:**

> **Kaun agent loop operate karta hai, aur uska kaam kahan execute hota hai?**

- **Control plane** — loop khud: jo sessions start karta hai, model ko feed karta hai, events stream
  karta hai, 3am crash pe restart karta hai
- **Execution plane** — jahan actions land karte hain: sandbox jahan tools chalte hain, data jise wo
  touch karte hain

Aapke laptop pe dono planes **ek** machine hain, isliye kabhi alag karne ki zaroorat nahi padi. Aage wale
ghar inhe alag kar sakte hain — sab se interesting ghar **jaan-boojh kar** alag karta hai.

## 4 Ghar

- **Ghar 1: Aapki session** — sab kuch aapka: config, runtime, uptime. Yahin trilogy hui. Ye **banane
  aur prove karne** ka sahi ghar hai. Iske upar **depend karne** ka galat ghar hai.
- **Ghar 2: Cloud schedule** — Config aapki (wahi rules file, skills, subagents), lekin **clock** kisi
  aur ke computer pe move ho jati hai. Claude Code Routine, ya GitHub Actions scheduled job. **Sab se
  chhota move, sab se bara immediate payoff.**
- **Ghar 3: Managed runtime** — Aap agent ki **definition** (model, prompt, tools, guardrails) hand over
  karte ho, vendor ka service **control plane** operate karta hai. Execution plane ek choice hai:
  vendor ka cloud sandbox default, ya jahan custody demand kare, **aapka control kiya hua sandbox**.
  **Aap loop operate karna chhor dete ho. Aap uske ird gird ka business operate karte rehte ho.**
- **Ghar 4: Apna process** — Harness ek library ban jati hai us software mein jo aap likhte ho, servers
  jo aap chalate ho. Sab aapka, poori responsibility bhi aapki. **Ye Agent SDK hai, aur ye Mode 2 ka
  ilaka hai** — is course tak sirf darwaza dikhaya jata hai.

| Ghar | Control Plane | Execution Plane | Raat 3am kaun jagta hai |
| --- | --- | --- | --- |
| 1. Aapki session | Aap | Aapka laptop | Aap |
| 2. Cloud schedule | Aap, scheduler ke zariye | Cloud runner | Shared |
| 3. Managed, cloud sandbox | Vendor | Vendor | Infrastructure unka, outcomes aapke |
| 3. Managed, self-hosted sandbox | Vendor | Aap | Plane se split |
| 4. Apna process | Aap | Aap | Aap, jaan-boojh kar |

> **Sawal technical nahi hai.** Ye wahi sawal hai jo har business apne har function ke baare mein poochta
> hai: **ye khud karein, ya kisi ko paisa den?** Rule jo baar baar ata hai: **sirf wahi own karo jo
> zaroori hai, jo chahte ho wo nahi.**

### Self-Check
**Sawal:** Ayesha (Lahore) apni freelance-invoicing loop apne laptop se chalati hai. Load-shedding zyada
tar shamon ko power kaat deti hai, aur usay ek naya client mila hai jo 6pm daily invoices chahta hai,
bina fail. Konsa ghar pehle chahiye, aur ghar 3 aaj kyun zyada hai?
**Jawab:** **Ghar 2, cloud schedule.** Uska masla sirf **clock** hai — loop proven hai, config kaam
karta hai, lekin machine 6pm promise nahi kar sakti. Schedule ko cloud runner pe move karna power cut
ko hata deta hai. **Ehtiyat:** zyada tar schedulers, CI schedules samet, waqt ke **around** promise
karte hain, **exact** nahi. Isliye "without fail" scheduler feature nahi — ye ek **kit** hai (Part 2 ka
minimum unattended kit): missed-run detector, safe retry, 6:30 tak koi run na ho to alarm. Ghar 3 un
problems ka jawab hai jo Ayesha ke paas abhi nahi (doosre users serve karna, long-job persistence,
scale) — aur unki keemat charge karta hai. Aaj, user Ayesha hai. Ghar 2 + kit kaafi hai.

---
[⬅ Index](README.md) · [Agla: Headless Bridge ➡](01-headless-bridge.md)
