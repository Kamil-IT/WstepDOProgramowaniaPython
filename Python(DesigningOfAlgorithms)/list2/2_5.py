import matplotlib.pyplot as plt
import networkx as nx


def find_boreholes(D, R):
    boreholes = {}
    for i in range(boreholes_horizontally + 1):
        for j in range(boreholes_vertical + 1):
            boreholes[len(boreholes) + 1] = (i * D, j * D)
            if len(boreholes) == R:
                return boreholes
    return boreholes


# Graph length
N = 10
# Graph width
K = 10
# Distance between points
D = 3
# Min distance between boreholes (odwierty)
S = 2
# Quantity of boreholes (odwierty)
R = 7

# Find boreholes
boreholes_horizontally = int(N / D)
boreholes_vertical = int(K / D)
boreholes = find_boreholes(D, R)

# Draw graph
G = nx.Graph()
for i in range(1, len(boreholes) + 1):
    G.add_node(i)

G_plane = nx.Graph()
pos_plane = {}
for i in range(0, N):
    for j in range(0, K):
        label = 'number' + str(i) + str(j)
        G_plane.add_node(label)
        pos_plane[label] = (i, j)

nx.draw(G, boreholes, node_size=100, with_labels=False, node_color='r')
nx.draw(G_plane, pos_plane, node_size=25, with_labels=False, node_color='b')
plt.show()
