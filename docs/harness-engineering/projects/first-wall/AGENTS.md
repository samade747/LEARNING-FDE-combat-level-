# The First Wall

This project has one job: prove a deny list actually blocks what it lists —
secret reads, recursive deletes, force-pushes — at the tool layer, before the
agent's own judgment ever gets a vote.

Do not weaken `.claude/settings.json`'s `permissions.deny` list to make a
demo attempt "succeed" — the whole point is that these attempts fail.
