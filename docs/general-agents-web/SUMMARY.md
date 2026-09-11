# General Agents on the Web — Summary

July 2026 mein Claude Cowork aur ChatGPT Work browser mein ek "agent surface" le kar aaye — chat box ke bagal mein, jo laptop band karne ke baad bhi chalta rehta hai. Yeh chapter is surface ko samajhne, safely use karne, aur choose karne ka poora lens deta hai.

## 00 — Overview: The Shift

- **Test:** "Agar main type karna band kar doon, kya kaam ruk jayega?" — Chat box: haan. Agent surface: nahi. Plain chat **synchronous** hai; agent run **delegated** hai.
- **Concept 2 — Remote Session:** Agent 2 jagah reh sakta hai — aapki machine (desktop apps) ya vendor ke servers (yeh course). Web pe, **browser tab ek window hai, machine nahi**: tab band karo, kaam chalta rahega; phone se session kholo, wahi session milegi; scheduled task band tab se bhi fire hoti hai. Ehtiyat: remote session sirf vendor ki machines reach karti hai (connectors, task filesystem, platform files) — local hard drive/desktop apps/logged-in browser khud reach nahi karti.
- **Concept 3 — 2 Vendors, Ek Shape:** ChatGPT Work aur Claude Cowork dono same 6 parts express karte hain: Heartbeat (Scheduled Tasks), Connectors (Plugin Directory), Run-until-done loop (Outcome-based execution), State spine (Cloud-synced sessions), Human gate (Approval prompts/mobile), Body (Cloud execution environment). **Shape ek dafa seekho, naya product 30-min read ban jata hai.**
- Boundary: regulated data (PHI, privileged matter, financial records) kisi bhi web surface ke target user nahi hai jab tak compliance likhit mein na kahe — working files/platform storage vendor ki custody mein hoti hain **by definition**.

## 01 — The Surface: Sessions, Files, Connectors, Gate

- **Concept 4 — Account Spine:** sessions/files account mein save hoti hain, kisi bhi device se continuity milti hai. Keemat: vendor ki custody + format mein dependency. 3 aadatein: sessions ko work-product naam do, ek session = ek workstream, dead cheezein prune karo.
- **Concept 5 — 3 File Tiers (course ka sab se zaroori concept):** Tier 1 (Task filesystem — temporary, kaam khatam pe cleanup), Tier 2 (Platform storage — permanently account mein, lekin vendor custody), Tier 3 (The Exit — file platform se nikal kar aapke control mein, jaise Drive/email/repo commit). **Yaad rakhne wali line: "Finished work exits the platform. Everything else may stay."** Har brief ke end mein file+tier listing line add karo.
- **Concept 6 — Connectors Web Pe:** double weight — reach bhi hain, Tier-3 exit door bhi. Read scope send scope nahi hai. Untrusted content (prompt injection) ke liye ask-before-acting mode.
- **Concept 7 — The Gate In Your Pocket:** human gate wahi rehta hai, sirf location badalti hai — approval phone pe aati hai. Phone gate hai, workbench nahi. Aadat: gate ko jaan-boojh kar ek dafa bajao, confirm karo notification phone tak pohanchi.

## 02 — Working Unwatched: Delegation Loop + Scheduled Tasks

- **Concept 8 — Delegation Loop (4 steps):** Brief (colleague-style, outcome+constraints+audience+wajah), Plan ("lay out your plan first, pause for approval" — yeh aapka akela intercept hai), Approve/redirect (4 checks: scope, order, reach, assumptions — ek sentence se redirect karo), Review (clarifying questions, contradiction-flagging, file+tier listing). Anti-pattern: is surface ko "superpowers wala chat box" treat karna — vague brief mein khali jagah agent khud decide karta hai.
- **Concept 9 — Scheduled Tasks:** ek assignment jo ek dafa describe karo, phir vendor ke servers apne clock pe chalate hain. 4 jawab order mein: kya karna hai (khaali-hafta case samet), kya touch kar sakta hai, kya reach kar sakta hai (connectors = permissions), kab shuru hota hai (cadence approximate hai). 3 rules: pehle haath se trust build karo, metered math likh kar karo, complete run ≠ successful task (success signal task ke apne output mein banao). Boundary: **reporting** schedules abhi safe hain, **acting** schedules (jo bhejti/file karti/decide karti hain) Loop Engineering course maangti hain.

## 03 — Choosing, Aur Open Path

- **Concept 10:** jo kaam touch kare uske hisaab se surface chuno — connector/document kaam + continuity → Web; local files/desktop apps → Desktop; code/repos → Coding agents; regulated data → koi nahi, pehle compliance. Rule: jaano har deliverable kaunse tier mein utri — Tier 3 mein deliverable ko farq nahi parta kaunse surface ne banaya.
- **Concept 11 — Open Path:** 2 open paths bina vendor cloud ke: **OpenWork** (self-hosted worker, aap infrastructure control karte ho) aur **OpenCode** (repo-attached, apna scheduler — cron/GitHub Actions). Trade: companies spine bech dete hain, open path banana parta hai — badle mein custody aur choice milti hai.
- **Concept 12 — Surface Kya Nahi Kar Sakti:** surface kaam behtar nahi banati, weak brief ko unattended banati hai. Har quality lever aapki taraf hai (brief, plan review, tier decision, gate test, walk-before-schedule). Surface mechanical facts sab se tezi purane hote hain — lasting layer: stop-typing test, window-not-runtime, 3 tiers, 6-part lens, 4-step loop, schedule ke 4 jawab.
- Aage jaana: Cowork &amp; OpenWork, Agentic Coding, Spec-Driven Development, Loop Engineering, Harness Engineering + Trusting the Checker, Leaving the Laptop.

## 04 — Practice Projects (6 Hands-On)

1. **The Closed-Lid Test** (Easy, 15 min) — multi-step session shuru karo, tab band karo, phone se dobara kholo — runtime kahan hai samjho.
2. **The Three-Tier Audit** (Easy, 30 min) — real task, full brief, har file ka tier batao, deliverable Tier 3 mein hona chahiye.
3. **Ring the Gate on Purpose** (Easy-Medium, 20 min) — safe low-stakes task jo approval mange, poori tarah computer se chale jao, phone confirmation verify karo.
4. **The First Reporting Schedule** (Medium, 30 min + 1 hafta) — Monday-morning brief, 4 jawab likho, 2 dafa unattended fire honi chahiye success signal ke sath.
5. **One Task, Two Vendors** (Medium, 45 min) — wahi assignment Cowork aur ChatGPT Work dono mein, comparison table verify karo.
6. **The Exit Drill (Capstone)** (45 min) — farz karo platform gayab ho gaya, sirf Tier 3 se working state reconstruct karo, jo reconstruct na ho sake uski list banao (= Tier-2 exposure).

Har project ka apna runnable scaffold [`projects/`](projects/README.md) mein hai (Setup + Steps + Done-jab checklist).

## 05 — Test Your Understanding

10 scenario-based questions, sab 12 concepts grounded — [`05-test-your-understanding.md`](05-test-your-understanding.md) (scenario version) aur [`quiz.md`](quiz.md) (same content, standalone).
