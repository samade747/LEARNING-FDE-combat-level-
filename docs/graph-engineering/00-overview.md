# 00 — Overview: Memory Problem

## Ek Loop Se Bohat Loops Tak

Aapki loop kaam karti hai. Har subah 9am pe fire hoti hai, harness usay fence karti hai, aur uski spine
(`progress.md`) kal ka seekha hua aaj mein le ati hai. **Ek loop, ek memory file.** Itna kaafi tha.

Ab dekho jab aap **kamyab** ho jate ho: aap doosri loop add karte ho. Phir ek review loop. Phir, ek
busy hafte, aap **20 agents** ko 20 files audit karne ke liye chhor dete ho. Har agent **khaali context
window** se start hota hai. Har ek wahi cheez dobara dhoondta hai jo koi aur agent ek ghanta pehle dhoond
chuka. Har ek apni findings ek transcript mein likhta hai jo koi aur agent kabhi parhega hi nahi. **Kaam
multiply hua. Memory nahi hui.** Aap ne ek team bana li jiska koi **shared brain** nahi.

**Graph engineering** yehi problem solve karti hai. Idea ek jumle mein: **agent bhool jata hai, graph
nahi bholti.** Agents jo seekhein, wo transcripts mein chhorne ki bajaye, **typed, connected records**
(nodes + edges) ki tarah likhte hain, jo koi bhi baad wala agent **query** kar sake.

## 2 Graphs, Alag Alag Kaam

| | **Commit DAG** | **Knowledge Graph** |
| --- | --- | --- |
| Yaad rakhta hai | **Kaam** — kya try hua | **Facts** — kya pata hai |
| Nodes | Commits, experiments, runs | Entities, claims, sources |
| Edges | `parent_of`, `derived_from` | `supports`, `works_for`, `about` |
| Jawab deta hai | Kya badla? Kaunsi lineages abhi zinda hain? | Kaunsi entities exist karti hain? Kaunsa source claim ko back karta hai? |
| Aap ke paas pehle se hai | Git history, partially | Kuch nahi — Part 3 isay banati hai |

**Alag rakhna zaroori kyun hai?** Kyunke inke truth rules alag hain. Ek **commit fact hai construction
se** — wo ho chuka, Git guarantee karta hai. Knowledge graph mein ek **claim evidence wali statement**
hai — galat ho sakti hai, mis-extract ho sakti hai, ya supersede ho sakti hai. Dono ko mila do to ya to
guesses ko history samajh loge, ya history ko guesses ke neeche dafan kar doge.

Dono **connect** hote hain:
```
(agent_run_183) —produced→   (claim_441)
(agent_run_183) —modified→   (commit_a81f)
(claim_441)     —about→      (entity_vendor_x)
(claim_441)     —supported_by→ (source_contract_pdf)
(claim_441)     —supersedes→ (claim_238)
```
Ek run ne kaam kiya (commit) aur kuch seekha (claim). Claim ek entity ke baare mein hai, ek source se
backed hai, aur ek purani claim ki jagah leti hai. **Kaam left mein, knowledge right mein, connected
lekin kabhi merged nahi.**

## Graph Kya Hai — Nodes, Edges, Direction

Ek **graph** points (**nodes**) ka set hai jo arrows (**edges**) se connected hain. 3 properties sab kaam
karti hain:

1. **Nodes typed hain** — "ek box" nahi, balke "Entity", "Claim", "Source", "Commit"
2. **Edges labeled aur directed hain** — `(claim_441) —supported_by→ (source_readme)` reverse arrow se
   alag matlab rakhta hai. **Direction hi matlab hai.**
3. **Paths jawab hain** — *"Kya Vendor X, Incident Y se connected hai?"* ban jata hai *"kya supported
   edges ka ek path Vendor X se Incident Y tak exist karta hai?"*

**DAG** (directed acyclic graph) — arrows kabhi wapas circle nahi karte. **Git history** ek DAG hai — har
commit apne parent ki taraf point karta hai.

> **Simple:** Nodes nouns hain. Edges directed verbs hain. Graph "sentences" ka set hai (subject, verb,
> object), tasveer ki tarah, taake computer prose samjhe bina arrows ki chain follow kar sake.

## Kya Aapko Waqai Graph Chahiye?

Zyada tar systems ko knowledge graph nahi banani chahiye. **Chhota test:** agar aapke tasks independent
hain, jawabat ek document se ate hain, relations fixed aur simple hain, ek relational table sab kuch
answer kar deta hai, aur kisi ko provenance nahi chahiye — **yahin ruk jao**. Ek loop + spine sahi jawab
hai.

**Balance tab tilt hoti hai** jab do loops facts exchange karein, ya 20 workers ko ek synthesis chahiye,
ya relations badalte rehte hon, ya koi ek din puchay *"humein ye kaise pata?"*.

### Self-Check
**Sawal:** Aapki triage loop aur changelog loop dono ko pata hona chahiye is hafte konsi PRs ship hui.
Abhi har ek `git log` chala kar dobara derive karti hai. Kya waste ho raha hai?
**Jawab:** Kaam har context window mein dobara ho raha hai aur dobara interpret ho raha hai. Fix: jo loop
pehli dafa "PR #212 shipped, fixes issue #98" establish kare, wo isay **ek dafa** typed record (commit
hash ke sath) likhe. Dono loops record parhein. **Derive once, query many times.**

---
[⬅ Index](README.md) · [Agla: DAG of Work ➡](01-dag-of-work.md)
