# 00 — Overview: The Shift

## Ab Tak Sirf Chat Tab

6 courses tak, aap chat tab mein kaam karte rahe. Aap ne poocha. Wo bola. Aap ne phir poocha. **Har turn
aap se shuru hota tha.** Ye seekhne ka acha tareeqa tha. Lekin plain chat ki ek limit hai: **jab aap
type karna band karo, conversation ruk jati hai.**

**July 2026 ne ye badal diya.** Do bari companies (Anthropic, OpenAI) ne apne apne agent surfaces browser
mein la diye, chat box ke bilkul bagal mein, usi web address pe:

- **claude.ai** pe **Claude Cowork** — Anthropic ke servers pe **remote session** ki tarah chalta hai
- **chatgpt.com** pe **ChatGPT Work** — Chat mode ke bagal mein ek naya *mode*, GPT-5.6 pe based

Chat box nahi badla — abhi bhi aapka wait karta hai. **Jo badla wo iske bagal wala surface hai.** Wahan
session shuru karo, aur ye company ke servers pe chalti hai. Aap tab band kar sakte ho. Plane mein baith
sakte ho. **Kaam chalta rehta hai.** Aur jab ye kisi aisi decision pe pohanche jo sirf aap le sakte ho,
sawal aapke phone pe ata hai.

## Test — Jo Kisi Bhi Company Ke Marketing Ko Cut Through Karta Hai

> **"Agar main type karna band kar doon, kya kaam ruk jayega?"**

Chat box: **haan.** Agent surface: **nahi.** Ye ek sawal har jagah, har company se, har saal is line ko
alag kar deta hai.

**Deeper version:** plain chat turn **synchronous** hai — aap wait karte ho, jawab ata hai, phir wapas
aapka wait. Agent run **delegated** hai — ek dafa shuru karo, wo outcome ki taraf badhta rehta hai. Aapke
agle turn ki zaroorat nahi.

## Concept 2: Remote Session — Tab Ek Window Hai, Runtime Nahi

Agent 2 jagah reh sakta hai. **Aapki machine pe** (desktop apps, terminals — agli courses) — wahan app
hi runtime hai, laptop band = kaam ruka. Ya **vendor ke servers pe** (ye course) — wahan **aapka browser
tab ek window hai, machine nahi.**

**3 consequences:**
- **Tab band karo: kaam chalta rehta hai** — session tab mein kabhi thi hi nahi
- **Phone se session kholo: wahi session hai** — copy nahi, wahi chalta hua kaam
- **Scheduled task ek band tab se bhi fire hoti hai** — schedule bhi vendor ke servers pe rehta hai

**Ehtiyat:** Remote session sirf wahi reach karti hai jo vendor ki machines reach karti hain — aapke
connectors, apni task filesystem, aapki platform files. **Ye aapki local hard drive, desktop apps, ya
browser jahan aap bank mein login ho, khud reach nahi karti.** Un cheezon ke liye local bridge/agent
chahiye — agli courses ka kaam.

> **Simple:** Desktop agent aapke ghar ke andar ek worker hai — ghar ki bijli jaye, worker ruk jata hai.
> Remote session vendor ke office mein ek worker hai — aapke ghar ki bijli se farq nahi parta, aapka
> laptop aur phone sirf windows hain jinse aap check karte ho.

## Concept 3: 2 Vendors, Ek Shape

Anthropic aur OpenAI ne days ke andar agent surfaces browser mein bhej diye. **Dono products same 6 parts
express karte hain:**

| ChatGPT Work Isay Kehta Hai | Book Isay Kehta Hai | Matlab |
| --- | --- | --- |
| Scheduled Tasks | **Heartbeat** | Kya bina aapke kaam shuru karta hai: once, schedule, event, ya monitor |
| Plugin Directory | **Connectors** | Aapki real services tak permission-scoped reach |
| Outcome-based execution | **Run-until-done loop** | Outcome do, wo steps mein us tak pohanchta hai |
| Cloud-synced sessions | **State spine** | Devices/runs ke darmiyan yaad rehne wali memory |
| Approval prompts (mobile) | **Human gate** | Risky decisions phone pe insaan tak ati hain |
| Cloud execution environment | **Body** | Jahan kaam asal mein hota hai — docs, sheets, decks |

**Same table Cowork pe bhi chal jati hai, sirf Anthropic ke naam ke sath.** 2 vendors. Ek shape.

> **Sab se zaroori idea:** Naye products aate rahenge, naam badalte rahenge. **Shape ek dafa seekho, aur
> har naya agent product 30-minute read ban jata hai, naya subject nahi.**

**Farq kahan hai?** Model (Claude vs GPT-5.6), plan structure, connector ka naam. **Asal farq deeper hai:**
OpenAI ka coding agent (Codex) **usi app** mein hai jaise Work — Anthropic ka Claude Code **poori tarah
alag surface** hai.

**Ek boundary sab pe lagu hai:** Regulated data (PHI, privileged matter, financial records) **kisi bhi**
web surface ke liye target user nahi hai jab tak compliance likhit mein na kahe — kyunke working files
aur platform storage vendor ki custody mein hoti hain, **by definition**.

### Self-Check
**Sawal:** Aglay quarter, ek 3rd vendor "Flows" naam ka product launch karta hai: triggers, integrations,
autopilot mode, workspace memory. In 4 naamon ko book ke parts se map karo, bina docs parhe.
**Jawab:** Triggers = heartbeat. Integrations = connectors. Autopilot mode = run-until-done loop
(sawal: stopping condition kya hai, kaun check karta hai?). Workspace memory = state spine. **Aap ne
ek aisa product parh liya jo kabhi dekha nahi, ek minute se kam mein — yehi is concept ki skill hai.**

---
[⬅ Index](README.md) · [Agla: The Surface ➡](01-the-surface.md)
