# 06 — Recap + Try This Now

## Recap

- **Chat batata AI ko kya karna hai ek baar. Skill sikhata kaise, har baar. Connector hath deta
  tumhari apps tak pahunchne ke liye.** Connectors kitchen hain, Skills recipe cards.
- **Skill = folder with `SKILL.md`** — naam, description, plain-English instructions.
- **Connector = safe, scoped access** (Drive, Gmail, Slack) MCP standard par, AI tumhari
  permissions inherit karta.
- **Claude.ai mein skills khud fire hoti** jab prompt description match kare. Slash commands aur
  naam lena overrides hain — isliye description sabse important cheez hai jo tum likhte ho.
- **Friction se diagnose karo** — how re-explain = Skill, app se copy-paste = Connector, dono =
  dono.
- **Skills describe kar ke banate ho**, skill-creator likhta hai. Phir kya fire karta test karo,
  output test karo, fix karo.
- **Ek baar likhi skill multiple tools mein chalti** (Agent Skills open standard) — ChatGPT ke
  GPTs/Gemini ke Gems ke ulat. Claude.ai mein seekho, concepts Claude Code/OpenCode/Cowork/
  OpenWork tak carry hote.
- **Care capability ke sath uthti hai.** Skills enable karne se pehle parho, trusted sources se
  install karo, connectors read-only se shuru karo, scope tight rakho.

AI box jisme type karte ho se layer ban jata jo tumhare standards jaanta aur tools tak pahunchta
hai. Skills aur Connectors isi hafte yeh shift karne ka tareeqa hain.

## Try This Now (6 Exercises, ~30 min)

**1. Built-in skill shuru karo.** File creation on confirm karo (Settings→Capabilities). Phir:
   `"Turn this into a one-slide PowerPoint... [3 facts about your work]."` Skill naam liye bina
   khud fire hote dekho.

**2. Ek app read-only connect karo.** Drive/Gmail connect+enable karo: `"Find [a document] in my
   Drive and give me a three-sentence summary plus the three numbers that matter most."` Kuch
   download/paste nahi kiya notice karo.

**3. Pehli skill banao, baat kar ke.** Apne hafte ka sabse repetitive "how re-explain" task pick
   karo: `"Use the skill-creator skill to help me build a skill for [your task]. Here's exactly
   how I want it done every time: [rules/format]. Ask me anything you need, then build it."`

**4. Description pressure-test karo.** Build hone ke baad: `"When would you use the skill we just
   made? And when would you NOT use it?"` Jawab wide/narrow ho to fix batao.

**5. Ek skill safety ke liye audit karo.** Jo tumne nahi likhi: `"Read this skill and tell me, in
   plain language, exactly what it instructs you to do. Flag anything that contacts an external
   server, handles credentials, or could send my data anywhere."`

**6. Apne 3 tasks diagnose karo.** 3 recurring annoyances likho. Har ek ke liye: how re-explain
   (Skill), app-se-fetch (Connector), ya dono? Ab tumhare pehle 3 projects hain.
