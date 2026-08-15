# 00 — Local Tier: Laptop Pe Model (Ollama)

## Concept 1: Apni Machine Pe Ek Brain

Sab se tez tareeqa isay samajhne ka: ek dafa kar ke dekho. **Ollama** free program hai jo AI model
download kar ke aapki machine pe chalata hai.

```bash
ollama run gemma3:4b
```

Sawal type karo, enter dabao. **Concept 1 done jab:** aap ne sawal poocha aur **apni machine** pe chalne
wale model ne jawab diya. WiFi band karo aur dobara poocho — abhi bhi kaam karega. **Kuch bhi aapke
computer se bahar nahi gaya.**

Model `localhost` naam ke address pe sunta hai — ka matlab hai "yehi computer". Aapki machine khud se
baat kar rahi hai.

## Concept 2: Sab Se Zaroori Idea — Brain Sirf Ek Address Hai

Aapke AI tool ke **2 parts** hain:
- **Harness** — machine pe program: files parhta, commands chalata, changes dikhata (Claude Code)
- **Brain** — model jo decide karta hai kya kahna/karna hai

Harness brain tak **address** se pohanchta hai — jaise phone number. Number badlo, wahi harness ab
**alag brain** se baat karta hai. Concept 1 mein naya number `localhost` tha.

> **Ehtiyat:** Local brain aapke pehle use kiye brain ki **chhoti copy nahi** hai — ye ek **alag** brain
> hai, shayad kaafi kamzor.

> **Simple:** Food delivery app jaisa socho. App aapke phone pe roz same hai. Restaurant address badlo,
> wahi app ab alag kitchen se order karta hai. AI tool app hai. Address phone number hai. Us address
> pe kitchen wahan hai jahan model cook karta hai.

## Concept 3: Coding Agent Ko Local Brain Pe Lagana

```bash
ollama launch claude --model qwen3:8b
ollama launch opencode   # OpenCode ke liye
```

**By-hand (Claude Code):**
```bash
export ANTHROPIC_BASE_URL=http://localhost:11434   # bare address, /v1 nahi
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=                          # khaali hona chahiye
claude --model qwen3:8b
```

**By-hand (OpenCode)** — `opencode.json` mein, note karo `/v1` yahan required hai:
```json
{
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "http://localhost:11434/v1" },
      "models": { "qwen3:8b": { "name": "Qwen3 8B (local)" } }
    }
  },
  "model": "ollama/qwen3:8b"
}
```

> **Zaroori farq:** Claude Code **bare** address dial karta hai. OpenCode **`/v1`** ke sath. Ye contrast
> yaad rakho — kisi bhi tool ko kisi bhi local brain se wire kar sakte ho.

## Concept 4: Real Task Do, Dekho Kya Hota Hai

Throwaway git folder mein, local brain pe agent se poocho: *"Is folder mein ek chhota, safe improvement
dhoondo, badlo, dikhao."*

**Strong machine pe:** kaam karta hai — clean change milta hai. **Plain laptop pe:** deewar mehsoos hoti
hai — ya har step minutes leta hai, ya run beech mein ruk jati hai (bad tool call ka error).

## Concept 5: Kyun Ruki Ya Toot Gayi — 2 Deewarein

Local coding agent ko **2 alag deewarein** clear karni hoti hain:

| Deewar | Kya Chahiye | Fix Karti Hai | Fix Nahi Karti |
| --- | --- | --- | --- |
| **Capability** | Har action pe sahi tool call | Stronger model (tool-use trained) | Faster hardware akela |
| **Throughput** | Lambi instruction seconds mein parhna | GPU | Smarter, chhota model |

Sasti machines **dono** deewarein miss karti hain — isi liye plain laptop **chat** ke liye theek hai
lekin **coding agent** ke liye bura.

**Model ready-for-coding guide:**
| Model | Size | Memory | Coding Ready? |
| --- | --- | --- | --- |
| `llama3.2:3b` | 3B | ~8GB | Nahi — tool calls mangle karta hai |
| `qwen3:8b` | 8B | ~16GB | Simple tasks ke liye theek |
| `qwen3:30b-a3b` | 30B mix | 20-24GB | Best balance |

### Self-Check
**Sawal:** Aapki task ruk gayi, har turn 4 minute laga. Aap zyada smart model pe switch karte ho same
laptop pe. Kya tez hogi?
**Jawab:** Nahi. Slow turn **throughput** wall hai, smarter model iske liye kuch nahi karti. Throughput
sirf GPU se theek hoti hai.

## Concept 6: Tool Call Andar Se Kaisi Dikhti Hai

Healthy tool call **structured data** hai:
```json
{"type": "tool_use", "name": "edit_file", "input": {"path": "README.md", "old": "Hello", "new": "Hello, world"}}
```

Kamzor model isay text ki tarah bhejta hai, harness reject kar deta hai. **Ye Concept 4 ki run tori.**

**Context window** bhi zaroori hai — Ollama mein `num_ctx`. Zyada tar laptops pe default sirf **4,096
tokens** hai, jo instruction ko chup chaap trim kar deta hai (koi error nahi). **Fix: kam se kam 64,000
tokens set karo:**
```text
The context window looks too small and it is breaking tool calls. Set it to at least 64,000 and try the task again.
```

## Concept 7: Brain Own Karna Kab Kaam Ka Hai

- **Privacy** — kaam kabhi machine se bahar nahi jata
- **Offline** — koi network, koi account, koi outage nahi
- **Cost, jab kaam din bhar chale** — Loop Engineering mein loops jo har kuch minute chalti hain, apna
  brain own karna cloud se sasta ho sakta hai

**Part 1 complete:** aapke paas brain hai, aap ne 2 coding agents wire kiye, aur 2 deewarein jaanti ho.
Lekin kitchen ne sirf **ek customer** serve kiya — aap. 10 requests ek saath do, queue mein wait karoge.
**Yehi Part 2 hai.**

---
[⬅ Index](README.md) · [Agla: Server Tier ➡](01-server-tier.md)
