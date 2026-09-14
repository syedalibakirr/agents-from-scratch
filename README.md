# Agents From Scratch

Building AI agents from scratch, no frameworks. Documented in public, with the traces attached.

No LangChain. No CrewAI. A model, a loop, and a few tools.

Every build ships with its runs, its numbers, and the failures. Nothing here is a claim you have to take on trust.

## What an agent actually is

1. You hand a model some tools and a task.
2. It replies with either an answer, or a request to call a tool.
3. If it asks, you run the tool, truncate the output, hand the result back.
4. You loop until it stops asking.

What makes it an agent isn't the model and isn't the prompt. It's the loop, and the fact that the model picks its own next tool call instead of you picking for it.

## What the builds found so far

**An agent can be right by accident.** In build 01 the agent returned the correct answer. Reading the trace afterwards, only 1 of its 6 searches had contributed anything. Right answer, useless process, and the output looked identical either way.

**Removing one tool description broke it silently.** In build 02, deleting a single tool's description was enough to make the agent return a confidently wrong answer with zero errors logged. Nothing in the output said anything had gone wrong. The cheapest model was also wrong; the most expensive was right.

**Clutter does not cause wrong tool calls, but it does cause silence.** Build 03 added 50 unused tools. Across 19 runs the agent never once called a fake tool. The single miss came from making zero tool calls at all: it answered from general knowledge and asserted it had no access to the codebase, while holding a search tool.

**Measurement lies too.** Before trusting any number the scoring harness produced, I audited the harness itself and found three classes of false positive in my own measurement.

## Builds

Each build is its own folder: a self-contained, runnable snapshot with its own README covering what it adds and what broke along the way.

| Build | What it adds | Code |
|---|---|---|
| 01 | The loop. A model, three tools, one trace log | [`build-01/`](./build-01) |
| 02 | Breaking the loop on purpose, three failure modes | [`build-02/`](./build-02) |
| 03 | 50 unused tools. Does clutter degrade tool use? | [`build-03/`](./build-03) |
| 04 | One sentence, three wordings. Does rewording a tool description change behavior? | [`build-04/`](./build-04) |
| 05 | 20 runs, one question. API default temperature against an explicit one, and what happens when the model rejects the parameter | [`build-05/`](./build-05) |
| 06 | Every run had a trace and every run erased the last one, plus testing three claims made about Opus 5 | [`build-06/`](./build-06) |

See [`LESSONS.md`](./LESSONS.md) for the transferable principles, updated after each build.

## Notes

`traces.jsonl` is gitignored throughout this repo. It contains content from whatever project you point the agent at, which can include private code. Never committed.

## Who

Syed Ali Bakir. Computer Science at Rutgers New Brunswick, B.S. May 2027. Founder and sole engineer of [Triptic](https://triptic.ai), an AI workspace for the college application running 12 agents behind an intent classifier.

Each build is also written up on [LinkedIn](https://www.linkedin.com/in/syedalibakir/).
