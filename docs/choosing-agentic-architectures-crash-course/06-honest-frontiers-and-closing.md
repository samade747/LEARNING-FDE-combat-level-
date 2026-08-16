# 06 — Part 6-7: Honest Frontiers Aur Closing (Concepts 17-19)

## Concept 17 — Cost Aur Latency Architectural Constraints Hain, Afterthoughts Nahi

**Cost profile per pattern (rough orders of magnitude, GPT-5-class pricing):**

| Pattern | Cost Per Task | Cost Driver |
| --- | --- | --- |
| Sequential workflow | 1x (baseline) | LLM calls ki tadaad (usually 1-3) |
| Single agent + ReAct | 3-10x | ReAct iterations ki tadaad |
| Planning + ReAct | 5-15x | Planning call + per-stage ReAct loops |
| Reflection | +2-3x underlying pattern | Critique + refinement passes |
| Multi-agent | 5-20x | Specialists + coordinator + integration |

Numbers illustrative hain, exact nahi. **Jo matter karta hai ratios hain:** reflection ke sath multi-
agent system sequential workflow se 30-60x zyada cost kar sakta hai. Jab yeh multiplier quality se
justify ho, theek hai. **Jab aesthetics se justify ho, budget catastrophe wait kar rahi hai.**

**Latency profile:** Sequential (lowest, ~1-5s) → Single agent + ReAct (medium, ~10-30s) → Planning +
ReAct (medium-high, ~30-90s) → Reflection (+2-3x) → Multi-agent (variable, parallel execution madad
karti hai lekin coordination overhead add karti hai).

**Practical discipline:** decision tree walk karne se pehle latency aur cost budgets likh lo. Tree ka
chuna pattern budget violate kare to 3 options: (1) constraints badlo (zyada budget lo), (2) scope
badlo (system ki responsibility kam karo taake simpler pattern kaafi ho), (3) worse fit accept karo
(kam elaborate pattern use karo, jaante hue kuch failure modes hongi). **Jo option chuna, document karo
aur wajah likho.**

## Concept 18 — Pattern Composition: Alag Layers Par Multiple Patterns

Real systems aksar alag layers par patterns compose karte hain: top par planning agent, har plan stage
ke andar ReAct + tools, final output par reflection. **3 composition shapes:**

- **Hierarchical** — higher-level pattern lower-level patterns wrap karta hai (Planning top + ReAct
  har stage ke andar; Multi-agent coordinator top + sequential workflows specialists ke andar)
- **Sequential** — patterns ek ke baad ek chalte hain (Sequential workflow extract → ReAct agent
  investigate; ReAct agent generate → reflection critique)
- **Conditional** — alag patterns alag cases handle karte hain, router pattern select karta hai
  (known-shape → workflow, unknown-shape → ReAct)

**Pragmatic rule:** har layer ka pattern choice usi 5 sawal se justify hona chahiye, us layer ke scope
par apply karke. Top-level pattern poore task par tree walk karke chuno; har sub-component ka pattern
uska apna kaam dekh kar chuno. **Composition sophisticated lagne ke liye mat karo; karo kyunki har
layer ki task properties usay demand karti hain.**

**Sabse common composition mistake:** layers add karna kyunki "achi engineering" lagti hai. **Test:**
sabse upar wali layer hatao — outputs degrade na hon to layer apna cost nahi kama rahi thi.

## Concept 19 — Pattern Selection: Agent Factory Curriculum Mein Connective Tissue

Yeh course *agent kya hai* (agent-building course) aur *usay ship karna kya lagta hai* (cloud
deployment, eval-driven courses) ke darmiyan pul hai. Pattern selection ke bina, yeh connective tissue
missing hai — aap agent bana sakte ho, deploy kar sakte ho, lekin darmiyan ka design decision (is task
ke liye kaunsa agent type) unprincipled tha.

**Deployment composition:** Sequential workflows sandbox layer poori tarah skip karte hain; single-
agent ReAct poora stack use karta hai; planning+ReAct plan persistence + longer background workers add
karta hai; reflection multi-provider model routing introduce karti hai; multi-agent per-specialist
tracing/routing logs/cost attribution maangta hai. **Yeh farq ~$130/month wale deployment aur ~$400/
month wale deployment ke beech hai, same workload ke liye — pattern over-elaborate hone ki wajah se.**

**Evaluation composition:** har pattern ka apna eval signature hai — sequential (DeepEval step-level),
ReAct (Phoenix reasoning traces), planning+ReAct (plan-execution divergence custom metric), reflection
(pre/post comparison + rubber-stamp detection), multi-agent (3 scoreboards).

