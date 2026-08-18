---
name: joke-loop
description: Fetch one fresh joke from a public API by running this skill's bundled script, never from memory or made up. Use it whenever the user asks for a joke, wants the "joke loop" to run, or runs a scheduled job that should tell a joke.
allowed-tools: Bash, Read
---

# Joke loop

The whole point of this loop is trust: the joke has to be **real**, fetched fresh
every time, never invented on the spot. A joke "from memory" is indistinguishable
from a joke made up right now — so this skill never tells one without running the
script first.

## Getting a joke

Run the script:

```bash
python3 .claude/skills/joke-loop/scripts/joke.py
```

It calls the public joke API and prints a setup/punchline card. The script owns
the API call and the retry logic, so none of that has to be remembered.

For the raw fields (to log, email, or compute with), ask for JSON:

```bash
python3 .claude/skills/joke-loop/scripts/joke.py --json
```

## When the fetch fails

The script exits non-zero and says so. Say the joke loop could not run this
time, in one line, and stop. Do not fill in a remembered or made-up joke and
present it as real — a fabricated joke told as genuine is the one thing this
loop must never do. The next scheduled run will try again.
