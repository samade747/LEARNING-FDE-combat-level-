# 05 — The Skill Author, and the Connector/Plugin Engineer

## Subject Matter Expert as Skill Author — Woh Role Jise Market Ne Abhi Naam Nahi Diya

Woh accountant, lawyer, ya supply-chain expert jo apni judgment ko **SKILL.md** (ek plain-text file
jo ek skill package karti hai jise agent load aur follow kar sake) mein encode karta hai, aur Digital
FTE ka **knowledge engine** ban jata hai. Kaam concrete hai: woh tacit rule lo jo aap bina soche
apply karte ho — ek seasoned auditor kaise decide karta hai kaunse transactions flag karne hain, ek
claims adjuster kaise ek borderline case parhta hai — aur usay itni precision se likho ke agent
execute kar sake, phir test karo ke agent ke decisions aapke se match karte hain ya nahi, aur SKILL.md
ko revise karo jab tak match na ho jaye.

Zyadatar market lists is role ko miss kar dete hain kyunke woh ab bhi AI work ko sirf engineering
samajhte hain. Yeh book domain judgment ko khud ek aisi cheez ki tarah treat karti hai jise author,
test, aur deploy kiya jaye — aur expert ko teeno karna sikhati hai. Vendor-neutral FDE ki tarah,
yeh bhi ek aisa role hai jo almost koi aur train nahi karta.

**Yeh do "unnamed" roles ek doosre ki zaroorat rakhte hain.** Vendor-neutral FDE ka doosra System of
Record kisi author ke bagair exist nahi ho sakta — kyunke uske andar procedures ek practitioner ki
awaaz mein likhe gaye hote hain, unke real files se derived. Aur Skill Author ko koi chahiye jo uski
judgment ke liye governed ghar banaye. Koi bhi junior partner nahi. Expert 20 saal ka tajurba aur
licence laata hai. Engineer method aur build laata hai.

**Market ne is role par ek price print kar diya hai.** 2026 ke mid mein, Business Insider ne Yousuf
Imran ki story chhapi — ek Google account executive jinki sales commissions $170,000 base ko
taqreeban **$986,000/saal** tak barha deti thin. April mein usne resign kar diya Mangosteen Studio
banane ke liye — ek AI product lab jo salespeople ke liye sales tools banata hai. Headline number se
aage, notice karo woh **kya nahi hai:** software engineer. Uska stated asset tha 20 saal ka
salespeople ke problems seekhna, aur uska bet tha ke yeh judgment, AI products mein encode ki gayi
jo woh khud own kare, near-million-dollar salary rent karne se zyada valuable hai. **Headline
kehta hai ek insan ne $986,000 chhora. Mechanism kehta hai domain expertise ek manufacturing input
ban gayi, aur expert ne factory apne paas rakhi.**

## The Connector and Plugin Engineer

Yeh role un agent hosts ko extend karta hai jinmein doosre log pehle se kaam karte hain. Ek Worker
banane se pehle jo apna khud ka loop rakhti hai, ek poora discipline hai un cheezon ko banane ka jo
agent apne ird gird reach karta hai — aur market isay paanch naamon se pukar rahi hai ek waqt mein:
MCP engineer, integrations engineer, connector developer, plugin developer, agent-tooling
engineer. **Yeh ek job hai do addresses par.**

**Connector-native app** chat app (claude.ai) ko end users ke liye extend karta hai: aap ek remote
MCP server ship karte ho — tools, stored state, real sign-in, fail-closed session gate — jo koi
ajnabi ek pasted URL se add kar deta hai, aur us waqt se model khud aapka customer ban jata hai.

**Plugin** coding agent (Claude Code, OpenCode) ko builders ke liye extend karta hai: skills,
subagents, hooks, aur MCP servers ek install ke peeche, jahan ek deterministic hook woh line hai jo
"advice jise model skip kar sakta hai" aur "rule jo har baar chalta hai" ke darmiyan hoti hai.

**Ek hi move, do hosts:** aur dono ke neeche wahi artifact baitha hai — ek MCP server, isi liye book
inhein back-to-back sikhati hai. Through-line thesis se ek idea hai: aap ek unit ship karte ho jise
host load kare, aur aap extension ke malik ho jabke host loop ka malik hai. Book dono ko poora
train karti hai, ek deployed artifact tak.

---
[⬅ Two Systems of Record](04-the-fde-systems-of-record-and-pod-of-one.md) · [⬆ Index](README.md) · [Agla: Supporting Roles aur Jahan Book Rukti Hai ➡](06-supporting-roles-and-where-book-stops.md)
