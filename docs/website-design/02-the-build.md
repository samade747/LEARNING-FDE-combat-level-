# 02 — The Build

## Concept 8: Ek Kahani, Ek Scroll

Achi websites **stack ki hui sections** nahi hain — ek **kahani** hain, jo scroll karte waqt sunayi
jati hai. Ek screen, ek idea.

- **Build shuru hone se pehle kahani likho** — 5-8 steps, **beats** kehte hain. Accountant ke liye:
  shoebox of receipts → sorting → accounts khud balance ho rahe → clear monthly picture → person →
  book a meeting
- **Ek screen, ek idea** — 2 points ek screen pe, matlab **zero** points
- **Page ka top real cheez dikhaye**, slogan nahi — shoebox of receipts, na ke "Innovative solutions"
- **Ek moment bold ho, baaki calm** — sab jagah bold hona mess lagta hai

**Aakhri beat kuch KARE.** Simple website ke paas message receive karne ka koi system nahi hota —
**3 options, sasta pehle:**

1. **WhatsApp link** — `https://wa.me/923001234567?text=...` — kuch banane ki zaroorat nahi, message
   wahin ata hai jahan owner already reply karta hai
2. **Form service** — Formspree, free plan kaafi hai
3. **Server pe chhota program** — Vercel, jab project itna bara ho ke zaroorat pare

> **Kahani jo ek button pe khatam ho jo kuch na kare, website nahi — poster hai.**

## Concept 9: Media Pipeline — 4 Lanes

**Real secret: tasveerein aadha kaam karti hain.**

**Lane 1: Real photographs (free, hamesha)** — Unsplash, Pexels. **Light match karo** (mixed lighting
"assembled from strangers" lagti hai). **Crop jaan-boojh kar karo.** Local business ke liye: **phone
camera evening light mein generic stock se behtar hai.**

**Lane 2: AI-made pictures, free (ek catch ke sath)** — *"jab free ho, quality ya convenience, dono
nahi."* **2a: haath se, best AI se** (ChatGPT free plan — text kar sakta hai, consistent style rakhta
hai). **2b: automatic, kamzor** (Pollinations.ai, Cloudflare Workers AI) — rough drafts ke liye. *"Free
plans mausam ki tarah hain"* — jis din banao, us din ka page check karo.

**Lane 3: Paisay ke chand cents per picture** — same excellent AI, automatic, ~half cent (low) se ~20
cents (high) tak. fal.ai, Replicate.

**Lane 4: Video, paid credits ke sath** — Higgsfield: `npm install -g @higgsfield/cli`. **Cost pehle
check karo:**
```bash
higgsfield generate cost workflow draw_to_video --duration 8.2 --resolution 720p
```
**Gemini Omni Flash** shot **dhoondta** hai (talk kar ke refine karo). **Seedance 2.0** shot **lock**
karta hai (steady motion, 9 reference pictures). **Pehle dhoondo, phir lock karo.**

> **Har lane ka rule:** Story se pictures banao, ek per beat, `assets/` mein clear naam se, final layout
> se **pehle**.

**Permission ke 4 aadatein:** current rules parho, kya banaya record rakho, real logon/logos ka istemal
mat karo, client ko batao kaunsi pictures AI-made hain.

## Concept 10: Mobile Primary Device Hai

**"Same story, alag shape ke liye dobara film ki gayi."**

- **Kahani nahi badalti** — sab beats har device pe. Test: agar phone pe beat drop ho sakti hai, wo
  decoration thi, story nahi
- **Pictures dobara li jati hain** — wide video **tall** video banti hai, squeeze nahi hoti
- **Layout kahan badalti hai, jaan-boojh kar decide karo:** *"768px se neeche, tall video use karo,
  sections full-width karo"*
- **Thumbs mouse pointers nahi hain** — buttons bare hon, hover pe kuch important na ho

**Kab karein:** **Wahi session mein**, computer version ke turant baad, AI ki memory taazi ho.

```text
computer version → phone version → screenshots at both widths → audit → second opinion → publish
```

## Multi-Page Sites — 3 Zaroori Rules

**Rule 1:** Har page ki apni wajah honi chahiye — *"visitor ke paas alag kaam ho to naya page."*

**Rule 2:** Alag clients ke darmiyan Hallmark sameness se larti hai. **Ek client ke andar, sameness hi
chahiye** — 5 pages ek building ke 5 kamre lagne chahiye, same `design.md`.

**Rule 3:** Simple site pe, **file hi address hai** (`services.html` = `/services.html`). Asal mushkil
**copying** hai — menu/footer har file mein duplicate. **Light fix:** automatic check jo save block kare
agar menus match na karein. **Heavy fix:** Astro jaisi system jo menu ek dafa likhe.

---
[⬅ Taste as a Skill](01-taste-as-skill.md) · [Agla: Verification for Design ➡](03-verification.md)
