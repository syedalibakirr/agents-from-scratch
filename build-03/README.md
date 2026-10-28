# Build 03: the flood test

Add 50 fake tools to the agent's list and ask the same questions about a real
codebase. Does the clutter make it call the wrong tools?

It didn't. Across 19 runs the agent never called a fake tool. The one wrong answer
came from somewhere else: on one question, with the flooded list, it made **zero
tool calls**, answered from general knowledge, and got the codebase wrong. That
happened 4 times out of 4.

The prompt for this build was a paper, "The Bitter Lesson of Tool Calling"
(arXiv 2608.06370), which reports that JSON tool calling gets worse as the context
fills with clutter. This build tests one narrow version of that on the Build 01
agent.

## The setup

The agent is Build 01's loop with its 3 real tools: `list_files`, `read_file`,
`search`. The target is a private production codebase (my startup, Triptic). Eight
fixed questions, each with one answer that can only be found in the code:

| Q | Question |
|---|---|
| 1 | Which of these three folders is the live backend: server, python-backend, or triptic-backend? |
| 2 | What embedding model does the semantic search use, and what vector dimension does the column expect? |
| 3 | Which file triggers Google OAuth sign-in? |
| 4 | Is the Supabase session stored in localStorage or sessionStorage? |
| 5 | What access does fix_chat_upload_permissions.sql grant on the chat-attachments bucket? |
| 6 | Which file calls the Anthropic API? |
| 7 | What is the timeout, in seconds, on the Anthropic HTTP call? |
| 8 | What is the name of the BroadcastChannel used to sync auth across tabs? |

Two conditions, and nothing else changes between them:

| Condition | Tools the model sees |
|---|---|
| `clean` | the 3 real tools |
| `flood` | the 3 real tools plus 50 fake ones (`query_database`, `send_email`, `resize_image` and so on) with realistic names, descriptions and parameters |

Calling a fake tool does nothing: `agent.py` logs a `fake_tool_attempt` and returns
`ERROR: <name> is not available.`

Model: `claude-sonnet-5`, default temperature, for every run.

## Results

Every number comes from [`RESULTS_BUILD3.md`](./RESULTS_BUILD3.md), which lists
every run and every tool call. Answers were graded by hand against an answer key.

| | `clean` | `flood` |
|---|---|---|
| Questions answered correctly | 8 of 8 | 7 of 8 |
| Fake tools called | n/a | 0 |
| Total tool calls, one run per question | 44 | 34 |

Tool calls per question (wall time in brackets):

| Q | `clean` | `flood` |
|---|---|---|
| 1 | 26 (51.7 s) | 19 (43.5 s) |
| 2 | 3 (13.2 s) | 2 (11.0 s) |
| 3 | 5 (14.4 s) | 4 (13.7 s) |
| 4 | 3 (12.3 s) | **0, 0, 0, 0** (8.8, 8.4, 10.6, 8.9 s) |
| 5 | 3 (16.0 s) | 3 (15.2 s) |
| 6 | 1 (8.2 s) | 2 (14.0 s) |
| 7 | 2 (8.6 s) | 3 (15.0 s) |
| 8 | 1 (5.0 s) | 1 (7.7 s) |

What happened:

- **The fake tools were ignored.** 19 valid runs, 50 fake tools on offer in 11 of
  them, 0 calls to a fake tool.
- **The miss was silence.** On Q4 with the flooded list, the agent made no tool
  calls at all and answered "localStorage", which is Supabase's default. This
  codebase uses sessionStorage. The `clean` run searched 3 times and found that.
- **It repeated.** I ran Q4 `flood` 3 more times. All 4 runs made zero tool calls
  and gave the default answer. 2 of the 4 said outright that they had no access to
  the codebase, while holding a search tool. A third offered to check.

So the clutter did not cause wrong tool calls. On one question it caused no tool
calls, and the answer sounded just as confident.

## Statistics, stated plainly

- 0 fake-tool calls in 19 runs: the 95% upper bound on the true rate is 17.6%.
  "Never" here means "not in 19 tries".
- 4 of 4 zero-call runs on Q4 `flood`: the 95% lower bound is 39.8%. It is a real,
  repeatable behaviour on this question, not a one-off.
- One run per question per condition (plus the 3 repeats) is too few to say the
  flood changes tool-call counts in general. The 44 vs 34 total is a description,
  not a finding.

## Limitations

- One codebase, one model, 8 questions, 19 valid runs.
- Only Q4 broke, and Q4 is the one question with a well-known default answer the
  model could give without looking. That may be the real cause, with the flood as
  the trigger.
- The fake tools are unrelated to the questions. Fake tools that look useful for
  the task could behave differently.
- 22 runs crashed on a network error (`APIConnectionError`) before the model
  replied once. They were re-run and are excluded; they are listed at the end of
  `RESULTS_BUILD3.md`.
- `run_test.py` overwrites `traces.jsonl` on every run, so only the last raw trace
  survived. Build 06 fixed that.

## Traces and privacy

The target is a private codebase. `run_test.py` writes the agent's full answers to
`FLOOD_TEST_RESULTS.md`, which is gitignored. `make_public_results.py` turns it into
`RESULTS_BUILD3.md`: every question, condition, wall time, tool call and input,
with each answer replaced by its length. Answers from runs with zero tool calls are
kept word for word, because those runs never opened the codebase.

## How to reproduce

You need your own target repo and your own 8 questions; the codebase used here is
private.

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-api-key-here"   # placeholder, never commit a real key

cd build-03
# edit QUESTIONS and the target path in run_test.py first
python run_test.py --q 1 --condition clean
python run_test.py --q 1 --condition flood
# repeat for --q 1 to --q 8

python make_public_results.py
```

## What's here

| Path | What it is |
|---|---|
| `agent.py` | Build 01's agent, plus 50 fake tool schemas added to `SCHEMA` when `FLOOD=1`. |
| `run_test.py` | Runs the agent once for one question and condition, appends the run to `FLOOD_TEST_RESULTS.md` (gitignored). |
| `make_public_results.py` | Writes the public `RESULTS_BUILD3.md` from the private results. |
| `RESULTS_BUILD3.md` | Every valid run: tool calls, inputs, counts, times. The source for every number above. |
