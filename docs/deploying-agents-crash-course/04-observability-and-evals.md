# 04 — Part 4: Observability Aur Evals As Architectural Surfaces (Concepts 11-12)

## Concept 11 — Observability As Architectural Surface

**Observability:** woh tools jo bataye running harness kya kar raha hai, kuch tootne par, aur cause
dhoondne mein madad karein. **Zyada tar production AI failures observability failures hain** — agent
kuch galat karta hai, kisi ko din tak pata nahi chalta, delay ki cost barhti jati hai. Isliye
observability ek feature nahi jo aakhir mein bolt-on ho — yeh ek aur architectural surface hai, shuru
se plan ki gayi.

**4 surfaces jo harness ko ek sath dekhte hain, har ek apna sawal:**

| Surface | Kya Sawal Own Karta Hai |
| --- | --- |
| **Application Insights** | Harness ki infrastructure healthy hai? |
| **OpenTelemetry traces** | Ek request services ke across kaise flow hui? |
| **OpenAI Agents SDK traces** | Is run ke doran agent ne kya kiya? |
| **Phoenix** | Agent ka behavior waqt ke sath kaise badal raha hai? |

**Application Insights** Azure ka built-in monitor hai — container view: request rate, error rate,
latency, CPU/memory, restart counts, log streams. Replica crash ho to pehle yeh notice karta hai. Agent
ka behavior nahi dekh sakta — "POST /runs returned 200 in 12 seconds" ke ilawa kuch nahi janta.

**OpenTelemetry (OTel)** ek request ko services ke across trace karne ka open standard hai. Ek trace
ek poore run ka complete record hai. Agent ki reasoning tool calls ke darmiyan nahi dekh sakta — sirf
yeh record karta hai model call hua, kyun nahi.

**OpenAI Agents SDK** apna trace emit karta hai: kaunse model decisions hue, kaunse tools kis
arguments ke sath call hue, handoffs kahan gaye — agent-behavior view own karta hai. Execution ke bahar
kuch nahi dekh sakta.

**Phoenix** waqt ke sath agent traces dekhta hai aur bure traces ko future tests mein badalta hai —
trend view own karta hai: sirf agent ne kya kiya nahi, kaunse runs kal ke regression tests bannay
chahiye. Transient infrastructure outages nahi dekh sakta.

**Yeh surfaces overlap karte hain, replace nahi.** Ek shared `run_id` se interconnect hote hain, isliye
team kisi bhi surface se shuru karke doosre tak ek click mein ja sakti hai. Application Insights alert
→ OTel trace (kaunsa span slow tha) → SDK trace (agent kya kar raha tha) → Phoenix (pattern recur ho
raha hai?). Ek surface skip karo, ek step kho dete ho.

> **5wan surface** sirf tab ata hai jab runs ko durable-execution layer mein wrap karo — [Nervous
> System course](../ai-agent-nervous-system-crash-course/README.md) ka territory hai, is course ka
> nahi.

## Concept 12 — Evals As Architectural Surface

**Eval:** ek test jo agent ka behavior measure kare (jawab sahi tha, tool sahi tha, reasoning sound
thi), sirf yeh nahi ke code chala. [Eval-Driven Development course](../eval-driven-development-crash-course/README.md)
ne 4 eval frameworks banaye — yeh concept batata hai woh deployed harness se kahan attach hote hain.
**Attachment hi poora point hai — uske bina eval suite sirf theory hai.**

**Boundary ek jagah hai: traces.** Eval suite jo bhi grade karti hai, ek trace se parhti hai, aur
traces 2 stores mein rehte hain. **Neon** durable record rakhta hai, scheduled jobs aur audit se query
hota hai. **Phoenix** real-time sample rakhta hai, live dashboard par dikhta hai. **Yaad rakhne wali ek
cheez: integration traces ke through mediated hai, aur traces Neon aur Phoenix mein rehte hain.**

Jab ek run khatam hoti hai, harness trace ko Neon mein synchronously likhta hai (durable record) aur
ek sample Phoenix ko asynchronously stream karta hai (live view). Wahan se eval frameworks specific
points par attach hote hain: **CI gate** har pull request par chalti hai, **scheduled jobs** pichle din
ki traces nightly grade karti hain, **Phoenix ke inline checks** traces arrive hote hi chalte hain.

**Isay ab plan karna zaroori hai, baad mein nahi:** observability wire hone se pehle produce hui traces
gayab ho jati hain, aur eval suite sirf un traces se grow hoti hai jo usne dekhi hon.

---
[⬅ The Execution Plane](03-execution-plane.md) · [⬆ Index](README.md)

*(Baqi parts — Lab, Honest Frontiers, Closing — is course ke content ko cover karte rahenge.)*
