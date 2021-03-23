import math
import random
import sys

import matplotlib.pyplot as plt
import networkx as nx


def close_connection(key, keys, pos):
    min_distance = sys.maxsize
    min_connection_key = key
    for key_connect in keys:
        if key_connect != key and (key, key_connect) not in G.edges and (key_connect, key) not in G.edges:
            current_distance = math.sqrt(
                (pos[key][0] - pos[key_connect][0]) ** 2 + (pos[key_connect][1] - pos[key][1]) ** 2)
            if min_distance > current_distance:
                min_distance = current_distance
                min_connection_key = key_connect

    return min_connection_key


def find_random_positions(random_seed, graph_width, graph_length, size):
    random.seed(random_seed)
    pos = {}
    while len(pos) < graph_element_number:
        location = (random.randint(0, graph_width), random.randint(0, graph_length))
        if location not in pos.values():
            location_name = str(location[0]) + ',' + str(location[1])
            pos[location_name] = location
    return pos


# Graph properties
graph_length = 100
graph_width = 100
graph_element_number = 5

pos = find_random_positions(25, graph_width, graph_length, graph_element_number)

G = nx.Graph()

# Constrain edges
keys = list(pos.keys())
edges = []
min_connection_key = keys[0]
for key in keys:

    if key == keys[0]:
        min_connection_key = close_connection(key, keys, pos)
    else:
        min_connection_key = close_connection(key, [i[0] for i in edges], pos)

    edges.append((key, min_connection_key))

# Plot diagram

for edge in edges:
    # Draw graph
    G.add_edge(edge[0], edge[1])
    label = str(
        round(
            math.sqrt(
                (pos[edge[0]][0] - pos[edge[1]][0]) ** 2 +
                (pos[edge[1]][1] - pos[edge[0]][1]) ** 2),
            2))
    G.add_weighted_edges_from([(edge[0], edge[1], label)])
    nx.set_node_attributes(G, pos, 'coord')
    nx.draw_networkx_nodes(G, pos, node_size=200)
    nx.draw_networkx_labels(G, pos, font_size=10)
    plt.show()
    plt.pause(1)

pos_show = {}
labels = {}
full_labels = nx.get_edge_attributes(G, 'weight')
for label_key in full_labels.keys():
    nx.set_node_attributes(G, pos, 'coord')
    nx.draw_networkx_nodes(G, pos, node_size=200)
    nx.draw_networkx_labels(G, pos, font_size=10)
    labels[label_key] = full_labels[label_key]
    pos_show[label_key[0]] = pos[label_key[0]]
    pos_show[label_key[1]] = pos[label_key[1]]
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos_show, edge_labels=labels)
    plt.show()
    plt.pause(1)

# uncomment to enable connections with edges
# nx.draw_networkx_edges(G, pos)

# plt.show()
