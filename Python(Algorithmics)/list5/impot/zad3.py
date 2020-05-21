from Graph import Graph


g = Graph( Graph.random(5, 0, 15, False, False) )  # generate a random graph [nodes=5, [min_weight=0, [max_weight=5, [directed=True, [loops=True]]]]]
print(f'\n{g}')

print('\nAlgorytm Kruskala:')
g.kruskal()

print('\nAlgorytm Prima:')
g.prim()