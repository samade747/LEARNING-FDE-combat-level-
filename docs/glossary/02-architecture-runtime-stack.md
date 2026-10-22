# 02 — Architecture: The Runtime Stack

Yeh terms **AI-Native Company** ke components naam dete hain jo Agent Factory produce karti hai — architecture chapters aur thesis mein har jagah milte hain. Ek baar yahan parh lo, phir har build mein dobara milenge.

---

These terms name the components of the **AI-Native Company** that the **Agent Factory** produces. They appear throughout the architecture chapters and the thesis. Read them once here; you'll meet them again in every build.

> 💡 **How the pieces fit together:** The Agent Factory (the process) builds the AI-Native Company (the output). Inside that company, humans set direction from the Edge Layer, and Digital FTEs execute in the AI Workforce Layer. Paperclip manages the workforce. Each Digital FTE runs on a runtime engine of its choice. Triggers wake the system from the outside world.

---

### AI Worker

The **workforce** of the AI-Native Company. Role-based agents that get hired, assigned, rostered, and retired. Same concept as **Digital FTE** and **Digital Worker**: the thesis uses _AI Worker_, the book uses _Digital FTE_. Pick whichever term fits your audience.

> 📌 **Workforce vs. staff (load-bearing distinction):** Only AI Workers are workforce. The **delegate** (OpenClaw) and the **manager** (Paperclip) are permanent staff, not workforce. **Runtime engines** are not staff at all; they are the skills the workforce runs on. When the thesis says _agent_, it means anyone in the building (staff or workforce). When it says _AI Worker_, it means the workforce specifically.

> 🔹 **Example:** A resume-screening AI Worker reads 200 resumes per day, scores them against a job spec, and hands the top 10 to a human recruiter. It's a Digital FTE inside the AI-Native Company's HR workforce — hired by Paperclip, rosterable, retirable.

---

### AI-Native Company

The **output** of the Agent Factory. The running enterprise: a firm staffed by AI Workers (Digital FTEs), coordinated by a management plane, and directed by humans at the edge. The AI-Native Company is what you end up running. The book also calls this the **Agentic Enterprise** — same concept, business-facing name.

> 💡 **Analogy:** The Agent Factory is the process, like a method of building skyscrapers. The AI-Native Company is the skyscraper that method produces — the thing you actually run.

> 📌 **The triad:** Agent Factory (process) → AI-Native Company (output) → AI Workers (workforce inside the output). Three terms, three different roles. Not interchangeable.

---

### Two-Layer Model

The architectural pattern that makes the Agent Factory thesis complete: humans set intent from the **Edge Layer**, AI Workers execute in the **AI Workforce Layer**, and specs are the contract language between them.

> 🔹 **Example:** A CEO tells their OpenClaw delegate (Edge Layer) to "run the weekly customer-churn report." The delegate hands the task to a Digital FTE in the AI Workforce Layer. The Digital FTE pulls the data, generates the report, and hands it back through the delegate to the CEO for verification.

---

### Principal

The human at the apex of the runtime stack: the one who sets intent, defines the budget, draws the authority envelope, and owns the outcome. Invariant 1 of the thesis. Every legitimate chain of action originates with a principal; a system that acts without one is not autonomous, it is unowned (no liability, no alignment target, no budget owner, no judge of outcome).

> 🔹 **Example:** A CFO writes a spec: "Reduce accounts receivable aging by 20% within a $30K budget, without changing payment terms." That spec carries intent, budget, and constraints, the principal layer in concrete form. The delegate (OpenClaw) reads it and brokers work to the workforce; the principal returns to verify the outcome.

> 📌 **What can replace it:** nothing. Reference implementations of every other layer can change; the principal layer is non-transferable.

---

### Edge Layer

The layer of the AI-Native Company that serves the individual human. Each human has one agent at the Edge — a **personal identic agent** (such as OpenClaw) that knows their context, speaks on their behalf, and delegates work downstream.

> 💡 **Analogy:** The Edge Layer is the chief-of-staff floor. One agent per executive, representing them across the company.

---

### AI Workforce Layer

