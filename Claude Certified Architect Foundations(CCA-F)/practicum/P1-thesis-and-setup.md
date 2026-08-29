# P1 — FDE, SoR Thesis, and Setup

*Practicum week 1. Reads: [[ecosystem-fde-af-model]] · [[ecosystem-system-of-record]]. Deliverables:
(a) thesis — durable product governed knowledge kyun hai, chatbot kyun nahi; (b) 3 candidate
verticals; (c) environment install verified.*

---

## (a) Thesis — Durable product = governed knowledge, not a chatbot

**Dava:** Ek FDE engagement ka **durable, transferable asset** woh **governed knowledge corpus** hai
jo customer ke domain ki authoritative rules, sources, aur boundaries ko encode karta hai — **na ke**
us corpus ke upar baitha koi ek chatbot.

**Kyun:**

1. **Model/harness/UI sab replaceable hain, knowledge nahi.** Aaj ka agent framework 18 mahine mein
   purana ho jayega. Lekin "is vertical mein authoritative source kaun hai, conflict kaise resolve
   hota hai, kahan abstain karna hai" — yeh knowledge har naye model ke neeche dobara plug hoti hai.
   Chatbot ek *projection* hai; corpus *source* hai.

2. **Chatbot bina governance ke ek liability hai.** Ungoverned RAG confidently galat jawab deta hai
   jab source purana ho, conflicting ho, ya sawal boundary se bahar ho. Governed SoR mein: har claim
   ka source + date, conflict annotation, aur ek explicit **abstention policy** ("in cheezon ka
   jawab nahi denge") — yeh woh discipline hai jo regulated customer actually khareedta hai.

3. **Do projections, ek source.** Same governed corpus se: **human-readable site** (Fumadocs) aur
   **agent-readable MCP surface**. Agar knowledge chatbot ke andar phansi ho, doosri projection
   banana rebuild hai. Agar woh ek governed corpus hai (`knowledge/` + provenance), dono projections
   derive hoti hain.

4. **FDE ka evidence yehi hai.** Internship review ka primary portfolio artifact "maine ek bot
   banaya" nahi — "maine is vertical ki knowledge ko govern kiya, provenance ke sath, aur prove kiya
   ke woh sahi behave karti hai (3-class eval)."

**Ek line mein:** *Chatbot woh cheez hai jo customer maangta hai; governed SoR woh cheez hai jo unki
problem actually solve karti hai aur jo aap agle customer tak carry kar sakte ho.*

*(Method — outcome contract, workflow archaeology, three-bin sort, source hierarchy,
thin-slice-and-prove — [[ecosystem-designing-the-vertical-sor]] mein hai; P3 mein apply karenge.)*

---

## (b) 3 Candidate Verticals

*Screening criteria (P2 mein formally apply honge): knowledge intensity · regulatory weight · source
availability · willingness to pay · **personal access**. Personal access woh factor hai jo tum khud
laate ho — main sirf shortlist propose kar raha hoon.*

| # | Vertical | Knowledge intensity | Regulatory weight | Source availability | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | **Pakistan freelancer/software-house tax & FBR compliance** (income tax, sales tax on IT services, PSEB registration, remittance rules) | High — rules change yearly, many exceptions | High — FBR/SROs | Good — FBR site, Finance Acts, SRO PDFs (public) | Big local audience (GIAIC/Panaversity crowd), clear willingness to pay |
| 2 | **SECP company incorporation & annual compliance** (pvt ltd setup, Form filings, director changes, statutory returns) | Medium-high | High — SECP Ordinance/regs | Good — SECP portal, circulars | Narrower but sharper pain; consultants charge a lot |
| 3 | **AAOIFI Shariah-compliance rules for Islamic fintech** (murabaha, ijarah, sukuk structuring constraints) | Very high | High — AAOIFI standards + local Shariah boards | Medium — standards are paywalled; secondary literature public | Differentiated, global; source-availability is the risk |

**P2 par tum decide karoge** — sabse zyada wazan **personal access** ko do: kis domain mein tumhare
paas real practitioners hain jinse verify kara sako, aur real source documents jinhe reviewed
Markdown mein convert kar sako.

---

## (c) Environment — verified 2026-08-29

| Requirement | Installed | Status |
| --- | --- | --- |
| Node.js 24+ | v24.18.0 | ✅ |
| pnpm | 9.12.3 | ✅ |
| uv | 0.6.0 | ✅ |
| Python | 3.13.2 | ✅ (entry contract: "read simple Python") |
| git | 2.44.0 | ✅ |

`@panaversity/ksor` (npm 0.0.42) shipped hai — P4 se `npx @panaversity/ksor@latest init` real path
hai. `docs/status.md` P4/P6/P9 se pehle har baar re-check karna hai (KSoR evolving).

---

## Done jab

- [x] Thesis likha (governed knowledge vs chatbot, 4 reasons)
- [x] 3 candidate verticals with screening notes
- [x] Node 24+ / pnpm / uv verified
- [ ] P2: ek vertical commit + source register shuru *(next session — tumhari personal-access input chahiye)*
