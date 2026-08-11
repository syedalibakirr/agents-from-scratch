# Build 03 — The flood test

arXiv 2608.06370 ("The Bitter Lesson of Tool Calling") reports that JSON tool calling
degrades under context clutter — a ~2.3% drop, 11/14 → 13/14 on BFCL v4 depending on
fan-out. This build tests that on the Build 1 agent directly: does padding its tool list
with 50 fake, never-callable tools change how it uses its 3 real ones?

## What's here

| File | What it does |
|---|---|
| `agent.py` | Build 1's agent, unchanged, plus one additive block: 50 fake tool schemas appended to `SCHEMA` when `FLOOD=1`. Fakes are never callable — calling one logs the attempt and returns an error. |
| `run_test.py` | Runs `agent.py` once for one of 8 hardcoded questions against a fixed target repo, under `clean` or `flood`, and appends the result to `FLOOD_TEST_RESULTS.md` |
| `FLOOD_TEST_RESULTS.md` | Created on first run; accumulates every run's question, condition, answer, tool calls, and fake-tool attempts |

## Run it

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key"
cd build-03
python run_test.py --q 1 --condition clean
python run_test.py --q 1 --condition flood
```

Repeat for `--q 1` through `--q 8`, both conditions — 16 runs total. `run_test.py` does
not grade the answers; it only records what happened. Correctness is judged separately,
against an answer key, by a human.

## The two conditions

- `clean` — `FLOOD` unset. The model sees exactly 3 tools: `list_files`, `read_file`,
  `search`. Identical to Build 1's agent.
- `flood` — `FLOOD=1`. The model sees those same 3 tools plus 50 fake ones
  (`query_database`, `send_email`, `resize_image`, etc.) with realistic names,
  descriptions, and parameter schemas. None of the 50 do anything — if the model calls
  one, `agent.py` logs a `fake_tool_attempt` trace line and returns
  `"ERROR: <name> is not available."` as the tool result.

Nothing else changes between conditions: same model (`claude-sonnet-5`), same
temperature (default), same prompts, same target repo, same question. The only variable
is the length of the tool list.

## What's measured

Per run, `FLOOD_TEST_RESULTS.md` records: the question, the condition, wall time, total
tool call count, the ordered list of tools called (with inputs), any fake-tool attempts,
and the agent's final answer verbatim. Compare `clean` vs `flood` per question to see
whether call count, tool choice, or answer quality shifts.

Note: the runner overwrites traces.jsonl per run, so only the final
run's raw trace survives. Full tool-call sequences for all 19 runs are
recorded in FLOOD_TEST_RESULTS.md.