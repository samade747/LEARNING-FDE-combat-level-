---
paths: ["src/api/**/*"]
---

# API conventions

- Every handler validates its input with a schema before touching business logic.
- Return `4xx` for validation failures, `5xx` only for genuinely unexpected errors.
- Never log request bodies that may contain credentials.
