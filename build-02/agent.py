"""
Build 1 — Agents From Scratch
The whole agent: a model, a loop, and three tools. No framework.

Run it like:
    python agent.py /path/to/a/repo/you/know  "What does this project do?"

Success = a file called traces.jsonl appears with a few lines in it.

BUILD 2 — DAMAGE SWITCHES
Three env vars let you break this on purpose, one thing at a time:
    BREAK_DROP_DESC=search    -> that tool's description becomes "" (blank)
    BREAK_FAIL_TOOL=read_file -> that tool always returns an error string
    BREAK_MODEL=claude-haiku-4-5 -> use this model instead of the default
Leave all three unset and it runs exactly like Build 1.
"""
import anthropic, json, os, sys

# ---- config ----
BREAK_DROP_DESC = os.environ.get("BREAK_DROP_DESC")   # tool name whose description gets blanked
BREAK_FAIL_TOOL = os.environ.get("BREAK_FAIL_TOOL")    # tool name that always errors
BREAK_MODEL     = os.environ.get("BREAK_MODEL")        # model override

MODEL = BREAK_MODEL or "claude-sonnet-5"   # found in console → Build → Workbench → model dropdown
REPO  = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
TASK  = sys.argv[2] if len(sys.argv) > 2 else "What does this project do? Name the main entry file."

client = anthropic.Anthropic()       # reads ANTHROPIC_API_KEY from your environment
trace  = open("traces.jsonl", "w")
def log(kind, data):
    trace.write(json.dumps({"kind": kind, "data": data}, default=str) + "\n"); trace.flush()

# ---- the three tools: each takes a string, returns a string ----
def list_files(_=None):
    out = []
    for root, _d, files in os.walk(REPO):
        if "/." in root or "node_modules" in root: continue
        for f in files:
            out.append(os.path.relpath(os.path.join(root, f), REPO))
    return "\n".join(out[:200]) or "empty repo"

def read_file(path):
    try:
        return open(os.path.join(REPO, path), errors="ignore").read()[:2000]
    except Exception as e:
        return f"ERROR: {e}"

def search(query):
    hits = []
    for root, _d, files in os.walk(REPO):
        if "/." in root or "node_modules" in root: continue
        for f in files:
            try:
                for i, line in enumerate(open(os.path.join(root, f), errors="ignore"), 1):
                    if query.lower() in line.lower():
                        hits.append(f"{os.path.relpath(os.path.join(root,f), REPO)}:{i}: {line.strip()[:120]}")
            except Exception: pass
    return "\n".join(hits[:40]) or "no matches"

TOOLS  = {"list_files": list_files, "read_file": read_file, "search": search}
SCHEMA = [
    {"name": "list_files", "description": "List all file paths in the repo.",
     "input_schema": {"type": "object", "properties": {}}},
    {"name": "read_file", "description": "Read one file. Pass a repo-relative path.",
     "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}},
    {"name": "search", "description": "Search the repo for a string. Returns matching lines.",
     "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
]

# damage switch 1: blank out one tool's description
if BREAK_DROP_DESC:
    for tool in SCHEMA:
        if tool["name"] == BREAK_DROP_DESC:
            tool["description"] = ""

def call_tool(name, arg):
    # damage switch 2: this tool always fails, no matter what's asked
    if BREAK_FAIL_TOOL and name == BREAK_FAIL_TOOL:
        return f"ERROR: {name} is temporarily unavailable."
    return TOOLS[name](arg)

messages = [{"role": "user", "content": TASK}]

# ==== THE LOOP — this is the entire agent ====
while True:
    resp = client.messages.create(model=MODEL, max_tokens=1024, tools=SCHEMA, messages=messages)
    log("model_step", [b.model_dump() for b in resp.content])
    messages.append({"role": "assistant", "content": resp.content})

    if resp.stop_reason == "tool_use":
        results = []
        for block in resp.content:
            if block.type == "tool_use":
                arg = (list(block.input.values())[0] if block.input else None)
                out = call_tool(block.name, arg)[:2000]        # hard truncation
                print(f"  -> agent called {block.name}({block.input})")
                log("tool_call", {"name": block.name, "input": block.input, "output_preview": out[:200]})
                results.append({"type": "tool_result", "tool_use_id": block.id, "content": out})
        messages.append({"role": "user", "content": results})
    else:
        answer = "".join(b.text for b in resp.content if b.type == "text")
        log("final_answer", answer)
        print("\n=== AGENT ANSWER ===\n" + answer)
        break

trace.close()
print("\nDone. Open traces.jsonl and read every line — that's what your agent actually did.")
