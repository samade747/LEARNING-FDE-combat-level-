# sdk_parser

Directory-scoped guidance for Claude Code — applies only to files under `lib/sdk_parser/`.

- Keep `formatter.py` free of network/API calls — it only formats already-parsed response dicts.
- Log through `logger.py`'s shared `logger`, not `print()`.
- Any new function here should be testable without a real `ANTHROPIC_API_KEY`.
