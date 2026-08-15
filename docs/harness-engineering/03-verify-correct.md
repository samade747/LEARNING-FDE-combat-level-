# 03 — Verify & Correct: Check Karna Aur Theek Karna

Constraint forbidden cheez ko rokti hai. Information sahi cheez ko enable karti hai. Teesra aur chautha
verb us **beech** ki cheez sambhalte hain: kaam jo allowed tha, try hua, aur **ghalat nikla**. Verify
pakarta hai. Correct run ko recover karta hai, phir wahi ghalti dobara na ho — yaqeeni banata hai.

## Concept 8: Hooks — Khud-Chalne Wali Verification

Pichli course ka maker-checker split har beat ke **end** mein sirf ek dafa verify karta hai. **Hook**
**musalsal** verify karta hai — ye code hai jo harness **khud, fixed moments** pe chalati hai, chahe
model kuch bhi chahe. Har edit ke baad linter chalao. Har Bash command se pehle check karo. Session
khatam hone se pehle tests chalao, aur agar fail hon to **khatam hi na hone do**.

**Zaroori lafz: "refuse".** Ye hooks ko suggestion se harness part banata hai:

- **Action se pehle** wala hook (ya session khatam hone se pehle) action ko **poora rok** sakta hai
- **Action ke baad** wala hook jo ho chuka usay **undo nahi** kar sakta — iski power ye hai ke failure
  agent ke **agle turn** mein push kar de, taake ghalti chup na jaye, fix ho

Dono soorat mein, agent hook ko **skip nahi kar sakta, bahas nahi kar sakta, bhool nahi sakta** — kyunke
harness isay chalati hai, model nahi.

> Chhote loop ki kamzori yaad hai? Iska sirf ek built-in stop tha — **model ki apni opinion apne aap
> ke baare mein**. Hooks iska structural ilaaj hain. "Done" ab model ka claim nahi, **harness ka proven
> state** ban jata hai.

### Claude Code — `settings.json`

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "npm run lint --silent >&2 || exit 2" }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "npm test --silent >&2 || exit 2" }
        ]
      }
    ]
  }
}
```

**Contract exit codes hain** (event ke hisaab se farq): Gate events (`PreToolUse`, `Stop`) pe sirf
**exit `2`** block karta hai (action ruk jati hai ya session khatam nahi hota). `PostToolUse` pe edit ho
chuki hoti hai, to exit `2` undo nahi kar sakta — iski jagah error text agent ke agle input mein wapas
jata hai (yehi AX hai: lint hook jo **konsi rule fail hui** batata hai, khud heal ho jata hai).

### OpenCode — Do Layers

1. **Plugins** — chhota JS/TS module jo `tool.execute.before` / `tool.execute.after` events subscribe
   karta hai
2. **Git hooks + CI** — universal layer. `pre-commit` linter/tests chalata hai, lekin ye **local gate**
   hai aur bypass ho sakta hai (`--no-verify`) — isliye ise **pehli line** samjho, **last line** nahi.
   Asal last line hai: **required CI check + branch protection** (jo Loop Engineering course mein
   GitHub Actions loops se aap ne banaya tha).

```bash
# .git/hooks/pre-commit — tool-agnostic verify gate
#!/bin/sh
npm run lint --silent && npm test --silent || {
  echo "pre-commit: lint or tests failed — commit blocked"; exit 1;
}
```

## Concept 9: Typed Output — Kaam Ko Machine-Checkable Banao

Ek jagah verification chup chaap tootti hai: jab check ki jaane wali cheez **free text** ho. Reviewer
`PASS` ya `FAIL` deta hai, loop us word pe branch karta hai. Us raat kya hoga jab wo jawab de *"This
mostly passes, though I have some doubts..."*? Loop ya to galat parh lega ya ruk jayega. Ek checker jiska
verdict parse hi na ho sake, wo checker **hai hi nahi**.

**Fix: typed output** — fixed, machine-checkable shape mangao, phir code se validate karo isse pehle ke
koi agla step usay trust kare. Blank page vs printed form ka farq hai — fixed boxes, taake ek clerk ek
nazar mein har jawab check kar sake.

```markdown
Reply with ONLY a JSON object, no other text. A passing review
looks exactly like this:
{
"verdict": "PASS",
"reasons": [],
"risk": "low"
}
Allowed values: verdict is PASS or FAIL; risk is low or high; reasons
holds one short string per reason, and is empty only on a clean PASS.
```

```bash
# loop validate karta hai believe karne se pehle — har field, allowed values ke against
echo "$review" | jq -e '
  (.verdict == "PASS" or .verdict == "FAIL") and
  (.risk == "low" or .risk == "high") and
  (.reasons | type == "array") and all(.reasons[]; type == "string")
