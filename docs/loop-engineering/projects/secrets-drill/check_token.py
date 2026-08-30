"""Loop Engineering Project 10 (Secrets Drill) — where does a secret live?

Tries two places for MY_API_TOKEN, in order:
  1. a .env file at the repo root   <- the WRONG way: .env is gitignored, so a fresh
                                        cloud clone of this repo never contains it
  2. the process environment        <- the RIGHT way: set it in the routine's
                                        Environment -> Variables panel

Run 1 of the drill: no .env in the clone, no env var  -> this script exits 1 (FAIL)
Run 2 of the drill: MY_API_TOKEN set as a routine variable -> exits 0 (OK)
"""
import os
import pathlib
import sys

repo_root = pathlib.Path(__file__).resolve().parent.parent
env_file = repo_root / ".env"

token = None
source = None

if env_file.exists():
    for line in env_file.read_text().splitlines():
        if line.strip().startswith("MY_API_TOKEN="):
            token = line.split("=", 1)[1].strip()
            source = ".env file"
            break

if token is None and os.environ.get("MY_API_TOKEN"):
    token = os.environ["MY_API_TOKEN"]
    source = "environment variable"

if token is None:
    print("FAIL: MY_API_TOKEN not found — no .env in this clone, not in the environment either.")
    print("      A gitignored .env never reaches a fresh cloud checkout. Put the secret in the")
    print("      routine's Environment -> Variables panel instead.")
    sys.exit(1)

print(f"OK: MY_API_TOKEN resolved via {source}. Starts with 'dummy'? {token.startswith('dummy')}")
sys.exit(0)
