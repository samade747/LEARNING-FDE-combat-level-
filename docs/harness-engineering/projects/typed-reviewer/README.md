# Harness Project 5 — The Typed Reviewer

**Concept:** 9 (typed output) · **Time:** 1-1.5 hrs · **Difficulty:** Medium-Hard

Upgrades the plain PASS/FAIL reviewer (like Loop Engineering's
[`fix-loop-demo`](../../../loop-engineering/projects/fix-loop-demo/)) to a typed JSON verdict, with
field-by-field `jq` validation. `schema.json` defines the required shape. `validate.sh` checks it.
Two samples are included: `sample_bad_verdict.json` (a protocol break — `"MAYBE"` isn't an allowed
verdict, and `files_reviewed` is missing) and `sample_good_verdict.json` (valid).

## Setup

Needs `jq` installed (`jq --version` to check). **Windows gotcha:** not installed by default —
`winget install jqlang.jq`, then open a **new** terminal (PATH only refreshes for new windows,
same gotcha as `gh` CLI in the Doorbell project). Then:

```bash
cd docs/harness-engineering/projects/typed-reviewer
chmod +x validate.sh   # not needed on Windows git-bash, harmless either way
```

## Test It

```bash
./validate.sh sample_good_verdict.json   # expect: VALID, exit 0
./validate.sh sample_bad_verdict.json    # expect: PROTOCOL BREAK, exit 1
```

Then wire this into your own reviewer (from `fix-loop-demo` or `daily-triage-demo`): change its
output format to match `schema.json`, run `validate.sh` on its output, and route any non-zero exit
to a "needs a human" escalation instead of guessing what the reviewer meant.

## Done jab (self-check)

- [ ] `sample_good_verdict.json` → VALID
- [ ] `sample_bad_verdict.json` → PROTOCOL BREAK (exit 1, not silently accepted)
- [ ] Apni reviewer se same test kiya — hand-crafted bad verdict escalate hui, guess nahi hui

---
[⬆ Harness Practice Log](../../11-practice-log.md) · [Poori list](../../07-practice-projects.md)
