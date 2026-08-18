# 01 — The Generalist Core

Chaar core roles ek **single pipeline** ki tarah chalti hain, intent se production tak:

> **Outcome Architect (kya)** → **Digital FTE Builder (build)** → **AI-Native Company Architect
> (system)** → **Cloud AI Engineer (run)**

Isay apni company ke andar chalao aur yeh chaar roles hain. Isay ek client ki company ke andar
chalao, ek embedded vendor-neutral engineer se end-to-end carry karo, aur yeh **Forward Deployed
Engineer** ban jata hai. Baqi sab is line ko support, extend, ya bound karta hai.

## Outcome Architect — Intent Owns Karta Hai, Execution Nahi

Agent era mein kaam teen hisson mein bantta hai: intent, execution, verification. Worker execution
ka malik hai. Yeh role **intent** ka malik hai — yeh decide karta hai ke Worker ko kya achieve karna
chahiye, spec likhta hai jo isay pin down kare, "correct" ka matlab set karta hai, aur prioritize
karta hai ke kaunse Workers pehle banayein: woh insan jo **kya aur kyun** ka jawab deta hai, isse
pehle ke Builder **kaise** ka jawab de.

Software history mein zyadatar waqt slow hissa **banana** tha. Coding agents ne yeh tor diya — ek
engineer ab pehle se kai guna zyada ship karta hai, kyunke agent banane ka kaam karta hai. Lekin us
speed ne ek naya slow hissa expose kar diya: agar ek engineer paanch cheezein ek sath bana sakta
hai, to koi to decide kare kaunsi paanch cheezein banane layak hain — aur itni clarity se likh de ke
agent execute kar sake. Yehi deciding hi is role ka **intent** hai, aur yeh tez nahi hui.

Ek number mein poori shift: companies pehle roughly **ek product manager har aath engineers ke
liye** rakhti thin. Har engineer ka output multiply hone se, wahi ek insan ab bees ke kaam ko feed
kar raha hai. **Building scale hui. Deciding nahi hui.** Isliye deciding hi bottleneck ban gayi —
woh point jis par baqi sab wait karta hai.

Market isay dekh kar sochti hai ke product managers ki kami hai. Yeh book alag padhti hai: yehi
woh moment hai jab Outcome Architect — woh role jo intent ka malik hai — company ki sabse zaroori
seat ban jata hai.

**Book isay poora train karti hai:** spec-driven development, apne core mein, wahi discipline hai
jo aisi intent likhne ki hai jispar Worker ko hold kiya ja sake.

## Digital FTE Builder — Unit Product, End-to-End

Market isay AI Engineer kehti hai — catch-all term us insan ke liye jo AI components se applications
banata hai aur AI coding agents drive karta hai. Is book ka naam sharper hai, kyunke jo cheez aap
banate ho woh sharper hai: **Digital FTE**, woh unit jis se poori company assemble hoti hai. Yeh
book ka primary graduate hai. Yeh poori spine train karti hai: spec-driven development, SKILL.md
authoring, agent architecture, tool aur MCP interfaces, evaluation, aur human oversight — deployment
itna ke ship ho sake, aur depth Cloud AI Engineer ke liye chhori gayi.

## AI-Native Company Architect — Company Design Karta Hai, Akela Worker Nahi

Poora enterprise: Two-Layer Model, management layer, workforce, events carry karne wala nervous
system, aur system of record jis par sab chalta hai. **Agent Factory** process hai jo yeh architect
practice karta hai. **AI-Native Company** product hai jo woh ship karta hai. Book iska canonical
source hai. Paanch-quarter Certified Agentic AI Architect program iska credential hai.

## Cloud AI Engineer — Jo AI Worker Aur Company Ko Production Mein Chalata Hai

Digital FTE banana kaam ka aadha hissa hai. Usay reliably chalana doosra hai — aur poori AI-Native
company ko bhi chalana. Jahan AI-Native Company Architect enterprise design karta hai, yeh role isay
operate karta hai: Workers, management layer, aur nervous system ko real cloud infrastructure par
deploy aur scale karna — Azure Container Apps ship karne ke liye, Inngest durable execution ke
liye, Dapr aur Kubernetes scale ke liye. Yahin system prototype hona chhod kar ek dependable company
ban jata hai.

---
[⬅ The Question Behind Every Title](00-the-question-behind-every-title.md) · [⬆ Index](README.md) · [Agla: The FDE — Why Palantir Needed It ➡](02-the-fde-why-palantir-needed-it.md)