' >/dev/null || {
  echo "reviewer broke protocol — escalating to a human" >&2
  echo "- reviewer output unparseable: needs a human" >> progress.md
  continue
}
```

**Zaroori baat:** har field ko uske allowed values ke against check karo — sirf `.verdict` exist karta
hai check karna kaafi nahi (wo lazily `{"verdict": "MAYBE"}` accept kar lega). Aur `||` branch dekho:
malformed verdict **hamesha ke liye retry nahi hoti**, **guess** bhi nahi hoti — ye **escalate** karti
hai (verb 5). Jo harness verify nahi kar sakti, wo decision insaan ko de deti hai — **visibly**.

## Concept 10: Correct — Run Recover Karo, Phir System Ko Ratchet Karo

Chautha verb do clocks pe kaam karta hai:

- **Fast clock (Recovery):** kuch **isi run ke andar** ghalat hua, harness ko agle second mein react
  karna hai
- **Slow clock (Ratchet):** run khatam ho chuki, ab yaqeeni banao ke yahi ghalti **kabhi wapas na aaye**

Beginners sirf doosra banate hain, pehla bhool jate hain.

### Recovery — Error Ko Classify Karo

| Error type | Kya karo |
| --- | --- |
| **Transient** (network blip, rate limit, timeout) | Retry karo, badhta hua wait time, hard cap ke saath |
| **Hard failure** (missing permission, tool exist nahi karta) | Retry mat karo — wahi call hamesha wahi fail degi. Skip karo ya escalate karo |
| **Poisoned state** (run ne khud ko broken files/wrong turns mein phasa liya) | Retry ya reroute nahi — **wapas jane ka raasta** chahiye |

**Checkpoint** — ek saved good state jahan run wapas ja sake ya resume kar sake (video game ka save
point jaisa). Coding harness mein sab se sasta checkpoint store: **git**. Har verified step ke baad
commit karo. Claude Code ka `/rewind` session aur files ko earlier point pe roll back karta hai.

> **Production standard:** *ek crashed run resume karti hai, restart nahi.* Jo run sirf restart kar
> sakti hai, wo har failure pe **poori cost dobara** deti hai — tokens, waqt, aapki daily run cap.

### Ratchet — Hashimoto Ka Founding Rule

> *"Jab agent ghalti kare, sirf kaam theek mat karo. Harness ko badal do taake wo ghalti **namumkin** ho
> jaye, phir aage barho aur kabhi is baare mein na socho."*

**Ratchet** ek tool hai jo sirf ek taraf ghumta hai aur wapas ghumne se lock ho jata hai. Har pakri hui
failure ek **permanent part** ban jati hai. Harness sirf **tight** hoti jati hai.

### 4 Failure Classes — Har Ek Ka Apna Ghar

| Failure Class | Nishani | Verb | Fix Kahan Hai |
| --- | --- | --- | --- |
| **Context failure** | Usay pata nahi tha. Galat convention, missed constraint. | **Inform** | Rules file, skill, tool description |
| **Constraint failure** | Aisi cheez ki jo kabhi kar hi nahi sakna chahiye tha. | **Constrain** | Permission rule, sandbox, branch fence |
| **Verification failure** | Bura kaam "done" keh diya gaya. Tests nahi chalayi gayin. | **Verify** | Hook, required CI check, typed output |
| **Planning failure** | Sahi pieces, galat order/size. Bhatakna, bundled changes. | **Structure** (loop layer) | Chhota task, subagent split, `steps` caps |

**Practice:** har failure ke baad 5-minute review — kya hua parho, class naam do, us class ki surface pe
fix likho, khatam. **Same shape ki 2 failures namumkin honi chahiyen.** Agar doosri dikhe, matlab pehli
ko galat classify kiya tha.

> **Harness khud bhi test karo:** Har naya rule, hook, threshold behavior badalta hai. Ek survey mein
> 1,300+ professionals mein se ~90% ke paas observability thi, lekin sirf ~50% offline evals chalate
> the. Wo dekh sakte thay, test nahi kar sakte thay. Fix: chhota, fixed set of test tasks jo har harness
> change ke baad dobara chalao.

### Self-Check
**Sawal:** Raat ki run mein agent ne 3 unrelated fixes ek PR mein bundle kar diye (skill kehti hai "ek
fix per PR"), aur `~/other-project/` se ek file bhi parh li jo repo se related hi nahi. Dono classify
karo.
**Jawab:** Rule likhi hone ke bawajood bundle karna **planning failure** hai (usay rule pata thi, lekin
kaam ko badha tarah structure kiya) — fix structural hai (jaise "ek candidate pe kaam karo, phir ruk
jao"). Project se bahar file parhna **constraint failure** hai — usay ye **karne ki qabiliyat hi nahi**
honi chahiye thi. Fix: filesystem fence ya deny rule, na ke "ghar pe raho" wali ek aur sentence.

---
[⬅ Inform](02-inform.md) · [Agla: Complete Harness Example ➡](04-complete-harness-example.md)
