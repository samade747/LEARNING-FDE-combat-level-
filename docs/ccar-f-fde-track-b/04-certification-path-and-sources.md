# 04 — Certification Path + Sources of Truth

## Panaversity Route

> ⚠️ **2026-09-02 (Zia Tutor corpus gen 61, book "Version note": updated 1 Sep 2026):** book ne
> certifications section restructure kiya (ab ek group hai jismein har Panaversity exam ka apna page:
> `/docs/certifications/pcao-f`, `/pcar-f`, `/pcar-p`, `/pcdv-f`). Yeh syllabus file (user-provided,
> 26 Aug 2026) us se **purani** hai — iska route line stale hai. **Current route (book se):**
>
> **PCAO-F → PCAR-F → FDE Internship Program → *(optional)* CCAO-F → CCAR-F**
>
> - PCDV-F/CCDV-F ab FDE gate ka hissa **nahi** — "additional technical credential".
> - **PCAO-F pehle** aata hai (Associate = judgment foundation), phir PCAR-F (Architect = system design).
> - **Stage Two (Anthropic exams) ab explicitly OPTIONAL** — book: *"Sitting the Anthropic exams is
>   optional... The Panaversity credentials and the internship stand on their own."* Panaversity
>   internship participants ki registration mein **assist** karta hai (pehle framing "yehi ek route" thi).
> - Har Panaversity exam ab **"same blueprint, one level up"** hai: matching Anthropic blueprint poora
>   (published weights) + phir vendor-neutral / professional coverage.
> - **PCAO-F rollout dates:** sample 10 Sep 2026, proctored 18 Sep 2026 se live. **PCAR-F sample +
>   proctored "coming soon" — koi date nahi** (interim rehearsal: book ka CCAR-F Practice Exam,
>   `/docs/certifications/ccar-f` → Prep Resources).

**Is syllabus ka apna route line (26 Aug 2026, ab stale):** ~~Track B → PCAR-F → PCDV-F preparation →
pass PCDV-F → FDE Internship Program + partner access → CCAR-F → CCDV-F~~

Zaroori distinctions:
- PCAO-F/PCAR-F **Panaversity ki apni requirements** hain, Anthropic prerequisites nahi
- Yeh syllabus sirf **PCAR-F/CCAR-F architecture content** prepare karta hai — **PCAO-F** (associate
  exam, ab pehla gate exam) ka judgment/evaluation focus alag se prepare karna hoga (dekho
  [[certifications]] chapter — [`docs/certifications/00-overview.md`](../certifications/00-overview.md)
  ka updated pathway + [`docs/certifications/pcao-f/`](../certifications/pcao-f/README.md) /
  [`docs/certifications/ccao-f/`](../certifications/ccao-f/README.md) blueprint)
- Vertical specialization practicum mein hi shuru ho jati hai, sirf certification ke baad nahi
- **Anthropic exams (optional):** Claude Certification Program registration ke liye ek **eligible
  organisational account** chahiye (personal email accept nahi) — jo FDE Internship se milta hai;
  registration Anthropic Partner Academy se shuru hoti hai, Panaversity assist karta hai

Poora certification-program detail (pricing, retakes, renewal, 6-week free study plan, sample tests)
already [`docs/certifications/`](../certifications/README.md) shared files + [`pcar-f/`](../certifications/pcar-f/README.md)
/ [`ccar-f/`](../certifications/ccar-f/README.md) mein cover hai — is chapter mein duplicate nahi kiya.

## Sources of Truth (Version Discipline)

| Topic | Authority |
| --- | --- |
| CCAR-F blueprint, format, task statements | Claude Certified Architect — Foundations Exam Guide, v1.0 (July 2026) |
| Anthropic scheduling/retakes/Partner Academy route | Pearson VUE Claude Certification Program page |
| Panaversity qualification sequence + attempts + per-exam rollout dates | Agent Factory certifications section — per-exam pages `/docs/certifications/{pcao-f,pcar-f,...}` (Zia Tutor MCP se confirmed, gen 61 — dekho [[certifications]]) |
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
