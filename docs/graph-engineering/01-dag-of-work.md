# 01 — DAG of Work: Karpathy Ka Rasta

## Concept 4: Autoresearch — Ratchet Apni History Git Mein Likhta Hai

Loop course ne aapko **ratchet** sikhaya: ek change try karo, evaluate karo, sirf tab rakho jab number
behtar ho, warna revert karo. Karpathy ka **autoresearch** (7 March 2026) bilkul wahi loop hai, ML
training pe lagi hui, aur is course ke liye iski ehmiyat ek design choice mein hai: **loop ki memory
transcript nahi hai. Ye commit DAG hai.**

**Setup — 3 files:**
1. `prepare.py` — fixed data prep, agent isay **touch nahi kar sakta** (ek "frozen node")
2. `train.py` — model, optimizer, training loop — agent ka **ek** editable surface
3. `program.md` — plain-language instructions: metric, budget, commit/revert rules

**Beat, hamesha:** `train.py` + recent history parho, **ek** motivated change propose karo, commit karo,
~5 minute train karo, validation loss measure karo. **Behtar?** Commit rehta hai. **Bura ya crash?**
Last retained commit pe reset. Dono soorat mein, **result record karo aur chalte raho** — koi insaan
beech mein nahi.

**Yahan pe 2 memories hain, ek nahi:**

| | Kya rakhta hai | Truth standard |
| --- | --- | --- |
| **Git branch** | Sirf **retained** improvements, rising chain of commits | Verified — har commit ne metric ko beat kiya |
| **`results.tsv`** | **Har** attempt: commit hash, metric, kept/discarded/crashed | Complete — attempts record hote hain, achievements nahi |

**Zaroori detail:** failure pe kya hota hai. Agar metric behtar ho, branch aage barhta hai. Agar wahi
ya bura ho, `git reset` se wahin wapas jaate hain jahan se shuru kiya. **Reset commit ko side branch pe
park nahi karta — remove kar deta hai.** Discarded experiment sirf `results.tsv` mein bachta hai — jo
**deliberately Git se untracked** hai.

> Ye design hai, mistake nahi. **Git** wo kaam rakhta hai jiski value **prove** ho chuki. **TSV** har
> attempt ka honest record rakhta hai, crashes samet. Jo ye **nahi** karta: alternative lineages ko
> zinda aur traversable nahi rakhta — discarded idea ek text row ban jati hai jo koi doosra agent query
> nahi kar sakta. Yehi gap Concept 5 bharta hai.

**4 conditions jo isay kaam karwati hain** (loop course ka checklist): output **verifiable** hai
(validation number), action **reversible** hai (git reset), horizon **short** hai (5-minute runs),
environment **bounded** hai (ek repo, ek editable file).

## Concept 5: AgentHub — Search Graph Traverse Karo, `main` Pe Merge Mat Karo

3 din baad, Karpathy ne agla step post kiya: loop ko **"asynchronously massively collaborative"** hona
chahiye — SETI@home jaisa. **AgentHub** iska sketch hai: ek Go binary, ek SQLite database, ek bare Git
repo, ek message board. Slogan: **"GitHub is for humans. AgentHub is for agents."**

**Concept 4 ka gap:** ek akeli ratchet apni failures **reset** kar deti hai — discarded idea ka sirf ek
row bachta hai jo koi query nahi kar sakta. AgentHub ka central move: reset karna band karo, **rakhna**
shuru karo. Agents commits bundles ki tarah push karte hain, har pushed commit **durable node** ban jata
hai, aur `main` pe converge hona zaroori nahi. **Alternatives zinda aur traversable rehte hain.**

**Swarms kyun different plumbing chahte hain:**
- **Hazaron ek saath explore karte hain** — human repos handful of branches assume karte hain
- **Zyada tar results kabhi merge nahi hote — jaan-boojh kar** — failed experiment **evidence** hai
- **Primary operation badal jata hai** — "isay main mein merge karo" nahi, balke **"search graph
  traverse karo"**

```bash
ah push                 # apna commit naye node ki tarah publish karo
ah children <hash>      # is result ke upar kya try hua?
ah leaves                # frontier: jo results kisi ne abhi build nahi kiye
ah lineage <hash>        # poori ancestry path jisne ye outcome banaya
ah diff <a> <b>          # kisi bhi do experiments ko compare karo
ah log --agent X         # ek agent ka poora trail
```

**Message board** social layer hai. Agent ko har pichli transcript nahi chahiye — relevant lineages
query karta hai, summaries parhta hai, ek commit fetch karta hai, aage barhta hai. Isay **"graph-grounded
context construction"** kehte hain — poori history replay karne ki bajaye connected state retrieve karo.

> **Honesty note:** AgentHub ab **public nahi hai** — release ke turant baad private ho gaya. Preserved
> forks milte hain lekin koi license file nahi thi. Isay dependency ki tarah use mat karo — sirf design
> se seekho: **commits as nodes, bundles as push unit, traversal as primary operation.**

### Dynamic Workflows (Bonus)

Anthropic ka **Dynamic Workflows** (28 May 2026) is idea ka production example hai: aap fan-out script
nahi likhte, Claude khud current task ke liye orchestration program likhta hai — files glob karo, per-file
auditor spawn karo, findings filter karo, reviewers spawn karo, phir ek synthesizer cited report banaye.
**Limits:** up to 16 concurrent agents, 1,000 agents total per run (docs check karo, badalte rehte hain).

### Self-Check
**Sawal:** AgentHub mein agent A ka experiment fail hota hai (bara batch size memory limit pe crash).
GitHub thinking mein branch abandon ho jati. Graph thinking mein kya hota hai?
**Jawab:** Failed commit DAG mein node ki tarah rehta hai, aur message board pe post uski lineage cite
karti hai: "batch 64 is hardware pe memory exceed karta hai. Depth change se branch karo." Har future
agent jo us lineage pe `children` query kare, crash dobara chalaye bina warning inherit kar leta hai.
**Failure shared memory ban gayi.** Yehi swarm aur crowd ka poora farq hai.

---
[⬅ Overview](00-overview.md) · [Agla: Graph of Facts ➡](02-graph-of-facts.md)
