# 03 — Verification for Design

## Concept 11: Visual Verification Loop

Poori book ka sab se zaroori pattern: **try, check, fix, repeat.** Design ke liye "acha lagta hai"
pehle check nahi ho sakta tha — ye concept usay fix karta hai. **3 checkers, gentle se strict:**

### Checker 1: Screenshot — AI Ko Aankhein Do

Har build round ke baad, AI apni banai page ki **tasveer leta hai aur usay dekhta hai** — code nahi.
Code parhne wala AI ye nahi jaan sakta ke 2 text pieces overlap kar rahe hain, video load nahi hui, ya
button background jaisa color hai.

> Anthropic ki design skill: ***"a picture is worth 1000 tokens."*** Dekhna **sasta** hai code parhne
> se.

```text
After every significant change, take a picture of the page at
1440 pixels wide and at 390 pixels wide, and look at both before
saying you are done.
```

**Poori page capture karo**, sirf pehla hissa nahi. Site online hone ke baad, **live** page ki tasveer
lo.

### Checker 2: Audit — Taste Ko List Mein Badlo

Hallmark ka `audit` command specific problems ki list deta hai, kuch badalta nahi. *"Kam generic banao"*
kabhi fail nahi ho sakta, isliye kuch drive nahi karta. *"In 7 problems ko fix karo"* khatam ho sakta
hai, check ho sakta hai.

### Checker 3: Automatic Rule — Jo Hamesha Sach Hona Chahiye

Kuch cheezein AI ke judgment pe nahi chhorni chahiye. **Rules file mein likhna** ek instruction hai jo
AI **usually** follow karta hai. **Real check** ek chhota program hai jo yes/no jawab deta hai:

```javascript
// check-site.mjs — MISSING DESCRIPTION aur TOO BIG check karta hai
// ... (imgs bina alt ke, files size limit se bare)
if (problems.length) { console.error(problems.join("\n")); process.exit(1); }
console.log("All checks passed.");
```

> **Ehtiyat, coding course se dohraya gaya:** Ye checks **khud likho**, AI se mat likhwao — apni hi
> aadaton ke khilaf test likhne wala AI usay aasan bana dega.

**Ye kya nahi pakar sakta:** Ayesha project mein, beat 3 ka ledger PKR 217,950 total tha, beat 4 mein
PKR 217,930 dikha. **Audit, reviewing AI, screenshots — kisi ne nahi pakra**, kyunke sab "page theek
lagti hai" check kar rahe the. **Ek insaan ne 3 numbers add kiye aur pakar liya.**

> **Automate karo jo check ho sake, apna attention us pe kharch karo jo kabhi nahi ho sakta.**

**2 groups jo pehli build se hi honi chahiye:**
- **Sab log site use kar sakein** — contrast, keyboard navigation, motion-reduce respect
- **Page load hone jitni halki ho** — Pakistan jaisi jagah mein log mid-range phones + data by megabyte
  use karte hain — first screen <1MB, video ke peeche still picture, scroll pe lazy-load, autoplay
  video muted

## Concept 12: Cross-Model Design Review

*"AI jisne kuch banaya, wahi review karne ke liye sab se bura hai."* Design mein ye rule aur mazboot hai:
**AI apni hi habits nahi dekh sakta** — uske liye ye "websites kaisi lagti hain" hai, habit nahi.

**Setup:**
1. **Ek AI banata hai** — Kimi K3
2. **Alag company ka AI review karta hai** — same AI dobara nahi, sibling bhi nahi. Brief + `design.md`
   + **screenshots** do. Demanding sawal poocho: *"3 jagah batao jahan AI-made lagti hai aur kyun"*
3. **Builder findings parh kar fix karta hai** — agar dono AI disagree karein, aap decide karo

> **Alag company kyun zaroori hai:** 2 AI models same blind spot share kar sakte hain bina same company
> se hue bhi. Kahin aur se reviewer sab se sasta tareeqa hai wo dekhne ka jo builder khud apne baare
> mein nahi dekh sakta.

**Bonus:** Review file save hoti hai — client ko dikha sakte ho: *"Independent review ne 5 issues
dhoonde, sab 5 fix ho chuke."*

---
[⬅ The Build](02-the-build.md) · [Agla: Ship ➡](04-ship.md)
