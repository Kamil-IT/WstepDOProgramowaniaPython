

def add_node(graph, node):
    """Wstawia wierzchołek do grafu."""
    if node not in graph:
        graph[node] = []


def add_edge_undirected(graph, edge):
    """Dodaje krawędź do grafu nieskierowanego."""
    source, target = edge
    add_node(graph, source)
    add_node(graph, target)
    # Możemy wykluczyć pętle.
    if source == target:
        raise ValueError("pętle są zabronione")
    if target not in graph[source]:
        graph[source].append(target)
    if source not in graph[target]:
        graph[target].append(source)


def list_nodes(graph):
    """Zwraca listę wierzchołków grafu."""
    return graph.keys()


def list_edges(graph):
    """Zwraca listę krawędzi (2-krotek) grafu skierowanego bez wag."""
    L = []
    for source in graph:
        for target in graph[source]:
            L.append((source, target))
    return L


def print_graph(graph):
    """Wypisuje postać grafu skierowanego bez wag na ekranie."""
    for source in graph:
        print(source, ":", end=' ')
        for target in graph[source]:
            print(target, end=' ')
        print()


graph = {"A": ["B", "F", "C"], "B": ["C", "D"], "C": ["D", "B", "A"], "D": ["C"], "E": ["C"], "F": []}
undirected_graph = {}


print_graph(graph)

add_edge_undirected(graph, {"asd": []})

print_graph(graph)




print(list_edges(graph))
