from dotenv import load_dotenv
load_dotenv()

import os
from langchain_community.graphs import Neo4jGraph
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings("ignore")

NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
NEO4J_DATABASE = os.getenv('NEO4J_DATABASE')

print("Connecting to Neo4j...")
kg = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD, database=NEO4J_DATABASE)

# Fetch the graph data
print("Fetching graph data...")
query = """
MATCH (p:Person)-[r]-(m:Movie)
RETURN p.name as person, m.title as movie, type(r) as relationship
"""
result = kg.query(query)

# Build NetworkX graph
print("Building network graph...")
G = nx.Graph()

person_nodes = set()
movie_nodes = set()

for row in result:
    person = row['person']
    movie = row['movie']
    rel_type = row['relationship']

    person_nodes.add(person)
    movie_nodes.add(movie)

    # Add edge with relationship type as attribute
    G.add_edge(person, movie, relationship=rel_type)

print(f"Graph has {len(person_nodes)} people and {len(movie_nodes)} movies")
print(f"Total nodes: {G.number_of_nodes()}, Total edges: {G.number_of_edges()}")

# Calculate centrality metrics
print("\nCalculating centrality metrics...")
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# Get top 5 by each metric (only people)
print("\nTop 5 People by Degree Centrality:")
people_degree = {k: v for k, v in degree_centrality.items() if k in person_nodes}
for person, score in sorted(people_degree.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"  {person}: {score:.3f}")

print("\nTop 5 People by Betweenness Centrality:")
people_betweenness = {k: v for k, v in betweenness_centrality.items() if k in person_nodes}
for person, score in sorted(people_betweenness.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"  {person}: {score:.3f}")

# Create visualization
print("\nCreating visualization...")
fig, axes = plt.subplots(1, 2, figsize=(20, 10))

# Visualization 1: Full Network with node sizes by degree
ax1 = axes[0]
pos1 = nx.spring_layout(G, k=2, iterations=50, seed=42)

# Node sizes based on degree
node_sizes = [G.degree(node) * 300 for node in G.nodes()]

# Node colors: blue for people, orange for movies
node_colors = ['#3498db' if node in person_nodes else '#e74c3c' for node in G.nodes()]

nx.draw_networkx_nodes(G, pos1, node_size=node_sizes, node_color=node_colors,
                       alpha=0.7, ax=ax1)
nx.draw_networkx_edges(G, pos1, alpha=0.3, ax=ax1)
nx.draw_networkx_labels(G, pos1, font_size=8, font_weight='bold', ax=ax1)

ax1.set_title("Movie Network - Node Size = Degree (Connections)\nBlue = People, Red = Movies",
              fontsize=14, fontweight='bold')
ax1.axis('off')

# Visualization 2: Only People Network (projected)
ax2 = axes[1]

# Create person-to-person projection (people connected if they share a movie)
person_graph = nx.Graph()
for person in person_nodes:
    person_graph.add_node(person)

# Connect people who worked on the same movie
for movie in movie_nodes:
    neighbors = list(G.neighbors(movie))
    people_in_movie = [n for n in neighbors if n in person_nodes]

    # Create edges between all pairs of people in this movie
    for i, p1 in enumerate(people_in_movie):
        for p2 in people_in_movie[i+1:]:
            if person_graph.has_edge(p1, p2):
                person_graph[p1][p2]['weight'] += 1
            else:
                person_graph.add_edge(p1, p2, weight=1)

# Calculate betweenness for person graph
person_betweenness = nx.betweenness_centrality(person_graph)
max_betweenness = max(person_betweenness.values()) if person_betweenness.values() else 1

pos2 = nx.spring_layout(person_graph, k=3, iterations=50, seed=42)

# Node sizes based on betweenness centrality
node_sizes_2 = [person_betweenness.get(node, 0) * 5000 + 300 for node in person_graph.nodes()]

# Color based on betweenness (gradient)
node_colors_2 = [person_betweenness.get(node, 0) for node in person_graph.nodes()]

nodes = nx.draw_networkx_nodes(person_graph, pos2, node_size=node_sizes_2,
                               node_color=node_colors_2, cmap='YlOrRd',
                               alpha=0.8, ax=ax2, vmin=0, vmax=max_betweenness)

# Edge widths based on collaboration count
edges = person_graph.edges()
weights = [person_graph[u][v]['weight'] for u, v in edges]
nx.draw_networkx_edges(person_graph, pos2, width=[w*0.5 for w in weights],
                       alpha=0.4, ax=ax2)
nx.draw_networkx_labels(person_graph, pos2, font_size=7, font_weight='bold', ax=ax2)

ax2.set_title("Person Collaboration Network\nNode Size & Color = Betweenness Centrality\nEdge Width = # Shared Movies",
              fontsize=14, fontweight='bold')
ax2.axis('off')

# Add colorbar
plt.colorbar(nodes, ax=ax2, label='Betweenness Centrality')

plt.tight_layout()
plt.savefig('/Users/anirudhnuti/Documents/graph_rag/network_visualization.png',
            dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved to: network_visualization.png")

# Identify connected components
print("\n" + "="*60)
print("CONNECTED COMPONENTS ANALYSIS")
print("="*60)
components = list(nx.connected_components(person_graph))
print(f"\nNumber of disconnected components: {len(components)}")

for i, component in enumerate(components, 1):
    print(f"\nComponent {i} ({len(component)} people):")

    # Find the most central person in this component
    subgraph = person_graph.subgraph(component)
    sub_betweenness = nx.betweenness_centrality(subgraph)
    most_central = max(sub_betweenness.items(), key=lambda x: x[1])

    print(f"  Most central person: {most_central[0]} (betweenness: {most_central[1]:.3f})")
    print(f"  Members: {', '.join(sorted(component)[:10])}")
    if len(component) > 10:
        print(f"  ... and {len(component) - 10} more")

print("\n✓ Analysis complete!")
plt.show()
