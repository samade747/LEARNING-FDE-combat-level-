# P6-P7 — Stateless MCP I/II: Core + MRTR

*Practicum weeks P6 ("Stateless MCP I") + P7 ("Stateless MCP II: Schemas and MRTR"),
[`../../02-fde-practicum.md`](../../02-fde-practicum.md). Milestone 2 target (with P8): working MCP
agent surface.*

**Scope:** local-only (`127.0.0.1`), stdlib Python, no framework, no live deployment. Demonstrates
the **concepts** P6/P7 test — statelessness and the MRTR round-trip contract — over a simplified
transport (this scaffold uses a flat `{"method", "params"}` body, not the real HTTP headers/JSON-RPC
envelope). **2026-08-29 update:** field names (`resultType`, `inputRequests` as a map of
`elicitation/create` requests, `inputResponses` shaped like `ElicitResult`) and the `requestState`
integrity rules are now grounded directly against the primary source — the book only confirms the
stateless-HTTP *pattern*, so this was re-verified against
[the 2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) and
[the MRTR pattern page](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr)
directly. See `server.py`'s module docstring for the exact clauses each design choice traces to.

## Files

- `server.py` — a stdlib-only HTTP server (`ThreadingHTTPServer`) exposing `POST /mcp`. Two tools:
  `search_corpus` (plain stateless call) and `request_approval` (MRTR: first call returns
  `resultType: "input_required"` + a spec-shaped `inputRequests` map + a signed, opaque
  `requestState`; the retry supplies `inputResponses` + that same `requestState` to complete).
  `requestState`'s integrity envelope carries the principal, a 5-minute TTL, and a request digest —
  the spec's own replay-window guidance (2026-07-28 MRTR pattern, "Server Requirements" #5).
- `test_server.py` — starts the server as a subprocess, exercises it over real HTTP, verifies: two
  identical stateless calls agree, the MRTR round-trip completes (both the `accept` and `decline`
  `ElicitResult` actions), **replaying** the completed round-trip is safe (re-entrancy), and a
  **tampered** `requestState` is rejected, not silently trusted.

## Kaise Chalayein

```bash
cd docs/ccar-f-fde-track-b/projects/p6-p7-stateless-mcp
python test_server.py
```
This starts the server itself and shuts it down when done — no separate terminal needed. To poke at it
manually instead:
```bash
python server.py &   # or in a separate terminal
curl -s localhost:8765/mcp -d '{"method":"tools/call","params":{"tool":"search_corpus","arguments":{"query":"bin"}}}'
```

## Done Jab (Self-Check)

- [x] `test_server.py` passes — stateless calls agree, MRTR round-trip works (both `accept` and
      `decline` `ElicitResult` actions)
- [x] Re-entrancy check passes — replaying the same `requestState`+`inputResponses` twice is safe
- [x] Tamper check passes — a modified `requestState` is rejected with an explicit error, never
      silently accepted
- [ ] You read `unpack_state()` in `server.py` and can explain in one sentence why HMAC verification
      here is not the same thing as a server-side session lookup
- [ ] You can point at the exact spec clause each of `sign_state()`'s 3 envelope fields
      (`principal`, `exp`, `request_digest`) traces to — [MRTR pattern page](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr),
      "Server Requirements (Basic Workflow)" #5

---
[⬅ Practicum Index](../../02-fde-practicum.md) · [⬆ Chapter Index](../../README.md)
