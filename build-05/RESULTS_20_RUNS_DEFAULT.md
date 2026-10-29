# 20 Runs, API Default Temperature

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Target repo:** Triptic's private codebase (the working repo; builds moved to copies from Build 07 on), fixed across all 20 runs.

**Model:** `claude-sonnet-5`

**Runs:** 20, condition `clean` (3 real tools, no flood), question Q1 only.

**Temperature:** API default (1.0). No `temperature` parameter was passed to `client.messages.create()` for these runs — `agent.py`'s `TEMP` env var was unset, so `float(os.environ.get("TEMP", "1.0"))` fell through to its default. A separate 20-run batch at an explicit `temperature=0` was attempted and is not included here — every one of those 20 calls raised `anthropic.BadRequestError: temperature is deprecated for this model` before a single tool call was made. See `README.md` for that finding.

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 23

**Tools called, in order:**
```
list_files({})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
search({"query": "server/                "})
search({"query": "deploy"})
read_file({"path": "triptic-backend/main.py"})
list_files({})
read_file({"path": "triptic-backend/railway.json"})
search({"query": "VITE_API_URL"})
search({"query": "server/index"})
search({"query": "render.com"})
search({"query": "API_BASE_URL"})
search({"query": "import.meta.env.VITE_API"})
read_file({"path": "README.md"})
read_file({"path": "python-backend/main.py"})
search({"query": "server/"})
read_file({"path": "python-backend/README.md"})
search({"query": "triptic-backend"})
search({"query": "\"scripts\""})
read_file({"path": "package-lock.json"})
read_file({"path": "server/package.json"})
search({"query": "deprecated"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1378 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 7

**Tools called, in order:**
```
list_files({})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
search({"query": "server"})
read_file({"path": "CLAUDE.md"})
search({"query": "NEXT_PUBLIC_API"})
search({"query": "localhost:8000"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1289 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 8

**Tools called, in order:**
```
list_files({})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
search({"query": "server/"})
read_file({"path": "triptic-backend/main.py"})
read_file({"path": "python-backend/README.md"})
list_files({})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1310 chars about a private codebase]
Named as the live backend: server
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 16

**Tools called, in order:**
```
list_files({})
search({"query": "server"})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
list_files({})
search({"query": "render.com"})
search({"query": "deploy"})
search({"query": "VITE_API"})
read_file({"path": ".env.local"})
list_files({})
read_file({"path": "python-backend/main.py"})
read_file({"path": "triptic-backend/main.py"})
read_file({"path": "python-backend/app.py"})
search({"query": "railway"})
search({"query": "python-backend/"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1559 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 16

**Tools called, in order:**
```
list_files({})
search({"query": "server"})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
read_file({"path": ".env.local"})
list_files({})
search({"query": "python-backend/"})
search({"query": "render.com"})
search({"query": "VITE_API"})
read_file({"path": "python-backend/main.py"})
read_file({"path": "triptic-backend/main.py"})
read_file({"path": "server/src/server.tsx"})
read_file({"path": "python-backend/app.py"})
search({"query": "\"scripts\""})
read_file({"path": "README.md"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1675 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 17

**Tools called, in order:**
```
list_files({})
search({"query": "server"})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
list_files({})
read_file({"path": "CLAUDE.md"})
search({"query": "render.com"})
search({"query": "VITE_API"})
search({"query": "deprecated"})
read_file({"path": "triptic-backend/main.py"})
search({"query": "python-backend/api/routes.py"})
search({"query": "/api/counselor/research/history"})
search({"query": "server/src/routes"})
read_file({"path": "README.md"})
read_file({"path": "python-backend"})
list_files({})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1333 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 46

**Tools called, in order:**
```
list_files({})
read_file({"path": "CLAUDE.md"})
read_file({"path": "README.md"})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
search({"query": "server/"})
search({"query": "deploy"})
list_files({})
read_file({"path": "triptic-backend/main.py"})
read_file({"path": "python-backend/README.md"})
search({"query": "VITE_API"})
search({"query": "railway.app"})
read_file({"path": "triptic-backend/railway.json"})
read_file({"path": ".env.local"})
search({"query": "VITE_API_BASE_URL="})
list_files({})
search({"query": "Node.js backend"})
search({"query": "FastAPI AI backend"})
search({"query": "legacy"})
list_files({})
search({"query": "server/index"})
search({"query": "server/package.json"})
search({"query": "\"server/src\""})
search({"query": "express"})
read_file({"path": "server/src/server.tsx"})
read_file({"path": "server/package.json"})
list_files({})
search({"query": "match_score"})
search({"query": "ai_search"})
read_file({"path": "triptic-backend/routes/ai_search.py"})
read_file({"path": "triptic-backend/routes/match_score.py"})
read_file({"path": "triptic-backend/routes/verification.py"})
search({"query": "ai-search"})
search({"query": "match-score"})
search({"query": "send-verification-email"})
search({"query": "railway.json"})
search({"query": "Procfile"})
search({"query": "Dockerfile"})
read_file({"path": "triptic-backend"})
search({"query": "triptic-backend/"})
search({"query": "FROM python"})
search({"query": "requirements.txt"})
search({"query": "server/                            \u2190"})
search({"query": "\u251c\u2500\u2500 server"})
search({"query": "\u251c\u2500\u2500 triptic-backend"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1445 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 14

**Tools called, in order:**
```
list_files({})
search({"query": "triptic-backend"})
search({"query": "python-backend"})
read_file({"path": "CLAUDE.md"})
search({"query": "server/"})
read_file({"path": "triptic-backend/main.py"})
read_file({"path": "python-backend/README.md"})
search({"query": "triptic-backend"})
search({"query": "\"server\""})
read_file({"path": "README.md"})
read_file({"path": "docs/architecture/MIGRATION_SUMMARY.md"})
search({"query": "deploy"})
read_file({"path": "python-backend/main.py"})
search({"query": "VITE_API"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1456 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 23

**Tools called, in order:**
```
list_files({})
search({"query": "server"})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
list_files({})
search({"query": "server/"})
search({"query": "Render"})
search({"query": "deploy"})
list_files({})
search({"query": "VITE_API"})
search({"query": "railway.app"})
read_file({"path": "triptic-backend/main.py"})
read_file({"path": "triptic-backend/railway.json"})
read_file({"path": "python-backend/main.py"})
read_file({"path": "python-backend/README.md"})
search({"query": "python-backend/                  \u2190 FastAPI"})
read_file({"path": "CLAUDE.md"})
search({"query": "python-backend/"})
search({"query": "server/                            \u2190"})
search({"query": "triptic-backend"})
list_files({})
search({"query": "match_score"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1708 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 10

**Tools called, in order:**
```
list_files({})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
search({"query": "server/"})
read_file({"path": "CLAUDE.md"})
read_file({"path": "triptic-backend/main.py"})
search({"query": "server"})
list_files({})
list_files({})
read_file({"path": "server/src/server.tsx"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1394 chars about a private codebase]
Named as the live backend: server
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 15

**Tools called, in order:**
```
list_files({})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
search({"query": "server/"})
read_file({"path": "database/analysis/MIGRATION_PLAN.md"})
read_file({"path": "triptic-backend/main.py"})
search({"query": "render.yaml"})
search({"query": "triptic.ai"})
read_file({"path": "CLAUDE.md"})
search({"query": "Render"})
search({"query": "Deployment"})
read_file({"path": "python-backend/main.py"})
search({"query": "VITE_API"})
search({"query": "onrender.com"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1728 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 27

**Tools called, in order:**
```
list_files({})
search({"query": "server"})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
list_files({})
search({"query": "FastAPI AI backend"})
search({"query": "Backend Server for UniVerse"})
read_file({"path": "triptic-backend/main.py"})
search({"query": "VITE_API_URL"})
search({"query": "render.yaml"})
search({"query": "python-backend/api/routes.py"})
list_files({})
search({"query": "triptic-backend"})
search({"query": "client/src/lib/api"})
search({"query": "match_score"})
search({"query": "import uvicorn"})
read_file({"path": "python-backend/app.py"})
search({"query": "\u251c\u2500\u2500 server"})
read_file({"path": "python-backend/README.md"})
search({"query": "2. Repo Structure"})
read_file({"path": "CLAUDE.md"})
search({"query": "supabase.co/functions"})
search({"query": "Live in production"})
search({"query": "server/                            \u2190"})
search({"query": "Edge Function"})
search({"query": "deployed"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1327 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 26

**Tools called, in order:**
```
list_files({})
search({"query": "triptic-backend"})
search({"query": "python-backend"})
read_file({"path": "CLAUDE.md"})
read_file({"path": "CLAUDE.md"})
search({"query": "server/"})
search({"query": "Render"})
search({"query": "deploy"})
read_file({"path": "triptic-backend/railway.json"})
search({"query": "VITE_API"})
search({"query": "railway.app"})
read_file({"path": ".env.local"})
read_file({"path": "triptic-backend/main.py"})
read_file({"path": "python-backend/main.py"})
list_files({})
read_file({"path": "python-backend/README.md"})
search({"query": "server/package.json"})
search({"query": "legacy"})
search({"query": "server (deprecated"})
search({"query": "Node.js backend"})
search({"query": "Express"})
list_files({})
read_file({"path": "README.md"})
search({"query": "triptic-backend/"})
search({"query": "Triptic-backend"})
search({"query": "onrender.com"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1794 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 12

**Tools called, in order:**
```
list_files({})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
search({"query": "server"})
read_file({"path": "CLAUDE.md"})
read_file({"path": "triptic-backend/main.py"})
search({"query": "server/"})
search({"query": "Render"})
search({"query": "VITE_API"})
read_file({"path": ".env.local"})
read_file({"path": "python-backend/README.md"})
search({"query": "onrender"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1496 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 15

**Tools called, in order:**
```
list_files({})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
search({"query": "server/"})
read_file({"path": "triptic-backend/main.py"})
search({"query": "Railway"})
search({"query": "deploy"})
read_file({"path": "python-backend/main.py"})
search({"query": "VITE_API"})
search({"query": "triptic-production"})
search({"query": "up.railway.app"})
search({"query": "VITE_API_BASE_URL="})
read_file({"path": "python-backend/README.md"})
search({"query": "python-backend"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 836 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 3

**Tools called, in order:**
```
list_files({})
search({"query": "backend"})
read_file({"path": "README.md"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 311 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 5

**Tools called, in order:**
```
list_files({})
read_file({"path": "CLAUDE.md"})
read_file({"path": "README.md"})
search({"query": "backend"})
list_files({})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1049 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 21

**Tools called, in order:**
```
list_files({})
search({"query": "server"})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
list_files({})
search({"query": "Live in production"})
search({"query": "render.com"})
search({"query": "VITE_API_URL"})
list_files({})
read_file({"path": "CLAUDE.md"})
search({"query": "Node/Express"})
search({"query": "legacy"})
search({"query": "deprecated"})
search({"query": "FastAPI AI backend"})
list_files({})
search({"query": "\u251c\u2500\u2500"})
search({"query": "python-backend/app.py"})
search({"query": "main.py"})
read_file({"path": "python-backend/main.py"})
read_file({"path": "triptic-backend/main.py"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1453 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 19

**Tools called, in order:**
```
list_files({})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
search({"query": "server"})
read_file({"path": "CLAUDE.md"})
read_file({"path": "triptic-backend/main.py"})
search({"query": "python-backend/                  \u2190"})
search({"query": "server/                            \u2190"})
list_files({})
search({"query": "render.yaml"})
search({"query": "vercel.json"})
search({"query": "\u251c\u2500\u2500 server"})
search({"query": "deploy"})
read_file({"path": "python-backend/README.md"})
read_file({"path": "triptic-backend/railway.json"})
read_file({"path": "CLAUDE.md"})
search({"query": "legacy"})
search({"query": "Express"})
search({"query": "FastAPI"})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1544 chars about a private codebase]
Named as the live backend: python-backend
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Temperature:** 1

**Tool call count:** 27

**Tools called, in order:**
```
list_files({})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
search({"query": "server/"})
list_files({})
read_file({"path": "python-backend/README.md"})
search({"query": "Render"})
search({"query": "deploy"})
read_file({"path": "triptic-backend/railway.json"})
read_file({"path": "triptic-backend/main.py"})
search({"query": "VITE_API"})
read_file({"path": "CLAUDE.md"})
search({"query": "\u251c\u2500\u2500"})
read_file({"path": "CLAUDE.md"})
search({"query": "CLAUDE.md:"})
search({"query": "Node.js backend"})
search({"query": "Express"})
read_file({"path": "server/src/server.tsx"})
search({"query": "match_score"})
search({"query": "ai_search"})
search({"query": "match-score"})
search({"query": "8000"})
search({"query": "railway"})
read_file({"path": "python-backend/main.py"})
search({"query": "VITE_API_BASE_URL="})
list_files({})
```

**Fake-tool attempts:**
(none)

**Final answer:**
```
[redacted: 1766 chars about a private codebase]
Named as the live backend: python-backend
```

---

