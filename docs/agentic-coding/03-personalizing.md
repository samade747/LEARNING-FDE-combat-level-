# 03 — Personalizing: Skills, Hooks, Subagents

3 alag problems, 3 alag solutions:

| Type | Kya Karta Hai | Kab Use Karo |
| --- | --- | --- |
| **Command/Skill** | Saved reusable prompt, `/name` se ya khud auto-invoke | Same instructions baar baar type kar rahe ho |
| **Hook/Plugin** | Rule jo **hamesha khud chalti hai** | Kuch hamesha true hona chahiye |
| **Subagent** | Alag AI helper, apni window mein kaam kare | Bara search/research jo main conversation clutter kare |

## Concept 9: Commands Aur Skills

Ek **saved, reusable instruction** jo file mein rehti hai — dobara type nahi karni parti. Farq sirf ye
hai ke isay **kaun invoke karta hai**: aap (`/name`), ya model khud (jab task uski `description` se
match kare).

**"Agar model ko pehle se pata hai, skill kyun likhein?"**
- **Model ko aapki specifics nahi pata** — team ka commit format, internal tool ke flags
- **Janna aur bar-bar wahi tareeqe se karna alag baat hai** — skill exact steps pin karta hai
- **Model khud sahi approach tak nahi pohanchega** — skill ki `description` hi trigger hai

**Claude Code** — `.claude/skills/review/SKILL.md` → `/review` command banta hai:
```markdown
---
name: extract-transcript
description: Extract a clean transcript from a YouTube video URL. Use when...
---
1. URL lo
2. `yt-dlp` chalao
3. `transcripts/{video-id}.txt` mein save karo
For style, see `references/style.md`.
```

**OpenCode** commands aur skills **alag** rakhta hai: skill (`SKILL.md`, khud auto-invoke) aur command
(`/name`, aap invoke karte ho) — dono `.opencode/commands/` aur `.opencode/skills/` mein.

> **Ehtiyat:** Skill ke andar `@` auto-import syntax use mat karo (rules file wala) — plain relative
> path use karo, taake lazy loading kaam kare.

**Skill deterministic nahi banata** — LLMs probabilistic hain. Skill sirf **range narrow karta hai**:
"har dafa alag procedure" se "same procedure, alag phrasing" tak. Jab **guaranteed** result chahiye,
model ki memory pe trust mat karo — script/hook use karo (deterministic).

**Rules:**
- **Description sab se zaroori line hai** — vague description zyada activate hoga
- **`SKILL.md` chhota rakho** — extra detail alag files mein
- **Chhoti skills banao, bari nahi** — research/draft/format/review ke liye ek nahi, 4 skills
- **Over-constrain mat karo** — pin karo jo identical hona chahiye, baaki model pe chhoro
- **Examples ab narrow kar sakti hain** (naye models ke liye) — teen examples "boundary" ki tarah parhe
  jate hain. Behtar: field ke legal values likho (`pending`, `in_progress`, `completed`)

## Concept 10: Hooks (Claude Code) / Plugins (OpenCode)

Skills model ke choose karne pe depend karte hain. **Hook/Plugin** rule hai jo **hamesha khud chalti
hai**, model ki marzi se farq nahi.

