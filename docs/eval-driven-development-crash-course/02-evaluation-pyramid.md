# 02 — Part 2: The Evaluation Pyramid (Concepts 4-7)

## Concept 4 — 9-Layer Evaluation Pyramid

Reliable agentic AI ko multiple layers par evaluation chahiye, bilkul jaise reliable SaaS application
ko multiple layers par testing chahiye (unit → integration → end-to-end → manual QA → monitoring).
Agentic AI ke layers SaaS testing pyramid ko replace nahi karte, **extend** karte hain.

**3 groups:**
- **Foundation (layers 1-2)** — unit aur integration tests, SaaS tradition se seedhe carry hote hain
- **LLM/Agent evaluation (layers 3-6)** — output, tool-use, trace, RAG evals — yeh agentic-AI ki apni
  discipline hai
- **Operational reliability (layers 7-9)** — safety, regression, production evals — yeh working eval
  suite ko production-grade reliability practice banate hain

**3 observations:**
1. **Har layer un failures ko pakarta hai jo neeche wali layers ke liye invisible hain** — layered
   defense, redundant nahi
2. **Cost aur frequency upar jate hue trade-off karte hain** — unit tests almost free, har commit par
   chalte hain; production evals continuously background mein sampled real traces par chalte hain
3. **Ek dataset, kai lenses** — ek hi golden-dataset example ko output eval, tool-use eval, trace eval,
   aur safety eval — chaaron grade kar sakte hain, alag scores ke sath

**9 Layers, Ek-Ek Karke:**

| Layer | Kya Check Karta Hai | Kya Cover Karta Hai (Courses 3-8) |
| --- | --- | --- |
| 1. Unit tests | Deterministic code: tool functions, utility modules, schema validation | Tool implementations, MCP server code, Inngest step functions |
| 2. Integration tests | Components sath kaam karte hain: API contracts, DB transactions, auth | Paperclip approval primitive, durability layer |
| 3. Output evals | Final response: sahi jawab, format, hallucination avoid | Har agent ka response |
| 4. Tool-use evals | Sahi tool, sahi arguments, sahi response handling | Har Worker ka tool-using behavior — **yeh pehli genuinely agent-specific layer hai** |
| 5. Trace evals | Poora internal execution path: reasoning, handoffs, retries | Multi-step reasoning, especially Claudia ke signed-delegation decisions |
| 6. RAG/knowledge evals | Retrieval quality, grounding, faithfulness | Course 4 ki MCP-served knowledge bases — **sabse common production failure retrieval failure hai** |
| 7. Safety/policy evals | Constraints, unsafe actions, permissions, escalation | Authority envelope (Course 6), auto-approval policy (Course 7), delegated envelope (Course 8) — **sabse consequential failures yehi hain** |
| 8. Regression evals | Current behavior vs previous behavior | Har change har agent mein — **yehi shipping ko engineering banata hai, guesswork nahi** |
| 9. Production evals | Real traces, user feedback, operational metrics | activity_log aur governance_ledger — **sabse hard layer, sabse zyada underestimate hoti hai** |

**Pyramid checklist nahi hai** jahan har layer equal attention maange. Ek pragmatic team neeche se
shuru karti hai aur upar badhti hai, jaise-jaise agent ki complexity aur deployment stakes barhein.

### Ek Eval Kaisi Dikhti Hai (Concepts 5-7 Se Pehle)

**Ek golden-dataset row:** task_id, category, input, customer_context, expected_behavior,
expected_tools, expected_response_traits, unacceptable_patterns, difficulty — sab JSON mein.

**Ek rubric:** markdown mein 1-5 scale, har score ka criteria describe karta hai.

**Ek grading output:** score + rationale + threshold + result (PASS/FAIL).

**Yehi shape har eval ka hai: dataset row, rubric, grader, score.** Course dozens se sainkron aisi
evals banata hai, pyramid ki har layer par, aur unhe CI/CD mein wire karta hai taake critical metrics
regress hone par merges block hon.

## Concept 5 — Output Evals: Accessible Starting Point Aur Uski Limits

Output evals likhna sabse asaan hai aur sabse common starting point. Yeh acha hai (jaldi ship hona
kuch na karne se behtar hai), lekin trap bhi hai (jo teams sirf yahan ruk jati hain woh sabse zyada
nuksan wale failure modes miss kar deti hain).

**Output eval kaisa lagta hai:** agent task receive karta hai, response deta hai; eval usay metrics par
grade karti hai (LLM-as-judge grader, usually agent se bara/capable model).

**Output evals jo achi tarah pakarte hain:**
- Format violations
- Refusals jo nahi honi chahiye thi
- Obvious factual errors
- Grounded tasks par hallucinations
- Tone aur clarity

**Output evals jo systematically miss karte hain:**
- **Process failures with correct outputs** — response sahi lag sakta hai jabke agent ne galat kaam
  kiya (Concept 3 ka wrong-customer example)
- **Unnecessary tool calls** — output theek hai, process wasteful hai
- **Lucky correctness** — flawed reasoning phir bhi sahi response, lekin agli baar sahi nahi hoga
- **Reasoning failures post-hoc rationalization se chupi hui** — response ek confident explanation
  deta hai jo agent ne asal mein kya kiya usse match nahi karta

