# 03 — Part 3: Extending Reach (Concepts 8-9)

## Concept 8: Connectors, Apps, aur Sawal Ko Route Karna

Ab tak assistant zyada tar us information ke sath kaam karta tha jo tum front mein dete ho. Lekin
tumhari real information kahin aur rehti hai: email, calendar, cloud storage, project-management
tools, chat systems, company knowledge bases. **Connectors aur apps** assistant ko wahan tak reach
dete hain.

**Connector ya App?** Claude "**connector**" kehta hai. ChatGPT "**app**" kehta hai same category ke
liye (pehle yeh bhi "connector" kehta tha, rename ho gaya). Lafz alag, purpose same — assistant doosre
system mein search/read/act (permissions ke mutabiq) kar sakta hai.

**MCP: shared integration standard.** Dono ecosystems **Model Context Protocol (MCP)** support karte
hain. Shorthand hai **"USB-C for AI tools"** — ek standard plug, ek baar bana tool kai assistants use
kar sakte hain. Lekin yeh shorthand ek cheez chhupa deta hai: **USB-C cable plug karna trust decision
nahi hai. MCP tool connect karna hai. Plug standard hai; access nahi.**

**Connections permission decisions hain.** Connect karne se pehle poocho:
1. Yeh kya **parh** sakta hai?
2. Yeh **likh/send/delete/buy** ya kuch act kar sakta hai bahar ki duniya mein?
3. Mujhe source par **trust** hai?
4. Mujhe is account/system ko connect karne ki **ijazat** hai?

Connector/app ko usi tarah treat karo jaise software install karna — useful, aur jaan-boojh kar
permission-gated. Yeh 4 sawal ki apni limit hai: connector sirf wo kar sakta hai jiske liye bana hai
— permissions **existing actions** ke beech choose karti hain, nayi actions **add nahi** karti.

**Search, Thinking, ya Research?** Beginners galat mode choose karte hain:

| Tumhe kya chahiye | Use karo | Example |
| --- | --- | --- |
| Ek current fact | Web search | "What is today's exchange rate?" |
| Hard reasoning, no new info | Thinking mode | "Compare these three pricing strategies." |
| Thorough, cited investigation | Research mode | "Research the current market for warehouse robotics." |
| Apni organization ki info | Workplace search/connected apps | "Find the latest approved pricing policy." |

Pehla sawal: **main assistant se kaunsa kaam karwa raha hoon?** Ek fact par deep research mat kharch
karo jo search seconds mein de sakta hai; search mat use karo jahan asal masla reasoning hai.

**Research mode "behtar search" nahi hai** — assistant ek investigation **plan** karta hai, kai
searches chalata hai, leads follow karta hai, sources parhta hai, structured cited report deta hai.
Yeh minutes leta hai, seconds nahi — tum ek **investigation delegate** kar rahe ho. Report aane par
bhi judgment zaroori hai: important claims check karo, citations kholo.

> **Yaad rakho:** sawal ko bhejne se pehle route karo.

## Concept 9: Prove It on Work You Already Know

Course ka sab se zaroori sawal: **assistant asal mein tumhare kaam mein achha hai, yeh kaise pata
chale?** Kisi benchmark par nahi. Kisi demo par nahi. **Tumhare** task par, **tumhare** data par,
**tumhare** standard se.

Best beginner method: **assistant ko wo kaam test karo jo tum already finish kar chuke ho aur
trust karte ho.**

**Example:** ek program director har quarter attendance/employment outcomes analyze karta hai. Wo
naye data se shuru nahi karta — **last quarter ka raw data** deta hai (kyunke usay already pata hai
correct analysis kya hai), reproduce karwata hai, phir compare karta hai. Agar assistant pattern miss
kare, instructions improve hoti hain. Agar data mein hi gap mile, data problem mil gaya. Agar abhi
bhi reliable nahi, **wo hissa human reh jata hai.** Teeno outcomes useful hain.

**5-step proving loop:**
1. **Ek recurring task pick karo.** Precise raho.
2. **Ek purana example dhoondo** jiska correct result tumhe pehle se pata hai.
3. **Assistant ko reproduce karne do.** Wahi context do jo normally hota.
4. **Compare karo.** Kya match hua? Kya fail hua? Kaunsi instruction missing thi?
5. **Refine karo, dobara chalao.** Jab tak "good enough" na ho, ya tum decide karo yeh task delegate
   nahi honi chahiye.

Aakhri outcome **failure nahi hai** — yeh seekhna ke kya **delegate nahi karna**, apna waqt deserve
karta hai.

**Passing kya prove karta hai?** **Earned confidence for similar future work.** Yeh prove nahi karta
har future case par sahi hoga. Aur yeh **responsibility transfer nahi karta** — tumhe phir bhi: naye
results check karna, final work ke peeche khade hona, zaroorat ho to AI-assistance disclose karna,
high-risk decisions human control mein rakhna hai.

Agar mumkin ho, same test Claude aur ChatGPT dono mein chalao — yeh platform awareness banane ka sab
se fast tareeqa hai. Yeh chhoti exercise tumhari **pehli evaluation suite** hai.

> **Yaad rakho:** trust known work ke against earned hona chahiye, acha-dikhne-wale jawab se assume
> nahi.

---
[⬅ Part 2 — Projects & Memory](02-part2-projects-memory.md) · [Agla: Recap + 6 Prompts ➡](04-recap-and-practice-prompts.md) · [⬆ Index](README.md)
