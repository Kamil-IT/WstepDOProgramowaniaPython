from queue import Queue


# Binary tree
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


# Breadth-first search
def traverse_queue(top, visit):
    if top is None:
        return
    Q = Queue()
    Q.put(top)
    while not Q.empty():
        node = Q.get()
        visit(node)
        if node.left:
            Q.put(node.left)
        if node.right:
            Q.put(node.right)


# Pre-order traversal
def traverse_stack(top, visit):
    if top is None:
        return
    stack = list()
    stack.append(top)
    while stack:
        node = stack.pop()
        visit(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Converting leaf(from binary tree) to root
def leaf_to_root(top, leaf_n):
    if top is None:
        return
    Q = Queue()
    Q.put(top)
    while not Q.empty():
        node = Q.get()
        if node.left.data == leaf_n:
            return node.left
        if node.right.data == leaf_n:
            return node.right
        if node.left:
            Q.put(node.left)
        if node.right:
            Q.put(node.right)


# Creating binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# ex. 1.1
print('ex. 1.1')
traverse_queue(root, print)

# ex. 1.2
print('ex. 1.2')
traverse_stack(root, print)

# ex. 2.1
print('ex. 2.1')
leaf_as_root = leaf_to_root(root, 2)
# Printing new tree
traverse_queue(leaf_as_root, print)
