# Cloud Module

Load for managed services, IAM, networking, resilience, regional design, or cloud cost.

## Service choice

- Start from workload, data classification, recovery, latency, scale, portability, and operating constraints.
- Prefer an existing managed service when it meets requirements and ownership is clear.
- Record quotas, regional availability, failure modes, egress, and pricing dimensions before commitment.

## Security and networking

- Use workload identity and short-lived credentials; scope IAM to required actions and resources.
- Default to private connectivity where practical, restrict ingress/egress, and centralize auditable policy.
- Encrypt in transit and at rest with explicit key ownership and rotation requirements.
- Separate accounts/projects and blast radius according to environment and data sensitivity.

## Reliability and cost

- Define SLOs, backups, restore tests, RPO/RTO, capacity, and regional failover behavior.
- Test dependency loss and degraded modes; replication is not a backup.
- Tag ownership and budgets, measure unit cost, and bound autoscaling and log growth.

Infrastructure changes require a reviewed plan, least-privilege diff, non-production validation where possible, and rollback. Do not mutate a cloud account without explicit authorization.
