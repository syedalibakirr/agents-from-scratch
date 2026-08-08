# Build 01 — The loop

The whole agent: a model, a loop, and three tools. No framework.

## What's here

| File | What it does |
|---|---|
| `agent.py` | The whole agent — ~40 lines of loop, three tools, one trace log |
| `read_trace.py` | Prints `traces.jsonl` as a readable step-by-step of what the agent decided |

## Run it

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key"
python3 agent.py /path/to/some/repo "What does this project do?"
python3 read_trace.py
```

## What an agent actually is

1. You hand a model some tools and a task.
2. It replies with either an answer, or a request to call a tool.
3. If it asks, you run the tool, truncate the output, hand the result back.
4. You loop until it stops asking.

Every step gets written to `traces.jsonl`, one line each.

What makes it an agent isn't the model and isn't the prompt. It's the loop — and the
fact that the model picks its own next tool call instead of you picking for it.

## Build log

**Build 1 — Run the loop once.** Pointed it at a project I built months ago and asked
one question about the code. It answered correctly: full stack, both entry files.

But the trace was more interesting than the answer:

- **11 tool calls** to answer one question. Six were searches; four came back empty or useless.
- It called `list_files` **twice**, getting the identical result the second time.
- It never worked the codebase out by reading code. One search surfaced a line inside
  `CLAUDE.md` — a doc I'd written for a different AI tool — so it read that instead.
  **The answer came from my own notes.**

Two things I wasn't looking for: good documentation is now infrastructure for AI, not
just humans. And the four dead searches were my fault — `search` reads file *contents*,
never filenames, but my description of it just said "search the repo for a string."

Same model, same code. Four wasted calls because of one vague sentence I wrote.

## Known bugs (fixed in later builds)

- [ ] `search` description doesn't say it reads contents, not filenames — Build 3
- [ ] `search` reads binary files (returns junk from `.pyc` caches) — Build 3
- [ ] No way to find a file by name at all — Build 3
- [ ] Agent re-calls `list_files` instead of reusing what it has — Build 25

## Notes

`traces.jsonl` is gitignored on purpose — it contains content from whatever repo you
point the agent at.
