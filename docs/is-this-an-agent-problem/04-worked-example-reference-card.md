# 04 — Ek Real Task Par Teenon Gates Chalao + Reference Card

## Teenon Gates Ek Sitting Mein

Gates theory hi rehte hain jab tak aap ek real task ko teenon se guzaar nahi dete.

Kuch chuno jo abhi karna hai. Isay walk through karo:

1. **Gate 1.** Regular tool, chatbot, ya agent? Agar "agent" se pehle ruk jaye — aap ne poora session
   bacha liya, sahi tool use karo aur aage barho.
2. **Gate 2.** Agar agent job hai: ek dafa (Mode 1), ya helper banao (Mode 2)? Agar teenon dials upar
   hain, Mode 2 task hai: haath se solve karte raho jab tak method stop change hona, phir worker mein
   cross karo.
3. **Gate 3.** Agar solve-it-once agent job hai: teen lines likho. Works from, want at end, done when.

Agar task doosre sirre tak pahunche — agent, Mode 1, teen lines likhi hui — **tab** agent kholo.

> **Yeh kyun matter karta hai:** Gates lagbhag 10 minute lete hain. Jo galtiyan yeh rokte hain, woh
> poori dopeher le sakti hain — aur Mode 2 wali galtiyan mahine le sakti hain. Poora trade yehi hai:
> thora sochna shuru mein, badle mein woh ghante jo aap otherwise ghalat jagah se shuru karke gawa dete.

Pehla decision kabhi bhi "agent se kaise baat karein" nahi tha. Woh tha: **kya karna hai**, **kis type
ka kaam hai**, aur **kis taraf**. Yeh sahi karo, to agent se baat karna aasan ban jata hai.

---

## Reference Card — Har Answer Aapko Kahan Bhejta Hai

Teenon gates aapke *kaam* ko route karte hain, kisi tool ka naam liye bina — jaan-boojh kar. Gate
constant hai; tool variable hai (tools har kuch mahino mein badalte hain). 2026 mein yeh variable aisa
dikhta hai:

| Gates Ne Kahan Bheja | Matlab | 2026 Tools |
| --- | --- | --- |
| **Sirf jawab** (Gate 1 → chatbot) | Knowledge, draft, ya ideas chahiye the. Kuch bhi aapka nahi chhuta. | claude.ai, ChatGPT, ya Gemini |
| **Ek dafa solve karo** (Gate 1 → agent, Gate 2 → Mode 1) | Agent jo aap *drive* karte ho ek session ke andar: woh act karta hai, aap dekhte ho, ship karte ho, chale jate ho. | Claude Code ya OpenCode (terminal/editor); Cowork ya OpenWork (desktop app) |
| **Worker khud own karo** (yeh *ownership* choice hai, mode nahi) | Aapko ek durable worker chahiye jo aap khud chalayein aur own karein — jo hafton tak yaad rakhe aur aap ke sote waqt bhi jawab de. | Personal harness: OpenClaw (kai chat apps tak reach) ya Hermes (deep memory) |
| **Manufacture karo** (Gate 2 → Mode 2) | Ek organization ke liye bana worker — ek Digital FTE jo reliably aur scale par chale. | OpenAI Agents SDK, ya managed Claude agent setup |

### Jahan Yeh Do Rows Blur Hote Hain

Row 3 aur 4 dono "durable worker jo aap ke bina chalta hai" hain. Farq batane wali cheez: **worker
kiske liye hai.** Agar *aap* ke liye hai — aapka inbox, code, errands — woh personal harness hai, poora
Mode 2 track nahi chahiye. Agar *organization* ke liye hai — deployed, governed, scale karna hai — woh
Mode 2 hai. Same activity, different owner.

**Ownership koi teesra mode nahi hai.** Yeh ek alag sawal hai: aap Mode 1 (ek-dafa solve) **ya** Mode 2
(banao taake chale) — dono, ek owned harness ke upar bhi chala sakte ho.

- **Ownership** poochta hai: "mai drive karta hoon, ya own karta hoon?"
- **Mode** poochta hai: "ek dafa solve karta hoon, ya lasting banata hoon?"

Yeh do alag sawal hain, kabhi collide nahi karte.

---
[⬅ Gate 3](03-gate-3-what-is-finished.md) · [⬆ Index](README.md) · [Agla: Practice ➡](05-practice-projects.md)
