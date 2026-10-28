# Build 04: one sentence, three wordings

Change one sentence in a tool's description, keep everything else fixed, and ask
the same question 20 times per wording. Does the agent behave differently?

It did. A rewording that kept the exact same meaning moved the agent from mostly
one tool call to mostly several (14 of 20 runs used one call before, 4 of 20 after,
p = 0.004). Dropping information from the sentence moved it in the same direction,
but less clearly (p = 0.056).

The prompt for this build was a line attributed to Garry Tan (CEO of Y Combinator),
that "a markdown file is an employee that will do the job perfectly every single
time." This tests a narrow version of it: does the wording of one sentence in a
markdown file change what an agent does?

## The setup

The agent's three tool descriptions now live in `tools.md`, which `agent.py` loads
at startup. Only the `search` tool's sentence changes:

| Condition | `search` description | File |
|---|---|---|
| A, original | "Search the repo for a string. Returns matching lines." | [`tools/tools_A_original.md`](./tools/tools_A_original.md) |
| B, information dropped | "Find text inside the project files." | [`tools/tools_B_info_dropped.md`](./tools/tools_B_info_dropped.md) |
| C, same meaning reworded | "Searches the repo for a given string and returns the matching lines." | [`tools/tools_C_paraphrase.md`](./tools/tools_C_paraphrase.md) |

Held fixed: the loop (Build 03's agent, `clean` condition, 3 tools), the other two
tool descriptions, the target (a private production codebase, Triptic), and the
question, Q2 from Build 03:

> What embedding model does the semantic search use, and what vector dimension does
> the column expect?

Model: `claude-sonnet-5`, default temperature (no `temperature` is passed anywhere).
20 runs per wording.

## Results

Numbers come from `analyze.py`, which reads every run in [`runs/`](./runs).

| Condition | Runs | Total tool calls | Mean | Min | Max | More than 1 call | Used `read_file` |
|---|---|---|---|---|---|---|---|
| A, original | 20 | 27 | 1.35 | 1 | 3 | 6 of 20 | 0 of 20 |
| B, information dropped | 19 | 41 | 2.16 | 1 | 4 | 12 of 19 | 6 of 19 |
| C, same meaning reworded | 20 | 43 | 2.15 | 1 | 4 | 16 of 20 | 3 of 20 |

What happened:

- **Original wording.** The agent usually searched once and answered. It never
  opened a file.
- **Information dropped.** "Returns matching lines" became "find text". Average
  calls went from 1.35 to 2.16, and 6 of 19 runs started opening files with
  `read_file`, which no run did before.
- **Same meaning, different words.** The sentence carried the same information as
  the original, and the shift was larger: 16 of 20 runs made more than one call.

The model does not read your intent. It reads the sentence, and two sentences that
mean the same thing to a person can produce measurably different behaviour.

## Statistics, stated plainly

Fisher's exact test, two-tailed, on runs with 1 call versus more than 1 call
(implemented with `math.comb`, no scipy):

- A vs B: A = (14, 6), B = (7, 12), p = 0.056. Not below 0.05.
- A vs C: A = (14, 6), C = (4, 16), p = 0.004.

## Limitations

- One question, one model, one codebase, 20 runs per wording. This is one
  repeatable observation, not a rule about tool descriptions.
- Answer correctness was not scored; only tool-call behaviour was.
- One run in B crashed with an Anthropic 529 "Overloaded" error before answering.
  `analyze.py` excludes crashed and timed-out runs, so B has 19. B was backfilled
  with a second batch of 10 to keep it close to 20.
- `runs/B_info_dropped_round1.md` also contains 10 runs of a different question
  (Q8); `analyze.py` counts Q2 only.

## Traces and privacy

The target is a private codebase. The original run files, with the agent's full
answers, are kept in `runs_private/` (gitignored). `make_public_runs.py` copies them
into `runs/` with each answer replaced by its length. Tool calls, counts and wall
times are unchanged, so `analyze.py` prints the same numbers on either folder.
`traces.jsonl` is one sample trace kept to show the format, with tool outputs and
the answer replaced by their length.

## How to reproduce

You need your own target repo; the codebase used here is private.

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-api-key-here"   # placeholder, never commit a real key

cd build-04
cp tools/tools_A_original.md tools.md      # or tools_B_info_dropped.md / tools_C_paraphrase.md
python run_test.py --q 2 --condition clean # run 20 times per wording
```

`run_test.py` appends each run to `FLOOD_TEST_RESULTS.md` (the name is left over
from Build 03). Move each batch into `runs_private/` with the naming used in
`analyze.py`, then:

```bash
python make_public_runs.py
python analyze.py
```

## What's here

| Path | What it is |
|---|---|
| `agent.py` | The Build 03 loop, reading its tool descriptions from `tools.md`. |
| `tools.md` | The descriptions `agent.py` loads. Copy one of `tools/` over it to pick a wording. |
| `tools/` | The three tested wordings. |
| `run_test.py` | Runs the agent once and appends the run to a results file. |
| `runs/` | The 5 run batches, answers redacted. |
| `analyze.py` | Reads `runs/`, keeps Q2, drops crashed runs, prints the table and Fisher tests above. |
| `make_public_runs.py` | Writes the redacted `runs/` and `traces.jsonl` from the private originals. |
| `traces.jsonl` | One sample trace, outputs redacted, to show the trace format. |
