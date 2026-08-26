# Graph Project 7 — A Gold Set for Extraction

**Concept:** 6, 7 (measure the pipeline that fills your memory, one course early) ·
**Time:** 2-3 hrs · **Difficulty:** Hard

Hand-label 5 documents, then score an extraction prompt against your own labels — this IS graph
autoresearch: same ratchet loop, a prompt as the artifact instead of a training script.

## Files

- `docs/doc1.md` … `doc5.md` — 5 short documents (a fictional patent-dispute story, fake data)
- `gold_labels.json` — hand-labeled truth: 5 entities, 7 relations, merged across all 5 docs
- `predicted_v1.json` — a simulated **first-attempt** extraction (worse): one misspelled entity name
  ("Data Core Systems" vs the correct "DataCore Systems"), one wrong predicate, one hallucinated
  relation, one missed entity (James Wu)
- `predicted_v2.json` — a simulated **second attempt**, after one prompt-line fix ("copy entity names
  exactly as printed, prefer the document's own verb") — better, still misses 1 relation
- `score_extraction.py` — computes relation precision/recall (exact triple match), entity recall, and
  a schema-valid rate

## Setup

Python 3 only.

## Test It (Verified Numbers)

```bash
cd docs/graph-engineering/projects/gold-set-extraction
python score_extraction.py predicted_v1.json
python score_extraction.py predicted_v2.json
```

Expect exactly this ratchet:

| | Precision | Recall | Entity recall |
| --- | --- | --- | --- |
| `predicted_v1.json` | 0.33 | 0.29 | 0.60 |
| `predicted_v2.json` | 1.00 | 0.86 | 1.00 |

One prompt-line fix (consistent entity spelling + verb-matched predicates) took precision from 0.33 to
1.00. This is the number the book means by "keep or revert on the number" — not a feeling.

## Apna Kaam Karo (Real Ratchet)

1. Read `docs/doc1.md`–`doc5.md` yourself, hand-label your **own** `my_gold_labels.json` — don't peek
   at `gold_labels.json` first, then compare afterward to calibrate your labeling judgment.
2. Run Project 3's extraction prompt (or your own) against all 5 docs, merge the results into one
   `my_predicted.json`.
3. `python score_extraction.py my_predicted.json` — note precision/recall/schema-valid rate.
4. Change exactly **one line** of the prompt, re-run, re-score. Keep the change only if the number
   improved. Do this at least 3 times, keeping a record of every attempt (including reverted ones).

## Done Jab (Self-Check)

- [ ] `predicted_v1.json` aur `predicted_v2.json` par scorer upar wali table match karta hai
- [ ] Apni real extraction ratchet kam se kam 3 dafa chalayi, reverted attempts samet record ke saath
- [ ] Aap bata sakte ho: **precision** kis mistake ko punish karta hai (galat/hallucinated relations),
      **recall** kis ko (missed relations) — aur apni v1→v2 mein har fix ne kaunsa number move kiya

---
[⬆ Practice Projects Index](../../08-practice-projects.md)
