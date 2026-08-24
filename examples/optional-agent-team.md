# Optional Agent Team

## Request

> A monorepo upgrade fails independently in the web build, database migration checks, and deployment image build. Diagnose all three before choosing the release fix.

## Selection

Parallel work may help because the investigations have distinct evidence and ownership:

- Worker A owns the web package and returns the first failing compiler boundary.
- Worker B owns migration validation and returns schema compatibility evidence.
- Worker C owns container build layers and returns the first reproducible image failure.

The integrating agent owns the release decision, cross-cutting dependency version, final diff, and all verification.

## Do not use a team when

The same dependency change must be understood before any investigation can proceed, or all workers would edit the same lockfile and pipeline. In that case, one agent should establish the shared cause first, then reconsider delegation.
