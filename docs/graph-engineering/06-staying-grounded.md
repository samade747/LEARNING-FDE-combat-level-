# 06 — Staying Grounded: Kab Nahi Banani

## Concept 14: Level Chuno, Budget Set Karo

Graph ke khilaf case se pehle, level chunne ka procedure. **6 sawal**, order mein, decide karte hain
kitni structure kaam ko chahiye. Har "nahi" jawab ek layer bacha leta hai.

1. **Success verify ho sakta hai?** Agar nahi, autonomy se shuru mat karo — pehle test/rubric define karo
2. **Steps stable hain?** Haan → chain kaafi hai. Nahi → planning/orchestrator chahiye
3. **Subtasks independent hain?** Haan → parallelize karo. Nahi → dependencies model karo
4. **Alternative lineages zinda rehni chahiyen?** Haan → **DAG** chahiye (Concept 5)
5. **Facts run se bach kar rehne chahiyen?** Haan → artifacts + graph state persist karo
6. **Cost + latency afford ho sakti hai?** Workers add karne se pehle budget set karo

| Situation | Shuru karo | Kyun |
| --- | --- | --- |
| Simple, low-risk sawal | Zero-shot | Kam latency, koi machinery nahi |
| Output check ho sakta hai | Loop | Repeated feedback artifact improve karta hai |
| Sequence stable hai | Chain | Predictable, testable stages |
| Categories clear hain | Router | Policies/models alag rakhta hai |
| Units independent hain | Parallel workers | Wall-clock time kam |
| Decomposition har task pe alag | Orchestrator-workers | Dynamic specialization |
| Alternatives zinda rehni chahiyen | Commit DAG | Experiment branches preserve |
| Facts sessions se bachni chahiyen | Knowledge graph | Persistent shared memory |
| Bohat bara parallel kaam | Dynamic workflow | Fan-out/fan-in automate |

**Graph 8th row hai, pehli nahi.** Zyada tar kaam pehle hi ruk jata hai — ye failure nahi, sahi outcome
hai.

**Har run se pehle "complexity budget" declare karo:** max model calls, max sub-agents, max concurrent
workers, max tool calls, max wall-clock time, max tokens, max cost, max retries, max graph writes, aur
**minimum evidence** jo "finished" kehne se pehle chahiye — yehi wo item hai jo log bhool jate hain.

> **Budget khatam ho jaye to:** best current artifact wapas do, jo kaam complete hua, jo issues khule
> reh gaye, aur ruknay ki wajah. **Partial failure ko fluent final answer ke peeche mat chupao.** *"40
> mein se 40 files pe ruka kyunke token budget khatam ho gaya, ye raha jo 40 ne dikhaya"* us confident
> report se zyada valuable hai jo chup chaap 2/3 kaam cover kare.

## Concept 15: Kab Graph Nahi Banani Chahiye

Concept 14 procedure deta hai. Ye concept **case against** deta hai — is book ki honest-grading tradition
mein. **Sirf isliye knowledge graph mat banao kyunke system mein agents hain.** Graph ek real bill wali
machinery hai: extraction errors, resolution risk, schema maintenance. **Skip karo jab:**

- tasks independent hon, cross-session state ki zaroorat na ho
- jawabat ek document se aayein
- relations fixed aur simple hon (relational table sab kuch answer kar deta hai)
- provenance zaroori na ho
- extraction errors traversal value se zyada hon

**Graph tab apni cost kamati hai** jab connected queries, evolving relations, provenance, ya shared
world state central hon.

**2 failure modes jo bani hui graphs mein hoti hain:**

- **Graph builder ke judgment ko amplify karti hai — bad judgment samet.** Loop apna objective aur
  evaluator amplify karti hai. Graph apni **ontology aur source policy** amplify karti hai. Galat entity
  types choose karo, galat sources admit karo — automation error ko scale kar deta hai.
- **Metrics yahan bhi game ho sakte hain.** Sirf entity recall ke liye tuned extraction pipeline graph
  ko flood kar degi. Sirf compression ke liye tuned resolution ajnabiyon ko merge karegi (Concept 7 ka
  trap). Har optimization ko apna counter-metric chahiye — precision vs recall, compression vs false
  merges.

> **Simple:** Graph facts ke liye ek **bureaucracy** hai. Achi bureaucracy sab kuch findable aur
> auditable banati hai. Buri bureaucracy rumors ko official-looking seal laga kar khoobsurati se file
> kar deti hai. **Stamp truth nahi hai — file ke neeche ka receipt truth hai.**

## Concept 16: Graph Kya Nahi Kar Sakti

**"Checker ka PASS ab trustworthy hai."** Nahi. Grounding ne verdict ko impression se audit tak upgrade
kiya, lekin auditor phir bhi model hai — galat edge cite kar sakta hai, exist karta path miss kar sakta
hai. Checker ko measure karna (golden sets, calibration, drift) agli course hai: **Trusting the Checker**.

**"Memory apni jagah safe hai."** Sirf utni safe jitna uska ghar. Laptop repo mein graph laptop ke sath
marti hai. Swarm ki shared memory wahan honi chahiye jahan har worker (local, scheduled, cloud) pohanch
sake. Ye agli course hai: **Leaving the Laptop**.

**"Behtar wiring ka matlab behtar judgment hai."** Is book ki sab se purani boundary, jo hilti nahi.
Graph memory aur evaluation ko context window se **bahar** rakhti hai — yehi is poore course ka sab se
zaroori insight hai: **bottleneck aksar agla model call nahi hota. Ye memory aur evaluation ki placement
hoti hai.** Lekin ontology, source policy, anchors, aur *"behtar ka matlab kya hai"* ka jawab — ye sab
**har graph ke bahar se, aapse ata hai.**

> **Simple:** Graph memory aur checking ko agent ke "sar" se bahar move karti hai — ye ek real jeet hai:
> isi liye 1000 agents ek problem pe kaam kar sakte hain bina zero se shuru kiye. Lekin ye decide nahi
> kar sakti memory **kis liye** hai. Kisi ko choose karna hai kaunsi cheezein yaad rakhne ke qabil hain,
> kaunse sources evidence count hote hain, aur "behtar" ka matlab kya hai. **Wo koi aap ho, aur koi bhi
> wiring ye kaam nahi le sakti.**

---
[⬅ Complete Graph Example](05-complete-graph-example.md) · [Agla: Practice Projects ➡](07-practice-projects.md)
