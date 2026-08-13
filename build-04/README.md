# Build 04 — one sentence, three wordings

Garry Tan (CEO of Y Combinator) has said that "a markdown file is an employee that
will do the job perfectly every single time." This build tests a narrow version of
that claim: does rewording one sentence in a markdown file change what an agent
actually does?

The agent's three tool descriptions live in `tools.md` (moved out of `agent.py`,
which loads them at runtime via `load_descriptions()`). Everything else — the model,
the loop, the two other tool descriptions, the question, the target repo — is held
fixed. Only the `search` tool's description sentence changes, across three wordings,
and the same question is asked 20 times per wording.

## Setup

- Agent: the same loop as build-01/build-03 (`agent.py`, unchanged), reading its 3
  real tool descriptions from `tools.md` at startup.
- Model: `claude-sonnet-5`, default temperature.
- Condition: `clean` throughout (`FLOOD` unset — exactly 3 tools, no flood).
- Question (Q2 from `run_test.py`'s question list): *"What embedding model does the
  semantic search use, and what vector dimension does the column expect?"*
- Target repo: a fixed external codebase (unrelated to this repo).
- 20 runs per wording (condition B's first round of 10 had 1 crash, backfilled with
  a second round of 10 — see Limitations).

## The three conditions

Only the `## search` line in `tools.md` changes between conditions. The full text of
each wording is in `tools/`.

| Condition | File | `search` description |
|---|---|---|
| A — original | [`tools/tools_A_original.md`](./tools/tools_A_original.md) | "Search the repo for a string. Returns matching lines." |
| B — info dropped | [`tools/tools_B_info_dropped.md`](./tools/tools_B_info_dropped.md) | "Find text inside the project files." |
| C — paraphrase | [`tools/tools_C_paraphrase.md`](./tools/tools_C_paraphrase.md) | "Searches the repo for a given string and returns the matching lines." |

`tools.md` at the repo root is the file `agent.py` actually reads. To reproduce a
condition, copy the matching file over it before running (see **Reproduce** below).

## Results

Tool-call counts on Q2, per condition (from `analyze.py`):

| Condition | n | total calls | mean | min | max | >1 call | used `read_file` |
|---|---|---|---|---|---|---|---|
| A — original | 20 | 27 | 1.35 | 1 | 3 | 6/20 | 0/20 |
| B — info dropped | 19 | 41 | 2.16 | 1 | 4 | 12/19 | 6/19 |
| C — paraphrase | 20 | 43 | 2.15 | 1 | 4 | 16/20 | 3/20 |

Dropping the information in the description ("returns matching lines" →
"find text") roughly doubled the average number of tool calls and pushed the agent
to call `read_file` where it otherwise wouldn't (0/20 → 6/19). A same-meaning
paraphrase (condition C) also raised the call count and `read_file` usage relative
to A, despite carrying the same information as the original sentence.

**Fisher's exact test** (two-tailed, `math.comb`-based, no scipy), on the split of
1 tool call vs more than 1 tool call:

- A vs B: A = (14, 6), B = (7, 12) → **p = 0.056**
- A vs C: A = (14, 6), C = (4, 16) → **p = 0.004**

The paraphrase (C) — which preserves the original sentence's information — shows a
stronger, more significant shift away from 1-call runs than the info-dropped wording
(B) does, on this split and this sample size.

## Limitations

This is one question, against one model, on one codebase, with 20 runs per
condition. It is not a general law about tool descriptions — it's one repeatable
observation that a single-sentence reword changed measured behavior on this setup.
A different question, model, or codebase could show a different or absent effect.
The A-vs-B result (p = 0.056) does not clear the conventional p < 0.05 threshold;
only A-vs-C does.

One run in condition B's first round (10-run batch) failed with an Anthropic API
529 "Overloaded" error, unrelated to the experiment itself — the agent crashed
mid-run before producing a final answer. `analyze.py` excludes any run whose final
answer contains "agent crashed" or "TIMED OUT", so this run is dropped from B's
n=19 rather than counted as a 0-call or otherwise misleading data point. Condition
B was backfilled with a second 10-run batch to keep its sample size close to A and
C's 20.

## What's here

| Path | What it is |
|---|---|
| `agent.py` | The agent loop, unchanged from build-01/build-03. Reads tool descriptions from `tools.md`, reads `ANTHROPIC_API_KEY` from the environment. |
| `run_test.py` | Runs `agent.py` once for a given question/condition against the fixed target repo and appends the result to a results file. |
| `tools.md` | The tool descriptions `agent.py` actually loads at runtime. Swap in one of `tools/tools_*.md` to reproduce a condition. |
| `tools/` | The three tested wordings of `tools.md`, one per condition. |
| `runs/` | The 5 raw result batches (`A_original_round1.md`, `A_original_round2.md`, `B_info_dropped_round1.md`, `B_info_dropped_round2.md`, `C_paraphrase.md`), each a sequence of per-run sections with question, tool calls, and final answer. |
| `analyze.py` | Parses `runs/`, filters to Q2, excludes crashed/timed-out runs, and prints the stats table and Fisher's exact test above. |
| `traces.jsonl` | One sample raw trace, kept to show the trace format `agent.py` writes — not a full archive of every run. |

## Reproduce

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key"
cd build-04

# pick a condition by swapping tools.md
cp tools/tools_A_original.md tools.md      # or tools_B_info_dropped.md / tools_C_paraphrase.md

python run_test.py --q 2 --condition clean
```

`run_test.py` appends each run to `FLOOD_TEST_RESULTS.md` (the filename is a
leftover from build-03, which this script was copied from). Run it 10-20 times per
condition and rename/move the accumulated file into `runs/` to reproduce the
`runs/` naming convention used here. `run_test.py` does not grade answers — only
`analyze.py`'s tool-call counts are analyzed above; answer correctness was not
scored in this build.

```bash
python analyze.py
```

should print the results table and Fisher's exact test shown above.
