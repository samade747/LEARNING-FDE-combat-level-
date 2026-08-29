# Trade-off Notebook — Track B

*Graded artifact (7% of architect grade). Har architect lab ke baad 3 sawal:*

1. **Kaunsa trade-off face kiya?**
2. **Kya choose kiya?**
3. **Plausible alternatives yahan kyun kamzor thay?**

*Yeh wahi reasoning practice karta hai jo exam ke scenario items maangte hain — "sahi jawab kyun,
distractor ka trap kya, reusable decision rule kya."*

---

## Week 1 — Foundations Sprint

### Notebook prompt: "Woh problem jo maine galat classify kar diya tha, aur woh clue jisne theek kiya"

*(Full working: `week-01-foundations-sprint/hour3-classification-lab.md`)*

- **Problem:** Legal contract extraction (12 structured fields, kuch contracts mein kuch fields
  missing).
- **Trade-off:** "Input varied hai" ko "agent chahiye" samajh lena vs control-flow ki asal nature
  dekhna.
- **Almost-choice:** Single agent — kyunki contracts ka structure alag alag hai.
- **Clue jisne theek kiya:** Output shape hamesha same 12 fields; har doc independently process hota
  hai; koi runtime "ab kya karun" decision nahi. Variability *input* mein hai, *control flow* mein
  nahi. Adaptive control flow = agent ka signature — yahan absent.
- **Choice:** Workflow — ek constrained extraction call + deterministic semantic-validation +
  targeted retry with the specific error.
- **Alternatives kyun kamzor:** Single agent = non-determinism + cost, koi control-flow benefit
  nahi. Direct call bina validation = syntactic-valid-but-semantically-wrong JSON silently pass.
- **Reusable rule:** *Path known + fixed → workflow. "Input varied" alone agent ko justify nahi
  karta.*

---

## Week 2 — The Agentic Loop by Hand

### Lab: correct by-hand loop + 5-bug diagnostic

- **Trade-off:** Loop ka stop condition kaise decide karun — (a) response mein text block hai?,
  (b) `stop_reason == "end_turn"`?, ya (c) har turn ke baad model se explicitly puchun "done?".
- **Choice:** (b) — `classify_stop_reason(response.stop_reason)` ko single branch point banaya, ek
  naya `sdk_parser` helper jo protocol signal ko loop-decision mein map karta hai.
- **Alternatives kyun kamzor:**
  - (a) "text block hai" = **Bug 3**. Mixed turn (prose + tool_use, stop_reason abhi `tool_use`)
    galat "final" classify hota hai, tool call silently drop.
  - (c) extra model round-trip = cost + latency + ek aur cheez jo galat ho sakti hai; model ki
    self-report reliable nahi (Domain 5 ka wahi sabaq — sentiment/confidence par mat bharoso).
- **Reusable rule:** *Loop completion protocol se decide hota hai (`stop_reason`), content shape ya
  model self-report se nahi.*

### Second trade-off: ceiling as symptom-patch vs root-cause fix

- **Trade-off:** "Loop forever chalta hai" ka fix — `MAX_TURNS` ceiling (Bug 4) ya check karo tool
  result wapas pahonch raha hai (Bug 2)?
- **Choice:** Dono. Ceiling zaroori hai (safety net, diagnosable error), lekin asal fix `tool_result`
  plumbing hai.
- **Alternatives kyun kamzor:** Sirf ceiling = crash to ruk gaya, lekin har run `MAX_TURNS` par
  waste hoke fail hoga — root cause (model ko result nahi mil raha) untouched.
- **Reusable rule:** *Symptom-patch aur root-cause-fix ek saath — ceiling crash rokta hai, plumbing
  masla theek karta hai.*
