# Module Catalog

Load at most the module that matches the current domain decision. These files are optional extensions to the core priority order, not a checklist to preload.

| Module | Load when |
|---|---|
| [Frontend](frontend/MODULE.md) | Browser UI, state, accessibility, rendering, or client security |
| [Backend](backend/MODULE.md) | APIs, jobs, service logic, concurrency, or external integrations |
| [Database](database/MODULE.md) | Schemas, migrations, transactions, or query behavior |
| [DevOps](devops/MODULE.md) | CI/CD, containers, environments, deployment, or rollback |
| [Security](security/MODULE.md) | Threat modeling, auth, secrets, or vulnerability remediation |
| [Testing](testing/MODULE.md) | Test strategy, regression design, fixtures, or flaky suites |
| [Performance](performance/MODULE.md) | Measured latency, throughput, memory, bundle, or cost problems |
| [Cloud](cloud/MODULE.md) | Managed services, IAM, networking, resilience, or cloud cost |

Add a module only when it contains domain decisions that would otherwise repeatedly inflate `SKILL.md` or a cross-cutting reference.
