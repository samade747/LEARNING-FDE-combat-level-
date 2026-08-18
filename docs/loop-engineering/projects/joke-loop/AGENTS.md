# The Joke Loop

This project has one job: fetch one real joke, every time it runs.

**Any request for a joke is answered by running this project's script, never
from memory:**

    python3 .claude/skills/joke-loop/scripts/joke.py

(In Claude Code this runs automatically through the `joke-loop` skill; any
other agent should run the script directly.) The script owns the API call and
the retry logic.

The one thing to hold onto: a joke told as real has to **be** real. Making one
up and presenting it as fetched is the one thing this loop must never do — and
if the fetch fails, say so plainly instead.
