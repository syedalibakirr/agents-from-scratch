# Flood Test Results

Comparing the same 3-tool agent under two conditions: `clean` (3 real tools) vs `flood` (3 real tools + 50 fake, never-callable tools). No grading here — just what the agent called and what it said.

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.8s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (via LiteLLM), and the `embedding` column in the `counselor_insights_embeddings` table is defined as `vector(1536)` — i.e., it expects 1536-dimensional vectors.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.2s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (used via LiteLLM), and the database's `embedding` column is defined as `vector(1536)` — i.e., it expects 1536-dimensional vectors (see `database/migrations/create_counselor_insights_embeddings.sql`, line 26).
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.4s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (accessed via LiteLLM), and the `embedding` column in `counselor_insights_embeddings` is defined as `vector(1536)` — i.e., it expects 1536-dimensional vectors.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 8.7s

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
The semantic search uses OpenAI's **`text-embedding-3-small`** model, and the database's `embedding` column expects a vector of dimension **1536** (`vector(1536)`), as defined in `database/migrations/create_counselor_insights_embeddings.sql`.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 4.7s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **`text-embedding-3-small`** model, and the database column expects a **1536-dimension vector** (`embedding vector(1536)`), as defined in `database/migrations/create_counselor_insights_embeddings.sql`.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.4s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (via LiteLLM), and the database column `embedding` in `counselor_insights_embeddings` is defined as `vector(1536)` — i.e., it expects 1536-dimensional vectors.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.1s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model, and the database column stores it as `vector(1536)` — i.e., a 1536-dimensional embedding.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.1s

**Tool call count:** 2

**Tools called, in order:**
```
search({"query": "embedding"})
list_files({})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model, and the database column (`embedding` in `counselor_insights_embeddings`) expects a **`vector(1536)`** dimension.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.8s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses **OpenAI's `text-embedding-3-small`** model (accessed via LiteLLM), and the vector column in the database is defined as **`vector(1536)`** (see `counselor_insights_embeddings.embedding` in `database/migrations/create_counselor_insights_embeddings.sql`), matching that model's 1536-dimensional output.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 8.1s

**Tool call count:** 2

**Tools called, in order:**
```
search({"query": "embedding"})
search({"query": "text-embedding-3-small"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **`text-embedding-3-small`** model (configured via `EMBEDDINGS_MODEL_ID` in `python-backend/config.py`, defaulting to that model, accessed through LiteLLM).

The corresponding database column expects a **1536-dimensional vector** — e.g., in `database/migrations/create_counselor_insights_embeddings.sql`:

```sql
embedding vector(1536) NOT NULL
```

This matches the 1536-dimension output of `text-embedding-3-small`, as noted in `python-backend/models/ai_models.py`.
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.4s

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

**Wall time:** 5.1s

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
The BroadcastChannel used to sync auth across tabs is named **`triptic-auth-sync`**.
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 3.8s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "BroadcastChannel"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The BroadcastChannel used to sync auth state across tabs is named **`triptic-auth-sync`**.
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.8s

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

**Wall time:** 3.9s

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

**Wall time:** 4.1s

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

**Wall time:** 4.8s

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

**Wall time:** 6.2s

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

**Wall time:** 4.1s

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

