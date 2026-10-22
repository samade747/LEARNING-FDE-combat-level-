# Project 1 — Build Your First Real Skill

**Time:** ~30-45 min · **Tool:** Claude.ai (free tier enough)

Apne sabse zyada re-explain kiye jane wale task ko skill mein badlo jo khud tumhara tareeqa
jaanti ho.

## Step 1 — Skill Build Karo

```text
Use the skill-creator skill to build me a weekly study-notes skill.
Whenever I ask for "study notes" or "weekly notes", take my raw class
notes and format them as a heading per topic, a short bold key-terms
list, and exactly three review questions at the end. Ask me anything
you need, then build it.
```

(Apne task ke liye: same shape rakho, jo dobara type karte ho wo swap kar do.)

skill-creator kuch sawal pucheta, `SKILL.md` likhta, test-run karta. **Save skill** click karo.

## Step 2 — Description Check Karo

```text
When would you use the weekly-study-notes skill, and when would you NOT use it?
```

Wide/narrow ho to fix batao.

## Step 3 — Prove It Works

Bilkul **nayi chat** mein, skill ka naam liye bina:

```text
Make study notes from this:
[paste a week of your notes]
```

Skill khud fire ho kar tumhara exact format wapas deti hai.

## Done

- [ ] Skill khud fire hoti natural request se
- [ ] Format bina reminders ke sahi aata
- [ ] Unrelated request par hijack nahi karti
