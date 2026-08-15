# 03 — Graph Se Kaam Lena: Subgraph + Grounded Checker

## Concept 9: Subgraph, Poori Graph Nahi — Context Construction

Aap ne context-dumping se bachne ke liye graph banayi. Isay barbaad karne ka sab se tez tareeqa: **poori
graph ko har prompt mein serialize kar dena.** 50,000 edges wali graph context window mein utni hi
bekaar hai jitni 50 transcripts. **Discipline hai: bounded retrieval** — har worker ko sirf **task-
specific subgraph** milta hai, aur kuch nahi.

**7 steps:**
1. **Resolve** — task jin entities ka zikr kare, unhe graph mein resolve karo
2. **Expand** — un nodes se 1-2 hops, sirf allowed edge types pe
3. **Include** — current artifact versions jo task touch kare
4. **Prioritize** — recent, verified claims ko stale/low-confidence pe tarjeeh do
5. **Conflicts shamil karo** — agar 2 claims contradict karein, worker ko dono dikhao
6. **Token budget mein serialize karo** — plain triples ki tarah
7. **Stable edge identifiers attach karo** — taake worker `edge_1042` cite kar sake

> **Zaroori:** Ek orchestrator jo 20 workers coordinate karta hai, ab apni window mein 20 outputs copy
> nahi karta. Workers **typed graph updates publish** karte hain. Ek synthesizer graph traverse kar ke
> findings combine karta hai — **chahe kisi ek agent ne bhi saare source documents na dekhe hon.**
> **Orchestrator ki context clean rehti hai.** Yehi property hai jo multi-agent systems ko graph ke sath
> **scale** karati hai aur bagair graph ke **suffocate** karati hai.

> **Simple:** Naye employee ko poori filing cabinet mat do. Wo 3 folders do jo unke task ko touch karte
> hain, aur sticky note "ye do folders disagree karte hain: check karo." Yehi subgraph hai — chhota,
> relevant, conflicts ke baare mein honest, citable.

## Concept 10: Grounded Checker — "Triple Not Found" > "Seems Off"

Yahan memory layer governance layer se milti hai. Loop course ne maker-checker split diya. Harness
course ne checker ko typed output diya. Lekin checker ka verdict phir bhi ek **impression** tha — model
kaam parh kar apna feeling schema ke sath report karta tha. **Graph badalti hai checker kya ho sakta
hai:** ye claims ko **edges** ke against check kar sakta hai.

Ek claim walk karo: maker ka report kehta hai *"Vendor X ne wo component supply kiya jo Incident Y mein
shamil tha."* Grounded checker nahi puchta *"ye sahi lagta hai?"* — ye graph se **2 mechanical sawal**
puchta hai: kya `(vendor_x, supplied, component_z)` edge exist karta hai? Kya
`(component_z, involved_in, incident_y)` exist karta hai? Agar koi missing ho:

```json
{
  "decision": "revise",
  "claim": "Vendor X supplied the component in Incident Y",
  "reason": "No supported path from vendor_x to incident_y",
  "required_evidence": [
    "A source-backed 'supplied' relation from vendor_x",
    "A source-backed 'involved_in' relation to incident_y"
  ]
}
```

**2 failure messages compare karo:** *"Seems off"* maker ko guess karne bhejta hai reviewer ko kya
naapasand tha. *"Triple not found: ye 2 edges chahiye"* maker ko exactly batata hai kya dhoondna hai ya
kaunsi claim withdraw karni hai. **Ek mood hai. Doosra work order hai.**

> Demand dono directions mein honest hai: kabhi kabhi maker source dhoondh leta hai aur **graph ko naya
> edge milta hai**. **Grounding memory improve karti hai, sirf report nahi.**

Yahi grounding har workflow pattern ko upgrade karti hai: Chain mein, graph ek stage-gate hai. Fan-out
mein, ye shared surface hai jahan workers overlap kiye bina publish karte hain. Orchestrator-workers
mein, ye shared memory hai jo orchestrator ki context clean rakhti hai. Evaluator-optimizer mein, ye har
verdict ke neeche ki evidence layer hai. **Ek graph, 5 patterns, same 3 roles hamesha: shared memory,
grounding layer, persistent world model.**

> **Zaroori honesty:** Grounded verdict sirf utna hi achha hai jitni 2 cheezein jo grounding test nahi
> karti — kya graph ke edges khud sahi hain (Concepts 7-8 risk kam karte hain, khatam nahi), aur kya
> checker reliably wo paths dhoondta hai jo waqai exist karte hain. *"Checker ne graph consult ki"*
> *"checker ki ek impression thi"* se behtar claim hai. **Lekin phir bhi ek claim hai**, model ki bani
> hui. Checker ki quality kaise measure karein — is ka poora discipline agli course hai: **Trusting the
> Checker**.

> **Simple:** Ungrounded reviewer ek critic hai: *"mujhe pasand nahi aya."* Grounded reviewer ek auditor
> hai: *"Line 4 payment claim karti hai. File mein koi receipt nahi. Receipt do ya line hatao."* Critic
> se aap hamesha bahas kar sakte ho. Auditor ki demand ya poori hoti hai ya nahi.

### Self-Check
**Sawal:** Aapka grounded checker report ki har claim pe PASS deta hai, edge IDs cite karte hue. Ek hafte
baad, ek claim galat nikalti hai. Failure kahan ho sakti hai, aur konsi course fix karti hai?
**Jawab:** Ya to **graph galat thi** (bad extraction ya false merge — Part 3 discipline problem, jise
tight resolution/provenance audit fix karta hai), ya **checker galat tha** (galat edge cite ki jo asal
mein support nahi karti — checker-quality problem, jise **Trusting the Checker** measure karti hai).
Grounding ne *"kahin kuch ghalat hai"* ko **2 auditable suspects** tak narrow kar diya — yehi jeet hai.

---
[⬅ Graph of Facts](02-graph-of-facts.md) · [Agla: Graph of Loops ➡](04-graph-of-loops.md)
