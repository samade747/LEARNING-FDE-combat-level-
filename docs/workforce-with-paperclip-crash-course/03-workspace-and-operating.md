# 03 — Scenario 7 + Monthly Operating: Workspace Aur Company Chalana

## Scenario 7 — Company Ko Real Desk Do, Taake Woh Real Files Banaye (~10 min)

Ab tak team ka kaam board par **comments** ki tarah rehta hai. Company ne kaam describe kiya, kuch
banaya nahi jo aap pakar sako. Missing piece: **workspace** — ek real folder (ya git repo) jahan aap
company ko point karte ho, taake agent task karte waqt asal files likhe.

```text
Give my company a real place to work. Make a fresh folder for the
Northwind site, point a Paperclip project at it as its workspace.
```

Phir:
```text
Now hand the CMO one task in that project: turn the landing-page copy
it already wrote into an actual landing-page.html. Fire the CMO's
heartbeat, let it work, then show me the file on disk.
```

> **Note:** Yeh Paperclip ka woh hissa hai jiski exact wiring versions ke beech drift karti hai —
> prompts agent ko batate hain live docs se current steps confirm karo.

**Done jab:** Aapke folder mein ek real file (`landing-page.html`) ho, CMO ne likhi hui, jise aap browser
mein khol sako. **Yehi demo aur company ke beech ki line hai.**

## Har Mahine: Company Operate Karo (~10 min)

Company chalana ek standing responsibility hai, one-time setup nahi. Waqt ke sath accumulate hota hai —
har hire, budget change, setting ek chota decision tha, aur chote decisions drift karte hain.

```text
Run my Paperclip monthly company audit. Walk through everything hired,
configured, scheduled, approved, or paused since the last audit. Flag
anything I did not explicitly sign off on, any agent that has not done
productive work, any budget that has drifted, and any setting looser
than it should be.
```

**Common "loose knobs":** Ek hire jo apne budget cap ke bina slip ho gayi (chupke se poori company
ceiling inherit karti hai), ek agent jo bohat zyada cheezein ek sath chala raha, ek config file jo live
state se match nahi karta, ek task `in_review` mein parked jo sirf aapke decision ka wait kar raha.

**Done jab:** Aapke paas ek trusted report ho, aap kam az kam ek loose knob naam le sako, aur kam az kam
ek decision liya ho (missing cap set karna, runaway concurrency ghatana, stale config refresh karna,
idle agent retire karna, ya parked task band karna).

## Aap Ne Kya Banaya

Ek ghante se kam mein, laptop par ek real company khadi ki aur usay founder ki tarah chalaya: goal set
kiya, CEO hire kiya, strategy approve ki, specialist approve kiya, team ka delegated kaam dekha, workspace
diya taake asal file bane, phir poori run ledger se audit ki. **Har move — hire, approve, budget,
delegate, audit — governance move tha, prompt nahi.**

**2 cheezein aap yahan se le jate ho:** Durable artifact **`AGENTS.md`** hai — brief jo aapka general
agent har session parhta hai. Durable skill hai **stance:** autonomy ek grant hai, default nahi —
isliye aap tight budgets, hires/strategy par required sign-off, aur cadence par review se board bane
rehte ho, chahe company khud chal rahi ho.

---
[⬅ Budget Aur Audit](02-budget-and-audit.md) · [⬆ Index](README.md)
