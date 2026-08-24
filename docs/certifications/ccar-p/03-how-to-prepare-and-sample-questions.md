# 03 — How to Prepare + Sample Questions (Full Text, Section 7-8)

## How to Prepare (Official Guide, Section 7)

**Koi single required course nahi hai. Anthropic yeh guarantee nahi karta ke koi ek resource pass
result ensure karega.** Candidates ko hands-on experience ko in resources ke sath combine karna
recommend kiya jata hai:

- Section 6 ka exam blueprint study karo aur har objective ke against khud ko self-assess karo
- Official Anthropic documentation review karo — Claude API, models, prompt engineering, MCP, aur Skills
- **Kam se kam ek end-to-end Claude solution build aur operate karo** — RAG, evaluation, aur
  observability sameet
- Architectural decision-making practice karo: model selection, integration protocols, aur security
  tradeoffs
- Section 8 ke sample questions complete karo item-style se familiar hone ke liye

## Sample Questions (Full Text, Correct Answer + Rationale)

Guide khud kehta hai: *"Yeh illustrative items exam ka style aur cognitive level dikhate hain. Live
item bank se nahi liye gaye."*

### Sample 1 — Domain 3, Integration

> Ek team ek customer-support agent expose karti hai jo tickets read kar sakta hai, replies draft kar
> sakta hai, refunds issue kar sakta hai, aur user accounts delete kar sakta hai. Support staff ko
> sirf tickets read karna aur replies draft karna chahiye hota hai. Least-privilege principles apply
> karke, kaunsa change risk sab se zyada reduce karta hai?

- A. Refund aur delete tools mein logging add karo taake misuse baad mein audit ho sake
- B. Refund aur delete tools ko agent ke configuration se **poori tarah remove** karo
- C. Sab tools rakho lekin refunds/deletions se pehle confirmation prompt add karo
- D. Agent ko ek bara model se replace karo jo instructions zyada reliably follow kare

**Sahi jawab: B.** Least privilege ka matlab hai wo capabilities remove karna jo role ko chahiye hi
nahi — attack surface **eliminate** karna, sirf monitor ya guard karna nahi. Logging (A) aur
confirmations (C) **detective/compensating controls** hain, unnecessary privilege ka removal nahi;
model size (D) authorization scope se unrelated hai.

### Sample 2 — Domain 2, Models, Prompting & Context

> Ek application har request pe wahi 8,000-token system prompt aur policy document bhejta hai, uske
> baad ek chhota, varying user message. Latency aur cost dono concerns hain. Kaunsa optimization dono
> ko sab se directly address karta hai?

- A. Policy document ko pehle 1,000 tokens tak truncate karo
- B. Task fit se qatai matlab na rakhte hue sab se chhote available model pe switch karo
- C. Static system prompt aur policy ko dynamic content se **pehle rakho** aur **prompt caching enable**
  karo
- D. Policy document ko few-shot example block mein move karo

**Sahi jawab: C.** Stable content ko pehle order karna aur prompt caching enable karna repeated
prefixes ko reuse hone deta hai — time-to-first-token aur per-request cost dono kam hota hai, bina
zaroori context discard kiye. Truncation (A) zaroori policy kho deta hai; blindly downsizing (B)
quality risk karta hai; few-shot mein relocate karna (D) ek cacheable, reusable prefix create nahi
karta.

### Sample 3 — Domain 4, Evaluation & Optimization

> Ek RAG system document refresh ke baad achanak confident lekin **incorrect** answers dena shuru kar
> deta hai, jabke latency aur model version unchanged hain. Sab se pehle investigate karne ki sab se
> likely jagah kya hai?

- A. Model weights silently change ho gaye hain
- B. Retrieval/indexing step irrelevant ya stale chunks return kar raha hai
- C. Temperature setting bohat kam hai
- D. Context window shrink ho gaya hai

**Sahi jawab: B.** Document refresh ke baad confident-but-wrong answers, jabke model aur latency
unchanged hain — yeh retrieval ka model ko poor context dena point karta hai, jaise ek broken re-index
ya mismatched embeddings. Baaqi options specifically document-refresh se trigger nahi hote.

---
[⬅ 02 — Book Coverage & Scope](02-book-coverage-and-scope.md) · [Next: 04 — Policies, Resources & Doc Control ➡](04-policies-resources-and-doc-control.md)
