# Agents From Scratch

Building AI agents from scratch, no frameworks — 30 builds, documented in public.

No LangChain. No CrewAI. A model, a loop, and a few tools.

## What an agent actually is

1. You hand a model some tools and a task.
2. It replies with either an answer, or a request to call a tool.
3. If it asks, you run the tool, truncate the output, hand the result back.
4. You loop until it stops asking.

What makes it an agent isn't the model and isn't the prompt. It's the loop — and the
fact that the model picks its own next tool call instead of you picking for it.

## Builds

Each build is its own folder: a self-contained, runnable snapshot with its own README
covering what it adds and what broke along the way.

| Build | What it adds | Code |
|---|---|---|
| 01 | The loop — a model, three tools, one trace log | [`build-01/`](./build-01) |
| 02 | Breaking the loop on purpose — three failure modes | [`build-02/`](./build-02) |
| 03 | 50 unused tools — does clutter degrade tool use? | [`build-03/`](./build-03) |
| 04 | One sentence, three wordings — does rewording a tool description change behavior? | [`build-04/`](./build-04) |
| 05 | 20 runs, one question — API default temperature vs. an explicit one, and what happens when the model rejects the parameter | [`build-05/`](./build-05) |

## Notes

`traces.jsonl` is gitignored throughout this repo. It contains content from whatever
project you point the agent at, which can include private code — never committed.
