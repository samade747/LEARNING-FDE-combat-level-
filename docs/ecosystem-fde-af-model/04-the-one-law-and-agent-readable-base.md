# 04 — Ek Law: Repeated Work Neeche Jata Hai — Aur Agent-Readable Base

## Ecosystem Khud Pehla Proof Hai

Ek cheez notice karo: ecosystem khud **model apne aap par apply kiya hua hai** (ek recursion). Layer 2
FDE AF Model sikhata hai, aur Layer 2 khud FDE AF Model se bani hai. Iski System of Record Layer 1 ka
pehla deployed instance hai. Iske live gateways (Zia Tutor AI aur Zia Developer AI) Layer 2 components
compose karte hain. Iska content usi tareeqe se assemble hua jo yeh book aapko sikhati hai.

Proof sirf diagram nahi hai. Model par bane products already chal rahe hain. [Zia Tutor AI](../ecosystem-zia-tutor-ai/README.md)
kholo aur is page ke baare mein ek sawal poocho, ya apna agent [System of Record](../ecosystem-system-of-record/README.md)
se connect karo. Aisa karte hue aap Layers 0 se 2 use kar rahe ho.

## Ek Law: Jo Repeat Ho, Neeche Move Ho

FDE literature mein ek warning sabse upar hai, aur sabse sharp version Kevin Bai se aata hai (jinhone
Palantir mein FDE engagements lead kiye, phir Rippling ki FDE function pehli hire ki tarah banayi). Unka
jawab: agar har engineer scratch se banaye, aapke paas FDE function nahi — ek **dev shop** hai. Yeh
profitable ho sakta hai, lekin alag business hai, aur maintenance cost aakhir mein profit kha jaati hai.
FDE function isay isliye banata hai kyunke engineers kabhi scratch se software nahi likhte — ek set of
shared primitives already exist karta hai, aur engineer unhe assemble karta hai. To FDE AF Model ka ek
law hai, aur yeh optional nahi:

> **Jo cheez ek layer par repeat ho, usay us se neeche wale layer mein promote karne ke liye evaluate
> karo.**

Promotion ka matlab hai ek reusable capability ko neeche, shared layer mein move karna taake zyada log
use kar sakein.

- Ek Layer 4 customization jo teen ya zyada customers use karein, Layer 3 vertical ki candidate ban jati
  hai.
- Ek Layer 3 component jo kisi bhi profession mein useful ho, Layer 2 library ki candidate ban jati hai.
- Ek infrastructure pattern jo kai components ko chahiye, Layer 1 ya Layer 0 ki candidate ban jati hai.

Repetition sirf ek **review shuru karti hai**, automatic promotion nahi. Ek capability tab promote hoti
hai jab yeh saari conditions poori karti hai:

1. Koi confidential customer data nahi
2. Ek customer ke unique process se alag ki ja sake
3. Platform strategy mein fit ho
4. Security aur compliance review pass kare
5. Tests aur agent evaluations shaamil hon
6. Ek named long-term owner ho

Promotion ek fair customer sawal ka jawab bhi deti hai: *jis kaam ka maine payment kiya, woh aapke shared
platform ka hissa kyun bane?* Teen commitments customer ko protect karte hain:

1. **Clean-room promotion** — sirf general pattern shared layer mein jata hai; customer ka data aur
   confidential ontology Layer 4 par rehte hain
2. **Opt-in promotion** — engagement contract mein permission hona zaroori; promotion rights kabhi assume
   nahi hote
3. **Rewarded promotion** — jab customer ke kaam se ek reusable improvement banti hai, customer ko koi
   incentive milta hai (jaise lower ongoing fees)

Do companion rules isi principle ko doosri boundaries par apply karte hain: **Layer 2** par ek vertical
deployed generic products ko customize nahi karti — apne shared components se apna gateway banati hai.
**Layer 3** par ek customer ko domain builder ka alag fork nahi milta — ek versioned builder har company
ko serve karta hai.

Yeh law ek return path bhi banata hai: customer work se lessons neeche shared foundation mein jate hain
jab safe aur reusable hon. Versioned improvements phir wapas upar un products aur customer deployments
mein jati hain jo unhe use kar sakte hain. Field work isi liye paid delivery bhi hai aur platform R&D ka
source bhi.

Yehi law hai jis se ek graduate ki apni vertical System of Record **thin se thick** hoti hai — naye
outcomes expert ke saath derive kiye jate hain, aur repeated customer work safe hone par neeche shared
vertical mein jata hai. Ek cheez jo growth jaisi lagti hai lekin nahi: ek jurisdiction add karna ek naya
build hai, thicker version nahi, kyunke har jurisdiction ke apne rules aur apni ladders hoti hain, sirf
expert ki methodology share karte hue.

## Base Agent-Readable Hona Zaroori Hai

Ek aur zaroorat model ke centre mein hai: base ko AI agents ke liye samajhna aur use karna aasan hona
chahiye. Becker predict karta hai ke kaamyab software bases mein shuru se hi LLM ke liye zaroori context
hoga. Jensen Huang (NVIDIA CEO) ek related enterprise argument dete hain: agents ko authoritative sources
chahiye jinhe woh parh sakein, update kar sakein, check kar sakein.

Akela open-source repository kaafi nahi hai. Context ke bina code AI agent ko assumptions banane par
majboor karta hai. Ek governed System of Record code se zyada deta hai — versioned, citable source
material. MCP agents ko ek standard tareeqa deta hai isay access karne ka, jabke pgvector unhe meaning se
passages dhoondne mein madad karta hai.

Yahan yeh stack ek generic boilerplate se kyun behtar hai:

- **Versioned Markdown, stable identifiers ke saath** — passages predictable rehte hain. Wahi Markdown
  ek website ki tarah bhi publish hoti hai, to ek source dono readers ko serve karta hai.
- **MCP** — agent ko defined tools deta hai call karne ke liye, website scrape karne ke bajaye.
- **Better Auth, JWKS verification har boundary par** — confirm karta hai kaun request kar raha hai aur
  usay permission hai ya nahi. Yeh activity auditable banata hai — regulated customers ke liye zyada
  suitable.
- **Vector index aur governed corpus wahi Postgres system use karte hain** — retrieval source content ke
  version aur approval status ko follow karta hai. Ek agent us paragraph ko retrieve nahi kar sakta jise
  governance ne retire kar diya ho.

Inme se koi bhi property GitHub par pare code repository ke saath free nahi aati — har ek design ki gayi
thi.

---
[⬅ Layer 4](03-layer-4-customer-instances.md) · [⬆ Index](README.md) · [Agla: Business Model ➡](05-business-model-where-each-layer-earns.md)
