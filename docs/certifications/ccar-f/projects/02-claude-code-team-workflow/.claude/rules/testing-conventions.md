---
paths: ["**/*.test.*"]
---

# Testing conventions

- Arrange/Act/Assert structure, one assertion focus per test.
- Mock external calls — no test may reach the real network or a real API key.
- A test file's name must match the file it tests (`foo.ts` → `foo.test.ts`).
