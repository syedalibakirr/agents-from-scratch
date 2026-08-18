# 20 Runs, API Default Temperature

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Target repo:** an external codebase (`~/Desktop/Cursor - LP`, not part of this repo), fixed across all 20 runs.

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

**Final answer (verbatim):**
```
Based on my research, **`python-backend`** is the live backend.

Evidence:
- The client's frontend (`client/src/services/*.ts`) calls `VITE_API_BASE_URL` (defaulting to `http://localhost:8000`) for all real functionality — dashboard summaries, research chat, essay/activity embeddings, counselor insights, meeting-intent detection, etc.
- `python-backend/main.py` is explicitly labeled as the **Railway entry point** ("Railway will look for 'app' object in main.py"), i.e., it's what's actually deployed to production.
- `python-backend/README.md` describes it as the live microservice in the architecture: `Client (React) → Python Backend (port 8000) → OpenAI API`, with `server/` (Node/Express) shown as a separate legacy piece.
- Root `README.md` confirms the stack as "Backend: Python + FastAPI."
- `server/` is an Express/TypeScript backend that appears to be legacy — env var loading logic in `python-backend/supabase_client.py` treats `server/.env` as lower priority/fallback, suggesting migration away from it.
- `triptic-backend/` is a small, separate FastAPI stub (`ai_search`, `verification`, `match_score` routes) with its own `railway.json`, but nothing in the client code points to it, and it isn't referenced anywhere else in the docs/architecture as the active service — it looks like a newer/experimental or unused service.

So the answer is **python-backend**.
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

**Final answer (verbatim):**
```
Based on the repo evidence, **`python-backend`** is the live backend.

Key confirmations:
- `CLAUDE.md` (the project's dev bible, describing the "live in production" Triptic.ai app) explicitly maps the repo structure with `python-backend/ ← FastAPI AI backend`.
- The frontend client (`client/.env.example`) references `VITE_PYTHON_BACKEND_URL=http://localhost:8000`, confirming the client calls into `python-backend`.
- `python-backend` has extensive active documentation (`README.md`, `QUICKSTART.md`, `start.sh`, `test_api.py`) describing real endpoints like `/api/essay/analyze`, `/api/essay/upload`, `/api/health`, and Swagger docs — all indicating a fully fleshed-out, running FastAPI service.
- `server/` appears to be a minimal/legacy Node+Express scaffold (`server.tsx` just logs "We've now got a server!" — boilerplate/lecture-style code, not a real production service).
- `triptic-backend/` contains only a tiny `main.py` with a single health-check stub (`{"status": "ok", "service": "triptic-backend"}`), suggesting it's an early scaffold or placeholder, not the active backend.

So while `server` and `triptic-backend` look like stubs/leftovers, `python-backend` is the fully-built, documented, and actively-referenced FastAPI backend that the live frontend actually talks to.
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

**Final answer (verbatim):**
```
Based on the repo's documentation, **`server`** is the live backend (Node.js/Express), working alongside `python-backend` as an AI microservice.

Details:
- **CLAUDE.md** (the project's "development bible") describes `server/` as part of the core, actively maintained monorepo structure, with the app "Live in production at triptic.ai — real users."
- **`python-backend/README.md`** explicitly diagrams the architecture as:
  ```
  ├── client/           (React frontend - Vite)
  ├── server/           (Node.js backend - Express)
  ├── python-backend/   (THIS SERVICE - Python AI engine)
  └── database/         (PostgreSQL/Supabase schemas)
  ```
  confirming `server` is the main backend, while `python-backend` is a secondary microservice specifically for AI/essay-coaching features (calling OpenAI, orchestrated by the main server).
- **`triptic-backend`** appears to be a minimal, seemingly experimental/legacy FastAPI stub (just a health check and a few routers for `ai_search`, `verification`, `match_score`), not referenced anywhere in the main docs/architecture as the production backend — it looks unused or superseded by `python-backend`.

So the live/production backend is **`server`**, with **`python-backend`** as a supporting AI microservice, and **`triptic-backend`** as a leftover/unused stub.
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

**Final answer (verbatim):**
```
This confirms it: **`python-backend`** is the live backend.

Evidence:
- `CLAUDE.md` (the project's dev bible, describing the live production repo structure at triptic.ai) explicitly lists `python-backend/` as "FastAPI AI backend" in the canonical repo structure, and extensive docs (`docs/setup/RESEARCH_CHATBOT_SETUP.md`, `docs/architecture/MIGRATION_SUMMARY.md`, `database/OPTIMIZATION_PLAN.md`) all reference real, actively-developed features (research chatbot, college recommender, Supabase integration) living in `python-backend/`.
- `python-backend/main.py` is a Railway deployment entry point that imports the fully-built `app.py` (title "AI Essay Coach Backend", CORS config from a real config module, routes mounted from `api/routes.py`, plus `services/`, `college_recommender/`, `data/` subfolders) — a mature, production-grade FastAPI app.
- The frontend (`client/src/services/*.ts`) calls `import.meta.env.VITE_API_BASE_URL` (defaulting to `localhost:8000`, FastAPI's default port), matching `python-backend`.
- By contrast:
  - `triptic-backend/main.py` is a much thinner FastAPI app with only 3 routers (`ai_search`, `verification`, `match_score`) and a bare `/health` check — looks like an early scaffold/prototype, not referenced anywhere else in docs or client code.
  - `server/` is a Node/Express + TypeScript stub (`server.tsx` with just a "We've now got a server!" console log) — clearly boilerplate/starter code, not integrated with the rest of the app.

So the actively used, documented, and integrated backend is **`python-backend`**.
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

**Final answer (verbatim):**
```
python-backend is the live backend. Here's the evidence:

- **README.md** explicitly states the stack: "Backend: Python + FastAPI" — no mention of `server` or `triptic-backend`.
- **CLAUDE.md** (the project's dev bible) lists `python-backend/` in the repo structure as "← FastAPI AI backend," and references it extensively throughout docs (`docs/setup/RESEARCH_CHATBOT_SETUP.md`, `docs/architecture/MIGRATION_SUMMARY.md`, `docs/rag/STUDENT_AGENT.md`, `database/OPTIMIZATION_PLAN.md`, etc.).
- `python-backend/main.py` is explicitly a **Railway entry point** (`# Railway will look for 'app' object in main.py`), confirming it's the deployed production service.
- `python-backend/app.py` runs on port 8000, which matches the frontend's actual API calls: `client/src/services/dashboardAgentApi.ts`, `researchApi.ts`, `chatIntentApi.ts`, `counselorInsightsApi.ts`, and `CounselorResearchWindow.tsx` all default to `VITE_API_BASE_URL || "http://localhost:8000"`.
- By contrast:
  - `server/` is a minimal, unfinished Express/TypeScript scaffold (`server.tsx` just logs "We've now got a server!" and has no real routes wired up beyond a placeholder), and nothing in the client calls it.
  - `triptic-backend/` is a small, separate FastAPI stub (`main.py` with just a health check and a few routers for `ai_search`, `verification`, `match_score`) that isn't referenced anywhere in the docs, CLAUDE.md architecture, or the client's API service files.

So `python-backend` is the actively used, documented, and deployed (Railway) FastAPI service — the real live backend — while `server` and `triptic-backend` appear to be legacy/experimental scaffolds not wired into the live product.
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

**Final answer (verbatim):**
```
Based on my research, **`python-backend`** is the live backend.

Evidence:
- The project README explicitly states the stack: **"Backend: Python + FastAPI"** (with Supabase/pgvector DB and OpenAI for AI features).
- The client code (`client/src/services/*.ts`, `CounselorResearchWindow.tsx`) calls a `VITE_API_BASE_URL` (defaulting to `http://localhost:8000`) with endpoints like `/api/research/ask` and `/api/counselor/research/history` — these routes are implemented in `python-backend/api/routes.py`.
- `CLAUDE.md`'s repo structure map labels it directly: `python-backend/ ← FastAPI AI backend`.
- Extensive docs (`docs/setup/RESEARCH_CHATBOT_SETUP.md`, `docs/architecture/MIGRATION_SUMMARY.md`, `docs/rag/*`) all reference `python-backend` as the active service being developed/migrated.

By contrast:
- **`server`** is a separate, much more minimal Node/Express + TypeScript scaffold ("Backend Server for UniVerse") that looks like leftover/starter boilerplate (e.g., `server.tsx` with just a console.log "We've now got a server!") rather than the actively wired-up API.
- **`triptic-backend`** is a small FastAPI stub with only 3 routers (`ai_search`, `verification`, `match_score`) and no references elsewhere in docs or client code — it appears to be an early/experimental scaffold, not the one the frontend actually talks to.
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

**Final answer (verbatim):**
```
Based on the evidence in the repo, **`python-backend`** is the live backend.

**Why:**

1. **It's the one actually wired into the frontend.** Multiple client services (`dashboardAgentApi.ts`, `chatIntentApi.ts`, `researchApi.ts`, `counselorInsightsApi.ts`, `CounselorResearchWindow.tsx`, `EssayFeedbackChat.tsx`) call `import.meta.env.VITE_API_BASE_URL || "http://localhost:8000"` — port 8000 matches `python-backend`'s documented port, and there's even a log line `"✅ [CHAT] Received response from Python backend"` in `EssayFeedbackChat.tsx`.

2. **It's the one documented in `CLAUDE.md`**, the repo's canonical dev doc ("single source of truth"), which lists the repo structure as `client/` + `python-backend/` (described as "FastAPI AI backend") + `database/`. Neither `server/` nor `triptic-backend/` appears in that structure.

3. **`server/` is a dead stub**, not a real implementation — its own source file literally says `// This file should set up the express server as shown in the lecture code` and just returns a `{ping: "pong"}` placeholder. It has no wired-up business logic and isn't referenced by the client.

4. **`triptic-backend/` looks like an unintegrated/experimental service.** It does have deployment scaffolding (`Dockerfile`, `railway.json`), but its three routes (`/api/ai-search`, `/api/match-score`, `/api/send-verification-email`) are not called anywhere in `client/src` — there's no fetch/axios call to those paths
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

**Final answer (verbatim):**
```
This confirms it clearly - the client points to port 8000 as `VITE_API_BASE_URL`, which matches `python-backend` (its README states it runs FastAPI on port 8000, has a Railway entrypoint at `python-backend/main.py` that imports from `app.py`, and hosts all the real endpoints like `/api/research/`, `/api/counselor/research/`, dashboard agent, chat intent, etc.).

**`python-backend` is the live backend.**

Supporting evidence:
- Root `README.md`: "Backend: Python + FastAPI"
- `CLAUDE.md` repo structure explicitly labels it `python-backend/ ← FastAPI AI backend`
- `python-backend/main.py` is a Railway deployment entry point importing the real `app.py`
- All client-side API calls default to `http://localhost:8000` (python-backend's port), used for research chat, dashboard agent, counselor insights, etc.
- Extensive docs (`docs/setup/RESEARCH_CHATBOT_SETUP.md`, `docs/architecture/MIGRATION_SUMMARY.md`, `docs/rag/STUDENT_AGENT.md`) all reference active development happening in `python-backend/`.

By contrast:
- **`server/`** is the old Node.js/Express backend, referenced mainly in migration docs (`MIGRATION_PLAN.md`) as the thing being migrated *away from* into `python-backend`.
- **`triptic-backend/`** looks like a minimal/skeleton FastAPI stub (just `main.py` with a `/health` check and three routers), likely an early scaffold or a separate/unused service — not referenced anywhere in the main docs or client code as the active API target.
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

**Final answer (verbatim):**
```
Based on the evidence in the repo, **`python-backend`** is the live backend.

Key findings:

1. **CLAUDE.md** (the project's development bible) explicitly labels it in the repo structure diagram as `python-backend/ ← FastAPI AI backend`, and references it throughout (e.g. `python-backend/services/...`).

2. **Client wiring**: The frontend services (`researchApi.ts`, `chatIntentApi.ts`, `counselorInsightsApi.ts`, `dashboardAgentApi.ts`, `CounselorResearchWindow.tsx`) all call `import.meta.env.VITE_API_BASE_URL || "http://localhost:8000"` — and `python-backend` is the FastAPI service documented to run on port 8000 (per its own README: *"Client (React) → Python Backend (port 8000) → OpenAI API"*).

3. **Extensive real usage**: `python-backend` has a full structure (`app.py`, `config.py`, `models/`, `services/`, `api/routes.py`, `college_recommender/`, `data/`) and is referenced across many docs (`docs/setup/RESEARCH_CHATBOT_SETUP.md`, `docs/rag/STUDENT_AGENT.md`, `docs/architecture/MIGRATION_SUMMARY.md`, `database/OPTIMIZATION_PLAN.md`) as the actual AI engine powering search, research chat, essay coaching, and college recommendations.

By contrast:
- **`server/`** (Node/Express) contains only placeholder boilerplate — e.g. `src/server.tsx` literally says `// This file should set up the express server as shown in the lecture code` and just logs `"We've now got a server!"`. It's a leftover/unused stub.
- **`triptic-backend/`** is a small, separate FastAPI stub (just `ai_search`, `verification`, `match_score` routes plus a Railway deploy config) that isn't referenced anywhere else in the codebase or docs — it looks like a newer/experimental scaffold not yet wired into the live client.
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

**Final answer (verbatim):**
```
This confirms it: **`server`** is the live backend (Node.js/Express).

Evidence:
- `server/package.json` explicitly describes it as "Backend Server for UniVerse" with `start`/`dev`/`start:prod` scripts, and `server/src/server.tsx` is a full Express app with CORS config, JSON routes (`configRoutes`), a 404 handler, and `app.listen(port)` — i.e., a real, runnable service.
- `server/src/config/supabase.ts` shows it manages actual Supabase auth/config — real production wiring, not a stub.
- `python-backend/README.md` itself lists `server/` as "(Node.js backend - Express)" alongside itself, confirming `server` is the primary backend and `python-backend` is a separate/auxiliary "FastAPI AI backend" (per `CLAUDE.md`) used for specific AI features (recommendations, chatbot, etc.), sharing env config with `server/.env`.
- `triptic-backend/main.py` is a minimal, barely-implemented FastAPI stub (just a `/health` route plus a few routers referenced), showing no signs of being deployed/live — it looks like a scaffold/experiment, not referenced elsewhere in docs or CLAUDE.md's repo structure.

So the hierarchy is:
- **`server`** → live Node/Express backend (primary, production).
- **`python-backend`** → live-but-secondary FastAPI service for AI/college-recommendation features, working alongside `server`.
- **`triptic-backend`** → unused/incomplete scaffold, not part of the live system.
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

**Final answer (verbatim):**
```
This confirms it clearly: **`python-backend` is the live/production backend.**

Evidence:
- `python-backend/main.py` is explicitly labeled as the **Railway entry point** ("Railway will look for `app` object in main.py") with a comment literally reading `#adding a comment to test the deployment` — a telltale sign of live deploy testing.
- `python-backend/config.py` has production CORS origins hardcoded: `https://triptic.ai` and `https://www.triptic.ai`.
- The frontend client (`client/src/services/*.ts`, `CounselorResearchWindow.tsx`) all call `VITE_API_BASE_URL` (falling back to `localhost:8000`, the standard FastAPI dev port), which is this Python/FastAPI service — not `server` or `triptic-backend`.
- CLAUDE.md's repo map labels it explicitly: `python-backend/ ← FastAPI AI backend`, and it's the subject of active migration docs (`database/analysis/MIGRATION_PLAN.md`, `docs/architecture/MIGRATION_SUMMARY.md`, `docs/rag/STUDENT_AGENT.md`, `docs/setup/RESEARCH_CHATBOT_SETUP.md`) describing real, in-use features (research chatbot, AI recommender, RAG student agent).

By contrast:
- `server` appears to be an older/parallel Node.js Express backend, referenced mostly in passing/legacy migration notes (e.g., "Add to `python-backend/.env` or `server/.env`"), not something the client actively targets.
- `triptic-backend` looks like a newer, minimal/experimental FastAPI scaffold (`main.py` with just a `/health` route and a few routers for `ai_search`, `verification`, `match_score`) — no evidence of it being wired into the live client or deployment pipeline; it reads like a work-in-progress rewrite rather than the deployed service.

So: **`python-backend`** is the live backend powering triptic.ai in production.
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

**Final answer (verbatim):**
```
## Answer: **python-backend**

Here's the evidence:

**`python-backend`** is the real, actively-used backend:
- `CLAUDE.md` (the project's canonical dev doc, described as "the single source of truth for how we build Triptic," which is "Live in production at triptic.ai") explicitly lists it in the repo structure as `python-backend/ ← FastAPI AI backend`.
- Its own `README.md` describes it as "Part of the UniVerse platform" microservice with a real architecture: `Client (React) → Python Backend (port 8000) → OpenAI API`, plus Supabase for persistence.
- It's extensively referenced across active documentation (`docs/setup/RESEARCH_CHATBOT_SETUP.md`, `docs/architecture/MIGRATION_SUMMARY.md`, `docs/rag/STUDENT_AGENT.md`, `database/OPTIMIZATION_PLAN.md`, `database/analysis/MIGRATION_PLAN.md`), with real file/line references and real endpoints (`/api/research/ask`, `college_recommender`, etc.).
- It has a full, mature structure: `app.py`, `config.py`, `models/`, `services/` (intent classifier, essay analyzer, chatbot, conversation orchestration), and a compiled `__pycache__` file whose embedded path (`.../UniVerse-Interns-Repo/python-backend/api/routes`) confirms it's actually been run.

**`server`** is legacy/unused boilerplate:
- Its code is literally lecture scaffolding: `// This file should set up the express
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

**Final answer (verbatim):**
```
Based on my review of the repo, **`python-backend`** is the live backend.

Evidence:
- The root `README.md` describes the stack as "Backend: Python + FastAPI" — no mention of `server` or `triptic-backend`.
- `python-backend` is extensively referenced throughout the codebase: `client/src/services/*Api.ts` files (dashboard agent, research, chat intent, counselor insights) all call it via `VITE_API_BASE_URL` (default `http://localhost:8000`), and `docs/setup/RESEARCH_CHATBOT_SETUP.md`, `docs/rag/STUDENT_AGENT.md`, `docs/architecture/MIGRATION_SUMMARY.md`, and `CLAUDE.md` all document it as "← FastAPI AI backend."
- `python-backend/main.py` is explicitly set up as a **Railway entry point** (`# Railway will look for 'app' object in main.py`), confirming it's the deployed service, and it imports the full `app.py` with routers for essay coaching, research chat, dashboard agent, RAG retrieval, etc.
- `server/` is legacy/unused boilerplate — its own source file literally says `// This file should set up the express server as shown in the lecture code`, and `python-backend/README.md` labels it plainly as the old "(Node.js backend - Express)" with no active usage found (per `database/COLLEGE_DETAILS_MIGRATION.md`: "Node.js Backend: No direct usage found").
- `triptic-backend/` is a small, isolated FastAPI app (only `ai_search`, `verification`, `match_score` routes) that isn't referenced anywhere else in the repo — no docs, no client code, nothing points to it. It appears to be an orphaned/experimental service, not the integrated production backend.

So while both `python-backend` and `triptic-backend` have Railway deploy configs (suggesting both *could* be deployed), only `python-backend` is actually wired into the frontend and documented as the real backend of the platform.
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

**Final answer (verbatim):**
```
This confirms it clearly. **`python-backend` is the live backend.**

Evidence:
- CLAUDE.md (the project's development bible, describing the live production app at triptic.ai) lists the repo structure with `python-backend/` explicly labeled **"← FastAPI AI backend"**, and it's referenced throughout active docs (routes, config, services) as the real, in-use AI microservice.
- The frontend (`client/`) actually calls it: `VITE_API_BASE_URL || "http://localhost:8000"` is used across live services (`researchApi.ts`, `dashboardAgentApi.ts`, `chatIntentApi.ts`, `counselorInsightsApi.ts`, `CounselorResearchWindow.tsx`), and `python-backend` runs on port 8000.
- `python-backend/README.md` explicitly describes it as part of the real "UniVerse platform" microservice architecture (Client → Python Backend → OpenAI/Supabase), matching those frontend calls exactly.
- `server/` (the Express/Node backend) does exist and is used for some auth/API routes, but it's the legacy/secondary Node service, not what the AI-driven frontend features currently call.
- `triptic-backend` (FastAPI, with routers for `ai_search`, `verification`, `match_score`) appears to be a minimal/skeleton service — it's not referenced anywhere else in the codebase (docs, client code, or CLAUDE.md), suggesting it's a stub or experimental/unused scaffold rather than the live service.

So while `server/` is a real secondary Node backend, the actively used, documented, and frontend-integrated backend is **`python-backend`**.
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

**Final answer (verbatim):**
```
Based on the CLAUDE.md repo structure documentation, `python-backend` is confirmed as the actively developed and referenced FastAPI AI backend (handling essay coaching, research chatbot, college recommender, match scoring, etc.), and it's the one the client actually calls (via `VITE_API_BASE_URL`, defaulting to `http://localhost:8000`, which is python-backend's port).

By contrast, `triptic-backend` appears to be a minimal/stub FastAPI app (just a health check and a few route stubs) — likely an early scaffold or unused prototype, not referenced anywhere else in the codebase or docs.

There is no top-level `server` folder found in this repo (only referenced in older docs describing a legacy/planned Node.js Express backend that doesn't appear to exist in the current repo).

**Conclusion: `python-backend` is the live backend.**
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

**Final answer (verbatim):**
```
python-backend is the live backend — it's the FastAPI (Python) service referenced throughout the docs (README.md, CLAUDE.md) as the actual AI backend, with `VITE_PYTHON_BACKEND_URL` used by the frontend to call it. `server` and `triptic-backend` don't appear referenced as the active backend in the docs/config.
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

**Final answer (verbatim):**
```
Based on CLAUDE.md and README.md, **`python-backend`** is the live backend.

Key evidence:
- README.md states the stack is **Frontend**: React + TypeScript + Vite, **Backend**: Python + FastAPI.
- CLAUDE.md's repo structure section explicitly lists `python-backend/ ← FastAPI AI backend` as part of the live repo structure, and references `python-backend/services/`, `python-backend/college_recommender/data_loading.py`, and `python-backend/college_recommender/pipeline.py` as active code paths.
- The frontend's `essayApi.ts` calls out to it via the `VITE_PYTHON_BACKEND_URL` env var (per PROMPT.md).
- `.gitignore` also references `python-backend/venv/`, indicating it's an actively developed Python virtual environment in use.

There's no equivalent mention of `server` or `triptic-backend` being wired into the app's routes, env vars, or CLAUDE.md's documented architecture — suggesting those are either legacy/unused or experimental folders, while `python-backend` is the one actually powering the live triptic.ai backend (AI/FastAPI services).
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

**Final answer (verbatim):**
```
Based on this, `python-backend` is the live backend.

## Summary

- **`python-backend`** — This is the live/production backend. It's explicitly documented in `CLAUDE.md` (the project's "single source of truth" dev bible) as `← FastAPI AI backend`, with `app.py` as the entry point and `api/routes.py` for all API routes. It has a `main.py` that's a **Railway deployment entry point** (`# Railway will look for 'app' object in main.py`, plus a comment "adding a comment to test the deployment"), confirming it's actively deployed to production. It's also referenced extensively throughout `docs/`, `database/analysis/MIGRATION_PLAN.md`, and setup guides (e.g., the research chatbot feature) as the real backend serving the app.

- **`server`** — A minimal/stub Node+Express backend (`"description": "Backend Server for UniVerse"`) whose source file literally says `// This file should set up the express server as shown in the lecture code` — this reads like leftover scaffolding/tutorial code, not part of the current architecture (it's not mentioned in `CLAUDE.md`'s repo structure at all).

- **`triptic-backend`** — Also a small FastAPI stub (just a health check and three routers for `ai_search`, `verification`, `match_score`). It isn't referenced in `CLAUDE.md` or elsewhere in the docs, suggesting it's an early prototype/scratch backend that was superseded by `python-backend`.

So the actual live backend for Triptic.ai is **`python-backend`**.
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

**Final answer (verbatim):**
```
This confirms it clearly: CLAUDE.md (the current dev bible for the live product, Triptic.ai) explicitly names `python-backend/` as the "FastAPI AI backend" in the repo structure, and the README's tech stack line says "Backend: Python + FastAPI" — pointing to `python-backend`.

Comparing the three:

- **`python-backend`** — Fully built out FastAPI service (essay analysis, chatbot, RAG retrieval, college recommender, Supabase client, `railway` entrypoint `main.py` that imports the real `app.py`, extensive routes/services). This is the one referenced throughout `CLAUDE.md` and the docs as *the* AI backend for the live product.
- **`server`** — A minimal Node/Express scaffold (`server.tsx` with a comment "should set up the express server as shown in the lecture code") — looks like leftover/legacy boilerplate from an earlier "UniVerse" course-project version, not part of the current Triptic architecture.
- **`triptic-backend`** — A tiny FastAPI stub (just `main.py` with three empty routers for `ai_search`, `verification`, `match_score`, plus a `railway.json`). It looks like a newly scaffolded/placeholder service (probably an in-progress rename/rewrite target) rather than the actual running backend — none of its routes have real logic yet.

**Answer: `python-backend` is the live backend.** It's the fully implemented FastAPI service that CLAUDE.md and the README describe as the production AI backend, while `server` is legacy/unused Express boilerplate and `triptic-backend` is an empty scaffold with no real implementation yet.
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

**Final answer (verbatim):**
```
I have enough information to answer confidently.

**`python-backend` is the live backend.**

Evidence:
- `CLAUDE.md` (the project's "development bible" for the live production app, triptic.ai) explicitly lists the repo structure as `client/` (React frontend) + `python-backend/` (FastAPI AI backend) + `database/` — it doesn't include `server/` or `triptic-backend/` as part of the active stack.
- The client code actually calls it: multiple files in `client/src/services/*.ts` and `client/src/components/portal/CounselorResearchWindow.tsx` hit `import.meta.env.VITE_API_BASE_URL || "http://localhost:8000"`, and `python-backend` is the service that runs on port 8000 (`app.py`, `config.py`, `uvicorn app:app ... --port 8000`).
- `python-backend/main.py` is a Railway deployment entry point (`from app import app`) with real routes for essay analysis, research chatbot, dashboard agent, chat intent, counselor insights, etc. — extensively documented in `docs/setup/RESEARCH_CHATBOT_SETUP.md`, `docs/rag/STUDENT_AGENT.md`, `docs/architecture/MIGRATION_SUMMARY.md`.

By contrast:
- **`server/`** is an Express/Node stub — `server/src/server.tsx` literally starts with the comment `// This file should set up the express server as shown in the lecture code`, indicating unfinished course/boilerplate code, not wired into the live app.
- **`triptic-backend/`** is a minimal FastAPI service (`main.py` with just `ai_search`, `verification`, `match_score` stub routes and a `/health` check, plus a `railway.json`/`Dockerfile`). It has its own Railway config but there's no evidence the client actually calls its endpoints (no references to `/match-score`, `ai_search`, etc. from `client/`) — it looks like a newer/parallel service not yet integrated into the live product.
```

---

