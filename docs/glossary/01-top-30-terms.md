# 01 — Top 30 Terms You Must Know First

Yeh **30 terms** poori book mein har page par milti hain — Chapter 1 kholne se pehle yeh parho. English definitions + book ke apne examples/analogies **verbatim** rakhe gaye hain (precision ke liye, glossary ka point hi yeh hai).

---

These appear on almost every page. Read these before you open Chapter 1.

Note: terms related to agents as buyers (ACP, AP2, x402, MPP, authority envelopes, signed mandates) are covered in Section 11 and not included in Top 30 terms.

---

**1. AI (Artificial Intelligence)**: Making computers do things that normally require human intelligence.

> 🔹 When your phone's keyboard predicts the next word you're typing, that's AI.

**2. LLM (Large Language Model)**: A giant AI system trained on billions of pages of text, capable of understanding and generating human language and code. Claude, GPT, and Gemini are LLMs.

> 💡 Think of an LLM as a research assistant who has read every book in the world's largest library. You ask a question, they answer from everything they've read.

**3. Agent (AI Agent)**: An AI that doesn't just answer questions. It takes action, makes plans, and gets things done on its own.

> 🔹 A chatbot answers "What's the cheapest flight to Dubai?" An agent actually searches airlines, compares prices, and books the ticket for you.

**4. Agentic AI**: The category of AI focused on building agents that plan, reason, and act autonomously. This is the frontier of AI in 2026 and the focus of this entire book.

> 🔹 Regular AI: you ask a question, you get an answer. Agentic AI: you give it a goal ("reduce customer churn by 15%") and it researches, plans, executes, and reports back, making decisions along the way.

**5. Digital FTE (Digital Full-Time Equivalent)**: An "AI employee" that does the continuous work of a full-time human worker, 24/7, at a fraction of the cost. Also called an AI Worker in the thesis — same role, different register.

> 🔹 A Digital FTE for customer support handles 500 conversations per day, every day — doing the work of 5-10 human agents.

**6. Agent Factory**: The central concept of this book. The spec-driven, human-supervised, Claude-Code-powered **process** by which AI Workers are designed, manufactured, and deployed. Not a product you buy; a practice you adopt. The Agent Factory builds the AI-Native Company, and the AI-Native Company employs Digital FTEs.

> 💡 Like an assembly line: each station performs one specialized task, parts move through in order, and what emerges at the end is a finished product built to spec. The Agent Factory industrializes the making of AI employees.

**7. Prompt**: The instruction or question you type into an AI model.

> 🔹 "Summarize this report in three bullet points" is a prompt. Better prompts = better answers.

**8. Context Window**: The AI's "working memory": how much text it can read and think about at one time.

> 💡 A small context window is like a tiny desk where you can only spread out a few pages. Claude's large context window is like a huge conference table where you can lay out an entire novel at once.

**9. Token**: The basic unit of text an LLM reads. Roughly ¾ of a word. "I love biryani" ≈ 4 tokens.

> 🔹 You pay per token when using AI APIs. A full page of text ≈ 500-700 tokens.

**10. Hallucination**: When AI confidently generates something that isn't true.

> 🔹 You ask about a Supreme Court case and the AI invents a fake judgment with fake citation numbers, and presents it as fact. It sounds right, but it's fabricated.

**11. Spec (Specification)**: A detailed blueprint describing exactly what you want built: goals, inputs, outputs, constraints.

> 💡 An architect's blueprint for a house. No builder starts by guessing. They follow the plan. In AI development, the spec is that plan.

**12. Spec-Driven Development (SDD)**: Write the blueprint first, then let AI generate the code, tests, and documentation from that blueprint.

> 🔹 You write: "Build an API for a bookstore with endpoints for listing, adding, searching, and deleting books." Claude Code generates the entire application.

**13. Claude Code**: Anthropic's AI coding agent. You talk to it in the terminal and it reads your entire codebase, understands your project, and writes code.

> 🔹 You type "Add user authentication to my app": Claude Code reads your existing code, generates the auth module, writes tests, and integrates everything.

**14. Cowork**: Anthropic's desktop agent for non-coding knowledge tasks: documents, research, file management.

> 🔹 "Organize my Downloads folder by project and summarize all PDFs from this month." Cowork does it while you focus on other things.

