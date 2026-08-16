# 00 — Part 1: The Shift (Concepts 1-3)

## Concept 1 — Teesra Paradigm: Aap Ab "Kaise" Design Nahi Karte

Computing ke 3 tareeqe rahe hain. **Batch** computing mein aap poora workflow pehle se specify karte
the aur wait karte the. **Command** computing (desktop, web, app) mein aap machine ko step-by-step
drive karte the — *kaise* pahunchna hai uska bojh aap par tha.

**Teesra paradigm** kism mein alag hai, degree mein nahi. Aap **outcome** state karte ho, agent steps
choose karta hai. "Kaise" ka bojh insan se machine ki taraf move ho jata hai.

**Yehi ulat-pher hai jispar course ke baaki sab concepts khare hain.** Jab aap steps design nahi karte,
aap 3 nayi cheezein design karte ho: banda kaise **intent express** kare, kaise **trust kare** un steps
par jo usne choose nahi kiye, aur kaise **recover** kare jab machine ghalat choose kare. Yaad rakho:
**intent, trust, recovery** — yehi poora course miniature mein hai.

## Concept 2 — 2 Audiences, Ek System

**Sabse zyada teams jo idea miss karti hain:** Aapka agentic product **do kism ke users** ek sath use
karte hain. Ek insan, jise samajhna aur trust karna hai. Aur **doosre agents** — jo aapki service call
karte hain, data parhte hain, kisi banda ki taraf se act karte hain. **Woh bhi users hain.** Woh sirf
pixels ki jagah structure parhte hain.

Industry ek confusing acronym (**AX**) use karti hai 2 alag halves ke liye:

| Term | Kisne Banaya | Matlab | Yeh Course Isay Bulata Hai |
| --- | --- | --- | --- |
| **Agentic Experience** | John Maeda | Insan ka delegate karne ka experience | **Human surface** (Part 2) |
| **Agent Experience** | Matt Biilmann (Netlify) | Agent ka aapke product ke user hone ka experience | **Machine surface** (Part 3) |

Dono real hain. Zyada tar courses sirf pehla sikhate hain. **Hum dono sikhate hain** — kyunki Digital
FTE jo aap ship karte ho, insan **aur** uske aas-paas ke agents dono use karte hain.

## Concept 3 — Interface Gayab Nahi Hota; Woh Move Hota Hai

Kuch log kehte hain agents interface design ka ant hain. Lekin dekho stakes barhne par kya hota hai —
aapki map app route suggest kare, aap phir bhi dekh lete ho. **Jitni zyada stakes, utna zyada banda
verify karna chahta hai.**

Har autonomous agent chupke se **3 naye interfaces** banata hai jo pehle nahi the:

- **Configuration** surface — agent ko apni preferences kaise sikhayein
- **Monitoring** surface — bina pagal huye woh kya kar raha hai kaise dekhein
- **Intervention** surface — jab ghalat ho to kaise step in karein

**Interface gayab nahi hota. Uska center of gravity move hota hai:** "task ko widget mein translate
karo" se "intent ka system shape karo" ki taraf. Aap screens banana chhod kar delegated relationship ki
plumbing design karte ho.

---
[⬆ Index](README.md) · [Agla: Human Surface ➡](01-human-surface.md)
