"""
Build 7 - Hands, a wall, and a watcher.

Same loop as Builds 1-6. What is new:
  1. HANDS: an edit_file tool, so the agent can change or create files.
  2. WALL:  set WALL=1 and edit_file refuses any path outside python-backend/.
(The WATCHER lives in run_test.py. It checks the disk after each run.)

Run it like:
    python agent.py /path/to/workspace "the task"
    WALL=1 python agent.py /path/to/workspace "the task"
"""
import anthropic, json, os, sys

# ---- config ----
MODEL     = os.environ.get("MODEL", "claude-sonnet-5-5")   # which brain
REPO      = os.path.realpath(sys.argv[1] if len(sys.argv) > 1 else ".")   # the folder it works in
TASK      = sys.argv[2] if len(sys.argv) > 2 else "What does this project do?"
WALL      = os.environ.get("WALL")                          # WALL=1 turns the wall on
ALLOWED   = "python-backend"                                # the only folder the wall lets through
MAX_STEPS = 40                                              # safety cap: a confused run can't loop forever

client = anthropic.Anthropic()        # reads ANTHROPIC_API_KEY from your environment, never from code
trace  = open(os.environ.get("TRACE", "traces.jsonl"), "w")
def log(kind, data):                  # one line in the diary per event
    trace.write(json.dumps({"kind": kind, "data": data}, default=str) + "\n"); trace.flush()
log("config", {"model": MODEL, "wall": bool(WALL)})

def skip(root):                       # ignore hidden folders and downloaded libraries
    return "/." in root or "node_modules" in root

# ---- EYES: the three read-only tools from Builds 1-6 ----
def list_files():
    out = []
    for root, _d, files in os.walk(REPO):
        if skip(root): continue
        for f in files:
            out.append(os.path.relpath(os.path.join(root, f), REPO))
    return "\n".join(out[:300]) or "empty repo"

def read_file(path, start_line=1):    # now reads 150 lines at a time, with line numbers
    try:
        lines = open(os.path.join(REPO, path), errors="ignore").read().splitlines()
    except Exception as e:
        return f"ERROR: {e}"
    start = max(1, int(start_line))
    chunk = lines[start - 1:start - 1 + 150]
    body = "\n".join(f"{i}: {l}" for i, l in enumerate(chunk, start))
    return f"{path} ({len(lines)} lines total, showing {start}-{start + len(chunk) - 1})\n{body}"

def search(query):
    hits = []
    for root, _d, files in os.walk(REPO):
        if skip(root): continue
        for f in files:
            try:
                for i, line in enumerate(open(os.path.join(root, f), errors="ignore"), 1):
                    if query.lower() in line.lower():
                        hits.append(f"{os.path.relpath(os.path.join(root, f), REPO)}:{i}: {line.strip()[:120]}")
            except Exception: pass
    return "\n".join(hits[:40]) or "no matches"

# ---- HANDS: the one new tool ----
def inside(full, folder):             # is this path inside that folder?
    return full == folder or full.startswith(folder + os.sep)

def edit_file(path, old_text, new_text):
    full = os.path.realpath(os.path.join(REPO, path))   # realpath turns tricks like ../../ into the true address

    # SAFETY NET, always on: never write outside the workspace copy
    if not inside(full, REPO):
        log("write_attempt", {"path": path, "result": "outside_workspace"})
        return "ERROR: that path is outside the project."

    # THE WALL, only when WALL=1
    if WALL and not inside(full, os.path.join(REPO, ALLOWED)):
        log("write_attempt", {"path": path, "result": "blocked_by_wall"})
        return f"BLOCKED: you may only change files inside {ALLOWED}/."

    # create a new file
    if old_text == "":
        if os.path.exists(full):
            return "ERROR: file already exists. To change it, pass the exact text to replace as old_text."
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, "w").write(new_text)
        log("write_attempt", {"path": path, "result": "created"})
        return f"OK: created {path}"

    # change an existing file: old_text must appear exactly once
    try:
        text = open(full, errors="ignore").read()
    except Exception as e:
        return f"ERROR: {e}"
    n = text.count(old_text)
    if n != 1:
        log("write_attempt", {"path": path, "result": f"old_text_found_{n}_times"})
        return f"ERROR: old_text must appear exactly once in {path}; it appears {n} times."
    open(full, "w").write(text.replace(old_text, new_text, 1))
    log("write_attempt", {"path": path, "result": "edited"})
    return f"OK: edited {path}"

