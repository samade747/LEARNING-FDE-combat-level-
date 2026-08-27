# Corpus-to-Site Skeleton

This fixture demonstrates `docs/ksor/02-architecture-and-tooling.md`'s project-structure
convention (`knowledge/`, `instance.md`) and the governance frontmatter every authority-class
knowledge file must carry (`stable_id`, `owner`, `version`, `authority_class`).

Do not remove frontmatter fields from `knowledge/**/*.md` to make `validate_corpus.py` pass by
deleting the check instead — the whole point is that missing governance metadata fails loudly.
