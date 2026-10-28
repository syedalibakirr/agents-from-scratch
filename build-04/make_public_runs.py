#!/usr/bin/env python3
"""
Build 04: scrub runs/ for publishing.

run_test.py records the agent's full answer for every run. Those answers
describe a private codebase, so the originals live in runs_private/
(gitignored). This script copies them into runs/ with each answer replaced
by its length. Tool calls, counts and wall times are untouched, so
analyze.py gives the same numbers on either folder. A run that crashed
keeps the words "agent crashed" so analyze.py still excludes it.

It also scrubs traces.jsonl: each tool output preview is replaced by its
length, keeping the trace format visible without the code.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(HERE, "runs_private")
OUT_DIR = os.path.join(HERE, "runs")
# The answer can contain its own ``` code blocks, so it ends at the fence that
# closes the run's section (followed by the --- separator or the end of file).
ANSWER_RE = re.compile(r"(\*\*Final answer \(verbatim\):\*\*\s*```)(.*?)(```\s*\n(?:---|\Z))", re.S)


def scrub_answer(m):
    body = m.group(2)
    if "agent crashed" in body or "TIMED OUT" in body:
        kind = "TIMED OUT" if "TIMED OUT" in body else "agent crashed"
        new = f"\n({kind}, no final answer. Error details removed.)\n"
    else:
        new = f"\n[redacted: {len(body.strip())} chars about a private codebase]\n"
    return m.group(1) + new + m.group(3)


def scrub_runs():
    for name in sorted(os.listdir(SRC_DIR)):
        if not name.endswith(".md"):
            continue
        text = open(os.path.join(SRC_DIR, name), encoding="utf-8").read()
        out = ANSWER_RE.sub(scrub_answer, text)
        open(os.path.join(OUT_DIR, name), "w", encoding="utf-8").write(out)
        print("scrubbed", name)


def scrub_trace():
    src = os.path.join(HERE, "traces_private.jsonl")
    dst = os.path.join(HERE, "traces.jsonl")
    lines = []
    for line in open(src, encoding="utf-8"):
        row = json.loads(line)
        data = row.get("data")
        if isinstance(data, dict) and isinstance(data.get("output_preview"), str):
            data["output_preview"] = f"[redacted: {len(data['output_preview'])} chars of private code]"
        if row.get("kind") == "final_answer" and isinstance(data, str):
            row["data"] = f"[redacted: {len(data)} chars about a private codebase]"
        if row.get("kind") == "model_step" and isinstance(data, list):
            for part in data:
                if part.get("type") == "text":
                    part["text"] = f"[redacted: {len(part['text'])} chars]" if len(part["text"]) > 200 else part["text"]
        lines.append(json.dumps(row))
    open(dst, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("scrubbed traces.jsonl")


if __name__ == "__main__":
    scrub_runs()
    scrub_trace()
