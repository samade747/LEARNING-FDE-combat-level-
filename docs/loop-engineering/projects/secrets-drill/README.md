# Project 10 — The Secrets Drill

*Loop Engineering, [`09-routine-drills-and-dreaming.md`](../../09-routine-drills-and-dreaming.md) §10.
Appendix A4 (secrets), A2 (environment).*

> 🧩 **Sabse aasan zaban mein:** jaise ghar ki chaabi kisi ko dete waqt sirf woh darwaza kholti ho jo
> zaroori hai — aur woh chaabi aap register mein nahi likhte. Secret bhi aise: `.env` file jo git
> ignore karta hai woh cloud tak **kabhi nahi jaati**; secret ko routine ke **Environment → Variables**
> panel mein rakhna padta hai, jahan se woh run ke waqt inject hota hai.

## Setup (throwaway repo `samade747/my-doorbell`)

| File | Kya |
| --- | --- |
| `secrets-demo/check_token.py` | `MY_API_TOKEN` ko pehle root `.env` mein dhoondta hai, phir `os.environ` mein. Kuch na mile → exit 1 |
| repo-root `.gitignore` | `.env` — yani `.env` kabhi commit nahi hota |
| (local only) `.env` | `MY_API_TOKEN=dummy-abc123` — sirf aapki machine par, git isay ignore karta hai |

Seed: [`check_token.py`](check_token.py) ki copy yahan.

## Run 1 — secret `.env` mein (cloud mein FAIL) ✅ Done

Routine `Secrets Drill Run 1 — .env` (`trig_01ES54hQwfs1H3N54KctsQLh`), session
`cse_01CxujYh3GgfPX1w8Bq5jSGy` — `success`, 8s:

```
$ python secrets-demo/check_token.py
FAIL: MY_API_TOKEN not found — no .env in this clone, not in the environment either.
exit=1
$ ls -la .env        → No such file or directory
$ git ls-files | grep -c env   → 0
```

**Mechanical wajah:** `.env` gitignored hai → kabhi commit nahi hua → fresh ephemeral cloud checkout
mein woh file hai hi nahi, aur koi env var bhi set nahi. Script sahi FAIL deta hai.

Ek aur probe run (`trig_0138q61FibxDJNqb7TEcf1j2`, session `cse_01M2MJpvJbB3DAT85QfV8oFN`) ne
`os.environ` scan kiya — `MY_API_TOKEN`/`MY_DUMMY_TOKEN` dono **UNSET**. (Environment mein sirf
session ke apne infra creds the: `GITHUB_TOKEN`, `AWS_*`, `CLAUDE_CODE_*` — drill se unrelated.)

## Run 2 — secret Variables panel mein (PASS) — 1 browser step baaqi

**Blocker:** RemoteTrigger API `environment_variables` ko trigger config mein allow nahi karta
(*"not supported on triggers — trigger configs are persisted and replayed on every fire"* — secrets
ko trigger JSON mein persist nahi karna chahte). Yeh **jaan-boojh kar** hai — yehi drill ka point
bhi hai: secret trigger definition mein nahi, environment mein.

**Aap ko karna hai (claude.ai, ~2 min):**

1. [Routine kholo](https://claude.ai/code/routines/trig_01ES54hQwfs1H3N54KctsQLh) (ya ek naya
   banao same repo par)
2. **Environment → Variables** → add `MY_API_TOKEN` = `dummy-abc123`
3. Prompt: *"Run `python secrets-demo/check_token.py` and report stdout + exit code. Credentials are
   in environment variables; do not look for a .env file."*
4. **Run now** → ab output: `OK: MY_API_TOKEN resolved via environment variable. Starts with
   'dummy'? True`, exit 0

## Done jab (self-check)

- [x] Run 1 token `.env` mein → FAIL (cloud), mechanical wajah pata hai
- [x] Confirm kiya gitignored `.env` cloud clone tak nahi pahunchta (`git ls-files` → 0)
- [ ] Run 2 token Variables panel mein → PASS *(browser step upar)*

**Sabak:** gitignored files cloud runner ke liye invisible hain. Secrets environment/variables
config mein rehte hain — runtime par inject hote hain, kabhi commit nahi hote.
