# Graph Engineering — Aasan Summary (Roman Urdu + English)

*Source: The AI Agent Factory — "Graph Engineering: A Crash Course" (Panaversity) — 16 Concepts, Parts 1-7*
*URL: https://agentfactory.panaversity.org/docs/graph-engineering-crash-course*
*Poora tafseeli breakdown: [`docs/graph-engineering/`](docs/graph-engineering/README.md) (8 files, 00-07)*

---

## 🎯 Bunyadi Idea (The Big Shift)

> **"Agent bhool jata hai, graph nahi bhoolta."**

Yeh chapter Loop Engineering aur Harness Engineering ke oopar banti hai. Ek loop ki memory
(`progress.md`) sirf **usi ek loop** ke liye kaafi hai. Lekin jaise hi aap doosra loop add karte hain, phir
ek review loop, phir 20 agents ek saath 20 files audit karne chhorh dete hain — har agent khaali context
se shuru hota hai, wahi bug dobara dhoondta hai jo kisi aur ne pehle hi dhoondh liya tha. **Kaam barh
gaya, memory nahi barhi.**

Hal: agents jo seekhein usay **typed records** ki tarah likhein — entity, claim, source, run — labeled
arrows se jude hue. Koi bhi baad wala agent isay query kar sakta hai.

---

## 0. Zaroori Terms — Glossary

| Term | Aasan Matlab |
| --- | --- |
| Graph | Points (nodes) jo arrows (edges) se jude hon — direction ka matlab hota hai |
| Node | Graph ka ek point — entity, claim, commit, source, agent run |
| Edge | Do nodes ke darmiyan labeled arrow — jaise `supports`, `parent_of`, `produced` |
| DAG | Directed Acyclic Graph — arrows kabhi wapas apni taraf nahi aate (Git history isi ki misaal) |
| Commit DAG | Kaam ka graph — commits nodes, parent links edges. "Kya try hua?" ka jawab |
| Knowledge Graph | Facts ka graph — entities nodes, typed relations edges. "Kya sach hai?" ka jawab |
| Entity Resolution | Kaunse surface forms ek hi cheez hain, unhe ek canonical node mein jorna |
| Provenance | Claim ki "receipt" — kaunsa source, kaunsa run, kitna confidence |
| Subgraph | Graph ka chhota, relevant hissa — ek task ke liye. Poora graph kabhi nahi diya jata |
| Grounding | Jawab ko graph ke asal edges se jorhna, apni impression se nahi |
| Governance Graph | Wo graph jiske nodes khud loops hain — kaun kise check karta hai |
| Anchor | Wo measurement jis se koi loop bahas nahi kar sakta — asal test, asal customer, asal paisa |
| Frozen Node | Wo rule/file jo optimizing loops kabhi nahi badal sakte |

---

## Part 1 — Memory Ka Masla (Concepts 1-3)

- **progress.md ek loop ke liye theek hai**, lekin: doosra loop is par bharosa nahi kar sakta (prose,
  format badal sakta hai), 20 parallel agents share nahi kar sakte, query nahi kar sakte, source nahi deta
- **Graph = teen cheezein:** nodes typed hote hain (sirf "box" nahi), edges labeled+directed hote hain,
  paths jawab hote hain — "Kya X, Y se juda hai?" ban jata hai "kya edges ka koi raasta maujood hai?"
- **Do graphs, mila mat do:** Commit DAG (kaam — nodes=commits, truth=fact-by-construction) vs
  Knowledge Graph (facts — nodes=entities/claims, truth=statement-with-evidence, ghalat ho sakti hai).
  Dono jud sakte hain: `(agent_run) →produced→ (claim) →about→ (entity)`
- **Rukiye yahin agar:** tasks independent hain, jawab ek document se aate hain, relations simple hain,
  provenance nahi chahiye — ek spine wala loop hi kaafi hai

## Part 2 — Kaam Ka DAG (Concepts 4-5, Karpathy Ka Rasta)

- **Autoresearch (7 March 2026):** memory transcript nahi, **commit DAG** hai. Git branch = sirf
  retained/verified improvements; `results.tsv` = HAR attempt (kept/discarded/crashed). Reset commit
  branch se hatata hai, TSV mein reh jata hai — discarded idea koi query nahi kar sakta
- **AgentHub:** "GitHub insaano ke liye hai, AgentHub agents ke liye." Reset karna band, **rakhna**
  shuru — har commit durable node banta hai. `ah push/children/leaves/lineage`. Ghalat experiment bhi
  ek node banta hai jisse agla agent seekh sake — yehi swarm aur crowd mein farq hai. (Nota bene:
  AgentHub abhi private hai — sirf design idea seekhein)

## Part 3 — Facts Ka Graph (Concepts 6-8, Anthropic Ka Rasta)

Anthropic ki Knowledge Graph Construction Cookbook — 4 stages, koi trained NLP model nahi chahiye:

- **Extraction:** Pydantic schema (Entity, Relation) hi "training data" hai. Sasta model (Haiku) volume
  kaam karta hai; `description` field decoration nahi, resolution ke liye zaroori context hai
- **Resolution:** "Edwin Aldrin"/"Buzz Aldrin"/"Col. Aldrin" — 3 naam, 1 insaan. String similarity fail hoti
  hai. Fix: reasoning task ki tarah treat karo, strong model canonical clusters banwaye. **Usool:
  additive + reversible** — aliases kabhi mitao mat, sirf link karo. False merge sabse bara khatra hai
- **Provenance — 4 invariants:** har claim ka source (ya "inference" mark), har artifact ka authoring
  run+version, har evaluation apni rubric bataye, har superseded object addressable rahe (replace,
  delete nahi)

