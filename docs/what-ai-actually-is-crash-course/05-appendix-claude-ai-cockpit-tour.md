# 05 — Appendix: Claude.ai Ka Cockpit Tour (A.1-A.10) + Sources

> Yeh optional appendix hai — 9 ideas vendor-neutral hain (Claude, ChatGPT, Gemini, sab par lagu hoti
> hain). Yeh appendix jaan-boojh kar **ek** product, Claude.ai, tour karta hai aur uske har switch/
> setting ko wapis usi idea se jorta hai jo usko explain karti hai. Agar aap koi doosra product use
> karte ho, controls ke naam alag honge lekin same machine operate karte hain — mapping transfer ho
> jati hai.

## A.1 — Andar Aana

Claude teen jagah chalta hai: browser mein [claude.ai](https://claude.ai), Mac/Windows desktop app,
aur iOS/Android mobile apps. Account free hai, credit card nahi chahiye, aur kam se kam 18 saal ka
hona chahiye. Free plan genuinely usable hai: ek capable model par chalta hai jiski **session-based
usage limit har 5 ghante mein reset hoti hai**.

Yeh limit Idea 4 se jorho — arbitrary nahi rehti. Limit messages mein nahi, **tokens** mein count hoti
hai — machine ke kaam aur cost ki real unit. Chhota sawal thora budget kharch karta hai. Lambi chat har
turn ke saath zyada kharch karti hai, kyunke poora transcript har baar context window mein replay hota
hai (Idea 5). Isi liye Urdu ya kisi non-Latin script mein kaam karna wahi budget jaldi kharch karta
hai. Paid plans (Pro aur upar) bara token budget aur zyada features unlock karte hain.

## A.2 — Window

Interface ek chat box hai teen zaroori controls ke saath:

| Control | Kahan | Yeh mechanically kya hai |
| --- | --- | --- |
| **Prompt box** | Center | Context window ka darwaza (Idea 5). Jo bhi type ya attach karo, desk par land karta hai. |
| **Model selector** | Prompt box ke neeche (web/desktop), top (mobile) | Kaunse frozen weights (Idea 2) se baat kar rahe ho, choose karta hai. Alag model, alag frontier shape (Idea 7). |
| **Effort/thinking control** | Model selector ke paas | Kitni reasoning answer se pehle desk par daali jaye (Idea 9). Zyada effort = zyada hidden tokens, behtar answers hard problems par, zyada time/budget. |

Left panel mein pichli conversations, projects, artifacts hote hain.

## A.3 — Model Ladder

Claude ek saath kayi models ship karta hai, fast-and-cheap se deep-and-expensive tak ek ladder mein
arranged. Naam badalte rehte hain (mid-2026 mein ladder: Haiku, Sonnet, Opus, aur ek tier Opus se upar)
— naam yaad na rakho, **ladder logic** yaad rakho:

- **Default middle mein rakho** — mid-tier model zyada tar tasks achi tarah handle karta hai aur token
  budget slowly kharch karta hai.
- **Depth ke liye upar escalate karo** — top-tier model tab lo jab task ko ek bara, complex structure
  ek saath coherent rakhna ho: lambi document analysis, hard architecture.
- **Bulk ke liye neeche drop karo** — chhota, fast model high-volume, low-depth kaam ke liye:
  reformatting, quick summaries, simple classification at scale.

Ladder Idea 7 ki wajah se exist karti hai: capability jagged hai aur priced accordingly.

## A.4 — Thinking Aur Effort

Thinking control Idea 9 ko ek dial mein badal deta hai. Higher settings model ko answer se pehle lambi
hidden chain of working generate karne dete hain; naye models par yeh adaptive hai — model khud judge
karta hai sawal kitna hard hai. Kuch models par yeh thinking summary expand karke parh sakte ho — kam
se kam ek baar zaroor karo, yeh sabse achi free lesson hai machine ke problem-approach ki.

Trade hamesha same hai: thinking extra tokens hai (Idea 4), is liye time aur budget kharch karta hai.
Real-consequence decisions par kharcho; lookups aur reformatting ke liye skip karo.

## A.5 — Desk Ke Tenants, Product Settings Ki Tarah

Idea 5 ne context window ko shared desk kaha, aur uske tenants list kiye. Claude.ai almost har tenant
ke liye control surface deta hai. Yeh section appendix ka dil hai — chaar features asal mein **ek**
feature hain (sahi text ko sahi waqt desk par rakhna), chaar naamon mein.

**Account instructions.** Settings mein "Instructions for Claude" ek text field hai jo **har**
conversation par apply hoti hai. Mechanically, yeh text hai jo product aapke pehle word se pehle desk
par rakh deta hai, system prompt ke paas. Rule: **sirf woh likho jo har conversation ke liye sach ho**
— aap kaun ho, kaunsa tone chahiye, "agree karne ke bajaye push back karo." Topic-specific cheezein ek
level neeche, projects mein dalo.

**Projects.** Ek project ek folder hai do superpowers ke saath: apni **instructions** (sirf uske andar
ki chats par) aur apni **knowledge files** (documents jo project ke andar sab chats dekh sakti hain).
Mechanically: project ek **pre-loaded desk** hai. Free accounts ko 5 projects milte hain; paid
accounts ko unlimited. Jab project ki knowledge context window se bari ho jaye, product sirf relevant
parts fetch karne lag jata hai — Idea 5 ka wohi progressive-disclosure trick, aapki apni documents par
apply.

**Memory.** Settings > Capabilities mein on kar sakte ho. Mechanism Idea 2 ke note mein mil chuka —
weights nahi badaltay; kuch nahi badal sakta. Product periodically aapki chats ko ek note mein
summarize karta hai, aur har naye conversation ke shuru mein wapis desk par rakh deta hai. Teen
controls: aap Claude ko directly bata sakte ho kya yaad/bhool rakhna hai; memory settings khol kar
parh/delete kar sakte ho (schedule par karna worth hai, kyunke note purani baaton ko bhi save rakhta
hai jo ab sach nahi rahi); **incognito** toggle memory bilkul skip kar deta hai.

**Chat history aur past-chat search.** Ek chat ke andar, history exactly Idea 5 ki tarah kaam karti
hai. Chats ke across, product ek search deta hai: aap Claude se poochh sakte ho pichle hafte kya kar
rahe the, aur yeh stored transcripts search kar ke relevant thread current desk par la deta hai. Yeh
mechanically **memory nahi, retrieval-then-context hai** — Idea 8 ka wohi move.

> **A.5 ka one-liner:** Account instructions har desk par note hain; project ek pre-loaded desk hai;
> memory ek self-updating note hai; history transcript replayed hai. Chaar features, ek mechanism:
> sahi scope par desk par kya land karta hai control karna.

## A.6 — Desk Par Cheezein Rakhna: Uploads

**+** button (ya drag-and-drop) files upload karta hai: PDFs, images, spreadsheets, code, lambe
contracts. Har upload tokens mein convert ho kar window mein rakha jata hai (Idea 4), is liye 200-page
report genuinely model ke saamne baithti hai, aur analysis quality summary paste karne se zyada acha
hota hai — model sirf woh use kar sakta hai jo desk par hai (Idea 5).

Do boundaries: images ke andar fine print/small detail weak rehti hai tokenization ki wajah se (Idea
4) — patch ek chunk hai. Aur Claude images parh sakta hai lekin conventional photos/illustrations
generate nahi karta — Claude.ai mein photo-style image generation nahi hai. Diagrams, charts, SVG
graphics, interactive visualizations code likh kar bana sakta hai (Artifacts mechanism, agla section).

## A.7 — Desk Se Cheezein Nikalna: Artifacts Aur Files

Jab aap kuch substantial mango (document, webpage, code, diagram, interactive tool), Claude use
**Artifact** ki tarah produce karta hai: chat ke saath ek dedicated panel jahan output ek "cheez" ki
tarah rehti hai, scrolling text nahi. Aap surgically iterate karte ho ("teesra section badlo," "button
neela karo") poori cheez regenerate karne ke bajaye, aur finished artifacts apni tab mein collect ho
jate hain aur link se share ho sakte hain unke saath bhi jinka Claude account nahi hai.

Code execution aur file creation Settings mein on karne se artifacts **real files** tak extend hote
hain: Word documents, working formulas wali Excel spreadsheets, PowerPoint decks, PDFs — computer par
download-able. Mechanically yeh poora section Idea 8 ko visible banata hai: model code/content
predict karta hai, tool use real mein chalata/render karta hai, result aapke paas ek working object ki
tarah wapis aata hai.

## A.8 — Tools Menu: Search, Research, Skills, Connectors

Chaar tools, ascending order mein ke kitna Idea 8 wala loop chalate hain.

**Web search** usually default on hota hai, aur frozen weights (Idea 2) ko current facts se rescue
karta hai. Ek catch: model hamesha realize nahi karta ke search karna chahiye — jahan current-ness
zaroori ho aur zaroorat sawal se obvious na ho, explicitly bolo "web search karo."

**Research** (paid-plan feature) web search hai jo poora agent loop chalata hai: sawal diye jane par,
Claude strategy plan karta hai, kayi searches chalata hai jo ek doosre par build karte hain, sources
ke across parhta hai, aur ek structured, cited report deta hai — minutes lagte hain, seconds nahi.
Rule of thumb: fact chahiye to web search, action-able document chahiye to Research.

**Skills** — Idea 5 mein mechanism level par mil chuke: expertise ke folders jo desk se bahar rehte
hain aur request match hone par load hote hain. Product mein Anthropic built-in skills ship karta hai
(documents, spreadsheets, presentations professionally behave karte hain inki wajah se), aur aap apni
khud bhi bina scratch se likhe bana sakte ho: Claude ko workflow batao, uske interview questions ka
jawab do, achi output ki ek example attach karo, aur yeh skill file draft kar deta hai. Doosra path
isse bhi behtar hai: jab chat ka back-and-forth exactly wahi output produce kar de jo chahiye tha,
bolo "isko skill mein badal do," aur Claude refined process draft kar deta hai reuse ke liye. Dono
tareeqon mein, drafting deployment nahi hai: generated skill file review karo, skills settings mein
install/enable karo, aur test karo ke matching request use actually trigger karti hai — jis skill ki
description aapke phrasing se match nahi karti, wo kabhi fire nahi hogi.

**Connectors** — Claude ko aapki real apps (Google Drive, Gmail, Slack, Calendar, aur lambi directory)
se Idea 8 ke MCP standard par wire karte hain: standard plug, per-service ek appliance, results desk
par har tool result ki tarah aate hain. Permissions deliberately grant karo: connector aapke actual
data tak scoped access hai, aur permission screen click-through karne ka waqt nahi, parhne ka waqt hai.

## A.9 — Ek 30-Minute Setup

Yeh steps ek baar, order mein karo, aur is course ka har major idea product ke andar exercise ho jayega.

1. **Account banao, teen controls dhoondo** (A.2 se): prompt box, model selector, thinking control.
   (Ideas 5, 2, 9.)
2. **Account instructions likho**: 3-4 sentences jo har conversation ke liye sach hain. Aap kaun ho,
   kaunsa tone chahiye, aur ek line jaisi "jab lagey main ghalat hoon, agree karne ke bajaye push back
   karo." Yeh line Idea 6 ki trained-in agreeableness ka direct counter hai.
3. **Ek project banao** apne sabse repeated stream of work ke liye. Instructions aur 2-3 knowledge
   files do: ek-page brief, achi output ki example, constraints. (Idea 5: pre-loaded desk.)
4. **Memory ke baare mein decide karo.** On karo agar self-updating note help karta ho; incognito
   toggle kahan hai jaan lo. Monthly reminder rakho note prune karne ke liye. (Idea 2: re-fed note.)
5. **Ek artifact banao**: chhota interactive tool ya formatted document mango, do baar iterate karo.
   (Idea 8: predict, render, refine.)
6. **Ek deep dive chalao.** Paid plan par, ek Research task chalao kisi aisi sawal par jo aapko waqai
   pasand ho, progress panel khol kar loop dekho. Free plan par, ek web-search sawal chalao jisko kayi
   sources chahiye. (Idea 8, in the open.)
7. **Ek skill banao** kisi weekly-repeat workflow se, interview se ya "isko skill mein badal do" se.
   Draft review karo, enable karo, test karo ke fire hoti hai. (Idea 5: expertise jo desk visit karti
   hai.)

30 minutes ka setup, aur product text-box hona chhor kar system ban jata hai.

## A.10 — Kya Badalta Hai, Kya Nahi

Is appendix mein sab kuch age hoga. Model naam badalte hain, prices move karti hain, buttons migrate
hote hain, features preview se default tak graduate hoti hain. Jab yeh page aur live product disagree
karein, product sahi hai — [Claude Help Center](https://support.claude.com/en/) aur
[Anthropic ki prompt-engineering docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
current sources hain.

Jo age **nahi** hoti wo mapping hai. Har control jo aap kabhi milenge, is product mein ya kisi doosre
mein, 9 ideas mein se ek par handle hai: frozen weights ke sets ke darmiyan selector, kitni reasoning
desk par jaye uska dial, sahi scope par text window mein rakhne ka mechanism, ya loop mein wire kiya
gaya tool. Jab koi naya feature ship ho aur tutorials scramble karein usko explain karne ke liye, yeh
test chalao jo yeh course ne sikhaya: *yeh desk ka kaunsa tenant hai, ya loop ka kaunsa step hai?*
Aap usually tutorials se pehle jawab jaan chuke honge.

## Sources and Further Reading

- **Anthropic's prompt engineering documentation** ([platform.claude.com](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)) — official, current guidance.
- **The Claude Help Center** ([support.claude.com](https://support.claude.com/en/)) — plans, limits, personalization, Skills, Research ka authoritative source.
- **OpenAI, "What are tokens and how to count them"** ([help.openai.com](https://help.openai.com/en/articles/4936856)) — token-to-word ratio ka standard reference (Idea 4).
- **Ouyang et al., "Training language models to follow instructions with human feedback" (2022)** ([arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155)) — instruction tuning aur RLHF ka paper (Ideas 2, 6).
- **Dell'Acqua et al., "Navigating the Jagged Technological Frontier" (2023)** — jagged frontier ko naam aur measure karne wala study (Idea 7).
- **Andrej Karpathy, "Intro to Large Language Models" (2023)** — is course ke baad agli depth ke liye best video, bina heavy math ke.

---
[⬅ Recap + Practice Prompts](04-recap-and-practice-prompts.md) · [⬆ Index](README.md)
