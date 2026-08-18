# 01 — Part 1: How AI Knows Things (Concepts 1-3)

Ek baar aap samajh gaye ke jab aap AI se sawal poochte ho to asal mein kya ho raha hai, aap failures
se surprised hona band kar dete ho.

## Concept 1 — Novice vs Power User

Dekho kya badalta hai do prompts ke darmiyan. Sawal same hai; briefing nahi hai.

- **Car khareedna.** Novice: "kaunsi car best hai?" Power user: spec sheets, dealer quotes, insurance
  plans upload karta hai, phir poochta hai "trade-offs kya hain? sab parho aur think hard karo."
- **Self-review at work.** Novice: "meri boss ke liye self-review likho." Power user: project tracker
  ka screenshot, recent project docs, aur notes ka voice memo upload karta hai, phir draft mangta hai.
- **Business idea critique karna.** Novice: "mera ek great business idea hai, mobile tie-dyeing,
  critique karo." Yeh sycophancy bait hai — AI zyada tar taarif hi karega. Power user: "Objectively
  analyze karo. Yeh rubric use karo: kya koi real problem hai, kya market hai, kya competitive
  advantage hai?" AI ne wahi idea ko 100 mein se 8 score diya aur wajah batayi.
- **Blog post likhna.** Novice: "BlackBerry ke baare mein blog post likho." Result: AI slop — fluent
  surface, andar khaali. Grammatically clean, "in today's fast-paced world" jaisi phrases se bhara,
  aur ek ghante baad reader ko kuch yaad nahi rehta. Yeh AI default mein produce karta hai jab aap koi
  context ya constraint na do. Power user: pehle outline, outline critique, har heading ko bullets mein
  expand, bullets critique, tab jaake prose mango.

Mental model jo inko jorta hai: **AI ek bohat smart fresh college grad jaisa hai. Highly motivated.
Aapke baare mein abhi zyada nahi jaanta.** Usko waise hi brief karo. Kya ek naya colleague ke paas
itni information hoti ke wo yeh kaam achha kar sake? Agar nahi, to usko zyada do.

## Concept 2 — Pretrained Knowledge

AI ne duniya ko *experience* kar ke nahi seekha. Iska koi body nahi, senses nahi, duniya mein ghoomne
ka koi waqt nahi. Isne duniya ke baare mein text parh kar seekha — internet ka bohat bara hissa.
Reddit, Quora threads, Wikipedia, books, news, research papers, blogs, forums.

Training data mein frequency roughly answer ki reliability ke barabar hai:

- **Strong:** cooking, celebrity gossip, common medical advice, top-1000 movies, popular programming
  languages, Voyager 1 record par kya hai, cats deewaron ko kyun ghoorti hain.
- **Sparse:** quasars, Cantonese (internet text ka 0.1% se bhi kam), regional history, niche
  professional knowledge.
- **Absent:** aapki company ka secret data, aapka private calendar, model ke knowledge cutoff ke baad
  publish hui koi bhi cheez, koi bhi cheez jo kisi ne kabhi public internet par dali hi nahi.

Do practical consequences:

**Typos fix karne mein waqt zaya mat karo.** AI internet text par trained hai, jo typos se bhara hai.
Yeh misspelled prompts ko gracefully handle karta hai.

**Absorbed errors se hoshiyar raho.** AI ne unhi sources se misconceptions aur outdated information
bhi absorb ki hai. Ek confidently ghalat forum post, model mein confidently ghalat ban jati hai.
Kuch important check karo primary source ke against.

Ek quick mental test kisi bhi pretrained answer par trust karne se pehle:

| Question type | Training data mein kitna well-represented? | Trust level |
| --- | --- | --- |
| "Roux kaise banayein?" | Cooking internet ke sabse zyada discuss hue topics mein se hai | High |
| "Top-1000 movie ka plot" | Hazaron baar review hui | High |
| "Kisi obscure village ki history" | Shayad sirf ek Wikipedia paragraph, ya kuch nahi | Low; primary source se verify karo |
| "Aapki industry mein recent regulatory change" | Almost certainly knowledge cutoff ke baad | Web search ke bina kuch trust mat karo |
| "Hamari company ne pichle quarter kya decide kiya" | Training data mein bilkul nahi | Kuch trust mat karo; model guess kar raha hai |

Yeh koi rule nahi jo memorize karna ho. Yehi wahi instinct hai jo aap kisi bhi doosre source par apply
karte: "yeh insaan yeh kaise jaanta hoga?" AI par bhi apply karo.

