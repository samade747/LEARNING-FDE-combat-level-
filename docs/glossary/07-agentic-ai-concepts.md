# 07 — 5. Agentic AI Concepts

Agents kaise plan karte, act karte, aur decide karte hain — is book ka core subject.

---

The heart of this book: AI systems that don't just answer questions, but take action.

### Agent (or AI Agent)

An AI system that can independently perceive its environment, make decisions, and take actions to achieve a goal, without a human guiding every step.

> 🔹 **Example:** A chatbot just answers questions. An AI agent receives a goal like "find me the cheapest Karachi-to-Dubai flight next Friday" and then searches airlines, compares prices, checks your calendar, and books the ticket, all on its own.

> 💡 **Analogy:** A chatbot is a librarian who answers questions from behind a desk. An agent is a personal assistant who takes your request and goes out into the world to get things done.


### Agentic AI

The category of AI focused on building agents that plan, reason, act, and adapt autonomously. This is the frontier of AI in 2026.

### General Agent

An AI agent used through natural language for a wide range of tasks. It isn't built for one specific job; it's a versatile "Swiss Army knife" that can help with coding, writing, research, file management, and more.

> 🔹 **Example:** Claude Code is a general agent: you can ask it to organize files, write an API, analyze a spreadsheet, or debug a Python error. It adapts to whatever you need, using natural language instructions.

> 💡 **Analogy:** A general agent is like a highly capable executive assistant. You don't hire them for one task; you give them different assignments each day, and they figure out how to get each one done.

### Autonomy

The degree to which an AI agent can operate independently without human approval at every step.

> 💡 **Analogy:** A junior employee who needs permission for every email has low autonomy. A senior director who makes decisions independently has high autonomy. Agents exist on this same spectrum: some need human approval for every action; others operate with full independence within defined boundaries.

### Reasoning

An agent's ability to think through a problem logically: analyzing information, weighing options, and drawing conclusions before acting.

> 🔹 **Example:** You ask an agent: "Should we launch in Lahore or Islamabad first?" A non-reasoning agent might just pick one. A reasoning agent analyzes: "Lahore has 2x the population, but Islamabad has higher per-capita income. Your product targets professionals, so Islamabad's demographics are a better fit. I recommend Islamabad first, then Lahore in month 3."

### Acting

When an agent actually does something in the real world: sending an email, writing a file, querying an API, placing an order, booking an appointment.

### Planning

An agent's ability to break a complex goal into a sequence of steps and determine the order to execute them.

> 🔹 **Example:** You tell an agent: "Prepare a market analysis report on Pakistani cement exports." The agent plans: (1) search for export data, (2) gather competitor info, (3) analyze trends, (4) write the report, (5) format and export as PDF.

### Task Decomposition

Breaking a large, complex task into smaller, manageable subtasks that can be solved individually.

> 💡 **Analogy:** "Plan a wedding" is overwhelming as one task. Decomposed: find a venue, choose a caterer, design invitations, arrange flowers, hire a photographer. Each subtask is solvable. AI agents decompose complex goals the same way.

### Orchestration

Coordinating multiple agents or tools to work together, managing the flow of information between them.

> 💡 **Analogy:** A cricket team captain doesn't bowl, bat, and field all at once. They position fielders, set bowling rotations, and adjust strategy based on the match situation. Agent orchestration works similarly: coordinating specialists toward a shared goal.

### Multi-Agent System

A system where multiple AI agents collaborate (each handling different parts of a task) to accomplish something none could do alone.

> 🔹 **Example:** One agent researches competitor pricing, another drafts the analysis, a third formats the slides, and a fourth prepares speaker notes. They work as a team.


### Supervisor Agent

An agent whose job is to coordinate and manage other agents: distributing tasks, monitoring progress, and collecting results.

> 💡 **Analogy:** A construction site foreman. They don't lay bricks or wire outlets. They assign specialists to each task, check quality, and make sure everything comes together correctly.

### Handoff

When one agent passes a task (and its context) to another agent, like a relay runner passing the baton to the next.

### Tool Use / Function Calling

An agent's ability to use external tools (searching the web, querying databases, sending emails, running code) rather than just generating text from memory.

