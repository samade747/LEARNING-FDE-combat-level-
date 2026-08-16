# 05 — Part 7: Poore Workforce Ko Serve Karna Aur Operate Karna

> **Aasan lafzon mein:** Layer jo sirf ek chat window ke andar kaam kare, khatam nahi hai. Yeh part usay
> khol deta hai taake dusre tools jo aapke colleagues already use karte hain, same corpus tak pahunch
> sakein — same rules ke sath.

## 2 Tareeqe, Sirf Ek Permission Boundary Rakhta Hai

**Native Onyx MCP server** quick route hai — lekin **client** apna scope choose karta hai, server caller
ke role se scope derive nahi karta. To direct connected Worker aapke **gate ke bahar** search karta hai.
Community Edition mein, iska matlab **sab kuch.**

> **Caution:** Native Onyx MCP endpoint ko iski honest capacity mein use karo — admin tool, public
> corpus demo, ya production route **sirf** permission fidelity prove hone ke baad.

**Context Gateway MCP server** woh route hai jo tikta hai — wahi gateway jo aap ne pehle banaya, ab
bahar expose kiya hua:

```text
Wrap our gateway as its own MCP server called context-gateway. Expose
search_permitted_context, confirm_rule, get_opportunity,
get_contract_state, validate_action... For identity, use bearer tokens
mapped server-side to roles. A role must never arrive as a tool
argument.
```

```text
ACCOUNT_EXECUTIVE_TOKEN  ->  account_executive
SALES_MANAGER_TOKEN      ->  sales_manager
VP_SALES_TOKEN           ->  vp_sales
```

**Client kabhi apna role naam nahi leta** — jo client aisa kar sake, uska koi boundary hi nahi.

> **Caution:** Token hi boundary hai — plain text mein mat bhejo. TLS lagao, per-person token do (per-role
> nahi), expiry rakho. Kabhi expire na hone wala role-shaped token ek shared password hai jispe job
> title likhi hai.

**Test jo matter karta hai:** same sawal `account_executive` aur `vp_sales` se poocho — 2 different
results confirm karo. Agar nahi, gateway kisi client-controlled cheez se identity resolve kar raha hai.

> **Workforce test:** Context layer complete nahi hota kyunki ek chat interface search kar sakta hai —
> complete hota hai jab **har authorized human aur AI Worker** same governed inventory tak apni working
> surface se pahunch sake, same identity aur same permission boundary ke sath.

## Operate Karna

Har connector ke liye 9 cheezein record karo: owner, source class, credential owner, refresh frequency,
expected doc count, last sync, acceptable staleness, escalation path.

> **Trap:** Error mein connector already-indexed content nahi hataata. Search kaam karta rehta hai
> chahe corpus stale ho jaye. **Alert mein farq karo: "search kaam kar raha hai" vs "corpus current
> hai."**

**Upgrade discipline (8 steps):** version record karo → release notes parho → backup lo → settings
export karo → eval baseline chalao → non-production par pehle upgrade karo → evals dobara chalao →
compare karo.

## Production Definition of Done

- Har source classify hai (shared method/Vertical authority/operational state/working context)
- Har connector ka owner, canonical source, refresh expectation, failure alert hai
- Authority routing versioned aur domain experts se reviewed hai
- Governed knowledge source par confirmed hai reliance se pehle
- Current facts live confirmed hain
- Source permissions retrieval se pehle synchronized/enforced hain
- Conflicts aur missing evidence visible rehte hain
- Citations canonical source reopen karte hain
- Backups aur restoration test ho chuke hain
- System of Context applicable System of Record ke around likh nahi sakta

## Digital FTE Ka Bridge

Aapke paas ab ek hi cheez ke 2 halves hain. Pichle course ne Worker ko **owned knowledge** di. Yeh course
ne Worker ko company ki knowledge tak **access** diya — permission, provenance, confirmation ke sath.

**Digital FTE** woh hai jab aap is Worker ke around ek "contract of success" rakhte ho aur usay ek
outcome par point karte ho. Uska retrieval woh hai jo aap ne yahan banaya. Uski authority woh hai jo
aapka governed record kehta hai. Aur uski trustworthiness model ki property hai hi nahi.

---
[⬅ Northstar Case](04-northstar-case-and-proving.md) · [⬆ Index](README.md)
