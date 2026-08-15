# 00 — Foundations

## Concept 1: Ye Tools Asal Mein Kya Hain

Ye chatbot nahi hai jisay aap **query** karte ho — **co-worker** hai jisay aap **assign** karte ho.
*"Ye PDF summarize karo"* query hai. *"Ye 3 vendor MSAs parho, hamari redline standard se deviate hone
wali har clause flag karo, aur risk-level se color-coded comparison memo banao"* assignment hai.

**Chat mein worst case:** galat jawab — annoying, contained. **Yahan worst case:** confidently execute
hui galat action jo dazan files ko touch kar chuki hai.

## Concept 2: Architecture 3 Pieces Mein

- **Desktop app** — jahan agent rehta hai, aapki machine pe locally chalta hai
- **Task loop** — outcome describe karo → agent plan banata → aap approve/redirect → agent execute
  karta → significant actions se pehle ruk kar approval mangta
- **Execution surface** — local files (jo access di), sandbox code execution, external services
  (connectors)

**Zaroori privacy farq:** Cowork mein aapke prompts + file content Anthropic ko processing ke liye jate
hain. OpenWork mein aap model provider chunte ho (Anthropic, OpenAI, self-hosted). **Files khud dono mein
machine pe rehti hain.**

## Concept 3: Folders, Connectors, Approvals — Trust Model

**Folder access:** agent sirf wahi filesystem parh/likh sakta hai jo aap grant karo. **Sab se zyada
leverage wali aadat:** ek **dedicated working folder** banao (`~/Claude-Workspace/`), poori `Documents`
ya `Home` nahi. Jab kuch ghalat ho, blast radius sirf working folder hai.

**Connectors:** har on karne wala connector ek alag trust decision hai — install pe jo OAuth scopes grant
karte ho, wahi agent read/write kar sakta hai. **Read scope ≠ send scope** — mail connector ko read scope
dena summarize karne deta hai, write/send alag ask hai.

**Approval modes:** *Ask before acting* (default, har significant action pe rukta) vs *Act without
asking* (Cowork) / stacked `allow always` (OpenWork). **Deletions dono modes mein explicit permission
maangti hain.**

> **Approval table asymmetric hai jaan-boojh kar:** reads automatic hain; writes, modifications,
> deletions, moves — sab explicit click maangte hain.

**Recovery:** Agent-edited files ki koi automatic version history nahi hoti — backup (Time Machine,
OneDrive, git) aap pe depend karta hai. **Stop button** chalti session turant halt kar deta hai.

> **Pehle 2 hafte approvals tight rakho.** Notice karo kaunse actions baar baar wahi approve kar rahe
> ho — wo delegate karne layak hain. Kaunse actions mein aapko waqai sochna para — wo supervised rehni
> chahiye.

## Pehla Real Task — Multi-Source Follow-Up Brief

**Scenario:** Aap ne Acme ke sath sales call ki. Rep ne notes liye, prospect ke sawal chat thread mein
hain. Follow-up email promise ki thi.

**5-step template:**
1. **Folder scope** — working folder chuna, poora filesystem nahi
2. **Explore before assigning** — *"Read everything, tell me what's here, ask 1-2 questions"*
3. **Outcome framing** — deliverable describe karo, assembly agent pe chhoro
4. **Plan request + review** — *"Lay out your plan first, then pause for my approval"*
5. **Approval mode** — cautious mode mein raho kyunke content teesre banday ne likha

```text
Yes, draft the follow-up email. It should:
- Thank Raj and reference one specific thing from the call
- Answer the two questions he asked in the chat thread
- Suggest next steps
- Match my normal email tone

Save as acme-followup.md in this folder. Lay out your plan
first, then pause for my approval before touching anything.
```

**Plan parhte waqt check karo:** kya dono source files identify hui? Kya chat-thread ke sawal represent
hue? Kya saari constraints capture hui?

**Deliverable review — 2 options:**
- **Hand se edit karo** — jab kaam 90% theek ho
- **Agent ke sath iterate karo** — jab structural issue ho: *"Implementation-timeline sawal ka jawab
  bohat generic hai; chat thread ki 4-6-week security-review detail se rewrite karo"*

---
[⬅ Index](README.md) · [Agla: Context, Sessions, Projects ➡](01-context-sessions.md)
