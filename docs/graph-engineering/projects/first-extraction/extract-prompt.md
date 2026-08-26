Read the document at {DOC_PATH}. Extract every entity and relation it mentions, and return ONLY JSON
matching this exact shape (no prose, no markdown fences):

{
  "entities": [{"name": "...", "type": "Organization|Person|Component|Incident|Contract", "description": "..."}],
  "relations": [{"subject": "...", "predicate": "...", "object": "..."}]
}

Rules:
- "name" must be the surface form exactly as it appears in the document (do not normalize or resolve
  names across documents — that is a later step).
- "description" must capture real context from the document (what makes this entity identifiable),
  not a one-word label.
- Every "subject" and "object" in relations must match a "name" you declared in "entities".
- Do not invent entities or relations not stated or clearly implied by the document.
