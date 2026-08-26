# Graph Project 4 — The DAG Speaks

**Concept:** 4, 5 (two memories, AgentHub traversal) · **Time:** 30-45 min · **Difficulty:** Medium

AgentHub itself is private now — but its `children`/`leaves`/`lineage` questions are just Git
traversal. This project builds a tiny real repo with a kept lineage and two abandoned experiment
branches, and answers all 3 questions with plain `git`.

## Files

- `setup.sh` — builds `demo-repo/` (git-ignored, regenerate any time): a baseline commit, one improved
  experiment that got merged, and two experiments that branched off but were never merged (one crashed,
  one made the metric worse) — a miniature `autoresearch` history.
- `GRAPH.md` — the 3 commands, run against the demo repo, with real (verified) output

## Setup

```bash
cd docs/graph-engineering/projects/the-dag-speaks
bash setup.sh
```

This creates `demo-repo/` with 4 commits across 3 branches (`master`, `exp-batch-64`,
`exp-dropout-0.2`). Re-run any time to reset it — it's `.gitignore`d, not committed.

## Test It

```bash
cd demo-repo
git log --all --oneline --graph          # see the shape: 1 kept lineage, 2 abandoned leaves
git branch --no-merged master             # Q2: the unexplored frontier
git log --oneline master                  # Q3: the lineage that produced current state
```

Compare your output to `GRAPH.md` — it should match exactly (branch names/hashes will differ each
`setup.sh` run, but the shape — 1 merged, 2 unmerged — is stable).

## Apna Kaam Karo (Real Repo)

Repeat the 3 questions against a repo with real history — this repo itself, or any project you work
in:

1. Pick a commit that clearly branched into multiple follow-up attempts (or pick your own repo's
   oldest interesting commit).
2. Answer all 3 questions with the commands in `GRAPH.md`.
3. Write your own `MY-GRAPH.md` with the 3 commands + your repo's real output, so a future agent could
   ask the same questions.

## Done Jab (Self-Check)

- [ ] `setup.sh` ne demo repo banaya, `git log --all --oneline --graph` sahi shape dikhata hai (1 kept, 2 abandoned)
- [ ] Sab 3 commands kaam karte hain aur `GRAPH.md` ke output se match karte hain
- [ ] Aap bata sakte ho DAG **kya nahi bata sakti**: kyun `dropout=0.2` discard hua (evaluation reasoning
      commit history mein nahi hai — sirf ek `claims.json` mein hota, Part 6 pattern se)
- [ ] Real repo (apni) par bhi 3 sawal answer kiye, `MY-GRAPH.md` likha

---
[⬆ Practice Projects Index](../../08-practice-projects.md)
