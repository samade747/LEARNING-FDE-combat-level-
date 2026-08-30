# Project 11 — Build the Two-Routine Gate

*Loop Engineering, [`09-routine-drills-and-dreaming.md`](../../09-routine-drills-and-dreaming.md) §11.
Appendix A3 (API trigger), A4 (the gate), A6 (checklist).*

> 🧩 **Sabse aasan zaban mein:** bank mein bara transaction 2 alag logon ke sign maangta hai. Yahan
> **Routine A** kuch reviewable draft karti hai, aur **Routine B** ka koi schedule nahi — woh **sirf
> tab** chalti hai jab koi insaan usay explicitly fire kare (API trigger). B khud-ba-khud kabhi nahi
> chalti — yehi gate hai.

## ⚠️ Status: Blocked on Claude GitHub App

Dono routines ko `samade747/my-doorbell` par branch push / PR open karna hai. Cloud sandbox se
`git push` **HTTP 403** deta hai:

> "Claude doesn't have GitHub access to samade747/my-doorbell for your organization."

Yeh **Projects 9 aur 12 wala hi recurring blocker** hai ([[reference-claude-github-app-not-installed]]).
**Fix (1 min, browser):** https://github.com/apps/claude/installations/select_target — Claude
GitHub App install karo (ya claude.ai → Settings → Connectors → GitHub reconnect). Uske baad neeche
wale steps ~5-10 min mein chalte hain.

## Design (ready to run once unblocked)

### Routine A — the drafter (one-off / weekly cron)

- **Prompt:** *"Draft a short release note for this week's changes on a new branch
  `claude/release-note`. List the commits by short hash. Do NOT open a pull request."*
- **Repo:** `github.com/samade747/my-doorbell`
- **Tools:** `Bash, Read, Glob, Grep`
- Fire it (`RemoteTrigger run`), then **review the branch content yourself**.

### Routine B — the gated action (API trigger, NO schedule)

- **Trigger:** API / webhook — **no `cron_expression`**. Iska matlab woh apne aap kabhi nahi chalegi.
- **Prompt:** *"Open a pull request from `claude/release-note` to `master` with the content already
  on that branch. Title: 'Release note (approved)'."*
- **Bearer token:** generate hote hi copy karo (ek hi baar dikhta hai) — ya is repo se
  `RemoteTrigger action:run` se fire karo.

### The gate in action

1. Routine A chalao → `claude/release-note` branch banti hai
2. Aap khud branch ka content padho (yeh human review step hai)
3. Sahi lage → **aap** Routine B fire karo (`curl` bearer token se, ya `RemoteTrigger run`)
4. Routine B ka transcript padho → PR khuli confirm karo

**Yehi point hai:** B ne kaam **sirf isliye** kiya kyunki ek insaan ne deliberately fire kiya —
kisi schedule ya automatic trigger se nahi.

## Done jab (self-check)

- [ ] B sirf isliye chali kyunki **aap** ne fire kiya (koi schedule nahi)
- [ ] B ke transcript mein PR **actually** khuli dikhti hai
- [ ] Dono routines par A6 checklist chala: connectors pruned (jo chahiye sirf wahi),
      unrestricted pushes off, state file chuna hua

## A6 checklist (dono routines ke liye)

| Check | Kyun |
| --- | --- |
| Connectors pruned | Routine ko sirf woh connectors do jo uska kaam maangta hai — Gmail/Drive/Canva/Figma default attach ho jate hain, hata do agar zaroorat nahi |
| Unrestricted pushes off | Routine `master` par direct push na kar sake — sirf `claude/*` branches + PR |
| State file chosen | Agar routine ki apni memory chahiye (jaise dreaming loop ki `dreaming-state.md`), woh explicitly repo mein ho |
| Least-privilege tools | `allowed_tools` mein sirf zaroori tools |
