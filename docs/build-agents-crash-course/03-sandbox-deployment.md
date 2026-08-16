# 03 — Part 4: Sandbox Deploy Karna (Concepts 14-16)

Guardrails/approvals (Part 3) decide karte hain action allowed hai **ya nahi**. Sandbox decide karta hai
**agar ho jaye to kahan chalega.** Python agent aapke process mein rehta hai; sirf uski risky tool calls
(Shell, Filesystem) container ke andar chalti hain.

## Concept 14 — Sandboxes Kyun, Aur `SandboxAgent` Kya Hai

Har agent-builder ka sawal: agent laptop par kaam karta hai; kya usay arbitrary code chalane doon?
Honest jawab: **depends** — model usually refuse karta hai lekin hamesha nahi. **Model reliable safety
boundary nahi hai.**

Fix: sandbox. `SandboxAgent` + **capabilities** vocabulary — cheezein jo aap agent ko sandbox ke andar
grant karte ho (shell commands, files read/write, lessons yaad rakhna, long runs auto-summarize).

```python
dev_agent = SandboxAgent(
    name="Developer",
    model="gpt-5.5",
    instructions="You are a developer working inside a sandbox...",
    capabilities=Capabilities.default(),   # Filesystem + Shell + Compaction
)
```

> **Trap yaad rakho:** `SandboxAgent` sirf **built-in capabilities** sandbox karta hai, aapke apne
> `@function_tool` functions ki bodies ko nahi. Ek plain `@function_tool` body wahin chalti hai jahan
> `Runner.run` call hua — aapka Python process, filesystem, network.

| Tool Kism | Body Kahan Chalti Hai | Kis Par Trust |
| --- | --- | --- |
| Built-in capability (`Shell()`, `Filesystem()`) | Container ke andar | Sandbox |
| `@function_tool` HTTPS API call | Aapka Python process | TLS + auth |
| `@function_tool` `subprocess.run`/file write | Aapka Python process | **Kuch nahi. Fix karo.** |

**Sandbox Clients (blast radius se):**

| Client | Kahan Chalta Hai | Real Isolation? |
| --- | --- | --- |
| `UnixLocalSandboxClient` | Laptop par subprocess | Nahi |
| `DockerSandboxClient` | Local Docker container | Haan |
| `E2BSandboxClient` | E2B ke cloud par managed microVM | Haan |
| `CloudflareSandboxClient` | Cloudflare edge par container | Haan |

**Mental model:** "agar model wild ho jaye to kya survive karta hai?" Sirf Docker/E2B/Cloudflare
production ke liye sahi jawab dete hain.

## Concept 15 — Cloudflare Sandbox Bridge Worker + R2 Mounts

Cloudflare Sandbox **bridge** pattern use karta hai — ek remote workshop jahan aap kaam mail karte ho.

- **Worker** — chota program jo Cloudflare data centers mein chalta hai, requests route karta hai
- **Sandbox API** — HTTP endpoints jo Worker expose karta hai ("sandbox banao," "shell command chalao")
- **`CloudflareSandboxClient`** — Python class jo un URLs ko call karti hai

**Chain:** Python agent → `CloudflareSandboxClient` → HTTP → Worker (Cloudflare edge) → sandbox container

**2 tiers:**

| Path | Chahiye | Cost |
| --- | --- | --- |
| **Local dev** (`wrangler dev`) | Free account + Docker Desktop | Free |
| **Production deploy** (`wrangler deploy`) | Workers Paid plan + Docker | $5/mo+ |

**R2 mount** — files jo agent likhta hai durable storage mein land karte hain, ephemeral container
filesystem mein nahi:

```python
manifest = Manifest(entries={
    "data": R2Mount(
        bucket="chat-agent-data",
        account_id=os.environ["CLOUDFLARE_ACCOUNT_ID"],
        access_key_id=os.environ["R2_ACCESS_KEY_ID"],
        secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
        read_only=False,   # default True hai
        mount_strategy=CloudflareBucketMountStrategy(),
    ),
})
session = await client.create(manifest=manifest, options=options)
```

**3 easy-to-miss cheezein:** (1) key `"data"` hai, `"/data"` nahi; (2) `read_only=False` chahiye —
default `True` hai aur silently writes no-op ho jati hain; (3) `mount_strategy` chahiye.

## Concept 16 — Kaam Survive Karwana: R2 Persistence

Cloudflare sandbox tez marta hai — container idle timeout ke baad reap ho jata hai, `/workspace` samet.
Fix: **R2 bucket mount karo sandbox ke andar** — agent jo mounted path par likhe woh durable storage
mein jata hai.

> **User laptop band kar ke ek ghante baad wapis aaye — sandbox zinda hai?** **Nahi.** Default lifetimes
> minutes hain, ghante nahi. Sahi response: files R2 mein confirm karo, phir fresh sandbox spin karo aur
> re-mount karo.

`/workspace/data` (mounted) survive karta hai; baqi `/workspace` container ke sath mar jata hai.

**`Compaction()` capability:** Lambe sandbox runs prompt context barhate hain (tool outputs, file
listings). Compaction context threshold cross hone par purane turns summarize kar deta hai — runaway
bills ke bina lambe effective runs.

**Sandbox `Memory()` vs SDK `Session` — confuse mat karo:**

| Primitive | Kya Store Karta Hai | Lifetime |
| --- | --- | --- |
| **SDK `Session`** | Conversation history | Same conversation ke across runs |
| **Sandbox `Memory()`** | Purane runs se distilled lessons | Alag sandbox runs ke across jo seekhein |

`Session` "pichli baat yaad rakhna" karta hai. `Memory()` "doosri baar yeh bug fix karte waqt kam
exploration" karta hai.

---
[⬅ Safety/Observability/Routing](02-safety-observability-routing.md) · [⬆ Index](README.md) · [Agla: Worked Example ➡](04-worked-example.md)
