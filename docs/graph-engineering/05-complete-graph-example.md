# 05 — Ek Complete Graph (Morning Triage Upgrade)

Theory khatam. Ab wahi morning-triage loop (Loop Engineering se) — jo Harness Engineering ne fence ki
thi — ko prose spine se ek chhoti, **queryable graph** mein upgrade karte hain. **Sirf files aur shell,
koi database, koi framework nahi** — graph repo mein 3 JSON files hai, discipline **schema** hai,
storage nahi.

## Disk Pe Shape

```
graph/
  SCHEMA.md        # contract: fields, types, write rules
  entities.json    # nodes: cheezein jinke baare mein loops baat karti hain
  claims.json      # edges-with-receipts: kya establish hua
  runs.json        # kaam ka side: kaunsi beat ne kya likha
evidence/
  run_2026-07-21-triage.log   # raw tool output jise claim point kar sake
```

2 directories, alag cheezein rakhti hain. `graph/` **curated memory** hai — chhoti, schema-checked.
`evidence/` **raw output** hai jise claims point back karti hain. `evidence/` mein kuch bhi kabhi edit
nahi hota.

**JSON kab kaafi nahi rehta?** Low thousands of claims tak comfortable hai, ~10,000 ke ird gird dard
shuru hota hai. Upgrade path: **relational table** (Postgres/SQLite) — real ids, indexes, transactions.
**Graph database** (Neo4j) — multi-hop traversal ek query ki tarah, code nahi. Koi bhi move kisi
invariant ko nahi badalta. **Jab query slow ho ya write kho jaye, tab move karo — pehle nahi.**

## Ek Claim, Poori Tarah

```json
{
  "id": "claim_0007",
  "subject": "test_payments_flaky",
  "predicate": "diagnosed_as",
  "object": "tz_default_utc",
  "confidence": 0.9,
  "source": {
    "kind": "tool_output",
    "command": "pytest tests/test_payments.py -x",
    "exit_code": 1,
    "ref": "evidence/run_2026-07-21-triage.log#L88-L94",
    "captured": "2026-07-21T09:14:22Z"
  },
  "produced_by": "run_2026-07-21-triage",
  "supersedes": "claim_0004",
  "created": "2026-07-21"
}
```

**3 zaroori design decisions:**

1. **Koi `status` field nahi.** Claims **append-only** hain — kabhi edit, kabhi delete nahi. Claim abhi
   bhi current hai ya nahi — ye stored nahi hota, **read time pe derive hota hai**: claim active hai
   agar koi baad wali claim usay supersede na kare.

```bash
# active claims = jinhe koi supersede nahi karta
jq '[.[].supersedes] as $dead
    | [.[] | select(.id | IN($dead[]) | not)]' graph/claims.json
```

2. **Predicate `diagnosed_as` hai, `caused_by` nahi.** Failing test (exit code 1) prove karta hai kuch
   fail hua. Ye prove nahi karta **kyun** — wo agent ki reading hai. Isliye claim wahi bolti hai jo
   evidence support karti hai. `caused_by` tak upgrade zyada evidence maangta hai.

3. **Source tool ka naam leta hai, agent ka nahi.** `"kind": "tool_output"` command + exit_code + line
   range ke sath us cheez ki taraf point karta hai jo **kisi model ne nahi likhi**: pytest fail hua, aur
   yahan wo kehta hai. **Rule:** run log sirf tab anchor hai jab cited lines **model ke bahar se
   captured output** hon. Agent ka apna prose log mein evidence nahi, claim hai.

Baaki 2 files chhoti hain:

```json
// entities.json
[{ "id": "test_payments_flaky", "type": "TEST",
   "aliases": ["tests/test_payments.py::test_tz"], "first_seen": "2026-07-14" }]

// runs.json
[{ "id": "run_2026-07-21-triage", "beat": "morning-triage",
   "evidence": ["evidence/run_2026-07-21-triage.log"],
   "claims_written": ["claim_0007"], "verdict": "PASS" }]
```

## Maker Graph Mein Likhta Hai

Triage skill mein ek paragraph add hota hai. Purana *"update progress.md"* ab ye ban jata hai:

```markdown
## 5. Update the graph last

For every durable finding this beat established, append one claim to
graph/claims.json following the schema in graph/SCHEMA.md. Rules:

- claims.json is APPEND-ONLY. Never edit and never delete an existing claim.
  To correct a claim, append a new one whose "supersedes" names the old id.
- Every claim needs a source a later agent could open and verify. Prefer
  captured tool output. If the finding is your own reasoning with no
  external output, mark it "source": {"kind": "inference"}.
- Never cite your own prose in a log as the evidence for your own claim.
- New entities go in entities.json first. Check aliases before adding.
- Session notes, dead ends, chatter stay in progress.md. The graph is for
  what was established, not what was said.
```

