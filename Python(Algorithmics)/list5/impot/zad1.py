from Graph import Graph


g = Graph([
  [0,1,1,0,0,0],
  [1,0,0,0,0,0],
  [1,0,0,0,0,0],
  [0,0,0,0,1,1],
  [0,0,0,1,0,0],
  [0,0,0,1,0,0],
])
# g = Graph( Graph.random(5, 0, 15, False, False) )  # generate a random graph [nodes=5, [min_weight=0, [max_weight=5, [directed=True, [loops=True]]]]]
print(f'\n{g}')

g.connected_components()