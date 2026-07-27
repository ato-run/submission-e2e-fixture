# Ato submission E2E fixture

Minimal public source fixture for the Capsule Submission Wizard E2E.

- one Python standard-library web service
- no submodules, Git LFS, secrets, or external state
- `GET /health` returns `ok`
- `GET /` returns the exact commit label supplied as one argv element
- `GET /evidence` returns the observed argv and working directory

The v1 runtime launches source capsules at `/app`; the E2E requires the
`/evidence` response to report that exact working directory and preserve
`"commit A with spaces"` as one argument.