## Part 4 — Graph Se Kaam Lena (Concepts 9-10)

- **Subgraph, poori graph nahi:** bounded retrieval — resolve → expand (1-2 hops) → include current
  versions → prioritize recent/verified → conflicts shamil karo → token budget mein serialize → stable
  edge IDs attach karo. *"Naye employee ko poori filing cabinet mat do — sirf 3 relevant folders."*
- **Grounded Checker — "Triple not found" > "Seems off":** verdict ab edges ke against check hota hai.
  Maker: "Vendor X ne component supply kiya." Checker: `(vendor_x, supplied, component_z)` edge
  maujood hai? Nahi → `{"decision": "revise", "required_evidence": [...]}`. Yeh ek work order hai, mood
  nahi — aur jab maker evidence dhoondh leta hai, graph ko nayi edge milti hai

## Part 5 — Loops Ka Graph, Governance (Concepts 11-13)

- **Wiring:** governance graph mein loop khud node hai. Teen sawal har edge par: Routing (result kise
  jaye?), Trust boundaries (kaunsa loop kise fire kar sakta hai?), Gate placement (insaan kahan?).
  Model classify kare (probabilistic), route table deterministic ho
- **Perez ke 4 Failures:** Gaming (counter-metric watching loop), Blindness upward (dheema loop tez
  loop ka target owns kare), Conflict (arbitration node), Measurement decay (independent audit loops)
- **Anchors + Frozen Nodes:** circular graph (sab aapas mein "agree" karte hain, reality check nahi) se
  bachao — asal test/customer/paisa (anchors), check.py/prepare.py (frozen nodes), "behtar" ka faisla
  sirf insaan de sakte hain

## Part 6 — Ek Complete Graph (Concept — Morning Triage Upgrade)

3 JSON files, koi database nahi: `entities.json` (nodes), `claims.json` (edges-with-receipts),
`runs.json` (kaunsa beat ne kya likha) + `evidence/run_log.txt` (raw tool output).

**2 zaroori usool:** koi `status` field nahi (claims append-only, "active" read-time par derive hota hai —
jise koi supersede na kare wahi active hai); predicate `diagnosed_as` hai `caused_by` nahi (jitna evidence
prove kar sake, utna hi likho); source **tool** ka naam le, agent ka nahi.

*Pehle (sirf spine):* "kaunsi timezone thi?" → transcripts mein khudai. *Baad mein (graph):* `jq`
command se ek line mein receipt ke saath jawab.

## Part 7 — Grounded Rehna (Concepts 14-16)

- **Level chunna — 6 sawal pehle poochein:** success verify ho sakta hai? steps stable? subtasks
  independent? alternative lineages zinda rehni chahiye? facts run ke baad zinda rehne chahiye? cost
  afford ho sakta hai? → **Graph 8th row hai, pehla nahi.** Har run se pehle complexity budget declare
  karo (max calls/workers/tokens/cost)
- **Kab graph na banayen:** tasks independent, jawab ek document se, relations fixed/simple, provenance
  ki zaroorat nahi, extraction errors traversal ke faide se zyada honge
- **Graph kya nahi kar sakta:** "Checker ka PASS bharosemand hai" (nahi — checker phir bhi model hai),
  "Memory apni jagah mehfooz hai" (sirf jitni uski home mehfooz hai), "Behtar wiring = behtar judgment"
  (nahi — "behtar" ka matlab sab bahar se, insaan se aata hai)

---

## 8 Practice Projects

| # | Naam | Kya Prove Karta Hai |
| --- | --- | --- |
| 1 | Draw Your System | Apna poora setup nodes/edges ki tarah kheenchna |
| 2 | Spine to Claims | 10 findings ko typed claims mein badalna |
| 3 | First Extraction | Schema-constrained prompt se entities nikalna |
| 4 | The DAG Speaks | AgentHub ke 3 sawal plain Git se poochna |
| 5 | Resolution Drill | Sahi merge, ghalat merge se bachna |
| 6 | The Grounded Reviewer | Checker ko edge maangne par majboor karna |
| 7 | A Gold Set for Extraction | Extraction pipeline ko measure karna |
| 8 | Two Loops, One Graph (Capstone) | Do loops, ek shared graph, poora traceable |

---

## Exam-Prep Cheat Sheet

- Agent bhool jata hai, graph nahi bhoolta
- Do graphs: Commit DAG (kaam) aur Knowledge Graph (facts) — mila mat do
- Graph ke 3 usool: nodes typed hain, edges labeled/directed hain, paths jawab hain
- Autoresearch: Git branch (retained), `results.tsv` (har attempt)
- AgentHub: reset nahi, keep — har commit ek node banta hai
- Extraction: schema hi training data, cheap model volume ke liye
- Resolution: additive + reversible — false merge sabse bara khatra
- 4 Provenance Invariants: source, authoring run, rubric, supersession (kabhi mitao mat)
- Subgraph: poora graph kabhi nahi — resolve, expand, prioritize, conflicts shamil, budget mein serialize
- Grounded checker: "Triple not found" — mood nahi, work order
- 4 Failures: Gaming, Blindness upward, Conflict, Measurement decay — fix hamesha edge hai
- Anchors + Frozen nodes: circular graph se bachne ka ilaj
- 6 sawal pehle poochein level chunne se pehle — graph 8th row hai, pehla nahi
- Complexity budget: har run se pehle limits declare karein

---

Poori tafseeli breakdown (8 files, task-by-task) ke liye dekho [`docs/graph-engineering/`](docs/graph-engineering/README.md).
