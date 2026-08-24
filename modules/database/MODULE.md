# Database Module

Load for schema design, migrations, transaction semantics, query behavior, or data integrity.

## Model and invariants

- Put durable invariants in constraints when the database can enforce them.
- Choose types, nullability, defaults, keys, and uniqueness from domain meaning, not sample data.
- Make tenant or ownership boundaries explicit in every access path.

## Queries and transactions

- Parameterize queries and inspect plans with representative cardinality before adding indexes.
- Keep transactions short; define isolation needs and lock ordering for concurrent writes.
- Avoid unbounded reads and N+1 access; paginate with stable ordering.
- Treat ORM convenience as syntax, not proof of correct query count or transaction behavior.

## Migrations

- Design expand/migrate/contract phases for mixed application versions.
- Separate schema change, backfill, validation, and cleanup when locks or data volume matter.
- Make retries idempotent, monitor progress, and define rollback or forward-fix behavior.
- Never claim a destructive migration is safe without backup and restore evidence appropriate to the environment.

## Verification

- Test constraints, concurrent edge cases, representative data volume, and both upgrade and rollback/forward-fix paths.
- Confirm explain plans and lock impact for performance-sensitive production queries.
