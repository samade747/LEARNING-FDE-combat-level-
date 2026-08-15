# 00 — Overview: Loop Engineering Kya Hai

## Purana Tareeqa vs Naya Tareeqa

Ab tak coding agent (Claude Code / OpenCode) use karne ka tareeqa simple tha:

1. Aap ek instruction dete
2. Agent files padhta, change karta
3. Aap result check karte
4. Phir agli instruction dete

Har step pe **aap** control mein thay — aap heartbeat (kab chalega), checker (theek hai ya nahi), aur
memory (kya hua tha) — teeno khud thay.

**Loop engineering** is se agla level hai. Ab aap ek chhota sa **system** banate hain:

- Har subah khud shuru hota hai
- Dekhta hai raat mein kya change hua
- Decide karta hai kya karna hai
- Har kaam ek agent ko deta hai
- Result check karwata hai
- Sirf un decisions ke liye aapko bulata hai jo waqai insaan ko chahiye

Aap ye system **ek dafa** banate hain. Uske baad wo khud chalta rehta hai.

| Prompting (jo aap jaante hain) | Looping (jo naya seekhna hai) |
| --- | --- |
| Aap har turn start karte hain | Schedule ya event har turn start karta hai |
| Aap output parh kar decide karte hain | Ek checker output check karta hai, loop decide karta hai |
| Jab aap type karna band karo, kaam ruk jata hai | Aap sote waqt bhi chalta rehta hai |
| Ek task, ek session, poori tawajjo | Kai chhote runs, zyadatar unattended, tawajjo sirf gate pe |

## Value Kahan Gayi?

Loop khud ke steps handle karta hai, lekin **do cheezein** hamesha insaan ki rahengi:

1. **Intent** — Itni saaf tarah batana ke aapko kya chahiye, ke result **check** kiya ja sake.
2. **Accountability** — Jo bhi ship hota hai, uski zimmedari lena.

Loop beech ke steps sambhalta hai. Do sirey (start aur end) hamesha aapke hain.

## Do Loop, Ek Naam (Optional Detail)

"Loop engineering" ka lafz do alag cheezon ke liye use hota hai:

- **Chhota loop (inner loop):** Ye har agent ke andar hoti hai — model ko context bhejo, model tool
  mangta hai, tool chalao, result wapas do, repeat karo, jab tak model khud na kahe "main done hoon".
  **Masla:** yahan sirf model khud decide karta hai ke kaam mukammal hai — koi bahar se check nahi.

  ```python
  while True:
      reply = model(context)
      if not reply.tool_calls:
          break   # model ne khud decide kiya ke kaam khatam
      context += run_tools(reply.tool_calls)
  ```

- **Bara loop (outer loop) — yehi course sikhata hai:** Ye "manager" hai. Ye decide karta hai kaam
  konsa dena hai, kab start karna hai, kaise grade karna hai, aur kal ke liye kya yaad rakhna hai.
  Chhote loop ka ek poora chakkar bara loop ka sirf **ek "beat"** hota hai.

**4 layers jo waqt ke saath ubhre (har ek tak 1 saal lagta raha):**

1. Prompt engineering — jo lafz aap bhejte hain
2. Context engineering — model jo dekhta hai ek turn mein
3. Harness engineering — model ke ird gird ka code (yahan chhota loop rehta hai)
4. **Loop engineering (ye course)** — bara cycle: system kis pe kaam karta hai, kab start hota hai,
   kaise pata chalta hai ke khatam ho gaya

Har layer alag tarah ki ghalti rokta hai. Achi context kamzor prompt ko bacha sakti hai, lekin koi bhi
prompt missing context, missing checker, ya "schedule jo abhi bhi aap hi hain" ko theek nahi kar sakta.

> **Zaroori baat:** Loop khud chalne wala loop khud galtiyan bhi khud kar sakta hai. Ye prompting se
> **asaan nahi, mushkil hai**. Faida ye hai ke ek achi loop bana lo, wahi kaam baar baar khud karta
> rahega — jo warna har dafa haath se karna parta.

## Loop Ke 6 Parts (Anatomy)

Har real (khud chalne wala) loop mein **5 working parts + 1 memory layer** hoti hai:

1. **Heartbeat** — Schedule ya event jo loop start karta hai. Iske bagair ek run hai, loop nahi. Har
   ek dafa loop chalna "**beat**" kehlata hai.
2. **Worktree** — Alag working folder, taake do agents ek dusre ki file overwrite na karein.
3. **Skill** — Project ki knowledge ek dafa likhi hui, taake har run zero se shuru na ho.
4. **Subagents (Maker-Checker)** — Jo agent likhta hai, wo apna kaam khud approve nahi karta — doosra
   agent grade karta hai.
5. **Connector (MCP)** — Loop ko real tools tak reach: PR khol sakta hai, ticket update kar sakta hai —
   sirf suggest nahi karta, **act** karta hai.
6. **Spine (State/Memory)** — Disk pe file (`progress.md`, `CLAUDE.md`/`AGENTS.md`) jo record karti hai
   kya ho chuka aur aage kya karna hai. Model runs ke darmiyan sab bhool jata hai. Spine yaad rakhta hai.
   **No spine, no loop.** Iske bagair loop apna pehla step hamesha repeat karega.

## Code Sirf Nahi — Kisi Bhi Repo Pe Chalta Hai

Ye idea sirf code ke liye nahi. Ek kitaab, report, course, newsletter — sab ek repo ban sakte hain
(markdown files ka), aur loop ke sab parts wahan bhi kaam karte hain. Sirf ek cheez badalti hai: **checker**.
Code ke paas tests/linters hote hain (proof). Prose ke paas mechanical checks (broken links, missing
figures) + ek reviewer agent hota hai jo rubric se grade karta hai (claim, proof nahi).

## Do Rastay: Built-in Tools vs Khud Connect Karna

- **Claude Code:** Loop ke parts product ke andar hi mojood hain — `/loop`, `/goal`, `/schedule`,
  Routines, `--worktree`, `.claude/agents`, Channels, hooks. Cloud Routines laptop band hone pe bhi
  chalti hain, lekin daily run limit hoti hai.
- **OpenCode:** Aapko "worker" milta hai (`opencode run`), lekin scheduler/trigger khud lagana parta
  hai — cron, launchd, Task Scheduler, ya GitHub Actions. Zyada setup, zyada control, koi vendor cloud
  zaroori nahi.

Dono ka **shape same hai** — sirf commands alag hain. Ye shape hi asal skill hai, jo transfer hoti hai.

---
[⬅ Index](README.md) · [Agla: Heartbeats ➡](01-heartbeats.md)