**Example — regional folk game.** Ek reader ne AI se apni dadi ke gaon mein khela jane wala regional
folk game ke rules poochhe. AI ne confidently teen paragraphs rules ke produce kiye. Dadi se poocha to
maloom hua rules almost bilkul ghalat the: AI ne doosre regions ke milte-julte games ki descriptions
blend kar di thi kyunke yeh specific game internet par barely tha. AI ne jhoot nahi bola; usne sparse
data se generalize kiya. Reader ki galti poochna nahi thi, balke yeh assume karna thi ke confidence
accuracy ke barabar hai.

## Concept 3 — 3 Retrieval Modes: Pretrained, Web Search, Deep Research

Jab aap sawal poochte ho, modern AI tools chupke se decide karte hain kaise jawab dena hai. Ya to wo
sirf pretrained knowledge se jawab dete hain, ya web search chala kar kuch pages parhte hain, ya deep
research chalate hain — jahan wo kayi minutes lagakar dozens sources scan karte hain aur ek structured
report likhte hain.

Aapko yeh jaan-na chahiye ke kaunsa mode fire ho raha hai, kyunke har ek ki apni strengths aur failure
modes hain.

- **Pretrained achha kaam karta hai:** "cats deewaron ko kyun ghoorti hain," "Hamlet ka plot," "Voyager
  1 record par kya hai." Yeh week-to-week nahi badalte.
- **Web search stale model ko rescue karta hai:** har model ka knowledge cutoff date hota hai; jo bhi
  uske baad viral hua wo model ke liye invisible hai. Web search ke saath, AI ek recent article pull
  karta hai aur sahi jawab deta hai.
- **Web search ghalat bhi ho sakta hai:** ek dost ne poocha "Henderson, Nevada mein kahan run karein."
  AI ne 20-saal purani web page cite ki aur ek school recommend kiya jo ab public ke liye khula nahi
  hai. Web search yeh check nahi karta ke sources current hain ya nahi.
- **Deep research wait ke laayak hai:** "hamare neighborhood mein Halloween haunted house plan karo,
  permits, fire safety, noise ordinances sameet." AI ek research plan propose karta hai, kayi parallel
  searches chalata hai, summarize karta hai, decide karta hai aage kya dig karna hai, aur ek
  multi-section report checklists ke saath produce karta hai.

> **Web search actually kaise kaam karta hai (aur kabhi kabhi pages kyun misread karta hai):**
> Ek **search-and-retrieval layer** searches chalata hai, result list scan karta hai, sabse relevant
> pages pull karta hai, aur har ek ko ek short passage/summary mein reduce karta hai — often yeh layer
> ek separate, chhota model hota hai. Sirf reduced version aapse baat karne wale model tak jata hai.
> Model aapse baat karta hua original page seedha nahi parhta — condensed version parhta hai. Isi liye
> yeh kabhi kabhi page ne asal mein kya kaha, usko misrepresent karta hai. **Fix:** AI ko batao kis
> tarah ke sources use karne hain ("WHO, FDA, EMA, aur peer-reviewed studies use karo. Forums ya
> personal blogs nahi"), aur AI se source quote karwao ("har claim ke liye exact sentence quote karo
> jo usko support karta hai").

**AI vs Google.** Yeh same tool nahi hain. Quick scans ke liye, kisi specific known site par jane ke
liye, ya kuch khareedne ke liye Google use karo. Jab synthesis chahiye ho — pros/cons, multi-source
comparison, written-out analysis — AI use karo. Choice is ke aapko link chahiye ya answer.

| Task | Google Se Behtar | AI Se Behtar |
| --- | --- | --- |
| "Form 1040 ka official IRS page dhoondo" | Haan — aap ek specific known site par jana chahte ho | Nahi |
| "Teen diabetes medications compare karo, recent evidence ke saath" | Slower — 8 tabs parhne parenge | Faster — AI ek jagah evidence synthesize karta hai |
| "2018 ThinkPad ke liye replacement charger khareedo" | Haan — aap product link chahte ho | Nahi |
| "6-saal ke bachche ke saath 4-din Lisbon trip plan karo, museums nahi" | Slow | Fast — AI constraints integrate karta hai |

Agar aapka sawal "X kahan hai" hai, Google use karo. Agar aapka sawal "yeh sab dekh kar mujhe kya
sochna chahiye" hai, AI use karo.

---
[⬅ Overview](00-overview.md) · [⬆ Index](README.md) · [Agla: Part 2 — Talking to AI Well ➡](02-talking-to-ai-well.md)
