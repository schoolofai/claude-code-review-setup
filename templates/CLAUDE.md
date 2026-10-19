# Invoice service (demo)
Python 3.11+, standard library only, SQLite via `sqlite3`.

## Checks you can run
- Tests: `python3 -m unittest -v`
- Show the output of the tests before saying a change is done.

## Conventions
- All SQL uses `?` placeholders. Never build SQL with f-strings or `+`.
- Never log customer emails, names or invoice amounts. Log IDs only.
- Pages are 1-indexed in the public API (`page=1` is the first page).

## Non-goals
- No ORM, no web framework in this repo.
