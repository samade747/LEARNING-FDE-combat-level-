# 07 — Practice Log (Meri Apni PCAR-F Push)

*Yeh file baaqi files se alag hai. Woh files batati hain **"exam kya hai, kaise structured hai"**. Yeh
file record karti hai **"maine khud kya kiya"** — apna prep, week-by-week, checkbox ke sath. Isi
pattern par jo [Loop Engineering](../loop-engineering/11-practice-log.md) aur
[Harness Engineering](../harness-engineering/11-practice-log.md) ki practice logs mein use hua.*

**Goal (2026-08-24 ko set hua):** 2026-10-05 tak **PCAR-F** (free Panaversity internal exam) pass
karo — CCAR-F/CCDV-F ki taraf, phir poori CCAR-F/CCDV-F ki taraf pehla concrete step. Deadline se
6 hafte se kam waqt hai, isliye [04-gaps-and-study-plan.md](04-gaps-and-study-plan.md) ka 6-week plan
compress karke follow karo.

**Rule:** ek week ka checkbox tab hi tick hota hai jab uska "Done jab" criteria khud dekh liya ho.

---

## Progress Checklist

| Week | Focus | Status | Notes |
| --- | --- | --- | --- |
| 1-2 | CCAR-F blueprint + domain-weighted study ([03](03-exam-domains.md)) | ⬜ Not started | |
| 3-4 | Ek chhoti application banao jo 5+ domains touch kare | ⬜ Not started | |
| 5 | Free sample test (CCAR-F) exam conditions mein, weak domains drill | ⬜ Not started | |
| 6 | Re-test weak domains, **PCAR-F sit karo** | ⬜ Not started | |

Status legend: ⬜ Not started · 🔶 In progress · ✅ Done

---

## Week 1-2 — Blueprint + Domain-Weighted Study

**Kya karna hai:** [pcar-f/README.md](pcar-f/README.md) (ya [ccar-f/README.md](ccar-f/README.md) full
detail ke liye) ki domain table se weights confirm karo (Agentic Architecture 27%, Claude Code Config
20%, Prompt Engineering 20%, Tool Design/MCP 18%, Context Management 15%). Is repo mein jo already
cover hai wahan se revise karo — jo 🔲 hai (Skills & Connectors, Code You Never Write, How to Think in
the AI Era) uske liye Zia Tutor se fresh fetch karo ya Anthropic Academy free courses use karo.

### Done jab (self-check)
- [ ] Sab 5 CCAR-F domains ka apna ek-line summary likh sakta hoon
- [ ] Pata hai konsi domain is repo mein already strong hai (Agentic Architecture — 4 courses) aur
  konsi thin hai (Prompt Engineering, Tool Design/MCP — kuch gaps)

---

## Week 3-4 — Ek Chhoti Application Banao

**Kya karna hai:** ek weekend project jo API call kare, kam se kam ek tool/MCP server use kare,
prompt/context engineering apply kare, aur ek basic eval include kare. (Is repo mein already
[connector-native-apps](../connector-native-apps/README.md) aur
[trusting-the-checker](../trusting-the-checker/README.md) projects isi shape ke hain — reuse ya
extend karo.)

### Done jab (self-check)
- [ ] Project chalta hai aur kam se kam 3 CCAR-F domains touch karta hai
- [ ] Ek trade-off likh sakta hoon jo banate waqt khud decide kiya (batch vs real-time, agent vs
  workflow, MCP server vs custom tool)

---

## Week 5 — Practice Test + Weak-Domain Drill

**Kya karna hai:** [pcar-f/README.md](pcar-f/README.md) ke "Prep Resources" se CCAR-F sample test free
lo, exam conditions mein (120 min, no notes). Explanations parho — samjho **kyun** sahi trade-off sahi
hai, na sirf kya sahi hai.

### Done jab (self-check)
- [ ] Ek full practice attempt complete hua, score aur weak domains note kiye
- [ ] Weakest 1-2 domains ka targeted re-study hua

---

## Week 6 — PCAR-F Sit Karo

**Kya karna hai:** weak domains dobara test karo, phir **PCAR-F** book karo aur do (Panaversity ke
zariye, [01-stage-one-panaversity.md](01-stage-one-panaversity.md) dekho). Pass = 720/1000.

### Done jab (self-check)
- [ ] PCAR-F attempt complete hua
- [ ] Result (pass/fail + score) yahan note hua

---

## Open Note — Root README.md Stale Hai

Is chapter ke domain-mapping ([03-exam-domains.md](03-exam-domains.md)) banate waqt pata chala ke
root `README.md` ka status table **stale hai**: `docs/roles-this-book-trains/`, `docs/ai-prompting-2026/`,
`docs/what-you-carry-in/`, `docs/what-ai-actually-is-crash-course/`, `docs/markdown-html-crash-course/`
jaise folders **poore documented hain** (README + numbered files + SUMMARY.md), lekin README.md ka
Front Matter (12) aur Foundations (6) sections abhi bhi "0/12" aur "0/6" dikhate hain. Yeh separate
audit/fix hai — is task ke scope se bahar, lekin flag kar diya taake bhoola na jaye.
