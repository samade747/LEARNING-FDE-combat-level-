# 05 — Ek Ordinary Workflow, Shuru Se Akhir Tak

Ayesha regional logistics company mein operations lead hai. Uski team hand se bari customers ke
liye weekly service-exception report likhti. Wo proposal deti: AI dispatch records se draft kare,
phir account manager send kare.

## 5.1 — The Case

- **Reversibility:** send karne se pehle high, baad mein low
- **Consequence of error:** meaningful — delivery failures contracts+trust affect kar sakti
- **Human element:** moderate — summary mechanical hai, par disputed accounts par tone matter
  karti
- **Accountability:** company har factual claim ke liye jawabdeh rehti

**Classification:** appropriate with human review. **Deciding factor:** accountability.

**Gate:** account manager delivery facts dispatch record ke against check karta, disputed
accounts par tone review karta, report send hone se pehle.

## 5.2 — The Data

Inputs: customer names, shipment info, delivery windows, failure reasons, free-text operational
notes. **Kam az kam yellow hai** — internal customer data identifiers ke sath.

Task ko identifiers chahiye? **Haan** — customer report customer+shipments identify kare. Sab
identifiers strip karna solve nahi karta. Team confirm karti **specific workspace+integration
route** is info ke liye approved hai.

## 5.3 — The Capability

Team dispatch system ka connector chahti.

- **Source:** internal platform team
- **Reach:** sirf required reporting tables
- **Fit:** strong — manual export step hata deta
- **Outside content:** kuch free-text fields customer communications se copied text rakhte
- **Actions:** workflow ko report send karne ki permission **nahi** chahiye

**Outcome:** scope confirmation ke baad read-only access enable. Sending account manager ke pass
rehti.

## 5.4 — The People

Customers affected hain, par drivers+operations staff bhi (jo failure notes mein described hain).
Summary "weather delay" ko "driver failure" bana sakti, ya kuch teams ke liye harsher language use
kar sakti.

**Fairness+accuracy check add karo.** Attribution dispatch record se match kare, team phrasing
compare kare reports ke across.

**Disclosure:** contractual+organizational requirements pehle check karo. Silent hon to routine
operational report ko shayad special customer notice nahi chahiye. **Employee-facing consequences
alag se sochni chahiye.**

## 5.5 — The Evidence

Control stronger hota jab pata chale kaam kar raha ya nahi. Pehle quarter ke liye:

- **Success measure:** account managers factual+tone check complete karte sending se pehle
- **Failure threshold:** koi AI-generated factual error itna bara jo matter kare customer tak
  pahunche
- **Monitor:** Ayesha monthly sample review karti
- **Residual risk:** consistent wording bias saare reports mein individual checks survive kar
  sakta — isliye sample review customers ke across bhi compare karti, har report ke andar bhi

**Residual risk** = kya abhi bhi galat ho sakta har planned control design ke mutabiq kaam karne
ke baad.

> **Ek modest workflow ne yeh sab produce kiya** — 15 minute, 7 concrete outputs, 1 escalation
> (driver-disclosure sawal HR ko). Yehi governance hai work-design ki tarah, baad mein add ki hui
> paperwork nahi.

4 questions order mein chalao ek real workflow par, aur answers ek-doosre par build hote hain.
