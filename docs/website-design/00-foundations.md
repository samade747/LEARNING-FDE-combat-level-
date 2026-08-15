# 00 — Foundations

## Concept 1: Kyun Sab AI Websites Same Lagti Hain

AI **choose nahi karta, predict karta hai.** Jab aap open sawal poochte ho ("achi website banao"), wo
sab se **common** jawab deta hai — jo cheez usne seekhne mein sab se zyada dekhi. Isay **AI slop**
kehte hain.

**Proof:** Anthropic ka apna **frontend-design plugin** apne hi AI ki 3 default looks list karta hai
(exact shade `#F4F1EA` samet) aur usay unhe **use na karne** ko kehta hai. **Company jisne AI banaya,
usne ek file likhi apne hi AI se bahas karne ke liye.**

**2 nateeje:**
- **Ye habits AI models ke darmiyan travel karti hain** — isliye second AI se review karwana automatically
  second eye nahi hai (dono ne shayad wahi habit seekhi)
- **Fix "prompt harder" nahi hai** — "unique banao" khud ek common request hai. Fix **structural** hai:
  ek taste file jo specific patterns ban kare

## Concept 2: 4-Piece Stack

| Piece | Kaam | Is Course Mein |
| --- | --- | --- |
| **Model** | Page ka code likhta hai | Kimi K3 (design), Claude (review) |
| **Taste** | AI ko boring default se rokta hai | Hallmark skill + Anthropic ki frontend-design plugin |
| **Media** | Real photos/video, kyunke boxes+text brand nahi hain | 4 lanes, free se paid tak |
| **Host** | Page ko internet pe daalta hai | Vercel |

> **Ye 4 boxes hi pricing hain:** client ke liye kaam karte waqt, in 4 lines pe invoice quote karo.

## Concept 3: Design Model Chunna

| Kaam | Chuno |
| --- | --- |
| Planning, architecture | Sab se capable model |
| Approved plan follow karna | Sasta/free model |
| **Visual design + polish** | **Jo bhi is quarter design arena lead kare** |

**Design ke liye alag row kyun?** 2 wajah: **Practice** (kuch companies zyada web design data pe train
karti hain) aur **Dekh sakna** — Kimi K3 apni banai hui page ki tasveer dekh kar sudhaar sakta hai, zyada
tar models sirf apna code parhte hain.

**3 aadatein:** Blind tests pe trust karo, marketing pe nahi (LMArena). Ek AI banaye, doosra judge kare.
**Leader badalne ki umeed rakho** — is course ka poora argument yehi hai ke **file** mein taste hai,
**model** mein nahi.

## Concept 4: Apne Tool Mein Koi Bhi Model

Claude Code Kimi K3 se baat kar sakta hai (Moonshot ne Claude Code ka format accept kiya):

```json
// .claude/settings.json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.moonshot.ai/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "YOUR_MOONSHOT_API_KEY",
    "ANTHROPIC_MODEL": "kimi-k3[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "kimi-k3[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "kimi-k3[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "kimi-k3[1m]",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1048576"
  }
}
```

**5 ehtiyatein:** Har model line set karo (background jobs ke liye bhi). Purani `ANTHROPIC_API_KEY`
delete karo. `/model` nahi, **`/status`** se check karo. Key ko `.gitignore` mein daalo. Web fetching is
route pe kaam nahi karti.

**OpenCode:** OpenRouter se ek minute mein setup — `/connect` → `openrouter` → key paste → `/models` se
`moonshotai/kimi-k3` chuno.

> **Rented-crown rule:** Apni aadatein **tool** aur **files** ke ird gird banao, ek AI model ke ird gird
> nahi. Ranking ka top model ek rented crown pehne hue hai — kisi aur ko mil jayega.

---
[⬅ Index](README.md) · [Agla: Taste as a Skill ➡](01-taste-as-skill.md)
