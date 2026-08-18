#!/usr/bin/env python3
"""joke.py — the deterministic fetch. One run = one real joke, fresh from the API.

A joke loop earns trust the same way a watch does: it never makes one up. If the
API cannot be reached, this exits non-zero and says so, rather than inventing a
joke and pretending it came from the internet. A fabricated joke told as real is
the one thing this script must never do.

Usage:
    python3 joke.py            # one joke, plain text
    python3 joke.py --json     # raw {setup, punchline, id} for computing
"""

import json
import sys
import time
import urllib.request

API = "https://official-joke-api.appspot.com/random_joke"
TIMEOUT = 10
TRIES = 3


def fetch():
    """Return one joke dict from the API, or exit non-zero with a reason."""
    last = None
    for attempt in range(1, TRIES + 1):
        try:
            with urllib.request.urlopen(API, timeout=TIMEOUT) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001 — every failure reads the same to this loop
            last = e
            if attempt < TRIES:
                time.sleep(1)
    print(f"Could not reach the joke API after {TRIES} tries ({last}).")
    print("Do not make one up — say the fetch failed and let the next run try again.")
    sys.exit(1)


def card(j):
    line = "─" * 50
    return "\n".join(
        [
            "",
            "  \U0001f602  JOKE OF THE RUN",
            f"  {line}",
            f"     {j['setup']}",
            f"     ... {j['punchline']}",
            f"  {line}",
            "",
        ]
    )


def main():
    j = fetch()
    if "--json" in sys.argv[1:]:
        print(json.dumps(j, indent=2))
    else:
        print(card(j))


if __name__ == "__main__":
    main()
