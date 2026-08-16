# Give Your AI Searchable Context: RAG on Postgres with pgvector

*Source: The AI Agent Factory — "Give Your AI Searchable Context: RAG on Postgres with pgvector — A Crash Course" (Panaversity)*
*URL: https://agentfactory.panaversity.org/docs/postgres-ai-crash-course*
*Group: Mode 2 — Manufacturing, Phase 1 · Building Blocks (Chapter 3 of 6)*

---

## Yeh Course Kis Baare Mein Hai

**15 Concepts · 80% of Real Use · Aapka agent banata hai, aap haath se nahi.** Imagine karo aap
computer se kahen: "Yeh documents ka folder lo, ek database banao jo unke **meaning** ko samjhe, aur
mujhe aisi search do ke 'the city that never sleeps' poochne se New York ke quotes milein — chahe woh
kabhi 'New York' naam na len." **Yeh course yehi banata hai.**

**Ek idea poore course ko click karati hai:** AI model ek waqt mein sirf itna hi dhyan de sakta hai jo
uski **context window** mein fit ho, aur jitni zyada irrelevant cheez ho, jawab utna hi kharab. Har AI
system ka core kaam hai: **sahi information sahi waqt par model ke saamne lana, baaki sab bahar rakhna.**
Aap yeh apne coding agent ke liye khud karte ho (rules file, sirf zaroori files). Vector database yehi
kaam app ke users ke liye **khud-b-khud** karta hai. **Isi ka naam hai RAG (Retrieval-Augmented
Generation) — yeh context management hai, ek layer neeche.**

**Bara claim:** zyada tar applications ke liye, **Postgres hi AI database hai.** Alag, specialized vector
database ek aur system hai jo pay, sync, aur maintain karna parta hai. Vectors unhi data ke paas rehne
chahiye jinko woh describe karte hain.

## Parts

1. [Foundations — Mindset, Vectors, Extensions, Neon Setup (Concepts 1-4)](00-foundations.md)
2. [Pehla RAG — Schema, Embedding Worker, Chunking, Search (Concepts 5-9)](01-first-rag.md)
3. [Search Ko Fast Banana — Indexes (Concepts 10-11)](02-making-search-fast.md)
4. [Search Ko Achha Banana — Evals, Filters, Hybrid, Multi-Tenancy (Concepts 12-15)](03-making-search-good.md)
5. [Worked Example + MCP Tool + Deployment + Agent (Parts 5-8)](04-shipping-and-next.md)

---

## Aapka Job Kya Hai

Sabse common misconception: *AI applications banane ke liye machine-learning team chahiye.* Nahi.
Models off-the-shelf hain. Infrastructure aisa database hai jo aap shayad already chalate ho. **Aapki
value stack mein upar move hoti hai** — `CREATE INDEX` type karne se, **kaunsa** index chahiye decide
karne tak; query likhne se, result achha hai ya nahi judge karne tak.

*Yeh summary poore course (Foundations + First RAG + Fast Search + Good Search + Worked Example +
MCP Tool + Deployment + Agent Handoff) ka overview hai.*
