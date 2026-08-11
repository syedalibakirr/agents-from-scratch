#!/usr/bin/env python3
"""
Build 3 — the flood test runner.

Runs agent.py once against a fixed target repo and a fixed question (chosen by
number), under one of two conditions:
    clean  -> the real 3-tool list only (FLOOD unset)
    flood  -> the real 3 tools plus 50 fake, never-callable tools (FLOOD=1)

Appends one section per run to FLOOD_TEST_RESULTS.md: question, condition, the
agent's final answer verbatim, tool call count, tools called in order, and any
fake-tool attempts. Does not grade or judge correctness — that's for a human
with an answer key.

Usage:
    python run_test.py --q 2 --condition clean
    python run_test.py --q 2 --condition flood
"""

import argparse, json, os, shutil, subprocess, sys, time

AGENT       = "agent.py"                                     # lives next to this file
TRACE_FILE  = "traces.jsonl"                                  # written to cwd by agent.py
RESULTS_FILE = "FLOOD_TEST_RESULTS.md"
TARGET_REPO = os.path.expanduser("~/Desktop/Cursor - LP")

QUESTIONS = {
    1: "Which of these three folders is the live backend: server, python-backend, or triptic-backend?",
    2: "What embedding model does the semantic search use, and what vector dimension does the column expect?",
    3: "Which file triggers Google OAuth sign-in?",
    4: "Is the Supabase session stored in localStorage or sessionStorage?",
    5: "What access does fix_chat_upload_permissions.sql grant on the chat-attachments bucket?",
    6: "Which file calls the Anthropic API?",
    7: "What is the timeout, in seconds, on the Anthropic HTTP call?",
    8: "What is the name of the BroadcastChannel used to sync auth across tabs?",
}


def run_agent(question, flood):
    env = {**os.environ}
    if flood:
        env["FLOOD"] = "1"
    else:
        env.pop("FLOOD", None)
    return subprocess.run(
        [sys.executable, AGENT, TARGET_REPO, question],
        env=env, capture_output=True, text=True, timeout=300,
    )


def read_trace():
    if not os.path.exists(TRACE_FILE):
        return []
    with open(TRACE_FILE) as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    parser = argparse.ArgumentParser(description="Run the flood test agent once.")
    parser.add_argument("--q", type=int, required=True, choices=sorted(QUESTIONS),
                         help="question number, 1-8")
    parser.add_argument("--condition", required=True, choices=["clean", "flood"],
                         help="clean = 3 real tools only; flood = 3 real + 50 fake tools")
    args = parser.parse_args()

    question = QUESTIONS[args.q]
    flood = args.condition == "flood"

    if os.path.exists(TRACE_FILE):
        shutil.move(TRACE_FILE, TRACE_FILE + ".bak")

    print(f"running: q{args.q} [{args.condition}] ...", flush=True)
    t0 = time.time()
    timed_out = False
    try:
        proc = run_agent(question, flood)
        stdout, stderr = proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        stdout, stderr = "", ""
        timed_out = True
    wall = time.time() - t0

    lines = read_trace()
    tool_calls = [l["data"] for l in lines if l.get("kind") == "tool_call"]
    fake_attempts = [l["data"] for l in lines if l.get("kind") == "fake_tool_attempt"]
    final_answer_lines = [l["data"] for l in lines if l.get("kind") == "final_answer"]
    final_answer = final_answer_lines[-1] if final_answer_lines else ""

    if timed_out:
        final_answer = "(TIMED OUT after 300s — no final answer)"
    elif not final_answer and stderr.strip():
        final_answer = f"(agent crashed, no final answer — stderr tail:\n{stderr.strip()[-800:]})"

    tools_called_in_order = [f'{c.get("name")}({json.dumps(c.get("input"))})' for c in tool_calls]

    section = []
    section.append(f"## Q{args.q} — {args.condition}\n")
    section.append(f"**Question:** {question}\n")
    section.append(f"**Condition:** {args.condition} ({'FLOOD=1, 53 tools' if flood else 'FLOOD unset, 3 tools'})\n")
    section.append(f"**Wall time:** {wall:.1f}s\n")
    section.append(f"**Tool call count:** {len(tool_calls)}\n")
    section.append("**Tools called, in order:**")
    if tools_called_in_order:
        section.append("```")
        section.extend(tools_called_in_order)
        section.append("```")
    else:
        section.append("(none)")
    section.append("\n**Fake-tool attempts:**")
    if fake_attempts:
        section.append("```")
        for a in fake_attempts:
            section.append(f'{a.get("name")}({json.dumps(a.get("input"))})')
        section.append("```")
    else:
        section.append("(none)")
    section.append("\n**Final answer (verbatim):**")
    section.append("```")
    section.append(final_answer)
    section.append("```")
    section.append("\n---\n")

    is_new = not os.path.exists(RESULTS_FILE)
    with open(RESULTS_FILE, "a") as f:
        if is_new:
            f.write("# Flood Test Results\n\n")
            f.write(
                "Comparing the same 3-tool agent under two conditions: `clean` (3 real tools) "
                "vs `flood` (3 real tools + 50 fake, never-callable tools). No grading here — "
                "just what the agent called and what it said.\n\n---\n\n"
            )
        f.write("\n".join(section) + "\n")

    print(f"  {len(tool_calls)} tool calls, {len(fake_attempts)} fake-tool attempts, {wall:.1f}s")
    print(f"  appended to {RESULTS_FILE}")


if __name__ == "__main__":
    main()
