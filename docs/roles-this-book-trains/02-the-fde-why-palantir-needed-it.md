# 02 — The FDE: Why Palantir Needed It

Upar wale chaar core roles apni company ke andar line chalate hain. Wahi line ek client ki company
mein carry karo, ek embedded engineer se end-to-end, aur uska ek naam hai jise market ab hire karne
ke liye tarap rahi hai.

## Ek FDE Asal Mein Karta Kya Hai

Zyadatar software engineers headquarters mein product banate hain aur woh customer kabhi nahi
milta jo use karta hai. Ek FDE ulta karta hai. Woh customer ki asal workplace mein jaata hai, un
logon ke sath baithta hai jo woh kaam karte hain, unke real problems samajhta hai, aur wahin,
on-site, apni company ke platform se solutions banata hai. Demo nahi. Slide deck nahi. **Working
software jo customer ke real environment mein chalta hai.**

Farq socho ek doctor ka jo dusre shehar se aapka chart parhta hai, aur doctor ka jo kamre mein
baith kar aapko check karta hai aur wahin treatment shuru karta hai. FDE doosra doctor hai.

**Palantir** ne yeh role 2010s ke shuru mein banaya, pehle unhein "Deltas" kehte the. 2016 tak,
Palantir ke paas normal software engineers se zyada FDEs the, kyunke unke customers (government
agencies aur bare traditional enterprises) ko koi chahiye tha jo on-site startup mentality se
internal bureaucracy kaat sake. Palantir ka farq samjhane ka tareeqa sabse clear hai: ek regular
developer **ek capability, kai customers** par focus karta hai (ek feature banao, sabko ship karo),
jabke ek FDE **ek customer, kai capabilities** par focus karta hai (ek client ke sath embed ho jao,
jo bhi chahiye woh solve karo).

## FDE 101: Kevin Bai Ka Nazariya

2026 ke mid mein, Kevin Bai (jinhone Palantir mein FDE engagements lead kiye, phir Rippling mein
FDE function zero se banaya, ab Anthropic ke Applied AI team mein hain) ne apni talk **"Forward
Deployed Engineering 101"** mein yeh role sabse clear tareeqe se explain kiya.

**Problem software kabhi nahi thi.** Palantir ka Foundry data centralize aur ek "ontology" banata
hai — companies ki tables ko proper nouns mein badalta hai. Lekin ek business leader ko yeh dikhao,
aur jawab hota hai: *"tumne mera data organize kar diya, isse mere business ko kya faida?"* Yahin
sirf technology bechna kam par jata hai. Bai ka fix: software bechna band karo, hours bechna band
karo, aur **outcome** becho. Log bhejo jo customer ka business samjhein, platform par solution
banayein, aur result hand over karein.

**Kaunse buyers ko yeh chahiye tha?** Foundry ek app-building platform hai — un companies ke liye
useless jinke paas pehle se acche engineers hain (Google, Meta). Jinhein zaroorat thi woh the Fortune
500 companies jaise oil aur gas — jahan, Bai ke alfaz mein, "pipelines data pipelines nahi hain."

**Proof contract size mein hai.** Public SaaS companies jo Fortune 500 ko serve karti hain, unka
average contract value dekho: Palantir taqreeban **$4 million**, ServiceNow ~$1.2 million, Workday
~$600,000 — koi aur public SaaS company $500K se upar nahi. **Outcomes bechna seats bechne se alag
price karta hai.**

## Test: Kya Aapko FDE Chahiye Bhi Hai?

Bai ka screen ek 2×2 hai: aap jo bechte ho woh kitna technical hai, aur jo khareedta hai woh kitna
technical hai. Char cells mein se teen ko koi forward deployment nahi chahiye:

- **Technical product, technical buyer** (GitHub, Datadog) — documentation aur developer relations
  kaafi hain.
- **Configurable product, technical buyer** — self-serve ya sales-led motion kaam kar jata hai.
- **Configurable product, non-technical buyer** (Rippling, Jira, Slack) — traditional sales-led
  motion.
- **Technical product, non-technical buyer** — **sirf yehi cell jahan FDE zaroori hai.** Yeh
  Palantir ka corner hai.

Bai ka discipline diagram se zyada matter karta hai: sawal yeh nahi ke "kya mujhe FDE function
chahiye" (kyunke fashionable cheez chahna aasan hai) — sawal yeh hai ke "kya mujhe kuch technically
complicated ek aise buyer ko bechna hai jo isay implement nahi kar sakta." Agar nahi, to forward
deployment shayad sahi fit nahi.

## Yeh Solutions Architect Se Alag Kaise Hai

Ek Solutions Architect **advise** karta hai — demos run karta hai, whiteboards par design karta hai,
proof-of-concept banata hai deal band karwane ke liye. Deal band hote hi involvement khatam. Ek FDE
wahan se shuru karta hai jahan Solutions Architect chhorta hai — customer ke infrastructure par,
real data ke sath, production code likhta hai, aur wahan tak rehta hai jab tak customer ko real
value na mile. Simple test: agar role customer-specific kaam ko production mein **chalane** ke liye
accountable hai, yeh FDE ke qareeb hai. Agar product **prove ya explain** karne ke liye accountable
hai, yeh solutions architect ke qareeb hai.

Real example: **OpenAI aur John Deere** — 190 saal purani farming company. See & Spray ke around AI
apply hui, customer success, dealer workflows, aur preseason recommendations mein. John Deere
credits See & Spray with **70% tak kam chemical use.** Yeh kaam customer ke **planting calendar**
par tha, kisi product roadmap par nahi — FDE ka job ek line mein: real production software, customer
ki duniya mein banaya gaya, aur customer ki asal zaroorat par ship kiya gaya.

Bai isay ek hiring test mein compress karta hai: FDE woh insan hai jo **engineering bar par akela
hire ho jaye**, aur jise aap **customer ke saamne bhi bhej sako.** Dono sach hone chahiye. Pehla
chhoro to account manager mil jata hai jo bana nahi sakta. Doosra chhoro to engineer mil jata hai
jise customer se door rakhna padta hai.

---
[⬅ The Generalist Core](01-the-generalist-core.md) · [⬆ Index](README.md) · [Agla: FDE Market aur Services Industry ➡](03-the-fde-market-and-services-industry.md)
