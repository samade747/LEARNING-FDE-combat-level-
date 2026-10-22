# Glossary — Answer Key

1. **Agentic AI** (vs regular AI) — chatbot sawal ka jawab deta hai, agent khud research/plan/
   execute/report karta hai, decisions leta hai raaste mein.
2. **10-80-10 Rule** — Steve Jobs (Apple): vision set karna (10%), team ko build karne dena (80%),
   polish/ship karne wapas aana (10%).
3. **Digital FTE/AI Workers = workforce** (hired, assigned, rostered, retired). **Delegate (OpenClaw)
   aur Manager (Paperclip) = permanent staff**, workforce nahi.
4. **OpenClaw = Delegate** (Edge Layer, chief-of-staff, ek per executive). **Paperclip = Manager**
   (management plane, COO, one-to-many workforce ke sath).
5. **Invariant** = structural requirement jo har version mein stay true rehti hai (jaisa "house must
   have a way to enter/exit"). **Reference implementation** = concrete product jo abhi usay realize
   karta hai (jaisa "mahogany double doors") — doors badal sakte hain, invariant nahi badalta.
6. **Meta-Layer (hiring as a callable capability)** — Paperclip gap detect karta hai, apni authority
   envelope ke andar hiring API call karta hai, naya Bahasa-speaking Worker manufacture hota hai, bina
   insaan ko jagaye.
7. **Harness = control plane** — agent loop, tool dispatch, approvals, tracing, context management,
   recovery, instructions, skills, validators. Model "brain" hai, harness "body + workplace + SOP."
8. Credentials **harness** mein rehte hain; model-generated code **sandbox** mein chalta hai — split
   security aur portability ke liye zaroori hai (sandbox vendor swap ho sakta hai bina agent rewrite
   kiye).
9. **Open-book exam vs closed-book** — AI apne documents mein facts lookup karta hai jawab dene se
   pehle, (potentially wrong) memory se guess karne ke bajaye — much more accurate.
10. USB se pehle har phone ka alag charger tha. **MCP = ek universal protocol** jo kisi bhi agent ko
    kisi bhi tool se plug karne deta hai — alag-alag custom integrations ki zaroorat nahi.
11. **AAIF** = governance body (MCP, AGENTS.md waghera standards ke liye neutral oversight). **A2A** =
    agent-to-agent protocol (agents ek doosre ko discover/communicate/delegate karte hain) — AAIF
    governs standards, A2A ek specific connection-type hai.
12. **Stateless** = AI ko conversations ke beech kuch yaad nahi rehta, har naya chat zero se shuru
    hota hai. Chat apps poori conversation har baar **re-send** karte hain, isliye memory ka "illusion"
    create hota hai.
13. Developer 2 PM ko code push karta hai → tests automatically 3 minute mein chalte hain → sab pass →
    naya version 2:10 PM tak live hai, zero manual steps.
14. Shipping container ki tarah — chahe truck mein Karachi mein ho ya ship mein ocean mein, **andar ka
    content identical aur self-contained rehta hai** — app kahin bhi (laptop, colleague's machine,
    cloud server) identically chalti hai.
15. **Trigger** = jis tareeqe se bahar ki duniya AI-Native Company ko motion mein bulati hai (schedule,
    webhook, API call, customer walk-in). **Claude Code Routines** reference implementation hai kyunke
    har external event ko ek session mein badal deta hai jo delegate ko jaga kar chain fire karta hai —
    bina isके system sirf tabhi move karta jab insaan prompt type kare.
