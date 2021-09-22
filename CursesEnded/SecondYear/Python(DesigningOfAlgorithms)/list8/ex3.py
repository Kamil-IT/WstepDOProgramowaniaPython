# Python program to print topological sorting of a DAG
from collections import defaultdict

# Class to represent a graph
import networkx as nx
from matplotlib import pyplot as plt
from networkx import Graph


class GraphTopological:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_calculate(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_calculate(i, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_calculate(i, visited, stack)

        print(stack)
        return stack


def time_for_job_started(time, best_sequence, edges_connections):
    # connections = [(index, connections, time), ...]
    jobs = [[i, list(edges_connections[i].keys()), None] for i in best_sequence]
    time = [time[i] for i in best_sequence]
    current_time = 0
    job_processed = []

    for i in range(len(jobs)):

        job_processing = jobs[i]

        if job_processing not in job_processed:

            if len(jobs) == i + 1:
                job_processing[2] = current_time
                job_processed.append(job_processing)
            e = 0
            while job_processing is not None and len(jobs) > i + e + 1:
                e += 1
                next_job = jobs[i + e]

                if next_job[0] not in job_processing[1] and job_processing[0] not in next_job[1]:
                    job_processing[2] = current_time
                    job_processed.append(job_processing)
                else:
                    job_processing[2] = current_time
                    job_processed.append(job_processing)
                    job_processing = None
            current_time += time[i]
    return job_processed


time = [10, 15, 7, 9, 10, 11, 12]
edges_connections = [(3, 6), (5, 2), (4, 0), (4, 1), (2, 3), (3, 4)]

g = GraphTopological(7)
for i in edges_connections:
    g.add_edge(i[0], i[1])

best_job_processing = g.topological_sort()

G = Graph()
for i in edges_connections:
    G.add_edge(i[0], i[1])
    G.add_edge(i[1], i[0])
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)

plt.show()


times_jobs = [i[len(i) - 1] for i in time_for_job_started(time, best_job_processing, G.adj._atlas)]

labeldict = {}
for i in range(len(best_job_processing)):
    labeldict[best_job_processing[i]] = times_jobs[i]
nx.draw(G, pos, labels=labeldict, with_labels=True)

plt.show()
