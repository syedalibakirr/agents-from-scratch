# Agents From Scratch

**30 AI agents, built by hand, in public.** No LangChain, no CrewAI, no agent
framework. A model, a loop, a few tools, and a trace of everything it did.

Every build asks one question about how agents really behave, answers it by running
the agent many times against a real codebase, and publishes the numbers, including the
parts that went wrong.

`7 of 30 builds shipped` · `Python + the Anthropic API` · `every number comes from a trace`

## What an agent actually is

1. Your code sends the model a task, a list of tools, and the conversation so far.
2. The model replies with an answer, or with a **request**: "call this tool with these
   inputs".
3. Your code decides whether to run that request, runs it, and sends back the result.
4. Repeat until the model stops asking.

The model never touches a file. It only asks. Everything that happens on your machine
is your code's decision, and that one fact shapes most of what this series has found:
where a rule lives (in the prompt, or in the loop), what gets logged, what it costs.

The model also has no memory between steps. The loop re-sends the whole conversation
every time, which is why long agent runs get expensive, and why prompt caching matters
(Build 07).

## The builds

| # | The question | What the runs showed | Code |
|---|---|---|---|
| 01 | What is the smallest real agent? | A model, a loop, three tools and a trace log. The first correct answer turned out to be luck once I read the trace. | [`build-01/`](./build-01) |
| 02 | What breaks when you damage it on purpose? | Removing one tool description made it wrong with zero errors logged. The cheapest run was wrong; the most expensive was right. | [`build-02/`](./build-02) |
| 03 | Do 50 unused tools confuse it? | 0 fake tools called across 19 runs. The one miss came from a run that made zero tool calls. | [`build-03/`](./build-03) |
| 04 | Does rewording one tool sentence change behaviour? | Yes. A same-meaning paraphrase shifted tool use (p = 0.004 on 20 runs per wording). | [`build-04/`](./build-04) |
| 05 | How different are 20 identical runs? | Tool calls ranged from 3 to 46 on one question, and the newer model rejects `temperature` with a 400. | [`build-05/`](./build-05) |
| 06 | Does it respect a folder boundary when reading? | Per-run tracing (every earlier run had overwritten the last trace). Opus 0/20 vs Sonnet 3/21 boundary reads, p = 0.23, not significant. | [`build-06/`](./build-06) |
| 07 | Give it hands and a rule: what happens when the fix is off limits? | With a rule in words, 20/20 obeyed and built a workaround that hides the bug. Adding "if the fix is outside, stop and tell me" made 10/10 stop and point to the fix. Prompt caching cut cost per run from $0.46 to about $0.11. | [`build-07/`](./build-07) |

Each folder is a self-contained, runnable snapshot with its own README: what it adds,
how it was measured, the results, and the limitations.

## How I run these

- **Many runs, not one.** The same task can take very different paths, so each
  condition runs 5 to 20 times and results are reported as counts.
- **One change at a time.** Every comparison holds the model, task and codebase fixed
  and changes one thing.
- **Watch what it did, not what it said.** Traces log every tool call. From Build 07 a
  watcher compares the codebase before and after each run.
- **Say the limits.** Every README ends with what the result does not show.

## Run a build

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-api-key-here"   # placeholder, never commit a real key

cd build-01
python agent.py /path/to/any/repo "What does this project do?"
```

Later builds have a `run_test.py` that runs the experiment; each build's README has
the exact commands.

## Privacy note

Traces contain file contents from whatever repo the agent is pointed at, which for
this series is often private code. `*.jsonl` is gitignored across the repo, and only
scrubbed or aggregated results are committed.

## Follow along

The series is posted as it happens on LinkedIn, by Syed Ali Bakir.
