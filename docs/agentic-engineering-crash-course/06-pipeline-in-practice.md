# 06 — Pipeline in Practice: Gamification Worked Example

Poora workflow end-to-end chalaya jata hai ek worked example par: course platform mein
**gamification service** add karna. Same example Python aur TypeScript dono mein banta hai; har step
Claude Code aur OpenCode dono mein chalta hai. **Point example nahi hai — shape hai.** Shape ek baar
internalize karo, language/harness sirf details reh jati hain.

## 6.1 Stage 1: Idea Ko Grill Karna

Stakeholder ka Slack message: *"Retention numbers acche nahi. Students sign up karte hain, kuch
lessons karte hain, phir drop off. Kuch gamification add karna chahta hoon: points, streaks, levels."*

Yeh spec nahi hai — **ek wish hai.** Agent ko "bana do" kehna kuch aisa degi jo stakeholder ke zehan
se match nahi karega, kyunke abhi tumhe khud nahi pata unke zehan mein kya tha. `grill-me` invoke
karo (client-brief.md parho, gamification par grill karo). Agent brief parhta hai, codebase explore
karta hai (existing `Lesson`, `Quiz`, `Enrollment` models), aur ek-ek sawal poochta hai apni
recommendation ke sath:

```
Q1. Points kis se milte hain? Recommendation: lesson completion + quiz pass.
Q2. Existing lesson_progress records ke liye retroactive? Recommendation: ek-baar backfill.
Q3. Streak granularity? Recommendation: daily, 1-day grace period.
Q4. Level thresholds: linear, quadratic, ya hand-tuned? Recommendation: quadratic, cap level 50.
```

Session 15-100 sawalon tak chal sakti hai. Khatam hoti hai jab agent report kare koi decision open
nahi raha — ab tumhare paas stable **design concept** hai. **Koi code, koi PRD nahi.** Grilling ka
output ek chat history hai; chat history hi explicit design concept hai.

## 6.2 Stage 2: Conversation Se PRD Tak

Design concept stabilize hone par, `to-prd` invoke karo — Skill dobara interview nahi karti, jo
tumne already bola usay **synthesize** karti hai:

```markdown
# PRD: Course Platform Gamification

## Problem Statement
Students drop off after a handful of lessons...

## Solution
Add a points/streaks/levels gamification layer...

## User Stories
1. As a student, I earn 10 points when I complete a lesson.
2. As a student, I earn 25 points when I pass a quiz.
3. As a student, I see my current streak on the dashboard.
... (12-20 more, each independently verifiable)

## Modules Touched
- NEW: gamification_service (deep module, owns points + streaks + levels)
- MODIFIED: lesson_progress_service (emits events on completion)
- NEW DB: point_events table, streak_state table

## Implementation Decisions
- Level formula: floor(sqrt(total_points / 50))
- Streak grace: 1 missed day allowed

## Out of Scope
- Leaderboards (separate PRD)
- Push notifications (separate PRD)
```

> **PRD approve karne se pehle kya parho:** **Drift ke liye skim karo, proofread mat karo.** Tum
> aur agent already grilling session se design concept share karte ho. 4 jagah dhyan do jahan
> summarization drift kar sakti hai: **user stories** (koi drop/invent hua?), **modules touched**
> (boundary wahi hai jo discuss hua?), **implementation decisions** (grilling ke calls match karte
> hain?), **out of scope** (boundary creep hua?). 2 minute focused skimming almost sab failures
> catch karti hai; poora document line-by-line parhna wahi failures catch karta hai 10x attention
> cost karke.

## 6.3 Stage 3: PRD Se Vertical-Slice Issues Tak

PRD destination describe karti hai. `to-issues` journey describe karti hai — kaise PRD ko
independently-grabbable, vertically-sliced issues mein todna hai, blocking relationships ke sath:

```
Issue #1 — Award points for lesson completion (E2E) — blocked by: nothing — Type: AFK
Issue #2 — Award points for quiz pass (E2E) — blocked by: #1 — Type: AFK
Issue #3 — Streak counter (E2E) — blocked by: #1 — Type: AFK
Issue #4 — Level threshold + UI badge — blocked by: #2 — Type: AFK
Issue #5 — Retroactive backfill — blocked by: #1 — Type: human-in-the-loop
```

**3 non-accidental properties:** (1) **Issue #1 khud working slice ship karti hai** — sirf #1 merge
ho ke ruk jayein to bhi platform ke paas functioning gamification feature hai (horizontal slicing
mein "phase 1" sirf ek empty database table deti). (2) **DAG parallelism allow karta hai** — #2 aur
#3 parallel sessions mein chal sakte hain #1 merge hone ke baad. (3) **#5 human-in-the-loop flagged
hai**, AFK nahi — backfills historical data touch karte hain, insaan har step dekhta hai.

## 6.4 Stage 4: Implementation — Ek Slice Par TDD

Queue ke unblocked top se pick karo: Issue #1. `tdd` invoke karo — strict red-green-refactor enforce
karti hai: **ek** failing test likho, fail hote dekho, **bas kaafi** code likho pass karne ke liye,
pass hote dekho, refactor karo (sab tests green), repeat.

**TDD kyun specifically?** (1) **Chhote steps force karti hai** — bina TDD, agent 6 files code
likhega aur baad mein test layer wrap karega — wo tests **cheat** karte hain (implementation test
karte hain, behavior nahi). TDD mein test pehle likha jata hai, implementation exist karne se pehle,
isliye shape nahi ho sakta jo agent ne likha usay fit karne ke liye. (2) **Har minute feedback** —
har test-pass ek checkpoint hai.

