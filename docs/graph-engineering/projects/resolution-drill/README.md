# Graph Project 5 — Resolution Drill

**Concept:** 7 (Resolution: additive, reversible, false merge is the catastrophic failure) ·
**Time:** 45-60 min · **Difficulty:** Medium

20 surface forms across 9 real entities — merge the real duplicates, and keep 2 same-named strangers
apart on purpose.

## Files

- `surface_forms.json` — 20 surface forms, each with `id`, `text`, `description`, `doc_ref`
- `expected_clusters.json` — the answer key (9 canonical entities)
- `clusters-good-example.json` — a correct clustering (matches the answer key exactly)
- `clusters-bad-example.json` — deliberately flawed: false-merges the trap, misses a real merge
- `check_resolution.py` — scorer: checks every real multi-form entity merged into one cluster, AND
  that the 2 "J. Patel" entries (same printed name, different people, different descriptions) stayed
  apart

## The Trap

`sf19` ("J. Patel", Bright Horizon compliance officer, approved an access-log review) and `sf20`
("J. Patel", an unrelated hardware vendor contact) share an identical printed surface form. String
similarity would merge them instantly — wrong. Their **descriptions** are the only thing that tells
you they're different people. This is Concept 7's exact failure mode, planted on purpose.

## Setup

Python 3 only.

## Test It

```bash
cd docs/graph-engineering/projects/resolution-drill
python check_resolution.py clusters-good-example.json   # expect: exit 0, "additive and correct"
python check_resolution.py clusters-bad-example.json     # expect: exit 1, 2 issues (missed merge + false merge)
```

## Apna Kaam Karo

1. `surface_forms.json` parho (bina `expected_clusters.json` khole).
2. Har surface form ko ek stronger model se dikhao (description ke sath), canonical clusters banwao
   rationale + confidence ke sath, har alias rakhte hue. Apni `my-clusters.json` likho (same shape as
   `clusters-good-example.json`).
3. `python check_resolution.py my-clusters.json` chalao.
4. Agar trap merge ho jaye, resolution prompt **fix mat karo pehle** — descriptions ko richer likho
   pehle (jaisa book kehti hai), phir dobara chalao.

## Done Jab (Self-Check)

- [ ] Good aur bad examples dono par scorer sahi result deta hai (exit 0 / exit 1)
- [ ] Apni `my-clusters.json` mein sab 7 real multi-form entities (Chen, Northwind, Meridian, Contract,
      Ortiz, Bright Horizon, Incident) fully merged hain
- [ ] Apni `my-clusters.json` mein 2 "J. Patel" alag clusters mein hain
- [ ] Har canonical entity apne surface forms list karta hai (alias kabhi mitaya nahi)

---
[⬆ Practice Projects Index](../../08-practice-projects.md)
