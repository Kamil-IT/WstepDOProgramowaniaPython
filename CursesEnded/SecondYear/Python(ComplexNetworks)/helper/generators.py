import networkx as nx

G_full = nx.complete_graph(20)
G_binary_tree = nx.binomial_tree(5)
G_powerlaw_cluster = nx.generators.random_graphs.powerlaw_cluster_graph(10, 5, 1)
G_grid = nx.grid_graph([5, 3])
G_single_grid = nx.grid_graph([2, 6])

# nx.draw(G_full)
# nx.draw(G_binary_tree)
nx.draw(G_powerlaw_cluster)


# plt.show()


def count_and_show_basic_characteristics(graph):
    print(f'Is grpah connected: {nx.is_connected(graph)}')


count_and_show_basic_characteristics(G_full)
count_and_show_basic_characteristics(G_binary_tree)
count_and_show_basic_characteristics(G_powerlaw_cluster)
count_and_show_basic_characteristics(G_grid)
count_and_show_basic_characteristics(G_single_grid)