**Zaroori:** Spine gayab nahi hoti — wo loop ki diary rehti hai. **Graph wo chhoti, sakht record hai jo
diary ne PROVE kiya.** 2 memories, 2 truth standards.

**Pre-commit hook** in rules ko real banata hai (guardrail harness mein rehta hai, prompt mein nahi):

```sh
#!/bin/sh
# .git/hooks/pre-commit — graph gate (sirf jq, koi framework nahi)
C=graph/claims.json
fail() { echo "claims.json: $1 — commit blocked"; exit 1; }

# 1. har claim mein required fields
jq -e 'all(.[]; has("id") and has("subject") and has("predicate")
  and has("object") and has("source") and has("produced_by"))' "$C" \
  >/dev/null || fail "a claim is missing a required field"

# 2. ids unique hain
[ "$(jq 'length' "$C")" = "$(jq '[.[].id] | unique | length' "$C")" ] \
  || fail "duplicate claim id"

# 3. har supersedes target exist karta hai
jq -e --argjson ids "$(jq '[.[].id]' "$C")" \
  'all(.[]; (has("supersedes") | not) or (.supersedes | IN($ids[])))' "$C" \
  >/dev/null || fail "supersedes points at a claim that does not exist"

# 4. append-only: jo commit ho chuka wo badal nahi sakta
git show HEAD:"$C" 2>/dev/null > /tmp/old.json || exit 0
jq -e --slurpfile new "$C" \
  'all(.[]; . as $o | $new[0] | any(.[]; . == $o))' /tmp/old.json \
  >/dev/null || fail "an existing claim was modified or removed"
```

**Honesty note:** Ye 4 checks real hain — required fields, unique ids, resolvable supersession,
append-only. Jo hook **check nahi karta**: field types, kya `subject` entities.json mein exist karta
hai, kya evidence file/line range asal mein exist karta hai. Jo abhi likhi nahi wo rule sirf `SCHEMA.md`
mein rehti hai — **guidance hai, guardrail nahi**.

## Reviewer Graph Se Parhta Hai

```markdown
You are the reviewer. For every factual claim in the maker's report:
1. Find the claim in graph/claims.json that supports it. Cite its id.
2. If no active claim supports it, your verdict is REVISE.
3. A claim whose source.kind is "inference" cannot by itself ground a
   factual assertion. Either cite a source-backed claim, or REVISE.
4. Never approve a factual claim on plausibility. "Sounds right" is not
   a citation.

Return only JSON:
{ "verdict": "PASS|REVISE|FAIL",
"grounded_in": ["claim_0007", "claim_0012"],
"missing": [],
"rubric": "reviewer-rubric-v3" }
```

**Rule 3 sab se zaroori hai jo log chhor dete hain.** Maker honestly inference record kar sakta hai —
yehi sahi hai (marked guess laundered guess se behtar hai). Lekin agar reviewer sirf check kare ke cited
claim **exist** karti hai, to marked guess bhi ek factual statement ko ground kar sakti hai, aur graph
ne usay launder kar diya. **Honest inference aur grounding evidence alag kaam hain. Reviewer ka kaam
unhe alag rakhna hai.**

## Ek Beat, Pehle Aur Baad Mein

**Pehle (sirf spine):** Mangal ko triage beat flaky test fix karti hai, prose likhti hai: *"fixed flaky
test, was a timezone thing."* Guruwar ko, changelog loop payments fix mention karti hai, uska reviewer
plausibility pe approve kar deta hai. 3 hafte baad koi puchta hai konsi timezone assumption thi — jawab
transcripts ki **archaeology dig** hai.

**Baad mein (graph):** Mangal ki beat `claim_0007` likhti hai, pytest output cite karte hue jo usne
`evidence/` mein capture ki thi. Guruwar ko, changelog loop `test_payments_flaky` ke ird gird 2-hop
subgraph pull karti hai. Uska reviewer approve karta hai **kyunke** `grounded_in: ["claim_0007"]`
resolve hoti hai. 3 hafte baad, sawal `jq` se **ek line mein, receipt ke sath** answer ho jata hai.

**Same loops. Same model. Sirf memory ka pata badla** — aur wo badalta hai har baad wala agent, aur har
baad wala insaan, kya jaan sakta hai.

---
[⬅ Graph of Loops](04-graph-of-loops.md) · [Agla: Staying Grounded ➡](06-staying-grounded.md)
