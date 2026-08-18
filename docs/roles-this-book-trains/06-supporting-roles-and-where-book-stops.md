# 06 — The Supporting Roles, and Where the Book Deliberately Stops

## Supporting Roles

Har pipeline ko chahiye woh log jo kaam check karein, rules set karein, aur zimmedari lein. Teen
roles yehi karte hain.

**Evals Engineer — AI Workers ko live jaane se pehle crash-test karta hai.** Aap ek gaari bina
crash-test kiye ship nahi karte. Aap ek dawa bina clinical trials ke release nahi karte. Ek AI
Worker jo real logon aur real paise ko affect karne wale decisions leta hai, usay wahi discipline
chahiye. Evals Engineer woh tests design karta hai: kya Worker sahi jawab deta hai? Kya woh gracefully
fail karta hai jab kuch aisa dekhe jo pehle kabhi nahi dekha? Kya woh apni diyi hui lines ke andar
rehta hai? Yeh koi afterthought nahi — yeh har chapter mein built-in hai.

**AI Governance Officer — decide karta hai AI ko kya karne ki ijazat hai.** Har company mein har
employee ki limits hoti hain. Ek junior accountant $500 tak expenses approve kar sakta hai, upar
manager ka signature chahiye. Ek bank teller deposit process kar sakta hai lekin loan approve nahi
kar sakta. AI Workers ko wahi structure chahiye. Governance Officer company-level par yeh rules
likhta hai: AI khud kya decide kar sakta hai, kya human approval ko jana chahiye, aur AI ko kabhi
kya touch nahi karna chahiye. Woh company ki industry ke regulations bhi map karte hain — bank mein
fair lending rules, hospital mein patient privacy, Europe mein data residency laws. Book yeh
governance framework discipline directly train karti hai — aapki industry ke specific regulations
aap khud laate ho.

**Digital FTE Supervisor — woh insan jiska naam line par hai.** Jab ek AI Worker ek claim process
karta hai, contract draft karta hai, ya transaction flag karta hai, kisi ko accountable hona hoga.
Yeh Supervisor hai — human-in-the-loop: reviewer jo kaam check karta hai, manager jo output approve
karta hai, woh naam jis par audit trail point karta hai jab kuch galat ho jaye. Yeh woh insan nahi
jisne Worker banaya — yeh woh insan hai jo isay din-ba-din chalata hai, jaise ek shift manager team
chalata hai.

## Jahan Book Jaan-boojh Kar Rukti Hai

**LLMOps Engineer — model tak, model khud nahi.** Production mein agents chalana Cloud AI Engineer
ka kaam hai, aur book yeh train karti hai. Book hands-on fine-tuning bhi train karti hai — lekin
last resort ki tarah, default nahi. Fine-tune aapke system ko ek model snapshot se baandh deti hai
aur woh optionality khatam kar deti hai jise poora method protect karta hai — isliye sirf tab reach
karo jab prompting, context, tools, aur retrieval genuinely kam par jayein. Hard stop hai: foundation
model ko scratch se pre-train karna scope se bahar hai, kyunke woh capability commoditize ho rahi
hai.

**Harness Engineer — runtime jo aap use karte ho, jo aap banate nahi.** Harness woh agent runtime
hai (OpenAI Agents SDK, Claude's managed agents, waghera) jo agent loop chalata hai, state manage
karta hai, aur tool calls execute karta hai. Book aapko inhein fluently use karna sikhati hai aur
inke aar-paar portable rehna, kyunke aapki discipline kisi bhi runtime se zyada zinda rehti hai.
Runtime khud banana job nahi hai.

**AI Data Engineer — agent-facing data layer.** System-of-record kaam agent-facing data layer ko
touch karta hai: Postgres, pgvector, aur MCP woh spine hai jisse agent parhta hai. Classic pipeline
aur warehouse engineering adjacent hai, central nahi.

---
[⬅ Skill Author aur Connector/Plugin Engineer](05-skill-author-connector-plugin-engineer.md) · [⬆ Index](README.md) · [Agla: Your Type aur FDE Appendices ➡](07-your-type-and-fde-appendices.md)
