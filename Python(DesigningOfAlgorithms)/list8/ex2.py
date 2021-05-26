from collections import defaultdict

import networkx as nx
from matplotlib import pyplot as plt


# odwiedzamy wszystkich sąsiadów /przeszukiwanie w szerz
class GraphBFS:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = [s]

        visited[s] = True

        history_queue = []

        while queue:
            s = queue.pop(0)
            history_queue.append(s)
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    history_queue.append(i)
                    visited[i] = True
        return history_queue


class GraphDFS:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS_calculate(self, v, visited, all_checked):
        visited.append(v)
        for neighbour in self.graph[v]:
            all_checked.append(neighbour)
            if neighbour not in visited:
                self.DFS_calculate(neighbour, visited, all_checked)

    def DFS(self, v):
        visited = []
        all_checked = []
        self.DFS_calculate(v, visited, all_checked)
        return visited


def is_graph_connected(edges, g_DFS):
    for i in edges:
        if i not in list(g_DFS.DFS(2)):
            return False

    return True


def is_graph_tree(g_DFS, g_BFS, edges):
    if is_graph_connected(edges, g_DFS):
        if len(g_BFS.bfs(2)) == len(edges):
            return True
    return False


def is_graph_forest(edges):
    e = defaultdict(list)
    for t, f in edges:
        e[t].append(f)
        e[f].append(t)

    seen = set()

    def dfs(node, prev):
        if node in seen:
            return False
        seen.add(node)
        for adj in e[node]:
            if adj != prev:
                if not dfs(adj, node):
                    return False
        return True

    for node in e:
        if node not in seen and not dfs(node, -1):
            return False

    return True


edges = [0, 1, 2, 3]
edges_connections = [(0, 1), (1, 0), (0, 2), (1, 2), (2, 1), (2, 0), (2, 3), (3, 2), (3, 3), (3, 4), (4, 3)]

g_BFS = GraphBFS()
for i in edges_connections:
    g_BFS.add_edge(i[0], i[1])

g_DFS = GraphDFS()
for i in edges_connections:
    g_DFS.add_edge(i[0], i[1])

visited_bfs = g_BFS.bfs(2)
visited_dfs = g_DFS.DFS(2)

print(f'bfs : ' + str(visited_bfs))
print(f'dfs : ' + str(visited_dfs))

print(f'Is graph connected: {is_graph_connected(edges, g_DFS)}')
print(f'Is graph tree: {is_graph_tree(g_DFS, g_BFS, edges)}')
print(f'Is graph forest: {is_graph_forest(edges_connections)}')

G = nx.Graph()
for i in edges_connections:
    G.add_edge(i[0], i[1])

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)

plt.show(block=False)
plt.pause(1)

for visited in visited_dfs:
    colors = []

    for i in G.nodes():
        if visited == i:
            colors.append('r')
        else:
            colors.append('b')

    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)

    plt.clf()
    nx.draw(G, pos, node_color=colors, with_labels=True)
    plt.draw()
    plt.pause(1)

pos = nx.spring_layout(G)
for visited in visited_bfs:
    colors = []

    for i in G.nodes():
        if visited == i:
            colors.append('r')
        else:
            colors.append('b')

    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)

    plt.clf()
    nx.draw(G, pos, node_color=colors, with_labels=True)
    plt.draw()
    plt.pause(1)
