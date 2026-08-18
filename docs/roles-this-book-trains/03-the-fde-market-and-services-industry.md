# 03 — The FDE: Market Demand and the Services Industry

## Har AI Company FDEs Kyun Chahti Hai

FDE job postings **800% se zyada barh gayin** 2025 ki pehli teen quarters mein. Salesforce ne apni
Agentforce platform ke liye dedicated FDE team banayi. OpenAI ne "Deployment Company" banayi — ek
majority-owned subsidiary, taqreeban **$4 billion** investor consortium se backed, zyadatar
enterprises ko FDEs se staff karne ke liye.

2026 ke mid mein yeh model hyperscalers tak pohanch gaya: **AWS ne $1 billion commit kiya** ek nayi
Forward Deployed Engineering unit ke liye — 5-6 engineers ke pods, clients ke paas ~45-din
deployments ke liye. Do din baad **Microsoft ne jawab diya $2.5 billion aur 6,000 logon se**
(Microsoft Frontier Co.), Unilever aur Novo Nordisk jaise early customers ke sath. **Ek hafte mein,
do sabse bare cloud providers ne combined $3.5 billion ek hi job title ke peeche laga diye.**

**Wajah simple hai:** 2025 ka MIT Media Lab study (Project NANDA) batata hai ke taqreeban **95%
custom enterprise AI pilots koi measurable return nahi dikhate.** AI kaam nahi karti isliye nahi —
balke company ke messy, real-world systems mein isay fit karna intehai mushkil hai. FDEs isi gap ko
band karte hain. Yehi wajah hai Palantir late 2024 tak **$136 billion market cap** paar kar gayi,
Lockheed Martin ko overtake karte huay.

**Wahi study ek doosri baat bhi kehti hai:** outside partners ke sath chalne wale initiatives ~67%
waqt deployment tak pohanche, jabke poori tarah in-house build kiye gaye tools sirf ~33%. **Outside
expertise akele jaane se behtar hai** — lekin study yeh nahi test karti ke woh expertise vendor ke
platform se welded honi zaroori hai ya nahi. **Vendor-neutral teesra column hai jo abhi tak
almost-empty hai.**

**Kyun ab, 2012 mein nahi?** Bai ka hypothesis: taqreeban har platform ab **agentic** hai. Agentic
matlab customizable. Customizable matlab customer ko nahi pata product kya karta hai ya kahan tak
push ho sakta hai — jo har vendor ko us ek cell mein daal deta hai jise forward deployment chahiye.

**Numbers, honestly.** Indeed ne April 2025 mein 643 US FDE postings ginin, April 2026 mein 5,330 —
**729% ka izafa**, typical salary bands $170,000-$200,000+. Anthropic ke apne FDE postings
$200,000-$300,000 chalte hain. Market-wide median ~$190,000, range $160,000-$220,000. Senior/staff
FDEs frontier labs par $450,000-$600,000 clear karte hain. Do details zyada matter karti hain: postings
9 mahino mein 800%+ barhin jabke candidate pool sirf ~50% — ek **supply gap**. Aur verified FDE
roles mein se kisi ek mein bhi **sales quota nahi tha** — market FDEs ko engineers ki tarah pay
karti hai, salespeople ki tarah nahi.

## Services Industry Bhi Wahi Math Dekh Rahi Hai

Sanjeev Aggarwal (jinhone Daksh banayi — India ki BPO industry ke pioneers mein se ek) ne CNBC-TV18
par plainly kaha: FDE ek insan mein engineer, product manager, aur AI architect fuse kar deta hai
("almost ek unicorn... 10x engineer"), aur is fusion par ek firm **~100 FDEs se $100 million ka
business** bana sakti hai — woh kaam jo traditional IT services model 2,000-2,500 logon se staff
karta tha, **70-90% gross margins** par. Uska nateeja geographic hai: *"India can be the FDE
factory for the world."*

**Aur professional services firms apna product reprice kar rahi hain.** March 2026 mein, PwC ke US
CEO Paul Griggs ne Financial Times ko bataya ke firm billable hour se hat kar clients ko
AI-powered tools offer karegi jo bina PwC professional ke pehle steps mein use ho sakein — potentially
annual subscription se. **PwC One** naam se yeh platform ship hua, chhe automated services ke sath —
M&A due diligence se tax rules tak. Griggs saaf tha: senior log jo AI-first sochna nahi seekhenge,
unhein replace kar diya jayega.

