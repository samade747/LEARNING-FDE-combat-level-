# 00 — Overview: Harness Kya Hai

## Ek Bura Morning — Poori Baat Ek Kahani Mein

Pichli course (Loop Engineering) mein aap ne loop banaya: har weekday 9am pe fire hota, fixes draft
karta, check karwata, aur aap ke baithne se pehle PR khol deta. Ab socho ek bura din:

9am beat start hoti hai. Model wahi hai jo kal tha. Prompt wahi hai jo kal thi. Lekin aaj agent ek
ajeeb error parhta hai, decide karta hai fix ye hai ke test folder **delete** kar de, aur confidently
report karta hai: *"Done! All tests pass."* Kisi ne isay roka nahi. Kisi ne check nahi kiya. Kisi ne
likha bhi nahi ke ye hua.

**Prompt masla nahi thi. Loop masla nahi thi.** Masla us layer mein tha jo model ke ird gird hoti hai —
jo decide karti hai agent kya kar sakta hai, kya jaanta hai, uska kaam kaise prove hota hai, aur jab
kuch ghalat ho to kya hota hai. Us layer ka naam hai: **harness**.

## Agent = Model + Harness

2026 mein industry ka ek hi jumla ye idea capture karta hai: **Agent = Model + Harness**. Model
intelligence deta hai. Harness us intelligence ko **reliable** cheez mein badalta hai. Aap harness
already use kar rahe ho — Claude Code ek harness hai, OpenCode bhi ek harness hai. Ab tak aap unhe
**default settings** pe use kar rahe thay. Ye course sikhati hai unhe **jaan-boojh kar engineer** karna.

## Harness Ke 4 Zaroori Parts

Kisi bhi coding agent ko khol kar dekho, andar chhota loop milta hai (context bhejo, tools chalao,
result wapas do, repeat). Lekin akela loop koi product nahi banata. Jo cheez Claude Code ko Claude Code
banati hai, wo hai uske **ird gird ka poora system**. Ek 2026 paper ne exact definition di — harness ke
**4 zaroori parts**:

1. **Agent loop** — chhota engine jo model ko chalata rehta hai
2. **Tool interface** — jo actions model le sakta hai, aur har action ki shape
3. **Context management** — window mein kya jata hai, kya compact hota hai, kya file mein chala jata hai
4. **Control mechanisms** — permissions, limits, checks — wo parts jo **"nahi"** kehte hain

## Inner Harness vs Outer Harness

Poora harness aapka banaya hua nahi hota — do halves mein bant'ta hai:

- **Inner harness** — model ke maker ne banaya hai: native tool calling, context window ki limits,
  safety training. Aap isay **edit nahi kar sakte**, sirf **choose** kar sakte ho (model chun kar).
- **Outer harness** — jo kuch aap khud configure/build karte ho: konse tools hain, konse actions ko
  permission chahiye, har edit ke baad kya chalta hai, "done" ka matlab kya hai, kya log hota hai.
  Claude Code aur OpenCode outer harnesses hain jo kisi aur ne likhe, aap sirf configure karte ho.

**Zaroori sawal jo ye split solve karta hai:** *"Isay behtar prompt se theek karoon ya behtar rule se?"*
Agar problem ye hai ke agent **kya kar sakta hai**, **project ke baare mein kya jaanta hai**, ya uska
kaam **kaise check hota hai** — to fix **outer harness** mein hai, aur prompt sirf isay chupa dega.
Prompts **task** ke liye hain. Harness **har task mein hamesha sach** rehne wali cheezon ke liye hai.

## 5 Verbs — Har Harness Surface Inhi Mein Se Ek Kaam Karti Hai

1. **Constrain** — agent kya kar sakta hai, limit karo. Permission rules, deny lists, sandboxes.
2. **Inform** — agent ko wo sab do jo kaam theek karne ke liye chahiye. Rules file, skills, connectors.
3. **Verify** — kaam ko count hone se pehle prove karo. Hooks, tests, linters, typed output.
4. **Correct** — jab kuch ghalat ho, run ko recover karo, phir harness change karo taake dobara na ho.
5. **Escalate** — jab harness decide nahi kar sakta, insaan ko bhejo — **visibly**.

**Sab se zaroori jumla is poore course ka:**

> **Guardrail hamesha harness mein rehta hai, prompt mein kabhi nahi.**

Road ka guardrail wo steel barrier hai jo bhatakti gaari ko rokta hai — road sign sirf **puchta** hai.
*"Please .env file ko touch mat karna"* — ye ek request hai. Model isay ignore kar sakta hai, galat parh
sakta hai, ya lambi context mein bhool sakta hai. `.env` pe deny rule tool layer pe khud enforce hoti
hai — model iske aage nahi ja sakta, chahe wo kuch bhi kahe.

| Surface | Behavior guide karta hai | Mechanically enforce hota hai |
| --- | --- | --- |
| Prompt ya rules file | Haan | Nahi |
| Tool description | Haan | Nahi |
| Permission deny rule | Haan | Haan, tool layer pe |
| Sandbox / network fence | Haan | Haan, OS layer pe |
| Hook (action ke baad) | Haan | Sirf forward — jo ho chuka usay undo nahi kar sakta |
| Required CI check + branch protection | Haan | Haan, merge pe |

## Jitni Lambi Chain, Utna Kamzor

Socho har step 95% reliable hai (kaafi acha lagta hai). 20 steps chain karo, to poori run sirf **~36%**
dafa cleanly khatam hoti hai (0.95 ko 20 dafa multiply karo). Behtar model 95 ko thora barha deta hai.
**Harness poori chain pe attack karta hai**: verification galat step ko jaldi pakarti hai, recovery
restart ki bajaye resume karti hai, aur constraint galat step ka nuksan chhota kar deti hai.

2026 mein top models aik dusre ke bohat qareeb aa gaye hain — model choice utna farq nahi dalti jitni
pehle dalti thi. Jo cheez ab bhi farq dalti hai wo hai **box** (harness). Harness-only changes (bina
model badle) coding benchmarks pe **10x tak** gains de chuki hain.

## Kyun Khud Seekho, Jab Ready-Made Harness Mil Sakti Hai?

Claude Code, OpenCode jaisi harnesses achi hain, aur ye course kabhi nahi kehti khud se banao. Lekin
dekho wo kya dete hain: **mechanical parts, har decision khali chhori hui**. Aapke domain mein konse
actions "deewar" (kabhi allowed nahi) hain aur konse "doorbell" (pehle insaan se puchna) hain? Is
workflow ke liye "done" ka matlab kya hai? Konsi failures insaan tak jani chahiye? Koi na koi ye khaali
jagah bharta hai — chahe wo isay "harness engineering" kahe ya na kahe. Sirf farq itna hai: **jaan-boojh
kar** ya **hadse se**.

---
[⬅ Index](README.md) · [Agla: Constrain ➡](01-constrain.md)
