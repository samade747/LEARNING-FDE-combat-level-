# 02 — Inform: Agent Ko Batana

Constraint batati hai agent kya **nahi** kar sakta. Doosra verb iska mirror hai: agent ko wo **sab kuch
do** jo kaam theek karne ke liye chahiye. Aadha aap pehle se jaante ho. Baaki aadha **2026 ka sab se
underrated idea** hai.

## Concept 6: Context Surfaces — Harness Parts Ki Tarah

Rules file, skills, connectors — inhe pehle "cheezein jo aap likhte ho" ki tarah sikhaya gaya tha. Ab
inhe **harness surfaces** ki tarah socho — har ek har beat pe ek sawal ka jawab deti hai:

- **Rules file** jawab deti hai: *yahan hamesha kya sach hai?* Conventions, boundaries, ratchet ke saved
  lessons. Har run parhta hai, isliye har line har beat pe cost karti hai — chhota rakho.
- **Skills** jawab deti hain: *ye specific kaam kaise karna hai?* Sirf tab load hoti hain jab task match
  kare — isliye detail tab tak "free" hai jab tak zaroorat na pare.
- **Connectors** jawab dete hain: *ye kya reach kar sakta hai, aur kaise?* Konsa MCP server attach hai —
  ye ek **inform decision** bhi hai aur **constrain decision** bhi ek saath.

**Bug kahan dhoondein:** Jab run isliye ghalat ho jaye kyunke agent ko **kuch pata nahi tha**, to bug in
teen surfaces mein se kisi ek pe hoga: hamesha-sach → rules file, task-specific → skill, reach →
connector. Ye triage 10 second leti hai aur poori shaam ki trial-and-error prompt rewriting bacha leti
hai.

## Concept 7: AX — Agent Experience

Ye hai underrated idea. Concept 6 ki har surface ka ek **reader** hota hai, aur wo reader **aap nahi**
ho — wo **agent** hai, task ke beech mein, poori context window ke saath, aur aap se puchne ka koi
tareeqa nahi. **AX (Agent Experience)** ka matlab hai us reader ke liye design karna — bilkul waisay
jaise **UX** human user ke liye design karta hai.

**3 findings, ab proper naam ke sath:**

1. **Kam, focused tools > bohat saare overlapping tools** — Har tool ek choice hai jo agent ko sahi
   banani hai, bina kisi ke dekhe, har beat pe.
2. **Tool descriptions asal kaam karti hain** — Description hi wo cheez hai jo agent ko decision ke waqt
   pata hoti hai. *"Searches the customer database by email or ID. Returns at most 20 rows"* > "customer
   tool" — jaise labeled darwaza unlabeled se behtar hai.
3. **Error messages batayein agla step kya hai** — Loop mein, error message hi agle attempt ka input
   hota hai. *"Permission denied: request the repo scope"* khud fix ho jata hai. *"Error 403"* ek beat
   waste kar deta hai, har baar, hamesha.

**Test har surface ke liye:** *kya ek competent ajnabi, sirf ye text dekh kar, sahi agla step le sakta
hai?* Agent wahi ajnabi hai, **har single beat pe**.

> **Naming collision se hoshiyar:** Is book ka "Designing Agent Experiences" course "agent experience"
> ka matlab **insaan ka** agent use karne ka tajurba leta hai. Industry ka **AX** zyada tar **agent ka**
> aapke system ko use karne ka tajurba leta hai. Same letters, opposite reader.

### Self-Check
**Sawal:** Loop har raat 2 beats waste karti hai kyunke agent `search_v1` call karta rehta hai jab usay
`search_v2` call karna chahiye, aur error sirf "invalid request" deta hai. 2 AX fixes aur (agar tool
kabhi bhi call na ho) harness verb batao.
**Jawab:** Pehla, **remove/rename** — agar `search_v1` kabhi use nahi honi chahiye, connector list se
delete kar do. Doosra, **error fix karo** — "invalid request" ki jagah "search_v1 retired: use
search_v2 with the same arguments" likho, jo agle beat pe khud fix ho jaye. Aur agar tool exist to kare
lekin is agent se kabhi call na ho, ye **constrain** verb hai — deny rule, description nahi.

---
[⬅ Constrain](01-constrain.md) · [Agla: Verify & Correct ➡](03-verify-correct.md)