Isay teen cheezon ki tarah padho: (1) Aggarwal ka arithmetic, doosri industry se confirm hua. (2)
Outcome-pricing claim, ek aisi firm se jiski economics billable hour par depend karti thin. (3) Ek
naya **cage** — PwC One ek platform hai, aur jo client baad mein rakhta hai woh usi par chalta hai —
wahi vendor lock-in jo agle part mein describe hota hai.

## Vendor Ke Andar Se Playbook

Pauline Brunet (Cursor ki global FDE team head) ne June 2026 mein apna playbook share kiya. Chaar
rules matter karte hain:

**Fit test.** Har engagement do axes par score hota hai: customer kitna digitally mature hai, aur
product kitna customizable hai. FDE **immature customer + deep customization** ke band mein rehta
hai.

**Staff-augmentation red flag.** Client jo kehta hai "we're understaffed" — yeh hours rent karne ki
request hai, capability transfer karne ki nahi. Brunet ka counter-move: "working team kaun hoga?"

**Directional scope.** Woh na open-ended engagements leti hai ("do FDEs, chhe mahine ke liye") na
fixed waterfall promises. Format: problem naam lo, KPI baseline naam lo, chhe-hafte ka directional
plan commit karo, aur client ke real systems se seekh kar pivot karo.

**ROI, teen sawalon mein.** Har engagement kam se kam ek sawal par khatam hona chahiye: humne revenue
barhaya, cost ghatai, ya risk kam kiya?

## Vendor Lock-In Problem

Har FDE Palantir mein Palantir ke platform par banata hai. Har FDE OpenAI mein OpenAI ke models par.
Har FDE Cursor mein Cursor ke SDK par. Engineer client ki company mein deep jaata hai, ek hi vendor
ka product sab jagah wire karta hai, aur chala jata hai. Baad mein switch karna waisa hi hai jaise ek
plumber jo sirf ek brand ki pipes lagata hai. Andrew Ng ne bhi note kiya hai ke clients aise FDEs
dhoondne mein struggle karte hain jo kisi ek vendor se bandhe na hon — kyunke role ka poora point,
vendor ke liye, client ko lock karna hai.

**Yeh book vendor-neutral FDE train karti hai** jise market maang rahi hai lekin mil nahi rahi. Method
kisi vendor se bound nahi. Graduate poori pipeline (intent specify karo, Worker banao, system design
karo, production mein chalao) client ki organization mein carry karta hai bina unhein kisi ek
platform mein lock kiye. Naya model agle quarter aaye ya sasta runtime agle saal — aap switch kar
sakte ho. Ek honest tradeoff: vendor ka FDE heavily subsidized hota hai (kabhi free), kyunke vendor
lock-in mein kama leta hai; vendor-neutral FDE client ya independent firm pay karti hai. **Yeh
feature hai, bug nahi** — client abhi optionality khareed raha hai, baad mein switching costs se
bachne ke liye.

## Sabse Mazboot Objection: Bina Platform Ke, Aap Dev Shop Ho

Bai khud strongest counter deta hai: agar har FDE scratch se sab banaye, to aapke paas dozens
repositories hain jinhein koi maintain nahi kar sakta — engineers resign kar jaate hain. Jo FDE
function banata hai, woh hai: engineers kabhi scratch se software nahi likhte. Shared primitives
pehle se maujood hain, aur engineer unhein customer ke liye assemble karta hai. **Bina iske,
maintenance cost profit khatam kar deti hai.**

Yeh vendor-neutrality ka bill hai. Vendor nikalo, aur shared primitives cage ke sath chali jaati
hain. Iska jawab agle part mein hai.

---
[⬅ Why Palantir Needed It](02-the-fde-why-palantir-needed-it.md) · [⬆ Index](README.md) · [Agla: Two Systems of Record aur Pod of One ➡](04-the-fde-systems-of-record-and-pod-of-one.md)
