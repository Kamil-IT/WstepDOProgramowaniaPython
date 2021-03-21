import networkx as nx
import matplotlib.pyplot as plt
from random import randint

# Graph properties
graph_length = 10
graph_width = 10
graph_element_number = 20

# Find position for edges
pos = {}
failed_found_number = 0
while failed_found_number < 100 and len(pos) < graph_element_number:
    location = (randint(0, graph_width), randint(0, graph_length))
    if location in pos.values():
        failed_found_number += 1
    else:
        location_name = str(location[0]) + ',' + str(location[1])
        pos[location_name] = location

if failed_found_number == 100:
    print("I cant generate good graph for you because I guessed 100 times wrong")

G = nx.Graph()

# Constrain edges
pos_key = list(pos.keys())
for pos_index in range(len(pos_key)):
    G.add_edge(pos_key[pos_index - 1], pos_key[pos_index])

# Draw graph
nx.set_node_attributes(G, pos, 'coord')
nx.draw_networkx_nodes(G, pos, node_size=200)
nx.draw_networkx_labels(G, pos, font_size=10)

# uncomment to enable connections with edges
# nx.draw_networkx_edges(G, pos)


plt.show()
