# 03 — AI Coding Ke Che Failure Modes

3 constraints predictable failures banate hain — **6 jo kaafi common hain** inko closed catalogue
ki tarah treat karte hain.

| # | Symptom | Root Cause | Cure | Skill |
| --- | --- | --- | --- | --- |
| 1 | "Agent ne wo nahi kiya jo maine chaha" | Shared design concept nahi tha | Asset likhne se pehle alignment force karo (Socratic interview) | `grill-me` |
| 2 | "Agent bohot verbose hai" | Koi ubiquitous language nahi, naming alag | `CONTEXT.md` har session load karo | `grill-with-docs` |
| 3 | "Code kaam nahi karta" | Weak feedback loops, agent blind coding kar raha hai | Loud environment (types/tests/lints) + TDD | `tdd` |
| 4 | "Hum ne ball of mud bana diya" | Shallow modules, agents jaldi banate hain | Daily module design + periodic deepening pass | `improve-codebase-architecture` |
| 5 | "Mera brain keep up nahi kar pa raha" | Har line 5x pace par parh rahe ho | Gray-box: interface design karo, implementation delegate karo | (architectural habit) |
| 6 | "Main building se zyada review kar raha hoon" | Throughput ne bottleneck ko review tak move kiya | Automated + human review layers, chhoti vertical slices | `automated-review` |

## Failure 1: "Agent Ne Wo Nahi Kiya Jo Maine Chaha"

Sab se common failure — **misalignment.** Tumhe clear picture thi, agent ne subtly alag kuch banaya.
Yeh communication problem hai, model problem nahi. Frederick P. Brooks ne naam diya tha: **design
concept** — jo banaya ja raha hai uska shared, ephemeral idea. PRDs/specs/conversations sirf **assets**
hain jo design concept capture karne ki koshish karte hain — koi bhi **khud** wo nahi hai.

**Cure:** design concept ko stabilize karo koi bhi code/formal asset likhne se **pehle**. Technique:
**grilling** — agent tumhe Socratically interview karta hai, decision tree ka har branch resolve
karta hai, har sawal ka apna recommendation deta hai, jab tak dono sides align na ho jayein.

## Failure 2: "Agent Bohot Verbose Hai"

Fresh agent tumhari jargon nahi jaanta — tum "lessons" kehte ho, agent "course units" kehta hai. Yeh
wahi problem hai jo **domain-driven design** ne 20+ saal pehle solve kiya: **ubiquitous language.**
Ek project ko ek shared vocabulary chahiye jisse code/tests/conversation/docs sab draw karen. Agents
ke sath ek doosra benefit hai: tighter vocabulary = kam thinking tokens ambiguity unfold karne mein.

**Cure:** repo root par `CONTEXT.md` rakho, har session load karo.

## Failure 3: "Code Kaam Nahi Karta"

Tumne align kiya, clean spec likhi, agent ne code banaya, aur code broken hai. Diagnosis almost
hamesha: **weak feedback loops.** Agent **blind coding** kar raha hai. *The Pragmatic Programmer*
warn karta hai "outrunning your headlights" ke against — agents yeh constantly karte hain, insaanon
se worse, kyunke woh khushi se 1000 lines likh denge bina check kiye ke compile hoti hain ya nahi.

**Cure:** environment loud banao (static types, tests, lints, pre-commit hook), phir **TDD** enforce
karo — failing test, pass karo, refactor, repeat.

## Failure 4: "Hum Ne Ball of Mud Bana Diya"

Agents sab kuch accelerate karte hain — including rate jis se codebase unmaintainable ban jata hai.
Bina intervention ke, yeh **shallow modules** banate hain (kai chhoti files, kai chhote functions,
implicit dependencies) — kyunke shallow modules ek-ek karke generate karna aasan hai. Agent jo apna
khud ka codebase navigate nahi kar sakta, har pass mein worse code banata hai — **poison loop.**

John Ousterhout ka alternative: **deep modules** — chand bare modules, simple interfaces, bohat
functionality chhupi hui. Deep modules agents ke liye test karna aasan (boundary = interface),
reason karna aasan, delegate karna aasan (interface design karo, implementation agent likhe).

**Cure:** daily module design mein invest karo (Kent Beck), periodically `improve-codebase-architecture`
chalao.

## Failure 5: "Mera Brain Keep Up Nahi Kar Pa Raha"

Surprising, serious failure. Senior engineers agents ke sath pehli baar kaam karte waqt **zyada
tired** report karte hain, kam kaam karne ke bawajood **zyada** ship karne ke baad. Agent 3-5x pace
par code produce karta hai — engineer **poora system** naye pace par apne zehan mein rakhta hai.
Bina architectural discipline, cognitive load **divide nahi hoti, multiply hoti hai.**

**Cure:** **gray-box principle.** Module interfaces full attention se design karo, implementation
agent ko delegate karo, module ko **bahar se** verify karo tests ke zariye, har line parh kar nahi.
Tum architectural map hold karte ho; agent bricks fill karta hai.

## Failure 6: "Main Building Se Zyada Review Kar Raha Hoon"

Throughput ka flip side. Agent jaldi ship karta hai, bottleneck **review** tak move hota hai, aur
review work usay fill karne ke liye expand hoti hai.

**Cure:** review ko 2 layers mein split karo — **automated layer** (high-throughput, routine issues
catch karti hai) aur **human layer** (low-throughput, jo automated nahi catch kar sakta). Ek
`automated-review` Skill fresh session mein chalti hai (sirf diff + coding standards + security
checklist input), structured comment PR par produce karti hai, pre-merge CI step ki tarah. Human
reviewer ko pre-triaged PR milta hai — taste, product-fit, aur ambiguous calls ke liye attention
free. Vertical slices diffs chhoti rakhti hain; persistent review loops automated reviewer ko
schedule par chalati hain. **Yeh human review khatam nahi karta — attention ko relocate karta hai
jahan judgement substitute nahi ho sakta.**

Yehi 6 failures hain jo baaqi chapter eliminate karta hai, order mein.

---
[⬅ Three Constraints](02-three-constraints.md) · [Agla: End-to-End Workflow ➡](04-end-to-end-workflow.md)
