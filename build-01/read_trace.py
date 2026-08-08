"""
read_trace.py — pretty-print traces.jsonl so it's actually readable.

Run it like:
    python3 read_trace.py
"""
import json

STEP = 0
with open("traces.jsonl") as f:
    for line in f:
        row = json.loads(line)
        kind, data = row["kind"], row["data"]

        if kind == "model_step":
            calls = [b for b in data if b.get("type") == "tool_use"]
            for c in calls:
                STEP += 1
                print(f"\n[{STEP}] Claude decided to call: {c['name']}({c.get('input', {})})")
            if not calls:
                STEP += 1
                print(f"\n[{STEP}] Claude is about to answer...")

        elif kind == "tool_call":
            preview = data["output_preview"].replace("\n", " ")[:100]
            print(f"     -> result: {preview}...")

        elif kind == "final_answer":
            print("\n" + "=" * 50)
            print("FINAL ANSWER:")
            print(data)
