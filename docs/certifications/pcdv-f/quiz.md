# Quiz — PCDV-F: Panaversity Certified Developer, Foundations (Test Your Understanding)

**10-question self-contained assessment**, PCDV-F-specific: Panaversity logistics (second exam in
Stage One, after PCAR-F) + the CCDV-F blueprint PCDV-F is aligned to (very uneven domain weights).
Grounded in this folder's `README.md` + the parent chapter's `01-stage-one-panaversity.md`. Same 10
questions also live in [`05-test-your-understanding.md`](05-test-your-understanding.md) as the
scenario version.

---

### Q1. PCDV-F ka number Stage One mein — pehla ya doosra?

**Q:** Ek candidate PCAR-F pass kiye bina seedha PCDV-F dena chahta hai. Kya yeh recommended sequence
hai?

- Haan, order matter nahi karta
- **Nahi — Stage One mein PCDV-F **doosra** exam hai, PCAR-F ke baad, kyunke implementation se pehle
  architecture ka mental model chahiye** ✅
- Haan, PCDV-F pehle dena behtar hai kyunke woh aasan hai
- Nahi, PCDV-F sirf PCAR-F ke 6 mahine baad diya ja sakta hai

**Explanation:** "Kyun Doosre Number Par" section explicit hai: PCDV-F prove karti hai ke aap
architecture se implementation tak move kar sakte ho — PCAR-F ka mental model pehle chahiye. Yeh ek
recommended sequence hai, hard 6-month wait nahi.
*(Source: README.md — "Kyun Doosre Number Par")*

---

### Q2. CCDV-F domain weights kitne "uneven" hain — practical impact kya hai?

**Q:** PCDV-F/CCDV-F ke sabse bare 2 domains milke exam ka kitna hissa banate hain, aur study time
par iska kya asar hona chahiye?

- Har domain 12.5% hai (8 domains, equal split) — equal time do
- **Applications/Integration (33.1%) + Model Selection (16.8%) milke ~50% exam banate hain — study
  time bhi utna hi asymmetric hona chahiye, sab domains ko equal time dena mistake hai** ✅
- Sabse chhota domain (2.6%) ko sabse zyada time do, kyunke woh sabse mushkil hai
- Domain weights sirf CCDV-F ke liye hain, PCDV-F alag hai

**Explanation:** Table khud kehti hai "Bohat Uneven" — top 2 domains milke aadha exam hain. Six
Mistakes ka #2 exactly yehi warn karta hai: 2.6% domain ko 33.1% jitna time dena galat allocation
hai. PCDV-F **usi** blueprint pe hai, koi alag weight nahi.
*(Source: README.md — Domain Weights table)*

---

### Q3. PCDV-F pass karne ke baad kya milta hai, agar PCAR-F pehle se pass hai?

**Q:** Candidate ne PCAR-F pehle hi pass kar rakha hai. PCDV-F bhi pass karne ke baad kya unlock hota
hai?

- Kuch nahi, dono independent hain
- **Panaversity FDE Internship Program & partner access — jo Anthropic ke CCAR-F/CCDV-F register
  karne ke liye zaroori hai** ✅
- Sirf CCDV-F register kar sakte hain, CCAR-F nahi
- Automatic CCDV-F pass ho jata hai

**Explanation:** "Unlocks" row: dono (PCAR-F + PCDV-F) pass hone se FDE Internship Program & partner
access milta hai, jo dono Anthropic exams (CCAR-F **aur** CCDV-F) ke liye eligibility deta hai — sirf
ek ke liye nahi.
*(Source: README.md — Quick Facts "Unlocks")*

---

### Q4. PCDV-F ke practice projects kahan hain?

