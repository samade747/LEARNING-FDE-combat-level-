# 05 — Complete Worked Example: Ayesha Ki Practice Site

**Client:** Ayesha Rehman, Lahore mein accountant. Wo apni practice relaunch kar rahi hai — purani site
ek purana page hai outdated logo ke sath. Visitors (small business owners) ko lagna chahiye: *"ye banda
meri mess samajhta hai"* aur *"ye pehle hi solve kar chuka hai."*

**6-Beat Story Spine:**
1. Shoebox — receipts, sab ka guilty secret
2. Sorting — chaos categories ban raha hai
3. **Bold moment** — ledger animated hote hue balance hota hai
4. Monthly clarity — ek clean statement
5. Person — Ayesha, uska office, real Lahore light
6. Book a consultation — ek button

**Media:** Lane 1 (real photos) beats 1,2,4,5 ke liye — 2 phone pe li hui office photos. Beat 3 ka
animation code mein banaya, video nahi. Custom video optional extra, price pehle se quoted.

## 8 Steps

### Step 1: Rules File

```markdown
# ayesha-practice-site
## Layout
- `site/`: website source
- `assets/`: media, beat ke naam se
- `design.md`: brand constraints, design se pehle parho
- `docs/plans/story-spine.md`: approved 6-beat spine

## Critical rules
- design.md ek spec hai, mood nahi. Colors/fonts kabhi substitute mat karo.
- Har image ka alt attribute ho. Koi asset 500KB se bara nahi.
- Significant changes ke baad, 1440px aur 390px pe screenshot lo, dono review karo.
- Story spine ke beats reorder/drop mat karo bina puche.
```

### Step 2: Taste Layer Install Karo
```bash
npx skills add Nutlope/hallmark
```
Claude Code mein Anthropic ki frontend-design plugin bhi install karo.

### Step 3: Brand Extract Karo, Direction Study Karo
Purani site se colors/fonts/logo receipt ke sath nikalo. Phone call karo — Ayesha bata deti hai wo brand
change kar rahi hai (green rehta hai, gold amber ban jata hai, naya logo bhejti hai). Hallmark `study`
2 sites pe chalao jo usay pasand hain. Sab `design.md` mein, rules ki tarah marked.

### Step 4: Plan Mode — Spine Se Structure Tak
Plan mode mein 6 beats describe karo. **Pehla plan boring hota hai** — normal page, beats squeeze kiye
hue. Push back karo:
```text
The scroll is the story. One beat per screen. The balancing
animation gets a whole screen to itself. No rows of feature
boxes anywhere.
```

### Step 5: Design Model Se Build Karo
`/status` se Kimi K3 confirm karo. **Wahi session mein dono versions banao** — computer pehle, phone
turant baad, taake AI ki memory taazi rahe.

### Step 6: Media Pass
Helper AI free photo libraries mein beats 1,2,4 dhoondta hai (alag conversation mein). Office photos
beat 5 ke liye `assets/` mein.

### Step 7: Verify — Screenshots, Audit, Cross-Model Review
Hallmark `audit` **7 problems** dhoondta hai (ek sirf hover pe kaam karta tha — phone pe totally fail).
Fix karo, dobara chalao, list khaali hone tak. **Claude, Kimi K3 ke kaam ko review karta hai** — 2
cheezein pakarta hai jo builder khud nahi dekh saka: beat 4 ki photo ki light cooler thi, amber button
green background ke against parhna mushkil tha.

### Step 8: Publish, Process Save Karo
Findability (title, description, sharing card). `vercel` preview, live page ki final pictures lo,
Ayesha ko *"phone pe kholo"* ke sath bhejo. Approval ke baad: `vercel --prod`, uski `.pk` address
connect karo, Google se register karo, handover package do.

> **Compound move:** Poora process **skill file** ki tarah save karo — story template, brand sawal,
> audit-then-review order, publishing checklist. **Ayesha ki cousin ki textile business ke liye agli
> website aadhe waqt mein.**

## Kya Hua

Coding course se: rules file, plan mode, skills, helper AI, automatic checks, second opinion. Naya
yahan: taste file, pictures ka tareeqa, screenshot bataur test, live web address bataur finished product.

> **Aap designer nahi bane. Aap ne ek checking machine ko nayi tarah ke kaam pe point kiya** — aur
> machine, ek achhi taste file ke sath, baaki kaam kar deti hai.

**Zaroori limit:** Automatic checks ne Ayesha ke ledger ki galti nahi pakri (PKR 217,950 vs 217,930) —
sirf ek insaan ne numbers add kar ke pakri. **Yehi ratio poori course ka argument hai:** jo check ho
sake, automate karo; jo kabhi nahi ho sakta, uspe apna attention kharch karo.

---
[⬅ Ship](04-ship.md) · [⬆ Index](README.md)
