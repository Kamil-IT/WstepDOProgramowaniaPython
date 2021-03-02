import math


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # generic


class Stack:

    def __init__(self):
        self.length = 0
        self.head = None

    def __str__(self):
        if not self.empty():
            node = self.head
            for i in range(self.length):
                print(f'Node {i + 1}: {node}')
                node = node.next
            return ''
        else:
            return 'Empty stack'

    def __len__(self):
        return self.length

    def copy(self):
        return self

    def empty(self):
        return self.length == 0

    def push(self, data):
        node = Node(data)
        if self.empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self):
        if self.empty():
            raise ValueError('Empty stack')
        node = self.head
        node_data = node.data
        if self.head.next is None:  # self.length == 1
            self.head = None
        else:
            self.head = self.head.next
        node.next = None  # clearing connection
        self.length -= 1
        return node_data


class Graph:
    def __init__(self, graph=[]):
        self.graph = graph
        self.n = len(self.graph)

    def max_weight(self):
        max_weight = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.graph[i][j] > max_weight:
                    max_weight = self.graph[i][j]
        return max_weight

    def connected_components(self):
        C = [0] * self.n
        c_n = 0  # amount of connected components
        stack = Stack()

        for i in range(self.n):
            if C[i] > 0:
                continue
            c_n += 1
            stack.push(i)
            C[i] = c_n
            while not stack.empty():
                v = stack.pop()
                for u in range(self.n):
                    if self.graph[v][u] > 0:
                        if C[u] > 0:
                            continue
                        stack.push(u)
                        C[u] = c_n

        for i in range(1, c_n + 1):
            nodes = []
            for j in range(self.n):
                if C[j] == i:
                    nodes.append(j + 1)
            print(f'Top {i} : {nodes}')

    def dijkstra(self, v):
        d = [math.inf] * self.n
        p = [False] * self.n
        d[v] = 0
        for _ in range(self.n):
            min = math.inf
            u = None
            for i in range(self.n):
                if d[i] < min and p[i] == False:
                    min = d[i]
                    u = i
            if u != None:
                p[u] = True
            for w in range(self.n):
                weight = None
                if u != None:
                    weight = self.graph[u][w]
                else:
                    weight = 0

                if weight > 0 and p[w] == False and d[w] > d[u] + weight:
                    d[w] = d[u] + weight
        for node in range(self.n):
            if node != v:
                if d[node] == math.inf:
                    print(f'{node}: No connection')
                else:
                    print(f'{node}: {d[node]}')

    def kruskal_find(self, p, i):
        while p[i] != i:
            i = p[i]
        return i

    def kruskal_union(self, p, i, j):
        a = self.kruskal_find(p, i)
        b = self.kruskal_find(p, j)
        p[a] = b

    def kruskal(self):
        p = [i for i in range(self.n)]
        cost = self.graph
        for i in range(self.n):
            for j in range(self.n):
                if cost[i][j] == 0:
                    cost[i][j] = math.inf

        min_cost = 0
        for i in range(self.n):
            p[i] = i
        edge_count = 0
        while edge_count < self.n - 1:
            min = math.inf
            a = -1
            b = -1
            for i in range(self.n):
                for j in range(self.n):
                    if self.kruskal_find(p, i) != self.kruskal_find(p, j) and cost[i][j] < min:
                        min = cost[i][j]
                        a = i
                        b = j
            self.kruskal_union(p, a, b)
            print(f'Node {edge_count}: ({a}, {b})  |  price: {min}')
            edge_count += 1
            min_cost += min

        print(f'Min price: {min_cost}')

    def prim_is_valid_edge(self, u, v, mst):
        if u == v:
            return False
        if mst[u] == False and mst[v] == False:
            return False
        elif mst[u] == True and mst[v] == True:
            return False
        return True

    def prim(self):
        cost = self.graph
        for i in range(self.n):
            for j in range(self.n):
                if cost[i][j] == 0:
                    cost[i][j] = math.inf

        mst = [False] * self.n  # minimum spanning tree
        mst[0] = True
        edge_count = 0
        min_cost = 0
        while edge_count < self.n - 1:
            min = math.inf
            a = -1
            b = -1
            for i in range(self.n):
                for j in range(self.n):
                    if cost[i][j] < min:
                        if self.prim_is_valid_edge(i, j, mst):
                            min = cost[i][j]
                            a = i
                            b = j
            if a != -1 and b != -1:
                print(f'Node: {edge_count}: ({a}, {b})  |  price: {min}')
                edge_count += 1
                min_cost += min
                mst[b] = mst[a] = True

        print(f'Min price: {min_cost}')


g = Graph([
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
])

print('Graph')
print(g.graph)

print('ex1')
g.connected_components()

print('ex2')
g.dijkstra(0)

print('ex3')
print('Kruskal:')
g.kruskal()

print('Prim:')
g.prim()
