# Agent Orchestration

Read this only when delegation or parallel execution is being considered.

## Selection gate

Use one agent unless at least one condition is true:

- A bounded investigation would consume substantial context and can return a concise evidence summary.
- Two or more subtasks are independent, have non-overlapping ownership, and can proceed concurrently.
- A specialist review is required by the repository or the change's risk.

Do not delegate a small edit, a sequential dependency chain, or work whose integration requires continuous shared context. Agent Teams are optional; they are not a quality badge.

## Cost check

Expected value should exceed setup, duplicated reading, communication, review, and merge costs. If ownership cannot be stated in one sentence, the split is not ready.

## Safe delegation contract

Give each worker:

- one concrete outcome and explicit file or subsystem ownership;
- acceptance criteria, constraints, and permitted side effects;
- the minimum raw context needed, without leading it to a preferred conclusion;
- a required return format: findings or files changed, tests run, risks, and unresolved questions.

Workers must preserve other agents' and users' changes. Avoid overlapping writes. The integrating agent owns final correctness, security review, conflict resolution, and verification.

## Stop or collapse the team

Return to one agent when tasks become coupled, agents duplicate investigation, merge cost grows, or the next decision needs the same context. Never use parallelism to bypass approvals or expand the user's scope.
