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
[redacted: 714 chars about a private codebase]
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
[redacted: 414 chars about a private codebase]
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
[redacted: 283 chars about a private codebase]
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
[redacted: 230 chars about a private codebase]
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
[redacted: 238 chars about a private codebase]
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
[redacted: 250 chars about a private codebase]
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
[redacted: 403 chars about a private codebase]
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
[redacted: 269 chars about a private codebase]
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
[redacted: 591 chars about a private codebase]
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
[redacted: 598 chars about a private codebase]
```

---

