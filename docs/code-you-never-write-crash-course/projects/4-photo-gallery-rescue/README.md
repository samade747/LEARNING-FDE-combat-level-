# Project 4 — Photo Gallery Rescue

**Time:** ~45 min · **Tool:** any free AI assistant (Claude.ai, ya terminal surface agar ho)

Pehle 3 projects data **parhte** hain. Yeh **change** karta hai — isliye safety habit sikhata hai
jo baqi nahi sikha sakte. Photo gallery mein duplicates real space kha rahi — dhoondo, safely
delete karo, baqi ko date se sort karo.

## Step 1 — Duplicates Dhoondo (AI photos "dekhta" nahi)

2 photos alag batana ordinary code hai, AI judgment nahi. Code image ko chhota fingerprint banata,
fingerprints compare karta.

```text
Write and run code to find duplicate and near-duplicate photos in this
folder. Fingerprint each image with a perceptual hash, group the ones
that match, and tell me how many duplicates there are and how much
space they take. Don't delete anything yet.
```

Catch number ki tarah aata: _"47 duplicates across 18 sets, 2.1 GB."_

## Step 2 — Safety Gate (yeh step delete karta hai)

Deleted files recycle bin skip karti, fingerprint match galat ho sakta (2 alag sunsets same lagte
hain). Code ko plan dikhana majboor karo:

```text
For each set, keep the largest copy and list the ones you would delete,
with names and sizes. Change nothing yet. Copy the originals to a
backup first, then wait for my approval.
```

List parho. Almost hamesha ek "duplicate" asal mein alag moment hota — usay spare karo, baqi
approve karo. **Yeh review, file delete hone se pehle, poora safety lesson hai.**

## Step 3 — Baqi Ko Sort Karo

```text
Now take the photos that are left and sort them by date, newest first,
into a copy I can scan at a glance. Leave my originals untouched.
```

## Done

- [ ] Real number mila duplicates/space ke liye
- [ ] Kam az kam 1 false match catch ki approve karne se pehle
- [ ] Backup of originals exist karta
- [ ] Survivors date se sorted hain