The layer of the AI-Native Company that serves the enterprise. This is where AI Workers (Digital FTEs) live and execute — managed by Paperclip, running on runtime engines, coordinating through specs.

> 💡 **Analogy:** The AI Workforce Layer is the production floor. Many Digital FTEs, each doing specialized work, all coordinated by the management plane.

---

### Delegate

The personal agent at the Edge Layer that holds the principal's context, represents their judgment, carries their authority envelope, and brokers all downstream work on their behalf. Invariant 2 of the thesis. Without a delegate, the human bottleneck returns and scale collapses to typing speed. **OpenClaw** is the reference implementation; any MCP-speaking personal agent that holds identity, context, and authority qualifies.

> 💡 **Analogy:** A CEO's chief of staff. One per executive, knows their priorities, speaks for them, routes work to the right specialists.

_See also:_ **OpenClaw (as Delegate)** below for the reference implementation, and **Identic AI** in Section 1 for the human-sovereignty framing.

---

### OpenClaw (as Delegate)

OpenClaw is the reference implementation of the **delegate** at the Edge Layer — the "chief of staff" agent that represents the human, knows their context, and speaks on their behalf. Every human in an AI-Native Company needs a delegate; OpenClaw is how we build one.

> 🔹 **Example:** When you ask OpenClaw "summarize my week and draft three priorities for Monday," it pulls from your calendar, email, and Slack (tools it's authorized to access), synthesizes an answer in your voice, and waits for you to approve before acting on anything. It is you, at machine speed.

_See also:_ the **OpenClaw** entry earlier in the glossary for the framework itself.

---

### Manager (Management Plane)

The orchestrator that turns a pile of AI Workers into a workforce: assigns work, enforces budgets, approves risky moves, audits execution, keeps the ledger, and exposes hiring as a callable API. Invariant 3 of the thesis. Without it, agents collide, budgets leak, and no one can answer what the workforce cost or produced. **Paperclip** is the reference implementation; any orchestrator meeting the management contract qualifies.

> 💡 **Analogy:** If the delegate is the chief of staff, the manager is the chief operating officer. One-to-one with the human; one-to-many with the workforce.

_See also:_ **Paperclip** below for the reference implementation.

---

### Paperclip

The **management plane** of the AI-Native Company. Paperclip is the COO — it hires Digital FTEs, assigns them work, enforces their budgets, approves risky moves, and keeps the ledger. It exposes hiring as an API that any authorized agent can call, which is how the workforce grows on demand.

> 💡 **Analogy:** If OpenClaw is the chief of staff, Paperclip is the chief operating officer. One-to-one with the human; one-to-many with the workforce.

> 🔹 **Example:** A customer writes in Bahasa Indonesia. No Digital FTE on the roster speaks it. Paperclip detects the capability gap and, within its authority envelope, calls its own hiring API to manufacture a new Bahasa-speaking Digital FTE. The new worker reads the message and replies. No human was woken.

---

### Meta-Layer (Hiring as a Callable Capability)

The layer that exposes hiring as an API any authorized agent can call to provision a new AI Worker at runtime, inside the principal's authority envelope, without waking a human. Invariant 5 of the thesis. Solves the frozen-roster problem: when a capability gap appears (a customer writes in a language no current Worker speaks), the workforce staffs up on demand under policy. **Claude Managed Agents** is the reference implementation; any managed-agent API that can generate an agent and provision its environment at runtime qualifies.

> 🔹 **Example:** The Bahasa Indonesia trace under Paperclip above is the meta-layer firing. Paperclip detects the gap; the meta-layer's hiring API manufactures the new Worker; the Worker is registered with the manager and stays on the roster.

> 📌 **Dual role:** Claude Managed Agents serves as both an engine option (Invariant 4) and the meta-layer (Invariant 5). The same runtime-provisioning capability that runs a Worker also creates new ones, which is why the meta-layer is callable rather than batch-provisioned.

---

### Runtime Engine

The execution substrate a Digital FTE runs on. Each Digital FTE picks its own engine based on what the job demands — not one engine per company. Options include **Dapr Agents** (durable execution for mission-critical work), **Claude Managed Agents** (hosted and operated for you), **OpenAI Agents SDK** (self-hosted, portable), and **OpenClaw-native** (lightweight, fast to deploy). Internally, every engine has two planes: a **harness** (control plane) and a **compute plane** (execution plane / sandbox). See the next two entries.

> 💡 **Analogy:** The runtime engine is the skillset the employee brings to the job. A nurse on a heart-surgery team needs different skills than a nurse at a clinic. Same role, different engine.

---

### Harness (Agent Harness)

The control plane of an agent engine: everything around the model that turns it into a working system. Includes the agent loop, tool dispatch, approvals, tracing, context management, recovery, instructions, skills, and validators. Captured in the practitioner shorthand **Agent = Model + Harness**: the model is the brain you rent from a frontier lab, and the harness is the body, workplace, and standard operating procedure built around it. The compute plane (sandbox) sits next to the harness, not inside it. Credentials stay in the harness while model-generated code runs in the sandbox.

> 💡 **Analogy:** If the model is the CPU and the context window is the RAM, the harness is the operating system: it boots, dispatches drivers (tools), curates context, and manages the agent's lifecycle. Your agent code is the application running on top.

> 🔹 **Examples:** Claude Agent SDK is a harness you assemble. OpenClaw is a harness you extend through skills. Claude Code, Cursor, and Codex are harnesses tuned for coding work. Claude Managed Agents is a harness Anthropic runs for you behind stable interfaces.

> 📌 **Lineage:** The word evolved from _test harness_ (software engineering scaffolding that drives code under test) to _eval harness_ (lm-eval-harness, the scaffolding that drives a model through a benchmark) to _agent harness_ (the scaffolding that drives a model through real-world work). All three are scaffolding around something that does the actual work.

---

### Compute Plane / Sandbox Runtime

The execution plane that sits next to the harness: the secure sandbox where model-generated code actually runs (reads files, executes commands, writes artifacts). Distinct from cloud infrastructure (the metal, Kubernetes, networking) below it and from the harness (the orchestration logic) beside it. The split is load-bearing for security and portability: credentials stay in the harness, model-directed code runs in the sandbox, and the sandbox vendor (E2B, Cloudflare, Daytona, Modal, Runloop, Vercel, Blaxel, or your own Kubernetes) can be swapped without rewriting the agent.

> 🔹 **Example:** OpenAI Agents SDK is the harness; you choose the compute plane separately. Claude Managed Agents fuses both behind one API. Dapr Agents assumes Kubernetes as its compute plane.

> 📌 **Three things called "runtime":** language runtime (Node.js, Python interpreter) is pure infrastructure. Execution runtime / sandbox is this entry. Agent runtime is sometimes used as a synonym for the harness itself. Watch for the conflation when reading vendor docs.

---

### Trigger

The way the outside world calls the AI-Native Company into motion — a schedule comes due, a webhook arrives, an API call lands, a customer walks in. **Claude Code Routines** is the reference implementation: it turns each external event into a session that wakes the delegate and fires the chain. Without triggers, the system only moves when a human types a prompt — which isn't really a company, just an assistant with extra steps.

> 🔹 **Example:** Every Monday at 9 a.m., a scheduled trigger wakes OpenClaw, which asks Paperclip to run the weekly customer-health report. A Digital FTE pulls the data, generates the report, and emails the executive team. The human configured the trigger once; the system runs on its own from then on.

---

### Summary

A one-sentence taxonomy to memorize:

> **The Agent Factory** (process) builds **the AI-Native Company** (output). The AI-Native Company employs **AI Workers** (workforce), who operate across the **Two-Layer Model**: humans at the **Edge Layer** (via OpenClaw, the delegate), Digital FTEs in the **AI Workforce Layer** (managed by Paperclip), each running on a **runtime engine** of its choice, woken by **triggers** from the outside world.

You could add this as the last lin

---

**You now know enough to start reading.** The full glossary below goes deeper into each term and covers 250+ more.

---

---
[⬅ Prev](01-top-30-terms.md) · [Next ➡](03-agent-factory-book-specific-terms.md)
