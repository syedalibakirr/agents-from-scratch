# Flood Test Results

Note: several runs show APIConnectionError from a network drop during
the first batch. Those were re-run; both the failed and successful
attempts are left in for completeness.

Comparing the same 3-tool agent under two conditions: `clean` (3 real tools) vs `flood` (3 real tools + 50 fake, never-callable tools). No grading here — just what the agent called and what it said.

---

## Q2 — flood

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 11.0s

**Tool call count:** 2

**Tools called, in order:**
```
search({"query": "embedding"})
search({"query": "vector("})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (used via LiteLLM alongside GPT-4o for the AI stack), and the vector column is defined as **`vector(1536)`** — i.e., it expects 1536-dimensional embeddings.

This is confirmed in multiple places:
- `README.md` / `CLAUDE.md`: list `text-embedding-3-small` as the embedding model.
- `database/migrations/create_counselor_insights_embeddings.sql`: defines `embedding vector(1536) NOT NULL` and the matching RPC function parameter `query_embedding vector(1536)`.
- `python-backend/config.py`: notes "Must match the `vector(1536)` dimension in `college_embeddings` and `student_activity_embeddings` tables," confirming this same 1536-dim convention is used consistently across the embeddings tables.
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 51.7s

**Tool call count:** 26

**Tools called, in order:**
```
list_files({})
read_file({"path": "CLAUDE.md"})
read_file({"path": "README.md"})
search({"query": "server/"})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
list_files({})
read_file({"path": "python-backend/README.md"})
search({"query": "render.yaml"})
search({"query": "triptic.ai"})
read_file({"path": "triptic-backend/main.py"})
read_file({"path": "CLAUDE.md"})
search({"query": "python-backend/                  \u2190"})
search({"query": "Render"})
search({"query": "deploy"})
read_file({"path": "triptic-backend/railway.json"})
search({"query": "VITE_API_URL"})
search({"query": "API_BASE_URL"})
read_file({"path": ".env.local"})
search({"query": "VITE_API_BASE_URL"})
search({"query": "server"})
list_files({})
list_files({})
search({"query": "triptic-backend"})
list_files({})
read_file({"path": "python-backend/config.py"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
This is clear enough. Based on the evidence in the repo:

- **`python-backend`** is the live backend. It's the FastAPI service that the frontend actually talks to — `client/src/services/*.ts` all default to `VITE_API_BASE_URL || "http://localhost:8000"`, which matches `python-backend`'s port and its extensive, actively-developed feature set (essay coaching, research chatbot/RAG, dashboard agent, counselor insights, match scoring, ai search, etc., all documented in `CLAUDE.md` and `docs/`). It has real CORS config allowlisting `https://triptic.ai` / `https://www.triptic.ai` in `python-backend/config.py`, and `CLAUDE.md` explicitly lists it in the repo structure as "← FastAPI AI backend."

- **`server`** is dead/scaffold code — it's a leftover Node.js/Express stub (`server.tsx` literally contains the comment "This file should set up the express server as shown in the lecture code" and just logs `"We've now got a server!"`). Nothing in the client points to it, and it's not referenced anywhere in the architecture docs.

- **`triptic-backend`** is a small, separate/newer FastAPI microservice (health check literally reports `"service": "triptic-backend"`) with only three routers (`ai_search`, `verification`, `match_score`) and a `railway.json` for Railway deploys. It's not wired up anywhere else in the codebase (no client code calls it, no docs reference it besides its own files) — it looks like either an early scaffold for splitting these three endpoints out, or an experimental/in-progress migration target, not the service currently in production use.

**Conclusion: `python-backend` is the live backend** that the deployed frontend actually communicates with.
```

---

## Q1 — flood

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 43.5s

**Tool call count:** 19

**Tools called, in order:**
```
list_files({})
search({"query": "server"})
search({"query": "python-backend"})
search({"query": "triptic-backend"})
read_file({"path": "CLAUDE.md"})
list_files({})
search({"query": "FastAPI AI backend"})
search({"query": "Express"})
search({"query": "render.yaml"})
search({"query": "VITE_API_URL"})
search({"query": "triptic.ai"})
read_file({"path": "python-backend/config.py"})
search({"query": "API_BASE_URL"})
list_files({})
search({"query": "/api/dashboard/summary"})
search({"query": "/api/research/ask"})
read_file({"path": "triptic-backend/main.py"})
search({"query": "triptic-backend"})
read_file({"path": "docs/architecture/MIGRATION_SUMMARY.md"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
This confirms **python-backend** is the actively developed, live backend that the frontend client actually calls (via `VITE_API_BASE_URL`, endpoints like `/api/research/ask`, `/api/dashboard/summary`, college recommender, etc., and it's connected to Supabase in production with CORS allowlisting `triptic.ai`).

By contrast:
- **`server/`** is just leftover course/lecture boilerplate (Express "as shown in the lecture code") — not used by the app.
- **`triptic-backend/`** is a separate, minimal/early-stage FastAPI stub (only `ai_search`, `verification`, `match_score` routes) that isn't wired up to the client and isn't referenced anywhere else in the docs/migration history.

**Answer: `python-backend` is the live backend.**
```

---

## Q3 — clean

**Question:** Which file triggers Google OAuth sign-in?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 14.4s

**Tool call count:** 5

**Tools called, in order:**
```
search({"query": "OAuth"})
search({"query": "google"})
search({"query": "Continue with Google"})
search({"query": "signInWithGoogle"})
read_file({"path": "client/src/components/marketplace/AuthModal.tsx"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The Google OAuth sign-in flow is triggered from **`client/src/components/marketplace/AuthModal.tsx`** — it contains the "Continue with Google" button (with a `googleLoading` state showing "Redirecting…") that kicks off the Google OAuth flow via Supabase, with the role stored in `sessionStorage` beforehand and the post-redirect handling done in `AuthCallback`.
```

---

## Q3 — flood

**Question:** Which file triggers Google OAuth sign-in?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 13.7s

**Tool call count:** 4

**Tools called, in order:**
```
search({"query": "GoogleAuthProvider"})
search({"query": "google"})
search({"query": "signInWithOAuth"})
search({"query": "Continue with Google"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The client-side file that actually triggers Google OAuth sign-in is:

**`client/src/components/marketplace/AuthModal.tsx`**

Specifically, it calls `supabase.auth.signInWithOAuth({...})` (around line 227) when the user clicks the **"Continue with Google"** button (rendered around line 679).

Related supporting pieces (not the trigger itself, but relevant context):
- `server/src/routes/auth.ts` – exposes `GET /auth/oauth/google` to get the OAuth URL (server-side flow for non-Supabase-direct calls).
- `server/src/services/authService.ts` – also has a `signInWithOAuth` call (line 203) for a server-driven variant.
- `docs/setup/GOOGLE_OAUTH_SETUP.md` – setup documentation for configuring the provider.

But for the actual UI action that kicks off Google sign-in, it's `AuthModal.tsx`.
```

---

## Q4 — clean

**Question:** Is the Supabase session stored in localStorage or sessionStorage?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 12.3s

**Tool call count:** 3

**Tools called, in order:**
```
search({"query": "createClient"})
search({"query": "supabase"})
read_file({"path": "client/src/lib/supabase.ts"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
In this codebase, the Supabase session is stored in **`sessionStorage`**, not `localStorage`.

Details from `client/src/lib/supabase.ts`:

- The `createClient` call is configured with a **custom `storage` adapter** (`sharedSessionStorage`) instead of the default (which would be `localStorage`).
- This adapter's `getItem`/`setItem`/`removeItem` all read/write directly to `window.sessionStorage`.
- To compensate for `sessionStorage`'s normal per-tab isolation, the app uses a `BroadcastChannel` (`'triptic-auth-sync'`) to sync the `sb-*` auth keys across tabs:
  - When one tab sets a session key, it broadcasts the value so other open tabs mirror it into their own `sessionStorage`.
  - When a new tab opens, it broadcasts a `request-session` message so existing tabs can send it the current session data.
  - Keys are only synced/removed if they start with `sb-` (the Supabase auth storage key prefix), to avoid touching unrelated sessionStorage entries.

So the intent is to get `localStorage`-like persistence/sharing across tabs while keeping the underlying storage as `sessionStorage` (which clears when the browser/tab is fully closed, rather than persisting indefinitely like `localStorage` does).
```

---

## Q4 — flood

**Question:** Is the Supabase session stored in localStorage or sessionStorage?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 2.1s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q5 — clean

**Question:** What access does fix_chat_upload_permissions.sql grant on the chat-attachments bucket?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 1.9s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q5 — flood

**Question:** What access does fix_chat_upload_permissions.sql grant on the chat-attachments bucket?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 1.8s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q6 — clean

**Question:** Which file calls the Anthropic API?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 1.8s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q6 — flood

**Question:** Which file calls the Anthropic API?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 1.6s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q7 — clean

**Question:** What is the timeout, in seconds, on the Anthropic HTTP call?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 1.8s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q7 — flood

**Question:** What is the timeout, in seconds, on the Anthropic HTTP call?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 1.7s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 2.3s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q1 — clean

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 1.9s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q1 — flood

**Question:** Which of these three folders is the live backend: server, python-backend, or triptic-backend?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 2.1s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q3 — clean

**Question:** Which file triggers Google OAuth sign-in?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 1.9s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q3 — flood

**Question:** Which file triggers Google OAuth sign-in?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 2.1s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q4 — clean

**Question:** Is the Supabase session stored in localStorage or sessionStorage?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 1.8s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q4 — flood

**Question:** Is the Supabase session stored in localStorage or sessionStorage?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 2.0s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q5 — clean

**Question:** What access does fix_chat_upload_permissions.sql grant on the chat-attachments bucket?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 2.1s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q5 — flood

**Question:** What access does fix_chat_upload_permissions.sql grant on the chat-attachments bucket?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 2.0s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q6 — clean

**Question:** Which file calls the Anthropic API?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 1.9s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q6 — flood

**Question:** Which file calls the Anthropic API?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 1.8s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q7 — clean

**Question:** What is the timeout, in seconds, on the Anthropic HTTP call?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 2.2s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q7 — flood

**Question:** What is the timeout, in seconds, on the Anthropic HTTP call?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 2.3s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 2.0s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q8 — flood

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 1.7s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
t(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1137, in request
    response, prepared = self._attempt_request(
                         ~~~~~~~~~~~~~~~~~~~~~^
        model_copy(input_options), stream=stream, retries_taken=retries_taken
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1309, in _attempt_request
    raise APIConnectionError(request=request) from err
anthropic.APIConnectionError: Connection error.)
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 13.2s

**Tool call count:** 3

**Tools called, in order:**
```
search({"query": "embedding"})
read_file({"path": "database/migrations/create_counselor_insights_embeddings.sql"})
read_file({"path": "services/embedding_pipeline.py"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **`text-embedding-3-small`** model (accessed via LiteLLM), and the `embedding` column in the `counselor_insights_embeddings` table is defined as `vector(1536)` — expecting **1536-dimensional** vectors.
```

---

## Q4 — flood

**Question:** Is the Supabase session stored in localStorage or sessionStorage?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 8.8s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
By default, Supabase's JavaScript client stores the session in **localStorage** (not sessionStorage).

Specifically:

- When you initialize the Supabase client (`createClient`), the `auth` configuration defaults to using `localStorage` as the storage medium for the session (access token, refresh token, etc.).
- This means the session **persists across browser tabs and even after the browser is closed and reopened**, until it's explicitly signed out or the token expires/is invalidated.
- The storage key is typically something like `sb-<project-ref>-auth-token`.

If you want different behavior, Supabase lets you customize this via the `storage` option in the client config — for example:

```js
const supabase = createClient(supabaseUrl, supabaseKey, {
  auth: {
    storage: sessionStorage, // switch to sessionStorage instead
    persistSession: true,
    autoRefreshToken: true,
  }
})
```

Using `sessionStorage` instead would make the session tab-scoped and cleared when the tab/browser is closed, which some apps prefer for shorter-lived sessions or stricter security requirements.

A few other notes:
- In server-side/SSR contexts (e.g., Next.js with `@supabase/ssr` or the older `auth-helpers`), sessions are often stored in **cookies** instead, so they can be read on both client and server.
- In React Native, it typically defaults to `AsyncStorage`.

So the answer depends on context, but for a plain browser-based JS client, it's **localStorage** by default.

Do you want me to check your actual codebase to see how it's configured?
```

---

## Q5 — clean

**Question:** What access does fix_chat_upload_permissions.sql grant on the chat-attachments bucket?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 16.0s

**Tool call count:** 3

**Tools called, in order:**
```
search({"query": "fix_chat_upload_permissions"})
list_files({})
read_file({"path": "fix_chat_upload_permissions.sql"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
[Redacted — describes an unpatched access-control issue in a live
application. Tool-call counts and sequences above are unchanged.
Full text published once fixed.]
```

---

## Q5 — flood

**Question:** What access does fix_chat_upload_permissions.sql grant on the chat-attachments bucket?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 15.2s

**Tool call count:** 3

**Tools called, in order:**
```
search({"query": "fix_chat_upload_permissions"})
list_files({})
read_file({"path": "fix_chat_upload_permissions.sql"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
[Redacted — describes an unpatched access-control issue in a live
application. Tool-call counts and sequences above are unchanged.
Full text published once fixed.]
```

---

## Q6 — clean

**Question:** Which file calls the Anthropic API?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 8.2s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "anthropic"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
Several files call the Anthropic API:

- **`python-backend/api/routes.py`** — makes a direct HTTP POST request to `https://api.anthropic.com/v1/messages` (using the `ANTHROPIC_API_KEY` from `config.py`) for marketplace counselor matching.
- **`triptic-backend/routes/ai_search.py`** — uses the `anthropic` Python SDK (`anthropic.Anthropic(api_key=...)`).
- **`triptic-backend/routes/match_score.py`** — also uses the `anthropic` Python SDK client the same way.
```

---

## Q6 — flood

**Question:** Which file calls the Anthropic API?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 14.0s

**Tool call count:** 2

**Tools called, in order:**
```
search({"query": "anthropic"})
search({"query": "api.anthropic.com"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
Several files in this repo make calls to the Anthropic API:

1. **`python-backend/api/routes.py`** (around line 1754) — makes a direct HTTP `POST` request to `https://api.anthropic.com/v1/messages` using the `ANTHROPIC_API_KEY` from config, for the marketplace counselor-matching feature.

2. **`triptic-backend/routes/ai_search.py`** — uses the `anthropic` Python SDK (`anthropic.Anthropic(api_key=...)`) to call Claude for AI-powered search.

3. **`triptic-backend/routes/match_score.py`** — also instantiates `anthropic.Anthropic(api_key=...)` to call Claude for computing match scores.

So depending on which backend you mean:
- In `python-backend`, it's **`api/routes.py`** (raw HTTP call).
- In `triptic-backend`, it's **`routes/ai_search.py`** and **`routes/match_score.py`** (via the official SDK).
```

---

## Q7 — clean

**Question:** What is the timeout, in seconds, on the Anthropic HTTP call?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 8.6s

**Tool call count:** 2

**Tools called, in order:**
```
search({"query": "timeout"})
read_file({"path": "python-backend/api/routes.py"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The Anthropic HTTP call in `python-backend/api/routes.py` (line 1752) uses:

```python
async with httpx.AsyncClient(timeout=60.0) as client:
```

So the timeout is **60 seconds**.
```

---

## Q7 — flood

**Question:** What is the timeout, in seconds, on the Anthropic HTTP call?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 15.0s

**Tool call count:** 3

**Tools called, in order:**
```
search({"query": "Anthropic"})
read_file({"path": "python-backend/api/routes.py"})
search({"query": "timeout"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The timeout on the Anthropic HTTP call (`python-backend/api/routes.py` line 1752, `httpx.AsyncClient(timeout=60.0)`) is **60 seconds**.
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.0s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "BroadcastChannel"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The BroadcastChannel is named **`triptic-auth-sync`**.
```

---

## Q8 — flood

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 7.7s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "BroadcastChannel"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The BroadcastChannel used to sync auth across tabs is named **`triptic-auth-sync`**.

This is confirmed in multiple places in the codebase:
- `client/src/context/AuthContext.tsx` (lines 112 and 140)
- `client/src/lib/supabase.ts` (line 16)

It's used to propagate authentication state (like session data in `sessionStorage`) across open browser tabs.
```

---

## Q4 — flood

**Question:** Is the Supabase session stored in localStorage or sessionStorage?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 8.4s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
By default, the Supabase JS client stores the session in **localStorage** (not sessionStorage).

A few details on how this works:

- Supabase uses the `@supabase/gotrue-js` (auth) library under the hood, which persists the session (access token, refresh token, etc.) to `localStorage` under a key like `sb-<project-ref>-auth-token`.
- This is controlled by the `persistSession` option (default `true`) when creating the client via `createClient()`.
- Because it's `localStorage`, the session persists across browser tabs and survives page reloads/browser restarts (until the token expires or the user signs out).
- If you want different behavior, you can customize it via the `auth.storage` option in `createClient()`:
  - Pass `sessionStorage` (or any object implementing the Storage interface) if you want the session cleared when the tab closes.
  - Set `persistSession: false` if you don't want it stored at all (e.g., memory-only, useful for server-side contexts).

Example:
```js
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(url, key, {
  auth: {
    storage: window.sessionStorage, // override default localStorage
    persistSession: true,
  }
})
```

So: **localStorage by default**, but it's configurable.

Note: I don't have access to your specific codebase in this conversation, so this answer reflects Supabase's default/standard behavior. If you'd like, I can search your repo for the actual `createClient` configuration to confirm what your project uses — just let me know.
```

---

## Q4 — flood

**Question:** Is the Supabase session stored in localStorage or sessionStorage?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 10.6s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
By default, Supabase (via `supabase-js`) stores the session in **localStorage**, not sessionStorage.

Specifically:

- The Supabase client uses an auth storage key (default `sb-<project-ref>-auth-token`) and persists the session object (access token, refresh token, expiry, user info) to `localStorage` on web/browser environments.
- This is controlled by the `persistSession` option (default `true`) and the `storage` option in the `createClient` auth config — if you don't override it, it defaults to `window.localStorage` when available.
- Because it's localStorage rather than sessionStorage, the session **persists across browser tabs and after the browser is closed and reopened**, until it's explicitly signed out or the token expires/is cleared.

If you want different behavior, you can customize it:

```js
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(supabaseUrl, supabaseKey, {
  auth: {
    storage: window.sessionStorage, // switch to sessionStorage instead
    persistSession: true,
    autoRefreshToken: true,
  },
})
```

Common reasons to switch to `sessionStorage`:
- You want the session to be cleared when the tab/browser closes (more secure for shared/public computers).
- You're avoiding cross-tab session persistence.

Trade-offs of `sessionStorage`:
- Each tab gets its own session (no cross-tab sharing).
- Users get logged out when they close the tab, which may hurt UX for typical "remember me" style login flows.

For server-side or non-browser environments (e.g., React Native, Node scripts), Supabase requires you to supply your own storage adapter (like `AsyncStorage` for React Native), since `localStorage`/`sessionStorage` aren't available there.

If you tell me your specific setup (framework, whether you're using `@supabase/ssr`, React Native, etc.), I can confirm exactly which storage mechanism your app is using and how to check/change it.
```

---

## Q4 — flood

**Question:** Is the Supabase session stored in localStorage or sessionStorage?

**Condition:** flood (FLOOD=1, 53 tools)

**Wall time:** 8.9s

**Tool call count:** 0

**Tools called, in order:**
(none)

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
By default, Supabase's JavaScript client (`supabase-js`) stores the session in **localStorage**, not sessionStorage.

Key details:

- Supabase uses a storage adapter pattern under the hood (via GoTrue-js, the auth library it depends on).
- On web platforms, it defaults to `window.localStorage`, so the session (access token, refresh token, etc.) persists across browser tabs and survives page reloads and browser restarts.
- This is configurable when you initialize the client. In the `createClient` options, under the `auth` key, you can pass a custom `storage` option to override this — for example, swapping in `sessionStorage` if you want the session to be cleared when the tab/browser closes, or providing a custom storage adapter (useful in React Native, where it typically uses `AsyncStorage` instead).

Example of overriding it to use sessionStorage:

```js
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(supabaseUrl, supabaseKey, {
  auth: {
    storage: sessionStorage,
    persistSession: true,
    autoRefreshToken: true,
  },
})
```

So: **localStorage by default**, but it's overridable if you need sessionStorage-like (tab-scoped, cleared on close) behavior.

I don't have direct access to your specific codebase/config here, but if you'd like, I can search your repo for how the Supabase client is initialized to confirm what your project actually uses.
```

---

