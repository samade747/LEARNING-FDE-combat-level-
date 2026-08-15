# 01 — Taste As a Skill

## Concept 5: Hallmark — Ek Taste File Jiske Daant Hain

**[Hallmark](https://github.com/Nutlope/hallmark)** ek free design skill hai jo *"AI ki banai pages ko
made banati hai, generated nahi."*

```bash
npx skills add Nutlope/hallmark
```

Files `~/.claude/skills/hallmark/` mein jati hain — OpenCode wahi folder parhta hai, ek install dono
tools serve karti hai. **Organization khud ek lesson hai:** ek chhota `SKILL.md` + `references` folder
(58 checks, fonts, colors, spacing, 21 page shapes, themes). Model sirf zaroorat pe extra files parhta
hai.

**Andar kya hai:**
- **Pehle page ki "shape" chunti hai** — colors se pehle, **structure** 21 shapes mein se. Ye Hallmark
  ko special banata hai — zyada tar "different banao" koshishein sirf colors badalti hain, ye **skeleton**
  badalta hai
- **20 named themes + Custom** — rotation rule se ek theme pe settle nahi hoti
- **Lambi checklist wapas dene se pehle** — apne kaam ko khud criticize karti hai
- **Safety rule** — existing website pe point karo to bina bataye files delete nahi karti

**4 modes:**

| Command | Kya Karta Hai | Kab |
| --- | --- | --- |
| **default** | Naya page banata hai | Kuch naya shuru kar rahe ho |
| **audit** | Existing page review karta hai, kuch badalta nahi | Honest review chahiye |
| **redesign** | Purani shape phenk deta hai, words/brand rakhta hai | Page kaam karta hai lekin generic lagta hai |
| **study** | Ek pasand ki website se seekhta hai | Achi site se seekhna hai |

> **Lineage:** Hallmark Anthropic ki frontend-design plugin se inspired hai. Anthropic **judgment**
> sikhata hai (studio designer ki tarah kaam karo). Hallmark **machinery** deta hai (shapes, themes,
> checks). Dono saath kaam karte hain.

> **Ehtiyat:** Kimi K3 jaisay non-Claude model ke sath, AI khud se skills utha nahi pata reliably — har
> design step pe Hallmark ka naam type karo, umeed mat rakho.

## Concept 6: Study Karo, Copy Mat Karo

Kisi pasand ki site ko point karo, `study` likh deta hai kya cheez usay kaam karti hai — shape, fonts,
color, spacing — `design.md` mein. **Ye pixels copy nahi karta, ideas leta hai.**

**Rule:** Har project mein **2-3 sites study karo, kabhi ek nahi.** Ek site copy karne ki taraf khenchti
hai. 3 sites combine karne pe majboor karti hain — yehi original feel karne wale kaam ka source hai.

## Concept 7: Brand Extraction — Client Ki DNA Pehle Se Online Hai

**Asal idea:** **specific cheezein poocho, sab kuch nahi.** Poori page point karo to AI **confidently
galat color invent** kar deta hai.

**Route 1 (free):** AI se specific poocho, receipt ke sath:
```text
From this page, list the exact color codes of the three most-used
brand colors, the names of the fonts, and the address of the logo
file. For each one, quote the line of code where you found it.
```

**Route 2 (paid, cleaner):** Firecrawl jaisay tools — brand ka logo/colors/fonts seedha nikaal dete hain.

**Route 3 (kabhi mat skip karo):** **Client se seedha poocho.** Pehle 2 routes sirf first draft ke liye
hain. Live jane se pehle real files mango.

> **Zaroori farq:** Pasand ki sites **direction** hain (ideas borrow karo). Client ka brand **rules**
> hain (kabhi badal nahi sakte kyunke aapko kuch pyara mila). Taste skill in rules ke **andar** design
> karti hai.

---
[⬅ Foundations](00-foundations.md) · [Agla: The Build ➡](02-the-build.md)
