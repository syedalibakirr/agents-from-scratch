#!/usr/bin/env python3
"""
make_public_traces.py

Reads every traces/*.jsonl and writes a scrubbed copy into traces_public/,
same filename with a .public.json extension. Keeps only what's needed to
verify the boundary-violation, hallucinated-file, and refusal claims: tool
names, the arguments passed to them, and the final answer. Strips every
output_preview field (and anything else carrying file contents) completely.

Usage:
    python3 make_public_traces.py
"""

import glob, json, os

TRACE_DIR = "traces"
PUBLIC_DIR = "traces_public"


def load_trace(path):
    lines = []
    with open(path) as f:
        for raw in f:
            raw = raw.strip()
            if not raw:
                continue
            try:
                lines.append(json.loads(raw))
            except json.JSONDecodeError:
                continue
    return lines


def scrub(path):
    lines = load_trace(path)

    model = None
    for l in lines:
        if l.get("kind") == "config":
            model = (l.get("data") or {}).get("model")
            break

    steps = []
    n_read_file = 0
    n_search = 0
    for l in lines:
        if l.get("kind") != "tool_call":
            continue
        data = l.get("data") or {}
        name = data.get("name")
        steps.append({"tool": name, "input": data.get("input")})
        if name == "read_file":
            n_read_file += 1
        elif name == "search":
            n_search += 1

    final_answer_lines = [l["data"] for l in lines if l.get("kind") == "final_answer"]
    final_answer = final_answer_lines[-1] if final_answer_lines else None

    return {
        "model": model,
        "steps": steps,
        "final_answer": final_answer,
        "counts": {
            "tool_calls": len(steps),
            "read_file_calls": n_read_file,
            "search_calls": n_search,
        },
    }


def main():
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    src_paths = sorted(glob.glob(os.path.join(TRACE_DIR, "*.jsonl")))

    n_written = 0
    for src in src_paths:
        scrubbed = scrub(src)
        base = os.path.basename(src)
        stem = base[:-len(".jsonl")] if base.endswith(".jsonl") else base
        dest = os.path.join(PUBLIC_DIR, f"{stem}.public.json")
        with open(dest, "w") as f:
            json.dump(scrubbed, f, indent=2)
            f.write("\n")
        n_written += 1

    print(f"{n_written} file(s) written to {PUBLIC_DIR}/")


if __name__ == "__main__":
    main()
