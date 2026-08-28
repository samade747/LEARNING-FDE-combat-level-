# Claude Certified Architect Foundations (CCA-F)

Personal practice scaffold — sdk_parser build karne ki practice, Claude Code project conventions
(nested `CLAUDE.md`, `.claude/`) ke sath.

## Structure

```
.claude/              ← project-level Claude Code settings (khaali, abhi tak koi config nahi)
hello_world/           ← smoke-test script (hello.py)
__pycache__/           ← Python bytecode cache (auto-generated, tracked yahan sirf structure ke liye)
lib/sdk_parser/         ← core package: __init__.py, formatter.py, logger.py, CLAUDE.md (directory-scoped)
stop_reason/            ← plan.md — is hisse ka goal + approach
```

## Status

Skeleton stage — `lib/sdk_parser` ka `format_response_summary()` kaam karta hai (offline, koi API
call nahi), `stop_reason/plan.md` ka Goal likha hua hai, baaqi implementation abhi baaki hai.
