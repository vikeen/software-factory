# Calculator factory demo

Small Python calculator (`calc.py`) plus a static page (`web/index.html`) used to
exercise the v2 software factory end to end. Standard library only—no new
dependencies.

## Fresh checkout

From the repo root:

```bash
# No install step; Python 3.10+ only.
python3 -m unittest discover -s tests -t .
```

## Dev server (optional, for UI jobs)

Static files only. From the repo root:

```bash
python3 -m http.server 8000 --directory web
```

For factory jobs, use the port given in the agent prompt (see **Software factory**).

## Validation

Matches `factory/checks.sh`:

```bash
python3 -m unittest discover -s tests -t .
```

Conventions:

- Every function in `calc.py` should have tests under `tests/`.
- Prefer one test module per new function (e.g. `tests/test_subtract.py`).
- `tests/test_calc.py` is protected; add new tests in new files instead of editing it.

## Software factory

`/factory run` builds every open GitHub issue labeled `factory` through
intake → spec → build → gate → review → approve, one PR per issue. State is in
`factory/jobs/` (gitignored); `factory/bin/job` is its only writer. Checks:
`factory/checks.sh`. Dashboard: `cd factory && python3 -m http.server`, then
open http://localhost:8000/dashboard.html.

Each job works in its own git worktree, a full checkout of the repo at
`.worktrees/<job-id>` (gitignored). A tool run from the repo root that doesn't
read `.gitignore` sees those copies too; exclude `.worktrees/` in its config.

Example job artifacts (for learning the file formats): `examples/jobs/`.
