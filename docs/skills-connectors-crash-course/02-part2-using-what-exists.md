# 02 — Part 2: Jo Already Exist Karta, Use Karna (Concepts 6-9)

## Concept 6 — Built-In Skills

Anthropic ke skills jo finished files produce karte, sab ek switch par depend karte: **"Code
execution and file creation"** (Settings → Capabilities):

- **Word** — formatted `.docx`
- **PowerPoint** — description se full slide deck
- **Excel** — real spreadsheets, formulas ke sath
- **PDF** — create+fill

Sirf pucho: _"prepare a slide deck introducing agentfactory.panaversity.org to a general
audience"_ — finished deck wapas aayega.

Customize → Skills mein fresh account par ek skill milegi: **skill-creator** (Anthropic ki skill
jo tumhari skills banane mein help karti). Document skills missing nahi hain — wo **engine mein**
rehte, list mein nahi.

"+" → "Browse skills" se directory khulti — Notion/Figma/Atlassian jaisi partner skills bhi
one-click install ho sakti. Installed skills view-only hain; change karne ke liye copy download
karo, edit karo, apni tarah upload karo.

Wider ecosystem bhi hai — Skills late 2025 mein open standard bani, community sites tens of
thousands list karte. **Yeh gift aur hazard dono hai.** Stranger ka free skill ek text file hai
jise tum AI ko follow karne de rahe. Built-in + official directory safe starting point hain.

## Concept 7 — Apna Apps Connect Karna

~1 minute per app. Chat se "+" click karo (ya `/` → Connectors → "Manage connectors" → "+"), ya
Customize → Connectors. Service pick karo, Connect click karo, sign in karo — normal "allow this
app" flow.

**4 practical notes:**

- Connect karne ke baad, **conversation ke liye enable** karo ("+" → Connectors → switch on)
- Free plans mein 1 custom connector included; ready-made directory connectors broadly available
- Har connector actions ki list laata (settings isay "tools" bolte, is course ke 5-products se
  alag). **Tool access** setting control karti kab yeh actions load hon — 10+ connectors on hon
  to load-on-demand choose karo
- "Interactive" badge dekho — wo connectors live interfaces chat mein draw karte

**Doctor worked example (fake data):** "Make a one-page Word doc of a fake patient intake form
(DEMO-Okafor-2026-03...) aur save it to my Google Drive" → phir "Find DEMO-Okafor-2026-03 in my
Drive aur SOAP-style note banao." Ek connector mein dono directions dekhi.

> **2 honest notes:** Drive connector documents parhta hai par in-place edit nahi kar sakta — "write"
> ka matlab naya file save karna hai (Code execution + Drive write permission chahiye). Real data
> (healthcare/legal/student records) par sirf approved accounts use karo.

## Concept 8 — Real Magic: Skills + Connectors Together

**Connector real data fetch karta. Skill output shape karta.**

**Accountant ki monthly close:** "client-summary" skill + Drive connected = 2 short messages.
Pehla, sample ledger banao; phir: _"Prepare the March client summary for DEMO Trading from
DEMO-ledger-March in my Drive."_ Drive connector ledger fetch karta, skill currency-format karta,
expense-head se group, withholding flag, firm ke 4-section template mein. **2-ghante ka ritual
2-minute review ban jata.**

**Marketer ki weekly batch:** "brand-voice" skill (no exclamation marks, question-hook, banned
buzzwords) + Notion connector (content calendar) = "Draft captions for this week's three scheduled
posts in Notion, in our voice." Same template engineer (design-review skill + Linear connector)
aur teacher (lesson-plan skill + Drive connector) ke liye bhi fit karta.

## Concept 9 — Kaunsa Problem Kaunsa Chahta?

2 sawal pucho: **"Main 'how' dobara explain kar raha?"** = Skill. **"Main doosri app se data
fetch kar raha?"** = Connector. Dono = dono.

| Friction | Chahiye | Example |
|---|---|---|
| "Same formatting/voice/method rules paste karta har baar" | **Skill** | Brand voice, report template, SOAP notes |
| "Output ek certain tareeqe se dikhna chahiye hamesha" | **Skill** | Board-paper structure, invoice layout |
| "Drive/Gmail/Slack/tracker se data copy karta rehta" | **Connector** | Ledger, email thread, tickets pull karna |
| "AI ko doosri app mein kuch _karna_ hai" | **Connector** (write) | Linear issue banana, email reply draft, Notion page update |
| "Real data fetch karna hai _aur_ specific tareeqe se chahiye" | Dono | Monthly close, weekly batch, design review |
| "Sirf ek baar ka answer chahiye abhi" | Koi nahi | Single question, dobara na hone wala draft |

**2 honest cautions:** Har task skill deserve nahi karta — ek baar ka task sirf achhi prompt hai,
skill sirf tab worth hai jab task repeat ho. Zaroorat-se-zyada connector = khula darwaza — sirf
jo workflow chahta wo apps connect karo. **Scope safety hai.**