**15. MCP (Model Context Protocol)**: The universal standard that lets any AI agent connect to any external tool: databases, email, calendars, file systems. MCP is the protocol for agents calling tools. For the separate protocol family that handles agents paying for those tools, see Section 11: ACP, AP2, x402, and MPP.

> 💡 Before USB, every phone had a different charger. MCP is the "USB standard" for AI: one protocol that lets any agent plug into any tool.

**16. API (Application Programming Interface)**: Rules that let different software programs talk to each other. APIs are how agents interact with the outside world.

> 💡 A restaurant menu is an API. You (client) look at the menu (docs), place an order (request), and the kitchen (server) delivers your food (response).

**17. SDK (Software Development Kit)**: A pre-built toolkit for building applications on a specific platform.

> 💡 An SDK is like a LEGO set: pre-made pieces with instructions so you can build things quickly, instead of carving every piece from scratch.

**18. Python**: The most popular programming language in AI. Readable, versatile, and the primary language in this book.

> 🔹 Python reads almost like English: `if age > 18: print("Adult")`. This readability is why the AI world chose Python.

**19. Git**: A system that records every change to your code: who changed what, when, and why. You can always go back to any previous version.

> 💡 "Track Changes" in Microsoft Word, but for entire software projects. Every edit is recoverable.

**20. Docker**: A tool that packages your app into a portable box (container) that runs identically anywhere: your laptop, a colleague's machine, or a cloud server.

> 💡 A shipping container. Whether it's on a truck in Karachi or a ship in the ocean, the contents inside are identical and self-contained.

**21. Context Engineering**: Designing the full information environment an agent receives. The #1 skill that separates a $2,000/month agent from one nobody wants.

> 💡 A Toyota factory has quality controls ensuring every car meets spec. Context engineering is quality control for your AI agents: ensuring consistent, reliable output.

**22. Tool Use**: An agent's ability to use external tools (searching the web, querying databases, sending emails) rather than just answering from memory.

> 🔹 You ask "What's the weather in Karachi?": an agent with tool use actually checks a weather service and gives live data. Without tool use, it would just guess.

**23. Guardrails**: Safety constraints that prevent an agent from doing things it shouldn't.

> 🔹 A financial agent has a guardrail: no transactions above Rs. 5,000,000 without human approval. Like the barriers on a motorway that keep cars from going off the road.

**24. RAG (Retrieval-Augmented Generation)**: Giving AI access to external documents so it answers from facts, not from (potentially wrong) memory.

> 💡 Taking an open-book exam instead of a closed-book exam. The AI looks up facts in your documents before answering: much more accurate.

**25. 10-80-10 Rule**: The [operating rhythm of the AI workforce](https://agentfactory.panaversity.org/docs/thesis#the-10-80-10-rule-the-operating-rhythm-of-the-ai-workforce): human sets direction (10%) → AI executes (80%) → human verifies (10%).

> 🔹 You write a project brief (10%), Claude Code builds the entire application (80%), you review, test, and approve (10%). The industry calls these two postures **human in the loop** (you approve each action) and **human on the loop** (the system acts, you watch and can intervene) — see HITL and HOTL in Section 5.

**26. AGENTS.md / CLAUDE.md**: Configuration files that tell your AI agent the rules of your project: coding standards, preferences, architectural decisions.

> 💡 The onboarding document you give a new employee: "Here's how we work. Here's our style. Here's what we never do." Loaded into every interaction.

**27. Orchestration**: Coordinating multiple agents to work together on a task.

> 💡 A cricket team captain positions fielders, sets bowling rotations, and adjusts strategy. They don't do everything themselves; they coordinate specialists toward a shared goal.

**28. Stateless**: The AI forgets everything between conversations. Every new chat starts from absolute zero.

> 💡 A shopkeeper with amnesia: every time you walk in, they greet you as a stranger, even if you were there 5 minutes ago. Chat apps create the _illusion_ of memory by re-sending the full conversation each time.

**29. Deployment**: Making your application live and available to real users on the internet.

> 🔹 Your app works on your laptop. Deployment puts it on a cloud server so 10,000 people can use it simultaneously.

**30. CI/CD (Continuous Integration / Continuous Delivery)**: Automatically testing and deploying code every time a developer makes a change.

> 🔹 A developer pushes code at 2 PM. Tests run automatically in 3 minutes. All pass. The new version is live by 2:10 PM: zero manual steps.

---

---
[⬅ Prev](00-overview.md) · [Next ➡](02-architecture-runtime-stack.md)
