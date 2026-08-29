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
