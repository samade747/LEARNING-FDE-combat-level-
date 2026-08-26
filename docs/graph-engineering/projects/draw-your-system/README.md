# Graph Project 1 — Draw Your System

**Concept:** 2, 3, 11 (nodes and edges, two graphs, the wiring) · **Time:** 10-15 min · **Difficulty:** Easy

Koi code nahi — sirf ek diagram. Maqsad: apna asal setup (jo loops/checkers/gates aap abhi chalate ho)
typed nodes + labeled directed edges ki tarah dekhna, taake pata chale kahan koi finding sirf transcript
mein exist karti hai, aur kaunsi optimizing loop ka koi watcher nahi.

## Files

- `system-template.mmd` — Mermaid starter graph (blank shape, apne nodes se replace karo)
- `worked-example.mmd` — ek filled-in misaal (morning-triage + review loop) taake pattern samajh aaye

## Setup

Koi install nahi chahiye. Mermaid preview ke liye: VS Code ka "Markdown Preview Mermaid Support"
extension, ya [mermaid.live](https://mermaid.live) mein paste karo. Kagaz par bhi chal sakta hai.

## Steps

1. `worked-example.mmd` khol kar dekho — kaise loops, checkers, human gates, anchors, aur memory files
   sab **typed nodes** ban gaye hain, aur edges **labeled + directed** hain.
2. `system-template.mmd` copy karo, apna naam do (`my-system.mmd`), aur apna **asal** setup draw karo —
   jo bhi loops/agents abhi aap chalate ho (agar sirf yeh course kar rahe ho, apne imagined ya kisi
   practice-project ka setup use karo).
3. Har node ko type do: `Loop`, `Checker`, `HumanGate`, `Anchor`, `MemoryFile`, `Agent`.
4. Do cheezein circle karo (Mermaid mein `style` ya bas comment se mark karo):
   - Koi **finding jo sirf transcript mein exist karti hai** (kisi progress.md/memory file mein nahi)
   - Koi **optimizing loop jiska koi watcher/counter-metric na ho**

## Done Jab (Self-Check)

- [ ] Diagram mein kam se kam 5 typed nodes hain (mix of Loop/Checker/HumanGate/Anchor/MemoryFile)
- [ ] Har edge labeled hai (`produced`, `checks`, `feeds`, `triggers` — jo bhi sahi ho)
- [ ] Aap ek circled "transcript-only finding" point kar sakte ho aur bata sakte ho iski cost kya hai
      (agla agent isay dobara dhoondega)
- [ ] Aap ek circled "unwatched optimizing loop" point kar sakte ho aur bata sakte ho ye kaise game ho
      sakti hai (Perez ke 4 failures, Part 5 se)

---
[⬆ Practice Projects Index](../../08-practice-projects.md)
