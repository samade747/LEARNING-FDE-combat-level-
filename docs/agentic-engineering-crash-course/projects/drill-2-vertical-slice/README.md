# Drill 2 — Vertical Slice as Tracer Bullet

**Time:** ~1 session · **Tool:** Claude Code or OpenCode, `tdd` Skill installed (Drill 1 setup)

## Steps

1. Apne codebase mein koi unfinished feature pick karo.
2. Ek **single user story** likho jo smallest possible end-to-end path trace kare.
3. `tdd` Skill ke andar implement karo (red → green → refactor, ek failing test se shuru).
4. Notice karo slice kitni short hai, aur integration bugs kitni jaldi surface hoti hain (horizontal
   slicing ke muqable).

## Done Jab ("What Good Looks Like")

- [ ] Slice **ek session se kam** mein land hoti hai — test + implementation + reviewable diff, ek
  PR mein (agar nahi, slice too thick thi — split karo)
- [ ] Slice ke **doran** jo integration friction mili wahi drill ki value hai — **naye issues ki
  tarah capture karo**, current slice ko expand mat karo usay absorb karne ke liye
