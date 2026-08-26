# Graph Engineering — Summary

"The agent forgets, the graph does not." Ek loop ki memory (progress.md) sirf usi loop ke liye kaam karti hai. Jab kai loops/agents facts share karein, agents ko **typed, connected records** (nodes + edges) ki tarah likhna hai — graph engineering yehi sikhati hai. Loop Engineering aur Harness Engineering pe based hai.

## 00 — Overview: Memory Problem

- Ek loop se bohat loops tak: 20 agents khaali context se start hote hain, dobara wahi dhoondte hain, findings transcripts mein chhorte hain jo koi aur parhta nahi — **kaam multiply hua, memory nahi hui.**
- **2 Graphs, alag kaam:** Commit DAG (kaam yaad rakhta hai — kya try hua; nodes=commits; edges=parent_of/derived_from) vs Knowledge Graph (facts yaad rakhte hain — kya pata hai; nodes=entities/claims/sources; edges=supports/works_for/about). Truth rules alag: commit fact hai construction se, claim evidence wali statement hai (galat ho sakti hai). Dono connect hote hain lekin kabhi merge nahi.
- **Graph kya hai:** nodes typed hain, edges labeled+directed hain, paths jawab hain. DAG = directed acyclic graph (Git history isi ki misal).
- **Kya waqai graph chahiye?** Agar tasks independent, jawabat ek document se, relations fixed/simple, provenance zaroori nahi — relational table/spine kaafi hai, wahin ruk jao.

## 01 — DAG of Work: Karpathy Ka Rasta

- **Concept 4 — Autoresearch:** Karpathy ka ratchet-loop ML training pe. 2 memories: Git branch (sirf retained/verified improvements) vs results.tsv (har attempt, kept/discarded/crashed). Reset commit **remove** karta hai, park nahi — discarded experiment sirf untracked TSV mein bachta hai.
- **Concept 5 — AgentHub:** "asynchronously massively collaborative" — reset karna band, **rakhna** shuru. Har pushed commit durable node banta hai, main pe converge zaroori nahi. Commands: `ah push/children/leaves/lineage/diff/log`. "Graph-grounded context construction." Honesty: AgentHub ab public nahi hai — sirf design se seekho.
- **Bonus — Dynamic Workflows** (Anthropic, 28 May 2026): Claude khud orchestration program likhta hai (fan-out auditors, filter, reviewers, synthesizer). Limits: up to 16 concurrent agents, 1000 total per run.

## 02 — Graph of Facts: Anthropic Ka Rasta

- **Concept 6 — Extraction:** Anthropic Knowledge Graph Construction Cookbook — structured-output prompts (Pydantic schema = "training data"), sasta model (Haiku) volume work karta hai, `description` field context capture karti hai resolution ke liye.
- **Concept 7 — Resolution:** same entity, kai naam ("Edwin Aldrin"/"Buzz Aldrin"). String similarity fail karti hai dono directions mein. Fix: reasoning task — stronger model (Sonnet) canonical clusters propose karta hai descriptions se. Rule: resolution additive+reversible — kuch overwrite nahi hota. False merge sab se badi failure hai. Self-check: high compression ratio sirf tab achhi khabar jab pairwise precision qaim ho.
- **Concept 8 — Provenance:** NetworkX MultiDiGraph, lekin zaroori cheez container nahi. Dobara dikhne wali entity source+alias **add** karti hai, replace nahi; unresolved **drop** hota hai, guess nahi hota. **4 Invariants:** har claim ka source (ya "inference" mark), har artifact ka authoring run+version, har evaluation apni rubric identify kare, har superseded object addressable rahe (replace, delete nahi).

## 03 — Graph Se Kaam Lena: Subgraph + Grounded Checker

- **Concept 9 — Subgraph, poori graph nahi:** bounded retrieval, 7 steps (resolve, expand 1-2 hops, include current artifacts, prioritize recent/verified, conflicts shamil karo, token-budget serialize, stable edge identifiers). Workers typed graph updates publish karte hain, orchestrator ki context clean rehti hai.
- **Concept 10 — Grounded Checker:** verdict ab **claims ko edges ke against** check hota hai, sirf impression nahi. "Triple not found: ye 2 edges chahiye" &gt; "Seems off". Grounding memory bhi improve karti hai (maker naya edge dhoondh sakta hai). 1 graph, 5 workflow patterns (chain/fan-out/orchestrator-workers/evaluator-optimizer), same 3 roles: shared memory, grounding layer, persistent world model. Honesty: grounded verdict sirf utni achhi jitni graph ke edges sahi hain aur checker reliably paths dhoondta hai — checker-quality measurement agli course (**Trusting the Checker**) hai.

## 04 — Graph of Loops: Governance Layer

