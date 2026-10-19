# Claude Code review: copy Anthropic's setup

▶ **Video:** https://youtu.be/kv_s-StuHnc

This repo goes with the ProAI Clips video on how Anthropic reviews AI-written code. It has a throwaway demo repo with three planted problems, plus the three files from the video that you can copy into your own project: `CLAUDE.md`, `REVIEW.md` and a pull request template.

Timestamps (▶ mm:ss) point to the moment in the video where each step is shown.

## Quick start

You need git and Python 3.11 or newer. Steps 1 to 4 need nothing else. Steps 5 to 7 need Claude Code installed and logged in. They count toward your plan's usage or API billing like the rest of your session.

| # | Step | Command | Expected output | ▶ |
|---|---|---|---|---|
| 1 | Clone | `git clone https://github.com/schoolofai/claude-code-review-setup && cd claude-code-review-setup` | a `claude-code-review-setup` folder | 8:39 |
| 2 | Build the demo repo (in an empty throwaway folder) | `./demo/setup_demo.sh /tmp/cc-review-demo` | `Ready: cd /tmp/cc-review-demo/work  (branch add-customer-search, 1 commit ahead of origin/main)` then `FAILED (failures=1)` | 8:42 |
| 3 | See what the branch changes | `cd /tmp/cc-review-demo/work && git diff --stat origin/HEAD...` | `app/invoices.py \| 12 +++++++++++-`, `tests/test_search.py \| 10 ++++++++++`, `2 files changed, 21 insertions(+), 1 deletion(-)` | 8:55 |
| 4 | Layer one: run the check | `python3 -m unittest -v` | `test_page_sizes ... FAIL`, `AssertionError: 0 != 5`, `Ran 2 tests`, `FAILED (failures=1)` (on `main` it prints `OK`) | 9:11 |
| 5 | Local review (in Claude Code, in that folder) | `/code-review` | Findings arrive in your conversation when the background review finishes. Wording varies from run to run. We did not run it for the video, so there is no recorded output here | 9:24 |
| 6 | Security review | `/security-review` | A report on the branch's diff against `origin/HEAD`. Without an `origin` remote you get an `ambiguous argument 'origin/HEAD'` error, which is why step 2 makes a local one | 9:45 |
| 7 | Apply the findings, then re-run the referee | `/code-review --fix` then `python3 -m unittest -v` | Claude's edits go through your permission mode. The tests decide whether the fix worked | 9:59 |
| 8 | Copy the files into your own project | `cp templates/CLAUDE.md templates/REVIEW.md /path/to/your-repo/ && mkdir -p /path/to/your-repo/.github && cp templates/.github/pull_request_template.md /path/to/your-repo/.github/` | three files in your repo; edit them for your stack | 10:12 |

To post findings on a GitHub PR instead of in the terminal, add `--comment`: `/code-review --comment`. The answer key for the planted problems is in [docs/ANSWER_KEY.md](docs/ANSWER_KEY.md). Try the review before you read it.

## What's in here

```
demo/setup_demo.sh            builds the throwaway repo: bare origin.git + work/ on branch add-customer-search
demo/base/                    main branch: a tiny SQLite invoice service, CLAUDE.md, REVIEW.md, PR template, one test
demo/feature/                 the feature branch: customer search + a "paging fix" (with three planted problems)
templates/CLAUDE.md           read by Claude Code and by local /code-review   8:55
templates/REVIEW.md           read only by the managed Code Review service on GitHub   10:16
templates/.github/pull_request_template.md   Testing / Risk / How to revert   10:45
docs/ANSWER_KEY.md            the planted problems (spoilers)
```

`setup_demo.sh` refuses to run in a folder that isn't empty and touches nothing outside it.

## Two gotchas from the docs

- The local `/code-review` follows `CLAUDE.md` and does not read `REVIEW.md`. Only the managed Code Review service reads `REVIEW.md`, from your base or default branch. Rules you want in both places go in `CLAUDE.md`. 10:33
- An AI review can miss bugs, and it reads code without building or running it. Keep the tests as layer one. 11:02

## Sources

Official:
- Anthropic, "Solving code review at Anthropic" (15 Oct 2026): https://claude.dev/blog/solving-code-review-at-anthropic/
- Code Review is now generally available: https://claude.com/resources/articles/code-review-is-now-generally-available
- Code Review docs: https://code.claude.com/docs/en/code-review
- Review locally with /code-review: https://code.claude.com/docs/en/code-review-local
- Customize Code Review (REVIEW.md): https://code.claude.com/docs/en/code-review-customize

Anthropic's public GitHub examples from the video:
- [anthropics/claude-code/tree/main/plugins](https://github.com/anthropics/claude-code/tree/main/plugins): Anthropic's official Claude Code plugins folder
- [anthropics/claude-code/tree/main/plugins/code-review](https://github.com/anthropics/claude-code/tree/main/plugins/code-review): the open-source code-review plugin (4 parallel agents, confidence scoring)
- [anthropics/claude-code/blob/main/plugins/code-review/commands/code-review.md](https://github.com/anthropics/claude-code/blob/main/plugins/code-review/commands/code-review.md): the plugin's actual prompt: "We only want HIGH SIGNAL issues", a validation agent per finding
- [anthropics/claude-code/tree/main/plugins/pr-review-toolkit](https://github.com/anthropics/claude-code/tree/main/plugins/pr-review-toolkit): PR Review Toolkit: 6 specialist review agents
- [anthropics/claude-code-action/blob/main/.github/workflows/claude-review.yml](https://github.com/anthropics/claude-code-action/blob/main/.github/workflows/claude-review.yml): the review workflow that runs on every new PR in the action repo
- [anthropics/claude-code-action/blob/main/.claude/commands/review-pr.md](https://github.com/anthropics/claude-code-action/blob/main/.claude/commands/review-pr.md): the /review-pr command: 5 specialist subagents, posts only noteworthy feedback
- [anthropics/claude-code-action/pull/1595](https://github.com/anthropics/claude-code-action/pull/1595): PR #1595: claude[bot] flags a TypeError, the author fixes it with a regression test
- [anthropics/claude-code-action/pull/1867](https://github.com/anthropics/claude-code-action/pull/1867): PR #1867: findings, answered threads, and diff-only re-review
- [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review): the Claude Code security review GitHub Action (scans only changed files)
- [anthropics/claude-code-action/blob/main/examples/pr-review-comprehensive.yml](https://github.com/anthropics/claude-code-action/blob/main/examples/pr-review-comprehensive.yml): an example PR review workflow you can copy

## License

MIT. See [LICENSE](LICENSE).
