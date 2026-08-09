#!/usr/bin/env python3
"""
Build 2 — break the agent three ways, on purpose.

Build 1 found by accident that one vague tool description wasted 5 of 6 searches.
This runs the controlled version of that experiment: same question, same repo,
four conditions. Everything is measured off traces.jsonl, so the numbers are real.

HOW TO USE
----------
1. Point TARGET_REPO below at any repo you want to ask about.
2. python break_test.py   (run from inside this build-02/ folder)
3. It prints the table you'd post, and saves build2_results.json.

It never prints file contents, so the output is safe to screenshot.
"""

import json, os, shutil, subprocess, sys, time
from collections import Counter

# ─────────────────────────── ADAPTER — EDIT THIS ───────────────────────────
AGENT       = "agent.py"                                   # lives next to this file
TRACE_FILE  = "traces.jsonl"                                # where it logs
TARGET_REPO = os.path.expanduser("~/Desktop/some-project")  # <- point this at a real repo
QUESTION    = "What does this project do, and what's the main entry file?"

def run_agent(extra_env):
    """Call the agent once. agent.py takes plain positional args: repo path, question."""
    env = {**os.environ, **extra_env}
    return subprocess.run(
        [sys.executable, AGENT, TARGET_REPO, QUESTION],
        env=env, capture_output=True, text=True, timeout=300,
    )

# agent.py honours these three env vars — that's how each condition breaks it:
#   BREAK_DROP_DESC=search   -> pass "" as that tool's description
#   BREAK_FAIL_TOOL=read_file-> that tool always returns an error string
#   BREAK_MODEL=<model-id>   -> use this model instead of the default
CHEAP_MODEL = "claude-haiku-4-5"     # whatever your cheap tier is

CONDITIONS = [
    ("baseline",        {}),
    ("no description",  {"BREAK_DROP_DESC": "search"}),
    ("read_file errors",{"BREAK_FAIL_TOOL": "read_file"}),
    ("cheap model",     {"BREAK_MODEL": CHEAP_MODEL}),
]
# ───────────────────────────────────────────────────────────────────────────


def read_trace():
    """Return only the tool_call lines from the most recent run.
    agent.py logs every line as {"kind": ..., "data": ...} — model_step and
    final_answer lines aren't tool calls, so filter to kind == "tool_call"
    and unwrap "data" to get at name/input/output_preview."""
    if not os.path.exists(TRACE_FILE):
        return []
    with open(TRACE_FILE) as f:
        lines = [json.loads(l) for l in f if l.strip()]
    return [l["data"] for l in lines if l.get("kind") == "tool_call"]


def verdict(call):
    """Classify one tool call without ever exposing file contents."""
    name = call.get("name") or "?"
    res  = call.get("output_preview") or ""
    res  = res if isinstance(res, str) else json.dumps(res)
    low  = res.lower()
    if not res.strip():                       return name, "empty"
    if "error" in low or "traceback" in low:  return name, "error"
    if "no match" in low or "not found" in low or res.strip() in ("[]", "{}"):
        return name, "no match"
    return name, "ok"


def summarize(label, calls, wall, answered):
    names   = [verdict(c)[0] for c in calls]
    results = [verdict(c)[1] for c in calls]
    searches = sum(1 for n in names if "search" in n)
    useful   = sum(1 for n, r in zip(names, results) if "search" in n and r == "ok")
    reads    = sum(1 for n in names if "read" in n)
    errors   = sum(1 for r in results if r == "error")
    return {
        "label": label, "calls": len(calls), "searches": searches,
        "useful": useful, "reads": reads, "errors": errors,
        "secs": round(wall, 1), "answered": answered,
        "most_repeated": (Counter(names).most_common(1) or [("-", 0)])[0],
    }


def main():
    rows = []
    for label, env in CONDITIONS:
        if os.path.exists(TRACE_FILE):
            shutil.move(TRACE_FILE, TRACE_FILE + ".bak")   # mv works everywhere
        print(f"running: {label} ...", flush=True)
        t0 = time.time()
        err = ""
        try:
            proc = run_agent(env)
            out  = proc.stdout
            err  = proc.stderr
        except subprocess.TimeoutExpired:
            out = ""
            print("  TIMED OUT — that is itself a finding, record it")
        wall  = time.time() - t0
        calls = read_trace()

        print(f"  {len(calls)} tool calls in {wall:.0f}s")
        if not out.strip() and err.strip():
            print("  --- CRASHED, here's the error ---")
            print("  " + err.strip()[-600:])
        else:
            print("  --- the agent's answer ---")
            print("  " + (out.strip()[-400:] or "(no output)"))
        ok = input("  Did it get the answer RIGHT? [y/n] ").strip().lower().startswith("y")
        rows.append(summarize(label, calls, wall, ok))

    w = max(len(r["label"]) for r in rows) + 2
    print("\n\nBUILD 2 — SAME QUESTION, FOUR CONDITIONS")
    print("=" * (w + 52))
    print(f"{'condition':<{w}}{'calls':>7}{'searches':>10}{'useful':>8}"
          f"{'errors':>8}{'right?':>9}")
    print("-" * (w + 52))
    for r in rows:
        print(f"{r['label']:<{w}}{r['calls']:>7}{r['searches']:>10}"
              f"{r['useful']:>8}{r['errors']:>8}{'yes' if r['answered'] else 'NO':>9}")
    print("=" * (w + 52))
    for r in rows:
        tool, n = r["most_repeated"]
        if n > 1:
            print(f"  {r['label']}: called {tool} {n}x")
    print("\nPaste these numbers into build2.html and the post.")
    json.dump(rows, open("build2_results.json", "w"), indent=2)
    print("Also saved: build2_results.json")


if __name__ == "__main__":
    main()
