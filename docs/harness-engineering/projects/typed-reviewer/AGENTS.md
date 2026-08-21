# The Typed Reviewer

This project has one job: prove `validate.sh` rejects any verdict that
doesn't match `schema.json` exactly, then wire that same validation into a
real reviewer (from fix-loop-demo or daily-triage-demo).

Never widen `schema.json`'s allowed `verdict` values to make a hand-crafted
bad verdict pass — the point is that `"MAYBE"` and friends must fail.
