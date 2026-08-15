# 03 — Spine: Runs Ke Darmiyan Memory

Ye wo part hai jo beginners aksar skip kar dete hain — aur yehi loop ko **loop** banata hai.

**Sab se zaroori fact:** Model runs ke darmiyan **sab kuch bhool jata hai**. Agar har beat zero se shuru
ho, to loop nahi hai — bas wahi pehla step baar baar repeat ho raha hai. Fix simple lekin powerful hai:
state ko **model ke bahar**, disk pe rakho.

## Do Layers of State

- **Rules file** (`CLAUDE.md` / `AGENTS.md`) — hamesha wali aadatein, har run ke shuru mein parhi jati
  hain. Isay chhota rakho — bloated rules file har single beat pe cost karta hai.
- **Progress file** (`progress.md`) — plain markdown file (ya Linear board via MCP) jo record karti hai:
  kya try kiya, kya pass hua, kya abhi tak khula hai. **Yehi asal spine hai.** Kal ka 9am run isay khol
  kar wahi se continue karta hai jahan aaj ka run ruka tha.

**Aadat:** Har run **shuru mein progress file parhe** aur **end mein update kare**. Jab loop wahi
ghalti baar baar kare, fix "behtar prompt" nahi — fix ye hai ke loop us lesson ko **rules file** mein
likh de, taake har future run ke liye fix permanent ho jaye.

## Intern Ki Diary — Poori Baat Ek Kahani Mein

Socho aap ek naye intern ko train kar rahe ho. Aap unhe workflow, ticket board, aur kab aapse puchna hai
— sab batate ho. Phir unko ek diary aur do rules dete ho:

1. **Jab bhi feedback milay, diary ke front mein lesson likho, aur roz subah parho** — jaise "wo design
   pattern use mat karo", "ye team commits squash karti hai", "hamesha linter pehle chalao".
2. **Ghar jane se pehle, diary ke back mein likho kya khatam kiya aur kahan roke**, taake kal aaj se
   shuru ho, zero se nahi.

Diary ka **front** = rules file (permanent lessons, har run parhta hai).
Diary ka **back** = progress file (checkpoints, har run update hota hai).

Bina diary ke intern (ya loop) wahi correction baar baar seekhta rahega aur kal ka kaam phir se karega
— chahe kitna hi smart kyun na ho. Model ki memory har run ke baad **mit jati hai**, intern ki dheere
dheere fade hoti hai — lekin dono ke liye diary koi luxury nahi, **fark hai employee aur roz naye ane
wale ajnabi mein**.

## Progress File Ka Example

```markdown
<!-- progress.md — loop ki memory runs ke darmiyan -->

## Done
- 2026-06-22: fixed flaky test in test/auth (retry on token refresh)

## In progress
- Dependency audit: 3 of 7 advisories patched; lodash bump blocked by an API change

## Open / needs a human
- CVE-2026-xxxx in image lib — the fix changes the output format, escalating to a maintainer
```

> Progress file sirf memory nahi — ye aapka **record** bhi hai. Jab aap human gate pe baithte ho, to
> poori transcript nahi, sirf spine parhte ho.

## Real Project: Paper Watch (Spine Ko Kaam Karte Dekho)

Har din arXiv se naye "LLM agents" papers dikhata hai — sirf wo jo pehle nahi dikhaye. Same sawal
dobara pucho, to jawab: *"nothing new since last run ✓"*. Loop ne yaad rakha kyunke usne har paper
`progress.md` mein likha, aur wahi wapas parha.

Memory delete karo aur test karo:
```bash
rm progress.md
show me what's new on arXiv about "LLM agents"
```
Har paper phir se "naya" nazar aayega. **No spine, no loop** — ek command mein prove ho gaya.

## Industry Bhi Isi Design Pe Aayi

Anthropic ka apna memory research bhi isi tareeqe pe aakar ruka: rules file → in-session memory tools
→ skills → **aur ab: memory ko plain file system ki tarah treat karo** — folders mein markdown files,
`grep` jaisi normal tools se search karo, koi special memory API nahi. Ye bilkul wahi spine hai jo ye
course sikhata hai.

## Loop Jo Khud Ko Improve Kare (Hill-Climbing / "Dreaming")

Jab loop rules file mein lesson likh deta hai taake har future run behtar chale, ye **hill-climbing
loop** kehlata hai — iska output kaam nahi, balke **system ki improvement** hai.

**Dreaming** (Anthropic ka managed feature) isi ka out-of-band version hai: ek alag weekly loop jo:

1. Memory store + recent run transcripts collect karti hai
2. Subagents unko analyze karte hain
3. Pattern dhoondti hai jo repeat ho raha ho (ek ghalti = noise, teen dafa = missing lesson)
4. Memory store mein **changes propose** karti hai, evidence ke saath
5. **Insaan accept ya reject karta hai** har change ko, execute hone se pehle

> **Zaroori warning:** Ye loop un rules ko rewrite karta hai jo har doosri loop follow karti hai. Sab
> loops mein se, yehi wo hai jo **kabhi bhi bina human gate ke nahi chalni chahiye.**

**2 khatare:**
- **Memory poisoning** — koi bahar wala (issue/PR text mein) instruction plant kar sakta hai jo dreaming
  pass memory mein permanently likh de. Defense: hamesha evidence + human gate.
- **Brevity bias / context collapse** — baar baar rewrite karne se detail kho jati hai ("check response
  payload, not status code" ban jata hai "handle errors"). Defense: **chhote diffs, poore rewrite nahi**.

---
[⬅ Body](02-body.md) · [Agla: Complete Loop Example ➡](04-complete-loop-example.md)
