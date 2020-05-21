import random
import math
from Stack import Stack
 
class Graph:
  def __init__(self, graph=[]):
    self.graph = graph
    self.n = len(self.graph)
  
  def __str__(self):
    span = len(str( self.max_weight() )) # biggest number lenght
    output = ''

    # first row
    output += 'G'
    output += ' '*span  # spacing
    output += '│ '
    for i in range(self.n):
      output += f'{i+1} '
      output += ' '*( span - len(str(i+1)) )  # spacing
    output += '\n'
    # second row
    output += '─'*span  # spacing
    output += '─┼'
    for i in range(self.n):
      output += '─'*( span+1 )  # spacing
    output += '\n'
    # other rows
    for i in range(self.n):
      output += f'{i+1}'  # row number
      output += ' '*( span - len(str(i+1)) )  # spacing
      output += ' │ '
      for j in range(self.n):
        output += str(self.graph[i][j])
        output += ' '
        output += ' '*( span - len(str(self.graph[i][j])) )  # spacing
      output += '\n'

    return output

  def max_weight(self):
    max_weight = 0
    for i in range(self.n):
      for j in range(self.n):
        if self.graph[i][j] > max_weight:
          max_weight = self.graph[i][j]
    return max_weight

  def random(size=5, min=0, max=5, directed=False, loops=False):
    # create a blank matrix with zeroes
    graph = []
    for i in range(size):
      row = []
      for j in range(size):
        row.append(None)
      graph.append( row )
    
    for i in range(size):
      for j in range(size):
        if directed == False:
          if graph[j][i] == None:
            graph[i][j] = random.randint(min, max)
          else:
            graph[i][j] = graph[j][i]
        else:
          graph[i][j] = random.randint(min, max)

    if loops == False:
      for i in range(size):
        for j in range(size):
          if j == i:
            graph[i][j] = 0

    return graph


  def connected_components(self):
    C = [0]*self.n
    c_n = 0  # amount of connected components
    stack = Stack()

    for i in range(self.n):
      if C[i] > 0:
        continue
      c_n += 1
      stack.push(i)
      C[i] = c_n
      while stack.empty() == False:
        v = stack.pop()
        for u in range(self.n):
          if self.graph[v][u] > 0:
            if C[u] > 0:
              continue
            stack.push(u)
            C[u] = c_n

    print(f'Ilość spójnych składowych: {c_n}')
    for i in range(1, c_n+1):
      nodes = []
      for j in range(self.n):
        if C[j] == i:
          nodes.append(j+1)
      print(f'Wierzchołki {i} składowej: {nodes}')


  def dijkstra(self, v):
    d = [math.inf]*self.n
    p = [False]*self.n
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

        if weight > 0 and p[w] == False and d[w] > d[u]+weight:
          d[w] = d[u]+weight
    print(f'Najkrótsze ścieżki od wierzchołka {v} do wierzchołków:')
    for node in range(self.n):
      if node != v:
        if d[node] == math.inf:
          print(f'{node}: Brak połączenia')
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
    # generating a cost matrix where no connection is maximum weight
    cost = self.graph
    for i in range(self.n):
      for j in range(self.n):
        if cost[i][j] == 0:
          cost[i][j] = math.inf

    # Kruskal Algorithm
    min_cost = 0
    for i in range(self.n):
      p[i] = i
    edge_count = 0
    while edge_count < self.n-1:
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
      print(f'Węzeł {edge_count}: ({a}, {b})  |  Koszt: {min}')
      edge_count += 1
      min_cost += min

    print(f'Minimalny koszt: {min_cost}') 


  def prim_is_valid_edge(self, u, v, mst): 
    if u == v:
      return False
    if mst[u] == False and mst[v] == False:
      return False
    elif mst[u] == True and mst[v] == True:
      return False
    return True
    
  def prim(self):
    # generating a cost matrix where no connection is maximum weight
    cost = self.graph
    for i in range(self.n):
      for j in range(self.n):
        if cost[i][j] == 0:
          cost[i][j] = math.inf

    # Prim Algorithm
    mst = [False]*self.n  # minimum spanning tree
    mst[0] = True
    edge_count = 0
    min_cost = 0
    while edge_count < self.n-1:
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
        print(f'Węzeł: {edge_count}: ({a}, {b})  |  Koszt: {min}')
        edge_count += 1
        min_cost += min
        mst[b] = mst[a] = True
  
    print(f'Minimalny koszt: {min_cost}')