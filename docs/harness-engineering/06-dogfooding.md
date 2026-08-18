# 06 — Dogfooding: Yeh Kitaab Khud Apni Harness Kaise Use Karti Hai

Loop Engineering course ka aakhir un loops se hua tha jo yeh kitaab khud chalati hai. Wo loops ek
**harness** ke andar baithi hain — wahi harness jise iss page ko khud pass karna pada. Neeche paanch
verbs hain, **production mein**:

- **Constrain.** Book ke agents sirf `claude/` branches par likhte hain, aur `main` branch protection
  aur **ek insaan** (author) ke peeche khara hai. Figure aur sim folders writable hain. Publishing
  config nahi hai.
- **Inform.** Repo ki rules file house style ko **rule** ki tarah rakhti hai, preference ki tarah nahi:
  ESL-plain sentences, house palette ke hex codes, figure pipeline ke exact commands, footnote anchor
  pattern. Ek chapter agent style kabhi guess nahi karta. Wo isay **parhta** hai.
- **Verify.** Har change par mechanical hooks chalte hain: banned-words linter, heading-level check,
  internal-link checker, aur figure check (jo bhi image reference ho wo 2x par exist honi chahiye).
  Mechanical rung ke upar loop course wala reviewer rubric baitha hai, ab **typed**: numeric score wala
  JSON verdict, aur bar hai **95**. Bar se neeche, koi merge nahi.
- **Correct.** Review-cycle lessons (external reviews aur reader reports se) naye linter rules ya
  rules-file lines ki tarah land hoti hain — likhi hui shakal mein **ratchet**.
- **Escalate.** Jo bhi rubric ko **claims** ka masla lage (style ka nahi) — koi fact, version number, ya
  limit jo badal sakti ho — wo loop ko poori tarah skip kar ke seedha author ki queue mein jati hai.
  Kitaab ka wada *"jahan yeh course aur docs disagree karein, docs sahi hain"* isi tarah enforce hota
  hai: ek insaan docs khud parh kar.

**Honest note**, pichli course wali se ek layer neeche: harness mechanical problems pakarti hai aur
judgment calls ko **grade** karti hai, lekin model ka 95 abhi bhi ek **claim** hai, **proof** nahi.
Score decide karta hai kaunsi cheez **insaan tak pahonchti** hai. Wo kabhi decide nahi karta kya
**ship** hoti hai. Us call ka **ek** hi owner hai, aur harness isliye hai taake wo owner apna attention
sirf wahan lagaye jahan zaroorat ho.

---
[⬅ Staying the Engineer](05-staying-the-engineer.md) · [Agla: Practice Projects ➡](07-practice-projects.md) · [⬆ Index](README.md)
