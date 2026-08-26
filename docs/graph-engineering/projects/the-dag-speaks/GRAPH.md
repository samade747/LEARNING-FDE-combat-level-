# GRAPH.md — Answering AgentHub's 3 Questions With Plain Git

AgentHub is private now, but its `children`/`leaves`/`lineage` questions are just Git traversal.
Verified against `demo-repo/` (built by `setup.sh`) below.

## 1. `ah children` — what was tried on top of a given commit?

```bash
git log --all --oneline --children | grep <short-hash>
```

On the demo repo, children of the baseline commit `e01b3ab`:

```
e01b3ab b92ebff baseline: val_bpb=1.000
```

One child: `b92ebff` (the `lr=0.01` experiment). If two experiments had branched off the same commit,
both hashes would appear here — that is the traversal AgentHub's `children` command does.

## 2. `ah leaves` — where is the unexplored frontier?

```bash
git branch --no-merged main    # or: master, on this repo
```

On the demo repo:

```
exp-batch-64
exp-dropout-0.2
```

Both experiment branches exist but were never merged — they are frontier: real attempts, real
evidence (one crashed, one made the metric worse), but not part of the retained lineage. This is
exactly Concept 4's gap: `results.tsv` remembers these attempts happened, but only a graph query (or
here, plain Git) lets a future agent actually find them instead of re-running the same crash.

## 3. `ah lineage` — what path produced the current state?

```bash
git log --oneline main    # or: master
```

On the demo repo:

```
b92ebff try lr=0.01: val_bpb=0.940 (improved, keep)
e01b3ab baseline: val_bpb=1.000
```

Two commits: the baseline, then the one improvement that was kept. Note `exp-dropout-0.2` is NOT in
this lineage even though it exists in the repo — it made the metric worse (0.980 vs 0.940) and was
correctly never merged.

## What the DAG Cannot Tell You

Nothing in this repo's history explains **why** `dropout=0.2` was discarded — that reasoning (val_bpb
went from 0.940 to 0.980, worse) lived in whoever ran the experiment's head, or in a `results.tsv` row
if `autoresearch`'s convention were followed here. The commit DAG proves the experiment happened and
was not kept. It does not carry the evaluation that explains the decision — that is Concept 3's
"work vs facts" split: this file is pure commit-DAG (work), a `claims.json` (Part 6) would be needed to
carry the fact `dropout_0.2 -> made_worse -> 0.980`.
