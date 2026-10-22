# 06 — 4. Knowledge, Retrieval, and Context

RAG, vector databases, aur AI ko sahi information dene ki vocabulary.

---

These terms describe how AI agents access and use external knowledge for better, more accurate answers.

### RAG (Retrieval-Augmented Generation)

A technique where an AI first retrieves relevant information from external documents or databases, then uses that information to generate a more accurate response.

> 💡 **Analogy:** Taking an open-book exam. Instead of relying only on memorized (possibly wrong) knowledge, you look up specific facts in your reference material before writing your answer. RAG gives AI its own reference library.


### Embedding

Converting text into numerical coordinates so a computer can measure how similar different pieces of text are, capturing meaning, not just keywords.

> 💡 **Analogy:** Imagine placing every book in a library on a giant map where similar books cluster together. Cookbooks sit near each other, far from physics textbooks. Embeddings create this "similarity map" in mathematical space.

### Vector

A list of numbers representing a piece of text in mathematical space. When text is converted to an embedding, the result is a vector.

> 🔹 **Example:** The word "cricket" might become `[0.8, 0.3, 0.7, 0.1, ...]`: a long list of numbers that captures both the sport and the insect meanings, distinguished by surrounding context.

### Vector Database

A specialized database for storing and quickly searching vectors, finding similar content by meaning rather than exact keyword match.


> 🔹 **Example:** You store 10,000 company documents as vectors. When someone asks "What's our return policy?" the vector database finds the most relevant documents instantly, even if none of them contain the exact phrase "return policy."

> 💡 **Analogy:** A traditional database searches by exact keywords (like searching a phonebook by name). A vector database searches by meaning (like asking a librarian "find me books similar to this one").

### Semantic Search

Searching by meaning rather than exact keywords. "How do I return a product?" matches a document titled "Refund Process" even though the words are completely different.

> 🔹 **Example:** An employee searches "how to take time off" in the company knowledge base. Semantic search finds the document titled "Annual Leave Policy and Procedures", even though none of the search words appear in the title. Traditional keyword search would find nothing.

### Retrieval

Fetching relevant information from a data source (database, document collection, the web) for an AI to use in generating a response.

> 🔹 **Example:** A customer asks your support agent "What's your warranty on laptops?" The agent retrieves the warranty policy document from your knowledge base, reads the relevant section, and generates an accurate answer based on your actual policy; not a guess.

### Reranking

After retrieving multiple results, re-ordering them by relevance so the most useful result appears first: a quality filter after the initial search.

### Chunking / Chunk

Breaking a large document into smaller pieces so they can be stored and searched individually.

> 🔹 **Example:** A 200-page HR manual is split into paragraph-sized chunks. When someone asks about leave policy, the system retrieves only the 3-4 most relevant paragraphs, not the entire manual.

### Knowledge Base

An organized collection of information (documents, FAQs, manuals, policies) that an AI can search and reference.

> 🔹 **Example:** A company's internal wiki containing product docs, HR policies, and training materials, structured so an AI agent can find answers instantly.

### Grounding Data

The specific factual data connected to an AI model to ensure accurate, fact-based responses rather than hallucinated guesses.

### MCP (Model Context Protocol)

An open standard (created by Anthropic, now governed by the Linux Foundation) that lets any AI agent connect to any external tool using a universal protocol: search, databases, email, calendars, file systems. MCP is the protocol for agents calling tools. For the separate protocol family that handles agents paying for those tools, see Section 11: ACP, AP2, x402, and MPP.

> 💡 **Analogy:** Before USB, every phone had a different charger. USB became the universal connector. MCP is the "USB standard" for AI agents: one protocol that lets any agent plug into any tool. Build your agent once, connect it to everything.


### Connector

A specific integration linking an AI agent to an external service using **MCP** or another protocol.

> 🔹 **Example:** A "Gmail connector" lets an AI agent read, search, and send emails. A "Google Drive connector" lets it read and create documents.

### System Integration

Connecting different software systems so they share data and work together seamlessly: the "plumbing" behind any enterprise agent deployment.

> 🔹 **Example:** Your Digital FTE needs to read customer data from Salesforce, check inventory in SAP, process payments through JazzCash, and send confirmations via email. System integration connects all four systems so the agent can work across them in a single workflow.

---

---
[⬅ Prev](05-llm-basics.md) · [Next ➡](07-agentic-ai-concepts.md)
