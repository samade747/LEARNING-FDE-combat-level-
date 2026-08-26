# graph/SCHEMA.md — Claim Contract (Part 6 Pattern)

Har `claims.json` entry ye fields rakhta hai:

| Field | Type | Rule |
| --- | --- | --- |
| `id` | string | Unique. Derived (e.g. `claim_0001`), ID counter se nahi — taake retry duplicate na bana de. |
| `subject` | string | Kis cheez ke baare mein hai. |
| `predicate` | string | Relation — jitna evidence prove kar sake, utna hi specific (`diagnosed_as`, `caused_by` nahi jab tak proof na ho). |
| `object` | string | Relation ka doosra sira. |
| `source` | object | `{"kind": "tool_output"/"document"/"inference", ...}`. `inference` ke ilawa har kind ke paas `ref` ya `command` hona chahiye. |
| `produced_by` | string | Run ID jisne ye claim likha. |
| `supersedes` | string \| null | Agar kisi purani claim ki jagah leti hai, uski `id`. Purani claim **kabhi edit nahi hoti**, sirf naya claim usay supersede karta hai. |
| `created` | string (ISO date) | Kab likhi gayi. |

## 3 Invariants (self-check ke liye)

1. **Koi `status` field nahi.** "Active" hone ka faisla read-time par derive hota hai — jise koi doosri
   claim `supersedes` na kare, wo active hai.
2. **`source.kind: "inference"`** legal hai — lekin honest hona chahiye ("maine ye deduce kiya, kisi
   document se nahi liya").
3. **`supersedes` resolvable hona chahiye** — agar `claim_0004` ko supersede karti ho, to `claim_0004`
   file mein exist karni chahiye.
