# Graph RAG Learning Series

A hands-on learning journey exploring Graph RAG - combining knowledge graphs with retrieval augmented generation to answer complex questions that traditional RAG systems cannot handle.

**Part of the SWYL (Share What You Learn) series.**

## About This Series

Traditional RAG excels at semantic similarity but fails with:
- Geographical reasoning ("within 10km")
- Relationship traversal (connecting entities across documents)
- Numerical filtering (">$50M investments")
- Multi-document synthesis

This series explores how Graph RAG solves these problems by modeling relationships between entities in a knowledge graph, then combining vector search with graph traversal.

**Inspired by**: [DeepLearning.AI's Knowledge Graphs for RAG course](https://learn.deeplearning.ai/courses/knowledge-graphs-rag/)

## Series Roadmap

**Current**: Knowledge Graph Fundamentals (using movie dataset)
- Nodes, relationships, and Cypher query language
- Pattern matching and aggregations
- Path finding and centrality metrics

**Coming Next**:
1. Building SEC Knowledge Graphs - Chunking Form 10-K, creating embeddings
2. Relationship modeling - Connecting chunks, forms, preserving hierarchy
3. Multi-document integration - Form 13-F investment data
4. Advanced retrieval - Chunk windows, geospatial queries, context expansion
5. LLM-powered queries - Natural language to Cypher generation

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
