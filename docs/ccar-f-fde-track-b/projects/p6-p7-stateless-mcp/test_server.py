"""Starts server.py as a subprocess, exercises it over real HTTP, and checks
both P6 (stateless call) and P7 (MRTR round-trip + tamper rejection +
re-entrancy) behave as claimed. Run: python test_server.py
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

PORT = 8765
URL = f"http://127.0.0.1:{PORT}/mcp"
HERE = os.path.dirname(os.path.abspath(__file__))


def call(method: str, params: dict | None = None) -> dict:
    body = json.dumps({"method": method, "params": params or {}}).encode()
    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5) as resp:
        return json.loads(resp.read())


def main() -> int:
    proc = subprocess.Popen([sys.executable, "server.py"], cwd=HERE)
    errors: list[str] = []
    try:
        for _ in range(50):
            try:
                call("tools/list")
                break
            except (urllib.error.URLError, ConnectionRefusedError):
                time.sleep(0.1)
        else:
            print("FAILED: server never came up")
            return 1

        # P6 — stateless: two independent calls, no session between them,
        # both must succeed identically without any prior handshake.
        r1 = call("tools/call", {"tool": "search_corpus", "arguments": {"query": "bin"}})
        r2 = call("tools/call", {"tool": "search_corpus", "arguments": {"query": "bin"}})
        if r1 != r2:
            errors.append(f"P6: two identical stateless calls returned different results: {r1} vs {r2}")
        if not r1.get("result", {}).get("hits"):
            errors.append(f"P6: expected hits for query 'bin', got {r1}")

        # P7 — MRTR round 1: ask for approval, expect input_required + requestState.
        # inputRequests is a spec-shaped map: {"approver": {"method": "elicitation/create", ...}}.
        round1 = call("tools/call", {"tool": "request_approval", "arguments": {"amount": 500}})
        if round1.get("resultType") != "input_required" or "requestState" not in round1:
            errors.append(f"P7 round 1: expected input_required + requestState, got {round1}")
        if round1.get("inputRequests", {}).get("approver", {}).get("method") != "elicitation/create":
            errors.append(f"P7 round 1: inputRequests.approver should be a spec-shaped elicitation/create request, got {round1.get('inputRequests')}")
        state = round1.get("requestState", "")

        # P7 round 2: caller echoes requestState UNCHANGED and supplies
        # inputResponses, keyed the same as inputRequests, shaped like the
        # matching ElicitResult ({"action": "accept"|"decline", "content": {...}}).
        round2 = call(
            "tools/call",
            {
                "tool": "request_approval",
                "arguments": {"requestState": state, "inputResponses": {"approver": {"action": "accept", "content": {"decision": "yes"}}}},
            },
        )
        if round2 != {"resultType": "complete", "result": {"amount": 500, "approved": True}}:
            errors.append(f"P7 round 2: unexpected result {round2}")

        # P7 re-entrancy: replay the exact same round-2 call — must succeed
        # identically, proving the handler keeps no session that a first call
        # would have consumed.
        round2_replay = call(
            "tools/call",
            {
                "tool": "request_approval",
                "arguments": {"requestState": state, "inputResponses": {"approver": {"action": "accept", "content": {"decision": "yes"}}}},
            },
        )
        if round2_replay != round2:
            errors.append(f"P7 re-entrancy: replay gave different result: {round2_replay} vs {round2}")

        # P7 tamper rejection: a client-modified requestState must be refused,
        # never silently trusted.
        tampered_state = state[:-4] + "0000"
        tampered = call(
            "tools/call",
            {
                "tool": "request_approval",
                "arguments": {"requestState": tampered_state, "inputResponses": {"approver": {"action": "accept", "content": {"decision": "yes"}}}},
            },
        )
        if tampered.get("resultType") != "error":
            errors.append(f"P7 tamper check: tampered requestState was NOT rejected: {tampered}")

        # P7 decline path: the ElicitResult action can also be "decline".
        round1b = call("tools/call", {"tool": "request_approval", "arguments": {"amount": 900}})
        state_b = round1b.get("requestState", "")
        declined = call(
            "tools/call",
            {
                "tool": "request_approval",
                "arguments": {"requestState": state_b, "inputResponses": {"approver": {"action": "decline", "content": {}}}},
            },
        )
        if declined != {"resultType": "complete", "result": {"amount": 900, "approved": False}}:
            errors.append(f"P7 decline path: unexpected result {declined}")

    finally:
        proc.terminate()
        proc.wait(timeout=5)

    if errors:
        print("FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("All checks passed: stateless calls agree, MRTR round-trip works, replay is safe, "
          "tampered requestState is rejected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
