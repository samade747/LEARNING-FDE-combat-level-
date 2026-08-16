# 01 — Part 1: The Deployment Problem (Concepts 1-3)

## Concept 1 — "Works On My Machine" Deployment Nahi Hai

Agent laptop par "kaam karta hai" ka matlab specific hai: aap ne khud start kiya Python process, API
keys project folder ki file se parhta hai, state local file mein likhta hai, code apne hi process mein
import karke chalata hai. Model internet par call hota hai, baaki sab aapki machine par.

**Production in sab assumptions ko tortha hai:**
- Real users public internet se agent tak pahunchte hain, sirf aap laptop se nahi
- Kai users ek sath hit karte hain — ek Python script ek waqt mein ek handle karti hai
- Agent ki state host restart survive kare — temp folder ki local file nahi karti
- Agent ka generated code kahin chale jahan aapke data ko nuksan na pahunchaye — apne process mein,
  database credentials ke pas chalana serious security mistake hai
- Agent ke secrets agent ke generate kiye code ki pahunch se bahar hon — working directory ki key
  file nahi hoti
- Har run observable, auditable, aur recoverable ho — crash hone wala process in mein se koi nahi

Un 6 properties mein se kitni ek laptop script mein minor changes se, ek-do din ke kaam se add ho
sakti hain? Honest jawab hai: ek ya zero. **Production deployment "works on my laptop" ka thin wrapper
nahi hai. Yeh ek alag architecture hai.**

Temptation yeh hoti hai script ko server par chala dena. 2 mahine baad team ke paas hota hai: ek server
jo kabhi-kabhi crash hota hai, ek agent jo kabhi-kabhi user-influenced code production database ki
poori access ke sath chalata hai, state jo har reboot par gayab ho jati hai, aur agent ne kya kiya iska
koi record nahi.

## Concept 2 — Harness/Sandbox Split: Control Plane Vs Execution Plane

Course ka sabse important idea: **harness** (control plane) aur **sandbox** (execution plane) ka split.

**Harness agent ka dimaagh hai.** Users se network par requests receive karta hai. Agent loop chalata
hai: model call karna, agla tool decide karna, specialist agents ko handoffs, guardrails apply karna.
Durable state rakhta hai: conversation history, run history, audit log. Secrets rakhta hai: model key,
database credentials, storage credentials. Users ko results wapis deta hai.

**Sandbox agent ke haath hain.** Harness se workspace description (Manifest) receive karta hai. Us
description se match karta isolated workspace provision karta hai. Shell commands, file reads/writes,
code chalata hai jaisa agent request kare. Results harness ko wapis deta hai. **Harness ke secrets,
database, ya production systems tak access nahi rakhta** (siwaye jo Manifest explicitly mount kare).

**Boundary network aur security boundary hai.** Harness apne secrets sandbox ke sath share nahi karta.

**4 wajah yeh split matter karta hai:**
1. **Security** — agent-generated code galat ho sakta hai, subtly incorrect, ya adversarial setting
   mein malicious. Isay database credentials wale process mein nahi chalana chahiye. Split network/OS
   boundary daalta hai generated code aur harness ke secrets ke darmiyan
2. **Durability** — sandboxes create aur destroy hote rehte hain. Harness ko sandbox ki death survive
   karni hai. Agar harness sandbox ke andar rehta, sandbox ki death sab kuch le jati
3. **Scalability** — ek harness kai sandboxes coordinate karta hai — harness ki needs modest hain,
   sandbox ki spiky. Alag-alag scale hote hain
4. **Observability** — harness record own karta hai (agent ne kya decide kiya, konse tools call kiye,
   trace). Jab kuch galat ho, harness ka record hi parha jata hai

**2 anti-patterns jo yeh course avoid karta hai:**
1. **Harness ko sandbox ke andar chalana** — prototype ke liye convenient, production ke liye galat
2. **Agent-generated code ko harness ke andar chalana** — AI deployment ka "original sin." Harness
   database credentials, model key, aur users ka data rakhta hai. Eventually galat ho jata hai, aur
   jab hota hai, damage unbounded hoti hai

## Concept 3 — SDK Ko Cloud Infrastructure Se Kya Chahiye: 5 Surfaces

Harness/sandbox pattern ko realize karne ke liye SDK ko cloud infrastructure se kya chahiye? **5
surfaces**, 5-component stack ek-ek surface map karta hai:

1. **Long-running HTTP service (harness host karne ke liye)** — **FastAPI on Azure Container Apps**
2. **Durable state across runs** — **Neon Postgres**
3. **File aur artifact storage jo dono planes reach kar sakein** — **Cloudflare R2**
4. **Isolated execution agent-generated code ke liye** — **code-execution sandbox**
5. **Orchestration jo Surfaces 1-4 ko jorti hai** — **SDK khud**

**Poora composition:** Request FastAPI par arrive hoti hai (Azure Container Apps par). Harness Neon se
agent aur prior state load karta hai. Manifest compose karta hai. Sandbox provider se workspace
provision karwata hai. SDK agent loop chalata hai, tool calls sandbox tak bhejta hai, trace record
karta hai. Artifacts R2 mein jate hain; trace Neon mein. Result user ko wapis. **Yehi poora course hai
— har concept aur decision is composition ke ek hisse ki elaboration hai.**

> **Python nahi use kar rahe?** Harness aur sandbox features April 2026 tak Python-only hain.
> TypeScript app ho to Python harness alag service ki tarah chalao, apni app se HTTP par call karo.

---
[⬅ Overview](00-overview-and-stack-primer.md) · [⬆ Index](README.md) · [Agla: Five-Component Stack ➡](02-five-component-stack.md)
