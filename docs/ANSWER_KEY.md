# Planted issues on branch add-customer-search (answer key, keep off screen until the reveal)
1. Paging off-by-one: `offset = page * per_page` skips page 1 (CLAUDE.md says pages are 1-indexed). The existing test_page_sizes catches it (page 3 returns 0 rows instead of 5): this is layer 1, "give Claude a check it can run". Verified on the box 17 Oct 22:16 BST: main = OK, feature branch = FAILED (0 != 5).
2. SQL injection: f-string in `search_customers` (CLAUDE.md rule + /security-review target).
3. PII in logs: query (email fragment) and full name+email logged (CLAUDE.md rule).
Expected: /code-review should catch 1 and 3 (and likely 2); /security-review should catch 2. Record what each actually reports: [MEASURE].
