# 01 — Yeh Kaise Wire Hai: Ek Source, Teen Gateways

Diagram top se bottom parhta hai: **kaun use karta hai, kis se connect hote hain, woh connections kis
cheez se bani hain, aur truth kahan rehti hai.** Char layers, ek flow.

## Layer 1 — Teen Audiences, Teen Darwaze

- **Learners** apni free Claude account par aate hain. Ek connector add karo, ek baar authorize karo,
  seekhna shuru. Kuch install nahi, kuch pay nahi.
- **Builders** apne coding agent (Claude Code ya OpenCode) ke andar aate hain. Unka darwaza ek plugin
  hai, kyunke construction work wahin hota hai.
- **Authors** woh agents hain jo derivative books produce karte hain — topic, age, profession ke
  hisaab se rewrite kiye hue. Unka darwaza ek publishing pipeline hai.

Har audience ko wahin milo jahan woh already kaam karte hain. Koi naya app adopt nahi karna, koi nayi
habit nahi banani.

## Layer 2 — Thin Gateways, Ek Har Audience Ke Liye

- **Zia Tutor AI gateway** — teaching lane: jab Zia greet karta hai, understanding check karta hai,
  progress record karta hai, uska Claude isi se baat karta hai.
- **Zia Developer AI gateway** — construction lane: jab Zia architecture chunta hai, spec likhta hai,
  build karta hai, coding agent isi se baat karta hai.
- **Publishing gateway** — derivative-book pipeline, author agents ko canonical material deta hai jo
  woh specialize aur rewrite karte hain.

Gateways jaan-boojh kar **thin** rakhe gaye hain: woh sirf decide karte hain audience kya reach kar
sakta hai aur unke liye kaise shape karna hai. Asli functionality ek layer neeche hoti hai.

## Layer 3 — Component MCP Packages, Har Gateway Par Mounted

- **content** — book, System of Record ki shakal mein. Har lane verified chapters, definitions, aur
  patterns parhta hai, training data se guess karne ke bajaye.
- **learning** — learner state. Progress, history, kahan chhoda tha. Yehi cheez Zia Tutor AI ko
  din/hafton baad conversation resume karne deti hai.
- **pedagogy** — teaching moves. Kaise explain karna hai, kab quiz lena hai, kaise correct karna hai —
  yeh tools ki shakal mein encode kiya gaya hai, model ki apni marzi par nahi chhoda gaya.
- **builder** — build patterns. Specs, `SKILL.md` templates, aur recipes jo Zia Developer AI assemble
  karta hai working agents banane ke liye.

Yeh **composition hai, duplication nahi**. Har gateway sirf utna hi mount karta hai jitna use chahiye,
to content package ek baar fix karo aur teeno lanes ko fix mil jata hai.

## Layer 4 — Ek Source of Truth, Ek Database

- **Git repo (canonical)** — book MDX format mein. Har chapter, figure, definition ki master copy.
  Book yahan badlo, upar sab kuch inherit karta hai.
- **Ek Postgres** — baaqi sab kuch: relational data, vector embeddings, full-text search — sab ek hi
  database mein. Canonical MDX isi mein ingest hota hai taake packages fast query kar sakein.

Book ka apna thesis, khud par apply kiya hua: **consolidate by default, specialize deliberately.**

## Yeh Shape Kyun Hai

Truth ek baar define hoti hai (Git), ek baar store hoti hai (Postgres), reusable capabilities ke zariye
expose hoti hai (packages), aur thin, audience-shaped doors ke zariye deliver hoti hai (gateways). Baad
mein naya product add karna (nayi audience, naya lane) matlab bas usi packages par ek naya thin gateway.
Source kabhi nahi badalta. Yehi cheez isay **ecosystem** banati hai, teen alag apps nahi.

## Economics — Ek Naye Tarah Ka App, Aur Cost Zero Ke Qareeb Kyun Hai

Connector-native apps aur plugins **tools** laate hain; user apna **model** khud laata hai. Yeh
economics ko ulta kar deta hai: value un logon tak pohanchti hai jo already free tier AI apps use kar
rahe hain, to hum sainkron logon tak scale kar sakte hain us LLM bill ke bina jo aam taur par reach ko
cap kar deta hai — ghar mein bhi, bahar bhi.

Yeh khud seekhne ke liye chaar crash courses hain jo book mein already maujood hain:
[Connector-Native Apps](../connector-native-apps/README.md), Plugins for AI Agents, AI Identity (auth),
aur RAG on Postgres.

---
[⬅ Char Products](00-the-four-products.md) · [⬆ Index](README.md) · [Agla: Economics Aur Business Model ➡](02-economics-and-business-model.md)
