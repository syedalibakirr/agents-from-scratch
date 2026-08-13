# Flood Test Results

Comparing the same 3-tool agent under two conditions: `clean` (3 real tools) vs `flood` (3 real tools + 50 fake, never-callable tools). No grading here — just what the agent called and what it said.

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 9.6s

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
The semantic search uses OpenAI's **text-embedding-3-small** model (used via LiteLLM alongside GPT-4o for the AI layer), and the database's vector column is defined as **`vector(1536)`** — a 1536-dimensional embedding, as seen in `create_counselor_insights_embeddings.sql` (`embedding vector(1536) NOT NULL`) and confirmed by `python-backend/config.py`, which notes this dimension must match across the `college_embeddings` and `student_activity_embeddings` tables as well.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.7s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model, and the vector column (`embedding` in `counselor_insights_embeddings`) is defined as `vector(1536)` — expecting 1536-dimensional embeddings.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 7.7s

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
The semantic search uses OpenAI's **text-embedding-3-small** model (as used alongside GPT-4o via LiteLLM), and the embedding columns are defined as **`vector(1536)`** — i.e., 1536-dimensional vectors — across the relevant tables (`counselor_insights_embeddings`, `college_embeddings`, `student_activity_embeddings`).
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 15.1s

**Tool call count:** 4

**Tools called, in order:**
```
search({"query": "embedding"})
read_file({"path": "database/migrations/create_counselor_insights_embeddings.sql"})
read_file({"path": "services/embedding_pipeline.py"})
search({"query": "text-embedding-3-small"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (configured via `EMBEDDINGS_MODEL_ID` in `python-backend/config.py`, defaulting to `"text-embedding-3-small"`).

This matches the vector column definitions in the database, such as `counselor_insights_embeddings.embedding`, which is defined as:

```sql
embedding vector(1536) NOT NULL
```

So the expected/required vector dimension is **1536**, consistent with `text-embedding-3-small`'s native output size — as confirmed in `python-backend/models/ai_models.py`, which notes it uses "text-embedding-3-small (1536 dimensions) to match the vector columns."
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 32.9s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
am_cls=Stream[RawMessageStreamEvent],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1536, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1195, in request
    raise self._make_status_error_from_response(response) from None
anthropic.OverloadedError: Error code: 529 - {'type': 'error', 'error': {'type': 'overloaded_error', 'message': 'Overloaded'}, 'request_id': 'req_011CdztCT6HQtgEDuhfJGrjv'})
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.6s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (used via LiteLLM alongside GPT-4o), and the database column is defined as **`vector(1536)`** in `counselor_insights_embeddings`.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 10.4s

**Tool call count:** 3

**Tools called, in order:**
```
search({"query": "embedding"})
read_file({"path": "database/migrations/create_counselor_insights_embeddings.sql"})
search({"query": "text-embedding-3-small"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **`text-embedding-3-small`** model (configured via `EMBEDDINGS_MODEL_ID` in `python-backend/config.py`, accessed through LiteLLM).

The vector column (`embedding` in the `counselor_insights_embeddings` table) is defined as `vector(1536)`, expecting a **1536-dimensional** vector — which matches the native output size of `text-embedding-3-small`, as confirmed in `python-backend/models/ai_models.py`.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.7s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (used alongside GPT-4o via LiteLLM), and the database column stores it as `vector(1536)` — i.e., a 1536-dimensional embedding, as defined in `database/migrations/create_counselor_insights_embeddings.sql`.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.5s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (used via LiteLLM), and the vector column (`embedding` in `counselor_insights_embeddings`) is defined as `vector(1536)` — i.e., it expects 1536-dimensional embeddings.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 7.5s

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
The semantic search uses OpenAI's **text-embedding-3-small** model (accessed via LiteLLM, alongside GPT-4o for chat/completions), and the database `embedding` columns are defined as **`vector(1536)`** — i.e., they expect 1536-dimensional vectors, matching this model's output size (used consistently across `counselor_insights_embeddings`, `college_embeddings`, and `student_activity_embeddings` tables).
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 4.7s

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
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 4.0s

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
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 4.2s

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

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.0s

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
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 29.5s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "BroadcastChannel"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
(agent crashed, no final answer — stderr tail:
am_cls=Stream[RawMessageStreamEvent],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1536, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/anthropic/_base_client.py", line 1195, in request
    raise self._make_status_error_from_response(response) from None
anthropic.OverloadedError: Error code: 529 - {'type': 'error', 'error': {'type': 'overloaded_error', 'message': 'Overloaded'}, 'request_id': 'req_011CdztJqHgjG2ubi9oYBoK7'})
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
The BroadcastChannel used to sync auth across tabs is named **`triptic-auth-sync`**.
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 8.7s

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

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 4.3s

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
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 4.3s

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
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.5s

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

