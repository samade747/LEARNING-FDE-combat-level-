# HARNESS.md — Ratchet Log

One line per fix, every day for 7 days. Classify every agent mistake into one of the 4 failure
classes (Concept 10), then log which surface you fixed it on — same-shape mistake should become
**impossible** after the fix, not just less likely.

**4 failure classes:**
1. **Missing constraint** — agent could do something it shouldn't have been able to do
2. **Missing information** — agent didn't know something it needed to know
3. **Missing verification** — nothing checked the work before it counted as done
4. **Missing recovery** — when it went wrong, nothing caught/fixed it or told a human

## Day 1 — [date]

| Mistake | Class | Fix (which surface: deny rule / doc / hook / escalation) |
| --- | --- | --- |
| | | |

## Day 2 — [date]

| Mistake | Class | Fix |
| --- | --- | --- |

## Day 3 — [date]

## Day 4 — [date]

## Day 5 — [date]

## Day 6 — [date]

## Day 7 — [date]

## Week Verdict

- Per-class count: constraint __ / information __ / verification __ / recovery __
- Which class dominated? → that is where the harness was thinnest.
- Any same-shape mistake repeat after its fix? (should be **no** — that's the ratchet working)
