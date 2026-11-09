# Software Factory (v1 template)

This repository holds the **zazencodes software-factory-claude-code v1** bundle:
`.claude/` (orchestrator skill + subagents) and `factory/` (dashboard, backlog, job state).

## Using this in another project

Copy `.claude/` and `factory/` into your application repo root. Replace this file with
instructions for **your** app: install steps, dev server host/port, and how to run
tests, lint, typecheck, and build. The factory agents read this file; nothing
repo-specific lives in the skill or agent definitions.

## This standalone repo

There is no application codebase here—only the factory machinery. To run jobs against
real code, either embed the factory in an app repo or add an app and document commands
above.

## Dashboard

```bash
cd factory && python3 -m http.server
```

Open `http://localhost:8000/dashboard.html`.

## Commands (Claude Code)

- `/factory <feature>` — new job through the loop
- `/factory next` — first unchecked item in `factory/backlog.md`
- `/factory approve <job-id>` — merge a needs-human job
- `/factory rework <job-id> <note>` — send feedback back to the builder

Upstream: [software-factory-claude-code](https://github.com/zazencodes/zazencodes-season-3/tree/main/src/software-factory-claude-code)
