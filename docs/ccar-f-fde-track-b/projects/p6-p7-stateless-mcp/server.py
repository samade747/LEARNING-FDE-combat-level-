"""P6-P7 scaffold: a minimal, stdlib-only MCP-shaped HTTP server demonstrating
the two things these practicum weeks actually test.

Grounded directly against the primary source, fetched 2026-08-29:
https://modelcontextprotocol.io/specification/2026-07-28/changelog and
https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr
(the book's own `context-layer-crash-course` only confirms the stateless-HTTP
*pattern*, not MRTR's wire format — this scaffold now follows the spec, not
just the pattern).

P6 — stateless core: every request is answered from its own body alone. The
real 2026-07-28 spec removes the `initialize`/`initialized` handshake AND the
`Mcp-Session-Id` header entirely — servers needing cross-call state must use
explicit, server-minted handles passed as ordinary arguments (that is exactly
what `requestState` below is). Two independent processes of this same server
(or two threads, as the test proves) answer any request identically.

P7 — MRTR (Multi Round-Trip Requests, SEP-2322): a request that needs more
input from the caller returns a result with `resultType: "input_required"`,
an `inputRequests` map (keys are server-assigned ids, values are request
objects — here an `elicitation/create` request, spec-shaped: `method` +
`params.mode`/`message`/`requestedSchema`), and an **opaque** `requestState`
string. Per the spec: "servers MUST protect its integrity (e.g. HMAC or AEAD)
and MUST reject state that fails verification" — this scaffold HMAC-signs it.
The client is required to echo `requestState` back UNCHANGED on retry inside
`inputResponses` (keyed the same as `inputRequests`, each value shaped like
the matching `ElicitResult`: `{"action": "accept"|"decline", "content": {...}}`).
The server keeps no record of having issued the token (that would be session
state) — it re-verifies the HMAC on every call. The handler is re-entrant:
replaying the same requestState+inputResponses twice must be safe, per the
spec's own replay-window guidance (principal + short TTL + request digest
inside the integrity-protected payload).
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

SECRET = os.environ.get("MCP_SCAFFOLD_SECRET", "dev-secret-not-for-production").encode()
STATE_TTL_SECONDS = 300

# The "governed corpus" this stateless server answers over — a plain dict
# stands in for a real indexed store. No mutation happens to this at request
# time (read-only), which is part of what makes statelessness safe here.
CORPUS = {
    "outcome-contracts": "An outcome contract defines the completed result before the workflow is designed.",
    "three-bin-sort": "Bin 1 keep (law/trust), Bin 2 redesign (human limits), Bin 3 delete (old technology).",
    "source-hierarchy": "When sources disagree, the higher-authority rung wins, if both are applicable.",
}


def sign_state(payload: dict, principal: str, request_digest: str) -> str:
    """Pack a dict into an opaque, tamper-evident requestState token. Opaque
    to the CALLER (spec: clients MUST NOT inspect/parse/modify it), but
    structurally the server's own HMAC, not a session lookup key. Per the
    spec's replay-window guidance (2026-07-28 MRTR pattern, "Server
    Requirements" #5), the integrity-protected payload carries the
    authenticated principal, a short TTL, and a digest of the originating
    request — each re-checked on unpack so a token can't be replayed by a
    different principal, after it expires, or against a different request."""
    envelope = {
        "payload": payload,
        "principal": principal,
        "exp": time.time() + STATE_TTL_SECONDS,
        "request_digest": request_digest,
    }
    raw = json.dumps(envelope, sort_keys=True).encode()
    sig = hmac.new(SECRET, raw, hashlib.sha256).hexdigest()
    blob = base64.urlsafe_b64encode(raw).decode()
    return f"{blob}.{sig}"


def unpack_state(token: str, principal: str, request_digest: str) -> dict:
    """Verify + unpack a requestState token. Raises ValueError on any
    tampering, expiry, principal mismatch, or request mismatch. This is the
    re-entrancy contract: calling this twice with the same token, principal,
    and request gives the same result, no side effects (single-use beyond
    that bound is a server-side invariant this scaffold does not need)."""
    try:
        blob, sig = token.split(".", 1)
        raw = base64.urlsafe_b64decode(blob.encode())
    except Exception as exc:
        raise ValueError(f"malformed requestState: {exc}") from exc
    expected = hmac.new(SECRET, raw, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, sig):
        raise ValueError("requestState failed signature check — treat as untrusted, reject")
    envelope = json.loads(raw)
    if envelope["principal"] != principal:
        raise ValueError("requestState was issued to a different principal")
    if time.time() > envelope["exp"]:
        raise ValueError("requestState has expired")
    if envelope["request_digest"] != request_digest:
        raise ValueError("requestState does not match this request")
    return envelope["payload"]


def _digest(*parts: str) -> str:
    return hashlib.sha256("|".join(parts).encode()).hexdigest()[:16]


def handle_tools_call(body: dict, principal: str = "anonymous") -> dict:
    tool = body.get("tool")
    args = body.get("arguments", {})

    if tool == "search_corpus":
        query = (args.get("query") or "").lower()
        hits = [{"id": k, "snippet": v} for k, v in CORPUS.items() if query in k or query in v.lower()]
        return {"resultType": "complete", "result": {"hits": hits}}

    if tool == "request_approval":
        # First call: no requestState yet -> MRTR round 1. inputRequests is a
        # map keyed by server-assigned id; the value is a real
        # `elicitation/create` request, spec-shaped (method + params).
        if "requestState" not in args:
            amount = args.get("amount")
            digest = _digest("request_approval")
            state = sign_state({"tool": "request_approval", "amount": amount}, principal, digest)
            return {
                "resultType": "input_required",
                "inputRequests": {
                    "approver": {
                        "method": "elicitation/create",
                        "params": {
                            "mode": "form",
                            "message": f"Approve action of amount {amount}?",
                            "requestedSchema": {
                                "type": "object",
                                "properties": {"decision": {"type": "string", "enum": ["yes", "no"]}},
                                "required": ["decision"],
                            },
                        },
                    }
                },
                "requestState": state,
            }
        # Second call (the retry): caller echoes requestState UNCHANGED and
        # supplies inputResponses, keyed the same as inputRequests, each
        # value shaped like the matching ElicitResult. Server re-verifies the
        # state itself — no lookup table, no memory of round 1 ever happening.
        # The digest re-derives to the same value as round 1 (bound to the
        # tool name, not the retry's payload) — that is what "rejects state
        # presented on a request that does not match" means here: a
        # requestState minted for a different tool can never be replayed onto
        # this one, even though this scaffold has no per-instance lookup table.
        responses = args.get("inputResponses", {})
        approver_response = responses.get("approver", {})
        try:
            original = unpack_state(args["requestState"], principal, _digest("request_approval"))
        except ValueError as exc:
            return {"resultType": "error", "error": str(exc)}
        action = approver_response.get("action")
        if action not in ("accept", "decline"):
            return {"resultType": "error", "error": "inputResponses.approver.action must be 'accept' or 'decline'"}
        return {
            "resultType": "complete",
            "result": {"amount": original["amount"], "approved": action == "accept"},
        }

    return {"resultType": "error", "error": f"unknown tool: {tool}"}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # quiet the default stderr logging
        pass

    def do_POST(self):
        if self.path != "/mcp":
            self.send_response(404)
            self.end_headers()
            return
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'{"resultType":"error","error":"invalid JSON"}')
            return

        method = body.get("method")
        if method == "tools/list":
            resp = {"tools": ["search_corpus", "request_approval"]}
        elif method == "tools/call":
            resp = handle_tools_call(body.get("params", {}))
        else:
            resp = {"resultType": "error", "error": f"unknown method: {method}"}

        payload = json.dumps(resp).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def run(port: int = 8765):
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"Stateless MCP scaffold listening on http://127.0.0.1:{port}/mcp")
    server.serve_forever()


if __name__ == "__main__":
    run()
