# 03 — Part 3: The Execution Plane (Concepts 8-10)

## Concept 8 — Sandbox Execution Capabilities

Sandbox execution plane hai — jahan agent ka code harness ke secrets ki access ke bina chalta hai.
**5 capabilities jo agent ko chahiye:**

1. **Filesystem** — files parhna/likhna: inputs, intermediate artifacts, outputs. Unix-like filesystem
   tools ki tarah expose hota hai
2. **Shell** — commands chalana: test runner, package install, clone, custom tool
3. **Package install** — on-demand libraries install karna, "yeh library install karo, phir user ki
   uploaded file parho"
4. **Mounted storage** — files jo local disk ke liye bare hain — sandbox external storage (R2, S3, GCS)
   ko normal paths ki tarah mount karta hai
5. **Snapshot aur resume** — sandboxes throwaway hain aur mid-run fail ho sakte hain. Sandbox apni
   state checkpoint aur fresh workspace mein resume kar sakta hai

**3 properties jo production-grade sandbox ko prototype se alag karti hain:** **Isolation** (sandbox
harness ke network/filesystem/doosre sandboxes tak nahi pahunch sakta, provider infrastructure se
enforced), **Ephemerality** (har task ko fresh sandbox milta hai, task khatam par destroy), **Fast
provisioning** (chand seconds mein start — 30-second start chat-style agent ko slow kar deti).

**Sandbox kya nahi hai:** long-lived VM nahi (problem reinvent karta), serverless function nahi (ek
function chala kar return karta hai — sandbox many tool calls ke darmiyan persist karta hai), Kubernetes
nahi (provider poori container orchestration abstract karta hai).

## Concept 9 — Sandbox Provider Chunna

**Sabse zyada readers ke liye decide karne wala tradeoff:** Cloudflare ke sandbox ko paid Workers plan
chahiye + Python harness aur sandbox ke darmiyan chota bridge Worker. **E2B ka free Hobby tier hai,
native client SDK mein, koi bridge nahi.** Isliye lab bina paise kharch kiye complete karna ho to E2B
realistic free path hai; companion code E2B default karta hai kyunki yeh actually free test ho sakta
hai.

**Cloudflare sandbox ka fayda (jab paid plan par ho):** R2 se proximity — Cloudflare ke apne network
mein chalta hai, R2 bhi wahin, isliye mounting Cloudflare-internal speeds par hoti hai.

**Honest alternatives:**
- **E2B** — realistic free-tier path, storage-agnostic, polished general-purpose
- **Modal** — Python ML workloads par strong, GPU-backed inference ke sath
- **Daytona** — apne cloud account mein chalta hai, regulated industries ke liye (data residency)
- **Vercel** — agar team already Vercel ecosystem mein hai
- **Bring-your-own** — jab security team apne cloud mein sandbox maange

**Recommendation ek line mein:** paid Workers plan + R2 par ho to Cloudflare sandbox; warna E2B, khaas
kar free path chahiye to. Ek chuno aur ship karo, sab survey mat karo.

## Concept 10 — Harness-to-Sandbox Handoff

**Manifest handoff contract hai.** Harness Manifest compose karta hai jo workspace ki zaroorat describe
kare; provider matching workspace provision karta hai. April 2026 SDK mein Manifest **entries** se
banta hai: har entry workspace ka ek path hai jo file, directory, git repo, ya storage mount se mapped
hai.

```python
from agents.sandbox import Manifest
from agents.sandbox.entries import R2Mount
from agents.sandbox.entries.mounts.base import DockerVolumeMountStrategy

manifest = Manifest(
    entries={
        "/workspace/inputs": R2Mount(mount_path="/workspace/inputs",
            bucket="maya-harness-artifacts", account_id=R2_ACCOUNT_ID,
            mount_strategy=DockerVolumeMountStrategy(driver="rclone")),
        "/workspace/outputs": R2Mount(mount_path="/workspace/outputs",
            bucket="maya-harness-artifacts", account_id=R2_ACCOUNT_ID,
            mount_strategy=DockerVolumeMountStrategy(driver="rclone")),
    }
)
```

**Capabilities SDK ke defaults se chuni jati hain, aur passed list unhe replace karti hai (add nahi
karti):** `Capabilities.default()` standard set deta hai (filesystem, shell, compaction). Apni list
pass karo to woh default **replace** karti hai — isliye defaults rakh kar ek add karne ke liye
concatenate karo:

```python
from agents.sandbox.capabilities import Capabilities, Memory
capabilities = Capabilities.default() + [Memory()]
```

> **Real footgun:** `capabilities=[Shell()]` likhna silently filesystem aur compaction abilities gira
> deta hai jo default mein thi. Default rakho aur usme add karo.

**Sandbox `RunConfig` ke through attach hota hai, `Runner.run` argument ki tarah nahi.** Koi
`Runner.run(..., sandbox=...)` parameter nahi hai. `SandboxRunConfig` banao provider ke client aur
options object ke sath, usay `RunConfig` par rakho:

```python
from agents import Runner
from agents.run import RunConfig
from agents.sandbox import SandboxRunConfig
from agents.extensions.sandbox.e2b import E2BSandboxClient, E2BSandboxClientOptions

sandbox = SandboxRunConfig(
    client=E2BSandboxClient(),
    options=E2BSandboxClientOptions(sandbox_type="e2b"),
)
result = await Runner.run(agent, message, run_config=RunConfig(sandbox=sandbox))
```

Cloudflare sandbox ke liye shape same hai — sirf client aur options badalte hain.

**Credential discipline sabse important security point hai.** Harness storage root credentials aur
provider credentials rakhta hai. Specific objects ke liye presigned URLs mintata hai, short expiry ke
sath — sandbox sirf woh scoped URLs pata hai, isliye woh buckets enumerate nahi kar sakta, harness ki
database reach nahi kar sakta (koi connection string boundary cross nahi karti), ya harness ke doosre
services reach nahi kar sakta.

**Lifecycle, ek run ka:**
1. Harness request receive karta hai, session state load karta hai
2. Manifest compose karta hai, provider se workspace provision karwata hai
3. SDK agent loop chalata hai, filesystem/shell calls sandbox tak route karta hai, trace record karta
   hai
4. Workspace fail ho aur snapshots enabled hon to, SDK naya workspace latest snapshot se provision
   karta hai
5. Completion par, harness R2 se outputs parhta hai, trace aur artifact pointers Neon mein persist
   karta hai, sandbox destroy karta hai (kuch idle na rahe), result user ko wapis deta hai

---
[⬅ Five-Component Stack](02-five-component-stack.md) · [⬆ Index](README.md) · [Agla: Observability Aur Evals ➡](04-observability-and-evals.md)
