# 00 — The Shift

## Concept 1: Vibe Coding vs Spec-Driven Development

**Farq hai: aap sochte kab ho.**

**Vibe coding** mein aap AI ke banate **waqt** sochte ho — react kar ke pata chalta hai kya chahiye.
Fast lagta hai, lekin har round trip context kho deta hai, AI reasonable-but-wrong assumptions bharta
hai. **Cost baad mein, ek saath ati hai**, jab aap us cheez ko change ya trust karne ki koshish karte ho.

**Spec-driven development** mein aap **pehle** sochte ho, likh lete ho. AI banana shuru nahi karta jab
tak dono "done" ke matlab pe agree na karein. Build phir mostly **mechanical** hota hai — ek agreement
execute kar raha hai, guess nahi kar raha.

> **Rule of thumb:** agar result phenkne se aapko bura lagega, aap vibe coding ki safe limit se aage ja
> chuke ho. Spec likho.

## Concept 2: Spec Product Hai; Code Build Output Hai

**Yehi mental flip hai jo SDD ko naam deta hai.** Purana tareeqa: spec likho, cheez banao, spec phenk
do. **SDD ulta karta hai:** spec durable artifact hai jise aap maintain karte ho; code usse generate
hota hai, aur spec badalne pe **dobara generate** hota hai.

> **"Build output" ka matlab "black box" nahi hai:** Thoughtworks engineer Valentina Servile ka finding:
> jab agent tangled codebase se milta hai, zyada galat assumptions banata hai, zyada context jalata hai.
> **Spec batata hai system kya karta hai. Code hi honest evidence hai ke system kitna behtar hold ho
> raha hai.**

**Achi spec 3 sawal answer karti hai, order mein:**
1. **Why** — kaunsa problem solve kar rahe hain, kis ke liye?
2. **What** — done hone pe kya sach hona chahiye? Behaviors, inputs, outputs, rules, edge cases
3. **What NOT to build** — boundaries. Ye ek section zyada tar "usne bohat zyada kar diya" failures rokta
   hai

**Missing hai: HOW.** Spec behavior describe karti hai, implementation nahi. *"Users password reset kar
sakte hain emailed link se jo 30 minute mein expire ho"* spec hai. *"JWT aur Postgres table use karo"*
implementation hai — **plan** mein jati hai, baad ki phase mein.

> **Test har spec line ke liye:** *"Kya koi competent banda ye line satisfy karte hue galat cheez bana
> sakta hai?"* Haan to line **vague** hai, tighten karo. Spec **tab** finished hai jab kuch bhi
> **galat parhne layak** na bache.

## Concept 3: SDD Ke 3 Levels

| Level | Matlab | Kab Use Karo |
| --- | --- | --- |
| **Spec-First** | Spec ek dafa, shuru mein likho, phir build karo. Baad mein drift ho sakti hai | Zyada tar features. Default |
| **Spec-Anchored** | Spec source of truth rehta hai, behavior badalne pe update karte ho | Jo mahinon maintain karni hai |
| **Spec-as-Source** | Spec **hi** source hai, code poori tarah regenerate hota hai | Mature, high-discipline teams |

> **Ehtiyat:** Spec-as-Source ka claim sab se bara hai, field evidence sab se kam hai. Production mein
> agents-written systems decay **tezi** se hoti hain — agents rarely file ko usse behtar chhorte hain
> jitna unhe mila. **Har level jo Spec-First se upar hai, insaan ko periodically wapas dekhna chahiye.**

**Is course ke liye:** Spec-First se shuru karo, Spec-Anchored ki taraf badho.

---
[⬅ Index](README.md) · [Agla: The Method ➡](01-the-method.md)
