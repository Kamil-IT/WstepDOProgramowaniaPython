import random

import matplotlib.pyplot as plt
import networkx as nx


def usl(a, b):
    galleries = list(a.nodes)

    current_gallery = random.choice(galleries)
    a.nodes[current_gallery]['service'] = L[0]

    c = a.copy()
    j = 1
    for gallery in galleries:
        if gallery == current_gallery:
            continue

        services = [a.nodes[gal]['service'] for gal in list(a.neighbors(gallery))]
        if L[j] in services:
            j += 1
            if j >= len(L):
                print('You cant have different services in near galleries')
                c.remove_node(current_gallery)
                return usl(c, 0)
        a.nodes[gallery]['service'] = L[j]

    return a


# Services
L = ['clothes', 'coins', 'boots', 'tv', 'xbox', 'psp', 'wc', 'translator']

# Galleries
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'D')
G.add_edge('A', 'C')
G.add_edge('E', 'D')
nx.set_node_attributes(G, 'fake', "service")

a = usl(G, G)

# Draw graph
pos = nx.circular_layout(a)
node_labels = nx.get_node_attributes(a, 'service')
nx.draw_networkx_labels(a, pos, labels=node_labels)
nx.draw_networkx_nodes(a, pos, node_size=1500)
nx.draw_networkx_edges(a, pos)
plt.show()