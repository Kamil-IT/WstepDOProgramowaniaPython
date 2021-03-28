import networkx as nx
from scipy.spatial import distance


def dist(v, w):
    travel = nx.shortest_path(G, source=v, target=w)
    print('Path ' + str(travel))
    dis = 0
    for i in range(len(travel) - 1):
        dis += distance.euclidean(pos[travel[i] - 1], pos[travel[i]])
    print('Distance ' + str(dis))


G = nx.Graph()

pos = [(1, 2), (2, 3), (3, 4), (7, 5)]

G.add_weighted_edges_from([(1, 2, 1)])
G.add_weighted_edges_from([(2, 3, 2)])
G.add_weighted_edges_from([(3, 4, 3)])
G.add_weighted_edges_from([(7, 5, 4)])

dist(1, 4)
