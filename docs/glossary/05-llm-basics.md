# 05 — 3. LLM Basics

Large Language Models kaise kaam karte hain — tokens, context windows, waghera.

---

LLMs are the engines powering every AI agent in this book. This section explains how they work at a practical level.

### LLM (Large Language Model)

A very large AI model trained on vast amounts of text that can understand and generate human-like language and code. Claude, GPT-4, and Gemini are all LLMs.

> 💡 **Analogy:** An LLM is like an incredibly well-read research assistant who has read every Wikipedia article, millions of books, and billions of web pages. You can ask them about almost anything, and they'll draw on that reading to help: writing, analysis, code, translation, and more.

### Prompt

The input you give to an AI model: your question, instruction, or request. The quality of your prompt directly affects the quality of the response.

> 🔹 **Example:** "Write something about marketing" is a weak prompt. "Write a 500-word LinkedIn post about why Pakistani textile exporters should use AI agents for order tracking, in a professional but conversational tone" is a strong prompt.

### System Prompt

Hidden instructions given to an AI before your conversation starts. Set by the developer, not the user. They shape the model's personality, behavior, and constraints.

> 🔹 **Example:** A banking chatbot's system prompt might say: "You are a helpful assistant for HBL. Answer in Urdu or English based on the customer's language. Never reveal account balances without OTP verification. If asked about loans, direct to the loans page."

> 💡 **Analogy:** A system prompt is like a manager's briefing to a new employee on day one: "Here's who we are, here's how we talk to customers, here's what you must never do."

### User Prompt

The message you (the user) actually type. This is your side of the conversation.

### Instruction

A specific directive within a prompt telling the model what to do.

> 🔹 **Example:** "Summarize this in three bullet points," "Translate to Urdu," "Fix the bug in this code", each is a clear instruction.

### Context

All the information available to a model during a conversation: the system prompt, conversation history, uploaded documents, and your current message combined.

> 💡 **Analogy:** When you ask a colleague for advice on a deal, the "context" is everything they know: the client history, previous emails, the contract terms, your company's policies. The more relevant context, the better the advice.

### Context Window

The maximum amount of text an LLM can process at once, measured in **tokens**. Think of it as the model's "working memory."

> 🔹 **Example:** Claude models offer context windows ranging from 200,000 to over 1 million tokens. Even 200,000 tokens is roughly 150,000 words (an entire novel). Older models might handle only 4,000 tokens (a few pages).

> 💡 **Analogy:** A context window is like the size of a desk. A small desk holds only a few papers, and you keep removing old ones to make room. A huge desk lets you spread out an entire project and see everything at once. Bigger context window = bigger desk.


### Token

The basic unit of text an LLM processes. A token is roughly ¾ of a word. Short words like "the" are one token. Longer words like "unbelievable" get split into 3-4 tokens. Spaces and punctuation also consume tokens.

> 🔹 **Example:** "I love biryani" ≈ 4 tokens. A full page of text ≈ 500-700 tokens. You're charged per token when using AI APIs.

### Completion / Generation

The output an LLM produces in response to your prompt. When the model "completes" your request, that response is the completion.

### Structured Output

When an LLM generates its response in a specific, machine-readable format (like **JSON**) instead of conversational text, so other software can easily process it.

> 🔹 **Example:** Instead of "The temperature in Karachi is 35 degrees and it's sunny," a structured output would be: `{"city": "Karachi", "temp": 35, "condition": "sunny"}`. Software reads this format effortlessly.

### Hallucination

When an AI model confidently generates false, inaccurate, or fabricated information, presenting it as fact.

> 🔹 **Example:** You ask about a Supreme Court judgment and the model invents a case (complete with fake citation numbers and a fake bench) and presents it as real.

> 💡 **Analogy:** A student who doesn't know the answer on an exam but writes a very confident, detailed response anyway. It reads like it's correct, but it's entirely made up.

### Grounding

Connecting an AI model to factual, verified data sources so it gives accurate answers instead of hallucinating.

> 💡 **Analogy:** Grounding is like letting a student use their textbook during an exam. Now their answers are based on real information, not unreliable memory.

### Temperature

A setting that controls creativity vs. predictability in an LLM's responses. Low temperature (0) = very consistent. High temperature (1+) = more creative and varied.

> 💡 **Analogy:** Temperature is like a chef's freedom in the kitchen. Temperature 0: "Follow the recipe exactly, no substitutions." Temperature 1: "Improvise freely." You want exact recipes for medication dosages, but creative freedom for a new dish.

### Latency

The time delay between sending a request and receiving a response. Lower latency = faster. Measured in milliseconds or seconds.

> 🔹 **Example:** If Claude responds in 1 second, that's low latency. If it takes 15 seconds, that's high latency. Users get impatient beyond 2-3 seconds.

### Throughput

How many requests a system can handle per unit of time. High throughput = serving many users simultaneously.

> 💡 **Analogy:** Latency is how fast one car passes through a toll plaza. Throughput is how many cars the toll plaza handles per hour. You want both low latency and high throughput.

### Deterministic vs. Non-Deterministic

**Deterministic:** Same input always produces the exact same output (like a calculator: 2+2 always equals 4). **Non-deterministic:** Same input can produce different outputs each time.

LLMs are non-deterministic: ask the same question twice, and you may get slightly different (but equally valid) answers. This isn't a bug; it's fundamental to how the technology works.

### Stateless

Having no memory between separate interactions. Each new conversation with an LLM starts from absolute zero: the model has no knowledge of any previous conversation.

> 💡 **Analogy:** A shopkeeper with amnesia. Every time you walk in, they greet you as a stranger, even if you were there five minutes ago. Chat apps create the _illusion_ of memory by re-sending the entire conversation history with every message.


### Prompt Engineering

The skill of crafting clear, specific instructions to get the best possible output from an AI model. Not just "what you ask" but "how you ask it."

> 🔹 **Example:** Instead of "Write about AI," a prompt engineer writes: "You are a technology journalist writing for Dawn newspaper. Write a 600-word article explaining how Pakistani banks are using AI agents for fraud detection. Include one real example. Use simple language accessible to a non-technical business reader."

### NLP (Natural Language Processing)

The branch of AI dealing with understanding, interpreting, and generating human language, the foundation that makes LLMs possible.

> 🔹 **Example:** When you type a search query in broken English and Google still understands what you meant, that's NLP at work.

### Copilot

An AI assistant integrated into a software environment (like a code editor) that works alongside you to boost productivity, suggesting, auto-completing, and reviewing as you work.

> 🔹 **Example:** GitHub Copilot suggests code as you type. It's like having a knowledgeable colleague looking over your shoulder, finishing your sentences.

---

---
[⬅ Prev](04-core-ai-and-machine-learning.md) · [Next ➡](06-knowledge-retrieval-and-context.md)
