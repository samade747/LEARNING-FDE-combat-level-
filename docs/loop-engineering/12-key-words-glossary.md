# 12 — Key Words in Plain English (Glossary)

Yeh poori course mein baar baar yehi lafz aayenge. Ek baar abhi parh lo, phir jab bhi koi term unclear
lage, wapas yahan aa jao.

| Term | Plain-English Matlab |
| --- | --- |
| **Agent** | Ek AI system jo tools use kar sake aur steps complete kare, sirf sawal ka jawab na de. |
| **Prompt** | Instruction jo aap agent ko dete ho. |
| **Loop** | Ek system jo kaam start karta hai, check karta hai, result record karta hai, aur zaroorat pe repeat karta hai. |
| **Beat** | Loop ka ek poora run. |
| **Heartbeat** | Schedule, event, ya condition jo ek beat start karti hai. |
| **Trigger / fire** | Run start karna. Jaise, ek GitHub event ek Routine ko "trigger" ya "fire" kar sakta hai. |
| **Unattended** | Bina kisi insaan ke har step dekhe chalna. |
| **Stopping condition** | Ek testable rule jo loop ko batati hai kaam mukammal hai. |
| **Maker-checker** | Ek agent kaam banata hai. Doosra agent ya command usay check karta hai. |
| **Worktree** | Alag working folder aur branch — taake parallel agents ek dusre ki files change na karein. |
| **Skill** | Project ki knowledge ek dafa likhi hui, jise agent dobara use kar sake. |
| **Connector / MCP** | Ek connection jo agent ko bahar wale system (GitHub, Slack, database) use karne deta hai. |
| **State / memory** | Model ke bahar saved information, taake baad wala run pata laga sake pehle kya hua tha. |
| **Spine** | Is course ka naam us saved state ke liye jo ek beat ko doosri se jorti hai. |
| **Human gate** | Wo point jahan risky action aage barhne se pehle insaan ko review/approve karna padta hai. |
| **Routine** | Claude Code ka cloud automation — saved prompt aur trigger se fresh session start karta hai. |

Course kabhi kabhi body wali metaphors use karti hai: **heartbeat** kaam start karti hai, **body** usay
perform karti hai, aur **spine** runs ke darmiyan memory le jaati hai. Har metaphor apne technical
matlab ke sath hi aati hai.

> **Yeh kahan se aaya:** 2026 mein jinhon ne yeh tools banaye unhon ne saaf keh diya. Boris Cherny ne
> Claude Code banaya. Unhon ne kaha: *"I don't prompt Claude anymore. I have loops running that prompt
> Claude... my job is to write loops."* Peter Steinberger, jisne OpenClaw banaya, ne kaha *"you should
> be designing loops that prompt your agents."* Phir [Addy Osmani](https://addyosmani.com/blog/loop-engineering/)
> ne is pattern ko naam diya aur uske parts list kiye. Teenon mein se koi nahi kehta ke kaam aasan ho
> gaya. Wo kehte hain ke zaroori skill **shift** ho gayi. Yehi idea hai jispe yeh poori course khadi hai.
>
> Kuch log loop design ko is waqt ki sab se important agent-building skill kehte hain. Kuch kehte hain
> yeh sirf purane kaam ka naya naam hai jo agent tools pehle se karte thay. Dono views partly sahi hain.
> Parts naye nahi, lekin ab itne affordable aur reliable ho gaye hain ke everyday use ke layak hain. Isi
> wajah se asal kaam ab **loop design karna** ban gaya hai, har agent turn guide karne ki jagah. Naam
> tabhi useful banta hai jab practice common kaam ban jaye.

---
[⬅ Practice Log](11-practice-log.md) · [Agla: Where to Go Next ➡](13-where-to-go-next.md) · [⬆ Index](README.md)
