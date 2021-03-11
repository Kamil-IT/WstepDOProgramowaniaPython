import networkx as nx
import matplotlib.pyplot as plt

number_vertices = 10

G = nx.complete_graph(number_vertices)
pos = nx.circular_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)

plt.show()
