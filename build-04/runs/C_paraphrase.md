# Flood Test Results

Comparing the same 3-tool agent under two conditions: `clean` (3 real tools) vs `flood` (3 real tools + 50 fake, never-callable tools). No grading here — just what the agent called and what it said.

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 7.6s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses **OpenAI's `text-embedding-3-small`** model (used via LiteLLM alongside GPT-4o), and the database column is defined as **`vector(1536)`** — expecting 1536-dimensional embedding vectors.

This is confirmed in:
- `database/migrations/create_counselor_insights_embeddings.sql`: `embedding vector(1536) NOT NULL`
- `README.md` and `CLAUDE.md`: reference `text-embedding-3-small` as the embedding model
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 9.9s

**Tool call count:** 3

**Tools called, in order:**
```
list_files({})
search({"query": "embedding"})
search({"query": "vector("})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search in this codebase uses OpenAI's **`text-embedding-3-small`** model (accessed via LiteLLM), and the database vector columns (e.g., `counselor_insights_embeddings.embedding`, `college_embeddings`, `student_activity_embeddings`) expect a **`vector(1536)`** dimension — i.e., 1536-dimensional embeddings.

This is confirmed in multiple places:
- `README.md` / `CLAUDE.md`: list the AI stack as "OpenAI GPT-4o via LiteLLM, text-embedding-3-small"
- `database/migrations/create_counselor_insights_embeddings.sql`: defines `embedding vector(1536) NOT NULL`
- `python-backend/config.py`: notes "Must match the vector(1536) dimension in college_embeddings and student_activity_embeddings tables"
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 9.3s

**Tool call count:** 2

**Tools called, in order:**
```
search({"query": "embedding"})
search({"query": "vector"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses **OpenAI's `text-embedding-3-small`** model, and the vector columns are defined as **`vector(1536)`** (1536 dimensions) in the PostgreSQL/pgvector schema.

This is confirmed across multiple places in the codebase:

- **README.md**: Lists `text-embedding-3-small` as the embedding model under the AI stack.
- **CLAUDE.md**: Table entry — `AI | OpenAI GPT-4o via LiteLLM | text-embedding-3-small`.
- **`python-backend/models/ai_models.py`**: "Uses text-embedding-3-small (1536 dimensions) to match the vector columns."
- **`python-backend/config.py`**: Comment noting the config value "Must match the `vector(1536)` dimension in `college_embeddings` and `student_activity_embeddings` tables."
- **`database/migrations/create_counselor_insights_embeddings.sql`**: Defines `embedding vector(1536) NOT NULL` and the matching RPC function parameter `query_embedding vector(1536)`.

So consistently, embeddings are generated with `text-embedding-3-small` and stored/queried against `vector(1536)` columns using pgvector (with cosine similarity via `ivfflat` indexes and `vector_cosine_ops`).
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 7.5s

**Tool call count:** 3

**Tools called, in order:**
```
list_files({})
search({"query": "embedding"})
search({"query": "vector("})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (accessed via LiteLLM, alongside GPT-4o for the AI features), and the vector column is defined as `vector(1536)` — a 1536-dimensional embedding, consistent across tables like `counselor_insights_embeddings`, `college_embeddings`, and `student_activity_embeddings`.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 8.3s

**Tool call count:** 3

**Tools called, in order:**
```
list_files({})
search({"query": "embedding"})
search({"query": "vector("})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model, and the vector column is defined as **vector(1536)** — i.e., 1536-dimensional embeddings.

This is confirmed across multiple places in the repo:
- `README.md`: "AI: OpenAI (GPT-4o via LiteLLM, text-embedding-3-small)"
- `CLAUDE.md`: same model listed for AI/embeddings
- `database/migrations/create_counselor_insights_embeddings.sql`: `embedding vector(1536) NOT NULL` and the RPC function parameter `query_embedding vector(1536)`
- `python-backend/config.py`: comment noting "Must match the vector(1536) dimension in college_embeddings and student_activity_embeddings tables"

So the embedding dimension (1536) matches the native output size of OpenAI's `text-embedding-3-small` model, and this is consistently enforced across the `counselor_insights_embeddings`, `college_embeddings`, and `student_activity_embeddings` tables.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.3s

**Tool call count:** 2

**Tools called, in order:**
```
search({"query": "embedding"})
search({"query": "vector"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model, and the vector column expects a dimension of **1536** (i.e., `vector(1536)` in the pgvector-backed PostgreSQL/Supabase tables like `counselor_insights_embeddings`, `college_embeddings`, and `student_activity_embeddings`).
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 4.8s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (accessed via LiteLLM), and the `embedding` column in the `counselor_insights_embeddings` table is defined as `vector(1536)` — expecting **1536-dimensional** vectors.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 7.2s

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
The semantic search uses **OpenAI's `text-embedding-3-small`** model (used alongside GPT-4o via LiteLLM), and the database column is defined as **`vector(1536)`** — i.e., it expects 1536-dimensional embedding vectors.

This is confirmed across multiple places in the repo:
- `README.md` / `CLAUDE.md` list `text-embedding-3-small` as the embedding model.
- `database/migrations/create_counselor_insights_embeddings.sql` defines `embedding vector(1536) NOT NULL` and a matching `query_embedding vector(1536)` parameter for the RPC search function.
- `python-backend/config.py` notes that the dimension must match `vector(1536)` used in the `college_embeddings` and `student_activity_embeddings` tables as well.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.2s

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
The semantic search uses **OpenAI's `text-embedding-3-small`** model (used via LiteLLM alongside GPT-4o for the AI features), and the corresponding database columns are typed as **`vector(1536)`** — i.e., they expect 1536-dimensional embeddings, consistent across tables like `counselor_insights_embeddings`, `college_embeddings`, and `student_activity_embeddings`.
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
The semantic search uses OpenAI's **text-embedding-3-small** model (used alongside GPT-4o via LiteLLM for the AI stack), and the vector column is defined as **vector(1536)** — i.e., it expects 1536-dimensional embeddings.

This is confirmed in multiple places:
- `README.md` / `CLAUDE.md`: list **text-embedding-3-small** as the embedding model.
- `database/migrations/create_counselor_insights_embeddings.sql`: defines `embedding vector(1536) NOT NULL` and the `match_counselor_insights_embeddings` RPC uses `query_embedding vector(1536)`.
- `python-backend/config.py`: notes that the dimension must match `vector(1536)` used in the `college_embeddings` and `student_activity_embeddings` tables as well.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 7.9s

**Tool call count:** 3

**Tools called, in order:**
```
list_files({})
search({"query": "embedding"})
search({"query": "vector("})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (accessed via LiteLLM), and the corresponding database columns expect a **vector(1536)** dimension — confirmed in `create_counselor_insights_embeddings.sql`, `college_embeddings`, and `student_activity_embeddings` tables, matching the 1536-dimensional output of `text-embedding-3-small`.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 4.4s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model, and the database column expects a vector dimension of **1536** (`embedding vector(1536)` in `counselor_insights_embeddings`).
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
The semantic search uses OpenAI's **text-embedding-3-small** model (used alongside GPT-4o via LiteLLM), and the database vector column is defined as **`vector(1536)`** — i.e., it expects 1536-dimensional embeddings, matching the output size of `text-embedding-3-small`.

This is confirmed across multiple places:
- `README.md` / `CLAUDE.md`: list `text-embedding-3-small` as the embedding model.
- `database/migrations/create_counselor_insights_embeddings.sql`: defines `embedding vector(1536) NOT NULL` for the `counselor_insights_embeddings` table, and the `match_counselor_insights_embeddings` RPC function takes `query_embedding vector(1536)`.
- `python-backend/config.py`: comments note the dimension "must match the `vector(1536)` dimension in `college_embeddings` and `student_activity_embeddings` tables," confirming the same 1536-dimensional standard is used consistently across the embedding tables.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.0s

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
The semantic search uses OpenAI's **text-embedding-3-small** model (per README.md and CLAUDE.md, used via LiteLLM alongside GPT-4o).

The vector column is defined as **`vector(1536)`** — i.e., it expects 1536-dimensional embeddings, consistent across tables like `counselor_insights_embeddings`, `college_embeddings`, and `student_activity_embeddings`.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 10.9s

**Tool call count:** 3

**Tools called, in order:**
```
search({"query": "embedding"})
search({"query": "vector("})
read_file({"path": "python-backend/config.py"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search in this repo uses **OpenAI's `text-embedding-3-small`** model (confirmed in `README.md`, `CLAUDE.md`, and referenced as `EMBEDDINGS_MODEL_ID` in `python-backend/config.py`).

The corresponding database columns are defined as **`vector(1536)`** — i.e., they expect 1536-dimensional embeddings. This is seen in:
- `database/migrations/create_counselor_insights_embeddings.sql` — `embedding vector(1536) NOT NULL`
- The same 1536 dimension is also used for `college_embeddings` and `student_activity_embeddings` tables, per the comment in `config.py`:
  > "Must match the vector(1536) dimension in college_embeddings and student_activity_embeddings tables"

So: **model = text-embedding-3-small**, **dimension = 1536**.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 9.9s

**Tool call count:** 4

**Tools called, in order:**
```
search({"query": "embedding"})
search({"query": "vector("})
read_file({"path": "python-backend/config.py"})
search({"query": "text-embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **`text-embedding-3-small`** model for generating embeddings (configured via `EMBEDDINGS_MODEL_ID` in `python-backend/config.py`, defaulting to `text-embedding-3-small`).

The corresponding vector columns (e.g., in `counselor_insights_embeddings`, `college_embeddings`, and `student_activity_embeddings` tables) are defined as **`vector(1536)`**, i.e., they expect **1536-dimensional** embeddings, matching the output size of `text-embedding-3-small`.
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
The semantic search uses OpenAI's **text-embedding-3-small** model, and the corresponding database column (`embedding` in `counselor_insights_embeddings`) is defined as **`vector(1536)`** — i.e., it expects 1536-dimensional vectors.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.6s

**Tool call count:** 2

**Tools called, in order:**
```
list_files({})
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses **OpenAI's `text-embedding-3-small`** model (via LiteLLM), and the database's `embedding` column is defined as `vector(1536)` — i.e., it expects 1536-dimensional vectors, matching that model's native output size.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 7.9s

**Tool call count:** 2

**Tools called, in order:**
```
search({"query": "embedding"})
search({"query": "vector"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **`text-embedding-3-small`** model, and the vector columns (e.g., `embedding` in `counselor_insights_embeddings`, `college_embeddings`, `student_activity_embeddings`, `student_essay_embeddings`) all expect a **1536-dimension** vector (`vector(1536)` in Postgres/pgvector).

This is confirmed in multiple places:
- `README.md` / `CLAUDE.md`: lists AI stack as "OpenAI GPT-4o via LiteLLM, text-embedding-3-small"
- `database/migrations/create_counselor_insights_embeddings.sql`: `embedding vector(1536) NOT NULL`
- `python-backend/config.py`: comment noting "Must match the vector(1536) dimension in college_embeddings and student_activity_embeddings tables"
- `python-backend/models/ai_models.py`: "Uses text-embedding-3-small (1536 dimensions) to match the vector columns"
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.8s

**Tool call count:** 2

**Tools called, in order:**
```
search({"query": "embedding"})
read_file({"path": "database/migrations/create_counselor_insights_embeddings.sql"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
Based on the repository:

- **Embedding model**: `text-embedding-3-small` (OpenAI, accessed via LiteLLM)
- **Vector dimension**: The `embedding` column in `counselor_insights_embeddings` is defined as `vector(1536)`, i.e., it expects 1536-dimensional vectors.

This matches OpenAI's `text-embedding-3-small` model, whose default output dimensionality is 1536.
```

---

