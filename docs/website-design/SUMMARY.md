# Made, Not Generated — Website Design Crash Course — Summary

"Taste is now a file" — achi design ki knowledge ab ek file mein likhi ja sakti hai jise koi bhi AI
follow kar sake. **Generated** website = jab koi guide na kare. **Made** website = jab koi real
choices banaye.

## 00 — Foundations
- **AI slop:** AI choose nahi karta, predict karta hai — open sawal pe sab se common (average) jawab
  deta hai. Proof: Anthropic ka apna frontend-design plugin apni AI ke 3 default looks list karta hai
  (`#F4F1EA` samet) aur unhe avoid karne ko kehta hai. Fix "prompt harder" nahi — **structural** hai:
  ek taste file jo specific patterns bana ke.
- **4-piece stack:** Model (code likhta hai), Taste (defaults se rokta hai), Media (real photos/video),
  Host (Vercel) — yehi 4 boxes client invoice ki bhi basis hain.
- **Design model chunna:** planning ke liye sabse capable model, execution ke liye sasta, **visual
  design/polish** ke liye jo bhi quarter design-arena lead kare (blind tests/LMArena pe trust karo,
  marketing pe nahi). "Rented-crown rule": habits tool+files ke ird-gird banao, model ke ird-gird nahi.
- **Apne tool mein koi bhi model:** Claude Code ko Kimi K3 se connect karna (`.claude/settings.json`
  env vars) — 5 ehtiyatein (`/status` se check, key `.gitignore`, web fetching nahi chalti route pe).

## 01 — Taste As a Skill
- **Hallmark** (free skill, `npx skills add Nutlope/hallmark`) — pehle page ki "shape" chunti hai (21
  shapes) colors se pehle, 20 named themes + Custom, khud-critique checklist, safety rule (existing
  site delete nahi karti bina bataye). 4 modes: default, audit (review-only), redesign, study.
  Anthropic plugin = judgment, Hallmark = machinery.
- **Study karo copy mat karo:** `study` command ideas leta hai pixels nahi. Rule: har project mein
  2-3 sites study karo, kabhi ek nahi.
- **Brand extraction:** specific poocho sab kuch nahi. Route 1 (free, receipt ke sath specific poocho),
  Route 2 (paid, Firecrawl), Route 3 (kabhi skip mat karo — client se seedha poocho). Pasand ki sites =
  direction; client ka brand = rules.

## 02 — The Build
- **Ek kahani, ek scroll:** 5-8 "beats" likho build se pehle. Ek screen ek idea. Page ka top real
  cheez dikhaye slogan nahi. Aakhri beat kuch KARE (WhatsApp link / Formspree / server program).
- **Media pipeline — 4 lanes:** Lane 1 real photos (free — Unsplash/Pexels, light match karo), Lane 2
  AI-made free (ChatGPT free ya Pollinations/Cloudflare — "free plans mausam ki tarah"), Lane 3 paid
  cents (fal.ai/Replicate), Lane 4 video paid credits (Higgsfield — cost pehle check karo, Gemini Omni
  Flash = shot dhoondo, Seedance 2.0 = shot lock karo). Permission ke 4 aadatein (rules parho, record
  rakho, real logon ka istemal mat karo, AI-made batao).
- **Mobile primary device:** "same story, alag shape ke liye dobara film ki gayi" — kahani nahi badalti,
  pictures dobara li jati hain, layout-break jaan-boojh kar decide karo, thumbs ≠ mouse pointers. Wahi
  session mein karo.
- **Multi-page — 3 rules:** har page ki apni wajah ho; ek client ke andar sameness chahiye (same
  design.md); simple site pe file hi address hai — menu/footer duplication ka fix (light: auto-check;
  heavy: Astro).

## 03 — Verification for Design
- **Visual verification loop — 3 checkers:** Screenshot (AI apni banai page dekhe, 1440px+390px, poori
  page, live pe bhi), Audit (Hallmark ka `audit` — specific problem list, "kam generic banao" fail nahi
  ho sakta), Automatic Rule (chhota program jo yes/no de — checks khud likho AI se nahi likhwao).
- **Limit example:** Ayesha project mein ledger PKR 217,950 vs 217,930 mismatch — audit/review/screenshots
  kisi ne nahi pakra, sirf ek insaan ne numbers add kar ke pakra. "Automate jo ho sake, attention wahan
  jo kabhi na ho sake."
- 2 groups pehli build se: accessibility (contrast, keyboard nav, motion-reduce) aur page-weight
  (&lt;1MB first screen, lazy-load, muted autoplay).
- **Cross-model design review:** ek AI banata hai (Kimi K3), **alag company** ka AI review karta hai
  (Claude) — same/sibling AI dobara nahi, kyunke same blind spots share ho sakte hain. Demanding sawal:
  "3 jagah batao jahan AI-made lagti hai."

## 04 — Ship
- **Deploy (Vercel):** `vercel` = preview, `vercel --prod` = real. Apna address kharido (client ke naam
  pe), findability (title, description, `og.png` 1200×630 sharing card).
- **Client workflow — 6 steps:** likhit agreement pehle, brand dhoondo phir confirm, kahani becho na ke
  finished picture, phone pe review karwao, 4-boxes se price karo, sahi tareeqe se handover karo.
  Compound move: process ko skill file ki tarah save karo.
- **Cost discipline:** pictures pehle price karo. Poori website ka code chai ki keemat se kam ho sakta
  hai; video sab se mehnga hissa ho sakta hai. Doosri company ka AI conversation cost wapas laata hai
  (~10x discount tab tak jab tak conversation unchanged rahe).

## 05 — Complete Worked Example (Ayesha's Practice Site)
- Client: Ayesha Rehman, Lahore accountant. 6-beat story spine (shoebox → sorting → bold balancing
  animation → monthly clarity → person → book consultation). Media: Lane 1 (real phone photos) +
  code-animation (beat 3) + optional custom video.
- **8 steps:** rules file (AGENTS.md-jaisi), taste layer install (Hallmark), brand extract + study
  (2 sites), plan mode (6 beats, push back against boring first draft), build (computer→phone same
  session), media pass, verify (audit found 7 problems, cross-model review found 2 more — cooler light,
  low-contrast button), publish + save process as skill.
- **Zaroori limit repeat:** automatic checks ne ledger ki galti nahi pakri — sirf insaan ne. "Jo check ho
  sake automate karo, jo kabhi na ho sake uspe attention kharch karo."
