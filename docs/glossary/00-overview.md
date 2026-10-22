# 00 — Overview: Glossary Kya Hai Aur Kaise Use Karo

Yeh chapter koi "concept" nahi sikhata — yeh book ka **reference dictionary** hai. Poori *The AI
Agent Factory* book mein jo bhi term aayegi (AI se le kar agentic commerce tak), uski precise,
book-ki-apni English definition yahan milegi.

> **Book ka apna disclaimer:** "You don't need a computer science degree to read this book. But
> you do need to speak the language." Yeh glossary har zaroori term plain English, real-life
> examples, aur everyday analogies ke sath define karti hai.

## Kaise Use Karo

1. Pehle **Top 30 Terms** (file `01`) parho — yeh woh terms hain jo book ke har page par milte
   hain.
2. Phir **Architecture: The Runtime Stack** (file `02`) — AI-Native Company ke runtime components
   (AI Worker, Paperclip, OpenClaw, Harness, etc.) ek sath.
3. Baqi 15 numbered files har category ko cover karti hain — jab bhi koi naya term milay, `Ctrl+F`
   se dhoond lo.

Book-specific vocabulary (Agent Factory ki apni coined terms) **sab se pehle** aati hai, kyunke
Chapter 1 se hi yeh terms use hone lagti hain.

## The AI Landscape at a Glance

Book apne intro mein ek simple nesting diagram deti hai (text version, kyunke original diagrams
images hain jo yahan reproduce nahi ki ja sakti):

```
AI ⊃ ML ⊃ DL ⊃ LLMs
(Each is a subset of the one before it)
```

Matlab: **AI** sab se bara umbrella hai (koi bhi computer jo insaani intelligence wala kaam kare).
Uske andar **ML** (Machine Learning — examples se seekhna). Uske andar **DL** (Deep Learning —
neural networks wali ML). Uske andar **LLMs** (Large Language Models — DL ka wo subset jo language
samajhta/generate karta hai). Full detail category 2 (`04-core-ai-and-machine-learning.md`) aur
category 3 (`05-llm-basics.md`) mein hai.

Book ke do aur diagrams hain jo text mein describe hoti hain: "How an LLM generates a response:
from your prompt to the completion" aur "The Agent Factory pipeline: from human intent to working
Digital FTE" — dono ke underlying concepts (Prompt → Completion; Intent → Production Engine →
Outcome) is glossary ke relevant sections mein already defined hain (`01-top-30-terms.md`,
`03-agent-factory-book-specific-terms.md`).

## Scope Note — Is Chapter Mein Projects Nahi Hain

Yeh ek **pure reference chapter** hai (term + definition pairs), isliye yahan koi
`projects/` folder nahi hai — koi scaffold, koi "Done jab" checklist nahi, kyunke practice karne
layak koi concept-exercise nahi hai, sirf vocabulary hai. Agar kisi term ko practically explore
karna ho, uska apna dedicated chapter dekho (jaisa Harness Engineering, Loop Engineering, waghera
— jahan is glossary ke terms action mein aate hain).
