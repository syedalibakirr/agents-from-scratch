# Flood Test Results

Comparing the same 3-tool agent under two conditions: `clean` (3 real tools) vs `flood` (3 real tools + 50 fake, never-callable tools). No grading here — just what the agent called and what it said.

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 13.7s

**Tool call count:** 4

**Tools called, in order:**
```
search({"query": "embedding"})
search({"query": "vector("})
read_file({"path": "python-backend/config.py"})
read_file({"path": "database/migrations/create_counselor_insights_embeddings.sql"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
Based on the codebase, the semantic search / RAG pipeline uses:

**Embedding model:** OpenAI's `text-embedding-3-small` (referenced in `README.md`, `CLAUDE.md`, and configured via the `EMBEDDINGS_MODEL_ID` setting in `python-backend/config.py`).

**Vector dimension:** The database columns are defined as `vector(1536)` — this is used consistently across:
- `counselor_insights_embeddings.embedding`
- `college_embeddings`
- `student_activity_embeddings`

A comment in `config.py` explicitly notes: *"Must match the vector(1536) dimension in college_embeddings and student_activity_embeddings tables"* — confirming that `text-embedding-3-small`'s 1536-dimensional output is what the pgvector columns are built for.
```

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
The semantic search uses **OpenAI's `text-embedding-3-small`** model (accessed via LiteLLM, alongside GPT-4o for other AI tasks).

The corresponding database column is defined as **`vector(1536)`** — e.g., `embedding vector(1536) NOT NULL` in `counselor_insights_embeddings`, and the same 1536-dimension vector type is used consistently across `college_embeddings` and `student_activity_embeddings` tables as well.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 7.1s

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
The semantic search uses OpenAI's **text-embedding-3-small** model (used alongside GPT-4o via LiteLLM), and the vector columns (e.g., `embedding` in `counselor_insights_embeddings`, `college_embeddings`, `student_activity_embeddings`) expect a dimension of **1536** (`vector(1536)`).
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.7s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model, and the database column expects a **1536-dimension vector** (`embedding vector(1536) NOT NULL` in `database/migrations/create_counselor_insights_embeddings.sql`).
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.6s

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
The semantic search uses OpenAI's **text-embedding-3-small** model, and the database column expects a **vector(1536)** dimension (as seen in `counselor_insights_embeddings`, `college_embeddings`, and `student_activity_embeddings` tables).
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.5s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (via LiteLLM), and the database column is defined as **`vector(1536)`** — i.e., it expects 1536-dimensional embedding vectors (matching `text-embedding-3-small`'s native output size).
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 17.2s

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
The semantic search uses **OpenAI's `text-embedding-3-small`** model (accessed via LiteLLM), configured in `python-backend/config.py` via `EMBEDDINGS_MODEL_ID`.

The corresponding vector column — e.g., `embedding` in the `counselor_insights_embeddings` table — is defined as `vector(1536)`, meaning it expects **1536-dimensional** embeddings, matching the native output size of `text-embedding-3-small`.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 8.9s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (via LiteLLM), and the database's `embedding` column is defined as **`vector(1536)`** (a 1536-dimensional pgvector column, indexed with `ivfflat`/`vector_cosine_ops`) in `counselor_insights_embeddings`.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 8.6s

**Tool call count:** 3

**Tools called, in order:**
```
search({"query": "embedding"})
search({"query": "text-embedding-3-small"})
read_file({"path": "database/migrations/create_counselor_insights_embeddings.sql"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **`text-embedding-3-small`** model (accessed via LiteLLM, configurable through the `EMBEDDINGS_MODEL_ID` setting in `python-backend/config.py`, defaulting to `text-embedding-3-small`).

The corresponding database column expects a **1536-dimensional vector** — e.g., in `counselor_insights_embeddings`:

```sql
embedding vector(1536) NOT NULL
```

This matches `text-embedding-3-small`'s native output dimensionality of 1536, as also noted in `python-backend/models/ai_models.py` ("Uses text-embedding-3-small (1536 dimensions) to match the vector columns").
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 33.2s

**Tool call count:** 4

**Tools called, in order:**
```
search({"query": "embedding model"})
search({"query": "vector("})
search({"query": "text-embedding"})
read_file({"path": "python-backend/config.py"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **`text-embedding-3-small`** model (configurable via the `EMBEDDINGS_MODEL_ID` environment variable in `python-backend/config.py`, defaulting to this model).

The corresponding database columns expect a **1536-dimension vector** (`vector(1536)`), as seen in:
- `database/migrations/create_counselor_insights_embeddings.sql` — `embedding vector(1536)` and `query_embedding vector(1536)`
- Referenced also in `college_embeddings` and `student_activity_embeddings` tables, which must match this same 1536-dimension size to be compatible with `text-embedding-3-small`.
```

---

