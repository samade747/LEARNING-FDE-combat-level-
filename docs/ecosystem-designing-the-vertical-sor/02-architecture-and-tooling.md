# 02 — Quick Start, Project Structure, Knowledge as Code, Agent Surface

## 7. Quick Start Aur CLI

> ⚠️ **Yaad rahe:** neeche diye commands abhi **design** hain — chalane par "status notice" print hoga
> aur exit code 2 dega. Yeh implement nahi hue (package abhi `0.0.0` version par hai, sirf naam reserve
> karne ke liye).

```
npx @panaversity/ksor init my-ksor   # Naya KSoR banana
cd my-ksor
npx @panaversity/ksor dev            # Local development, website live update
npx @panaversity/ksor build          # Deployable human surface banana
npx @panaversity/ksor serve          # Agent surface (MCP) ke zariye expose karna
```

CLI vocabulary jaan-boojh kar chhota rakha gaya hai: `init`, `dev`, `build`, `serve` — bas yeh chaar
commands.

## 8. Project Structure

```
my-ksor/
├── knowledge/          # authoritative corpus (plain Markdown)
│   ├── about.md
│   ├── policies/
│   └── procedures/
├── site/                # human-surface config (Docusaurus)
├── .agents/skills/       # coding agents ke liye instructions
└── instance.md          # is KSoR ki identity/maqsad
```

| Folder/File | Kaam |
| --- | --- |
| `knowledge/` | Authoritative corpus — plain Markdown isliye ke portable, diffable, reviewable, version-controlled ho, insaan aur AI dono padh sakein, koi proprietary database na ho |
| `instance.md` | Is KSoR instance ki identity aur maqsad batata hai |
| `site/` | Human-readable surface ki config — ordinary source code rahega, koi opaque hosted service nahi |
| `.agents/` | AI coding agents ke liye instructions aur reusable skills — jaise "policy add karo", "provenance check karo", "quiz banao" |

## 9. Knowledge As Code + Build Provenance

KSoR institutional knowledge ko waise treat karta hai jaise software teams source code ko karti hain:

> **authored → reviewed → version controlled → validated → tested → built → published → consumed**

Git sirf storage nahi rehta — history, authorship, diffs, branches, pull requests, approvals, releases,
rollback, aur reproducible builds deta hai. Isi se yeh shift mumkin hoti hai: **institutional knowledge
governed infrastructure ban jati hai.**

### Build Provenance — har jawab trace ho sake

Har production jawab wapas us knowledge tak traceable hona chahiye jisne usay banaya. Ek
`build.lock.json` file included documents, unke hashes, source commit, KSoR version, waghera record
karti hai. Isse yeh chain banti hai:

> AI Answer → Retrieved Passage → Knowledge Document → KSoR Build → Git Commit → Reviewed Source

Jab koi poochay "agent ne yeh kyun kaha?", to architecture khud is sawal ka jawab discoverable banati hai.

## 10. Agent Surface — MCP

KSoR **Model Context Protocol (MCP)** ko governed knowledge aur AI runtimes ke darmiyan
interoperability boundary ki tarah use karta hai. Maqsad ek aur model-specific plugin banana nahi —
knowledge independent rehti hai, aur model/runtime replaceable ban jata hai (KSoR → MCP → ChatGPT /
Claude / AI Agents / Custom Apps / Digital FTEs).

### Retrieval Asal Product Nahi Hai

KSoR search, embeddings, RAG, ya kisi bhi retrieval technique ko use kar sakta hai — lekin yeh sab sirf
**implementation details** hain. KSoR bunyadi tor par vector database, embedding service, RAG
framework, chatbot, ya MCP wrapper nahi hai. Asal pehchan hai: **authoritative governed knowledge.**

**KSoR vs RAG:** RAG ka sawal — "Relevant information retrieve kar ke model ke context mein kaise dala
jaye?" KSoR ka sawal zyada bara hai — "Kaunsi knowledge itni authoritative hai ke organization insaan
aur AI agents ko is se operate karne ki ijazat deta hai?" RAG, KSoR ka hissa ho sakta hai, lekin KSoR sirf
ek RAG system nahi hai — Governance, Authority, Provenance, Versioning, Review, Scope, Human Surface,
Agent Surface — retrieval to inmein se ek chhota hissa hai.

**KSoR vs CMS:** CMS poochta hai "Content kaise banayen aur publish karein?" KSoR poochta hai "Kaunsi
knowledge authoritative, governed, traceable, aur insaan/agents ke bharose ke laiq hai?" Content ek input
hai — institutional knowledge asal asset hai, aur authority hi farq paida karti hai.

---
[⬅ 01 — Principles](01-principles-and-what-you-can-build.md) · [Agla: 03 — Governance aur AI-Native Role ➡](03-governance-and-ai-native-role.md)
