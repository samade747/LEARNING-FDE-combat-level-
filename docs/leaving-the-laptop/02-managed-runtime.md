# 02 — Managed Runtime (Ghar 3)

## Concept 5: Aap Definition Bhejte Ho, Ek Service Worker Chalati Hai

Ghar 2 ne clock move ki. Ghar 3 **control plane** move karta hai, aur agar aap chuno to **execution
plane** bhi sath. **Managed runtime** ek simple, radical contract wala service hai: aap apna agent
describe karte ho (model, prompt, tools/connectors, guardrails), aur service usay **operate** karta hai.

Concrete example: **Claude Managed Agents** (April 2026 public beta). Aap 3 cheezein banate ho:

- **Agent** — definition: model, prompt, tools, guardrails. Aapki rules file aur reviewer prompt, aisi
  shape mein translated jo service hold kar sake
- **Environment** — walled space jahan agent ke actions execute hote hain (harness course ki fences,
  service-side object ki tarah). **Execution plane hai, aur ek choice hai:** vendor ka cloud sandbox
  default, ya **self-hosted sandbox** aapke control ke infrastructure pe, jahan data ki custody demand
  kare
- **Session** — ek chalti hui kaam ka tukda, apni preserved state aur append-only event log ke sath
  (loop course ki beat, sirf ye **pause, resume, aur din tak survive** kar sakti hai, kyunke koi laptop
  khula rehna zaroori nahi)

**Sab se zaroori architectural detail:** is ghar mein, Concept 2 ke 2 planes **visible aur separable**
ban jate hain. Model jo sochta hai aur sandbox jo karta hai — **alag pieces hain, service se connected.**

**2 boundary facts, saaf tarah se:**
- **Managed control plane vendor-specific hai** — ye Claude chalati hai, Anthropic operate karti hai
- **Managed runtime SDK + hosting nahi hai** — Agent SDK aur Managed Agents **alag products** hain, ek
  ke liye likha code doosre pe deploy nahi hota

> **Simple:** Ghar 1 aur 2: aap worker ko employ karte ho **aur** office bhi maintain karte ho. Ghar 3:
> aap job description aur office rules likhte ho, aur ek **building-services company** office chalati
> hai: power, security, night shifts, repairs. Aap reports se visit karte ho, front door se nahi.

## Concept 6: Kya Milta Hai, Kya Dena Parta Hai, Keemat Kya Hai

**Kya milta hai:** Wo operations jo aap kabhi nahi chahte thay — sandboxing jo harness banane wale khud
maintain karte hain, session state jo crashes/days-long jobs se bach jati hai, context management +
prompt caching. **Behavioral drift ye solve nahi karta** — evals course ki scheduled baseline run apna
poora kaam rakhti hai. **Infrastructure pager unka hai** (3am restart contract se unki problem nahi).
**Business-outcome pager aapka rehta hai** — jab kaam galat ho, waqt pe, unki machines pe, escalation
phir bhi aapki responsibility hai.

**Kya dena parta hai:** 3 cheezein, halki se bhari:
- **Visibility** — aap service ka event log parhte ho, machine khud nahi
- **Custody** — aapke prompts, fixtures, work ke inputs aisi infrastructure pe execute hote hain jo aap
  control nahi karte. **Kisi bhi feature list se ye sawal nahi badalta**
- **Portability** — aapki definition is vendor ki shapes mein likhi hai — jis din aap chhorte ho,
  definition **move nahi hoti, rewrite hoti hai** (Part 6 ka subject)

**Keemat kya hai:** Ek nayi **kisam** ka bill. Ghar 1/2 tokens + runner cost karte hain. Ghar 3 **runtime
khud** ka meter add karta hai — ~8 cents per active session ghanta (idle time free), + tokens. **2
consequences:** (1) session jo thodi soche aur bohat der so, keep karne mein tقریباً free hai. (2)
**bhatakti hui loop (depth-3 disease) ab paisa bhi kharch karti hai, sirf waqt nahi** — **isliye eval
suite ek cost control bhi ban jati hai, sirf quality gate nahi.**

> **Simple:** Managed runtime ek trade hai. Aapko milta hai: vendor un operations ko sambhalta hai jo aap
> kabhi nahi chahte thay. Aap dete ho: kuch visibility, apne data ki custody, aasan portability. Aur ek
> naya bill type — aap active hours pe pay karte ho (idle free), to bhatakti hui loop paisa waste karti
> hai, sirf waqt nahi.

**Vendor updates madad bhi karte hain, nuksan bhi (Going Deeper):** Evals course ki drift story mein
fixed shape thi: model aapki unchanged harness ke neeche move hota hai. Ghar 3 mein **model AUR harness
saath move karte hain**, vendor ke schedule pe — usually kam problems, kabhi kabhi ek behavior badal
jata hai bina aapki kisi file ke. **Defense bilkul nahi badalta:** scheduled full-set run, committed
baseline, loud alert on drop. **Managed runtime aapka operations burden hataata hai. Measurement burden
nahi.** Kisi bhi course mein ye burden kabhi nahi hataya jata.

### Self-Check
**Sawal:** Colleague kehta hai: *"Managed runtime sessions ghante se metered hain, to zaroori taur pe
mehnge hain apne schedule pe chalane se."* 2 cheezein jo ye miss karta hai?
**Jawab:** **Meter:** ye sirf **active** runtime count karta hai, idle free hai. **Jo isne replace
kiya:** ghar 2 ki keemat kabhi sirf tokens nahi thi — tokens + runner + **aapke ghante** (configure
karna, update karna, failure pe jagna). Honest comparison operator samet total cost hai — ye hobby loop
ke liye alag hisab deta hai (ghar 2 easily jeetta hai) aur team serve karti 10 loops ke liye alag (pager
ki bhi keemat hai).

---
[⬅ Headless Bridge](01-headless-bridge.md) · [Agla: The Move ➡](03-the-move.md)
