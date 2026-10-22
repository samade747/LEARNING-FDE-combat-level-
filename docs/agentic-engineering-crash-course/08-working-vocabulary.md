# 08 — The Working Vocabulary

Precise vocabulary reasoning speed badati hai. Poora reference [Dictionary of AI Coding](https://github.com/mattpocock/dictionary-of-ai-coding)
hai; neeche wala subset is poori book parhne/likhne ke liye minimum hai.

| Term | Matlab |
| --- | --- |
| **Model** | Parameters. Stateless. Sirf next-token prediction karta hai. |
| **Harness** | Model ke around sab kuch jo usay agent banata hai: tools, system prompt, context-window management, permissions. Claude Code ek harness hai; OpenCode ek harness hai. |
| **Agent** | Model + harness, context window + tools ke sath operate karta hai. Jis se tum asal mein baat karte ho. |
| **Context window** | Fixed-size view jo model har request par dekhta hai. Finite. Model jo bhi perceive karta hai usi se. |
| **Smart zone / dumb zone** | Early-session region jahan attention sharp hai / late-session region jahan diluted hai. |
| **Hallucination** | Confidently-wrong output. *Factuality* hallucinations parametric-knowledge gaps se; *faithfulness* hallucinations dumb-zone drift se — fixes alag hain. |
| **Clearing** | Session khatam, naya shuru. Hard reset. Agent ko known state par wapis le jata hai. |
| **Compaction** | Session summarize karna naya seed karne ke liye. Lossy — kuch dumb-zone reasoning preserve karti hai. |
| **Handoff** | Context ek session se doosri tak artifact (PRD, ticket, CONTEXT.md) ke zariye transfer karna. |
| **AFK** | "Away from keyboard" — session kick off karo, sandbox mein unattended chalne do. |
| **Skill** | `SKILL.md` file ki tarah bundled teachable capability. On-demand loaded. Progressive disclosure ki unit. |
| **Tracer bullet / vertical slice** | Ek issue jo system ke har layer se ek thin path end-to-end ship karta hai. |
| **Deep module** | Chhota interface + bara internal implementation. Yehi shape AI codebases ko scalable banati hai. |
| **Design concept** | Jo banaya ja raha hai uska shared, ephemeral idea — user aur agent ke beech common. Asset nahi hai. |
| **Grilling** | Design concept banane ki technique — agent user ko Socratically interview karta hai, ek decision at a time. |
| **Vibe coding** | Agent code bina human review ke accept karna. "Low-quality coding" se alag — term review-stance naam deta hai, output nahi. |
| **Agentic engineering** | Agents ko production work mein use karne ka discipline **jabke professional software ka quality bar preserve ho.** Vibe coding ka opposite stance: floor raised, ceiling held. |
| **Jagged intelligence** | Empirical fact ke LLM capability sharply peak karti hai jahan labs verifiable RL se train kiya (math, code), aur stagnate hoti hai baaqi jagah. Jo agent 100k lines refactor kar sakta hai, wahi 50m door car-wash tak chalne ki advice de sakta hai. |
| **On distribution** | Model ki training data mein well-represented hona, isliye competently handled hona. Fresh shuru karte waqt, stack choose karo jahan model already strong hai. |
| **Loop / Routine** | Persistent ambient agent — schedule par invoke hone wala fresh session (cron locally; "routine" server-side) ek chhoti standing job ke against. Har tick stateless hai; **role** prompt mein persist karta hai. |

Ek working coder in sab terms ko bina hesitation use karta hai. *"Main /clear karunga, phir agle
unblocked vertical slice par `tdd` chalaunga"* aur *"yeh faithfulness hallucination hai — docs abhi
bhi context mein hain, bas turn forty ke around unko parhna band ho gaya"* — yehi sentences hain jo
vague conversation ko kaam-karne-wali conversation se alag karte hain.

---
[⬅ Architecture Principles](07-architecture-principles.md) · [Agla: Practical Drills ➡](09-practical-drills.md)
