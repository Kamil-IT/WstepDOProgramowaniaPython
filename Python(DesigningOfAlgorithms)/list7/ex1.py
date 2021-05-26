import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def root_to_dictionary(self):
        return {str(self.val): self.to_dictionary()}

    def to_dictionary(self):
        if self.left is None and self.right is None:
            return {}
            # return f'[{self.val}: []]'
        elif self.left is None:
            return {str(self.right.val): self.right.to_dictionary()}
            # return f'[{str(self.val)}: self.right.to_dictionary()]'
        elif self.right is None:
            return {str(self.left.val): self.left.to_dictionary()}
            # return f'[{str(self.val)}: self.left.to_dictionary()]'
        return {str(self.left.val): self.left.to_dictionary(), str(self.right.val): self.right.to_dictionary()}
        # return f'[{str(self.val)}: [{self.left.to_dictionary()},{self.right.to_dictionary()}]]'


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def add_edges(root, g):
    if root.left is not None:
        g.add_edge(str(root.val), str(root.left.val))
        add_edges(root.left, g)
    if root.right is not None:
        g.add_edge(str(root.val), str(root.right.val))
        add_edges(root.right, g)


def is_bst(root, elements):
    elements = sorted(elements)
    root_element_bst = elements[len(elements) // 2]
    good_bst_tree = Node(root_element_bst)
    for i in elements:
        good_bst_tree = insert(good_bst_tree, i)
    if good_bst_tree.to_dictionary() == root.to_dictionary():
        return True
    return False


def divide_and_conquer_search(list, val):
    id_0 = 0
    id_n = len(list) - 1

    while id_0 <= id_n:
        midval = (id_0 + id_n) // 2
        if list[midval] == val:
            return midval
        if val > list[midval]:
            id_0 = midval + 1
        else:
            id_n = midval - 1

    if id_0 > id_n:
        return None


def correct_bst(root, elements):
    if is_bst(root, elements):
        return root
    else:
        l = elements
        divide_and_conquer_search(l, max(l))
        r = Node(l[len(l) // 2])
        l.remove(l[len(l) // 2])
        for i in l:
            insert(r, i)
        return r


l = [30, 20, 40, 50, 70, 60, 80]
divide_and_conquer_search(l, max(l))
r = Node(l[len(l) // 2])
l.remove(l[len(l) // 2])
for i in l:
    insert(r, i)

G = nx.Graph()

add_edges(r, G)
pos = graphviz_layout(G, prog='dot')

nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)

nx.draw(G, pos)
plt.show()
