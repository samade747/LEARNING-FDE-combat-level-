# Connector-Native Apps: A Remote MCP Server Whose Customer Is an AI

*Source: The AI Agent Factory — "Connector-Native Apps: A Remote MCP Server Whose Customer Is an AI" (Panaversity)*
*URL: https://agentfactory.panaversity.org/docs/connector-native-apps*
*Group: Mode 2 — Manufacturing, Phase 1 · Building Blocks (Chapter 2 of 6)*

---

## Yeh Course Kis Baare Mein Hai

**14 Concepts.** 30 saal se humne software **insano** ke liye banaya — screens, buttons, forms. **Ab
customer AI bhi ho sakta hai.** Is course mein aap ek aisa product banate ho jiska **user ek AI hai.**

Ek **connector** woh add-on hai jo insan apne AI mein daalta hai taake woh bahar ki app tak pahunch
sake — ek URL paste karo, ek click. Uske baad AI aapka user hai: woh aapke tools ke naam parhta hai,
khud decide karta hai kaunsa call karna hai, inputs deta hai, results insan ko wapis bolta hai. **Aap
shop window nahi saja rahe — aap ek labeled tools ka pegboard latka rahe hain jise ek na-thakne wala
worker khud use karta hai.**

Course mein aap **ek real product** banate ho, end-to-end: ek remote MCP server ("Reading Room"), do
tables ki memory, real sign-in (OAuth), ek session contract, sab ek pasted URL se claude.ai mein chalta
hua.

## Parts

1. [Overview — 4 Invariants, Server Kya Hai](00-overview.md)
2. [The Shape — Direction, Tools Only, One Gateway (Concepts 1-4)](01-the-shape.md)
3. [State Aur Domain (Concepts 5-6)](02-state-and-domain.md)
4. [Identity Prove Karna — Jo Model Fake Nahi Kar Sakta (Concepts 7-8)](03-proving-identity.md)
5. [Model Ko Steer Karna (Concepts 9-11)](04-steering-the-model.md)
6. [Ship It + Capstone + Ceiling (Concepts 12-14)](05-shipping-and-capstone.md)

---

## Ek Rule Jo Har Mushkil Hissa Explain Karta Hai

> **"Aap server own karte ho, us dimagh ko nahi jo usay call karta hai."**

Intelligence AI ke host app mein rehti hai. Loop jo decide karta hai agla kya karna hai wahin rehta hai.
Aapka server sirf tab jawab deta hai jab call hota hai, aur caller ek aisa dimagh hai jo **guess** karke
sochta hai — fast, capable, aur puri tarah confused ho sakta hai, convince ho sakta hai, ya bas ghalat ho
sakta hai. Isiliye is course ka har mushkil hissa: **aapka server woh kaam karta hai jo AI khud ke liye
trust nahi kiya ja sakta.**

*Yeh summary poore course (4 Invariants + Shape + State/Domain + Identity + Steering + Shipping +
Capstone + Ceiling) ka overview hai.*
