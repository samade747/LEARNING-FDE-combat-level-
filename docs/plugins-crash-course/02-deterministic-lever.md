# 02 — Part 3: The Deterministic Lever — Hooks (Concepts 7-8)

## Concept 7 — Hooks: Code Jo Har Baar Chalta Hai

**Hook** ek command hai jo host agent lifecycle ke ek fixed point par **khud-b-khud** chalata hai. Yeh
model ko suggestion nahi — yeh aapka code hai, host se execute hota hai, aisi schedule par jo model badal
nahi sakta.

**3 Cadences:**
- **Session mein ek dafa:** `SessionStart`, `SessionEnd`
- **Turn mein ek dafa:** `UserPromptSubmit`, `Stop`
- **Har tool call par:** `PreToolUse` (block kar sakta hai), `PostToolUse`

Host script ko event ka JSON stdin par deta hai; script apna kaam karta hai, **exit code** se signal
deta hai:

- **Exit 0** — allow/done
- **Exit 2 on `PreToolUse`** — **tool call block.** `stderr` par jo print karo, model ko reason ki tarah
  milta hai
- Koi aur non-zero — non-blocking error, log hota hai, lekin action chalta rehta hai

**Yeh exit-2 rule hi guardrails ka poora khel hai**, aur sabse common galti hai (exit 1 **block nahi**
karta).

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Read|Edit|Write|Bash",
      "hooks": [{"type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/hooks/block-secrets.sh"}]
    }]
  }
}
```

## Concept 8 — Must-Always Ek Hook Hai, Instruction Nahi

**Course ki sabse important idea:** Skill ya `CLAUDE.md` mein likha kuch bhi **advisory** hai. Model
usually follow karta hai, lekin bhool sakta hai, context khatam ho sakta hai, ya lage conversation aage
badh gayi. Jo cheez **har baar** honi chahiye, uske liye advice kaafi nahi — hook chahiye.

**2 Patterns jo zyada tar value carry karte hain:**

**Format on write — `PostToolUse`:**
```bash
#!/usr/bin/env bash
path=$(jq -r '.tool_input.file_path // empty')
[[ -n "$path" ]] && npx --yes prettier --write "$path" 2>/dev/null
exit 0
```

**Block what must never happen — `PreToolUse`, exit 2:**
```bash
#!/usr/bin/env bash
input=$(cat)   # event ko EK BAAR parho
path=$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty')
cmd=$(printf '%s' "$input" | jq -r '.tool_input.command // empty')

if [[ "$path" == *.env* || "$path" == */secrets/* ]]; then
  echo "Blocked: $path is a secret file." >&2
  exit 2
fi
if [[ "$cmd" == *"rm -rf"* || "$cmd" == *"git push --force"* ]]; then
  echo "Blocked: refusing to run a destructive command." >&2
  exit 2
fi
exit 0
```

> **One-line gotcha:** stdin ek **stream** hai — pehli cheez jo parhe woh usay drain kar deti hai. Agar
> `jq` do dafa directly call karo, pehla call poora event consume kar leta hai, doosre ko kuch nahi
> milta — `cmd` silently empty ho jati hai aur guard `rm -rf` par kabhi fire nahi hoti. `input=$(cat)`
> se **ek dafa** capture karo.

> Skill jo *"kabhi `.env` mat parho"* kahe — hope hai. Yeh hook — **guarantee** hai.

**Prove karo:**
```bash
echo '{"tool_input":{"file_path":"/app/.env"}}' | ./hooks/block-secrets.sh; echo "exit: $?"   # 2
echo '{"tool_input":{"command":"rm -rf /"}}'    | ./hooks/block-secrets.sh; echo "exit: $?"   # 2
echo '{"tool_input":{"file_path":"/app/main.ts"}}' | ./hooks/block-secrets.sh; echo "exit: $?" # 0
```

✓ **Checkpoint:** Aap har edit par kuch hone dilwa sakte ho, aur har tool call par kuch rokwa sakte ho.
Yehi farq hai ek plugin jo **suggest** karta hai aur ek jo **enforce** karta hai.

> **4 Rules jab hook misbehave kare:**
> - **Fast rakho** — `PreToolUse` **har** matching call ko gate karta hai, slow logic agent ko stall
>   karta hai
> - **Fail safe, jaan-boojh kar** — formatter fail ho to exit 0 (edit rehne do); **guard** ulta hai — agar
>   decide na kar sake, block karna prefer karo
> - **Har baar bataao kyun block kiya** — bina message ke exit 2 model ko kuch nahi deta, woh wahi retry
>   karega
> - **Host ki tarah debug karo** — fake event pipe karo, exit code parho

---
[⬅ Capability Levers](01-capability-levers.md) · [⬆ Index](README.md) · [Agla: Ship It ➡](03-ship-it.md)
