# 00 — The Shape

## Story: 40 Minute, 50 Dollar, Kuch Nahi

Ek agent 40 minute chalta hai. 50 dollar kharch karta hai. Kuch use hone layak nahi banata. Log parhte
ho — wahi 3 cheezein baar baar try ki thin, sirf lafz thore alag.

**Zyada tar log prompt badalte hain.** Ye pehli cheez hai jo dekhte hain, aur 10 second mein edit ho
sakti hai. Rewrite karte hain, run dobara chalate hain — wahi kaam **dobara** 40 minute mein hota hai.

**Prompt theek thi.** Us system mein kuch bhi ye notice karne wala nahi tha ke run progress karna band
kar chuki hai — isliye kuch usay roka nahi. Fix ~11 lafzon ka tha, **ek alag file mein**, ek aisi layer
pe jiska naam zyada tar log nahi jaante.

## Concept 1: Containers, Steps Nahi

Sab se common galti: in 4 lafzon ko **ladder** ki tarah draw karna — prompt neeche beginners ke liye,
loop upar experts ke liye. Ye tasveer wada karti hai ke ek dafa achhe ho gaye, neeche ki steps chhor
doge.

**Ye galat hai, aur mehnga tareeqe se galat hai.**

**Har beat abhi bhi ek prompt banati hai.** Ek loop jo 6 mahine se schedule pe, checker + spine ke sath
chal rahi hai, phir bhi din mein kai dafa model ko message bhejti hai. Agar wo message vague hai, loop
vague kaam **tezi se** produce karti hai, ek timer pe. **Aap kabhi inner layers chhorte nahi. Unhe
wrap karte ho.**

**3 galat beliefs jo is tasveer se ate hain:**
- **Outer ka matlab baad mein nahi hai** — order mein nahi banate, zyada tar waqt 3 rent karte ho, 1
  own karte ho
- **Outer ka matlab zyada zaroori nahi hai** — careless prompt ek khoobsurat engineered loop ke andar
  bura kaam schedule pe deti hai, receipt ke sath
- **Ye ek box ke 4 sizes nahi hain** — 4 genuinely alag objects hain

## Concept 2: Unit-of-Work Test

Har layer us **kaam ke piece** se define hoti hai jiska wo zimmedar hai. Ye 4 seedhe samjho, aur kisi
bhi layer ko jangle mein pehchan sakte ho — chahe koi usay kuch bhi naam de.

| Layer | Unit of Work | Plain Words |
| --- | --- | --- |
| **Prompt** | Ek model call | Jo aap ne type kiya aur enter dabaya |
| **Context** | Poori window | Model jo dekh sakta hai us waqt — message, files, rules file, tool results |
| **Harness** | Ek beat | Instruction se le kar agent khamosh hone tak — tool call, result parhna, phir se sochna |
| **Loop** | Poori run | Jab koi type nahi kar raha. Kuch beat shuru karta hai, kuch judge karta hai, kuch yaad rakhta hai |

> **Test jo vocabulary badalne ke baad bhi kaam karta hai:** Jab koi blog, vendor, ya job description
> "harness" ya "context engineering" ya "the agent loop" kahe, **lafz pe bahas mat karo.** Ye poocho:
> **"kaunsa unit of work discuss ho raha hai? Ek model call, window, ek beat, ya poori run?"**

Agar unka "harness" schedule bhi shamil karta hai, unhon ne is book ki 2 layers ko ek mein draw kiya
hai. Koi bhi galat nahi hai — **alag maps hain.** Ab aap translate kar sakte ho, confuse hone ki bajaye.

---
[⬅ Index](README.md) · [Agla: 4 Layers ➡](01-four-layers.md)
