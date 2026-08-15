# 02 — Graph of Facts: Anthropic Ka Rasta

Git ne aapko commit DAG **free** mein diya. Knowledge graph aapko **khud banani** hai. Pehle iske liye
trained NLP pipeline chahiye thi. Anthropic ki **Knowledge Graph Construction Cookbook** (23 March 2026)
2026 wala version dikhati hai: poori pipeline **structured-output prompts** mein simat jati hai. 4 stages,
3 concepts.

## Concept 6: Extraction — Schema Hi Training Data Hai

Stage 1 unstructured text ko typed pieces mein badalta hai. Aap ek schema define karte ho, model ka
output us shape tak limit karte ho:

```python
class Entity(BaseModel):
    name: str
    type: EntityType          # apna enum: PERSON | ORG | PROJECT | ...
    description: str          # context, resolution ke liye use hoga

class Relation(BaseModel):
    source: str
    predicate: str             # chhota verb phrase: "commanded", "supplied"
    target: str

class ExtractedGraph(BaseModel):
    entities: list[Entity]
    relations: list[Relation]

def extract(text: str, client) -> ExtractedGraph:
    response = client.messages.parse(
        model="claude-haiku-4-5",           # sasta model — extraction volume work hai
        messages=[{"role": "user", "content": PROMPT.format(text=text)}],
        output_format=ExtractedGraph,
    )
    return response.parsed_output
```

**3 zaroori decisions:**
- **Pydantic schema hi "training data" hai** — koi labeled corpus, koi fine-tuned NER model nahi.
  Ontology badalna ab ek class edit karna hai, pipeline retrain karna nahi.
- **Sasta model volume work karta hai** — extraction har document pe chalta hai, isliye Haiku. Mehnga
  judgment (agla concept) strong model ko milta hai.
- **`description` field decoration nahi hai** — ye context capture karti hai jo Concept 7 ko chahiye
  decide karne ke liye ke 2 naam ek hi cheez hain ya nahi.

> **Simple:** Aap model ko sikhate nahi ke "person" ya "company" kya hai — usay pehle se pata hai. Aap
> usay ek **form** dete ho bharne ke liye, aur jo form fit na kare wo reply reject kar dete ho.

## Concept 7: Resolution — Same Cheez, Kai Naam

Extraction **surface forms** banata hai, saaf graph nahi. Wahi astronaut "Edwin Aldrin," "Buzz Aldrin,"
aur "Col. Aldrin" ban kar 3 documents mein ata hai. Bina merge kiye, graph 3 disconnected log rakhta hai.
**Entity resolution** decide karta hai kaunse surface forms ek hi real cheez hain.

**String similarity kyun nahi?** Ye dono directions mein fail karti hai. "Edwin Aldrin" aur "Buzz Aldrin"
exactly wahan differ karte hain jahan naam kisi ko identify karta hai — similarity score merge miss kar
deta hai. Doosri taraf, 2 alag log "Muhammad Khan" naam ke — similarity score perfect match deta hai aur
galat merge invent kar deta hai. **Naam evidence hain, proof nahi.**

**Cookbook ka move:** resolution ko **reasoning task** treat karo. Candidate entities ko type se group
karo, ek stronger model (Sonnet) ko `description` fields ke sath do, canonical clusters propose karwao.

**Rule jo graph ko durable banata hai: resolution additive aur reversible hona chahiye.** Canonical
entity apne aliases, source documents, model ki merge rationale, confidence, aur us run ka reference
rakhti hai jisne merge kiya. **Kuch overwrite nahi hota.** Surface forms link hote hain, destroy nahi.

> **Kyun itni ehtiyat?** Kyunke **false merge knowledge graphs ki sab se badi failure hai.** 2 logon
> ko ek node mein collapse kar do, aur har downstream traversal unke employers, projects, dates —
> confidently, invisibly, sab jagah mix kar deta hai. Receipts ke sath, bad merge sirf ek reversal hai.
> Bina receipts, poora rebuild hai.

> **Simple:** Naam merge karna 2 logon ke contact cards combine karne jaisa hai. Sahi tareeqa: dono
> original cards merged card ke peeche staple kar do, note ke sath ke kyun aur kitna confident thay.
> Galat tareeqa: 2 ajnabi staple ho jayein, aur koi na bata sake kab shuru hua.

### Self-Check
**Sawal:** Aapki resolution step 5:1 compression ratio report karti hai (5 surface forms per canonical
entity), pichle hafte se up. Team "cleaner" graph pe khush hai. Aapko kya check karna chahiye?
**Jawab:** **False-merge rate.** Compression akela over-merging ko reward karta hai — spectacular ratio
ka sab se tez tareeqa ajnabiyon ko staple karna hai. High ratio sirf tab achi khabar hai jab pairwise
precision qaim rahi ho: merged clusters sample karo aur verify karo members waqai ek hi cheez hain.

## Concept 8: Provenance — Har Edge Apna Receipt Rakhta Hai

Assembly (stage 3) mechanically simple hai — Cookbook ek in-memory NetworkX `MultiDiGraph` use karti hai.
Zaroori cheez container nahi, **har node/edge jo carry karna zaroori hai** wo hai:

```python
def add_entity(G, entity: Entity, source_doc: str) -> None:
    canonical = alias_to_canonical.get(entity.name)
    if canonical is None:                       # unresolved: guess mat karo
        return
    if canonical in G:                          # merge karo, overwrite nahi
        G.nodes[canonical]["source_docs"].add(source_doc)
        G.nodes[canonical]["aliases"].add(entity.name)
        return
    G.add_node(canonical, entity_type=entity.type, description=entity.description,
        source_docs={source_doc}, aliases={entity.name})
```

**2 details poora lesson hain:** dobara dikhne wali entity source document + alias **add** karti hai,
replace nahi. Aur jo resolution step resolve nahi kar saka, wo **drop hota hai, guess nahi hota**.

**4 Invariants** (yaad rakhne ke qabil):
1. Har **claim** ka source hai, ya explicitly "inference" mark hai
2. Har **artifact** ka authoring run + version hai
3. Har **evaluation** apni rubric identify karti hai
4. Har **superseded** object addressable rehta hai — replace hota hai, delete nahi

> **Invariants chup chaap ye mana karte hain:** graph **truth machine nahi hai**. Ye claims, sources,
> relationships store karta hai taake inspect ho sakein. Ye claims ko truth mein convert nahi karta. Ek
> biased corpus ek biased graph banata hai. **Graph ka honest promise chhota aur zyada valuable hai:
> ismein kuch bhi unattributed nahi, aur kuch bhi un-examinable nahi.**

**Invariant 4** ratchet ka bhai hai — jab naya evidence purani claim ko overturn kare, aap
`(claim_new) —supersedes→ (claim_old)` add karte ho. **Delete nahi karte.** Graph apni ghalti yaad
rakhta hai — jo aapko baad mein poochne deta hai *"10 March ko humein kya believe tha, aur kyun?"*

> **Simple:** Receipt ke bagair claim ek **rumor** hai. Rumors se bhara graph koi graph na hone se
> **bura** hai, kyunke ye organized dikhta hai. 4 invariants ek hi aadat hain: kabhi kuch mat likho bina
> ye likhe ke aapko kaise pata, aur ye kis ki jagah le raha hai.

---
[⬅ DAG of Work](01-dag-of-work.md) · [Agla: Working From the Graph ➡](03-working-from-graph.md)
