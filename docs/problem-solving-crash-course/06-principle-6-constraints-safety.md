# 06 — Principle 6: Constraints and Safety

> **Failure mode:** "Agent ne aisi files kyun chhui jo authorize nahi thi?"

Limits problem nahi hain — **yeh AI ko safe banate hain.** Agar AI kuch bhi bina poochhe kar sakta hai,
aapko har second dekhna parega. Agar sirf specific folders access kar sakta hai aur kuch cheezon se
pehle poochta hai, aap chale ja sakte ho aur kaam hone de sakte ho. **Limits AI ko slow nahi karte —
aapko itna trust dilate hain ke usay zyada azaadi de sako.**

Asli khatra yeh nahi ke full access wala AI slow kaam karta hai — khatra yeh hai ke woh **tez ghalat
direction mein** kaam karta hai: aisi files edit karna jo touch nahi karni thin, private data share
karna, aisi services se connect hona jo approve nahi thin.

## Teen Universal Trust Levers

1. **Scope** — kaunse files/folders/data agent dekh sakta hai
2. **Connections** — kaunsi external services agent reach kar sakta hai
3. **Approvals** — kab agent ruk kar aapki OK maangta hai

## Autonomy Ladder (5 Levels)

1. **Watching closely** — har action approve karo. Naye task type ke liye hamesha yahan se shuru karo.
2. **Ambient supervision** — kuch dafa kar chuke ho, theek chala; ab har kuch minute check karo.
3. **Walk away** — trust hai; start karo, doosra kaam karo, wapis aao jab khatam ho.
4. **Act without asking** — bina ruke kaam karta hai. Sirf un tasks ke liye jo kai baar bina problem
   kiye ho chuke hon.
5. **Scheduled/automated** — khud, timer par, bina insaan ke chalta hai. Sirf un tasks ke liye jo
   already "walk away" level par trusted hain.

**Sabse zyada accidents rokne wala rule:** Agar aap AI ko is task par walk-away trust nahi karte, isay
schedule bhi mat karo. Automation sab kuch tez karta hai — galtiyan bhi.

## Prompt-Injection Trap (Documents Mein Chhupi Instructions)

Agar AI koi bahar ki file parhe (email, resume, vendor PDF, webpage), usme chhupi hui instructions ho
sakti hain jo AI ko trick kar den. Text aapko normal lagega, lekin AI usay command samajh sakta hai.

**Bachne ke tareeqe:**
- Bahar ke sources ke sath kaam karte waqt full freedom mat do — "watching closely" level par raho
- Agar AI ka plan aisi files/services mention kare jo aap ne mangi hi nahi, approve mat karo
- Kuch ajeeb ho to turant Stop dabao

## Key Idea

**Tool ke settings mein set kiye rules permanent hain. Prompt mein likhe rules permanent nahi.** Agar
aap chat mein bolo "finance folder mat chhuna," AI 20 messages baad bhool sakta hai. Agar yeh tool ke
settings mein set ho, yeh har session, har baar apply hota hai.

## Hook Example (Dangerous Command Block)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "if echo \"$TOOL_INPUT\" | grep -q 'rm -rf'; then echo 'Blocked: rm -rf denied by hook' >&2; exit 2; fi"
      }
    ]
  }
}
```

Yeh `rm -rf` (sab kuch delete karne wala command) ko hamesha block karta hai. Rule settings mein hai,
prompt mein nahi — har session, har user ke liye apply hota hai.

## Hands-On Practice

Course wahi "Pack 1" folder reuse karta hai, lekin ab pehle se `.claude/settings.json` (ya equivalent)
mein deny rules set karo — sirf `downloads/` parhna allow, likhna/delete karna deny. Jab AI kuch outside
save/move karne ki koshish kare, settings usay **automatically block** kar dete hain — aapko "no" type
karne ki zaroorat nahi.

**Sabak:** Prompt mein rules tab tak chalte hain jab tak aap type karna yaad rakho. Settings mein rules
har baar khud chalte hain.

## Apne Kaam Par Apply Karo

1. **Check karo AI abhi kya access kar sakta hai** — kaunse folders, kaunsi services, read-only ya write.
2. **Repeat hone wale rules ko prompt se settings mein move karo.** Jo bhi baar baar type karte ho
   ("bas read-only"), settings mein daal do — 5 minute lagenge, permanent chalega.
3. **Apni trust level ke baare mein honest raho.** Confident nahi ho? Ek level neeche jao.
4. **Monthly reminder set karo** access clean-up ke liye.

---
[⬅ Principle 5](05-principle-5-persisting-state.md) · [⬆ Index](README.md) · [Agla: Principle 7 ➡](07-principle-7-observability.md)
