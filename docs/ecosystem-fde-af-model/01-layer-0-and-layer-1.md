# 01 — Layer 0 Aur Layer 1: Foundation Aur SoR Kernel

Har layer do sawalon se define hoti hai: **yeh kya produce karti hai, aur kaun isay consume karta hai?**
Agar dono ka jawab na de sako, jo cheez describe kar rahe ho woh kisi doosri layer mein belong karti hai.

Do cheezein saaf karna zaroori hai pehle. **"System of Record"** teen scopes par use hota hai — inhe alag
rakho:

| Term | Matlab | Example |
| --- | --- | --- |
| **Machinery** | Technical foundation jis se SoRs banti hain | Postgres, pgvector, MCP, authentication |
| **Kernel** | Ek reusable System of Record component | Layer 0 se assemble ki hui standard SoR software |
| **Instance** | Ek deployed System of Record, specific content ke saath | Is book ka SoR, client ki manual, ek Accounting SoR |

Layer 0 machinery banata hai. Layer 1 reusable kernel deta hai. Kernel se kai instances ban sakti hain.
Generic instances (jaise is book ka SoR ya client ki manual) Layer 1 par hain. Profession-specific
instances (jaise Accounting SoR) Layer 3 par hain.

Doosri cheez: yehi paanch-layer stack teen tarah se dekha ja sakta hai — **technical view** (kya bana),
**talent view** (kaun banata/chalata hai), **revenue view** (kaun kaise kamata hai). Layer definitions
neeche technical view use karte hain.

Poore chapter mein ek graduate, **Ayesha** (Lahore se), ko follow karenge har layer ke through — italic
mein ek line har layer ke liye batati hai uska Ayesha ke liye matlab.

## Layer 0 — Foundation Framework

Plain words mein: yeh technical machinery hai jis se upar sab kuch banaya jata hai. Yeh already running
hai, to isse upar koi isay dobara nahi banata.

**Produce karta hai** — insaan aur agents dono ke liye Systems of Record banane ki reusable machinery,
char parts:

- **Writing aur publishing** — content Markdown mein likha jata hai, Docusaurus se publish hota hai, to
  wahi source ek website bhi hai jo insaan directly parhte hain.
- **Meaning se dhoondna** — pgvector Postgres par content index karta hai, to meaning se search ho sakta
  hai, sirf keywords se nahi.
- **Content ko agents tak serve karna** — MCP (Model Context Protocol) agents ko tools call karne aur
  wahi content parhne deta hai. Yeh ek open standard hai.
- **Kaun pooch raha hai, yeh check karna** — Better Auth single authorization server ki tarah kaam karta
  hai. JWT/JWKS verification har network boundary par identity aur permissions confirm karti hai.

**Consume karta hai:** MCP component builders. Layer 0 kisi bhi subject ke baare mein kuch nahi janta —
yeh khaalis infrastructure hai, patterns aur machinery, koi content nahi.

Yehi us sawal ka jawab hai jo har FDE practice ko shuru se pehle poochna padta hai: *kya mere paas
platform hai, ya kya main ek banane ka invest karunga?* Zyada tar graduates akele "nahi" jawab dete, is
model mein woh **"haan" jawab dete hain kuch banaye bina**, kyunke Layer 0 aur 1 already chal rahe hain
aur Panaversity unhe operate karti hai. Graduate ke apne shared assets upar hain: method System of
Record jo usay diya jata hai, aur domain builder jo woh aur uska expert Layer 3 par khud maalik hote
hain.

> *Ayesha ke liye, yeh layer machinery hai jise usay kabhi banana nahi parta — yeh already chal rahi
> hoti hai jab woh shuru karti hai.*

## Layer 1 — Content System of Record Component (SoR Kernel)

Plain words mein: yeh koi bhi content (book, rulebook, manual) ko ek source of truth mein badal deta hai
jise insaan aur AI agents dono parh aur trust kar sakte hain.

**Produce karta hai:** SoR kernel, do shapes mein. Pehla, kernel already ek service ki tarah chal raha
hai: [Agent Factory System of Record](../ecosystem-system-of-record/README.md) — yeh is book ko dono
readers ko serve karta hai. Doosra, aap kernel apni content ke saath run kar sakte ho. Apna Markdown
corpus load karo aur apna khud ka governed System of Record milta hai — jaise ek Accounting System of
Record ya Core Banking System of Record.

Dono shapes mein kernel [semantic retrieval](../ecosystem-system-of-context/README.md) MCP par deta hai
— meaning se dhoondna, sirf exact keywords se nahi.

> **Akela retrieval System of Record nahi hai.** Content ko ek named owner, version control, review aur
> approval, access control, aur citation support bhi chahiye. Kernel governance ke liye technical
> features deta hai, lekin har instance ka owner governance process khud define aur operate karta hai.
> Bina trusted source material ke, agents information invent kar sakte hain. Iske saath, woh verified
> knowledge par act kar sakte hain.

**Consume karta hai:** Layer 2 ke ecosystem builders, Layer 3 ke vertical builders, aur koi bhi jise
apna source of truth chahiye. Clients ke liye instances banana aur govern karna graduate earning ladder
ki **pehli rung** hai. Ek boundary rungs ko alag rakhti hai: client SoR build ek content service hai, koi
Workers nahi, koi outcome contract nahi. Jaise hi engagement manufactured Workers aur ek contract of
success add karta hai, yeh Layer 4 ka kaam ban jata hai.

Yeh horizontal move hai: **ek component, kai corpora.** Agent Factory ka [System of Record](../ecosystem-system-of-record/README.md)
kernel ka pehla deployed instance hai. Ek accountancy corpus, ya ek bank ki policy manual, isi kernel ki
doosri instance hai.

Do properties har instance mein hoti hain. Pehla, ek domain instance sirf reference material nahi —
usme us domain ke crash courses bhi hote hain: AI agents, workers, aur AI-native companies banane ki
teaching content. Doosra, instances **pair** hoti hain. Har instance MCP bolti hai, to generic Agent
Factory SoR (jo method sikhati hai) kisi domain instance ke saath compose ho sakti hai. Ek source method
sikhata hai, doosra domain, aur agent ya student dono ek saath parhte hain.

Yehi pairing us sawal ka jawab bhi hai ke ek vendor-neutral FDE client mein **kya carry** karke jata hai
— *What You Carry In* isay poora explain karta hai. Vendor ka FDE vendor ka platform carry karta hai.
Humara **do Systems of Record** carry karta hai. Pehla method hai, jo usne khud nahi banaya: deployed
[Agent Factory System of Record](../ecosystem-system-of-record/README.md), gehri aur already governed,
Lahore ki firm par bhi wahi jo Chicago ki par. Doosra profession hai, jo usne khud banayi: uski apni
domain instance, ek vertical aur ek jurisdiction se bandhi, sirf uski.

Yehi wajah hai domain instance chota shuru ho sakti hai. Isme method bilkul nahi hota — spec, evaluation,
deployment, oversight sab pehle se pehli System of Record mein hai. Domain instance sirf woh rakhti hai
jo profession add karti hai: law, standards, expert ke procedures, invariants, decision map.

> *Ayesha ek training manual kernel mein load karti hai aur shaam tak ek searchable, citable source
> paati hai. Slow hissa governance hai: owner naam karna, review set up karna, decide karna kaun kya
> parh sakta hai.*

---
[⬅ Yeh Model Kahan Se Aaya](00-where-the-model-comes-from.md) · [⬆ Index](README.md) · [Agla: Layer 2 Aur Layer 3 ➡](02-layer-2-and-layer-3.md)
