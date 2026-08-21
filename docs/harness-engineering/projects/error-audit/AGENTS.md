# The Error Audit

This project has one job: rewrite `connector_before.py`'s 3 error messages
so each one tells the reader (an agent, not a human) exactly what to change
next, then prove the fix by re-running until the agent self-heals.

Do not just copy `connector_after.py` — write your own rewrite first, then
compare. Copying skips the actual skill this project teaches.
