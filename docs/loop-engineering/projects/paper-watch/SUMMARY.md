# Summary — Bonus: Paper Watch

**Concept:** 12 — The Spine (Memory Between Runs)
**Source:** 100% official (`panaversity/agentfactory-labs`)

## Kya Sikhata Hai

**"No spine, no loop"** — model har run ke baad sab bhool jata hai; disk par ek file yaad rakhti hai.

## Kyun Zaroori Hai

Yeh sabse "invisible" lekin sabse zaroori concept hai. Bina spine ke, har run bilkul waisi hi hoti hai
jaisi pehli thi — loop nahi, sirf ek hi step ka baar-baar repeat. Yeh project spine ko **ankhon ke
saamne** dikhati hai, na ke sirf explain karti hai.

## Kaise Kaam Karta Hai

`show me what's new on arXiv about "LLM agents"` poochte ho — naye papers ate hain, newest first. **Ab
wahi sawal dobara poocho:** is baar jawab "nothing new since last run ✓" hota hai. Loop ne **yaad
rakha** — har paper `progress.md` (spine) mein likha, aur wapis parha.

**Asal proof:** `rm progress.md` chalao aur dobara poocho — har paper phir se "naya" nazar ayega. Ek
command mein "no spine, no loop" prove ho jata hai.

**Sky Watch (Project 3) se farq:** dono daily Routines hain, lekin Sky Watch ko **koi memory nahi
chahiye** (roz "aaj" reprint karti hai), Paper Watch **spine ke bina kaam hi nahi kar sakti** (sirf
"naya" dikhana hai). Same heartbeat, opposite memory need — yehi contrast batata hai spine **kab**
chahiye.

## Maine Kya Test Kiya

`paperwatch.py --topic "loop engineering agents"` 2 baar chalaya: pehli run ne 1 real paper dikhaya
(*"LOGOS: A Living Logic for AI Agent Teams..."*), doosri run ne turant "nothing new since last run ✓"
bola. Spine confirmed working. Test ke baad `progress.md` clean kar diya (fresh state ke liye).

---
[⬆ Poori Project List](../../README.md#runnable-projects-poore-12-har-ek-ki-real-jagah)
