# DevOps Module

Load for CI/CD, containers, environments, deployment, configuration, or rollback.

## Build and supply chain

- Make builds reproducible from declared inputs; pin tools and review third-party automation.
- Use minimal, non-root runtime images and keep build credentials out of layers and logs.
- Generate an artifact once and promote it across environments instead of rebuilding per environment.

## Delivery

- Separate validation from mutation. Prefer plan, dry-run, or diff before deployment.
- Define health, readiness, rollout, rollback, and database compatibility before changing production behavior.
- Serialize or isolate deployments that mutate shared state.
- Keep environment-specific values in configuration, not divergent source branches.
- Ensure failure stops the pipeline; do not mask exit codes or continue after a partial critical step.

## Operations

- Give alerts an owner, user impact, and actionable runbook signal.
- Bound logs and artifacts; avoid secrets and personal data.
- Verify least privilege for CI identities and production credentials.

Test syntax, a non-mutating plan, failure propagation, and rollback on the closest safe environment available. External deployment still requires explicit authorization.
