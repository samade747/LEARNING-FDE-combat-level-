# 01 — Server Tier: Ek Machine, Kai Users (vLLM)

## Concept 8: Ek Kitchen — 50 Requests Ollama Pe Chalao

Part 1 ka claim: aapka Ollama setup **ek customer** serve karta hai. Chalo prove karte hain.

Ek script (`bench.py`) likho jo ek saath **N requests** (concurrency) fire kare aur report kare kitna
waqt laga, total **tokens per second** kya raha.

```bash
python bench.py http://localhost:11434/v1 qwen3:8b 1
python bench.py http://localhost:11434/v1 qwen3:8b 50
```

**Kya dekhoge:** Concurrency 1 pe theek. Lekin jaise jaise badhaate ho, total throughput mushkil se
badhta hai, wall-clock time badhta jata hai. 50 pe, batch shayad kai minute le. **Kyun:** Ollama sirf
chand requests parallel chalata hai (`OLLAMA_NUM_PARALLEL`), baaki **queue mein**.

> Ye Ollama ki kami nahi — **design choice** hai. Ollama **ek insaan ke laptop** ke liye banaya gaya,
> **restaurant** ke liye nahi.

> **Simple:** Ye ek ghar ki kitchen hai, ek cook aur do burners ke sath. Ek guest — wonderful. 50 guests
> — 45 hallway mein khare hain order slip ke sath.

## Concept 9: Industrial Kitchen — Wahi Brain vLLM Se Serve Karo

**vLLM** free, open source program hai jiska ek kaam hai: model ko **kai users ko ek saath** serve
karna, bina GPU waste kiye.

**2 tricks:**
- **Continuous batching** — GPU ko ek saath kai requests deta hai, jab ek khatam ho, agli **mid-stream**
  slide kar deta hai
- **Paged memory (PagedAttention)** — memory ko chhote pages mein deta hai, sirf zaroorat ke mutabiq

```bash
pip install vllm
vllm serve Qwen/Qwen3-8B \
  --enable-auto-tool-choice \
  --tool-call-parser hermes \
  --reasoning-parser qwen3
```

> **Zaroori:** `--enable-auto-tool-choice` + parser flags ke bagair, coding agents chup chaap fail
> hote hain — server kabhi clean tool call banata hi nahi.

**16GB card pe:** `Qwen/Qwen3-8B-FP8` compressed build use karo.

## Concept 10: Reveal — Wahi 50 Requests, 2 Curves

Wahi sweep vLLM ke against chalao. **Ollama line flat rehti hai** — users add karna throughput nahi
badhata, queue lambi karta hai. **vLLM line chadhti hai** — har naya user throughput add karta hai, jab
tak GPU pura na bhar jaye.

**Gap serving layer ki hai** — hardware same, brain zyada tar same, sirf serving layer alag.

### Self-Check
**Sawal:** Dost chart dekh kar kehta hai *"vLLM model ko tez banata hai, isay apne laptop pe bhi use
karo."* Kya sahi hai, kya galat?
**Jawab:** Dono galat. vLLM **ek user ke liye model tez nahi karta** (concurrency 1 pe dono curves qareeb
shuru hoti hain). vLLM **load ke neeche machine ko tez karta hai**. Plain laptop pe madad nahi karega —
continuous batching ko batch karne ke liye GPU chahiye.

## Concept 11: Coding Agents Ko Server Se Wire Karo

Same wiring, naya port:
```bash
export ANTHROPIC_BASE_URL=http://localhost:8000
export ANTHROPIC_AUTH_TOKEN=dummy
export ANTHROPIC_API_KEY=dummy
export ANTHROPIC_DEFAULT_OPUS_MODEL=Qwen/Qwen3-8B
export ANTHROPIC_DEFAULT_SONNET_MODEL=Qwen/Qwen3-8B
export ANTHROPIC_DEFAULT_HAIKU_MODEL=Qwen/Qwen3-8B
claude
```

> **Sharing warning:** Jis waqt aapki vLLM machine kisi aur ko serve kare, `localhost` machine ka real
> address ban jata hai. Kam se kam `--api-key` set karo.

## Concept 12: Server Tier Kab Kaam Ki Hai

- **Team ya classroom** — 50 log ek vLLM machine pe, sab ek cleared wall share karte hain
- **Din bhar chalne wali loops** — per-token bill kabhi nahi rukta. Apni GPU pe, ek aur request tقریباً
  free hai
- **Team-scale privacy** — data control ki hui machine pe, sab ko serve

**Honest limit:** vLLM ne **sirf throughput** wall move ki. Model **utna hi smart hai** jitna laptop
pe tha. Agar task 8B model ke liye bohat mushkil hai, koi serving layer isay bacha nahi sakti. **Yahan
se cloud tier chahiye.**

### Self-Check
**Sawal:** Aapki din-bhar chalti loop hard refactoring tasks pe galat jawab deti rehti hai. Colleague
Ollama se vLLM move karne ka kehta hai. Kya theek hoga?
**Jawab:** Nahi. Galat jawab **capability** wall hai, serving layer isay touch nahi karti — vLLM wahi
brain tez serve karta hai, smarter brain nahi. Fix ke liye Part 3 ka cloud tier chahiye.

---
[⬅ Local Tier](00-local-tier.md) · [Agla: Cloud Tier ➡](02-cloud-tier.md)
