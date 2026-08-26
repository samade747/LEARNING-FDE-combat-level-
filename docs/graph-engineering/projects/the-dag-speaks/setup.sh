#!/usr/bin/env bash
# Builds a tiny demo repo with a real commit DAG: one kept lineage (merged to main)
# and two abandoned experiment branches (never merged) — a miniature autoresearch history.
set -euo pipefail

DEMO_DIR="demo-repo"
rm -rf "$DEMO_DIR"
mkdir "$DEMO_DIR"
cd "$DEMO_DIR"

git init -q
git config user.email "demo@example.com"
git config user.name "Demo Loop"

echo "val_bpb=1.000" > metric.txt
git add metric.txt
git commit -q -m "baseline: val_bpb=1.000"

# Experiment 1: lr-0.01 — improves, gets merged (kept lineage)
git checkout -q -b exp-lr-0.01
echo "val_bpb=0.940" > metric.txt
git commit -q -am "try lr=0.01: val_bpb=0.940 (improved, keep)"
git checkout -q main 2>/dev/null || git checkout -q master
git merge -q exp-lr-0.01 -m "merge: lr=0.01 improved the metric"

# Experiment 2: batch-64 — branches off the new baseline, crashes (abandoned, never merged)
git checkout -q -b exp-batch-64
echo "val_bpb=CRASH_OOM" > metric.txt
git commit -q -am "try batch=64: crashed with OOM (discarded)"
git checkout -q main 2>/dev/null || git checkout -q master

# Experiment 3: dropout-0.2 — branches off the new baseline, makes it worse (abandoned, never merged)
git checkout -q -b exp-dropout-0.2
echo "val_bpb=0.980" > metric.txt
git commit -q -am "try dropout=0.2: val_bpb=0.980 (worse than 0.940, discarded)"
git checkout -q main 2>/dev/null || git checkout -q master

echo "Demo repo built at $(pwd)"
echo "Branches:"
git branch -a
