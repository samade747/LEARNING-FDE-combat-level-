# 04 — Judgment

## Concept 13: SDD Kab Kaam Ki Hai, Kab Overkill

SDD ek discipline hai, discipline ki keemat hoti hai — Specify aur Clarify slow lagenge, tens of minutes
sochne mein jab vibe coding pehle se code dikha rahi hoti. **Beginners method ko theek us waqt chhor
dete hain jab wo sab se bura lagta hai, kamai hone se theek pehle.**

| SDD Ke Liye Chuno... | Skip Karo (Sirf Vibe) Jab... |
| --- | --- |
| Kaam kai files/modules/data touch kare | Ek-baar ka script ya chhoti tweak hai |
| Koi aur (ya future-you) maintain karega | Result aaj hi phenk denge |
| Galat hona mehnga hai (paisa, data, trust) | Galat guess ki keemat "press undo" hai |
| Requirements fuzzy hain, pin karni hain | Task ek sentence mein poori tarah clear hai |
| Kai log "done" pe agree karna chahiye | Aap **seekhne** ke liye explore kar rahe ho |

> *"Is button ko blue karo"* ko poori constitution-to-implement process se guzaarna absurd hai. Lekin
> jaise hi task mein state, permissions, data models, paisa, ya kisi aur ki ummeedein ho, structure
> apni keemat kamana shuru kar deta hai.

**Doosra faida:** Ye aapko **unstuck** karta hai. Anthropic ke data mein, jab build galat direction mein
jati, sab se kam-experienced users **give up** karte the (doosron se kai guna zyada rate pe). Experience
ne jo khareeda wo tha agent ko **wapas track pe steer karne ki qabiliyat.** **Pehle se agreed spec wahi
steering wheel hai.**

**Spec ko zinda rakho (jo sab bhool jate hain):** Spec sirf tab source of truth hai jab **sach rahe.**
Behavior badle to **pehle spec badlo**, phir code re-derive karo. Ye Spec-First ko Spec-Anchored banata
hai.

> **Drift kaisi dikhti hai:** Koi digest email ka subject line seedha code mein badal deta hai, ship
> kar deta hai. Spec purani rehti hai. 3 hafte baad naya teammate spec parhta hai, code ko "fix" kar
> deta hai match karne ke liye — chalta hua kaam chup chaap tor deta hai. **Fix: change spec.md mein
> jaye, code ke sath usi commit mein, hamesha.**

## Specs Ki Limit — Code Ab Bhi Aapka Karza Hai

**Maximalist SDD version:** Specs asal programming language ban jate hain. Code ephemeral artifact ban
jata hai. Koi insaan implementation kabhi nahi parhta. Thoughtworks engineer Valentina Servile ne is
view ke khilaf 3 points diye — **ye course sab accept karta hai:**

1. **Design pin karne wali spec code jaisi lagne lagti hai.** Natural language ambiguous hai. Jab spec
   module boundaries, error handling, naming — sab fix kar de, aap **compiler-less programming language**
   mein program likh rahe ho — fewer guarantees ke sath
2. **Agents deterministic nahi hain, insaan black box ke doosri taraf baitha hai.** Compiler same input
   pe same output deta hai. Agent 5 dafa alag design deta hai. **Kaun decide kare trade-offs sahi hain?
   Judgment — jo spec file mein nahi rehta**
3. **Agent-written code decay hoti hai, aur agent isay hone deta hai.** Agents files ko better nahi
   chhorte jitna paya tha

**SDD in teenon se kaise bachta hai:**

| Objection | Course Kahan Jawab Deta Hai |
| --- | --- |
| Natural language ambiguous hai | Acceptance criteria **executable checks** ban jate hain, prose nahi |
| Agents non-deterministic hain | Aap **plan** review karte ho code se pehle, **result** har step ke baad |
| Code chup chaap decay hoti hai | Spec design pass ke liye fixed point hai, uska replacement nahi |
| Spec ek dafa likho, hamesha ke liye delegate karo | Yehi Waterfall hai, SDD nahi. "Spec zinda rakho" hi asal farq hai |

> **Reframe jo yaad rakhne layak hai:** Achi design ki **audience** badhi hai, gayab nahi hui. Aapke code
> ke ab **2 readers** hain — ek insaan jise judge karna hai system abhi bhi sahi hai ya nahi, aur ek
> agent jise agle hafte usay badalna hai. **Dono readers same defects se suffer karte hain** — tangled
> dependencies, teen jagah likhi hui ek rule, jhoothe naam.

> **Discipline "spec instead of code" nahi hai. Ye hai: what pe agree karo, how generate karo, phir jo
> nikla usay dekho.**

---
[⬅ Complete Worked Example](03-worked-example.md) · [Agla: Practice ➡](05-practice.md)
