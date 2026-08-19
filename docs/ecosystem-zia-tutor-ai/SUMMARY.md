# Zia Tutor AI — Summary

Yeh chapter khud us tool ki documentation hai jo shayad aap is book ko parhne ke liye use kar rahe ho. Sabse zaroori line: Chatbot **jawab** deta hai. Zia Tutor AI **sikhata** hai — sequence chunta hai, samajh check karta hai, "wahin se continue karo" sach karta hai kyunke iske paas **Learner Record** hai jo koi bare model nahi rakhta.

## Chapter Overview
- Ek personal learning agent — Zia Khan (Panaversity co-founder, book co-author) ka **digital twin**: teaching identity, method, personality ek agent mein encode. Poori learning journey ka context rakhta hai.
- Ecosystem Concept ki "ladder" ka **Rung 3** (SoR + personal teacher). FDE AF Model mein **Layer 2 reference-expert position** — har future vertical apna equivalent banayega.

## 00 — Ek Purpose, Do Roles, Teen Records
- **Ek purpose:** "Aapko woh expertise dilana ke aap AI Workers/Digital FTEs bana sako, aur FDE ban sako" — vertical personal AI agent for education.
- Zyada tar AI tutors sirf sawal ka jawab dete; Zia Tutor AI samajhta hai sawal journey mein kahan fit hota — naam se greet, yaad rakhta kahan chhoda, sessions/hafton ke aar-paar continue karta, sahi sequence sikhata, understanding check karta, agla topic pehchanta, har lesson governed knowledge base mein ground karta.
- **Do roles:** Learner ke liye personal learning agent; Agent Factory ke liye reference expert twin (Zia ki teaching identity/method/judgment encode). Layer 2 ke reference-expert position par — accounting/healthcare/legal/engineering/sales expert twins future mein isi pattern se.
- **Teen governed records:** Knowledge Record (SoR — concepts/methods/terminology), Learner Record (goal, progress, understanding, agla step), Identity Record (Zia ki voice/principles/explanations/standards/method). Teeno mil kar: grounded + recognizable + continuous tutor.
- **Kyun zaroori:** pehli AI-education generation ne answers diye; agli generation ek personal agent degi jo samjhe *kaun hai, kya chahta hai, kya janta hai, kahan struggle karta hai, aage kya*.

## 01 — Setup Karo: Connector, Skill, Aur Pehla Command
- claude.ai ke andar rehta hai, koi alag app nahi. ~2 minute setup, 2 steps:
  1. **Connector:** Connectors → Add custom connector → Name: `Zia Tutor AI`, MCP Server URL: `https://zia-tutor-ai.panaversity.org/mcp` → Advanced settings mein OAuth Client ID: `zia-tutor-ai` (Client Secret khaali) → Add → Connect, Panaversity account se sign in, approve. Tool permissions dono groups ke liye **Always allow** set karo (warna har reply par permission maangega).
  2. **Skill:** `zia-tutor-ai.zip` download karo → Skills → Add → Upload a skill → file drop karo (unzip mat karo).
- **Shuru:** kisi bhi chat mein `/zia-tutor-ai` type karo — Zia naam se hello bolega, wahin se shuru jahan chhoda tha. Sirf bulane par aata hai, baaki chats normal rehti hain. Abhi **Beta 1** — rough edges expect karo, feedback button top par hai.
