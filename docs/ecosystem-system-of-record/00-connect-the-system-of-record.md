# 00 — Connect Karo: Steps Aur Design Ke Peeche Ki Soch

## Yeh Design Kyun Aisi Hai

Chaar cheezein is record ko sirf "search over docs" se alag banati hain:

- **Koi bhi agent ya worker connect ho sakta hai** — Claude, ChatGPT, Claude Code, Cowork, ya koi custom
  agent kisi bhi SDK par: jo bhi MCP bolta hai, woh Agent Factory ka content parh sakta hai. Ek source,
  koi bhi host.
- **Grounded, guessing nahi** — agent book se jawab deta hai aur exact section cite karta hai, model ke
  training memory se improvise karne ke bajaye. Jab source unreachable ho, yeh **fail closed** hota hai
  — kehta hai jawab nahi de sakta, kuch bana kar nahi deta.
- **Book ke saath live rehta hai** — jab bhi book ka naya version publish hota hai, record usay dobara
  parh leta hai, to kabhi source se drift nahi hota. Book hi single source of truth rehti hai; record
  sirf book ko retrievable banata hai.
- **Book ka apna stack** — Postgres aur pgvector, read-only MCP tools ke zariye serve — bilkul wahi
  pattern jo book systems of record aur RAG ke liye sikhati hai, ab book par khud apply kiya gaya. Humne
  ise usi method se banaya jo hum sikhate hain.

## Connect Kaise Karein (claude.ai Custom Connector)

Beta 1 mein yeh **claude.ai** ke zariye connect hota hai aur book ke core content ko serve karta hai:
About se Glossary tak — yani woh ~80% path jahan zyada tar value rehti hai.

1. **claude.ai** ke sidebar mein **Connectors** kholo (Customize ke neeche).
2. **Add custom connector** click karo.
3. Yeh do fields paste karo:
   - **Name:** `Agent Factory System of Record`
   - **MCP Server URL:** `https://sor.panaversity.org/mcp`
4. **Advanced settings** kholo, wahan **OAuth Client ID** paste karo: `zia-tutor-ai`
   - **Client Secret khaali chhodo.** Is connector ka koi secret nahi hai — kuch type karoge to connect
     nahi hoga.
5. **Add** click karke connector save karo.
6. Apni connectors list mein isay dhundo, **Connect** click karo, aur access approve karo jab Claude
   pooche.
7. Ab Claude se kuch poocho aur dekho woh book se jawab deta hai: *"Use the Agent Factory System of
   Record and explain what AI actually is."*

Yeh **read-only** hai. Connect karte waqt authorization maangta hai. Yeh abhi beta mein hai, to behtar
hota rahega.

## FDE AF Model Mein Yeh Kahan Fit Hota Hai

Yeh **Layer 1** ka pehla live instance hai — SoR kernel. Isi component ko apni content ke saath run
karke aap apna khud ka governed System of Record bana sakte ho (jaise Accounting System of Record ya
Core Banking System of Record) — poori tafseel
[The FDE AF Model](../ecosystem-fde-af-model/README.md) mein hai. Aur agar aap khud apna vertical
System of Record design karna chahte ho, uska poora method
[Designing the Vertical System of Record](../ecosystem-designing-the-vertical-sor/README.md) mein hai.

---
[⬆ Index](README.md)