```python
# gamification/service.py — deep module ka interface (sirf 2 public methods)
class GamificationService:
    LESSON_COMPLETION_POINTS = 10
    def __init__(self, store, clock=datetime.utcnow):
        self._store = store
        self._clock = clock

    def award_lesson_completion(self, student_id: str) -> PointAward:
        award = PointAward(student_id, self.LESSON_COMPLETION_POINTS,
                            "lesson_completion", self._clock())
        self._store.append(award)
        return award

    def total_points(self, student_id: str) -> int:
        return self._store.total_for_student(student_id)
```

```python
# gamification/test_service.py — PEHLE likha gaya
def test_lesson_completion_awards_ten_points():
    store = InMemoryStore()
    svc = GamificationService(store, clock=lambda: datetime(2026, 5, 10))
    award = svc.award_lesson_completion("student-42")
    assert award.points == 10
    assert svc.total_points("student-42") == 10
```

> **Yahan kya matter karta hai:** (1) Service ka **chhota public interface** hai — sirf 2 methods.
> Baaqi sab class ke andar chhupa hai. (2) Test **sirf unhi 2 methods** ko call karta hai — internal
> helpers ko nahi poke karta, **behavior** check karta hai ("3 completions ke baad total 30 hai"),
> yeh kaise compute hota hai nahi. Yehi shape (chhota interface, wide implementation, boundary-par-
> tests) [§7](07-architecture-principles.md) **deep module** kehti hai. Python aur TypeScript
> versions line-for-line equivalent hain.

## 6.5 Stage 5: AFK Loop — Backlog Drain Karna

**6.5.1 — Sequential loop (bash):** ek chhota script jo while-loop mein chalta hai: open issues +
recent commits ek prompt mein feed karta hai, agent ko AFK run karta hai, jab tak agent **exact**
`NO_MORE_TASKS` sentinel na bole. Prompt agent ko batata hai: unblocked highest-priority AFK issue
pick karo, PRD parho, `tdd` skill se slice implement karo, feedback loops chalao (typecheck/tests/
lint), tabhi commit karo jab sab pass ho, issue reference kar ke commit+close karo. Claude Code aur
OpenCode mein sirf binary aur permission-flag badalta hai — baaqi script byte-identical hai.

**6.5.2 — Parallel orchestrator (TypeScript):** ek baar loop trust ho jaye, agla leverage point
**parallel execution** hai — sab unblocked issues pick karo, har ek ke liye ek sandboxed worktree
spin karo, concurrently chalao, merge karo. **3 ideas jo matter karti hain:**
1. **Parallel, sequential nahi** — teen slices same waqt, apni-apni isolated workspace mein. Subah 3
   PRs, 1 ki jagah.
2. **Har parallel run sandboxed hai** — `git worktree` + container jo laptop ko damage nahi kar
   sakta. Ghalti ho to blast radius ek worktree tak limited.
3. **Reviewer alag agent hai, fresh session mein** — different (cheaper) model, sirf diff + coding
   standards dekhta hai. Same chat mein review karna dumb-zone mein review karna hai.

**6.5.3 — Persistent Loops aur Ambient Agents:** upar wale loops backlog ek-baar drain karte hain.
Agla evolution: **hamesha chalte rehna.** Ek **loop** (Boris Cherny ke sense mein) `cron` se
scheduled agent invocation hai (har minute/5-minute/30-minute) ek chhoti standing job ke against.
Har invocation fresh session hai — hamesha smart zone mein shuru hota hai, dumb-zone drift kabhi
accumulate nahi hoti. **Agent zinda nahi rehta, job zinda rehti hai.**

Example loops: **PR janitor** (flaky CI rerun, rebase, typo-fix), **CI healer** (flaky test investigate
+fix), **feedback clusterer** (user feedback group kare, Slack summary poste kare). Yeh **ambient
agents** hain — background tax handle karte hain jo historically engineering hours khati thi.

**2 design rules:** (1) **Har tick fresh session hai** — koi state ticks ke beech survive nahi karti
except jo environment mein likhi gayi ho. (2) **Har loop ka ek hi job hai** — PR-janitor + CI-healing
+ feedback-clustering ek loop mein degrade ho kar koi bhi achhi tarah nahi karegi.

## 6.6 Stage 6: Human Review Aur QA

Loop chalne ke baad subah N pull requests hote hain. **Diffs parho, agent ka summary nahi.** Summary
agent ka lafz hai jo usne kiya; diff wo hai jo **asal mein** hua.

**Concrete example:** agent ka PR summary bola "points added, tests pass, dashboard shows total."
Diff same bola, except QA ne pakda ke dashboard kholne se pehle koi lesson complete na ho to crash
hota hai (`TypeError: ... 'awarded_at' of null`). Service mein empty-state handle hua tha, lekin
React widget ne `last_award_at` timestamp assume kiya. Agent ke tests empty-state UI render cover
nahi karte the. Yeh observation **backlog mein naya issue** ban kar wapis jati hai (type AFK).
**Yehi loop — insaan gap dhoondta hai, ticket queue mein wapis jata hai, agent AFK fix karta hai —
pipeline ko self-improving banata hai.**

QA pipeline ka **sab se valuable artifact** produce karti hai: **naye issues.** Yahan **taste**
rehta hai bhi — QA automate karna temptation hai jo resist karna chahiye: ek agent doosre agent ki
UI review kare to ek opinion milti hai jo kisi ki nahi hai, aur result gently-derivative "slop" hota
hai. Ek insaan ka "yeh padding ghalat hai" decision **irreducible step** hai. Agent 5x pace par
ship karta hai; tumhara kaam yeh ensure karna hai ke wo **tumhari** taste 5x pace par ship kare, kisi
aur ki nahi.

---
[⬅ Skills as Encoded Process](05-skills-as-encoded-process.md) · [Agla: Architecture Principles ➡](07-architecture-principles.md)
