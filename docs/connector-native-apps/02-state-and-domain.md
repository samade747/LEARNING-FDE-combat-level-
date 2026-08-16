# 02 — Part 2: State Aur Domain (Concepts 5-6)

## Concept 5 — State: Ek Banda Yaad Rakhne Layak

Generic chatbot tab bhool jata hai jab aap tab band karte ho. Aapki app aisa nahi kar sakti — session ke
across user yaad rakhna hi isay toy se product banata hai.

v1 chota rakho: Postgres database, **do tables**. Front desk ke do registers socho, loyalty number se
juda: **guest register** (kaun hai) aur **stay-log** (abhi kya kar raha hai). Kaun-hain barely badalta
hai; kya-kar-raha har visit badalta hai — isliye alag tables mein.

```sql
create table users (
  id    text primary key,     -- verified sign-in id, 'sub'
  email text
);

create table user_state (
  user_id text references users(id),
  state   jsonb               -- last position, saved values
);
```

`id` jo dono tables ko jodta hai wahi person ka verified sign-in id hai — code mein iska naam **`sub`**
hai (*subject*, identity ka woh ek piece jispe trust kar sakte ho).

Aapka coding agent **Neon** (hosted Postgres) ko Neon ke apne MCP server ke zariye drive karta hai — ek
project banata hai, branch banata hai, SQL chalata hai jab aap review karte ho.

**Prompt 1 — store banwao:**
```text
Using the Neon MCP server, create the two-table store (users, user_state)
on a dev branch, and save the branch's DATABASE_URL to .env.
```

**Prompt 2 — read/save code likhwao:**
```text
Write db.py: read and save a user's state, keyed by the verified sub
(never an id from a tool argument). Show me a value saving and reading
back on a fresh connection.
```

**Done jab:** Value fresh connection par round-trip kare — save karo, wahi cheez wapis parho. **State
identity se pehle kaam karta hai.**

## Concept 6 — Domain: Abhi Reference Se, Baad Mein Meaning Se

**Domain** matlab aapki app asal mein kis baare mein hai — articles, items, records. v1 simple tareeqe
se fetch karta hai: har record ka id hota hai, `domain_get_item(id)` usay return karta hai.

v1 **jaan-boojh kar** *semantic search* nahi karta abhi — "refunds wala part" ko exact id ke bina dhoondna.
Farq: library mein call-number se book maangna (id se fetch) vs librarian ko "sad whale wali kahani"
bolna (semantic search). v1 call-number desk hai; librarian upgrade hai — woh poora RAG course
(*Give Your AI Searchable Context*) ka subject hai.

```text
Make domain_get_item(id) return a real article from seed/articles.json
instead of the stub. Show me it returning a1 by id.
```

## Optional: Ek Real Agent Ko Apna Tool Call Karte Dekho

Server ko dev-time par test karne ke liye, apne hi coding agent ko ek stand-in client ki tarah use karo:

```bash
claude mcp add --transport http reading-room http://localhost:8000/mcp --scope project
```

Phir:
```text
Use the reading-room domain_get_item tool to fetch article a1, and show
me what came back.
```

Yeh round trip — ek AI aapka tool choose kar ke use karna — poora product miniature mein hai.

> **Do honest notes:** Yeh dev-time peek hai, real delivery nahi (woh claude.ai hai, Concept 13). Aur
> yeh sirf isliye kaam karta hai kyunki abhi auth nahi hai — Concept 8 mein lock lagega, phir bina auth
> call `401` degi.

---
[⬅ The Shape](01-the-shape.md) · [⬆ Index](README.md) · [Agla: Identity Prove Karna ➡](03-proving-identity.md)
