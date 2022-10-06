import networkx as nx
from matplotlib import pyplot as plt

G = nx.generators.random_graphs.powerlaw_cluster_graph(15, 5, 1)

color_map = ['red' if node == 1 else 'green' for node in G.nodes]
nx.draw(G, node_color=color_map)
plt.show()

edges = G.edges()