# ---- the menu Claude sees (descriptions live in tools.md) ----
def load_descriptions(path="tools.md"):
    here = os.path.dirname(os.path.abspath(__file__))
    text = open(os.path.join(here, path), encoding="utf-8").read()
    out, name = {}, None
    for line in text.splitlines():
        if line.startswith("## "):
            name = line[3:].strip(); out[name] = ""
        elif name and line.strip():
            out[name] = (out[name] + " " + line.strip()).strip()
    return out

DESC = load_descriptions()
log("tool_descriptions", DESC)

TOOLS  = {"list_files": list_files, "read_file": read_file, "search": search, "edit_file": edit_file}
SCHEMA = [
    {"name": "list_files", "description": DESC["list_files"],
     "input_schema": {"type": "object", "properties": {}}},
    {"name": "read_file", "description": DESC["read_file"],
     "input_schema": {"type": "object", "properties": {"path": {"type": "string"}, "start_line": {"type": "integer"}}, "required": ["path"]}},
    {"name": "search", "description": DESC["search"],
     "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
    {"name": "edit_file", "description": DESC["edit_file"],
     "input_schema": {"type": "object", "properties": {"path": {"type": "string"}, "old_text": {"type": "string"}, "new_text": {"type": "string"}}, "required": ["path", "old_text", "new_text"]}},
]

def call_tool(name, inp):             # now passes ALL inputs, not just the first one
    if name not in TOOLS:
        return f"ERROR: {name} is not available."
    try:
        return TOOLS[name](**(inp or {}))
    except TypeError as e:
        return f"ERROR: bad input for {name}: {e}"

messages = [{"role": "user", "content": TASK}]

def with_cache(msgs):
    """Mark the newest message as a cache point. Everything up to it gets saved on
    Anthropic's side, so the next step re-reads it at ~10% of the price instead of 100%."""
    last = dict(msgs[-1])
    content = last["content"]
    if isinstance(content, str):
        content = [{"type": "text", "text": content}]
    content = [dict(b) for b in content]
    content[-1]["cache_control"] = {"type": "ephemeral"}
    last["content"] = content
    return msgs[:-1] + [last]

# ==== THE LOOP - still the entire agent ====
steps = 0
while True:
    steps += 1
    if steps > MAX_STEPS:
        log("final_answer", "(stopped: hit MAX_STEPS)")
        print("Stopped: too many steps."); break
    resp = client.messages.create(model=MODEL, max_tokens=4096, tools=SCHEMA, messages=with_cache(messages))
    log("model_step", [b.model_dump() for b in resp.content])
    log("usage", resp.usage.model_dump())
    messages.append({"role": "assistant", "content": resp.content})

    if resp.stop_reason == "tool_use":
        results = []
        for block in resp.content:
            if block.type == "tool_use":
                out = call_tool(block.name, block.input)[:12000]
                print(f"  -> {block.name}({str(block.input)[:100]})")
                log("tool_call", {"name": block.name, "input": block.input, "output_preview": out[:200]})
                results.append({"type": "tool_result", "tool_use_id": block.id, "content": out})
        messages.append({"role": "user", "content": results})
    else:
        answer = "".join(b.text for b in resp.content if b.type == "text")
        log("final_answer", answer)
        print("\n=== AGENT ANSWER ===\n" + answer)
        break

trace.close()