**Q:** PCDV-F/CCDV-F ke How-to-Prepare checklist ("ek Claude application banao jo API+tool+security
exercise kare") practice karne ke liye is repo mein konsa scaffold hai?

- Koi scaffold nahi, CCDV-F ka guide sirf "kuch banao" kehta hai, koi concrete example nahi
- **`docs/certifications/ccdv-f/projects/00-integration-application/` — CCDV-F ke 3 official sample
  questions (batch-vs-realtime, prompt-injection guardrail, reusable MCP tool) ke around banaya
  gaya, PCDV-F usi ko point karta hai (same blueprint)** ✅
- Sirf CCAR-F ke projects, PCDV-F ke liye kuch nahi
- Har candidate ko khud se poori application banani padti hai, koi starting point nahi

**Explanation:** CCDV-F guide CCAR-F jaisi 4 numbered exercises nahi deta, sirf "ek application
banao" + 3 illustrative sample questions. Is repo ka scaffold un teenon sample questions (Domain 2,
7, 8) ko directly, testable code mein implement karta hai — PCDV-F usi blueprint pe based hai isliye
usi scaffold ko reuse karta hai.
*(Source: README.md — Practice Projects, is quiz ke sath add hua)*

---

### Q5. Sample Question 1 (batch vs realtime) ka sahi jawab kyun B hai, A nahi?

**Q:** 10,000 documents, non-urgent, cost primary concern, results agli subah tak chahiye. Kyun
"synchronous parallel calls jitni jaldi ho khatam karo" (option A) galat hai?

- A galat nahi hai, dono equally sahi hain
- **A latency minimize karta hai jab requirement latency-tolerance + cost hai — per-token cost kam
  nahi karta, jo asal binding constraint hai; Message Batches API (B) exactly isi tradeoff ke liye
  design hui hai** ✅
- A galat hai kyunke synchronous calls kaam hi nahi karte
- A sahi hota agar volume 10,000 se kam hota

**Explanation:** Sample question ka core lesson: requirement ko sahi se identify karo (yahan: cost,
na ke speed) phir uske liye design hui API choose karo. Speed-optimized approach jab cost binding
constraint ho, wrong-tool-for-the-job hai — is repo ka `mode_selector.py::choose_processing_mode`
yehi logic implement karta hai.
*(Source: ../ccdv-f/03-how-to-prepare-and-sample-questions.md — Sample 1)*

---

### Q6. Sample Question 2 (prompt injection) mein "temperature raise karo" kyun galat hai?

**Q:** Ek malicious web page hidden instruction rakhta hai. Kyun "model ka temperature raise karo"
effective mitigation nahi hai?

- Temperature raise karna hamesha behavior improve karta hai
- **Temperature injection-resistance se irrelevant hai — asal fix untrusted content ko trusted
  instructions se isolate karna hai, randomness badhana nahi** ✅
- Temperature raise karna crash kar deta hai
- Sirf CCAR-F mein temperature relevant hai, CCDV-F mein nahi

**Explanation:** Sample question ka distractor options root cause se distract karte hain (temperature,
polite request, bigger model) — sahi mitigation hamesha **structural isolation** hai: untrusted
content ko data ki tarah treat karo, kabhi instruction ki tarah nahi. Is repo ka
`content_guard.py::UntrustedContent` + `privileged_tool_call()` yehi structural gate hai.
*(Source: ../ccdv-f/03-how-to-prepare-and-sample-questions.md — Sample 2)*

---

### Q7. Sample Question 3 (MCP server) mein "built-in tool" (option D) kyun galat hai?

**Q:** Team ek internal inventory REST API ko Claude se reusable tareeqe se call karwana chahti hai.
Kyun "built-in tool pe rely karo" galat option hai?

- Built-in tools kabhi kaam nahi karte
- **Built-in tools automatically arbitrary internal/private REST APIs tak reach nahi karte — ek
  custom MCP server hi internal service ko expose kar sakta hai** ✅
- Built-in tools sirf CCAR-F ke liye relevant hain
- Option D sahi hai, guide ki apni official answer galat hai

