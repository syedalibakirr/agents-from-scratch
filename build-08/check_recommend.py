#!/usr/bin/env python3
"""
Build 8 test: does the website's college-suggestions call reach a real backend door?

It only READS files as text. It never starts a server and never runs Triptic code.

Usage:  python check_recommend.py <path-to-triptic-copy>

Three checks:
  1. Every backend address that suggestions.ts calls must exist in the backend.
  2. The backend must have exactly ONE door for college recommendations.
     (A second door that forwards a wrong address is a workaround, not a fix.)
  3. Every recommendation call must send the package the backend expects:
     the backend's RecommendRequest requires a "student_profile" field.
     (Right address + wrong package = 422 error, still broken.)
"""
import os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
CLIENT  = os.path.join(root, "client/src/services/college/suggestions.ts")
BACKEND = os.path.join(root, "python-backend")

# --- what the website calls ---
client_src = open(CLIENT, errors="ignore").read()
called = sorted(set(re.findall(r'}(/api/[\w/\-]+)', client_src)))

# --- what the backend serves ---
served = []   # (method, path, file)
route = re.compile(r'@(\w+)\.(get|post|put|patch|delete|api_route)\(\s*["\']([^"\']+)["\']')
for dirpath, dirnames, files in os.walk(BACKEND):
    dirnames[:] = [d for d in dirnames if d not in ("venv", ".venv", "__pycache__", "node_modules")]
    for f in files:
        if not f.endswith(".py"):
            continue
        p = os.path.join(dirpath, f)
        for obj, method, path in route.findall(open(p, errors="ignore").read()):
            full = path if obj == "app" else "/api" + path     # routers are mounted under /api in app.py
            served.append((method.upper(), full, os.path.relpath(p, root)))
served_paths = {s[1] for s in served}

failures = []
print(f"website calls: {called or 'nothing found'}")
for path in called:
    if path in served_paths:
        print(f"  PASS  {path} exists in the backend")
    else:
        failures.append(f"{path} is called by suggestions.ts but no backend route serves it (404)")
        print(f"  FAIL  {path} is not served by the backend (this is the 404)")

recommend_doors = [s for s in served if "recommend" in s[1]]
print(f"backend recommendation doors: {[d[1] for d in recommend_doors]}")
if len(recommend_doors) == 1:
    print("  PASS  exactly one recommendation door")
else:
    failures.append(f"expected 1 recommendation route, found {len(recommend_doors)}: {[d[1] for d in recommend_doors]}")
    print(f"  FAIL  {len(recommend_doors)} recommendation doors (expected 1)")

# --- check 3: the package (request body) ---
calls = [m.start() for m in re.finditer(r'}/api/[\w/\-]*recommend', client_src)]
for i, pos in enumerate(calls, 1):
    window = client_src[pos:pos + 800]            # the fetch(...) options that follow the address
    body = window[window.find("body"):] if "body" in window else ""
    if "student_profile" in body[:400]:
        print(f"  PASS  recommendation call {i} sends student_profile")
    else:
        failures.append(f"recommendation call {i} in suggestions.ts does not send student_profile (backend returns 422)")
        print(f"  FAIL  recommendation call {i} sends the wrong package (backend expects student_profile)")

print()
if failures:
    print(f"TESTS FAILED ({len(failures)})")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print("ALL TESTS PASSED")
