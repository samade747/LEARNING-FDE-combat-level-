# Summary — Project 6: The Doorbell

**Concept:** 7 — Event-Driven Loop
**Source:** 100% official (`panaversity/agentfactory-labs`)

## Kya Sikhata Hai

Loop jo **kisi event ka reaction** hai — schedule ka nahi, session ka nahi.

## Kyun Zaroori Hai

Ab tak ke 3 heartbeats (in-session, run-until-done, schedule) sab "kab shuru karo" ka jawab waqt se
dete hain. Doorbell doosra sawal jawab deta hai: **"jab kuch ho jaye tab react karo"** — jaise PR
khulna, message ana. Yeh 4th aur aakhri heartbeat pattern hai.

## Kaise Kaam Karta Hai

`.github/workflows/doorbell.yml` GitHub Actions workflow hai jo `pull_request` event (opened,
synchronize) par fire hota hai. Koi bhi PR khole, `anthropics/claude-code-action@v1` chalta hai,
bug review karta hai, aur comment karta hai — **bina kisi ne mangi.**

**Asal lesson:** yeh kabhi aapki machine par chala hi nahi. Laptop band karo, koi aur PR khole, review
phir bhi aata hai — kyunki GitHub Actions runner har baar ek naya, temporary machine hai. Doorbell =
"kuch nahi hota jab tak koi bell na baje, phir turant react karta hai."

## Maine Kya Kiya

Code copy kiya, workflow YAML syntax valid hai (`readings.py` ek sample file hai jisme aap khud bug
plant karte ho — off-by-one, ya deleted null check). **Poora chalane ke liye aapka apna GitHub repo +
Claude GitHub App install + `CLAUDE_CODE_OAUTH_TOKEN` secret chahiye** — yeh main khud nahi kar sakta,
aapke GitHub account ki zaroorat hai.

---
[⬆ Poori Project List](../../README.md#runnable-projects-poore-12-har-ek-ki-real-jagah)
