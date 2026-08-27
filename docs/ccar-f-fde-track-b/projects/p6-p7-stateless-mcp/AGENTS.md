# P6-P7 — Stateless MCP Scaffold

This project's one job: prove two properties, not just demo a server that runs.

1. **Stateless:** no in-memory session keyed by connection or client. Two identical calls must return
   identical results with no prior handshake.
2. **`requestState` is untrusted input on the way back in.** `unpack_state` in `server.py` re-verifies
   the HMAC every time — do not remove that check or replace it with a server-side lookup table (a
   lookup table would silently reintroduce session state).

Do not "simplify" `server.py` by caching approvals in a dict keyed by some session id — that defeats
the whole point of this scaffold.
