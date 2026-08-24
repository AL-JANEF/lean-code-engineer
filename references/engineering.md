# Engineering

Read this when implementation guidance is needed and no narrower reference or module is sufficient.

## Establish the contract

- Identify the observable behavior, callers, inputs, outputs, invariants, and failure modes.
- Read repository instructions and the nearest analogous implementation before choosing a pattern.
- Distinguish a requested behavior change from an accidental compatibility break.

## Implement the smallest complete slice

- Prefer the existing architecture, language idioms, dependency set, and error model.
- Keep validation at boundaries and domain invariants near the state they protect.
- Preserve useful error context. Do not turn failures into silent defaults.
- Avoid speculative generalization; extract an abstraction only when current duplication or variation proves it useful.
- Treat generated files, lockfiles, migrations, public schemas, and API contracts as explicit change surfaces.

## Manage uncertainty

- Search for evidence before guessing names, types, or behavior.
- If multiple designs are viable, choose the least irreversible one that meets current requirements.
- Surface a user decision only when alternatives materially change behavior, cost, safety, or compatibility.

## Review the diff

- Every changed line should support the requested outcome, its tests, or required documentation.
- Check edge cases at trust boundaries, empty states, retries, concurrency, and cleanup where relevant.
- Remove temporary logging, dead branches, broad suppressions, and stale comments.
- Use [verification](verification.md) before reporting completion.
