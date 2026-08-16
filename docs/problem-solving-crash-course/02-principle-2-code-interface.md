# 02 — Principle 2: Code as Universal Interface

> **Failure mode:** "Meri prose request baar baar galat kyun samjhi jati hai, aur AI apps ki hadd par
> kyun ruk jata hai?"

**Sarah ki example:** 3000 photos, teen jagah scattered (phone, camera, backup drive), filenames aisi
`IMG_4521.jpg`. Usne teen photo apps try kiye — har ek kuch karta tha, koi bhi combination nahi karta
tha. Usne ek paragraph likha ek general agent ko: location se organize karo, date se rename karo,
content se duplicates dhoondo. **15 minute mein khatam.** Agent ne ek chota program likha jo location
padhta, rename karta, image bytes hash kar ke duplicates dhoondta. Sarah ne koi code nahi likha.

## Do Hisse

1. **Jab kaam ek command ke liye zyada complex ho, AI code likh kar karta hai.**
2. **Format utna hi matter karta hai jitna content.** Plain paragraph vague hota hai. Table, checklist,
   ya structured template clear hoti hai. Jitna specific format do, AI utna kam guess karega.

## Bash vs Code (Farq)

| Surface | Role | Kya Karta Hai |
| --- | --- | --- |
| **Bash (P1)** | Haath | Navigate, search, move, observe — ek waqt ek command |
| **Code (P2)** | Dimagh | Compute, transform, orchestrate, persist, integrate |

Bash folder kholta hai; code har file parhta hai, bytes hash karta hai, compare karta hai, report likhta
hai. Jab kaam "yahan dekho, woh move karo" se "compute karo, decide karo, cheez banao" mein cross ho
jata hai — woh Principle 2 hai.

## Code Ke 5 Powers

1. **Precise thinking** — exact cent tak calculation, "kitna spend kiya" jaisa rough answer nahi.
2. **Workflow orchestration** — many-step rules (if/then) ek sath likhta hai, aap se har step pe nahi poochta.
3. **Organized memory** — folders/files banata hai taake baad mein wapis padh sake, zero se start na kare.
4. **Universal compatibility** — spreadsheet + emails + PDFs jaise mukhtalif formats ko ek sath combine karta hai.
5. **Instant tool creation** — jab koi app exact combination nahi karti, AI apna chota tool bana deta hai.

## Aapke Do Kaam (Yeh Nahi Badalte)

1. **Batao kya chahiye (define the problem).** Code walon ke liye: kya karna hai, output ka format kya
   ho, kya nahi chhuna. Documents walon ke liye: format batao, alfaz nahi — "one-page memo, 4 sections:
   summary, findings, risks (max 3), next steps."
2. **Result check karo (verify the output).** Code parhna aana chahiye (likhna nahi) taake galti pakri
   jaye. Documents ke liye: claims ko source se match karo. AI confident text likhta hai — yeh trap hai.
   Jo *sach* hai woh parho, jo *acha lagta hai* woh nahi.

## Hands-On Practice

Course "Pack 2 — Receipts" (15 receipts: photos, PDFs, screenshots — koi single app teenon parh nahi
sakti) deta hai. Prompt: AI se plan poochho (code mat likhwao pehle) ke woh kaise approach karega —
har step "5 Powers" mein se kaunsa use karta hai. Phir optional follow-up: step 1 actual execute
karwao — 15 receipts se `extracted.csv` banwao, ek shot mein.

## Apne Kaam Par Apply Karo

1. Woh kaam chuno jo aap 2+ apps se karte ho — yehi signal hai ke koi single tool poora nahi karta.
2. AI ko describe karo, **pehle walkthrough mango**, code seedha mat mangwao.
3. Sabse time-consuming step AI se karwao. Agar 20 minute bache, AI ne ek nayi tool bana di jo subah
   thi hi nahi.

**Do mistakes se bacho:**
- "Script likh do" mat kaho — pehle "apna approach batao" kaho.
- Agar kaam spreadsheet mein ho sakta hai, shayad AI chahiye hi nahi.

---
[⬅ Principle 1](01-principle-1-bash.md) · [⬆ Index](README.md) · [Agla: Principle 3 ➡](03-principle-3-verification.md)
