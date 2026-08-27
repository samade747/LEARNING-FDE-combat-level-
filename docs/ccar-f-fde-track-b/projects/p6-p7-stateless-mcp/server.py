"""P6-P7 scaffold: a minimal, stdlib-only MCP-shaped HTTP server demonstrating
the two things these practicum weeks actually test:

P6 — stateless core: every request is answered from its own body alone. No
in-memory session, no `initialize`/`initialized` handshake, no server-side
state keyed by a connection. Two independent processes of this same server
(or two threads, as the test proves) answer any request identically.

P7 — MRTR (multi-round-trip): a tool that needs more input from the caller
returns `input_required` with `inputRequests` and an **opaque** `requestState`
token. The token is HMAC-signed so the server can verify on the next call that
it issued it and it hasn't been tampered with — but the server keeps no record
of having issued it (that would be session state). The handler is re-entrant:
replaying the same requestState+inputResponses twice must be safe.

Concept scaffold only — field names here (`inputRequests`, `requestState`,
`inputResponses`) follow this repo's syllabus source
(`../../02-fde-practicum.md`), not a byte-exact MCP 2026-07-28 payload; the
book (`context-layer-crash-course`) confirms the stateless-HTTP *pattern* this
demonstrates, not MRTR's exact wire format — verify against the live spec
before treating this as a production implementation.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

SECRET = os.environ.get("MCP_SCAFFOLD_SECRET", "dev-secret-not-for-production").encode()

# The "governed corpus" this stateless server answers over — a plain dict
# stands in for a real indexed store. No mutation happens to this at request
# time (read-only), which is part of what makes statelessness safe here.
CORPUS = {
    "outcome-contracts": "An outcome contract defines the completed result before the workflow is designed.",
    "three-bin-sort": "Bin 1 keep (law/trust), Bin 2 redesign (human limits), Bin 3 delete (old technology).",
    "source-hierarchy": "When sources disagree, the higher-authority rung wins, if both are applicable.",
}


def sign_state(payload: dict) -> str:
    """Pack a dict into an opaque, tamper-evident requestState token.
    Opaque to the CALLER (it should not parse this), but structurally the
    server's own HMAC, not a session lookup key."""
    raw = json.dumps(payload, sort_keys=True).encode()
    sig = hmac.new(SECRET, raw, hashlib.sha256).hexdigest()
    blob = base64.urlsafe_b64encode(raw).decode()
    return f"{blob}.{sig}"


def unpack_state(token: str) -> dict:
    """Verify + unpack a requestState token. Raises ValueError on any
    tampering. This is the re-entrancy contract: calling this twice with the
    same token gives the same result, no side effects."""
    try:
        blob, sig = token.split(".", 1)
        raw = base64.urlsafe_b64decode(blob.encode())
    except Exception as exc:
        raise ValueError(f"malformed requestState: {exc}") from exc
    expected = hmac.new(SECRET, raw, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, sig):
        raise ValueError("requestState failed signature check — treat as untrusted, reject")
    return json.loads(raw)


def handle_tools_call(body: dict) -> dict:
    tool = body.get("tool")
    args = body.get("arguments", {})

    if tool == "search_corpus":
        query = (args.get("query") or "").lower()
        hits = [{"id": k, "snippet": v} for k, v in CORPUS.items() if query in k or query in v.lower()]
        return {"result": {"hits": hits}}

    if tool == "request_approval":
        # First call: no requestState yet -> ask for input (MRTR round 1).
        if "requestState" not in args:
            amount = args.get("amount")
            state = sign_state({"tool": "request_approval", "amount": amount})
            return {
                "status": "input_required",
                "inputRequests": [
                    {"id": "approver", "prompt": f"Approve action of amount {amount}? (yes/no)"}
                ],
                "requestState": state,
            }
        # Second call: caller supplies inputResponses + the requestState they
        # were given. Server re-verifies the state itself — no lookup table.
        try:
            original = unpack_state(args["requestState"])
        except ValueError as exc:
            return {"status": "error", "error": str(exc)}
        responses = args.get("inputResponses", {})
        decision = (responses.get("approver") or "").strip().lower()
        if decision not in ("yes", "no"):
            return {"status": "error", "error": "inputResponses.approver must be 'yes' or 'no'"}
        return {
            "status": "complete",
            "result": {"amount": original["amount"], "approved": decision == "yes"},
        }

    return {"status": "error", "error": f"unknown tool: {tool}"}


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
            self.wfile.write(b'{"status":"error","error":"invalid JSON"}')
            return

        method = body.get("method")
        if method == "tools/list":
            resp = {"tools": ["search_corpus", "request_approval"]}
        elif method == "tools/call":
            resp = handle_tools_call(body.get("params", {}))
        else:
            resp = {"status": "error", "error": f"unknown method: {method}"}

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