**Explanation:** Distractor yeh assume karta hai built-in tools "kuch bhi" reach kar sakte hain — jo
galat hai, khaas kar private/internal services ke liye. MCP server banana hi reusable, independently-
maintained integration ka sahi tareeqa hai. Is repo ka `inventory_mcp_tool.py::InventoryMCPServer`
yehi pattern (ek server, multiple app clients) demonstrate karta hai.
*(Source: ../ccdv-f/03-how-to-prepare-and-sample-questions.md — Sample 3)*

---

### Q8. PCDV-F pass karne ke liye kitne attempts free hain?

**Q:** PCDV-F ke liye Panaversity student ko kitne free attempts milte hain, aur teesra attempt kis
policy follow karta hai?

- Unlimited free attempts
- **2 free attempts, jaisa PCAR-F — teesra (aur baad wala) attempt fee leta hai (currently TBA)** ✅
- Sirf 1 free attempt
- Free attempts sirf CCDV-F ke liye hain, PCDV-F ke liye nahi

**Explanation:** PCDV-F ki cost policy PCAR-F jaisi hi hai — 2 free attempts Panaversity students ke
liye, phir fee. Yeh dono Panaversity exams ki shared policy hai, alag-alag nahi.
*(Source: README.md — Quick Facts "Cost")*

---

### Q9. PCDV-F/CCDV-F mein "Claude Code" domain sirf 3.1% weight kyun rakhta hai jabke poora repo isay deeply cover karta hai?

**Q:** Is repo mein Claude Code/OpenCode par kaafi content hai, lekin CCDV-F blueprint mein "Claude
Code" domain sirf 3.1% hai. Study time allocate karte waqt is mismatch ka kya matlab hai?

- Is repo ka content waste hai, CCDV-F ke liye irrelevant
- **Domain weight exam ka apna priority signal hai — 3.1% domain ko deep coverage ke bawajood
  proportionally kam time dena chahiye; "book mein kitna content hai" aur "exam mein kitna weight
  hai" alag cheezein hain** ✅
- Zyada content ka matlab zyada weight hona chahiye tha, guide galat hai
- Claude Code domain skip kar sakte hain, zero weight ke barabar hai

**Explanation:** Six Mistakes list ka #2 ("har domain ko equal time dena") isi confusion se related
hai — book ki apni depth kisi domain par uska exam-weight decide nahi karti. Study plan hamesha
**domain weight** follow kare, book mein available content ki matra nahi.
*(Source: README.md — Domain Weights table + parent 05-registration-costs-mistakes.md Six Mistakes #2)*

---

### Q10. PCDV-F ke liye "kam se kam ek application banao" instruction kitni specific hai?

**Q:** CCDV-F guide "ek Claude application banao" kehti hai, lekin PCAR-F/CCAR-F ki tarah 5 numbered
step-by-step exercises nahi deti. Iska candidate ke liye practical matlab kya hai?

- Koi structure follow karna zaroori nahi, kuch bhi bana lo
- **Guide khud kehti hai "koi single required course/format nahi" — candidate ko khud decide karna
  hai kaise practice karni hai, lekin 3 sample questions (batch/realtime, security, MCP) ek concrete
  starting shape dete hain** ✅
- Is repo ke scaffold ke alawa koi aur approach invalid hai
- CCDV-F mein practice karna optional hai, sirf theory kaafi hai

**Explanation:** CCDV-F guide's "How to Prepare" explicitly flexible hai (koi guaranteed-pass resource
nahi) — is flexibility ka fayda uthate hue is repo ne 3 sample questions ko ek concrete, testable
application mein convert kiya, taake "kuch banao" ek vague suggestion na reh jaye.
*(Source: ../ccdv-f/03-how-to-prepare-and-sample-questions.md — "How to Prepare")*

---
[⬅ PCDV-F Index](README.md) · [Scenario version (same content) ➡](05-test-your-understanding.md)
