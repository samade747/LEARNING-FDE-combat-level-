# 01 — Part 1: The Two Upgrades (Concepts 1-5)

## Concept 1 — Chat Box Se Operating Layer Tak

Accountant har mahine fresh chat open karta client summary ke liye — har baar same instructions
paste: reporting currency, thousands separators, **expense head** (spending category — travel,
rent, salaries) se group, **tax-withholding threshold** (jis amount ke upar tax rok ke government
ko bhejna hai) se upar flag, template follow. AI achha karta hai, phir bhool jata.

Doctor consultation notes **SOAP** format mein chahta (4-part clinical note: patient kya kehta,
doctor kya dekhta, assessment, plan) — allergies top par, har baar re-explain. Marketer brand-voice
rules paste karta har caption mein. Engineer severity-grouped review notes chahta.

**Sab ek shape hain: repeatable task, tumhare specific tareeqe se, sirf input change hota.**
**Skill** is shape ke liye saved instructions hain — "how" ek baar likho, AI jab bhi task aaye
apply kare.

Doosra friction: accountant ke numbers Excel file mein, quarter ka data email mein. Doctor ki
patient history Drive folder mein. Marketer ka content calendar planning tool mein. Engineer ke
open issues Jira/Linear mein. AI isse reason kar sakta, **sirf agar info AI tak pahunche.**
Copy-paste AI ke "no hands" hone ki price hai. **Connector** safe link hai jo AI ko ek app tak
pahunchata — permission se AI app kholta, jo chahiye leta, results wapas likhta jab allow karo.

Dono together: chat box ek colleague ban jata jo tumhare standards jaanta aur tumhari files tak
pahunch sakta. **Operating layer** — AI jo real kaam par act karta, box jisme type karte ho nahi.

## Concept 2 — Skill Actually Kya Hai

Embarrassingly simple: **ek folder, jisme ek text file hai.**

**SKILL.md** required file hai (exactly yeh naam, capital letters) — naam, short line kab use
karein, aur instructions. Naam + 1 line + plain-English paragraph kaam kar jata.

Folder mein example files, template document, reference notes, chhote programs bhi ho sakte —
koi required nahi. Accountant ki pehli skill 5 sentence formatting rules ho sakti. Programs real
code hain par **tum ek line kabhi nahi likhte** — AI jo bhi code chahiye likhta hai.

Anthropic: skills "folders of instructions, scripts, and resources that Claude loads dynamically."
Word hai "**dynamically**". AI har waqt har skill view mein nahi rakhta — sirf **description**
(short line kis liye hai) rakhta, match hone par full instructions kholta. **Progressive
disclosure** — isiliye dozens skills install kar sako bina slow kiye.

## Concept 3 — Connector Actually Kya Hai

AI ko safely apps/data tak pahunchane ka tareeqa. Google Drive connect karo, files search kar
sakta. Gmail connect karo, mail parh/draft-reply kar sakta. Slack/Linear/Asana/Notion se pull +
act kar sakta.

**MCP** (Model Context Protocol) — open standard jispar connectors chalte. Connector chhota
software hai jo company/AI ne code se banaya — **tum kabhi nahi banate ya parhte**, sirf _Connect_
click karte. _Code you never write_ ka bargain.

**3 facts matter karte:**

1. **AI tumhari permissions inherit karta** — account kuch na khol sake to connector bhi nahi.
   Drive connect karne se poori company ki drive hath nahi aa jati.
2. **Tum decide karte kitna AI kar sake** — **read-only** (dekh sakta, change nahi) jaise "search
   and summarize"; **write access** (edit/create/send/delete) jaise "send this email". Read-only
   se shuru karo, trust ke baad write access.
3. **Connectors per-conversation on karte ho** — connect karna available banata, tum decide karte
   kaunsa chat kaunsa connector use kare, aur **scope** (app ka kitna hissa — ek folder vs poori
   drive, chhota = safer).

Directory mein ready-made connectors (Drive, Gmail, Slack, Notion, Figma, Linear, Atlassian).
**Custom connector** khud setup kar sakte kisi bhi MCP-speaking service ke liye. **Interactive
connector** chat ke andar live panel draw karta.

## Concept 4 — Skills vs Connectors vs Projects vs Custom Instructions

**Project** = workspace jo files+instructions har chat mein load karta. **Custom instructions** =
preferences jo har chat par apply hoti.

| Feature | Kya hai | Best for | One-line test |
|---|---|---|---|
| **Skill** | Reusable how-to, relevant hone par load | Repeatable task tumhare tareeqe se | "Main yeh how dobara explain kar raha" |
| **Connector** | Outside app tak safe access | Files/email/messages/tickets read/act | "Main doosri app se copy-paste kar raha" |
| **Project** | Workspace jo har chat mein load hota | Standing context (client, course, book) | "Yeh files/rules har jagah lagte" |
| **Custom instructions** | Sab chats par preferences | Global style | "Yeh hamesha true ho, har jagah" |

3 lines jo confuse hoti: **Skill vs Project** — Project chat khulte hi load hota (always-on),
Skill match hone tak sleep karti, phir kahin bhi kaam karti. **Skill vs Connector** — Connector
access hai (kya reach kar sakta), Skill expertise hai (kaise behave kare) — partners hain,
alternatives nahi. **Skill vs Custom instructions** — custom instructions sab kuch touch karte,
Skill ek kisam ka task.

## Concept 5 — Slash Command, Ya AI Khud Jaanta Hai?

**Claude.ai mein skills khud shuru hoti.** Task plain language mein describe karo, AI request ko
har enabled skill ki description se check karta, matching load karta. **Fire** = skill bina naam
liye activate hoti. "Q3 results par PowerPoint" bolo, PowerPoint skill fire hoti.

Slash commands hands-on tools mein rehte: Cowork + Microsoft 365 add-ins mein `/` type karo browse
karne ke liye (plain words bhi chalte); Claude Code/OpenCode mein skills khud load hoti, deliberately
call bhi kar sakte.

3rd option har jagah chalti: skill ka naam plain English mein bolo — "use my brand-voice skill to
draft this caption."

| Chahte ho | Claude.ai | Cowork/Office add-ins | Claude Code/OpenCode |
|---|---|---|---|
| AI decide kare | Task describe karo, automatic | Task describe karo, automatic | Task describe karo, automatic |
| Specific skill force karo | Naam lo | `/` type karo ya naam lo | Naam lo, ya directly call |
| Browse karo | Customize→Skills | Sidebar mein `/` | Skills folder list |

Connectors same tareeqe se — app connect+enable hone ke baad, AI request ke mutabiq bulata.
"Drive mein contract summarize karo" — Drive se pull, no clicking.
