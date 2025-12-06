# Graph RAG Learning Series

Learning Graph RAG fundamentals using Neo4j and Cypher query language. Part of the SWYL (Share What You Learn) series.

## Setup

1. Create virtual environment:
```bash
uv venv
```

2. Activate virtual environment:
```bash
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
uv pip install -e .
```

4. Set up environment variables:
```bash
cp .env.example .env
# Add your Neo4j credentials and OpenAI API key
```

## What's Inside

### Movie Knowledge Graph Analysis
- **Notebook**: `src/graph_rag/l2-query-with-cypher.ipynb`
- **Dataset**: 7 movies, 38 people (actors, directors, producers, writers)
- **Queries**: 9 Cypher queries (Easy → Medium → Hard)
- **Topics**: Pattern matching, aggregations, path finding, centrality metrics, multi-role analysis

### Key Learnings
- MATCH vs OPTIONAL MATCH (INNER JOIN vs LEFT JOIN)
- COLLECT() + DISTINCT to avoid Cartesian products
- Degree centrality vs Betweenness centrality
- Analyzing disconnected graph components
- UNWIND for processing arrays

## Next Steps

Moving from movies to SEC filings:
- Chunking Form 10-K documents
- Creating vector embeddings
- Building financial knowledge graphs
- Combining vector search with graph traversal
