#!/usr/bin/env python3
"""
make_public_traces.py (Build 08)

Reads every traces/*.jsonl and writes a scrubbed copy into traces_public/.
Keeps: model, every tool call's name and inputs, and the final answer.
Removes: every tool output (file contents) and, for edit_file, the old_text and
new_text bodies, which are code from the private target repo. Only the path and
the length of each body are kept, so the edit can still be counted and located.

Usage:
    python3 make_public_traces.py
"""

import glob, json, os

TRACE_DIR = "traces"
PUBLIC_DIR = "traces_public"
CODE_FIELDS = ("old_text", "new_text", "content")


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


def redact_input(name, inp):
    if not isinstance(inp, dict):
        return inp
    out = dict(inp)
    for k in CODE_FIELDS:
        if k in out and isinstance(out[k], str):
            out[k] = f"[redacted: {len(out[k])} chars of private code]"
    return out


def scrub(path):
    lines = load_trace(path)
    model = None
    for l in lines:
        if l.get("kind") == "config":
            model = (l.get("data") or {}).get("model")
            break

    steps, counts = [], {}
    for l in lines:
        if l.get("kind") != "tool_call":
            continue
        data = l.get("data") or {}
        name = data.get("name")
        steps.append({"tool": name, "input": redact_input(name, data.get("input"))})
        counts[name] = counts.get(name, 0) + 1

    finals = [l["data"] for l in lines if l.get("kind") == "final_answer"]
    return {
        "model": model,
        "steps": steps,
        "final_answer": finals[-1] if finals else None,
        "counts": {"tool_calls": len(steps), **{f"{k}_calls": v for k, v in counts.items()}},
    }


def main():
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    n = 0
    for src in sorted(glob.glob(os.path.join(TRACE_DIR, "*.jsonl"))):
        base = os.path.basename(src)[: -len(".jsonl")]
        with open(os.path.join(PUBLIC_DIR, f"{base}.public.json"), "w") as f:
            json.dump(scrub(src), f, indent=2)
            f.write("\n")
        n += 1
    print(f"{n} file(s) written to {PUBLIC_DIR}/")


if __name__ == "__main__":
    main()
