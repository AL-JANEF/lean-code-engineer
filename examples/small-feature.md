# Small Feature

## Request

> Add a `slugify` helper beside the existing text utilities and cover Unicode whitespace without changing current punctuation behavior.

## Expected route

- Core `SKILL.md`.
- `references/engineering.md` if the repository pattern is not immediately clear.
- No Agent Team: the implementation and focused tests are small and coupled.

## Evidence shape

- Inspect neighboring utilities and their test conventions.
- Add the smallest compatible helper and boundary-focused tests.
- Run the focused test file, then the local utility suite if inexpensive.
- Report changed behavior and exact checks; do not claim broad application compatibility from a utility test.
