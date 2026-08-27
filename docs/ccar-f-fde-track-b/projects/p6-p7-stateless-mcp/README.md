# P6-P7 — Stateless MCP I/II: Core + MRTR

*Practicum weeks P6 ("Stateless MCP I") + P7 ("Stateless MCP II: Schemas and MRTR"),
[`../../02-fde-practicum.md`](../../02-fde-practicum.md). Milestone 2 target (with P8): working MCP
agent surface.*

**Scope:** local-only (`127.0.0.1`), stdlib Python, no framework, no live deployment. Demonstrates the
**concepts** P6/P7 test — statelessness and the MRTR round-trip contract — not a byte-exact MCP
2026-07-28 wire implementation. See the "Honest gap" note in
[`../../02-fde-practicum.md`](../../02-fde-practicum.md#technology-baseline): the book confirms the
stateless-HTTP *pattern*; MRTR's exact field names come from the MCP spec itself, verify against the
live spec before treating this as production-ready.

## Files

- `server.py` — a stdlib-only HTTP server (`ThreadingHTTPServer`) exposing `POST /mcp`. Two tools:
  `search_corpus` (plain stateless call) and `request_approval` (MRTR: first call returns
  `input_required` + `inputRequests` + a signed opaque `requestState`; second call supplies
  `inputResponses` + that `requestState` to complete).
- `test_server.py` — starts the server as a subprocess, exercises it over real HTTP, verifies: two
  identical stateless calls agree, the MRTR round-trip completes, **replaying** the completed round-trip
  is safe (re-entrancy), and a **tampered** `requestState` is rejected, not silently trusted.

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

- [x] `test_server.py` passes — stateless calls agree, MRTR round-trip works
- [x] Re-entrancy check passes — replaying the same `requestState`+`inputResponses` twice is safe
- [x] Tamper check passes — a modified `requestState` is rejected with an explicit error, never
      silently accepted
- [ ] You read `unpack_state()` in `server.py` and can explain in one sentence why HMAC verification
      here is not the same thing as a server-side session lookup

---
[⬅ Practicum Index](../../02-fde-practicum.md) · [⬆ Chapter Index](../../README.md)
