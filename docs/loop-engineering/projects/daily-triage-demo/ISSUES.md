<!-- Mock "open issues" board — stands in for real GitHub issues/npm audit, so this
     demo needs no live CI, no GitHub repo, no external service. -->

# Open Issues (Simulated)

## #1 — CI failure: greet_all drops the last name (bug)

`tests/test_greeter.py` is failing. `greet_all(["Ana", "Bilal"])` returns only
`["Hello, Ana!"]` — the last name in the list is silently missing.

**Risk:** low. Internal helper, one-line fix, tests define correct behaviour.

## #2 — Change the greeting format from "Hello, X!" to "Hi X" (feature request)

A teammate wants the greeting shortened. **This is a public-facing string other
services parse for the name.** Changing the format is a breaking change for any
consumer that expects `"Hello, "` as a prefix.

**Risk:** high — public behaviour change. Do NOT auto-fix. This is exactly the
kind of candidate the loop should escalate to "needs a human" instead of
shipping.
