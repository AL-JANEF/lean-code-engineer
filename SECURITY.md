# Security Policy

## Supported versions

Security fixes are provided for the latest tagged minor release. During the pre-1.0 phase, upgrades may include small compatibility changes documented in the changelog.

## Report a vulnerability

Do not open a public issue for a suspected vulnerability. Use GitHub's **Private vulnerability reporting** feature after the repository is published. If that feature is unavailable, contact the maintainer through a private channel listed on the future repository profile; do not send secrets or exploit data to an unverified address.

Include the affected version, impact, minimal reproduction, and any suggested mitigation. Remove real credentials, personal data, and production payloads.

We aim to acknowledge a complete report within 5 business days and provide a status update within 10 business days. These are response targets, not a guarantee of remediation time.

## Scope

In scope:

- Installer path handling, overwrite behavior, or command injection.
- Instructions that predictably encourage credential exposure, unsafe authorization, or destructive actions.
- Supply-chain and GitHub workflow risks in this repository.
- Generated artifacts that violate the documented security invariants.

Out of scope:

- General model behavior not caused by this skill.
- Attacks requiring a user to approve an obviously unrelated destructive command.
- Social engineering, denial of service, or reports without a reproducible project impact.

See [the threat model](docs/threat-model.md) for trust boundaries and non-goals.
