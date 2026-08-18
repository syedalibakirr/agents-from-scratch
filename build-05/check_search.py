import os, hashlib
R = os.path.expanduser("~/Desktop/Cursor - LP")

def hits(q):
    out = []
    for root, _d, files in os.walk(R):
        if "/." in root or "node_modules" in root: continue
        for x in files:
            try:
                for i, l in enumerate(open(os.path.join(root, x), errors="ignore"), 1):
                    if q.lower() in l.lower():
                        out.append(os.path.relpath(os.path.join(root, x), R) + ":" + str(i))
            except Exception: pass
    return out

for q in ["backend", "VITE_API_BASE_URL", "port"]:
    hs, n = [], 0
    for _ in range(5):
        a = hits(q)
        n = len(a)
        hs.append(hashlib.md5("\n".join(a[:40]).encode()).hexdigest()[:8])
    print(q.ljust(20), "matches=" + str(n).ljust(5), "capped=" + str(n > 40).ljust(6), "identical=" + str(len(set(hs)) == 1))
