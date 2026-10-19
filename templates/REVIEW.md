# Review instructions
(Read by the managed Code Review service on GitHub PRs. The local /code-review command does NOT read this file; it reads CLAUDE.md.)

## What Important means here
Important = wrong results, data leaks (PII in logs or errors), SQL injection, or anything that breaks paging for API clients.
Style and naming are Nit at most.

## Cap the nits
Report at most three Nits per review.

## Do not report
- Formatting or lint (CI does it)
- Anything under `tests/fixtures/`

## Always check
- Every new query uses `?` placeholders
- New public functions have a unit test
- Behaviour claims cite a file:line, not a guess from a name

## Summary
Start the summary with the number of Important findings. If there is nothing to fix, say so in one line.
