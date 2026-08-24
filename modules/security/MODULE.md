# Security Module

Load for dedicated threat modeling, authentication or authorization changes, secret handling, or vulnerability remediation. Also read the cross-cutting [security reference](../../references/security.md).

## Scope the threat

- State assets, actors, entry points, trust boundaries, abuse cases, and credible impact.
- Distinguish exploitability evidence from scanner severity or dependency metadata.
- Preserve forensic evidence while preventing continued harm.

## Remediation

- Fix the violated invariant at the narrowest shared boundary, not one observed payload.
- Keep deny-by-default authorization and object-level checks close to protected actions.
- Rotate exposed credentials through the owning secret system; deleting a committed secret is insufficient.
- Use maintained libraries and secure defaults for cryptography, sessions, tokens, and parsing.
- Consider compatibility and availability risks of a security change, but do not preserve an unsafe default silently.

## Evidence

- Add a regression test for the exploit mechanism and denied variants.
- Review adjacent code paths that share the same primitive or boundary.
- Record residual risk, affected versions, migration guidance, and coordinated disclosure needs.
- Avoid publishing working exploit details before users have a mitigation path.

Security review is contextual; a passing scanner or checklist is not proof of safety.
