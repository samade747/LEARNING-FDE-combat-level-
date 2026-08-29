# Project 12 — Build a Dreaming Loop (Capstone 2)

*Loop Engineering, [`09-routine-drills-and-dreaming.md`](../../09-routine-drills-and-dreaming.md) §12.
Concept 12 (spine + dreaming), 11 (maker-checker), 6 (schedule), Part 5 (human gate).*

> 🧩 **Sabse aasan zaban mein:** jaise raat ko so kar dimaag din bhar ki baatein "process" karta hai
> aur kal ka behtar plan banata hai — loop khud apne purane runs dekh kar khud ko behtar banati hai.
> Lekin woh apne aap apne rules nahi badalti: woh ek **PR draft** karti hai (evidence ke sath), aur
> insaan decide karta hai.

## Kya banaya

Ek **base loop** (`daily-triage`-jaisa) hafton se chal raha hai aur `progress.md` mein dated entries
chhod raha hai. Uske **upar** ek **dreaming loop** — weekly cloud routine — jo:

1. `dreaming-state.md` ki `last_reviewed_date` ke baad wali `progress.md` entries parhta hai
2. koi bhi failure/correction pattern dhoondta hai jo **ek se zyada baar** aaya ho
3. usay rokne wala **sabse chota `CLAUDE.md` change** ek **PR** ki tarah draft karta hai
   (`claude/dreaming-<date>` branch — kabhi direct commit nahi)
4. PR description mein **evidence**: kaunse runs, kitni baar, yeh line kyun rokegi
5. ek **deletion** bhi propose karta hai: koi rule jo recent runs ko chahiye nahi tha
6. aakhir mein `dreaming-state.md` ko aaj ki date se update karta hai

### Setup (throwaway repo)

`samade747/my-doorbell` → `dreaming-demo/` folder (Project 6 ka throwaway repo reuse kiya —
GitHub OAuth already set up). Seed files ki copies yahan:

| File | Kya |
| --- | --- |
| [`seed/progress.md`](seed/progress.md) | Base-loop memory — 2 planted repeated failures |
| [`seed/dreaming-state.md`](seed/dreaming-state.md) | `last_reviewed_date: 2026-08-01` |
| [`seed/CLAUDE.md`](seed/CLAUDE.md) | Base-loop rules — ek CHANGELOG rule jo kisi run ne kabhi use nahi kiya (deletion candidate) |

### Planted evidence

| Pattern | Entries | Count | CLAUDE.md mein? |
| --- | --- | --- | --- |
| **A — lint (`ruff`) skipped before commit**, reviewer ne bounce kiya | 2026-08-10, 2026-08-16, 2026-08-23 | **3x** | koi rule nahi → ADD karo |
| **B — reviewer subagent ko galat branch di gayi**, stale PASS | 2026-08-13, 2026-08-21 | **2x** | rule 2 exist karta hai par kamzor → TIGHTEN karo |
| Deletion candidate: "Always update `CHANGELOG.md` before committing" | (kabhi kisi entry mein nahi) | 0x | DELETE propose karo |

## The routine

| | |
| --- | --- |
| Name | `Dreaming Loop — my-doorbell (Loop Eng P12)` |
| ID | `trig_01BwicMH3whg74osL1QUEVqm` |
| Schedule | `0 0 * * 0` — har Sunday 00:00 UTC (weekly) |
| Repo | `github.com/samade747/my-doorbell` |
| Model | claude-sonnet-5 |
| Tools | Bash, Read, Write, Edit, Glob, Grep |
| Link | https://claude.ai/code/routines/trig_01BwicMH3whg74osL1QUEVqm |

Full prompt: [`routine-prompt.md`](routine-prompt.md).

## Run notes

Dekho [`RUN-LOG.md`](RUN-LOG.md).

## Done jab (self-check) — ✅ Complete (2026-08-30)

- [x] PR ka proposed change real hai, cited log entries tak trace hota hai (guess nahi)
- [x] Jaan-boojh kar planted repeated failure pakri gayi (A 3x, B 2x) + proposal ban gayi
- [x] Koi change `CLAUDE.md` (master) mein bina merge kiye nahi hua (sirf PR branch)
- [x] `dreaming-state.md` aaj ki date se update hui
- [x] Evidence-less improvement nahi (har claim ek dated entry tak trace)

**Result:** routine run `cse_01AEEzB36DSJKSx9zpAFV82C` (`success`, 62s) ne dono planted patterns
evidence ke sath pakre aur PR draft ki. Uska apna `git push` 403 se blocked tha (Claude GitHub App
account pe installed nahi — Project 9 wala hi blocker), fallback per poori PR description print ki.
User ke `gh` PAT se wahi change **real PR** ki tarah khola gaya:
**https://github.com/samade747/my-doorbell/pull/2** (merge nahi kiya — human gate). Full detail:
[`RUN-LOG.md`](RUN-LOG.md).
