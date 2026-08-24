# GitHub Repository Setup

Apply these settings only after the local project is reviewed and a repository owner is chosen.

## Repository

- Default branch: `main`.
- Description: `Correctness-first software engineering with selective context loading.`
- Topics: `agent-skill`, `claude-code`, `software-engineering`, `progressive-disclosure`, `context-efficiency`.
- Upload `assets/social-preview.png` as the social preview.
- Enable squash merging and automatic deletion of merged branches.
- Disable merge commits if maintainers want a linear release history.

## Branch protection

Protect `main` with pull requests, at least one approving review once more than one maintainer exists, dismissal of stale approvals, required conversation resolution, and the CI matrix as required checks. Do not require a named CODEOWNER until real maintainers are known.

## Security

- Enable private vulnerability reporting.
- Enable secret scanning, push protection, and Dependabot alerts where the hosting plan supports them.
- Review GitHub Action updates before merging; automation has repository-token access even when this project has no runtime dependencies.
- Keep workflow permissions read-only unless a documented job needs more.

## Releases

Use signed annotated tags when maintainer signing is configured. Follow [releasing.md](releasing.md). The `0.x` workflows validate but never publish, tag, or submit to a marketplace automatically.
