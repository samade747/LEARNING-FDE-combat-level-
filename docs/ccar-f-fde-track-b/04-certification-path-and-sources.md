# 04 — Certification Path + Sources of Truth

## Panaversity Route

> ⚠️ **2026-09-01:** book ne `certifications` page (Version note: updated 28 Aug 2026) par pathway
> restructure kiya. Yeh syllabus file (user-provided, 26 Aug 2026) us se **purani** hai — iska route
> line ab stale hai. **Current route (book se):**
>
> **PCAO-F → PCAR-F → FDE Internship Program + partner access → CCAO-F → CCAR-F**
>
> PCDV-F/CCDV-F ab FDE gate ka hissa **nahi** — "additional technical credential". Ab **PCAO-F pehle**
> aata hai (Associate = judgment foundation), phir PCAR-F (Architect = system design).

**Is syllabus ka apna route line (26 Aug 2026, ab stale):** ~~Track B → PCAR-F → PCDV-F preparation →
pass PCDV-F → FDE Internship Program + partner access → CCAR-F → CCDV-F~~

Zaroori distinctions:
- PCAO-F/PCAR-F **Panaversity ki apni requirements** hain, Anthropic prerequisites nahi
- Yeh syllabus sirf **PCAR-F/CCAR-F architecture content** prepare karta hai — **PCAO-F** (associate
  exam, ab pehla gate exam) ka judgment/evaluation focus alag se prepare karna hoga (dekho
  [[certifications]] chapter — [`docs/certifications/00-overview.md`](../certifications/00-overview.md)
  ka updated pathway + [`docs/certifications/ccao-f/`](../certifications/ccao-f/README.md) blueprint)
- Vertical specialization practicum mein hi shuru ho jati hai, sirf certification ke baad nahi
- Pearson VUE: Claude Certification Program Claude Partner Network organizations ke liye open hai;
  registration Anthropic Partner Academy se shuru hoti hai

Poora certification-program detail (pricing, retakes, renewal, 6-week free study plan, sample tests)
already [`docs/certifications/ccar-f/`](../certifications/ccar-f/README.md) mein cover hai — is
chapter mein duplicate nahi kiya.

## Sources of Truth (Version Discipline)

| Topic | Authority |
| --- | --- |
| CCAR-F blueprint, format, task statements | Claude Certified Architect — Foundations Exam Guide, v1.0 (July 2026) |
| Anthropic scheduling/retakes/Partner Academy route | Pearson VUE Claude Certification Program page |
| Panaversity qualification sequence + attempts | Agent Factory `certifications` page (Zia Tutor MCP se confirmed — dekho [[certifications]]) |
| MCP protocol | Model Context Protocol specification 2026-07-28 |
| KSoR shipped functionality | `panaversity/ksor` → `docs/status.md` |
| KSoR runtime requirement | Current KSoR README/status |
| Fumadocs runtime/setup | fumadocs.dev |

**Har cohort se pehle re-check karo:** current CCAR-F guide, Pearson programme page, KSoR status, MCP
spec, aur Fumadocs requirements — product/certification details change ho sakti hain. Yeh is repo ka
`AGENTS.md` rule 3 (Zia Tutor MCP se content, training-knowledge se kabhi nahi) yahan is tarah lagu
hota hai: is chapter ke andar jo bhi Claude/Anthropic technical facts likhi gayi hain (jaise stateless
MCP, [02](02-fde-practicum.md) mein), unhe book (`context-layer-crash-course`) se cross-check kiya gaya
— jahan book cover nahi karti (jaise MRTR ke exact field-level mechanics), wahan honestly note kiya
gaya ke source is syllabus/MCP-spec khud hai, book nahi.

---
[⬅ Required Projects](03-required-projects-and-assessment.md) · [Agla: Test Your Understanding ➡](05-test-your-understanding.md) · [⬆ Index](README.md)