**Closing thesis:** Agent-building course ne kaha *agent loop AI-native company ka engine hai.* Cloud
deployment course ne kaha *agent loop, production scale par deployed, sahi surfaces se observed, living
eval suite se graded, AI-native company jispar chalti hai.* **Yeh course missing prefix add karta hai:
task ke liye sahi agent loop woh cheez hai jispar AI-native company chalti hai.** Galat shape chunna —
overshoot ya undershoot — aisi systems banata hai jo slower ship hoti hain, zyada cost karti hain, zyada
failure modes mein tootti hain. Pattern selection pehla design decision hai; baaki sab isi par depend
karta hai.

**Aage kya:** cloud deployment course ke 3 frontiers (agent-to-agent commerce, identic-AI deployment,
multi-region active-active) still open hain. Yeh course ek aur add karta hai: **pattern-specific
testing harnesses.** Eval suite generic hai; future course pattern-specific test generators bana sakta
hai (jaise "sequential workflow tester" jo workflow ki branches cover karne wale inputs generate kare).

## Quick Reference — 5 Sawal, 5 Patterns

```
Q1: Solution path pehle se define ho sakta hai?
    Yes → Q2
    No  → Q3 (agentic reasoning chahiye)

Q2: Workflow fixed aur stable hai runs ke across?
    Yes → SEQUENTIAL WORKFLOW
    No  → Q3 (ya branched workflow agar kam stable variants hon)

Q3: Task structure execution se pehle articulable hai?
    Yes → PLANNING + REACT EXECUTION
    No  → SINGLE AGENT + REACT + TOOLS

Q4: Quality > speed AND criteria checkable hain?
    Yes → REFLECTION add karo chuni hui pattern ke upar
    No  → skip karo

Q5: Specialization, context, ya scale bottleneck hai?
    Yes → MULTI-AGENT SPECIALIST SYSTEM
    No  → single-agent pattern rakho
```

## 5 Decisions, Ek Nazar Mein

| # | Decision | Core Pattern + Additive Layers |
| --- | --- | --- |
| 1 | Maya's Tier-1 Support | Single agent + ReAct + tools. Koi additive layer nahi |
| 2 | Incident response | Planning + ReAct + reflection remediation par |
| 3 | Market research | Multi-agent (planning+ReAct specialists ke andar) + reflection synthesis par |
| 4 | Enterprise onboarding | Sequential workflow. Negative example agentic patterns ke liye |
| 5 | Coding agent | Multi-agent (planning+ReAct andar) + reflection coder output par — sab kuch composed |

## Design-Review Template (Ek-Page, Printable)

Team-shareable worksheet — 15-20 minutes mein walkable, print karo har architecture proposal ke liye.

**Sections:** (1) Task name/description, (2) Core Pattern Q1-Q3 evidence ke sath, (3) Additive Layers
Q4-Q5 evidence ke sath, (4) Final Architecture, (5) Implementation & Deployment (SDK primitives,
operational envelope, cloud deployment subset), (6) Risk Analysis (cost class, latency budget check,
most likely failure signal + mitigation, eval signals), (7) Anti-Pattern Check (senior engineer
objection + counter-argument), (8) Sign-off (Prototype/Pilot/Production, approved by, re-review date).

**Poora template repo ke source mein available hai; poora point sawalon ko team discussion ke doran
visible rakhna hai, solo fill karna nahi.**

## References (Chunay Hue)

- Bala Priya C, "Choosing the Right Agentic Design Pattern: A Decision-Tree Approach," *Machine
  Learning Mastery*, May 15, 2026 — is course ki decision tree unki hai
- Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (2022)
- Wang et al., "Voyager: An Open-Ended Embodied Agent with Large Language Models" (2023)
- Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning" (2023)
- OpenAI Agents SDK reference: `openai.github.io/openai-agents-python`
- [Build AI Agents](../build-agents-crash-course/README.md), [Eval-Driven Development](../eval-driven-development-crash-course/README.md), [Deploy Your Agent Harness](../deploying-agents-crash-course/README.md)

---

*"Ek rule jo dimaagh mein rakhna hai: woh simplest pattern chuno jiske assumptions task ki asal
zaroorat se match karein, aur complexity sirf tab add karo jab aap woh specific property naam le sako
jo usay demand kare."*

---
[⬅ Decision Lab](05-decision-lab.md) · [⬆ Index](README.md)
