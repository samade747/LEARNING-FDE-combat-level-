# 01 — Principle 1: Bash is the Key

> **Failure mode:** "AI sirf cheezon ke baare mein baat kyun karta hai, karta kyun nahi?"

**"Bash" ka matlab:** Terminal woh black-screen text interface hai jo har laptop ke sath ata hai. Bash
uske andar use hone wali language hai. Jab AI Bash chalata hai, woh wahi commands type kar raha hota hai
jo aap khud type karte agar Terminal app kholte (ya Windows par PowerShell). AI ke paas aapki machine ka
poora keyboard access hai — clicks ki jagah commands se. Cowork/OpenWork users ke liye: same principle,
alag surface (typed commands ki jagah step cards). Dono soorat mein: **AI aapke computer par act karta
hai, aap dekhte ho.**

## Beginner Mistake

Zyada tar log sawal poochte hain: "Meri pichle hafte ki notes kaise organize karoon?" AI lamba jawab
deta hai lekin kuch organize nahi karta. Aap ne advice mangi jab action mangni chahiye thi.

**Fix:** Specific instruction do.

| Advice mangna (weak) | Instruction dena (strong) |
| --- | --- |
| "Meri notes kaise organize karoon?" | "notes/ folder ki har file parho. Har file se action items aur zimmedar banda nikalo. Result weekly-summary.md mein save karo, banday ke hisab se sorted." |

Pehla prompt suggestions ka paragraph deta hai. Doosra prompt ek **finished file** deta hai. Yehi farq
hai chatbot use karne aur tool use karne mein.

## Mental Model

**Agent ke haath hain. Haathon ko brief karo, dimagh ko nahi.**

## Rule

Jab bhi khud ko sawal type karte pakdo, ruko aur poocho: "Kya isko instruction mein badal sakta hoon jo
ek file result de?" Taqreeban hamesha, haan.

## Examples (Alag Fields Se)

- **Legal:** "47 documents mein 'indemnification' search karo" — asking se essay milta hai; instruction
  se minutes mein har match ki list milti hai (`indemnification-hits.md` mein save).
- **Downloads folder:** "Kaise organize karoon" se generic tips milti hain; "abhi kya hai isme?" se AI
  khud dekhta hai, count karta hai, group karta hai — 30 second mein, bina aapke ek command type kiye.
- **Accounting reconciliation:** Tutorial ki jagah, AI khud match kar ke mismatches ki list deta hai
  20 minute mein.
- **Marketing:** "Q3 campaigns kaise chal rahe" se generic answer milta hai; instruction se real data se
  table milti hai 3 minute mein.

## Hands-On Practice (Course Ka Exercise)

Course "Pack 1 — Cluttered folder" download karwata hai (53 files ka messy downloads folder). Prompt
sirf 5 lafzon ka: *"What's in ./downloads/?"* Agent khud commands ka cascade chalata hai (`ls`, `find`,
`cat`) aur bina files move kiye ek accurate summary deta hai — duplicates, sizes, groups sab identify
kar leta hai. **Sabak:** Aap ne koi command type nahi ki. AI ne khud decide kiya kaunse commands chalane
hain.

## Apne Kaam Par Apply Karo

**Method nahi, brief likho.** Ek sentence: input naam do (kaunsa folder/thread/drive), output naam do
(summary file, list, report). Commands ya clicks specify karne ka lalach roko.

```text
The folder at <path> has been collecting <thing> for <how long>.
Inspect it and write me a <named output file> that <decision the
output should support>. Read-only, don't change anything.
```

**Sabse bara failure:** Agar prompt mein "find use karo" ya "spreadsheet kholo aur..." add karne lagein,
to aap wapas *method* specify kar rahe hain, *outcome* nahi. **How** batane wale verbs kaato, sirf
**what you want at the end** wale verbs rakho.

> **Kyun matter karta hai:** Yeh crash course ki sabse high-leverage habit hai, aur skilled log bhi isay
> install karne mein fail hote hain — kyunki method dictate karna wait karne se tez lagta hai. Nahi hai.
> Har minute jo method specify karne mein lagta hai, woh minute agent chala sakta tha.

---
[⬅ Overview](00-overview.md) · [⬆ Index](README.md) · [Agla: Principle 2 ➡](02-principle-2-code-interface.md)
