# 00 — Overview: Panch AI Employees, Apna Starting Point Dhoondo

Agent Factory ka thesis seedha hai: **future un AI employees ka hai jo result deliver karte hain.**
Yeh chapter woh **panch tools** batata hai jo poori kitaab mein use hote hain — aur sabse zaroori baat,
**konsa pehle try karna hai, yeh kaise decide karein.**

## Apna Starting Point Dhoondo

Sabse simple tareeqa: apne aap se shuru karo, apne kaam ke tareeqe se. Do sawal zyada tar jawab de dete
hain:

1. **Kahan kaam karna chahte ho** — terminal, desktop app, ya messaging app?
2. **Tumhara data kahan rehta hai** — local files, enterprise systems, ya chat workflows?

Do aur sawal pick ko refine karte hain jab tools ka feel aa jaye: **kitna autonomous** agent chahiye,
aur **kitni strict security** chahiye.

Tumhe sab panch tools day-1 par nahi chahiye. Neeche wali table tumhara **pehla cut** hai — wo row
dhoondo jo tumhare **primary** kaam se match kare aur wahan se shuru karo. Rows overlap karti hain (ek
developer power-user bhi hai, ek team-lead domain-expert bhi hai) — apne **main job** se pick karo.
Baqi tools baad mein add karte ho, abhi alternatives nahi (dekho "Migration & Fleet Evolution" neeche).

| Tum Kaun Ho... | Shuru Karo | Kyun |
| --- | --- | --- |
| **Developer/engineer** jo software banata hai | **Claude Code** + **OpenClaw** | Claude Code all-purpose AI employee hai jo tumhare computer se seedha kaam karta hai. OpenClaw phone/messaging apps par personal AI assistant add karta hai. |
| **Domain expert** (finance, law, operations, waghera) | **Claude Cowork** + **OpenClaw** | Cowork business workflows (reports, analysis, documents) handle karta hai, koi technical setup nahi chahiye. OpenClaw WhatsApp/Slack ke zariye daily tasks manage karta hai. |
| **Executive/team leader** AI adoption guide kar raha | **Claude Cowork** | Cowork common workplace tools (mail, drive, chat, calendar, e-signature) se connect hota hai aur scheduled tasks automatically chalata hai. Yahan se AI employees ka asal feel milta hai (paid Claude plan chahiye). |
| **Product manager/architect** AI-powered systems design kar raha | **Claude Code** + **Codex** | Claude Code general-purpose kaam aur prototyping ke liye. Codex heavy-duty reasoning ke liye jab complex system designs ho. |
| **Koi jo security aur data control ki bohat fikar karta ho** | **Cowork, Claude Code, NanoClaw** | NanoClaw har AI employee ko tumhari machine par ek sealed container mein chalata hai. Kuch leak nahi hota. Codebase chhota hai, khud audit kar sakte ho. |

## Day One Par Kya Install Karo

- **Developer ho to:** [OpenClaw](https://openclaw.ai) aur [Claude Code](https://claude.com/code)
  install karo. Dono Part 1 se use hon ge.
- **Domain expert ho to:** [Claude Cowork](https://claude.com/cowork) aur
  [OpenClaw](https://openclaw.ai) install karo. Cowork Claude Desktop app ke andar chalta hai, to pehle
  wo download karo — phir Cowork usi mein ek tab hai. Command line ki zaroorat nahi.
- **Executive/team-leader ho to:** sirf [Claude Cowork](https://claude.com/cowork) (Claude Desktop app
  ke andar) se shuru karo. Ek tool kaafi hai feel lene ke liye, team ko rollout karne se pehle. OpenClaw
  baad mein add karo jab messaging apps mein always-on automation chahiye ho.

## Samjho (Roman Urdu)

Yeh chapter **ranking nahi hai** — "best tool" jaisi koi cheez nahi, kyunke har tool alag job ke liye
banaya gaya hai. Decision tree simple hai: pehle apna **surface** (terminal vs desktop vs messaging) aur
apna **data ka ghar** decide karo, phir us row se shuru karo. Baaki 4 tools waqt ke sath add hote hain,
competition mein nahi.

---
[Agla: Fleet Economics & Trade-offs ➡](01-fleet-economics-and-tradeoffs.md)