**Output evals ka sahi role:** pyramid ki tez, sasti, frequent layer — har commit par chalti hai. Woh
failures pakarti hai jo response level par obvious hon. **2025-2026 mein modal pattern:** output scores
achi lagti hain, production failures phir bhi hoti rehti hain, team "evals don't work for agents"
conclude kar leti hai. Honest diagnosis: unki evals sirf ek layer par thi.

## Concept 6 — Tool-Use Aur Trace Evals: Path Bhi Result Jitna Matter Karta Hai

Tool-using agents (Course 3 se aage almost sab) ke liye **path** utna hi matter karta hai jitna
**result**. Tool-use evals aur trace evals woh 2 layers hain jo path grade karti hain — agentic AI
evaluation ki workhorse layers, jo output-only teams sabse zyada underestimate karti hain.

**Tool-use evals — 4 metrics:**
- **Tool-selection** — sahi tool chuna gaya?
- **Argument-correctness** — sahi arguments diye gaye?
- **Response-interpretation** — tool ke response ko sahi samjha gaya? (yehi metric wrong-customer
  refund example mein fail hota hai)
- **Efficiency** — unnecessary tool calls to nahi hue?

Tool-use evals ko **structured trace data** chahiye — har tool call ka record uske arguments aur
response ke sath.

**Trace evals — poora execution path:** model calls, tool calls, handoffs, guardrails, intermediate
reasoning, retries, error handling.

**Trace evals jo pakar sakte hain jo output/tool-use evals nahi pakar sakte:**
- Reasoning failures jo sahi tool calls ke darmiyan hoti hain
- Handoff failures (multi-agent systems mein galat specialist ko handoff)
- Guardrail bypasses
- Retry storms (stuck-loop pathology)
- Path-of-least-resistance failures

**Concrete example — Claudia ka signed-delegation behavior:** output eval final decision grade karta
hai (approved/escalated sahi tha?) — zaroori lekin insufficient. Tool-use eval har step grade karta
hai (sahi endpoint poll kiya, sahi instruction set retrieve kiya, sahi key se sign kiya?). Trace eval
reasoning grade karta hai (request ko standing instructions se sahi map kiya? confidence assignment
historical pattern se match karta hai?) — **yehi sabse important failure pakarta hai: Claudia ne ek
technically correct signed decision banaya jo Maya ke apne decide karne ke tareeqe se contradict karta
hai.** Teen layers, teen lenses, ek hi decision par — koi ek layer teeno failure modes nahi pakregi.

## Concept 7 — RAG Evals: Retrieval Failures Ko Reasoning Failures Se Alag Karna

Yeh layer **knowledge-layer agents** ke liye specific hai — jo koi knowledge base, documentation,
vector database, ya MCP-served knowledge se retrieve karke jawab dete hain. Course 4 ka pattern: agent
company ka poora knowledge context mein nahi rakhta, retrieval tool call karta hai jab zaroorat ho
(RAG — retrieval-augmented generation).

**RAG agent ke 3 failure modes jo doosre agents mein nahi hote:**

1. **Retrieval failure** — agent "billing policy" pucha, tool "shipping policy" wapis de deta hai.
   Reasoning sound ho sakti hai, source hi galat hai. Output evals isay agent reasoning failure
   misdiagnose karte hain.
2. **Grounding failure** — sahi documents retrieve hue, lekin response un documents se unsupported
   claims include karta hai — invented ya pre-training se.
3. **Citation failure** — retrieval sahi, grounding sahi, lekin agent ne source cite nahi kiya ya
   galat cite kiya — regulated industries mein apna compliance problem.

**Ragas ke 5 metrics, har failure mode ke liye:**

| Metric | Kya Measure Karta Hai | Kaunsi Failure Pakarta Hai |
| --- | --- | --- |
| Context Relevance | Retrieved context relevant tha? | Retrieval ne irrelevant chunks di |
| Faithfulness | Answer ke sab claims context se supported hain? | Agent ne invented facts diye |
| Answer Correctness | Ground-truth se compare karke, answer sahi hai? | Combined "final answer sahi hai?" check |
| Context Recall | Ground-truth ke kitne facts retrieved hue? | Retrieval ne key information miss ki |
| Context Precision | Retrieved chunks mein kitne relevant the? | Retrieval ne noise return kiya |

**Diagnostic value:** agar output eval sirf 2/5 score de, RAG metrics ke bina team nahi janti agent
ki reasoning prompt improve kare, retrieval logic, knowledge base, ya chunking/embedding strategy. **Har
failure mode ka apna alag fix hai**, aur RAG evals decompose karti hain ke kaunsa.

Isi wajah se lab mein **TutorClaw** introduce hoti hai (Decision 5) — ek teaching agent jo Agent Factory
book se retrieve karke jawab deti hai, isliye Ragas pattern usay achi tarah lagta hai. Maya ke customer-
support agents mostly tool-use aur reasoning dominant hain, primarily RAG nahi.

---
[⬅ The Discipline](01-the-discipline.md) · [⬆ Index](README.md) · [Agla: The Stack ➡](03-the-stack.md)
