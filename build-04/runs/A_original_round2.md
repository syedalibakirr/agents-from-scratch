# Flood Test Results

Comparing the same 3-tool agent under two conditions: `clean` (3 real tools) vs `flood` (3 real tools + 50 fake, never-callable tools). No grading here — just what the agent called and what it said.

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
The semantic search uses OpenAI's **text-embedding-3-small** model (used via LiteLLM alongside GPT-4o), and the `embedding` column in the `counselor_insights_embeddings` table is defined as `vector(1536)` — i.e., it expects 1536-dimensional vectors.
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
The semantic search uses OpenAI's **text-embedding-3-small** model (via LiteLLM), and the database column (`embedding vector(1536)` in `counselor_insights_embeddings`) expects a **1536-dimensional** vector.
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
The semantic search uses OpenAI's **text-embedding-3-small** model (accessed via LiteLLM), and the database column is defined as `vector(1536)` — i.e., it expects 1536-dimensional embedding vectors.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.3s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model (accessed via LiteLLM), and the `embedding` column in `counselor_insights_embeddings` is defined as `vector(1536)` — expecting 1536-dimensional vectors.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 4.0s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses OpenAI's **text-embedding-3-small** model, and the database column expects a **1536-dimension vector** (`embedding vector(1536) NOT NULL` in `counselor_insights_embeddings`).
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
The semantic search uses OpenAI's **text-embedding-3-small** model (accessed via LiteLLM), and the database column is defined as **vector(1536)** — i.e., it expects 1536-dimensional embedding vectors (matching `counselor_insights_embeddings.embedding vector(1536) NOT NULL`).
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.7s

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
The semantic search uses OpenAI's **text-embedding-3-small** model (used alongside GPT-4o via LiteLLM), and the database column expects a **vector(1536)** dimension, as seen in the `embedding vector(1536) NOT NULL` column definition and matching `query_embedding vector(1536)` parameter in the migration files, and confirmed by the comment in `python-backend/config.py` noting it "must match the vector(1536) dimension in college_embeddings and student_activity_embeddings tables."
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 9.6s

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
The semantic search uses OpenAI's **`text-embedding-3-small`** model (as confirmed in both `README.md` and `CLAUDE.md`, used via LiteLLM).

The vector column is defined as **`vector(1536)`** — a 1536-dimensional vector — as seen in `database/migrations/create_counselor_insights_embeddings.sql` (`embedding vector(1536) NOT NULL`) and confirmed in `python-backend/config.py`, which notes this dimension must match across the `college_embeddings`, `student_activity_embeddings`, and `counselor_insights_embeddings` tables.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.7s

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
The semantic search uses OpenAI's **`text-embedding-3-small`** model (used alongside GPT-4o via LiteLLM for the AI layer, as noted in both the README and CLAUDE.md).

The corresponding database column, `embedding` in the `counselor_insights_embeddings` table, expects a **`vector(1536)`** dimension (using pgvector), which matches the 1536-dimensional output of `text-embedding-3-small`.
```

---

## Q2 — clean

**Question:** What embedding model does the semantic search use, and what vector dimension does the column expect?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 6.1s

**Tool call count:** 1

**Tools called, in order:**
```
search({"query": "embedding"})
```

**Fake-tool attempts:**
(none)

**Final answer (verbatim):**
```
The semantic search uses **OpenAI's `text-embedding-3-small`** model (via LiteLLM), and the corresponding database column (`embedding` in `counselor_insights_embeddings`) is defined as `vector(1536)` — i.e., it expects 1536-dimensional vectors.
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 4.5s

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

**Wall time:** 5.2s

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
The BroadcastChannel used to sync auth across tabs is named **`triptic-auth-sync`**.
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

**Wall time:** 3.7s

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
The BroadcastChannel used to sync auth across tabs is named **`triptic-auth-sync`**.
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
The BroadcastChannel used to sync auth across tabs is named **`triptic-auth-sync`**.
```

---

## Q8 — clean

**Question:** What is the name of the BroadcastChannel used to sync auth across tabs?

**Condition:** clean (FLOOD unset, 3 tools)

**Wall time:** 5.6s

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

