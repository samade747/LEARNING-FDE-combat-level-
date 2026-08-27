# P8 — Agent Surface Scaffold

This project's one job: prove the knowledge boundary is enforced in application logic, not left to the
model to "remember." `cited_answer()` must return `status: abstain` for anything the corpus does not
cover — never a fabricated `answer` key.

Do not widen `_KEYWORD_MAP` with fuzzy/semantic matching that would make an out-of-corpus question
"accidentally" match a document — that defeats the test this scaffold exists to make.
