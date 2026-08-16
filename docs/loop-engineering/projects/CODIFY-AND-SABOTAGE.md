# Project 5 (Codify the Body) + Project 7 (Break It On Purpose)

> **In dono ka koi official starter kit nahi hai** — dono existing projects (4 aur 3) ke **upar**
> exercises hain, isliye inhe naya code nahi, sirf instructions chahiye.

---

## Project 5 — Codify the Body

**Concept:** Dynamic workflows interlude, 8 (worktree), 11 (maker-checker) · **Time:** 1-1.5 hrs

**Kya karna hai:** [`fix-loop-demo/`](fix-loop-demo/README.md) (Project 4) ko hath se ek baar chala
chuke ho. Ab usi cycle ko **ek re-runnable unit** bana do.

### Claude Code

`fix-loop-demo/` (apni throwaway copy) mein `claude` chalao, plain lafzon mein maango:

```text
use a workflow to draft a fix for the discount bug in an isolated worktree,
and have the reviewer subagent grade it
```

`ultracode` keyword se yeh trigger hoti hai. Jab result sahi lage, `/workflows` view mein `s` dabao
usay `/command` ki tarah save karne ke liye.

### OpenCode

Isi cycle ko shell script mein likho — capped `for` loop (Concept 5) + `&`/`wait` fan-out
(Concept 8):

```bash
for i in $(seq 1 3); do
  (
    git worktree add "../attempt-$i" -b "claude/fix-attempt-$i"
    cd "../attempt-$i"
    opencode run "Fix the failing tests in test_discount.py"
    opencode run "Grade the diff using @reviewer, reply PASS or FAIL"
  ) &
done
wait
```

### Done Jab

1. **Ek command/script poori draft-and-review body chalaye** — kai candidates, isolated checkouts,
   har ek ka apna verdict, bina aapke step-by-step prompt kiye
2. **Prove karo workflow loop NAHI hai:** fresh session/shell kholo isi folder mein, poocho *"what did
   the last workflow run do?"* — confirm karo usay kuch yaad nahi. Phir bata sako: isay loop banane ke
   liye kya chahiye — ek **heartbeat** (Routine/cron/`/loop`) jo isay fire kare, aur ek **progress
   file** jo agents likhein taake agli firing kuch yaad rakhe

**Yaad rakho (book ki apni warning):** *"Workflow = engine. Trigger = key jo engine start karta hai.
`progress.md` = agli trip tak information carry karta hai."* Workflow khud loop nahi hai.

---

## Project 7 — Break It On Purpose

**Concept:** Observability, 13 (cost), 14 · **Time:** 45-60 min

**Kya karna hai:** [`sky-watch/`](sky-watch/README.md) (Project 3) lo — isay maine khud test kiya hai,
kaam karti hai. Ab isay **jaan-boojh kar todo** aur sirf spine se diagnose karo.

### Step 1 — Ek Beat Measure Karo

```bash
cd sky-watch
time python .claude/skills/sky-watch/scripts/skywatch.py
```

Rough token estimate (Loop-Engineering-Summary.md ke real numbers use karke): agar yeh Routine
weekday-9am chale (5 runs/week), Sonnet pricing ke hisab se ~$0.20/beat maan kar, ~$4/month. Wahi loop
har 5 minute chale to ~$1,000+/month.

### Step 2 — Sabotage Karo

`sky-watch` ki copy mein `.claude/skills/sky-watch/scripts/skywatch.py` ko point karo ek file par jo
exist nahi karti, ya prompt mein aisi condition do jo kabhi poori na ho:

```text
run the sky-watch skill, but first read a file called nonexistent-config.yaml
and use its settings — do not proceed without it
```

Ek limit set karke chalne do:
```bash
for i in $(seq 1 3); do
  claude -p "run the sky-watch skill, but first read nonexistent-config.yaml"
done
```

### Step 3 — Sirf Spine Se Diagnose Karo

Poore transcript ko dobara mat parho. Sirf `progress.md`/log se pata lagao:
- Kya fail hua?
- Kab fail hua?
- Loop ne "needs a human" note chora ya chup ho gayi?

### Done Jab

1. Aap spine/log se hi bata sako kya fail hua aur kab (poora transcript replay kiye bina)
2. Loop ne clear "needs a human" note chora ho — khamoshi se fail nahi hui (agar khamoshi se fail hui,
   pehle woh fix karo — Concept 14 ka observability rule)
3. Aap apni loop ki monthly cost jaante ho current cadence par

**Lesson:** yeh Concept 13-14 ka poora point hai — loop **kaise fail hoti hai** utna hi zaroori hai
jitna **kaise chalti hai**.
