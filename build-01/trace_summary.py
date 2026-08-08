"""
trace_summary.py — one screenshot-sized view of what the agent actually did.

Prints the tool calls and whether each one was worth anything. Deliberately
prints NO file contents, so it's safe to share even when the agent was
pointed at a private repo.

Run it like:
    python3 trace_summary.py
"""
import json, os

calls = []
for line in open("traces.jsonl"):
    row = json.loads(line)
    if row["kind"] == "model_step":
        for b in row["data"]:
            if b.get("type") == "tool_use":
                arg = list(b.get("input", {}).values())
                calls.append({"name": b["name"],
                              "arg": str(arg[0]) if arg else "",
                              "out": None})
    elif row["kind"] == "tool_call":
        for c in calls:
            if c["out"] is None:
                c["out"] = row["data"]["output_preview"]
                break

def verdict(c):
    out = (c["out"] or "").strip()
    if c["name"] != "search":
        return "ok"
    if out.startswith("no matches"):
        return "no matches"
    first = out.split(":")[0]                      # filename only, never contents
    if first.endswith((".pyc", ".csv", ".lock", ".map")):
        return f"junk ({os.path.splitext(first)[1]})"
    return f"hit: {os.path.basename(first)}"

searches = [c for c in calls if c["name"] == "search"]
useful   = [c for c in searches if verdict(c).startswith("hit")]

print()
print(f"  AGENT RUN — {len(calls)} tool calls to answer one question")
print("  " + "-" * 46)
seen = set()
for i, c in enumerate(calls, 1):
    label = f'{c["name"]}({c["arg"][:22]})' if c["arg"] else f'{c["name"]}()'
    note  = verdict(c)
    key   = (c["name"], c["arg"])
    if key in seen:
        note = "same call as before"
    seen.add(key)
    print(f"  {i:>2}  {label:<34}{note}")
print("  " + "-" * 46)
print(f"  {len(searches)} searches. Only {len(useful)} found anything useful.")
print("  0 source files read. The answer was in my own docs.")
print()
