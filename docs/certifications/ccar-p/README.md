# CCAR-P — Claude Certified Architect: Professional

Yeh notes **Claude Certified Architect – Professional Exam Guide v1.0** (effective July 2026, exam
code CCAR-P) ka full breakdown hain — official PDF `Read` tool se poora parha gaya (2026-08-24), Zia
Tutor ke [Certifications](https://agentfactory.panaversity.org/docs/certifications) book-page ke
against cross-checked. Yeh charon Anthropic credentials (CCAR-F, CCDV-F, CCAO-F, CCAR-P) mein sab se
**senior/demanding** hai — is repo ke FDE path (CCAR-F → CCDV-F) ka hissa nahi, ek later capstone hai.

Source PDF: `docs/certifications/Claude+Certified+Architect+–+Professional+Exam+Guide.pdf`

## Index

1. [00 — Quick Facts, Purpose, aur Intended Audience](00-quick-facts-and-audience.md)
2. [01 — Domain Blueprint (7 domains, full objectives, CCAR-F se farq)](01-domain-blueprint.md)
3. [02 — Book Coverage, Scope Note, aur Scoring](02-book-coverage-and-scope.md)
4. [03 — How to Prepare + Sample Questions (full text, 3 questions)](03-how-to-prepare-and-sample-questions.md)
5. [04 — Registration, Policies, Resources, aur Document Control](04-policies-resources-and-doc-control.md)
6. [05 — Test Your Understanding (10 questions)](05-test-your-understanding.md) · [Quiz (same content)](quiz.md)

## Practice Projects

[`projects/00-professional-scenarios/`](projects/00-professional-scenarios/README.md) — all 3
official sample questions (least-privilege tool config, cache-aware prompt ordering, RAG regression
diagnosis) implemented as offline-testable decision logic, 6 pytest tests, all passing. Builds on
[CCAR-F's 5 scaffolds](../ccar-f/projects/README.md) for foundation practice.

## Ek Line Mein Poori Cheez

> CCAR-F test karta hai ke aap ek agentic system **design/build** kar sakte ho; CCAR-P test karta hai
> ke aap uski **poori lifecycle** own kar sakte ho — discovery se lekar governance, compliance
> (GDPR/HIPAA/FedRAMP), aur security/legal/exec stakeholders ke saamne architectural decisions
> defend karne tak. Isi liye 2 naye domains (Governance + Stakeholder Communication, combined 28%)
> hi is exam ka sab se bara farq hain CCAR-F se.

---
[⬅ Certifications Index](../README.md)