**Claude Code — `.claude/settings.json`:**
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{ "type": "command",
        "command": "jq -r '.tool_input.command' | grep -q 'rm -rf' && { echo 'Blocked' >&2; exit 2; } || exit 0" }]
    }]
  }
}
```
Exit code `2` = block. Koi bhi aur exit = allow.

**OpenCode — `.opencode/plugins/block-dangerous.js`:**
```javascript
export const BlockDangerousPlugin = async () => ({
  "tool.execute.before": async (input, output) => {
    if (input.tool === "bash" && output.args.command?.includes("rm -rf")) {
      throw new Error("Blocked dangerous command");
    }
  },
});
```

**Achi aadat:** Har edit pe hook mat lagao — **commit time** pe check karo. Kaam khatam hone do, phir
`git commit` pe tests/formatter chalao. Fail ho to commit block, error AI ko wapas, AI khud fix kare.

### Verification Loop — Is Poori Book Ka Sab Se Zaroori Pattern

**Attempt → Check → Fix → Repeat.** Model kaam karta hai. Independent check grade karta hai. Failure
message agli instruction ban jati hai. Model fix kar ke dobara try karta hai. **Beech mein koi insaan
nahi.**

> Boris Cherny (Claude Code creator) isay sab se zaroori tip kehte hain: AI ko apna output verify karne
> ka tareeqa do, ye result 2-3x behtar ho jayega. *"Kisi ko website banwao lekin browser kabhi mat
> kholne do"* — result acha nahi hoga.

> **Robert C. Martin (Clean Code ka author)** ne July 2026 mein kaha wo ab apne agents ka code parhta hi
> nahi — sirf **extreme constraints** (tests, coverage thresholds, mutation testing) rakhta hai. **Order
> zaroori hai:** usne pehle checks banaye, phir parhna chhora — ulta nahi. *"Rule ek ratio hai, permission
> slip nahi."*

**Aadat:** Jab bhi task do, **check karne ka tareeqa bhi do.** Test jo pass hona chahiye. Command jo
succeed ho. File jo exist kare.

## Concept 11: Subagents

300-file project mein "billing kahan hai?" poocho, AI dazan files khol dega — sab **aapki conversation
mein**. **Subagent** apni **isolated context window** wala agent hai — kaam private mein karta hai,
sirf **summary** wapas deta hai.

**Built-in subagents** (already milte hain): Claude Code — `Explore`, `Plan`, general-purpose. OpenCode
— `Explore`, `General`, `Scout`.

**Custom subagent — `.claude/agents/doc-fetcher.md`:**
```markdown
---
name: doc-fetcher
description: Fetches and summarizes external library documentation...
tools: WebFetch, Read, Write
---
You are a documentation researcher. Fetch docs, extract API surface,
write summary to tmp/docs-{library}.md. Don't paste full pages.
```

**2 tareeqe use hone ke:** **Automatically** (description match kare) ya **manually** (`@subagent-name`
type karo).

### Skill Ya Subagent? Farq

| | Skill | Subagent |
| --- | --- | --- |
| Chalta hai | Aapki current window mein | Apni isolated window mein |
| Kya wapas ata hai | Poori output inline | Sirf summary |
| Best for | Consistent approach, in-line | High-volume work isolate karna |

> **Ek line mein:** Skill aapke **current** agent ko badalta hai. Subagent kaam **alag** agent ko de
> deta hai jo wapas report karta hai. **Aur ye compose hote hain: subagent skills use kar sakta hai.**

## Placement Question — Parts 2-4 Ek Table Mein

Har sentence ke liye ek sawal: **kaunsi surface pe rakhein?**

| Knowledge | Chahiye | Rehti Hai | Rakho |
| --- | --- | --- | --- |
| Hamesha sach ("published/ mat chhuo") | har turn | hamesha | **Rules file** |
| Ek task ka procedure | jab task chale | hamesha | **Skill** |
| Ek tool ka use kaise ho | jab wo use ho | hamesha | **Uski apni description** |
| Is task ka goal/details | abhi | is task ke liye | **Prompt** |
| Bara/raw data (logs) | kabhi kabhi | varies | **File on disk** |
| "Done" ki definition (command se prove) | har attempt | task tak | **Executable reference** |
| Sirf chhota jawab chahiye (60 files search) | ek dafa | kabhi nahi | **Subagent** |
| Jo AI dekh kar khud jaan le | kabhi nahi | kabhi nahi | **Kahin nahi — delete karo** |

> **2 zaroori nateeje:** Prompt sirf task ke liye hai — jo bhi cheez aap 3rd baar re-explain karo, wo
> kisi aur surface pe jani chahiye. Aur **"hamesha" surfaces sab se zyada editing maangti hain** — inki
> cost hamesha ke liye repeat hoti hai.

---
[⬅ Rules File](02-rules-file.md) · [Agla: Connecting to the World ➡](04-connecting-world.md)
