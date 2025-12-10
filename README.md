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

## Series Contents

| Part | Name | Description | Notebook |
|------|------|-------------|----------|
| **Part 1** | **Knowledge Graph Fundamentals** | Learn Cypher query language using a movie dataset. Covers pattern matching, aggregations, path finding, centrality metrics, and multi-role analysis. Explores MATCH vs OPTIONAL MATCH, COLLECT() to avoid Cartesian products, and analyzing disconnected graph components. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](src/graph_rag/movies_dataset/query-with-cypher.ipynb) |
| **Part 2** | **Building Knowledge Graphs from Text** | Transform unstructured SEC 10-K filings into a queryable knowledge graph with vector search. Covers document chunking strategies, graph node creation with Cypher MERGE, vector embeddings with OpenAI, Neo4j vector indexing, and building a complete RAG pipeline with LangChain. Includes hallucination testing and prompt engineering techniques. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](src/graph_rag/SEC_dataset/construct-kg-from-text.ipynb) |
| **Part 3** | **Entity Extraction & Relationship Modeling** | *Coming soon* - Extract entities (companies, people, products, risks) from SEC filings and model relationships. Build multi-document knowledge graphs with DISCLOSED_RISK, COMPETITOR_OF, and INVESTED_IN relationships. | *Coming soon* |
| **Part 4** | **Hybrid Queries: Vector Search + Graph Traversal** | *Coming soon* - Combine vector similarity search with Cypher graph traversal to answer complex multi-hop questions like "Which competitors of NetApp disclosed AI risks and invested >$50M in R&D?" | *Coming soon* |
| **Part 5** | **Advanced Retrieval Patterns** | *Coming soon* - Explore chunk windows, parent-child relationships, geospatial queries, and context expansion techniques for production-grade Graph RAG systems. | *Coming soon* |
| **Part 6** | **Natural Language to Cypher** | *Coming soon* - Use LLMs to generate Cypher queries from natural language questions. Build an intelligent query interface with error handling and query validation. | *Coming soon* |

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

## Datasets

### Part 1: Movie Knowledge Graph
- **7 Movies**: Matrix trilogy, Top Gun, Jerry Maguire, A Few Good Men, The Devil's Advocate
- **38 People**: Actors, directors, producers, writers
- **Relationships**: ACTED_IN, DIRECTED, PRODUCED, WROTE
- **Focus**: Learning Cypher fundamentals, graph patterns, and centrality metrics

### Part 2: SEC 10-K Filing - NetApp
- **Source**: [NetApp 10-K (SEC Filing 0000950170-23-027948)](https://www.sec.gov/Archives/edgar/data/1002047/000095017023027948/0000950170-23-027948-index.htm)
- **Sections Processed**: Item 1 (Business), Item 1A (Risk Factors), Item 7 (MD&A), Item 7A (Market Risk)
- **Text Chunks**: 257 chunks (2000 characters each, 200 character overlap)
- **Embeddings**: 1536-dimensional vectors (OpenAI text-embedding-ada-002)
- **Focus**: Document chunking, vector search, RAG pipeline, hallucination control

## Key Concepts Covered

### Graph Database Fundamentals (Part 1)
- **Cypher Query Language**: MATCH, WHERE, RETURN, OPTIONAL MATCH
- **Pattern Matching**: Node and relationship patterns
- **Aggregations**: COUNT(), COLLECT(), AVG(), DISTINCT
- **Path Finding**: shortestPath(), variable-length relationships
- **Centrality Metrics**: Degree centrality, betweenness centrality
- **Advanced Patterns**: UNWIND for array processing, handling Cartesian products

### Graph RAG Pipeline (Part 2)
- **Document Processing**: Chunking strategies with LangChain's RecursiveCharacterTextSplitter
- **Graph Construction**: Cypher MERGE for idempotent operations, constraints for data integrity
- **Vector Embeddings**: OpenAI embeddings, storing vectors in Neo4j
- **Vector Indexing**: Cosine similarity search with Neo4j vector indexes
- **RAG with LangChain**: Neo4jVector, RetrievalQAWithSourcesChain, source attribution
- **Production Considerations**: Hallucination control, prompt engineering, similarity thresholds

## LinkedIn Series

Follow along with the learning journey on LinkedIn:

- **Part 1**: [Knowledge Graph Fundamentals with Cypher](linkedin_posts/linkedin_post_2.txt) - The OPTIONAL MATCH discovery and centrality metrics
- **Part 2**: [Building Knowledge Graphs from SEC Filings](linkedin_posts/linkedin_post_3.txt) - Document chunking, vector embeddings, and the hallucination problem
- **Part 3**: *Coming soon* - Entity extraction and relationship modeling

## What's Next?

### Part 3: Entity Extraction & Relationship Modeling
- Use LLMs to extract structured entities from text chunks
- Create dedicated nodes for companies, people, products, risks
- Model relationships: DISCLOSED_RISK, COMPETITOR_OF, INVESTED_IN, MENTIONS
- Link chunks to entities for enhanced retrieval

### Part 4: Hybrid Queries
- Combine vector similarity with graph traversal in single queries
- Answer complex questions: "Which competitors of NetApp disclosed AI risks?"
- Implement filtering by metadata (year, section, company)
- Explore sequential chunk reading and context expansion

### Part 5 & Beyond
- Multi-document knowledge graphs (integrate Form 13-F investment data)
- Temporal analysis (year-over-year risk disclosure changes)
- Advanced retrieval patterns (chunk windows, parent-child relationships)
- Natural language to Cypher generation with LLMs
