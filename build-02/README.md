# Build 02 — Break it on purpose

Build 1 found, by accident, that one vague tool description wasted 5 of 6 searches.
This build runs the controlled version of that experiment: same question, same repo,
same 3-tool agent from Build 1 — plus three switches to damage it on purpose, one at
a time.

## What's here

| File | What it does |
|---|---|
| `agent.py` | Build 1's agent, with three env-var damage switches added (`BREAK_DROP_DESC`, `BREAK_FAIL_TOOL`, `BREAK_MODEL`) |
| `break_test.py` | Runs the agent 4 times — once clean, three times broken — and scores each run off `traces.jsonl` |
| `build2_results.json` | The real output from one run of this experiment |

## Run it

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key"
cd build-02
python3 break_test.py    # edit TARGET_REPO inside first
```

It'll ask you, after each of the 4 runs, whether the agent's answer was actually
correct — that's a judgment only you can make about your own repo.

## The three damage switches, in plain terms

- `BREAK_DROP_DESC=search` — blanks out one tool's description. The model never sees
  your code, only the one sentence describing each tool — delete it and the model is
  guessing what the tool is for.
- `BREAK_FAIL_TOOL=read_file` — that tool always returns an error, no matter what.
- `BREAK_MODEL=claude-haiku-4-5` — swaps in a cheaper model, nothing else touched.

## What one run found

| condition | tool calls | seconds | useful searches | right? |
|---|---|---|---|---|
| nothing changed (control) | 11 | 24 | 3/4 | yes |
| no tool description | 10 | 31 | 1/3 | **no** |
| read_file always errors | 33 | 70 | 18/20 | yes |
| cheapest model | 8 | 13 | 1/1 | **no** |

The cheapest, fastest run was wrong. The slowest, most expensive run was right.
Call count and speed said nothing about correctness, in either direction.

Deleting one tool description didn't make the agent work harder — it made it work
*less* (fewer useful searches) and land on a wrong answer with no error anywhere in
the log. Breaking a tool outright didn't stop the agent at all — it just tripled the
cost to route around the damage. The cheap model didn't fail loudly — it answered
half the question and stopped, confidently incomplete.

## Known limit

One run per condition. These models aren't deterministic — a repeat run of the exact
same "nothing changed" condition won't always produce the exact same trace. Three runs
per condition is the statistically honest version of this experiment. That's a later
build's problem.

## Lessons carried into Build 3

- A tool description isn't documentation — it's the tool's entire interface to the model.
- A high retry count means the agent is struggling. It does not mean the final answer is wrong.
- A crash is a gift. Silence — a confident, wrong, or incomplete answer with no error — is the expensive failure mode.