> 💡 **Analogy:** A person answering questions only from memory vs. a person who can pick up a phone, open a laptop, and look things up. Tool use gives the agent access to the world beyond its training data.

### State

The current condition or data of a system at any given moment. "Maintaining state" means remembering where things stand in an ongoing process.

> 🔹 **Example:** You're filling a 10-page NADRA form online and you're on page 7. The "state" includes everything you've entered on pages 1-6 plus which page you're currently on.

### Memory (Agent Memory)

Mechanisms that let an agent remember information across interactions: previous conversations, user preferences, or learned facts.

> 💡 **Analogy:** **State** is short-term memory (what's happening right now in this conversation). Memory is long-term memory (what happened across past conversations). Without memory, every interaction starts from zero.

### Session

A single continuous interaction between a user and an AI system. Starting a new chat = starting a new session.

### Reflection

When an agent reviews its own output, identifies mistakes or weaknesses, and tries again with improvements.

> 💡 **Analogy:** A writer who finishes a draft, re-reads it, notices weak arguments, and revises before submitting. The agent does this automatically.

### Retry / Fallback

**Retry:** Attempting the same action again when it fails (maybe the server was temporarily unavailable). **Fallback:** Switching to an alternative approach when the primary one keeps failing.

> 🔹 **Example:** Agent tries to fetch data from a website. Site is down (retry: try again in 30 seconds). Still down after 3 retries (fallback: try a different data source for the same information).

### Guardrails

Safety constraints preventing an agent from taking harmful, inappropriate, or unauthorized actions. The financial version of guardrails — spending limits, vendor allowlists, audit triggers — is the authority envelope. See Section 11.

> 🔹 **Example:** A financial agent has a guardrail preventing transactions above Rs. 5,000,000 without human approval. A customer service agent has a guardrail preventing it from making promises about refunds it can't guarantee.

> 💡 **Analogy:** Guardrails on the Motorway keep cars from going off the road. AI guardrails keep agents from going off-limits.

### HITL (Human in the Loop)

A design pattern where a human must review, approve, or intervene at critical points in an agent's workflow. Nothing critical happens without the human's sign-off.

> 🔹 **Example:** An agent drafts a client email, but it's not sent until a human reads and approves it. The agent does the 80% of the work; the human provides the 10% of verification.

### HOTL (Human on the Loop)

A design pattern where the agent acts autonomously while a human monitors and can intervene, but doesn't approve each action. Faster and more scalable than HITL; safe only when the checker is strong and mistakes are cheap to reverse. See the [Loop Engineering crash course](/docs/loop-engineering-crash-course#human-in-on-the-loop) for how to set the mix per action.

> 💡 **Analogy:** HITL is a driving instructor with their own brake pedal, approving every move. HOTL is a supervisor watching the security cameras — the work runs on its own, and they step in only when something looks wrong.

> 🔹 **Example:** A morning-triage loop opens PRs to `claude/` branches all night on its own (on the loop), but a human reviews and merges each morning (back in the loop at the gate). A third term, **human out of the loop** — no monitoring, no intervention — is not a design option in this book; it is the failure mode that happens by drift when you stop reading what ships.

### Reliability

How consistently an agent produces correct, expected results. A reliable agent gets it right 99 out of 100 times, not 60.

> 🔹 **Example:** A reliable invoice-processing agent correctly extracts vendor name, amount, due date, and tax from 99% of invoices, across different formats, languages, and layouts. An unreliable one gets confused by unusual layouts and misreads amounts 20% of the time. The difference between a sellable product and a liability.

### Verifiability

The ability to check and confirm that an agent's output is correct, that its code passes tests, its numbers add up, its references exist.

### Auditability

The ability to trace back through every decision and action an agent took, understanding exactly what it did and why.

> 💡 **Analogy:** A bank statement traces every transaction. An audit trail for an AI agent traces every decision, tool call, and output, all critical for compliance and debugging.

### Workflow

A defined sequence of steps an agent follows to complete a task from start to finish.

> 💡 **Analogy:** A workflow is like a recipe: step-by-step instructions that, followed correctly, produce a predictable result.

---

---
[⬅ Prev](06-knowledge-retrieval-and-context.md) · [Next ➡](08-programming-and-software-terms.md)