- **Concept 11 — Wiring:** governance graph mein loop khud node hai, edges wiring hain. Maker-checker split = edge; two-routine gate = 3-node graph; dreaming loop = graph. "graph loops hain, composed." 2 machine types: execution loop vs improvement loop. 3 sawal har edge pe: routing, trust boundaries, gate placement.
- **Concept 12 — Perez Ke 4 Failures:** Gaming (Goodhart's law — counter-metric watching loop do), Blindness upward (slower loop faster loop ka target owns kare), Conflict (arbitration node/human gate), Measurement decay (independent audit loops).
- **Concept 13 — Anchors Aur Frozen Nodes:** circular graph (sab ek dusre se agree, kuch real-world check nahi) khatarnak hai. Graph ko chahiye: Anchors (measurements jinse koi loop bahas nahi kar sakti — real tool output, test runner), Frozen nodes (check.py, prepare.py, held-out test set — optimizing loops kabhi na badal sakein), Root judgment bahar se ("behtar" ka jawab logon se ata hai). Audit: 10 random claims/verdicts leaves tak walk karo — grounding ka number.

## 05 — Ek Complete Graph (Morning Triage Upgrade)

- Disk shape: `graph/` (SCHEMA.md, entities.json, claims.json, runs.json) + `evidence/` (raw tool output, kabhi edit nahi hota). JSON ~10,000 claims tak comfortable, upar Postgres/Neo4j.
- Ek claim example: `id`, `subject/predicate/object`, `confidence`, `source` (kind:tool_output, command, exit_code, ref, captured), `produced_by`, `supersedes`, `created`. 3 zaroori design decisions: **koi status field nahi** (append-only, active = jo supersede na ho), predicate `diagnosed_as` na `caused_by` (evidence jitna support kare utna hi), source tool ka naam le agent ka nahi.
- Pre-commit hook (jq): required fields, unique ids, resolvable supersedes, append-only enforce karta hai (field types/entity existence check nahi karta — wo guidance hai).
- Reviewer graph se parhta hai: har claim ke liye supporting claim cite karo, `inference` source akela ground nahi kar sakta, plausibility pe approve mat karo.
- Before/after: spine-only mein 3-hafte-baad sawal "archaeology dig" hai; graph ke sath `jq` se ek line mein receipt ke sath answer milta hai.

## 06 — Staying Grounded: Kab Nahi Banani

- **Concept 14 — Level chuno:** 6 sawal (success verify ho sakta hai? steps stable? subtasks independent? lineages zinda rehni chahiyen? facts run se bachni chahiyen? cost afford ho sakta hai?) — graph 8th row hai, pehli nahi. Har run se pehle complexity budget declare karo (calls, agents, workers, tools, time, tokens, cost, retries, graph writes, **minimum evidence**). Budget khatam ho to partial failure ko honestly report karo.
- **Concept 15 — Kab graph nahi banani:** skip karo jab tasks independent hon, ek document se jawab aayein, relations fixed/simple hon, provenance zaroori na ho. 2 failure modes: graph builder ke bad judgment ko amplify karti hai (ontology/source policy), metrics gameable hain (entity recall vs compression — dono ko counter-metric chahiye).
- **Concept 16 — Graph kya nahi kar sakti:** "Checker ka PASS trustworthy hai" — nahi (Trusting the Checker measure karti hai). "Memory apni jagah safe hai" — sirf utni jitna uska ghar (Leaving the Laptop). "Behtar wiring = behtar judgment" — nahi, ontology/source policy/anchors/"behtar ka matlab" hamesha insaan se ata hai.

## 07 — Dogfooding: Yeh Kitaab Khud Graph Kahan Use Karti Hai

Ye kitaab **proto-graph** chalati hai — reader notes, GitHub issues, PRs, aur lessons sab typed,
directed-linked records hain, jinse har shipped fix wapas us reader note tak trace ho sakti hai. Ye
poori knowledge-graph extraction/resolution **jaan boojh kar nahi chalati** (Concept 15 khud par apply):
relations simple hain, cross-session sawal links se hi answer hote hain, extraction pipeline abhi tak
kisi query se earn nahi hui. Graph tab banega jab ek real sawal usay demand kare.

## 08 — Practice Projects (8 Graph Builds)

2 rules hamesha: throwaway repo + real documents, schema pehle likho (`graph/SCHEMA.md`).
1. **Draw Your System** (Easy) — sab loops/checkers/gates/anchors ko typed nodes+edges draw karo.
2. **Spine to Claims** (Easy) — real progress.md ke 10 findings ko claims.json mein convert karo, inference-marked count karo.
3. **First Extraction** (Medium) — Concept 6 prompt 3 documents pe chalao, jq validate, duplicate surface forms count karo.
4. **The DAG Speaks** (Medium) — real Git history se AgentHub ke 3 sawal answer karo, GRAPH.md likho.
5. **Resolution Drill** (Medium) — 20 surface forms resolve karo, deliberately trap (2 same-named ajnabi) plant karo.
6. **The Grounded Reviewer** (Hard) — Part 6 reviewer ek chalti loop mein wire karo, 5 real beats chalao.
7. **A Gold Set for Extraction** (Hard) — 5 documents hand-label, prompt ko score/ratchet karo (kam se kam 3 dafa).
8. **Two Loops, One Graph (Capstone)** — triage + changelog loop ek graph share karein, pre-commit hook guard kare, counter-metric ho.

## 09 — Sources & Further Reading

Primary sources: Karpathy ka autoresearch + AgentHub (private ho chuki hai), Anthropic ki Knowledge
Graph Construction Cookbook + Dynamic Workflows, Peter Steinberger ka "loops vs graphs" sawal, Carlos E.
Perez ka governance essay. **Origin-story correction:** viral "1000x" PDF khud apne front page par
kehti hai *independently compiled, not affiliated with/endorsed by Karpathy or Anthropic* — course
apni khud ki provenance-discipline apne inputs par bhi apply karta hai.

## 10 — Test Your Understanding (18-Q Exam Assessment)

Live page ka `<Flashcards />` widget auto-generated hai (static copy possible nahi). Uske baad 18-question
scenario-based `<Quiz>` (Concepts 1-16, Part 6, dogfooding sameet) — English mein verbatim (precision ke
liye translate nahi kiya), sahi jawab + real-world analogy ke saath. Standalone copy: `quiz.md`.
