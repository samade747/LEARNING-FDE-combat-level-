# 05 — Yeh Move Har Domain Ke Liye: Kit, Platform, Rules, 80/20

## Wahi Move, Kisi Bhi Domain Ke Liye

`/vsor` jo imply karta hai usay dekho. Agent Factory ka SoR koi one-off nahi hai. Yeh ek **repeatable
kernel ka pehla instance** hai. Wahi component kai alag collections of knowledge rakh sakta hai: ek
accountancy body of knowledge, ek bank ki policy manual, ek cuisine, ek curriculum. Kernel ek baar theek
karo, aur har instance usay inherit karta hai.

Yahan combination powerful ban jata hai. Agent Factory SoR sikhata hai **agents kaise banate hain**. Ek
vertical SoR sikhata hai **profession kya janti hai**. Dono ko jodo aur poori ecosystem ki general
equation ban jati hai:

**Agent Factory SoR + Vertical SoR = us vertical ke AI workers sikhane aur banane ke liye poori governed
knowledge.**

Sales ko pehli instance ki tarah lo:

**Agent Factory SoR + Sales SoR = sales AI workers aur sales Digital FTEs (poora role carry karne wale
AI employees) samajhne, sikhane, aur banane ke liye sab kuch.**

Yehi equation har domain ke liye kaam karta hai, aur har vertical ko Agent Factory ke jaise hi teen
cheezein milti hain: ek System of Record, ek tutor twin, ek developer agent. Sales SoR ko Accounting
SoR se badlo aur accounting AI workers mil jate hain. Agent Factory wala side kabhi nahi badalta. Sirf
vertical wala side badalta hai.

Pehli verticals jo build list par hain woh har company ke beech se guzarti hain: sales, marketing, human
resources, supply chain, aur inse aage, koi bhi profession jiska body of knowledge govern karne layak
ho.

## Ek Kit, Sealed Product Nahi

To aap ek khud banate kaise ho? Yehi book ka agla section hai, abhi in progress: **Building the Vertical
FDE Harness**. Iska method already likha aur live hai:
[apna vertical chuno](../ecosystem-choosing-your-vertical/README.md), phir
[uska System of Record first principles se design karo](../ecosystem-designing-the-vertical-sor/README.md).
Harness us method ko ek running system mein badal deta hai.

Poori ecosystem ki ek property yeh hai: yeh atomic, open-source components se bani hai jo **use hone ke
liye nahi, upar banaye jaane ke liye** hain. Vertical SoR framework, harness templates, sample
repositories jin se developer agent banata hai, book ke apne SoR ke neeche wale kernel patterns — har
ek ek shuruwaat hai jo aap le sakte ho, adapt kar sakte ho, aur maalik ban sakte ho. Stack mein kuch bhi
sealed product nahi hai. Yeh ek kit hai. Isse apna vertical assemble karo, aur jo assemble hota hai woh
aapka hota hai.

## Platform As a Plugin, Aur Cost Zero Ke Qareeb Kyun Hai

Poori shape ka team ke andar ek naam hai: **platform as a plugin**. Ek vertical kisi naye app ki tarah
ship nahi hoti jo kisi ko adopt karni pare. Yeh plugins aur connectors ki tarah aati hai un AI apps aur
coding agents par jo users already chala rahe hain, apna System of Record saath laate hue. Yehi wo cheez
hai jo economics ko har jagah kaam karati hai: plugins tools laate hain, aur **user apna model khud
laata hai.** Intelligence us free tier se aati hai jo woh already use kar rahe hain. Aapki cost ek chota
server aur database hai, to value sainkron logon tak scale hoti hai us LLM bill ke bina jo aam taur par
reach cap karta hai. Book yeh sab banana sikhati hai:
[Connector-Native Apps](../connector-native-apps/README.md), Plugins for AI Agents, RAG on Postgres.

## Chaar Rules Jo Iske Saath Chalte Hain

Yeh concept sirf technical nahi hai. Chaar business rules poori shape ke saath chalte hain, seedha
book ki spine se:

1. **Kabhi woh mat banao jo lock-in karta ho.** Bare labs ke forward-deployed engineers har client ko
   ek vendor ke platform mein lock kar dete hain. Yeh book **vendor-neutral vertical FDE** train karti
   hai.
2. **Proof pitch ki jagah leta hai.** Aapke paas koi salesforce nahi hoga, aur zaroorat bhi nahi: agentic
   era mein, **deployment hi sales motion hai.** Buyer ke apne data par banaya gaya working proof hi
   convince karta hai.
3. **Apna suitcase khud utho.** Aapka method aur aapki governed knowledge woh cheezein hain jo aap apne
   saath le kar jaate ho — assets jo aap own karte ho, koi access nahi jo kisi ne grant kiya ho.
4. **Apna vertical select karo, phir gehra jao.** Ek profession, ek expert partnership, ek System of
   Record jis par baaqi sab khada hota hai.

## Aakhri Step: 80% Bana Hua, 20% Customized

Pipeline mein ek aur step hai, aur yehi jagah hai jahan ecosystem real customers aur real careers se
milti hai.

Vertical developer agents general market ke liye finished products nahi banate. Woh vertical agents
banate hain jo taqreeban **80% complete** hote hain. Baaqi **20% ek specific customer ke liye
customization** hai: unka data, unke rules, unke integrations, aur woh unusual cases jo sirf unke paas
hain.

Isay concrete banao. Ek Sales SoR sales agent ka 80% deta hai: qualification method, discovery
questions, objection answers, follow-up rhythm. FDE ka 20% woh sab hai jo sirf is customer ke paas hai:
unke CRM fields, unki pricing limits, unki approval chain, aur woh ek rule jo sirf unki legal team
enforce karti hai.

SaaS era mein, ek product har customer ko serve karta tha, aur customization ka matlab settings aur
checkboxes tha, kyunke human developers real customization ko scale par bohot mehenga bana dete the.
Fully custom software tha, lekin sirf un customers ke liye jo bhaari qeemat de sakte the, aur har custom
build delivery par freeze ho jata tha — us din se improvements inherit karna band. AI dono taraf arithmetic
badal deta hai. Agents 20% ko har customer ke liye affordable bana dete hain. Aur 80% base sab ke liye
common rehta hai, System of Records se continuously update hota hua, to har deployment ship hone ke baad
bhi fixes aur improvements inherit karta rehta hai. **Hand-built software jaisa custom, SaaS jaisa
hamesha current** — agentic era pehli baar dono ek saath de sakta hai.

Is 80/20 split ko book ke **10-80-10 rule** se confuse mat karo — dono alag cheezein divide karte hain.
10-80-10 rule ek task ko divide karta hai ke kaun karta hai: insaan intent se shuru karte hain, AI
darmiyan execute karta hai, insaan judgment se band karte hain. 80/20 split product ko divide karta hai:
har customer ko milne wala shared core, aur ek customer ko chahiye customization. Dono nest karte hain.
Jab FDE 20% deliver karta hai, woh usi par 10-80-10 chalata hai.

---
[⬅ Yeh LMS Kyun Nahi](04-why-not-an-lms-and-zia-developer.md) · [⬆ Index](README.md)
