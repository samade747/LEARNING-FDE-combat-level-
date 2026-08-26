# Graph Project 2 — Spine to Claims

**Concept:** 1, 8, Part 6 (provenance, the schema) · **Time:** 30-45 min · **Difficulty:** Easy

`progress.md` ek loop ke liye theek hai, lekin ek doosri loop is par bharosa nahi kar sakti — prose hai,
format badal sakta hai. Yeh project real (ya realistic) findings ko **typed claims** mein convert karta
hai, taake aap dekh sako kitna kuch aap "fact" samajh rahe thay sirf model ki fluency ki wajah se.

## Files

- `progress-sample.md` — 10 realistic triage-loop findings (fake data, real shape)
- `graph-SCHEMA.md` — Part 6 ka claim contract (fields, types, 3 invariants)
- `claims-example.json` — **worked answer key**: sab 10 findings convert kiye, invariants ke sath
- `claims-bad-example.json` — jaan-boojh kar 5 violations (missing source, duplicate id, unresolved
  supersedes) — dikhane ke liye ke validator kya pakarta hai
- `validate_claims.py` — validator script (book "jq" use karti hai; is machine par `jq` nahi tha, isliye
  Python se same checks — dependency-free, portable)

## Setup

Koi install nahi chahiye — sirf Python 3 (`python --version` check karo).

## Test It

```bash
cd docs/graph-engineering/projects/spine-to-claims
python validate_claims.py claims-example.json       # expect: exit 0, "All invariants hold"
python validate_claims.py claims-bad-example.json    # expect: exit 1, 5 violations listed
```

## Apna Kaam Karo

1. Apni **asal** `progress.md` (ya kisi loop ka real log) lo — agar nahi hai, `progress-sample.md` use
   karo.
2. Uske aakhri 10 durable findings ko `graph-SCHEMA.md` ke under apni `my-claims.json` mein convert karo.
3. Har claim ke liye faisla karo: kya isay ek real source cite ho sakta hai (`tool_output`/`document`
   with `ref`), ya kya ye sirf ek judgment call thi (`inference`)?
4. `python validate_claims.py my-claims.json` chalao — clean until it passes.

## Done Jab (Self-Check)

- [ ] `claims-example.json` aur `claims-bad-example.json` dono par validator sahi result deta hai
      (`0` aur `1` exit codes upar dikhaye gaye jaisay)
- [ ] Apni `my-claims.json` mein sab 10 claims validator pass karte hain
- [ ] **Inference count note kiya** — `claims-example.json` mein 4/10 hain (dark-mode classification,
      "felt right" null-check removal, latency-regression guess, public-API escalation reasoning).
      Apni file mein bhi count karo — yehi number batata hai aap kitni cheezein bina proof ke "fact"
      samajh rahe thay.

---
[⬆ Practice Projects Index](../../08-practice-projects.md)
