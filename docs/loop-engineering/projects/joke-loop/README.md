# Joke Loop — Project 7, Easy Version

A simpler stand-in for the sky-watch version of Project 7 (Break It On
Purpose). Same two concepts — **cost** and **observability** — just with a
fun, one-API-call script instead of an asteroid feed, so there's less to hold
in your head while you focus on the actual lesson.

**No API key needed.** The script calls a free, public joke API.

## Windows gotcha

The 😂 emoji triggers a `UnicodeEncodeError` on Windows cmd/PowerShell (cp1252
codec). Set `PYTHONIOENCODING=utf-8` before running the script directly (not
needed when Claude Code runs it through the skill):

```bash
set PYTHONIOENCODING=utf-8   # cmd.exe
$env:PYTHONIOENCODING="utf-8"   # PowerShell
export PYTHONIOENCODING=utf-8   # bash
```

---

## Step 1 — Measure One Beat

A "beat" is one run of the loop. Time it:

```bash
cd docs/loop-engineering/projects/joke-loop
time python .claude/skills/joke-loop/scripts/joke.py
```

Now do the cost math (same logic as the sky-watch version, just easier
numbers to hold onto): if this ran as a real LLM-driven Routine once a day,
at a rough ~$0.20/beat, that's **~$6/month**. The same loop firing every 5
minutes is **~288 beats/day** → **~$1,700+/month**. Frequency is the cost
driver, not the work itself — a joke costs the same whether it runs once a
day or a thousand times.

### Done jab (self-check)
- [ ] Ek beat ka real time naapa
- [ ] Daily vs every-5-minutes cadence ka cost farq khud calculate kiya

---

## Step 2 — Sabotage It

Open a **separate throwaway terminal** (this session's own terminal can't
spawn nested `claude` processes) and give the loop a precondition it can
never satisfy:

```bash
cd docs/loop-engineering/projects/joke-loop
claude -p "run the joke loop, but first read a file called nonexistent-config.yaml and use its settings — do not proceed without it"
```

Run it 2-3 times. **Windows cmd.exe note:** cmd doesn't understand bash's
`for i in 1 2 3; do ... done` loop syntax. Just run the line above 2-3 times
by hand, or use PowerShell:

```powershell
1..3 | ForEach-Object {
  claude -p "run the joke loop, but first read a file called nonexistent-config.yaml and use its settings — do not proceed without it" | Out-File -Append run.log
}
```

### Done jab (self-check)
- [ ] Loop ne khud confirm kiya file exist nahi karti (search kiya, guess nahi kiya)
- [ ] Loop ne fake settings invent nahi kiye

---

## Step 3 — Diagnose From the Log Only

Don't re-read the full conversation. Just look at what the agent's final
answer said (or what you logged to `run.log`) and answer:

- Did it say clearly it couldn't proceed, and why?
- Did it ask a human instead of guessing or going silent?
- Would you have known something was wrong just from the log, without
  watching the run live?

### Done jab (self-check)
- [ ] Sirf log/final-answer se pata chal gaya kya fail hua, transcript replay kiye bina
- [ ] Loop ne clear "needs a human" note chora — khamoshi se fail nahi hui

---

## Why This Version Is Easier

- **No astronomy/API-shape to learn** — a joke is a joke, setup + punchline,
  nothing to interpret.
- **One HTTP call, no date math, no NASA rate limits** — the script is ~60
  lines vs skywatch.py's ~225.
- **Same two lessons survive intact:** frequency drives cost, and a
  trustworthy loop fails loudly, never silently and never with a fabrication
  (a made-up joke told as real is exactly as dishonest as a fake "all clear").

Full Project 7 instructions (bash-loop version, matches the book's steps
exactly): [`../CODIFY-AND-SABOTAGE.md`](../CODIFY-AND-SABOTAGE.md).
